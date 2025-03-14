---
linkTitle: "Reactive Core"
title: Reactive Core
description: 스프링-웹 모듈은 서버 요청 처리를 위한 HttpHandler와 WebHandler API를 제공하며, 클라이언트 사이드에서는 논블로킹 I/O와 리액티브 스트림 기반의 WebClient가 지원된다. 또한, 서버와 클라이언트 모두 HTTP 요청 및 응답 콘텐츠의 직렬화와 역직렬화를 위한 코덱 기능을 포함하고 있다.
url : /egovframe-runtime/presentation-layer/web-reactive/web-reactive-reactive-core/
menu:
    depth:
        name: Reactive Core
        weight: 1
        parent: "web_reactive"
---
# Reactive Core

## 설명

스프링-웹 모듈에는 반응형 웹 애플리케이션을 위한 다음과 같은 기본 지원이 포함되어 있다.

- 서버 요청 처리에는 두 가지 수준을 지원한다.
  - HttpHandler: 논블로킹 I/O 및 리액티브 스트림 Back Pressure을 사용하는 HTTP 요청을 처리하며, Reactor Netty, Undertow, Tomcat, Jetty 및 모든 Servlet 3.1+ 컨테이너용 어댑터와 함께 사용한다.
  - WebHandler API: 요청 처리를 위한 약간 더 높은 수준의 범용 웹 API로, 주석이 달린 컨트롤러 및 기능적 엔드포인트와 같은 구체적인 프로그래밍 모델로 작성되어 있다.
- 클라이언트 사이드에서는 논블로킹 I/O 및 리액티브 스트림 Back Pressure으로 HTTP 요청을 수행하는 기본 ClientHttpConnector 계약과 함께 Reactor Netty, 리액티브 Jetty HttpClient 및 Apache HttpComponents용 어댑터가 있다. 애플리케이션에 사용되는 상위 수준의 WebClient는 이를 기반으로 구축된다.
- 클라이언트와 서버 모두 코덱으로 HTTP 요청 및 응답 콘텐츠의 직렬화 및 역직렬화를 한다.

### HttpHandler
HttpHandler는 요청과 응답을 처리하는 메소드를 하나만 가지고 있다. 의도적으로 최소한의 기능을 제공하며, 주된 목적은 다양한 HTTP 서버 API에 대한 최소한의 추상화이다.
지원하는 서버의 API는 아래 표와 같다.

| 서버 이름           | 사용하는 Servlet API                                                 | 리액티브 스트림 지원                                          |
|---------------------|----------------------------------------------------------------------|---------------------------------------------------------------|
| Netty               | Netty API                                                            | Reactor Netty                                                 |
| Undertow            | Undertow API API                                                     | spring-web: Undertow to 리액티브 스트림 브릿지                |
| Tomcat              | 서블릿 3.1 논블로킹 I/O; ByteBuffers로 byte[]를 읽고 쓰는 Tomcat API | spring-web: 서블릿 3.1 논블로킹 I/O to 리액티브 스트림 브릿지 |
| Jetty               | 서블릿 3.1 논블로킹 I/O; ByteBuffers로 byte[]를 읽고 쓰는 Jetty API  | spring-web: 서블릿 3.1 논블로킹 I/O to 리액티브 스트림 브릿지 |
| 서블릿 3.1 컨테이너 | 서블릿 3.1 논블로킹 I/O                                              | spring-web: 서블릿 3.1 논블로킹 I/O to 리액티브 스트림 브릿지 |

서버 Dependency는 아래 표와 같다(지원 버전 참고)

|   서버 이름   |         Group ID        |        Artifact Name        |
|-------------|-----------------------|---------------------------|
| Reactor Netty | io.projectreactor.netty | reactor-netty               |
| Undertow      | io.undertow             | undertow-core               |
| Tomcat        | org.apache.tomcat.embed | tomcat-embed-core           |
| Jetty         | org.eclipse.jetty       | jetty-server, jetty-servlet |

다음은 각 서버의 API 어댑터를 활용하는 HttpHandler이다.

#### 리액터 Netty
```java
HttpHandler handler = ...
ReactorHttpHandlerAdapter adapter = new ReactorHttpHandlerAdapter(handler);
HttpServer.create().host(host).port(port).handle(adapter).bind().block();
```

#### Undertow
```java
HttpHandler handler = ...
UndertowHttpHandlerAdapter adapter = new UndertowHttpHandlerAdapter(handler);
Undertow server = Undertow.builder().addHttpListener(port, host).setHandler(adapter).build();
server.start();
```

#### Tomcat
```java
HttpHandler handler = ...
Servlet servlet = new TomcatHttpHandlerAdapter(handler);

Tomcat server = new Tomcat();
File base = new File(System.getProperty("java.io.tmpdir"));
Context rootContext = server.addContext("", base.getAbsolutePath());
Tomcat.addServlet(rootContext, "main", servlet);
rootContext.addServletMappingDecoded("/", "main");
server.setHost(host);
server.setPort(port);
server.start();
```

#### Jetty
```java
HttpHandler handler = ...
Servlet servlet = new JettyHttpHandlerAdapter(handler);

Server server = new Server();
ServletContextHandler contextHandler = new ServletContextHandler(server, "");
contextHandler.addServlet(new ServletHolder(servlet), "/");
contextHandler.start();

ServerConnector connector = new ServerConnector(server);
connector.setHost(host);
connector.setPort(port);
server.addConnector(connector);
server.start();
```

#### 서블릿 3.1+ 컨테이너
서블릿 3.1+ 컨테이너에 WAR를 배포하려면 WAR에 AbstractReactiveWebInitializer를 확장하여 추가하면 된다. 이 클래스는 HttpHandler, ServletHttpHandlerAdapter를 감싸고 있으며, 이 핸들러를 서블릿으로 등록한다.

### WebHandler API
org.springframework.web.server 패키지를 보면 HttpHandler가 WebHandler와 여러 WebExceptionHandler, WebFilter로 체인을 형성해 요청을 처리하는 범용 웹 API를 제공한다.
WebHttpHandlerBuilder에 컴포넌트를 등록하거나 스프링 ApplicationContext 위치만 알려주면 자동으로 컴포넌트 체인에 추가한다.
HttpHandler는 서로 다른 HTTP 서버를 쓰기 위한 추상화가 전부인 반면, WebHandler API는 아래와 같이 웹 애플리케이션에서 흔히 쓰는 광범위한 기능을 제공한다.
- User session과 Session attributes
- Request attributes.
- Locale, Principal 리졸브
- form 데이터 파싱, 캐싱 조회
- multipart 데이터 추상화
- 기타 등등

#### Form Data
ServerWebExchange는 form 데이터에 접근할 수 있는 메소드를 제공한다.
```
Mono<MultiValueMap<String, String>> getFormData();
```
DefaultServerWebExchange는 설정에 있는 HttpMessageReader를 사용해 form 데이터를 MultiValueMap으로 파싱한다. 디폴트로 사용하는 리더는 ServerCodecConfigurer 빈에 있는 FormHttpMessageReader이다.

#### Multipart Data
ServerWebExchange는 multipart 데이터에 접근할 수 있는 메소드를 제공한다.
```
Mono<MultiValueMap<String, Part>> getMultipartData();
```
DefaultServerWebExchange는 설정에 있는 HttpMessageReader<MultiValueMap<String, Part»를 사용해 multipart/form-data 컨텐츠를 MultiValueMap으로 파싱한다. 현재로써는 Synchronoss NIO Multipart가 유일하게 지원하는 서브파티 라이브러리이며, 논블로킹으로 multipart 요청을 파싱하는 유일한 라이브러리이다. ServerCodecConfigurer 빈으로 활성화할 수 있다.
스트리밍 방식으로 multipart 데이터를 파싱하려면 HttpMessageReader<Part>가 리턴하는 Flux<Part>를 사용한다. 예를 들어 컨트롤러에서 @RequestPart를 선언하면 Map처럼 이름으로 각 파트에 접근하겠다는 뜻이므로 multipart 데이터를 한번에 파싱해야 한다. 반대로 Flux<Part> 타입에 @RequestPart를 사용허면 컨텐츠를 디코딩할 때 MultiValueMap에 수집하지 않는다.

#### Forwarded Headers
Load Balancers와 같이 프톡시를 경유한 요청은 호스트, 포트, URL 스킴이 변경될 수 있어서 클라이언트 입장에서는 원래의 URL 정보를 알아내기 어렵다.
RFC 7239 정의에 따르면 Forwarded HTTP 헤더는 프록시가 원래 요청에 대한 정보를 추가하는 헤더이다. X-Forwarded-Host, X-Forwarded-Port, X-Forwarded-Proto, X-Forwarded-Ssl, and X-Forwarded-Prefix 같은 비표준 헤더도 존재한다.
ForwardedHeaderTransformer는 forwarded 헤더를 보고 요청의 호스트, 포트, 스킴을 바꿔준 다음, 헤더를 제거하는 컴포넌트이다. ForwardedHeaderTransformer라는 이름으로 빈을 정의하면 자동으로 체인에 추가된다.
forwarded 헤더는 보안에 신경써야 할 요소가 있는데 프록시가 헤더를 추가한건지, 클라이언트가 악의적으로 추가한 것인지 애플리케이션에서는 알 수 없기 때문이다.
따라서 외부에서 들어오는 신뢰할 수 없는 프록시 요청을 제거할 때 ForwardedHeaderTransformer를 removeOnly=true로 설정하여 헤더 정보를 사용하지 않고 제거할 수 있다.
```
5.1 버전부터 ForwardedHeaderFilter는 제거대상(deprecated)이 되어 ForwardedHeaderTransformer를 대신한다. 따라서 exchange(http 요청/응답과 세션 정보 등의 컨테이너)를 만들기 전에 forwarded 헤더를 처리할 수 있다. 필터를 사용하더라도 이 필터는 전체 필터 리스트에서 제외되며 그 대신 ForwardedHeaderTransformer를 사용한다.
```

### Filters
WebHandler API에서는 WebFilter를 사용하면 다른 필터 체인과 WebHandler 전후에 요청을 가로채서 원하는 로직을 넣을 수 있다. WebFilter를 등록하려면 스프링 빈으로 만들어 빈 위에 @Order를 선언아거나 Ordered를 구현해 순서를 정해도 되고, WebFlux Config를 사용해도 된다.

#### CORS
CORS는 컨트롤러에 어노테이션을 선언하는 것으로 잘 동작한다. Spring Security와 사용하면 CorsFilter를 사용해서 Spring Security 필터 체인보다 먼저 처리하도록 해야 한다.

### Exceptions
WebHandler API에서는 WebFilter 체인과 WebHandler에서 발생한 예외를 WebExceptionHandler로 처리한다. WebExceptionHandler를 등록하려면 스프링 빈으로 빈 위에 @Order를 선언하거나 Ordered를 구현해 순서를 정해도 되고, WebFlux Config를 사용해도 된다.
아래 표는 바로 사용할 수 있는 WebExceptionHandler 구현체이다.

| Exception Handler | Description                                                                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ResponseStatusExceptionHandler        | Http status code를 지정할 수 있는 ResponseStatusException을 처리한다.                                                                                                         |
| WebFluxResponseStatusExceptionHandler | ResponseStatusExceptionHandler를 확장하는 것으로 다른 exception 타입도 @ResponseStatus를 선언해서 HTTP status code를 정할 수 있다.</br>이 핸들러는 WebFlux Config 안에 선언되어 있다.  |


## 참고자료

- [The Spring Framework - Web Reactive - Reactive Core](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/web-reactive.html#webflux-reactive-spring-web)