---
title: WebSocket
linkTitle: "WebSocket"
description: WebSocket은 HTTP 환경에서 양방향 통신을 지원하는 Spring 기술로, Spring은 기본적으로 STOMP sub-protocol을 사용한다. Spring Framework 4.0부터 spring-websocket 모듈이 추가되어 복잡한 WebSocket 통신을 지원하며, JSR356(Java WebSocket API)과 호환된다.
url : /egovframe-runtime/presentation-layer/webSocket/
menu:
    depth:
        name: WebSocket
        weight: 10
        parent: "presentation-layer"
        identifier: "WebSocket"
---
# WebSocket

## 개요

WebSocket 은 HTTP 환경에서 소켓 통신을 지원하기 위한 Spring 기술이다. Spring 은 기본적으로 WebSocket sub-protocol 로 STOMP 를 사용한다.

(RFC6455는 웹 어플리케이션을 위한 새 기능으로 WebSocket protocol을 정의한다. 서버와 클라이언트간 양방향 통신(full-duplex)을 지원하는데, 이것은 웹을 좀 더 인터랙티브하게 만들기 위해 사용하였던 java applet, XMLHttpRequest, Flash, ActiveX 등의 기술을 대체하기 위한 중요한 기능이 될 수 있다.)

HTTP 는 초기 handshake (protocol upgrade or switch 요청이고 서버가 동의하는 경우 101 응답을 내려 줌)를 위해서만 사용되며, handshake 가 성공하면 HTTP upgrade 요청에 기인하는 TCP 소켓이 open 된  채 서버와 클라이언트간 통신을 처리한다.

- Spring Framework 4.0 에서는 새로운 spring-websocket module 을 포함하며 이를 통해 복잡한 WebSocket 을 지원하고, 이 모듈은 Java WebSocket API (JSR356) 과 호환되며 추가적인 기능을 제공한다.

### Spring Framework 4.0 WebSocket 지원 기능

WebSocket을 위한 요구사항.

- Java EE 7, JDK 7
- Servlet 3.1 ( Container : Apache Tomcat 7.0.47+, Eclipse Jetty 9.0+, GlassFish 4.0+ )
- Spring MVC 4.0이상 (eGov 3.5에 포함)
- websocket을 지원하는 브라우저 [websocket 브라우저 테스트 페이지](http://websocketstest.com/)

**1. WebSocket Fallback Options**

WebSocket은 Servlet 3.1에서 제공하기 시작한 기능을 이용하여 구현된 기술로서 모든 브라우저가 WebSocket을 지원하지는 않는다(IE는 10부터 지원).
따라서 WebSocket을 지원하지 않는 브라우저의 경우 해당 기능을 사용할 수 없고, 몇몇 Proxy 에서는 긴 연결상태를 강제로 끊어버리는 등의 오작동이 있을 수 있다. (관련 대안으로 fallback option을 지원하도록 구성된 Spring framework의 SockJS protocol 참고 - Spring 설정을 활성화 시킴으로서 쉽게 Application 에 적용 가능)

**2. Messaging Architecture**

기존에 구성하던 방식의 개발방법인 REST는 Web application 개발에 있어 많은 URL (noun) 과 몇개의 HTTP method (verbs), 그리고 상태와 무관한 architecture 를 사용한다.

WebSocket application 에서는 초기 HTTP handshake 에서만 하나의 URL 을 사용하고, 그 후의 모든 메시지는 handshake 시 맺어진 TCP 연결을 통해서 전송된다. 이것은 전통적인 messging application (JMS, AMQP) 과 가까운 비동기, event-driven, messaging 아키텍처를 사용하는 것이다.

Spring Framework 4.0 에서는 spring-messging 모듈을 통해 기능을 제공하는데, 이 모듈은 스프링 통합 프로젝트에서 사용하는 Message, MessageChannel, MessageHandler 와 같은 추상화된 개념을 제공하여 messaging archtecture 의 근간이 된다. 이 모듈은 Spring MVC annotaion 기반의 programming model 과 유사하게 작성할 수 있도록 몇 가지 annotation 을 포함하고 있다.

**3. Sub-Protocol Support in WebSocket**

WebSocket 은 messaging architecture 를 함축하지만 특정 messaging protocol 사용을 강제하지 않는다. 이것은 매우 얇은 layer 이며 단순히 TCP 위에서 일련의 byte 스트림들을 메시지로 변환하는 것에 지나지 않는다. 메시지의 의미 해석은 Application 에 맡겨둔 채 말이다.

HTTP (이것은 application level protocol 이다.) 와 달리 WebSocket 의 protocol 은 단순화 하여 어떻게 처리할지 어디로 route 할지에 대한 충분한 정보가 제공되지 않는 저수준으로 제공된다. 이러한 이유로 WebSocket RFC 에서는 sub-protocol 들의 사용을 정의하였다. handshake 사용 중 클라이언트와 서버는 Sec-WebSocket-Protocol 헤더를 사용할 수 있고 이를 통해 서로 통신할 sub protocol 을 합의한다. WebSocket 은 sub-protocol 을 강제하지 않기에 필수적인 것은 아니지만 이 경우 client/server 는 서로 message 포맷에 대해 합의되어야 한다.

Spring 은 STOMP 지원을 제공하며 이는 HTTP 와 유사한 형태로 script 언어에서 사용을 위해 만들어진 것이다. STOMP 는 널리 지원되고 WebSocket 사용에 적합하다.

**4. WebSocket 을 사용하여야 하는가?**

WebSocket 은 서버와 클라이언트가 적은 지연에 매우 빈번하게 이벤트를 교환해야 할 경우에 적합하다. 이는 finance, game, collaboration 등의 application 일 수 있다. 이들은 모두 time delay 에 민감하고 매우 빈번하게 많은 종류의 메시지를 교환해야 한다.

social, news feed 와 같은 경우는 단순 polling 으로 충분하다. 이들은 latency 가 중요한 요소가 아니다. latency 가 중요하더라도 message 의 크기가 작다면 (network failure check 같은) long polling 이 충분한 대안이 될 수 있다.

low latency 와 high frequency 가 중요한 경우에는 WebSocket 이 적합하다. 하지만 이러한 경우에도 모든 client-server 통신이 WebSocket 을 이용해야 하는 지는 application 에 따라 다를 수 있다. 최적의 경우를 생각하여 client 가 사용할 수 있는 대안으로서 WebSocket 과 REST API 를 모두 제공해야 할 수도 있다. 이 경우 REST 호출을 통해 특정 메시지를 WebSocket 클라이언트들에게 모두 전달될 필요가 있을 수도 있다.

Spring Framework 는 @Controller, @RestController 클래스에 HTTP 핸들링 메소드와 WebSocket 핸들링 메소드를 사용할 수 있다. 게다가 Spring MVC 요청 핸들링 메소드는 모든 WebSocket 클라이언트에 메시지를 전달하거나 특정 사용자에게만 전달하는 것을 쉽게 제공한다.

### WebSocket API

Spring Framework 는 다양한 WebSocket Engine 에 적합하게 설계되었다. 예를 들어 Tomcat (7.0.47+) or GlassFish (4.0+), WildFly (8.0+) JSR-356 런타임상에서 구동하거나 Jetty (9.1+) 에서와 같이 native WebSocket 지원 환경에서 구동할 수 있다.

직접적인 WebSocket API 를 application 개발에 사용하는 것은 매우 저수준의 행위까지 설계해야 한다. 메시지 포맷에 대한 것 또는 annotation 을 통한 message 라우팅 같은 것을 지원하도록 application 에서는 sub-protocol 을 사용하는 것이 좋으며, 이러한 맥락에서 Spring 은 STOMP over WebSocket 을 지원한다.

#### Spring WebSocket 지원 살펴보기

**1. WebSocketHandler 설정**

Spring 은 WebSocketHandler 를 구현함으로 WebSocket 서버를 만드는 것을 지원한다. WebSocketHandler 는 TextWebSocketHandler 나 BinaryWebSocketHandler 로 세분화 되어 있다.

```java
import org.springframework.web.socket.WebSocketHandler;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.TextMessage;
 
public class MyHandler extends TextWebSocketHandler {
 
    @Override
    public void handleTextMessage(WebSocketSession session, TextMessage message) {
        // ...
    }
 
}
```

특정 URL 에 WebSocketHandler 를 설정하는 Java-Config 설정

```java
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;
 
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(myHandler(), "/myHandler");
    }
 
    @Bean
    public WebSocketHandler myHandler() {
        return new MyHandler();
    }
 
}
```

동일 설정을 위한 XML Config 설정

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
    </websocket:handlers>
 
    <bean id="myHandler" class="org.springframework.samples.MyHandler"/>
 
</beans>
```

위의 설정은 Spring 의 DispatcherServlet 을 사용하는 설정이다. 하지만 Spring 은 다른 Web 개발 환경에서 WebSocketHandler 를 사용할 수 있도록 WebSocketHttpRequestHandler 를 지원한다.

**2. WebSocket Handshaking 커스터마이즈**

초기 WebSockethandshake 를 커스터마이징 하는 가장 손쉬운 방법은 HandshakeInterceptor 를 사용하는 것인데 이것은 handshake 하는 것에 대한 before 와 after 처리를 기술할 수 있다. 이것은 handshake 를 준비하기 위해 사용되거나 WebSocketSession 에서 특정 attribute 를 이용할 수 있도록 하는데 사용된다. 아래는 Spring 에서 제공되는 interceptor 로 http 세션 attribute 를 WebSocketSession 에 전달해 주는 일을 한다.

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(new MyHandler(), "/myHandler")
            .addInterceptors(new HttpSessionHandshakeInterceptor());
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
        <websocket:handshake-interceptors>
            <bean class="org.springframework.web.socket.server.support.HttpSessionHandshakeInterceptor"/>
        </websocket:handshake-interceptors>
    </websocket:handlers>
 
    <bean id="myHandler" class="org.springframework.samples.MyHandler"/>
 
</beans>
```

좀 더 고급 옵션을 적용하려면 DefaultHandshakeHandler 를 확장하여야 한다. 이것은 validating, client origin, sub-protocol 협의 및 기타 여러가지를 포함하고 있다. application 은 특정 WebSocket server engine 이나 아직 지원하지 않는 버전에 대한 지원을 위해서 커스텀 RequestUpgradeStrategy 를 설정할 필요가 있다.

**3. WebSocketHandler Decoration**

Spring 은 WebSocketHandlerDecorator 기본 클래스를 제공한다. 이것은 WebSocketHandler 에 추가적인 행위를 decorate 하는데 사용된다. Logging, Exception Handling WebSocketHandlerDecorator 구현이 Java-config 나 XML config 를 통해서 기본적으로 제공되고 있다. ExceptionWebSocketHandlerDecorator 는 WebSocketHandler 에서 발생하는 처리되지 않은 모든 예외를 catch 하여 Server error 를 나타내기 위해 1011 status code 로 응답한다.

**4. 배포 고려사항**

Spring WebSocket API 는 Spring MVC application 과 통합이 쉽다. 그것은 Dispatcher Servlet 이 HTTP WebSocket handshake 뿐만 아니라 다른 HTTP 요청도 서비스 하기 때문이다. WebSocketHttpRequestHandler 를 사용하면 다른 HTTP 처리 시나리오 (Spring MVC 이외의 다른 Web Framework 와 같은) 와도 쉽게 결합할 수 있다. 그러나 JSR-356 runtime 에 특별한 고려사항이 있다.

Java WebSocket API (JSR-356) 는 두가지 배포 메커니즘을 제공한다. 첫번째는 시작 시 Servlet container classpath scan (Servlet 3 의 기능) 에 관한 것이고 다른 것은 Servlet container 초기화에서 사용하기 위한 registration API 에 관한 것이다. 이것 중 어느 것도 모든 HTTP 요청을 처리하는 단일 front controller 를 사용하지 못한다. 즉 DispatcherServlet 은 원칙적으로 WebSocket handshake 와 다른 모든 HTTP 요청에 대해서 사용할 수 없다.

이것은 JSR-356 이 가지는 매우 중요한 한계인데 Spring 의 WebSocket 지원은 JSR-356 runtime 환경에서도 서버 특화의 RequestUpgradeStrategy 를 제공함으로 이를 지원하고 있다. 현재 Spring 은 Tomcat 7.0.47+, Jetty 9.1+, GlassFish4.0+, WildFly8.0+ 을 지원한다. 추가적인 지원은 더 많은 WebSocket runtime 을 이용할 수 있을 때 추가될 것이다.

두 번째 고려사항은 JSR-356 지원의 Servlet container 가 SCI scan 을 수행하도록 하고 있어 application 구동을 느리게 (혹은 어떤 특정 상황에서는 매우 느리게) 할 수 있다는 것이다. 만약 JSR-356 지원 Servlet container version 업그레이드시 명백한 영향이 목격된다면, 선택적으로 web fragments (SCI scanning) 을 활성 및 비활성할 수 있다. (이는 web.xml 의 absolute-ordering 을 사용토록 한다.) web fragment 순서를 명확히 하도록 web.xml 에서 absolute-ordering 을 사용 토록 한다. (이는 scanning 을 사용치 않도록 하는 방법이다.)

**5. WebSocket 엔진 설정하기**

각각의 기반이 되는 WebSocket engine 들은 message buffer size 나 idle timeout 등의 runtime 특성을 조절할 수 있는 configuration properties 를 가지고 있다. 이는 Tomcat, WildFly, Glassfish 에서ServletServerContainerFactoryBean 을 WebSocket java config 에 추가하여 설정할 수 있다.

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Bean
    public ServletServerContainerFactoryBean createWebSocketContainer() {
        ServletServerContainerFactoryBean container = new ServletServerContainerFactoryBean();
        container.setMaxTextMessageBufferSize(8192);
        container.setMaxBinaryMessageBufferSize(8192);
        return container;
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
        http://www.springframework.org/schema/websocket/spring-websocket.xsd">
 
    <bean class="org.springframework...ServletServerContainerFactoryBean">
        <property name="maxTextMessageBufferSize" value="8192"/>
        <property name="maxBinaryMessageBufferSize" value="8192"/>
    </bean>
 
</beans>
```
client 측 WebSocket 설정을 위해서는 WebSocketContainerFactoryBean(XML) 이나 ContainerProvider.getWebSocketContainer() 를 이용한다.

Jetty 를 사용하는 경우에는 미리 설정된 WebSocketServerFactory 를 필요로 하고 이를 WebSocket java config 를 통해서 Spring 의 DefaultHandshakeHandler 에 추가한다.
```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
 
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(echoWebSocketHandler(),
            "/echo").setHandshakeHandler(handshakeHandler());
    }
 
    @Bean
    public DefaultHandshakeHandler handshakeHandler() {
 
        WebSocketPolicy policy = new WebSocketPolicy(WebSocketBehavior.SERVER);
        policy.setInputBufferSize(8192);
        policy.setIdleTimeout(600000);
 
        return new DefaultHandshakeHandler(
                new JettyRequestUpgradeStrategy(new WebSocketServerFactory(policy)));
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
        http://www.springframework.org/schema/websocket/spring-websocket.xsd">
 
    <websocket:handlers>
        <websocket:mapping path="/echo" handler="echoHandler"/>
        <websocket:handshake-handler ref="handshakeHandler"/>
    </websocket:handlers>
 
    <bean id="handshakeHandler" class="org.springframework...DefaultHandshakeHandler">
        <constructor-arg ref="upgradeStrategy"/>
    </bean>
 
    <bean id="upgradeStrategy" class="org.springframework...JettyRequestUpgradeStrategy">
        <constructor-arg ref="serverFactory"/>
    </bean>
 
    <bean id="serverFactory" class="org.eclipse.jetty...WebSocketServerFactory">
        <constructor-arg>
            <bean class="org.eclipse.jetty...WebSocketPolicy">
                <constructor-arg value="SERVER"/>
                <property name="inputBufferSize" value="8092"/>
                <property name="idleTimeout" value="600000"/>
            </bean>
        </constructor-arg>
    </bean>
 
</beans>
```


