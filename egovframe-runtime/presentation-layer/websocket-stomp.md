---
title: STOMP over WebSocket 개요 및 메시지 처리 흐름
linkTitle: "STOMP"
description: STOMP는 간단한 메시징 프로토콜로, Spring Framework에서 WebSocket과 결합해 메시지 전송 및 구독 기능을 제공한다. Spring WebSocket 설정을 통해 클라이언트와 서버 간의 메시지 흐름을 관리하며, 메시지를 처리하고 broadcasting하는 기능을 지원한다.
url : /egovframe-runtime/presentation-layer/webSocket/websocket-stomp/
menu:
    depth:
        name: STOMP
        weight: 1
        parent: "WebSocket"
---
# STOMP Over WebSocket Messaging Architecture

[http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-stomp](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-stomp)

WebSocket protocol 은 content 를 정의하지 않은 채 2 가지 유형 (text, binary) 의 메시지로 분류했다. content 를 정의하지 않은 대신 client 와 서버는 sub-protocol (content 를 정의하는 고수준의 protocol) 을 사용하는 것을 합의해야 할 수도 있다. sub-protocol 을 사용하는 것은 option 이지만 client 와 server 모두 메시지를 어떻게 해석해야 할지를 이해하는 것이 필요하다.

## 1. STOMP 개요

[STOMP](http://stomp.github.io/stomp-specification-1.2.html#Abstract) 는 Ruby, Python, Perl 과 같은 스크립트 언어를 위해 고안된 단순한 메시징 프로토콜이다. 그것은 메시징 프로토콜에서 일반적으로 사용되는 패턴들의 일부를 제공한다. STOMP 는 TCP 나 WebSocket 과 같은 신뢰성있는 양방향 streaming network protocol 상에 사용될 수 있다.

STOMP 는 HTTP 에 모델링된 frame 기반 프로토콜이다. 다음은 frame 의 구조이다.

```
COMMAND
header1:value1
header2:value2
 
Body^@
```

클라이언트는 메시지를 보내기 위해 SEND 명령을 사용하거나 수신 메시지에 관심을 표현하기 위해 SUBSCRIBE 명령을 사용할 수 있다. 이런 명령어들은 “destination” 헤더를 요구하는데 어디에 메시지를 전송할 지 혹은 어디에서 메시지를 구독할지를 나타낸다.

다음은 stock shares 를 구매하기 위한 요청 전송의 예이다.

```
SEND
destination:/queue/trade
content-type:application/json
content-length:44
 
{"action":"BUY","ticker":"MMM","shares",44}^@
```

다음은 stock quotes 를 얻기위한 클라이언트 구독의 예이다.

```
SUBSCRIBE
id:sub-1
destination:/topic/price.stock.*
 
^@
```

destination 의 의미는 STOMP spec 에서 투명하게 남겨두었다. 그것은 어떤 문자열이든 될 수 있고 그 의미나 문법은 온전히 STOMP 서버에 맡겨진다. 그러나 일반적으로 다음의 규칙을 사용하곤 한다.

“topic/..” - publish-subscribe (one to many) “queue/” - point-to-point (one to one)

STOMP 서버는 모든 구독자에게 message 를 broadcasting 하기 위해 MESSAGE 명령을 사용할 수 있다. 다음은 stock quote 를 구독자에서 전달하는 예이다.

```
MESSAGE
message-id:nxahklf6-1
subscription:sub-1
destination:/topic/price.stock.MMM
 
{"ticker":"MMM","price":129.45}^@
```

서버는 불분명한 메시지를 전송할 수 없음을 알아야 한다. 즉 서버의 모든 메시지는 특정 클라이언트 구독에 응답하여야 하고 서버 메시지의 “subscription-id” 헤더는 클라이언트 구독의 “id” 헤더와 일치하여야 한다.

지금까지 STOMP 의 가장 기본적인 이해를 위한 것이다. 상세한 것은 [specification](http://stomp.github.io/stomp-specification-1.2.html) 을 통해 살펴볼 수 있다.

다음은 STOMP over WebSocket 사용 application 의 장점을 요약한 것이다.

* Standard message format
* Application-level protocol with support for common messaging patterns
* Client-side support, e.g. stomp.js, msgs.js
* The ability to interpret, route, and process messages on both client and server-side
* The option to plug a message broker — RabbitMQ, ActiveMQ, many others — to broadcast messages (explained later)

순수 WebSocket 과 비교하여 STOMP 사용의 가장 중요한 요소는 Spring Framework 가 마치 SpringMVC 가 HTTP 에 프로그래밍 모델을 제공하는 것처럼 application 수준의 사용을 위한 프로그래밍 모델을 제공한다는 것이다.

## 2. Enable STOMP over WebSocket

Spring Framework 는 spring-messaging 와 spring-websocket 모듈을 통해 STOMP over WebSocket 사용을 제공한다.

다음은 SockJS fallback option 을 사용하는 STOMP WebSocket endpoint 설정의 예이다. endpoint 는 /app/portfolio URL 경로에 클라이언트가 접속할 수 있다.

```java
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
 
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
 
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.setApplicationDestinationPrefixes("/app")
            .enableSimpleBroker("/queue", "/topic");
    }
 
    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/portfolio").withSockJS();
    }
 
    // ...
 
}
```

동일 XML 설정은 다음과 같다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:websocket="http://www.springframework.org/schema/websocket" 
    xsi:schemaLocation=" 
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/websocket
        http://www.springframework.org/schema/websocket/spring-websocket-4.0.xsd">
 
    <websocket:message-broker application-destination-prefix="/app">
        <websocket:stomp-endpoint path="/portfolio">
            <websocket:sockjs/>
        </websocket:stomp-endpoint>
        <websocket:simple-broker prefix="/queue, /topic"/>
        ...
    </websocket:message-broker>
 
</beans>
```

브라우저 측에서는 stomp.js 나 sockjs-client 를 사용하여 접속한다.

```javascript
var socket = new SockJS("/spring-websocket-portfolio/portfolio");
var stompClient = Stomp.over(socket);
 
stompClient.connect({}, function(frame) {
}
```

SockJS 없는 WebSocket 사용은 다음과 같다.

```javascript
var socket = new WebSocket("/spring-websocket-portfolio/portfolio");
var stompClient = Stomp.over(socket);
 
stompClient.connect({}, function(frame) {
}
```

위의 stomp 클라이언트는 login 과 passcode 헤더를 정의할 필요가 없다. 제공되더라도 무시되거나 서버측에서 재정의 될 것이다. 인증에 대해서는 [Section 20.4.8, “Connections To Full-Featured Broker”](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-stomp-handle-broker-relay-configure) 와 [Section 20.4.9, “Authentication”](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/websocket.html#websocket-stomp-authentication) 를 참고하라

## 3. Flow of Messages

STOMP endpoint 가 설정될 때, spring application 은 연결된 클라이언트들에게 마치 STOMP broker 인 것처럼 동작한다. 들어오는 메시지를 처리하고 다시 메시지를 전송한다. 이 장에서는 Application 내에서 message flow 가 어떠한지에 대한 개략적인 개요를 제공한다.

spring-messaging 모듈은 [Spring Integration](https://spring.io/spring-integration) 프로젝트에 기반한 다양한 추상화를 포함하고 있으며, messging application 의 building block 으로 사용하도록 의도되었다.

* Message  —  represents a message with headers and a payload.
* MessageHandler — a contract for handling a message.
* MessageChannel  —  a contract for sending a message enabling loose coupling between senders and receivers.
* SubscribableChannel  —  extends MessageChannel and sends messages to registered MessageHandler subscribers.
* ExecutorSubscribableChannel  —  a concrete implementation of SubscribableChannel that can deliver messages asynchronously through a thread pool. 

제공되는 STOMP over WebSocket 설정 (Java,XML 모두) 은 다음의 3 가지 channel 들을 포함하여 실제적인 message flow 를 만들어내는데 사용된다.

* “clientInboundChannel” — for messages from WebSocket clients. Every incoming WebSocket message carrying a STOMP frame is sent through this channel.
* “clientOutboundChannel” — for messages to WebSocket clients. Every outgoing STOMP message from the broker is sent through this channel before getting sent to a client’s WebSocket session.
* “brokerChannel” — for messages to the broker from within the application. Every message sent from the application to the broker passes through this channel.

“clientInboundChannel” 의 메시지는 처리 (요청 실행과 같은) 를 위해 annotated method 로 흐르거나 broker (구동과 같은) 에 포워딩 될 수 있다. STOMP destination 은 단순한 prefix 기반 라우팅을 위해 사용되어진다. 예를 들어 ”/app” prefix 는 annotated method 로 라우팅하고 ”/topic” 이나 ”/queue” 는 broker 에 라우팅되는 것이다.

메지시 처리 annotated method 가 return type 을 갖을 때는 그 return value 는 Spring Message 의 payload 로서 “brokerChannel” 에 전송된다. 그러면 broker 는 메시지를 client 들에게 broadcasting 한다. 메시지를 destination 에 전송하는 것은 messaging template 의 도움으로 application 내 어디에서나 수행될 수 있다. 예를 들어, HTTP POST 처리 메소드는 메시지를 연결된 클라이언트들에게 broadcast 할 수 있는 것이다. 또는 service component 는 주기적으로 stock quotes 를 broadcast 할 수 있다.

다음은 메시지 흐름을 보여주는 단순한 예이다.

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
 
    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/portfolio");
    }
 
    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.setApplicationDestinationPrefixes("/app");
        registry.enableSimpleBroker("/topic/");
    }
 
}
```
```java
@Controller
public class GreetingController {
 
    @MessageMapping("/greeting") {
    public String handle(String greeting) {
        return "[" + getTimestamp() + ": " + greeting;
    }
 
}
```
다음은 위 예제의 메시지 흐름에 대한 설명이다.

* WebSocket clients connect to the WebSocket endpoint at ”/portfolio”. * Subscriptions to ”/topic/greeting” pass through the “clientInboundChannel” and are forwarded to the broker.
* Greetings sent to ”/app/greeting” pass through the “clientInboundChannel” and are forwarded to the GreetingController.
* The controller adds the current time and the return value is passed through the “brokerChannel” as message to ”/topic/greeting” (destination is selected based on a convention but can be overridden via @SendTo).
* The broker in turn broadcasts messages to subscribers and they pass through the “clientOutboundChannel”.

다음 장에서 argument 와 return value 의 종류를 포함한 annotated method 의 상세한 내용을 제공한다.

## 4. Annotation Message Handling

@MessageMapping annotation 은 @Controller 와 @RestController annotated class 의 메소드에 적용할 수 있다. 이것은 메소드를 path-like message destination 에 매핑하기 위해 사용될 수 있다. 이것은 또한 controller 내의 모든 annotated method 들과 공유되는 매핑을 표현하기 위해 type-level @MessageMapping 과 결합할 수 있다.

Destination mapping 은 Ant-style pattern (e.g. ”/foo*”, ”/foo/**”) 과 template variable (e.g. ”/foo/{id}”, 이것은 @DestinationVariable 메소드 인자를 통해 접근될 수 있다.) 을 포함할 수 있다. 이처럼 SpringMVC 사용자 친화적인데, 실질적으로 SpringMVC 가 그러하듯 AntPathMatcher 는 pattern 기반의 destination mapping 과 template variable 추출에 사용된다.

@MessageMapping 메소드에서 다음의 method 인자가 지원된다.

* Message method argument to get access to the complete message being processed.
* @Payload-annotated argument for access to the payload of a message, converted with a org.springframework.messaging.converter.MessageConverter. The presence of the annotation is not required since it is assumed by default. Payload method arguments annotated with Validation annotations (like @Validated) will be subject to JSR-303 validation.
* @Header-annotated arguments for access to a specific header value along with type conversion using an org.springframework.core.convert.converter.Converter if necessary.
* @Headers-annotated method argument that must also be assignable to java.util.Map for access to all headers in the message.
* MessageHeaders method argument for getting access to a map of all headers.
* MessageHeaderAccessor, SimpMessageHeaderAccessor, or StompHeaderAccessor for access to headers via typed accessor methods.
* @DestinationVariable-annotated arguments for access to template variables extracted from the message destination. Values will be converted to the declared method argument type as necessary.
* java.security.Principal method arguments reflecting the user logged in at the time of the WebSocket HTTP handshake.

@MessageMapping 메소드의 return value 는 org.springframework.messaging.converter.MessageConverter 를 통해 변환되고 새로운 메시지의 body 로 사용된다. 이 새로운 메시지는 기본적으로 “brokerChannel” 에 client 메시지와 같은 destination 이지만 기본값 ”/topic” prefix 를 사용하여 전달된다. @SendTo message level annotation 은 다른 destination 을 지정하고자 할 때 사용될 수 있다.

@SubscribeMapping annotation 은 @Controller 메소드에 구독 요청을 매핑하기 위해 사용될 수 있다. 이것은 method level 에 지원되지만, type level 의 @MessageMapping annotation 과 결합하여 같은 controller 내의 모든 message handling method 들과의 공유 매핑을 표현할 수 있다.

기본적으로 @SubscribeMapping 메소드의 return value 는 broker 에 전달되는 것이 아니라 바로 연결된 클라이언트들에 메시지로서 전달된다. 이것은 request-reply message 교환에 유용하다. 예를 들어, application UI 가 초기화 될 때 application data 를 가져오는 것이다. 대안으로서 @SubscribeMapping 메소드가 @SendTo 가 적용되는 경우 결과 message 는 지정된 대상 destination 을 사용하여 “brokerChannel” 에 전달된다.

## 5. Sending Messages

Application 의 어떤 부분에서라도 접속된 client 들에게 메시지를 보내고자 할 때 어떻게 해야 할까? 어떠한 application component 라도 “brokerChannel” 에 메시지를 전송할 수 있다. 이를 위한 가장 쉬운 방법은 SimpMessagingTemplate 을 주입받아서 메시지 전송에 사용하는 것이다. 이것은 다음의 예제를 통해 확인할 수 있다.

```java
@Controller
public class GreetingController {
 
    private SimpMessagingTemplate template;
 
    @Autowired
    public GreetingController(SimpMessagingTemplate template) {
        this.template = template;
    }
 
    @RequestMapping(value="/greetings", method=POST)
    public void greet(String greeting) {
        String text = "[" + getTimestamp() + "]:" + greeting;
        this.template.convertAndSend("/topic/greetings", text);
    }
 
}
```

## 6. Simple Broker

기본 제공되는 단순한 message broker 는 클라이언트로부터의 구독 요청을 처리하고 그것을 메모리에 저장하고 일치하는 destination 을 가지는 연결된 client 들에 메시지를 brodcasting 한다. broker 는 Ant-style destination pattern 구독을 포함하는 동시에 path-like destination 을 지원한다.

## 7. Full-Featured Broker

Simple broker 가 초기 시작을 위해서는 훌륭하지만 STOMP 명령의 subset 들만을 지원하고 (e.g. no acks, receipts, etc) 단순 메시지 전송 loop 에 의존하며, clustering 에 적합하지 않다. 대신 application 은 full-featured message broker 를 사용하도록 업그레이드 할 수 있다.

적합한 message broker 선택 ( [RabbitMQ](http://www.rabbitmq.com/stomp.html), [ActiveMQ](http://activemq.apache.org/stomp.html), others) 을 위해 STOMP 문서를 확인하라. 그것을 설치하고 STOMP 지원을 활성화하여 broker 를 구동하라. 그 다음 Spring configuration 에서 simple broker 대신 STOMP broker relay 를 활성화 하라.

다음은 full-featured broker 를 활성화하는 설정예제이다.

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
 
    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/portfolio").withSockJS();
    }
 
    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.enableStompBrokerRelay("/topic/", "/queue/");
        registry.setApplicationDestinationPrefixes("/app");
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
 
    <websocket:message-broker application-destination-prefix="/app">
        <websocket:stomp-endpoint path="/portfolio" />
            <websocket:sockjs/>
        </websocket:stomp-endpoint>
        <websocket:stomp-broker-relay prefix="/topic,/queue" />
    </websocket:message-broker>
 
</beans>
```

위의 설정에서 “STOMP broker relay” 는 Spring [MessageHandler](http://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/messaging/MessageHandler.html) 인데 이것은 외부 broker 에 메시지들을 forwarding 함으로써 메시지들을 처리한다. 그렇게 하기 위해 broker 에 TCP 연결을 맺고 모든 메시지를 broker 에 forwarding 하고 broker 로 부터 수신된 메시지를 WebSocket session 을 통해 client 에 역 forwarding (되돌려준다.) 한다. 본질적으로 그것은 마치 양방향으로 message 를 forwarding 하는 “relay” 처럼 동작한다.

org.projectreactor:reactor-net 의존성을 추가하여 TCP connection 관리를 할 수 있다.

게다가 application components (e.g. HTTP request handling method, business service, etc) 는 또한 메시지를 broker relay 에 전송할 수 있다. Section 20.4.5, “Sending Messages” 에서 subscribed WebSocket 클라이언트들에 메시지를 broadcast 하는 것이 설명되어 있다.

사실상 broker relay 는 강력하고 scalabale 한 message brodcasting 을 활성화 한다.

## 8. Connections To Full-Featured Broker

STOMP broker relay 는 broker 에 대한 단일 “system” TCP connection 을 유지한다. 이 connection 은 receiving message 가 아닌 server 측 application 에 기인하는 message 들만을 위해 사용된다. 이러한 접속을 위해 STOMP credentials 을 설정할 수 있다. (STOMP frame login 과 passcode 헤더) 이것은 Java config 와 XML 모두에서 systemLogin/systemPasscode 속성으로 노출된다. (기본값은 guest/guest 이다.)

STOMP broker relay 는 또한 모든 접속된 WebSocket client 를 위해 별도의 TCP 연결을 생성한다. 클라이언트를 대신해 모든 TCP 연결을 위해 STOMP credetial 을 설정할 수 있다. 이것은 Java config 와 XML 모두에서 clientLogin/clientPasscode 속성으로 노출된다. (기본값은 guest/guest 이다.)

STOMP broker relay 는 또한 “system” TCP connection 상에서 message broker 로부터의/로 hearbeat 을 전송하고 수신한다. heartbeat 전송/수신의 interval 을 설정할 수 있는데 기본값은 10 초이다. 만약 broker 에 대한 연결이 끊어지면 broker relay 는 재접속 시도를 성공할 때까지 5 초마다 계속한다.

Spring Bean 은 `ApplicationListener<BrokerAvailabilityEvent>` 를 구현할 수 있는데 이를 통해 broker 에 대한 “system” connection 이 끊기고 재접속될 때 알림을 받을 수 있다. 예를 들어, stock quote 를 broadcasting 하는 Stock Quote service 는 어떠한 active “system” connection 이 없을 때 메시지 전송시도를 중단할 수 있다.

STOMP broker relay 는 virtualHost 속성으로 설정될 수 있다. 이 속성의 값은 모든 CONNECT frame 의 host header 에 설정될 것이고 예를 들어 TCP connection 이 맺어진 실제 host 가 cloud-based STOMP service 를 제공하는 host 와 다른 cloud 환경에서 유용할 수 있다.

## 9. Authentication

WebSocket-style application 에서 누가 메시지를 보냈는지 아는것은 때때로 유용하다. 그래서 몇가지 인증 형태가 사용자 identity 를 형성하고 그것을 현재 session 에 연결하는데 필요하다.

Web application 은 이미 HTTP 기반의 인증을 사용한다. 예를 들어, Spring Security 는 보통 application 의 HTTP URL 을 보호할 수 있다. WebSocket session 이 HTTP handshake 로 시작하기 때문에 STOMP/WebSocket 에 매핑된 URL 은 이미 보호되고 인증을 요구한다는 것을 의미한다. 게다가 WebSocket 연결을 시작하는 page 는 그 스스로 거의 보호되는 것이고 실제 handshake 시까지 그 사용자는 인증되어져야 한다.

WebSocket hanshake 가 형성되고 새로운 WebSocket session 이 생성될 때 Spring WebSocket 지원은 자동적으로 HTTP request 로 부터 WebSocket session 으로 java.security.Principal 을 전달한다. 이후 WebSocket session 상의 application 을 통한 모든 message flow 는 사용자 정보가 포함되어진다. 그것은 message 의 header 에 존재한다. Controller 메소드는 javax.security.Principal 타입의 메소드 인자를 추가함으로 현재 사용자에 접근할 수 있다.

비록 STOMP CONNECT frame 이 인증을 위한 “login” 과 “passcode” 헤더를 가지고 있다하더라도, Spring 의 STOMP WebSocket 지원은 그것들을 무시하고 사용자가 HTTP 를 통해 기 인증되었기를 기대한다.

어떤 경우에는 사용자가 공식적으로 인증되지 않았을 때일지라도 WebSocket session 에 identity 를 부여하는것이 유용할 수도 있다. 예를 들면, mobile app 은 익명의 사용자에 어떤 identity (아마도 지리적 위치에 기반하여) 를 부여하기도 한다. 이때에 사용자 정의 handshake handler 가 사용될 수 있다. (Section 20.2.4, “Deployment Considerations” 에서 예제를 확인하라)

## 10. User Destinations

Application 은 특정 사용자를 지정하여 메시지를 전송할 수 있다. 연결된 사용자가 메시지를 수신하기 위해 그들은 인증되어져야 한다. 그래야 그들의 session 이 실제 user name 과 연결되기 때문이다. 앞선 section 에서 인증에 대해 확인하라

Spring 의 STOMP 지원은 /user/ 접두어로 destination 을 식별한다. 예를 들어, 클라이언트가 /user/position-updates destination 에 subscribe 할 수 있다. 이 destination 은 UserDestinationMessageHandler 에 의해 처리되고 사용자 session 에 unique 한 destination 으로 변환된다. (e.g. /user/position-updates-123) 이것은 일반적으로 명명된 destination 에 subscribing 편의를 제공하는 동시에 /user/position-updates 에 subscribe 하는 어떤 다른 사용자와 충돌하지 않음을 보장한다.

전송 측에서 메시지는 /user/{username}/position-updates 와 같은 destination 에 전송될 수 있다. 그러면 UserDestinationMessageHandler 에 의해 지정한 사용자 명에 속한 unique destination 과 같도록 번역될 것이다.

이것은 application 내의 어떤 component 도 name 과 일반적인 destination 만 알면 특정 사용자에 메시지를 전송할 수 있게 한다. 이것이 외부 message broker 와 같이 사용될 때 사용자 session 이 넘치면 모든 unique 한 사용자 queue 가 삭제되도록 하기 위해 inactive queue 를 다루는 방법에 대해 broker 문서를 확인하라. 예를 들어 RabbitMQ 는 /exchange/amq.direct/position-updates 와 같은 destination 이 사용될 때 auto-delete queue 를 생성한다. 클라이언트가 /user/exchange/amq.direct/position-updates 에 subscrbe 하는것이 그러한 경우이다. ActiveMQ 는 inactive destination 을 제거하기 위한 configuration options 이 있다.

## 11. ApplicationContext Events

STOMP messaging 지원은 다음의 ApplicationContext 이벤트를 발생시킨다. 이러한 이벤트들중 하나 혹은 그 이상을 처리하기 위해 Spring 관리 component 는 ApplicationListener 를 구현할 수 있다. 이벤트는 다음과 같다.

BrokerAvailabilityEvent — broker 가 available/inavailable 될 때 나타난다. “simple” broker 는 시작시 즉시 available 되고 application 구동중 유지되지만 STOMP “broker relay” 는 만약 broker 가 재시작되면 full featured broker 에 대한 연결을 잃을 지도 모른다. broker relay 는 reconnect logic 을 가지고 있고 broker 에 대한 “system” connection 을 broker 가 돌아오면 재설정 할 것이다. 그 결과 이 event 는 상태가 connected 에서 disconnected 가 될 때나 그 반대일때마다 발생한다. SimpMessagingTemplate 을 사용하는 Components 는 이 이벤트에 subscribe 하여야 하며 broker 가 이용불가일 때 메시지를 전송하지 말아야 한다. 어떤 경우에서는 메시지를 전송할 때 MessageDeliveryException 을 처리하도록 준비되어야 한다. SessionConnectEvent — 새로운 클라이언트 session 을 나타내는 STOMP CONNECT 가 수신될 때 나타난다. 이 이벤트는 session id , user information 및 client 가 보냈을 지 모르는 어떤 사용자 정의 header 를 포함한다. 이것은 client sessions 을 추적하는데 유용하다. 이 이벤트에 subscribe 하는 Components 는 SimpMessageHeaderAccessor 나 StompMessageHeaderAccessor 를 사용하여 메시지를 wrapping 할 수 있다. SessionConnectedEvent — broker 가 SessionConnectEvent 이후 CONNECT 에 대한 응답으로 STOMP CONNECTED frame 을 전송했을 때 짧게 발생한다. 이 시점에 STOMP session 은 완전히 연결되었음으로 간주될 수 있다. SessionDisconnectEvent — STOMP session 이 끝났을 때 발생한다. DISCONNECT 는 client 로 부터 전송되거나 WebSocket session 이 closed 될 때 자동적으로 발생되어질 수 있다. 어떤 경우에 이 이벤트는 세션당 한번 이상 발생할수도 있다. Components 는 복수의 disconnect events 에 대해 idempotent(멱등) 해야 한다. full-featured broker 를 사용할 때, STOMP “broker relay” 는 자동적으로 broker 가 일시적으로 이용불가한 “system” connection 을 재접속 한다. 그러나 Client connections 는 자동적으로 재접속 되지 않는다. heartbeats 이 활성화 되어 있다면, client 는 일반적으로 10초 안에 broker 가 응답하지 않음을 알게 될 것이다. Clients 는 스스로 reconnect logic 을 구현해야할 필요가 있다.

## 12. Configuration and Performance

성능에 대한 은총알은 없다. 많은 요인 (메시지 size, volume, application 메소드가 blocking 을 요하는 작업을 수행하는지 여부, network 속도 같은 외부요소 및 기타등등) 이 영향을 끼친다. 이 section 의 목적은 scaling 에 대한 생각과 더불어 이용가능한 configuration options 의 개요를 제공하는 것이다.

messaging application 에선 messages 는 thread pool 에 기반한 비동기 수행을 위해 channels 을 통해 전달된다. 이런 application 을 설정하는 것은 channels 과 messages flow 에 대한 지식이 요구된다. 그래서 Section 20.4.3, “Flow of Messages” 를 리뷰해보기 바란다.

시작하기 좋은 위치는 “clientInboundChannel” 과 “clientOutboundChannel” 를 지지하는 thread pools 을 설정하는 것이다. 기본적으로 이 둘은 사용가능한 processor 수의 2배로 설정된다.

막약 annotated method 에서 메시지 처리가 주로 CPU 소비에 기인하면 “clientInboundChannel” 의 thread 수는 processor 수에 가깝게 유지되어야 한다. 만약 작업이 IO 소비에 기인하고 database 나 다른 external system 에 blocking 을 요한다면 thread pool size 는 증가되어야 할 필요가 있다.

ThreadPoolExecutor 는 3 가지 중요한 property 를 갖는다. 그것은 core 와 max thread pool size 와 이용가능한 thread 가 없을 때 작업을 저장하기 위한 queue capacity 이다.

일반적인 혼동이 오는 지점은 core pool size (e.g. 10) 와 max pool size (e.g. 20) 설정이 10 에서 20 threads 를 가지는 thread pool 로 나타나는 것이다. 사실 capacity 가 그 기본값인 Integer.MAX_VALUE 인채로 남겨두면 thread pool 은 모든 추가적인 작업이 queue 에 쌓일 것이기 때문에 결코 core pool size 위로 증가하지 않을 것이다.

이러한 properties 들이 어떻게 작용하고 다양한 queuing strategies 를 이해하기 위해 ThreadPoolExecutor 의 Javadoc 을 확인하라.

“clientOutboundChannel” 측에서 thread pool 은 온전히 WebSocket clients 에 메시지를 전송하는 것과 관련있다. 만약 clients 가 빠른 network 에 있다면 스레드 수는 이용가능한 processors 수에 가깝게 유지되어야 한다. 만약 그들이 느리거나 low bandwidth 상에 있다면 그들은 메시지 소비를 위해 더 오래 점유할 것이고 thread pool 에 부담을 줄 것이다. 그래서 thread pool size 증가가 필요할 수도 있을 것이다.

“clientInboundChannel” 에 대한 부하는 예상가능하다 — 결국 그것은 application 이 무엇을 하는지에 기인한다.— ”clientOutboundChannel” 을 어떻게 설정해야 하는지는 application 제어를 넘어서는 요인에 기인하기 때문에 좀더 어렵다. 이러한 이유로 메시지 전송과 관련한 두가지 추가적인 properties 가 있다. 그것은 “sendTimeLimit” 와 “sendBufferSizeLimit” 이다. 이것은 얼마나 오래 그 전송이 허락되는가와 얼마나 많은 데이터가 client 에 메시지 전송시 buffer 되는지를 설정하는데 사용된다.

일반적인 생각은 어떤 주어진 시간에 단 하나의 thread 만이 client 에 메시지 전송을 위해 사용되어져야 한다는 것이다. 모든 추가적인 메시지는 동시에 버퍼링 되고 이러한 properties 가 얼마나 오래 메시지 전송에 점유가 허락되는가와 얼마나 많은 데이터가 동시에 버퍼링 되는가에 사용할 수 있다. 중요한 추가적인 세부사항은 XML schema 의 Javadoc 을 참고하라.

다음은 설정 예이다.

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
 
    @Override
    public void configureWebSocketTransport(WebSocketTransportRegistration registration) {
        registration.setSendTimeLimit(15 * 1000).setSendBufferSizeLimit(512 * 1024);
    }
 
    // ...
 
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
 
    <websocket:message-broker>
        <websocket:transport send-timeout="15000" send-buffer-size="524288" />
        <!-- ... -->
    </websocket:message-broker>
 
</beans>
```
위의 WebSocket 전송 설정은 들어오는 STOMP messages 에 허락되는 최대 사이즈를 설정하는데 사용될 수 있다. 비록 이론적으로 WebSocket message 가 size 에 제한이 없지만, 실제 WebSocket servers 는 한계를 부여한다. 예를 들어 Tomcat 에서 8K 이고 Jetty 에서 64K 이다. 이런 이유로 stomp.js 같은 STOMP clients 는 커다란 STOMP messages 를 16K boundaries 로 분리하고 그들을 복수개의 WebSocket messages 로 전송한 후 서버가 buffer 해서 재조합하도록 한다.

Spring 의 STOMP over WebSocket 지원은 이것을 수행한다. 그래서 applications 은 STOMP messages 를 위해 WebSocket server 고유의 message sizes 를 무시한 채 maximum size 를 설정할 수 있다. WebSocket message size 가 만약 최소 16K WebSocket messages 전송을 보장하여야 한다면 자동적으로 조정되어질 것을 명심하라.

다음은 설정예시이다.
```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
 
    @Override
    public void configureWebSocketTransport(WebSocketTransportRegistration registration) {
        registration.setMessageSizeLimit(128 * 1024);
    }
 
    // ...
 
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
 
    <websocket:message-broker>
        <websocket:transport message-size="131072" />
        <!-- ... -->
    </websocket:message-broker>
 
</beans>
```
scaling 에 대한 중요한 point 는 복수개의 application instances 를 사용하는 것이다. 현재 simple broker 로는 불가능하다. 그러나 RabbitMQ 같은 full-featured broker 를 사용할 때, 각 application instance 는 broker 에 연결하고 하나의 application instance 로부터의 messages broadcast 는 어떤 다른 application instances 를 통해 연결된 WebSocket clients 에 그 broker 를 통해 broadcast 할 수 있다.

## 13. Testing Annotated Controller Methods

Spring 의 STOMP over WebSocket 지원에 2가지 주요한 접근이 있다. 첫번째는 controller 의 기능과 annotated message handling method 의 기능을 검증하는 server-side tests 를 작성하는 것이다. 두번째는 client 와 server 구동과 관련한 전체 end-to-end tests 를 작성하는 것이다.

2 가지 접근은 상호 보완적이지 않다. 그와는 반대로 전체 test 전략에 각각 위치한다. Server-side tests 는 좀더 집중되고 작성하고 유지하기가 쉽다. 반면에 End-to-end integration tests 는 좀 더 완벽하고 테스트가 더 많지만 그것들은 작성과 유지에 더 많이 관련되어 진다.

가장 단순한 server-side tests 는 controller unit tests 를 작성하는 것이다. 그러나 이것은 충분히 유용하지 않다. 왜냐하면 controller 의 많은 부분이 annotations 에 의존하기 때문이다. 순수한 unit tests 는 그것을 테스트하지 못한다.

이상적으로 테스트 하의 controllers 는 마치 SpringMVC Test framework 에서 HTTP 요청을 처리하는 controller 를 테스트하는 접근같이 runtime 에서 처럼 호출되어야 한다. 즉 구동중인 Servlet container 없이 Spring Framework 가 annotated controllers 를 호출하는 것이다. Spring MVC Test 와 같이 2가지 가능한 대안이 있다. 그것은 “context-based” 나 “standalone” setup 을 사용하는 것이다.

Spring TestContext framework 의 도움으로 실제 Spring configuration 로드하고 “clientInboundChannel” 를 테스트 field 로 주입받아서, 이를 사용하여 메시지를 전송한다. 수동적으로 controllers 를 호출하기 위해 필요한 최소한의 Spring framework infrastructure 를 설정한다. (SimpAnnotationMethodMessageHandler) 그리고 메시지를 controller 에 직접 전달한다. 이 두가지 시나리오는 tests for the stock portfolio sample application 에서 시연되고 있다.

두번째 접근은 end-to-end integration tests 를 만드는 것이다. 이를 위해 WebSocket server 를 embedded mode 로 구동할 필요가 있고 STOMP frame 을 포함하는 메시지를 전송하는 WebSocket client 로서 서버에 접속한다. stock portfolio sample application 에 대한 test 는 embedded WebSocket 서버로서 Tomcat 을 사용하고 test 목적의 간단한 STOMP client 를 사용하는 접근을 보여준다.





