---
title: 스프링 WebFlux의 WebClient와 논블로킹 처리
linkTitle: "WebClient"
description: 스프링 WebFlux는 리액티브, 논블로킹 HTTP 요청을 위한 WebClient를 제공하며, 이를 통해 선언적인 프로그래밍이 가능하다. WebClient와 서버는 동일한 논블로킹 코덱을 사용해 요청과 응답을 인코딩 및 디코딩한다.
url : /egovframe-runtime/presentation-layer/web-reactive/web-reactive-webclient/
menu:
    depth:
        name: WebClient
        weight: 5
        parent: "web_reactive"
---
# WebClient
스프링 WebFlux는 리액티브, 논블로킹 HTTP 요청을 위한 WebClient를 제공한다. 웹 클라이언트는 리액티브 타입을 사용하는 함수형 API이기 때문에 선언적인(declarative) 프로그래밍이 가능하다. 웹플럭스 클라이언트와 서버는 동일한 논블로킹 코덱으로 요청, 응답을 인코딩, 디코딩한다.

## 설명
WebClient는 요청을 수행하기 위해 HTTP 클라이언트 라이브러리에 처리를 위임하며 아래와 같은 기능을 기본으로 제공한다.

- Reactor Netty
- Jetty Reactive HttpClient
- Apache HttpComponents
- Others can be plugged via ClientHttpConnector.

### Configuration
WebClient는 가장 간단하게는 스태틱 팩토리 메소드로 만들 수 있다.

- WebClient.create()
- WebClient.create(String baseUrl)

위 메소드는 디폴트 세팅으로 Reactor Netty HttpClient를 사용하므로 클래스패스에 io.projectreactor.netty:reactor-netty가 있어야 한다.

다른 옵션을 사용하려면 WebClient.builder()를 사용한다.

- uriBuilderFactory: base URL을 커스텀한 UriBuilderFactory
- defaultHeader: 모든 요청에 사용할 헤더
- defaultCookie: 모든 요청에 사용할 쿠키
- defaultRequest: 모든 요청을 커스텀할 Consumer
- filter: 모든 요청에 사용할 클라이언트 필터
- exchangeStrategies: HTTP 메시지 reader/writer 커스텀
- clientConnector: HTTP 클라이언트 라이브러리 설정

다음 예제는 HTTP 코덱을 설정한다.
```java
WebClient client = WebClient.builder()
    .codecs(configurer -> ... )
    .build();
```
WebClient는 한 번 빌드하고 나면 상태를 변경할 수 없다. 단 다음 예제와 같이 원본 인스턴스는 그대로 두고 복사해와서 설정을 추가할 수 있다.
```java
WebClient client1 = WebClient.builder()
.filter(filterA).filter(filterB).build();

WebClient client2 = client1.mutate()
.filter(filterC).filter(filterD).build();

// client1 has filterA, filterB

// client2 has filterA, filterB, filterC, filterD
```

### MaxInMemorySize
스프링 WebFlux는 애플리케이션 메모리 이슈를 방지하기 위해 코덱의 메모리 버퍼 사이즈를 제한한다. 디폴트는 256KB로 설정되어 있는데 버퍼가 부족하면 다음과 같은 에러가 보인다.
```java
org.springframework.core.io.buffer.DataBufferLimitException: Exceeded limit on max bytes to buffer
```
다음 코드를 사용하면 모든 디폴트 코덱의 최대 버퍼 사이즈를 조절할 수 있다.
```java
WebClient webClient = WebClient.builder()
    .codecs(configurer -> configurer.defaultCodecs().maxInMemorySize(2 * 1024 * 1024))
    .build();
```

### Reactor Netty
HttpClient는 Reactor Netty 설정을 커스텀할 수 있는 간단한 설정 프리셋을 가지고 있다.
```java
HttpClient httpClient = HttpClient.create().secure(sslSpec -> ...);

WebClient webClient = WebClient.builder()
    .clientConnector(new ReactorClientHttpConnector(httpClient))
    .build();
```

#### Resources
기본적으로 HttpClient는 reactor.netty.http.HttpResources에 묶여 있는 Reactor Netty의 글로벌 리소스를 사용한다. 이는 이벤트 루프 쓰레드와 커넥션 풀도 포함한다.</br>
이벤트 루프로 동시성을 제어하려면 공유 리소스를 고정해 놓고 사용하는게 좋기 때문이다. 이 모드에서는 프로세스가 종료될 때까지 공유 자원을 active 상태로 유지한다.</br>
서버가 프로세스와 함께 중단된다면 명시적으로 리소스를 종료시킬 필요는 없다. 하지만 프로세스 내에서 서버를 시작하거나 중단할 수 있다면(예를 들어 WAR로 배포한 스프링 MVC 애플리케이션) 다음 예제처럼 스프링이 관리하는 ReactorResourceFactory 빈을 globalResources=true롤 선언해야 스프링 ApplicationContext를 닫을 때 Reactor Netty 글러벌 리소스도 종료한다.
```java
@Bean
public ReactorResourceFactory reactorResourceFactory() {
return new ReactorResourceFactory();
}
```
원한다면 글로벌 Reactor Netty 리소스를 사용하지 않게 만들수도 있다. 하지만 아래 예제처럼 직접 모든 Reactor Netty 클라이언트와 서버 인스턴스가 공유 자원을 사용하게 만들어야 한다.
```java
@Bean
public ReactorResourceFactory resourceFactory() {
    ReactorResourceFactory factory = new ReactorResourceFactory();
    factory.setUseGlobalResources(false);
    return factory;
}

@Bean
public WebClient webClient() {

    Function<HttpClient, HttpClient> mapper = client -> {
        // Further customizations...
    };
 
    ClientHttpConnector connector =
            new ReactorClientHttpConnector(resourceFactory(), mapper);
 
    return WebClient.builder().clientConnector(connector).build();
}
```

#### Timeouts
다음은 커넥션 타임아웃을 설정하는 코드다.
```java
import io.netty.channel.ChannelOption;

HttpClient httpClient = HttpClient.create()
    .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 10000);

WebClient webClient = WebClient.builder()
    .clientConnector(new ReactorClientHttpConnector(httpClient))
    .build();
```
다음은 read/write 타임아웃을 설정하는 코드다.
```java
import io.netty.handler.timeout.ReadTimeoutHandler;
import io.netty.handler.timeout.WriteTimeoutHandler;

HttpClient httpClient = HttpClient.create()
    .doOnConnected(conn -> conn
        .addHandlerLast(new ReadTimeoutHandler(10))
        .addHandlerLast(new WriteTimeoutHandler(10)));

// Create WebClient...
```
다음은 모든 요청에 대한 타임아웃을 설정하는 코드다.
```java
HttpClient httpClient = HttpClient.create()
    .responseTimeout(Duration.ofSeconds(2));

// Create WebClient...
```
다음은 특정 요청에 타임아웃을 설정하는 코드다.
```java
WebClient.create().get()
    .uri("https://example.org/path")
    .httpRequest(httpRequest -> {
        HttpClientRequest reactorRequest = httpRequest.getNativeRequest();
        reactorRequest.responseTimeout(Duration.ofSeconds(2));
    })
    .retrieve()
    .bodyToMono(String.class);
```

### Jetty
다음은 Jetty HttpClient 설정을 커스텀하는 예제이다.
```java
HttpClient httpClient = new HttpClient();
httpClient.setCookieStore(...);

WebClient webClient = WebClient.builder()
    .clientConnector(new JettyClientHttpConnector(httpClient))
    .build();
```
HttpClient는 전용 리소스(Executor. ByteBufferPool, Scheduler)를 생성해서 기본적으로 프로세스가 종료되거나 stop()을 호출할 때까지 유지한다.

다음 예제처럼 스프링이 관리하는 JettyResourceFactory 빈을 정의하면 여러 Jetty 클라이언트(혹은 서버) 인스턴스에서 리소스를 공유할 수 있고 스프링 ApplicationContext를 닫을 때 리소스도 종료시킬 수 있다.
```java
@Bean
public JettyResourceFactory resourceFactory() {
    return new JettyResourceFactory();
}

@Bean
public WebClient webClient() {

    HttpClient httpClient = new HttpClient();
    // Further customizations...
 
    ClientHttpConnector connector =
            new JettyClientHttpConnector(httpClient, resourceFactory());
 
    return WebClient.builder().clientConnector(connector).build();
}
```

### HttpComponents
다음은 Apache HttpComponents HttpClient 설정을 커스텀하는 예제이다.
```java
HttpAsyncClientBuilder clientBuilder = HttpAsyncClients.custom();
clientBuilder.setDefaultRequestConfig(...);
CloseableHttpAsyncClient client = clientBuilder.build();
ClientHttpConnector connector = new HttpComponentsClientHttpConnector(client);

WebClient webClient = WebClient.builder().clientConnector(connector).build();
```

## retrieve()
retrieve()는 response body를 받아 디코딩하는 간단한 메소드이다. 사용방법은 아래와 같다.
```java
WebClient client = WebClient.create("https://example.org");

Mono<ResponseEntity<Person>> result = client.get()
    .uri("/persons/{id}", id).accept(MediaType.APPLICATION_JSON)
    .retrieve()
    .toEntity(Person.class);
```
혹은 body만 받아올 수 있다.
```java
WebClient client = WebClient.create("https://example.org");

Mono<Person> result = client.get()
    .uri("/persons/{id}", id).accept(MediaType.APPLICATION_JSON)
    .retrieve()
    .bodyToMono(Person.class);
```
다음 예제처럼 응답을 객체 스트림으로도 디코딩할 수 있다.
```java
Flux<Quote> result = client.get()
    .uri("/quotes").accept(MediaType.TEXT_EVENT_STREAM)
    .retrieve()
    .bodyToFlux(Quote.class);
```
4xx 또는 5xx 응답코드를 받으면 디폴트는 WebClientResponseException 또는 각 HTTP 상태에 해당하는 WebClientResponseException.BadRequest, WebClientResponseException.NotFound 등의 하위 exception을 던진다. 다음 예제처럼 onStatus 메소드로 상태별 exception을 커스텀할 수 있다.
```java
Mono<Person> result = client.get()
    .uri("/persons/{id}", id).accept(MediaType.APPLICATION_JSON)
    .retrieve()
    .onStatus(HttpStatus::is4xxClientError, response -> ...)
    .onStatus(HttpStatus::is5xxServerError, response -> ...)
    .bodyToMono(Person.class);
```

## Exchange
exchangeToMono() 및 exchangeToFlux() 메서드(또는 Kotlin의 awaitExchange {} 및 exchangeToFlow {})는 응답 상태에 따라 응답을 다르게 디코딩하는 등 더 많은 제어가 필요한 곳에 유용하다.
```java
Mono<Person> entityMono = client.get()
    .uri("/persons/1")
    .accept(MediaType.APPLICATION_JSON)
    .exchangeToMono(response -> {
        if (response.statusCode().equals(HttpStatus.OK)) {
            return response.bodyToMono(Person.class);
        }
        else {
            // Turn to error
            return response.createException().flatMap(Mono::error);
        }
    });
```
위의 방법을 사용할 때는 반환된 Mono 또는 Flux가 완료된 후 응답 본문을 확인하고 소비되지 않은 경우 메모리 및 연결 누수를 방지하기 위해 해제한다. 따라서 응답은 더 이상 다운스트림에서 디코딩할 수 없다. 필요한 경우 응답을 디코딩하는 방법을 선언하는 것은 제공된 함수에 달려 있다.

## Request Body
request body는 Mono, 코틀린 코루틴 Deferred 등 ReactiveAdapterRegistry에 등록된 모든 비동기 타입으로 인코딩할 수 있다.
```java
Mono<Person> personMono = ... ;

Mono<Void> result = client.post()
    .uri("/persons/{id}", id)
    .contentType(MediaType.APPLICATION_JSON)
    .body(personMono, Person.class)
    .retrieve()
    .bodyToMono(Void.class);
```
다음 예제처럼 객체 스트림으로도 인코딩할 수 있다.
```java
Flux<Person> personFlux = ... ;

Mono<Void> result = client.post()
    .uri("/persons/{id}", id)
    .contentType(MediaType.APPLICATION_STREAM_JSON)
    .body(personFlux, Person.class)
    .retrieve()
    .bodyToMono(Void.class);
```
비동기 타입이 아닌 실제 값을 가지고 있다면 bodyValue를 사용한다.
```java
Person person = ... ;

Mono<Void> result = client.post()
    .uri("/persons/{id}", id)
    .contentType(MediaType.APPLICATION_JSON)
    .bodyValue(person)
    .retrieve()
    .bodyToMono(Void.class);
```
### Form Data
form 데이터를 보내려면 MultiValueMap<String, String>을 body로 사용해야 한다. 이 때는 FormHttpMessageWriter가 자동으로 content-type을 application/x-www-form-urlencoded로 설정한다. 다음은 MultiValueMap<String, String>을 사용하는 예제이다.
```java
MultiValueMap<String, String> formData = ... ;

Mono<Void> result = client.post()
    .uri("/path", id)
    .bodyValue(formData)
    .retrieve()
    .bodyToMono(Void.class);
```
BodyInserters를 사용하면 인라인으로 form 데이터를 만들 수 있다.
```java
import static org.springframework.web.reactive.function.BodyInserters.*;

Mono<Void> result = client.post()
    .uri("/path", id)
    .body(fromFormData("k1", "v1").with("k2", "v2"))
    .retrieve()
    .bodyToMono(Void.class);
```
### Multipart Data
multipart 데이터를 보낼 때는 MultiValueMap<String, ?>을 사용해서 각 value에 part 컨텐츠를 나타내는 Object 인스턴스나 part의 컨텐츠와 헤더를 나타내는 HttpEntity를 담아야 한다. MultipartBodyBuilder를 사용하면 편리하다.
```java
MultipartBodyBuilder builder = new MultipartBodyBuilder();
builder.part("fieldPart", "fieldValue");
builder.part("filePart1", new FileSystemResource("...logo.png"));
builder.part("jsonPart", new Person("Jason"));
builder.part("myPart", part); // Part from a server request

MultiValueMap<String, HttpEntity<?>> parts = builder.build();
```
일반적으로는 part별로 content-type을 명시하지 않아도 된다. Content Type은 직렬화할때 쓰는 HttpMessageWriter나 Resource의 경우 파일 확장자에 따라 자동으로 결정한다. 필요하다면 빌더 part 메소드 중 MediaType을 받는 메소드를 사용하면 된다.
MultiValueMap을 만들었다면 가장 간단하게는 다음 예제처럼 body 메소드로 WebClient에 넘길 수 있다.
```java
MultipartBodyBuilder builder = ...;

Mono<Void> result = client.post()
    .uri("/path", id)
    .body(builder.build())
    .retrieve()
    .bodyToMono(Void.class);
```
MultiValueMap에 전형적인 form 데이터(application/x-www-form-urlencoded) 등 String이 아닌 갓이 하나라도 들어있으면 content-type을 multipart/form-data로 설정하지 않아도 된다.
MultipartBodyBuilder를 사용하면 항상 HttpEntity로 감싸주면 된다. MultipartBodyBuilder 대신 BodyInserters를 사용하면 인라인으로 multipart 컨텐츠를 만들 수 있다.
```java
import static org.springframework.web.reactive.function.BodyInserters.*;

Mono<Void> result = client.post()
    .uri("/path", id)
    .body(fromMultipartData("fieldPart", "value").with("filePart", resource))
    .retrieve()
    .bodyToMono(Void.class);
```
### Filter
다음 예제와 같이 WebClient.Builder를 통해 클라이언트 필터(ExchangeFilterFunction)를 등록하여 요청을 가로채고 수정할 수 있다.
```java
WebClient client = WebClient.builder()
.filter((request, next) -> {

            ClientRequest filtered = ClientRequest.from(request)
                    .header("foo", "bar")
                    .build();
 
            return next.exchange(filtered);
        })
        .build();
```
필터는 인증과 같은 교차 문제에 사용할 수 있다. 다음 예제에서는 정적 팩토리 메서드를 통한 기본 인증에 필터를 사용한다.
```java
import static org.springframework.web.reactive.function.client.ExchangeFilterFunctions.basicAuthentication;

WebClient client = WebClient.builder()
    .filter(basicAuthentication("user", "password"))
    .build();
```
필터는 기존 웹클라이언트 인스턴스를 변경하여 추가하거나 제거할 수 있으므로 원래 웹클라이언트에 영향을 주지 않는 새 웹클라이언트 인스턴스를 생성할 수 있다.
```java
import static org.springframework.web.reactive.function.client.ExchangeFilterFunctions.basicAuthentication;

WebClient client = webClient.mutate()
    .filters(filterList -> {
        filterList.add(0, basicAuthentication("user", "password"));
    })
    .build();
```
WebClient는 일련의 필터 체인을 둘러싸고 있는 얇은 외피에 ExchangeFunction이 뒤따른다. 요청을 하고 상위 수준 객체와 인코딩하기 위한 워크플로우를 제공하며 응답 콘텐츠가 항상 소비되도록 하는 데 도움이 된다.</br>
필터가 어떤 방식으로든 응답을 처리할 때는 항상 콘텐츠를 소비하거나 웹클라이언트로 다운스트림으로 전파하여 동일한 콘텐츠를 보장할 수 있도록 각별한 주의를 기울여야 한다.</br>
다음 예제는 미승인 상태 코드를 처리하지만 예상 여부에 관계없이 모든 응답 콘텐츠가 공개되도록 하는 필터다.
```java
public ExchangeFilterFunction renewTokenFilter() {
    return (request, next) -> next.exchange(request).flatMap(response -> {
        if (response.statusCode().value() == HttpStatus.UNAUTHORIZED.value()) {
            return response.releaseBody()
                .then(renewToken())
                .flatMap(token -> {
                    ClientRequest newRequest = ClientRequest.from(request).build();
                    return next.exchange(newRequest);
                });
        } else {
            return Mono.just(response);
        }
    });
}
```

### Attributes
요청에 속성을 추가할 수 있다. 이 기능은 필터 체인을 통해 정보를 전달하고 특정 요청에 대한 필터의 동작에 영향을 주고자 할 때 편리하다.
```java
WebClient client = WebClient.builder()
    .filter((request, next) -> {
        Optional<Object> usr = request.attribute("myAttribute");
        // ...
    })
    .build();

client.get().uri("https://example.org/")
        .attribute("myAttribute", "...")
        .retrieve()
        .bodyToMono(Void.class);

    }
```
모든 요청에 속성을 삽입할 수 있는 WebClient.Builder 수준에서 전역적으로 defaultRequest 콜백을 구성할 수 있으며, 이는 예를 들어 Spring MVC 애플리케이션에서 ThreadLocal 데이터를 기반으로 요청 속성을 채우는 데 사용될 수 있다.

### Context
속성은 필터 체인에 정보를 전달하는 편리한 방법을 제공하지만 현재 요청에만 영향을 준다. 중첩된 추가 요청에 전파되는 정보를 전달하려면(예를 들어 flatMap을 통해), 또는 이후에 실행되는 요청에 전파되는 정보를 전달하려면(예를 들어 concatMap을 통해) Reactor Context를 사용해야 한다.

다음 예제는 리액터 컨텍스트를 리액티브 체인의 끝에 채워 모든 작업에 적용하는 것을 보여준다.
```java
WebClient client = WebClient.builder()
    .filter((request, next) ->
        Mono.deferContextual(contextView -> {
            String value = contextView.get("foo");
            // ...
    }))
    .build();

client.get().uri("https://example.org/")
    .retrieve()
    .bodyToMono(String.class)
    .flatMap(body -> {
        // perform nested request (context propagates automatically)...
    })
    .contextWrite(context -> context.put("foo", ...));
```

### Synchronous Use
WebClient는 마지막에 결과를 블로킹하면 동기(synchronous)로 결과를 가져온다.
```java
Person person = client.get().uri("/person/{id}", i).retrieve()
    .bodyToMono(Person.class)
    .block();

List<Person> persons = client.get().uri("/persons").retrieve()
    .bodyToFlux(Person.class)
    .collectList()
    .block();
```
하지만 API를 여러번 호출하면 각 응답을 따로 블로킹하기보다는 전체 결과를 합쳐서 기다리는게 더 효율적이다.
```java
Mono<Person> personMono = client.get().uri("/person/{id}", personId)
    .retrieve().bodyToMono(Person.class);

Mono<List<Hobby>> hobbiesMono = client.get().uri("/person/{id}/hobbies", personId)
    .retrieve().bodyToFlux(Hobby.class).collectList();

Map<String, Object> data = Mono.zip(personMono, hobbiesMono, (person, hobbies) -> {
        Map<String, String> map = new LinkedHashMap<>();
        map.put("person", person);
        map.put("hobbies", hobbies);
        return map;
    })
    .block();
```
위 코드는 단지 한 가지 예시일 뿐이다. 요청이 끝날때까지 블로킹 하지 않고 리액티브 파이프라인을 구축해서 상호독립적으로 원격 호출을 여러번 실행하는 다른 패턴과 연산자도 많다.
```
스프링 MVC나 WebFlux 컨트롤러에서 Flux나 Mono를 사용한다면 블로킹할 필요가 없다. 단순히 컨트롤러 메소드에서 리액티브 타입을 리턴하기만 하면 된다. 코틀린 코루틴과 스프링 WebFlux에서도 마찬가지다. 컨트롤러 메소드에서 suspend 함수를 사용하거라 Flow를 리턴하면 된다.
```
참고자료
- [TThe Spring Framework - Web Reactive - WebClient](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/web-reactive.html#webflux-client)