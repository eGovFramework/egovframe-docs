---
title: SockJS Fallback Options
linkTitle: "SockJS"
description: Spring은 WebSocket이 지원되지 않는 환경에서 SockJS 프로토콜을 사용해 WebSocket API를 에뮬레이션하는 fallback 옵션을 제공한다.
url : /egovframe-runtime/presentation-layer/webSocket/websocket-sockjs/
menu:
    depth:
        name: SockJS
        weight: 2
        parent: "WebSocket"
---
# SockJS Fallback Options

[http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-fallback](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-fallback)

WebSocket 이 아직까지 모든 브라우저에서 지원되지 않거나 네트워크 프락시 제약등으로 사용할 수 없는 경우가 있다. 이에 Spring 은 fallback 옵션을 제공하는데 이는 SockJS protocol 에 기반으로 WebSocket API 를 emulate 한다.

## 1. SockJS 개요

SockJS 는 application 으로 하여금 WebSocket API 를 사용하는데 있다. 만약 WebSocket 사용이 불가한 경우에도 이를 fallback option 으로 제공하여 어떠한 코드 변화없이 WebSocket API 를 사용토록 한다.

### SockJS 구성

- [SockJS protocol](https://github.com/sockjs/sockjs-protocol)
- [SockJS client](https://github.com/sockjs/sockjs-client) - javascript library
- SockJS 서버 구현 - spring-websocket 모듈을 통해 제공

SockJS 는 여러가지 테크닉을 이용하여 다양한 브라우저 및 브라우저 버전을 지원한다. 전송 타입은 다음의 3가지로 분류된다.
**WebSocket, HTTP Streaming, HTTP Long Polling**. 이들 각각을 살펴보려면 여기 를 참조한다.

SockJS client 는 서버의 기본 정보를 얻기 위해서 “GET /info” 를 호출한다. 그 이후에 SockJS 는 어떤 전송 타입을 사용할지를 결정한다. WebSocket 은 최우선책이며, 이후로 HTTP Streaming > HTTP (long) polling 이 사용된다.

모든 전송 요청은 다음의 URL 구조를 갖는다.

`http://host:port/myApp/myEndpoint/{server-id}/{session-id}/{transport}`

- {server-id} - 클러스터에서 요청을 routing 하는데 사용하나 이외에는 의미가 없다.
- {session-id} - SockJS session 에 소속하는 HTTP 요청과 연관성이 있다.
- {transport} - 전송타입 ex> websocket, xhr-streaming, 기타 등등

WebSocket 전송은 WebSocket handshaking 을 위한 오직 하나의 HTTP 요청을 필요로 한다. 모든 메시지들은 그 이후에 사용했던 socket 을 통해 교환된다.

HTTP 전송은 좀 더 많은 요청을 필요로 한다. 예를 들어 Ajax/XHR streaming 은 server 에서 client 로의 메시지를 위해 하나의 long-running 요청이 있고 추가적인 HTTP POST 요청은 client 에서 server 로의 메시지를 위해 사용된다. Long polling 은 server 가 client 로의 응답 후에 현재의 요청을 끝내는 것을 제외하고는 XHR streaming 과 유사하다.

SockJS 는 최소한의 message framing 을 추가한다. 예를 들어 server 는 “o” (open frame) 를 초기에 전송하고, 메시지는 `[“message1”,”message2”]` 와 같은 JSON-encoded 배열로서 전달되며, 문자 “h” (hearbeat frame) 는 기본적으로 25초간 메시지 흐름이 없는 경우에 전송하고 “c” (close frame) 는 해당 세션을 종료한다.

이에 대한 자세한 이해는 브라우저에서 확인할 수 있다. SockJS 는 debug flag 를 제공하고, 전송타입을 고정하여 각각에 대해서 살펴볼 수 있다. 서버는 “org.springframework.web.socket” 에 TRACE 로깅을 활성화 하여 로그를 볼 수 있다.

## 2. SockJS 활성화

SockJS 는 설정을 통해 쉽게 활성화 할 수 있다.

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(myHandler(), "/myHandler").withSockJS();
    }
 
    @Bean
    public WebSocketHandler myHandler() {
        return new MyHandler();
    }
 
}
```
```xml
<beans xmlns="http://www.springframework.org/schema/beans" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:websocket="http://www.springframework.org/schema/websocket" 
    xsi:schemaLocation=" 
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/websocket
        http://www.springframework.org/schema/websocket/spring-websocket-4.0.xsd">
 
    <websocket:handlers>
        <websocket:mapping path="/myHandler" handler="myHandler"/>
        <websocket:sockjs/>
    </websocket:handlers>
 
    <bean id="myHandler" class="org.springframework.samples.MyHandler"/>
 
</beans>
```

위의 설정은 Spring MVC 에서 사용하기 위한 것으로 DispatcherServlet 설정에 포함되어져야 한다. (application context 를 계층적으로 가져갈 경우) 그러나 Spring WebSocket 이 SpringMVC 이외에도 사용할 수 있도록 제공되듯, SockJS 도 그러하다. 이는 [SockJsHttpRequestHandler](http://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/web/socket/sockjs/support/SockJsHttpRequestHandler.html) 를 통해서 제공된다.

browser (클라이언트) 측에서는 W3C WebSocket API 를 emulate 하는 [sockjs-client](https://github.com/sockjs/sockjs-client) 를 사용할 수 있다. 이를 통해 서버와 통신하여 최적의 전송타입을 선택한다. 이 외에도 포함할 전송타입을 지정하는 몇가지 설정을 제공한다.

## 3. IE 8, 9 에서의 HTTP Streaming (Ajax/XHR vs IFrame)

IE 8/9 는 대중적으로 사용되고 있다. 이것은 SockJS 가 필요한 핵심적인 이유이다.

SockJS 는 Ajax/XHR Streaming 을 Microsoft 의 [XDomainRequest](http://blogs.msdn.com/b/ieinternals/archive/2010/05/13/xdomainrequest-restrictions-limitations-and-workarounds.aspx) 를 통해 지원하고 있다. 이것은 서로 다른 도메인 간에도 동작하지만 cookie 전송을 지원하지 않는다. Cookie 는 Java Application 에서 매우 필수적이다. 그러나 SockJS 클라이언트는 Java 만을 위한 것이 아닌 많은 서버 타입을 위해 사용되도록 고안되었기 때문에 Cookie 를 중요하게 다룰지 여부를 알려주어야 한다. SockJS 클라이언트는 Ajax/XHR Streaming 을 선택하거나 그렇지 않다면 iframe 기반의 technique 을 사용한다.

SockJS 클라이언트로 부터의 최초 요청인 '/info' 는 클라이언트의 전송 타입 선택을 위한 정보를 위한 요청이다. 상세한 내용 중 하나는 서버 application 이 cookie 에 의존 (authentication 목적이나 session clustering with stick mode 등) 하는지 여부이다. Spring 의 SockJS 지원은 sessionCookieNeeded 라는 속성을 포함한다. 이것은 Java application 이 JSESSIONID cookie 에 의존하기 때문에 기본적으로 활성화 된다. 만약 이 기능을 OFF 한다면 비로서 SockJS 클라이언트는 xdr-streaming 을 IE 8/9 에서 사용토록 선택되어 진다.

iframe 기반의 전송을 사용한다면 browser 가 HTTP 응답헤더인 X-Frame-Option 이 DENY, SAMEORIGIN, ALLOW-FROM `<origin>` 로 설정됨에 따라 iframe 사용을 블락시킬수 있음을 염두에 두어야 한다. 이러한 헤더는 clickjacking 이라 알려진 공격을 방어하기 위한 목적으로 주로 사용된다.

Spring Security 3.2+ 에서 X-Frame-Options 헤더를 모든 응답에 설정하도록 지원하고 있다. 즉 Spring Security Java Config 에서 이 값을 DENY 로 기본설정한다. Spring Security XML 설정에서는 이 헤더를 설정하지 않지만 차후에 기본값으로 설정될 여지가 있다.

Spring Security 의 Section 7.1. Default Security Headers 에서 X-Frame-Options 헤더 설정에 대한 상세 문서를 살펴볼 수 있다. 이에 대한 추가적인 배경을 보고자 한다면 [SEC-2501](https://jira.spring.io/browse/SEC-2501) 을 살펴본다.

X-Frame-Option 응답헤더를 추가한다면 (Spring Security 를 사용한다면 그렇게 된다.) 헤더 값을 SAMEORIGIN 이나 ALLOW-FROM `<origin>` 으로 설정할 필요가 있다. 이와 더불어 Spring SockJS 지원은 SockJS 클라이언트의 location 을 알아야 할 필요가 있다. 왜냐하면 client 가 iframe 상에서 로드될 것이기 때문이다. 기본적으로 iframe 은 SockJS 클라이언트 (sockJS.js) 를 CDN location 으로부터 다운되도록 설정되어 있다. 이를 same origin 으로 설정하는 것이 필요하다.

Java Config 에서 아래와 같이 설정할 수 있다. XML 에서는 `<websocket:sockjs>` 에서 설정한다.

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/portfolio").withSockJS()
                .setClientLibraryUrl("http://localhost:8080/myapp/js/sockjs-client.js");
    }
 
    // ...
 
}
```

초기 개발중에는 SockJS client devel mode 를 활성화 하라. 이는 SockJS request (iframe 같은) 를 브라우저가 캐시하는 것을 방지한다. 이에 대한 방법은 [SockJS client](https://github.com/sockjs/sockjs-client) page 에서 확인할 수 있다.

## 4. Heartbeat Messages

SockJS 프로토콜은 server 가 hearbeat message 를 전송하도록 하여 proxies 가 connection 을 hung 으로 인식하지 못하도록 할 필요가 있다. Spring SockJS 설정은 heartbeatTime 속성을 가지는데 빈도를 조정하는데 사용된다. 기본값은 해당 커넥션에 어떤 메시지도 없는 25초를 사용한다. 이 25초는 [IETF 권고안](http://tools.ietf.org/html/rfc6202) 을 따르고 있다.

STOMP over WebSocket/SockJS 를 사용할 때 만약 STOMP 클라이언트와 서버가 heartbeat 교환에 합의한다면 SockJS heartbeat 은 비활성화 된다.

Spring SockJS 지원은 heartbeat 작업을 스케줄링하기 위해 TaskScheduler 를 설정하도록 하고 있다. TaskScheduler 는 이용가능한 processor 의 수에 따른 기본값으로 설정된 thread pool 로부터 가져오는데 이는 특정한 요구에 적합한 값을 설정하는 것을 고려해야 한다.

## 5. Servlet 3 Async Requests

HTTP streaming 과 HTTP long polling SockJS 전송은 커넥션을 보통의 경우보다 오래 open 되도록 한다. 이것에 대한 개요는 [다음](https://spring.io/blog/2012/05/08/spring-mvc-3-2-preview-techniques-for-real-time-updates/) 에서 확인한다.

Servlet Container 에서 이것은 Servlet 3 async 지원을 통해 수행되는데 이것은 요청을 처리중인 Servlet 스레드를 빠져나오고 다른 Servlet 스레드에서 응답을 기록하도록 한다.

Servlet API 가 가지는 특정 이슈가 있는데 그것은 클라이언트의 갑작스러운 사라짐에 어떠한 알림도 제공하지 않는 것이다. ( [SERVLET_SPEC-44](https://java.net/jira/browse/SERVLET_SPEC-44) 참고) 그러나 Servlet container 는 응답을 write 하기 위한 이어지는 시도에 예외를 발생한다. Spring SockJS 지원은 기본 25초 간격의 heartbeat message 를 전송하므로 이를 통해 보통 client disconnect 는 주기 안에 발견되어 진다. (주기를 짧게 하면 더 빨리 알게됨)

결론적으로, Network IO failure 은 client disconnect 에 대해서 빈번하게 발생할 여지가 있다. 이것은 로그를 stack trace 로 채우게 될 수도 있다. Spring 은 이러한 client disconnect 를 식별하기위해 최선의 노력을 하고 이에 따른 최소한의 메시지를 기록하려고 노력한다. (이 로그는 AbstractSockJsSession 에 정의된 DISCONNECTED_CLIENT_LOG_CATEGORY 로그 카테고리를 사용한다. 만약 stack trace 를 보고자 한다면 해당 로그 카테고리를 TRACE 로 설정하라)

## 6. CORS Headers for SockJS

SockJS protocol 은 XHR streaming 과 polling 전송에 cross-domain 지원을 위한 CORS 헤더를 사용한다. 그래서 CORS 헤더가 응답에서 발견되지 않는다면 CORS 헤더들이 자동으로 추가된다. 만약 Servlet Filter 등을 통해서 CORS 헤더가 이미 설정된다면 Spring SockJsService 는 이를 스킵한다.

다음은 SockJS 에 의해 기대되는 header 와 값들이다.

- “Access-Control-Allow-Origin” - intitialized from the value of the “origin” request header or “*”.
- “Access-Control-Allow-Credentials” - always set to true.
- “Access-Control-Request-Headers” - initialized from values from the equivalent request header.
- “Access-Control-Allow-Methods” - the HTTP methods a transport supports (see TransportType enum).
- “Access-Control-Max-Age” - set to 31536000 (1 year).

정확한 구현을 보고자 한다면 AbstractSockJsService.addCorsHeaders() 와 TransportType enum 을 소스에서 살펴보라.

대안으로서 CORS 설정은 SockJS endpoint prefix 를 제외 URL 목록으로 고려한다면, Spring SockJsService 가 그것을 처리토록 한다.


