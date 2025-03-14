---
title: 스프링 WebFlux의 DispatcherHandler와 요청 처리 흐름
linkTitle: "DispatcherHandler"
description: 스프링 WebFlux는 프론트 컨트롤러 패턴을 사용하며, DispatcherHandler가 중앙 WebHandler로서 요청을 다른 컴포넌트에 위임한다. DispatcherHandler는 스프링 설정에 따라 다양한 워크플로우를 지원하고, ApplicationContextAware 인터페이스를 구현해 실행 중인 컨텍스트에 접근할 수 있다.
url : /egovframe-runtime/presentation-layer/web-reactive/web-reactive-dispatcherhandler/
menu:
    depth:
        name: DispatcherHandler
        weight: 2
        parent: "web_reactive"
---
# DispatcherHandler


## 설명

스프링 WebFlux도 스프링 MVC와 유사한 프론트 컨트롤러 패턴을 사용한다. 중앙 WebHandler가 받은 요청을 다른 컴포넌트에 위임하는데 DispatcherHandler가 바로 이 중앙 WebHandler다. 이 모델 덕분에 다양한 워크플로우를 지원할 수 있다.
DispatcherHandler는 스프링 설정에 따라 그에 맞는 컴포넌트로 위임한다. DispatcherHandler도 스프링 빈이며 ApplicationContextAware 인터페이스를 구현했기 때문에 실행중인 컨텍스트에 접근할 수 있다. DispatcherHandler 빈을 WebHandler 이름으로 정의하면 WebHttpHandlerBuilder가 감지하고 WebHandler API에서 설명했던 체인에 추가한다.

WebFlux 애플리케이션에서 사용하는 일반적인 스프링 설정은 다음과 같다.

- webHandler 이름의 DispatcherHandler 빈
- WebFilter, WebExceptionHandler 빈
- 그 외 DispatcherHandler가 사용하는 빈
- 기타 등등

WebExceptionHandler가 체인을 만들 때 아래와 같이 사용한다.
```java
ApplicationContext context = ...
HttpHandler handler = WebHttpHandlerBuilder.applicationContext(context).build();
```

### Special Bean Types
DispatcherHandler는 요청을 처리하고 그에 맞는 응답을 만들 때 사용하는 특별한 빈이 있다. __특별한__ 빈이란 WebFlux 프레임워크가 동작하는데 필요하며 스프링이 관리하는 Object 인스턴스를 말한다. 이 빈들은 기본적으로 내장돼 있지만 프로퍼티를 수정해서 확장하거나 커스텀 빈으로 대체할 수도 있다.

DispatcherHandler는 다음과 같은 빈을 감지한다. 저수준에서 동작하는 다른 빈도 자동으로 추가될 수 있다는 점에 주의하라

| Bean type             | Explanation                                                                                                                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HandlerMapping        | 요청을 핸들러에 매핑한다. 매핑 기준은 HandlerMapping 구현체마다 다른다(어노테이션을 선언한 컨트롤러, URL 패턴 매칭 등)</br>주로 쓰는 구현체는 @RequestMapping을 선언한 메소드를 찾는 RequestMappingHandlerMapping, 함수형 엔드포인트를 라이팅하는 RouterFunctionMapping, URL 패스 패턴으로 WebHandler를 찾는 SimpleUrlHandlerMapping 등이 있다.     |
| HandlerAdapter        | 핸들러가 실제로 호출되는 방식에 관계없이 요청에 매핑된 핸들러를 호출할 수 있도록 DispatcherHandler를 지원한다.</br>예를 들어 어노테이션이 있는 컨트롤러를 호출하려면 어노테이션을 해결해야 한다.</br>HandlerAdapter의 주요 목적은 이러한 세부 사항으로부터 DispatcherHandler를 보호하는 것이다.                                                          |
| HandlerResultHandler	 | 핸들러 호출의 결과를 처리하고 응답을 종료한다. Result Handling을 참고하라.                                                                                                                                                                                                                                                  |

### WebFlux Config

애플리케이션은 요청을 처리하는 데 필요한 인프라 빈(웹 핸들러 API 및 DispatcherHandler)을 선언할 수 있다. 그러나 대부분의 경우 WebFlux Config로 시작하는게 좋다. 이 구성은 필요한 빈을 선언하고 이를 사용자 정의할 수 있는 상위 수준의 구성 콜백 API를 제공한다.

```
스프링 부트를 사용해도 이 WebFlux Config로 초기화하며 부트가 제공하는 옵션으로 좀 더 편리하게 설정을 관리할 수 있다.
```

### Processing
DispatcherHandler는 다음과 같이 요청을 처리한다.
- HandlerMapping에서 매칭되는 핸들러를 찾는다. 첫번째로 매칭된 핸들러를 사용한다.
- 핸들러를 찾으면 적당한 HandlerAdapter를 사용해 핸들러를 실행하고 HandlerResult를 돌려 받는다.
- HandlerResult를 적절한 HandlerResultHandler로 넘겨 바로 응답을 만들거나 뷰를 랜더링하고 처리를 완료한다.

### Result Handling
핸들러 호출의 반환 값은 HandlerAdapter를 통해 몇 가지 추가 컨텍스트와 함께 HandlerResult로 래핑되어 지원을 요청하는 첫 번째 HandlerResultHandler로 전달된다. 아래 표는 사용 가능한 HandlerResultHandler 구현을 보여 주며, 모두 WebFlux 구성에 선언되어 있다.:

|Result Handler Type	| Return Values | Default Order |
|-----------------------|---------------|---------------|
|ResponseEntityResultHandler	| ResponseEntity, 보통은 @Controller에서 사용	| 0 |
|ServerResponseResultHandler	| ServerResponse, 보통은 Functional Endpoints에서 사용	| 0 |
|ResponseBodyResultHandler	| @ResponseBody, @RestController에서 리턴한 값을 처리	| 100 |
|ViewResolutionResultHandler	| CharSequence, View, Model, Map, Rendering이나 다른 Object를 model attribute로 처리	| Integer.MAX_VALUE |

### Exceptions

HandlerAdapter가 리턴한 HandlerResult는 핸들러마다 다른 에러 처리 함수에 넘겨진다. 이 함수는 아래와 같을 때 호출된다.
- 핸들러 실행에 실패한 경우(예를 들어 @Controller)
- HandlerResultHandler가 핸들러가 리턴한 값을 처리하는데 실패한 경우

핸들러가 리턴한 리액티브 타입이 데이터를 produce 하기 전에 에러를 알아차릴 수 있으면 이 함수로 응답을 변경할 수 있다.(예를 들어 status로)
이로 인해 @Controller 클래스의 특정 메소드에 @ExceptionHandler를 선언할 수 있다. 스프링 MVC에선 HandlerExceptionResolver가 이 역할을 담당한다.
여기서 중요한 것은 MVC가 아니지만 WebFlux 핸들러를 선택하기 전 발생한 Exception은 @ControllerAdvice로 처리할 수 없다.

#### View Resolution
뷰 해상도를 사용하면 특정 뷰 기술에 종속되지 않고 HTML 템플릿과 모델을 사용하여 브라우저에 렌더링할 수 있다.
WebFlux에서 뷰 해상도는 ViewResolver 인스턴스를 사용하여 String을 View 인스턴스에 매핑하는 전용 HandlerResultHandler를 통해 지원된다. 그런 다음 뷰를 사용하여 응답을 렌더링한다.

##### Handling
ViewResolutionResultHandler로 전달된 HandlerResult에는 핸들러의 반환 값과 요청 처리 중에 추가된 속성이 포함된 모델이 포함된다. 반환 값은 다음 중 하나로 처리된다.
- 문자열, 문자 시퀀스: 구성된 뷰리졸버 구현 목록을 통해 뷰로 확인할 논리적 뷰 이름이다.
- void: 요청 패스에 맞는 디폴트 뷰 이름에서 앞뒤 슬래쉬를 제거하고 뷰로 리졸브한다. 뷰 이름이 제공되지 않거나(예를 들어 model attribute를 리턴한 경우) 비동기 값일 때도(예를 들어 Mono가 비어 있을 때) 동일하게 처리한다.
- 렌더링: 뷰 해상도 시나리오를 위한 API입니다. 코드 완성 기능이 있는 IDE에서 옵션을 확인해라.
- Model, Map: 요청에 대해 모델에 추가할 model attributes
- 기타: 다른 모든 반환 값(BeanUtils#isSimpleProperty가 true를 리턴하는 값은 제외)은 모델에 추가할 model attribute로 간주된다. @ModelAttribute 어노테이션이 없으면 conventions와 클래스명으로 속성 이름을 결정한다.

모델에는 비동기 리액티브 타입도 있을 수 있다(예를 들어 리액터나 RxJava가 리턴한 값). 이런 model attribute는 AbstractView가 랜더링하기 전에 실제값으로 바꿔준다.
single-value 리액티브 타입은 비어있지 않다면 값 하나로 리졸브되고 multi-value 리액티브 타입(에를 들어 Flux<T>)은 List<T>로 수집된다.

뷰 리졸브는 스프링 설정에 ViewResolutionResultHandler만 추가하면된다. WebFlux Config는 뷰 리졸브를 위한 설정 API를 제공한다.

##### Redirecting
리액티브는 뷰 이름에 redirect: 프리픽스를 붙이기만 하면 된다. UrlBasedViewResolver(히위 클래스도 포함)가 이를 리다이렉트 요청으로 판단한다.
프리픽스를 제외한 나머지 뷰 이름은 리다이렉트 URL로 사용한다. 동작 자체는 컨트롤러가 RedirectView나 Rendering.redirectTo(“abc”).build()를 리턴했을 때와 동일하지만, 이 방법은 컨트롤러가 직접 뷰 이름을 보고 처리한다.
redirect:/some/resource 같은 값은 현재 애플리케이션에서 이동할 페이지를 찾고 redirect:https://example.com/arbitrary/path 같이 사용하면 해당 URL로 리다이렉트한다.

##### Content Negotiation
content negotiation은 ViewResolutionResultHandler가 담당한다. 요청 미디어 타입과 View가 지원하는 미디어 타입을 비교해서 첫번째로 찾은 View를 사용한다.
스프링 WebFlux는 HttpMessageWriter로 Json, XML 같은 미디어 타입을 만드는 HttpMessageWriterView를 지원한다. 보통은 WebFlux 설정을 통해 HttpMessageWriterView를 디폴트 뷰로 사용한다. 디폴트 뷰는 요청 미디어 타입과 일치하기만 하면 항상 사용되는 뷰다.

## 참고자료
- [The Spring Framework - Web Reactive - DispatcherHandler](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/web-reactive.html#webflux-dispatcher-handler)