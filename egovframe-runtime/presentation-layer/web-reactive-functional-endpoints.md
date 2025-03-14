---
title: 스프링 WebFlux 함수형 프로그래밍 모델(WebFlux.fn)
linkTitle: "Functional Endpoints"
description: 스프링 WebFlux의 함수형 모델인 WebFlux.fn은 요청을 함수로 라우팅하고 처리하며, HandlerFunction이 HTTP 요청을 처리해 비동기 응답을 반환한다. RouterFunction은 요청을 해당 HandlerFunction에 매핑하며, 이는 어노테이션 모델의 @RequestMapping과 같은 역할을 수행하지만 데이터와 행동을 함께 제공하는 점이 다르다.
url : /egovframe-runtime/presentation-layer/web-reactive/web-reactive-functional-endpoints/
menu:
    depth:
        name: Functional Endpoints
        weight: 4
        parent: "web_reactive"
---
# Functional Endpoints
스프링 WebFlux는 경량화 된 함수형 프로그래밍 모델을 지원한다. WebFlux.fn이라고 하는 이 모델은 함수로 요청을 라우팅하고 핸들링하기 때문에 불변성(immutability)을 보장한다.
함수형 모델과 어노테이션 모델 중 하나를 선택하면 되는데 둘 다 리액티브 코어를 기반으로 한다.

## 설명
WebFlux.fn에선 HandlerFunction이 HTTP 요청을 처리한다. HandlerFunction은 ServerRequest를 받아 비동기 ServerResponse(예를 들어 Mono<ServerResponse>)를 리턴하는 함수다. 요청, 응답 객체 모두 불변하기 때문에 JDK 8 방식으로 HTTP 요청, 응답에 접근할 수 있다. HandlerFunction 역할은 어노테이션 프로그래밍 모델로 치면 @RequestMapping 메소드와 동일하다.

요청은 RouterFunction이 핸들러 펑션에 라우팅한다. RouterFunction은 ServerRequest를 받아 비동기 HandlerFunction(예를 들어 Mono<HandlerFunction>)을 리턴하는 함수다. 매칭되는 라이터 펑션이 있으면 핸들러 펑션을 리턴하고 그 외는 비어 있는 Mono를 리턴한다. RouterFunction이 하는 일은 @RequestMapping 어노테이션과 동일하지만 라우터 펑션은 테이터뿐 아니라 행동까지 제공한다는 점이 다르다.

라이터를 만들 때는 아래 예제처럼 RouterFunctions.route()가 제공하는 빌더를 사용할 수 있다.
```java
import static org.springframework.http.MediaType.APPLICATION_JSON;
import static org.springframework.web.reactive.function.server.RequestPredicates.*;
import static org.springframework.web.reactive.function.server.RouterFunctions.route;

PersonRepository repository = ...
PersonHandler handler = new PersonHandler(repository);

RouterFunction<ServerResponse> route = route()
.GET("/person/{id}", accept(APPLICATION_JSON), handler::getPerson)
.GET("/person", accept(APPLICATION_JSON), handler::listPeople)
.POST("/person", handler::createPerson)
.build();

public class PersonHandler {
// ...

    public Mono<ServerResponse> listPeople(ServerRequest request) {
        // ...
    }
 
    public Mono<ServerResponse> createPerson(ServerRequest request) {
        // ...
    }
 
    public Mono<ServerResponse> getPerson(ServerRequest request) {
        // ...
    }
}
```
RouterFunction을 실행하는 방법 중 하나는 HttpHandler로 변환해 내장된 서버 어댑터에 등록하는 것이다.
- RouterFunctions.toHttpHandler(RouterFunction)
- RouterFunctions.toHttpHandler(RouterFunction, HandlerStrategies)

### HandlerFunction
ServerRequest와 ServerResponse는 JDK 8 방식으로 HTTP 요청과 응답에 접근할 수 있는 불변(immutable) 인터페이스이다. 모든 요청, 응답 body 모두 리액티브 스트림 back pressure로 처리한다. request body는 리액터 Flux나 Mono로 표현한다.
response body는 Flux와 Mono를 포함한 어떤 리액티브 스트림 Publisher든 상관없다.

#### ServerRequest
ServerRequest로 HTTP 메소드, URI, 헤더, 쿼리 파라미터에 접근할 수 있으며, body를 추출할 수 있는 메소드를 제공한다.
다음은 request body를 Mono<String>으로 추출하는 예제다.
```java
Mono<String> string = request.bodyToMono(String.class);
```
다음 예제는 body를 Flux<Person>으로 추출한다. Person 객체는 JSON이나 XML 같은 직렬화된 데이터로 디코딩한다.
```java
Flux<Person> people = request.bodyToFlux(Person.class);
```
위 예제에서 사용한 메소드는 함수형 인터페이스 BodyExtractor를 받는 ServerRequest.body(BodyExtractor) 메소드의 축약 버전이다. BodyExtractors 유틸리티 클래스에 있는 인터페이스를 활용해도 된다. 예를 들면 앞의 예제는 아래와 같이 작성할 수도 있다.
```java
Mono<String> string = request.body(BodyExtractors.toMono(String.class));
Flux<Person> people = request.body(BodyExtractors.toFlux(Person.class));
```
아래 예제는 form 데이터에 접근하는 방법을 보여준다.
```java
Mono<MultiValueMap<String, String>> map = request.formData();
```
다음은 multipart 데이터를 map으로 가져오는 예제이다.
```java
Mono<MultiValueMap<String, Part>> map = request.multipartData();
```
다음은 multipart 데이터를 스트리밍 방식으로 한번에 하나씩 가져온다.
```java
Flux<Part> parts = request.body(BodyExtractors.toParts());
```
#### ServerResponse
HTTP 응답은 ServerResponse로 접근할 수 있으며 이 인터페이션은 불변이기 때문에 build 메소드로 생성한다. 빌더로 헤더를 추가하거나 상태코드, body를 설정할 수 있다. 다음은 JSON 컨텐츠로 200(OK) 응답을 만드는 예제이다.
```java
Mono<Person> person = ...
ServerResponse.ok().contentType(MediaType.APPLICATION_JSON).body(person, Person.class);
```
다음 예제는 boby 없이 Location 헤더만 201(CREATED) 응답을 만든다.
```java
URI location = ...
ServerResponse.created(location).build();
```
hint 파라미터를 넘기면 사용하는 코덱에 따라 body 직렬화/역직렬화 방식을 커스텀 할 수 있다. 아래 예제처럼 Jackson JSON View를 지정할 수 있다.
```java
ServerResponse.ok().hint(Jackson2CodecSupport.JSON_VIEW_HINT, MyJacksonView.class).body(...);
```
#### Handler Classes
핸들러 평션은 다음처럼 람다로 만들 수 있다.
```java
HandlerFunction<ServerResponse> helloWorld =
request -> ServerResponse.ok().bodyValue("Hello World");
```
편리한 방식이긴 하지만 펑션을 여러 개 사용해야 한다면 인라인 람다로 만들기는 부담스럽다. 이럴 때는 핸들러 클래스로 관련 핸들러 펑션을 묶을 수 있다.
핸들러 클래스는 어노테이션 기반 애플리케이션의 @Controller와 비슷하다. 다음 예제는 리액티브 Person 레퍼지토리와 관련된 요청을 처리한다.
```java
import static org.springframework.http.MediaType.APPLICATION_JSON;
import static org.springframework.web.reactive.function.server.ServerResponse.ok;

public class PersonHandler {
private final PersonRepository repository;

    public PersonHandler(PersonRepository repository) {
        this.repository = repository;
    }
 
    public Mono<ServerResponse> listPeople(ServerRequest request) {
        Flux<Person> people = repository.allPeople();
        return ok().contentType(APPLICATION_JSON).body(people, Person.class);
    }
 
    public Mono<ServerResponse> createPerson(ServerRequest request) {
        Mono<Person> person = request.bodyToMono(Person.class);
        return ok().build(repository.savePerson(person));
    }
 
    public Mono<ServerResponse> getPerson(ServerRequest request) {
        int personId = Integer.valueOf(request.pathVariable("id"));
        return repository.getPerson(personId)
            .flatMap(person -> ok().contentType(APPLICATION_JSON).bodyValue(person))
            .switchIfEmpty(ServerResponse.notFound().build());
    }
}
```
#### Validation
함수형 프로그래밍 모델은 스프링 validation facilities를 사용해서 request body를 검증할 수 있다. 다음 예제는 Person에 대한 커스텀 스프링 Validator 구현체를 보여주고 있다.
```java
public class PersonHandler {
private final Validator validator = new PersonValidator();

    // ...
 
    public Mono<ServerResponse> createPerson(ServerRequest request) {
        Mono<Person> person = request.bodyToMono(Person.class).doOnNext(this::validate);
        return ok().build(repository.savePerson(person));
    }
 
    private void validate(Person person) {
        Errors errors = new BeanPropertyBindingResult(person, "person");
        validator.validate(person, errors);
        if (errors.hasErrors()) {
            throw new ServerWebInputException(errors.toString());
        }
    }
}
```

### RouterFunction
라우터 펑션은 요청을 그에 맞는 HandlerFunction으로 라우팅한다. 라우팅 펑션을 직접 만들기보단, 보통 RouterFunctions 유틸리티 클래스를 사용한다.
RouterFunctions.route()가 리턴하는 빌더를 사용하거나 RouterFunctions.route(RequestPredicate, HandlerFunction)으로 직접 라우터를 만들 수 있다.
route() 빌더를 사용하면 static 메소드를 직접 임포트하지 않아도 된다. 예를 들어 GET 요청을 매핑할 수 있는 GET(String, HandlerFunction) 메소드와 POST 요청을 매핑하는 POST(String, HandlerFunction) 메소드가 있다.
빌더는 HTTP 메소드 외에 다른 조건으로 요청을 매핑할 수는 인터페이스도 제공한다. 각 HTTP 메소드는 RequestPredicate 파라미터를 받은 메소드를 오버로딩하고 있기 때문에 다른 조건을 추가할 수 있다.

#### Predicates
RequestPredicate를 직접 만들어도 되지만 요청 path, HTTP 메소드, 컨텐츠 타입 등 자주 사용하는 구현체는 RequestPredicates 유틸리티 클래스에 준비되어 있다. 다음은 유틸리티 클래스로 Accept 헤더 조건을 추가하는 예제이다.
```java
RouterFunction<ServerResponse> route = RouterFunctions.route()
.GET("/hello-world", accept(MediaType.TEXT_PLAIN),
request -> ServerResponse.ok().bodyValue("Hello World")).build();
```
여러 조건을 함께 사용할 수 있다.
- RequestPredicate.and(RequestPredicate) - 둘 다 만족해야 한다.
- RequestPredicate.or(RequestPredicate) - 둘 중 하나만 만족하면 된다.
RequestPredicates가 제공하는 구현체도 이 조합으로 만든 것이 많다.
예를 들어 RequestPredicates.GET(String)은 RequestPredicates.method(HttpMethod)와 RequestPredicates.path(String) 조합이다. 위에 있는 예제도 빌더 내부에서 RequestPredicates.GET과 accept를 조합한 것이다.

#### Routes
라우터 평션은 정해진 순서대로 실행한다. 첫번째 조건과 일치하지 않으면 두번째를 실행하는 식이다.
따라서 구체적인 조건을 앞에 선언해야 한다. 어노테이션 프로그래밍 모델에선 자동으로 가장 구체적인 컨트롤러 메소드를 실행하지만 함수형 모델에서는 그렇지 않다는 점을 유의해야 한다.
build()를 호출하면 빌더에 정의한 모든 라우터 펑션을 RouterFunction 한 개로 합친다. 다음 방법으로도 여러 라우터 펑션을 조합할 수 있다.

- RouterFunctions.route() 빌더의 add(RouterFunction)
- RouterFunction.and(RouterFunction)
- RouterFunction.andRoute(RequestPredicate, HandlerFunction) - RouterFunctions.route()를 RouterFunction.and()로 감싸고 있는 축약 버전
다음 예제는 라우터 펑션 4개를 사용한다.
```java
import static org.springframework.http.MediaType.APPLICATION_JSON;
import static org.springframework.web.reactive.function.server.RequestPredicates.*;

PersonRepository repository = ...
PersonHandler handler = new PersonHandler(repository);

RouterFunction<ServerResponse> otherRoute = ...

RouterFunction<ServerResponse> route = route()
.GET("/person/{id}", accept(APPLICATION_JSON), handler::getPerson)
.GET("/person", accept(APPLICATION_JSON), handler::listPeople)
.POST("/person", handler::createPerson)
.add(otherRoute)
.build();
```

#### Nested Routes
path가 같으면 대부분 같은 조건으로 사용하므로 라우터 평션을 그룹핑하는 경우가 많다. 앞의 예제는 라우터 펑션 세 개가 /person을 path 조건으로 사용했다.
어노테이션을 사용했다면 클래스 레벨이 @RequestMapping을 선언해 중복 코드를 줄일 수 있다. WebFlux.fn에선 path 메소드로 path 조건을 공유한다. 예를 들어 위 코드는 아래 예제처럼 라우터 펑션을 한번 감싸 개선할 수 있다.
```java
RouterFunction<ServerResponse> route = route()
.path("/person", builder -> builder
.GET("/{id}", accept(APPLICATION_JSON), handler::getPerson)
.GET(accept(APPLICATION_JSON), handler::listPeople)
.POST(handler::createPerson))
.build();
```
path가 가장 흔하기 하지만 빌더의 nest 메소드는 다른 조건도 감쌀 수 있다. 위 코드는 여전히 Accpet 헤더가 중복이다 nest 메소드를 함께 사용하면 코드를 한층 더 개선할 수 있다.
```java
RouterFunction<ServerResponse> route = route()
.path("/person", b1 -> b1
.nest(accept(APPLICATION_JSON), b2 -> b2
.GET("/{id}", handler::getPerson)
.GET(handler::listPeople))
.POST(handler::createPerson))
.build();
```
#### Running a Server
HTTP 서버에선 어떻게 라우터 펑션을 실행할까? 간단하게는 다음과 같이 라우터 펑션을 HttpHandler로 변환할 수 있다.
- RouterFunctions.toHttpHandler(RouterFunction)
- RouterFunctions.toHttpHandler(RouterFunction, HandlerStrategies)
리턴 받은 HttpHandler를 서버 가이드에 따라 서버 어댑터와 함께 사용하면 된다.

스프링 부트에서도 사용하는 좀 더 일반적인 옵션은 WebFlux Config로 컴포넌트를 스프링 빈으로 정의하고 DispatcherHandler와 함께 실행하는 것이다.
프레임워크는 다음과 같은 컴포넌트로 함수형 엔드포인트를 지원하는데 웹플럭스 설정을 사용하면 이를 모두 스프링 빈으로 정의한다.
- RouterFunctionMapping: 스프링 설정에서 RouterFunction<?>을 찾아 RouterFunction.andOther로 연결하고 최종 구성한 RouterFunction으로 요청을 라우팅한다.
- HandlerFunctionAdapter: 요청에 매핑된 HandlerFunction을 DispatcherHandler가 실행하게 도와주는 간단한 어댑터
- ServerResponseResultHandler: ServerResponse의 writeTo 메소드로 HandlerFunction 결과를 처리한다.
위 컴포넌트가 함수형 엔드포인트를 DispatcherHandler의 요청 처리 패턴에 맞춰주기 때문에 어노테이션 컨트롤러와 함께 사용할 수도 있다. 스프링 부트 웹플럭스 스타터도 이 방법으로 함수형 엔드포인트를 지원한다.

#### Filtering Handler Functions
핸들러 펑션에 필터를 적용할 땐 라우터 빌더의 before, after, filter 메소드를 사용한다.
이 기능을 어노테이션 모델로 구현하면 @ControllerAdvice나 ServletFilter를 사용했을 것이다. 필터는 빌더의 모든 라우터 펑션에 적용된다.
이 말은 필터를 감싸져 있는 라우터에서 정의하면 상위 레벨에는 적용되지 않는다는 뜻이다.
```java
RouterFunction<ServerResponse> route = route()
    .path("/person", b1 -> b1
        .nest(accept(APPLICATION_JSON), b2 -> b2
            .GET("/{id}", handler::getPerson)
            .GET(handler::listPeople)
            .before(request -> ServerRequest.from(request)
                .header("X-RequestHeader", "Value")
                .build()))
        .POST(handler::createPerson))
    .after((request, response) -> logResponse(response))
    .build();
```
라우터 빌더의 필터 메서드는 서버 요청과 핸들러 함수를 받아 서버 응답을 반환하는 함수인 핸들러 필터 함수를 받는다. 핸들러 함수 매개변수는 체인의 다음 요소를 나타낸다. 일반적으로 라우팅되는 핸들러이지만 여러 개의 필터가 적용되는 경우 다른 필터가 될 수도 있다.
이제 path를 보고 요청을 허가할지 말지를 결정하는 SecurityManager가 있다고 가정하고 간단한 보안 필터를 라우터에 적용해 보자.
```java
SecurityManager securityManager = ...

RouterFunction<ServerResponse> route = route()
    .path("/person", b1 -> b1
        .nest(accept(APPLICATION_JSON), b2 -> b2
            .GET("/{id}", handler::getPerson)
            .GET(handler::listPeople))
        .POST(handler::createPerson))
    .filter((request, next) -> {
        if (securityManager.allowAccessTo(request.path())) {
            return next.handle(request);
        }
        else {
            return ServerResponse.status(UNAUTHORIZED).build();
        }
    })
    .build();
```
위 예제를 보면 next.handle(ServerRequest) 호출은 선택이라는 점을 알 수 있다. 여기선 접근을 허가할 때만 실행했다.
빌더의 filter 메소드 대신 RouterFunction.filter(HandlerFilterFunction)로 필터를 추가하는 방법도 있다.
```
함수형 엔드포인트에서 CORS는 CorsWebFilter로 지원한다.
```
## 참고자료
- [The Spring Framework - Web Reactive - Functional Endpoints](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/web-reactive.html#webflux-fn)