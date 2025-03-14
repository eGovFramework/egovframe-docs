---
title: The ApplicationContext
linkTitle: "ApplicationContext"
description: "`org.springframework.context` 패키지는 `ApplicationContext`를 통해 `BeanFactory`를 확장하여 애플리케이션 프레임워크에 맞는 추가 기능을 제공하며, 대부분의 경우 ContextLoader 등으로 자동 인스턴스화된다."
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-the-applicationcontext/"
menu:
    depth:
        name: The ApplicationContext
        weight: 8
        parent: "ioc-container"
---
# The ApplicationContext

## 개요

 org.springframework.context 패키지는 BeanFactory 인터페이스를 확장하는 ApplicationContext 인터페이스를 추가하고, 다른 인터페이스를 확장하여 보다 애플리케이션 프레임워크 지향적인 스타일로 추가 기능을 제공한다.  
많은 사람들이 ApplicationContext를 완전히 선언적인 방식으로 사용하며, 프로그래밍 방식으로 생성하지 않고 ContextLoader와 같은 지원 클래스에 의존하여 Java EE 웹 애플리케이션의 정상적인 시작 프로세스의 일부로 ApplicationContext를 자동으로 인스턴스화한다.

## 설명

 ApplicationContext는 BeanFactory를 확장한 것으로 BeanFactory의 기능 외에 아래와 같은 기능을 제공한다.

- MessageSource : i18n-sytle로 메시지를 access할 수 있도록 지원한다.
- Access to resources : URL, File 등과 같은 자원을 쉽게 access할 수 있도록 지원하다.
- Event propagation : ApplicationListener interface를 구현한 bean에게 Event를 전달한다.
- Loading of multiple (hierarchical) contexts : 계층 구조의 context를 지원함으로써, 어플리케이션의 웹 레이어 등과 같은 특정 레이어에만 집중적인 context를 작성할 수 있다.

### BeanFactory or ApplicationContext?

 아주 특별한 이유가 없는 한 ApplicationContext를 사용하는 것이 좋다. 다음은 BeanFactory와 ApplicationContext의 기능 비교표이다.

| Feature | BeanFactory | ApplicationContext |
| --- | --- | --- |
| Bean 객체화/엮음 | Yes | Yes |
| BeanPostProcessor 자동 등록 | No | Yes |
| BeanFactoryPostProcessor 자동 등록 | No | Yes |
| 편리한 MessageSource 접근(for i18n) | No | Yes |
| ApplicationEvent 발송 | No | Yes |

### MessageSources를 사용한 국제화(Internationalization using MessageSources)

 본 장의 내용은 [Resource](./resource.md)를 참조한다.

### Event

 ApplicationContext는 Event 처리를 위해 ApplicationEvent, ApplicationListener interface를 제공한다. ApplicationListener interface를 구현한 bean은 ApplicationContext에 발생한 모든 ApplicationEvent를 전달받는다. Spring이 제공하는 표준 event는 다음과 같다.

| Event | 설명 |
| --- | --- |
| ContextRefreshedEvent | ApplicationContext가 초기화된거나 refresh될 때 발생한다(refresh하기 위해서 ConfigurableApplicationContext interface의 refresh() 메소드를 사용한다). “초기화”라는 단어는, 모든 bean이 load되었고, post-processor bean이 탐지되어 활성화되었으며, singleton 객체가 선객체화되어, ApplicationContext 객체가 사용가능한 상태에 있다는 것을 의미한다. refresh는 context가 닫혀지지 않은 한, 여러번 발생할 수 있으며, ApplicationContext가 “hot” refresh를 지원해야한다 (XmlWebApplicationContext는 “hot” refresh를 지원하지만, GenericApplicationContext는 지원하지 않는다). |
| ContextStartedEvent | ApplicationContext가 시작될 때 발생한다(시작하기 위해서 ConfigurableApplicationContext interface의 start() 메소드를 사용한다). “시작됨(Started)“이란 단어는, 모든 Lifecycle bean이 명시적인 시작 신호를 받았음을 의미한다. 이 event는 일반적으로 명시적인 정지(stop) 후에, 재시작하기 위해서 사용되지만, 자동시작(autostart)로 설정되지 않은 컴포넌트를 시작하기 위해서도 사용된다 |
| ContextStoppedEvent | ApplicationContext가 정지할 때 발생한다(정지하기 위해서 ConfigurableApplicationContext interface의 stop() 메소드를 사용한다). “정지됨(Stopped)“란 단어는, 모든 Lifecycle bean이 명시적인 정지 신호를 받았음을 의미한다. 정지된 context는 start() 호출을 통해 재시작될 수 있다. |
| ContextClosedEvent | ApplicationContext가 닫혔을 때 발생한다(닫기 위해서 ConfigurableApplicationContext interface의 close() 메소드를 사용한다). “닫힘(Closed)“란 단어는, 모든 singleton bean이 파괴되었음을 의미한다. 닫힌 context는 생명주기의 끝에 도달한 것으로, refresh 되거나 재시작될 수 없다. |
| RequestHandledEvent | 웹에 특화된 event로서, HTTP request가 처리되었음을 알린다(request가 종료된 후에 발송된다). Spring의 DispatcherServlet를 사용하는 웹 어플리케이션인 경우에만 사용할 수 있다. |

 새로운 event를 구현하는 것도 어렵지 않다. ApplicationContext interface를 구현한 새로운 event 객체를 ApplicationContext의 publishEvent() 메소드를 통해 발행하면 된다. publishEvent() 메소드는 모든 listener가 event 처리를 마칠때까지 block 상태로 있게 된다. 게다가 transaction context가 가능하다면, listener가 event를 받았을 때, 발행모듈의 transaction context 내에서 event를 처리한다.

 아래는 예제이다.

 ```xml
<bean id="emailer" class="example.EmailBean">
    <property name="blackList">
        <list>
            <value>black@list.org</value>
            <value>white@list.org</value>
            <value>john@doe.org</value>
            </list>
    </property>
</bean>
 
<bean id="blackListListener" class="example.BlackListNotifier">
    <property name="notificationAddress" value="spam@list.org"/>
</bean>
```

 ```java
public class EmailBean implements ApplicationContextAware {
    private List blackList;
    private ApplicationContext ctx;
 
    public void setBlackList(List blackList) {
        this.blackList = blackList;
    }
 
    public void setApplicationContext(ApplicationContext ctx) {
        this.ctx = ctx;
    }
 
    public void sendEmail(String address, String text) {
        if (blackList.contains(address)) {
            BlackListEvent event = new BlackListEvent(address, text);
            ctx.publishEvent(event);
            return;
        }
        // send email...
    }
}
```

 ```java
public class BlackListNotifier implements ApplicationListener {
    private String notificationAddress;
 
    public void setNotificationAddress(String notificationAddress) {
        this.notificationAddress = notificationAddress;
    }
 
    public void onApplicationEvent(ApplicationEvent event) {
        if (event instanceof BlackListEvent) {
            // notify appropriate person...
        }
    }
}
```

### 웹 어플리케이션을 위한 편리한 ApplicationContext 객체화(Convenient ApplicationContext instantiation for web applications)

 BeanFactory가 프로그램적으로 생성되는 것과 반대로, ApplicationContext 객체는 ContextLoader 등을 사용하여 선언적으로 생성될 수 있다. 물론 ApplicationContext 객체 역시 프로그램적으로 생성할 수 있다.  
ContextLoader에는 ContextLoaderListener와 ContextLoaderServlet가 있다. 둘 다 기능적으로는 같지만, listener 버전은 Servlet 2.3 컨테이너에서는 사용할 수 있다.  
Servlet 2.4 스팩 이후로, servlet context listener는 웹 어플리케이션을 위한 servlet context가 생성되어 첫번째 요청을 처리할 상태가 된 직후 수행된다(그리고 servlet context가 막 종료되었을 때도 수행된다).  
따라서 servlet context listner가 Spring ApplicationContext를 초기화할 최적의 장소이다.  
ContextLoaderListener를 사용하여 ApplicationContext를 등록하는 방법은 아래와 같다.

 ```xml
<context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/daoContext.xml /WEB-INF/applicationContext.xml</param-value>
</context-param>
 
<listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
 
<!-- or use the ContextLoaderServlet instead of the above listener
<servlet>
    <servlet-name>context</servlet-name>
    <servlet-class>org.springframework.web.context.ContextLoaderServlet</servlet-class>
    <load-on-startup>1</load-on-startup>
</servlet>
-->
```

 Listener는 'contextConfigLocation' 파라미터를 검사한다. 만약 존재하지 않으면 기본적으로 /WEB-INF/applicationContext.xml를 사용할 것이다.  
만약 'contextConfigLocation' 파라미터 값이 존재할 경우, 미리 정해놓은 구분자(comma(','), semicolon(';'), 공백문자(whitespace))를 사용하여 파라미터 문자열을 분리한 후, application context를 찾을 것이다.  
Ant-style path 패턴이 지원된다. 예를 들어 /WEB-INF/*Context.xml'은 “WEB-INF” 디렉토리에 존재하는 “Context.xml”로 끝나는 이름을 가진 모든 파일을 의미하고, \\  
/WEB-INF/**/*Context.xml은 “WEB-INF” 디렉토리 및 하위 디렉토리에 존재하는 “Context.xml”로 끝나는 이름을 가진 모든 파일을 의미한다.

## 참고자료

- [Spring Framework - Reference Document / 1.15 Additional capabilities of the ApplicationContext](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#context-introduction)