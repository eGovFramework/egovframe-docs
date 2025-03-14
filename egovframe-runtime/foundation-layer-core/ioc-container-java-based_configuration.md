---
title: "Java-based Configuration"
linkTitle: "JavaConfig"
description: Java-based Configuration은 XML 대신 Java 코드를 사용하여 Spring 빈과 애플리케이션 설정을 구성하는 방법이다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-java-based_configuration/"
menu:
    depth:
        name: JavaConfig
        weight: 12
        parent: "ioc-container"
---
# Java-based configuration

## 개요

 Java 코드에서 주석을 사용하여 스프링 컨테이너를 구성하는 방법에 대해 알아본다.

## 설명

### 기본 개념 : @Bean, @Configurationl

 스프링의 자바 기반 설정에서는 @Configuration 어노테이션 클래스와 @Bean 어노테이션 메소드를 지원한다.  
@Bean 어노테이션은 Spring IoC 컨테이너가 관리할 새로운 객체를 인스턴스화하고, 초기화하는데 사용되며, Spring의 XML 설정에서의 &lt;bean/&gt;과 같은 역할을 한다.  
@Bean 어노테이션은 붙인 메소드는 스프링 @Component와 함께 사용할 수 있지만, 대체로 @Configuration Bean과 사용한다.  
@Configuration 어노테이션은 해당 클래스의 목적이 Bean 설정을 위한 소스임을 나타내며, @Configuration 클래스는 같은 클래스 안에 있는 @Bean 메소드들끼리 서로를 호출하여 Bean 사이의 의존성을 정의할 수 있게 한다.  
@Configuration 클래스를 아래와 같이 구성할 수 있다.

 ```java
@Configuration
public class AppConfig {
    @Bean
    public MyService myService() {
        return new MyServiceImpl();
    }
}
```

 예제의 AppConfig 클래스는 아래의 Spring &lt;bean/&gt; XML과 동일한 역할을 한다.

 ```xml
<beans>
    <bean id="myService" class="com.acme.services.MyServiceImpl"/>
</beans>
```

### AnnotationConfigApplicationContext를 이용한 스프링 컨테이너 인스턴스화

 AnnotationConfigApplicationContext는 다재다능한 ApplicationContext 구현체로, 입력으로 @Configuration 클래스뿐만 아니라 평범한 @Component 클래스와 JSR-330 메타데이터로 어노테이션이 붙은 클래스들도 받아들일 수 있다.  
@Configuration 클래스가 입력으로 제공되면 @Configuration 클래스 자체가 Bean 정의로 등록되고, 해당 클래스내의 선언된 모든 @Bean 메서드들도 Bean 정의로 등록된다.  
@Component와 JSR-330 클래스들이 제공되면 이 클래스들은 Bean 정의로 등록되고 해당 클래스내에서 필요한 곳에 @Autowired나 @Inject 같은 DI 메타데이터가 사용되었다고 가정한다.

#### 간단한 구성

 ClassPathXmlApplicationContext를 인스턴스화 할 때 스프링 XML 파일을 사용하는 방법과 거의 동일하게 AnnotationConfigApplicationContext를 인스턴스화 할 때 @Configuration 클래스들을 입력으로 사용할 것이다.  
이를 통해 전혀 XML을 사용하지 않고 스프링 컨테이너를 사용할 수 있다.

 ```java
public static void main(String[] args) {
    ApplicationContext ctx = new AnnotationConfigApplicationContext(AppConfig.class);
    MyService myService = ctx.getBean(MyService.class);
    myService.doStuff();
}
```

#### register(Class<?>...)로 프로그래밍 방식으로 컨테이너 빌드

 인수 없는 생성자를 사용하여 AnnotationConfigApplicationContext를 인스턴스화한 다음 register() 메서드를 사용하여 구성할 수 있다.  
이 접근 방식은 AnnotationConfigApplicationContext를 프로그래밍 방식으로 빌드할 때 특히 유용하며 아래와 같이 사용할 수 있다.

 ```java
public static void main(String[] args) {
    AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext();
    ctx.register(AppConfig.class, OtherConfig.class);
    ctx.register(AdditionalConfig.class);
    ctx.refresh();
    MyService myService = ctx.getBean(MyService.class);
    myService.doStuff();
}
```

#### scan(String...)으로 컴포넌트 스캔

 @Configuration구성 요소 스캔을 활성화하려면 다음과 같이 구성할 수 있다.

 ```java
@Configuration
@ComponentScan(basePackages = "com.acme") // 구성요소 스캔을 활성화함
public class AppConfig  {
    // ...
}
```

 경험있는 스프링 사용자들은 다음과 같이 일반적으로 사용되는 스프링의 context: 네임스페이스로 XML을 선언하는데 익숙할 것이다.

 ```xml
<beans>
    <context:component-scan base-package="com.acme"/>
</beans>
```

 위의 예제에서 com.acme 팩키지는 스캔되고 @Component 어노테이션이 붙은 클래스들을 찾고 이러한 클래스를 컨테이너내 스프링 빈 정의로 등록할 것이다.  
AnnotationConfigApplicationContext에는 같은 컴포넌트 스캔 기능을 하는 scan(String…) 메서드가 있다.

 ```java
public static void main(String[] args) {
    AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext();
    ctx.scan("com.acme");
    ctx.refresh();
    MyService myService = ctx.getBean(MyService.class);
}
```

#### AnnotationConfigWebApplicationContext를 사용한 웹 어플리케이션 지원

 AnnotationConfigApplicationContext의 WebApplicationContext 변형은 AnnotationConfigWebApplicationContext로 사용할 수 있다.  
이 구현체는 스프링 ContextLoaderListener 서블릿 리스너, 스프링 MVC DispatcherServlet 등을 설정할 때 사용할 수 있다.  
아래는 전형적인 스프링 MVC 웹 어플리케이션을 설정하는 web.xml의 예제로 contextClass context-param과 init-param의 사용방법을 보여준다.

 ```xml
<web-app>
    <!-- 기본 XmlWebApplicationContext 대신 AnnotationConfigWebApplicationContext를 사용하는 ContextLoaderListener를 설정한다. -->
    <context-param>
        <param-name>contextClass</param-name>
        <param-value>
            org.springframework.web.context.support.AnnotationConfigWebApplicationContext
        </param-value>
    </context-param>
 
    <!-- 설정 위치는 반드시 콤마나 공백을 구분자로 사용하는 하나 이상의 정규화된 @Configuration 클래스들로 구성되어야 한다. 정규화된 패키지는 컴포넌트 스캔으로 지정될 수도 있다. -->
    <context-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>com.acme.AppConfig</param-value>
    </context-param>
 
    <!-- ContextLoaderListener를 사용해서 루트 어플리케이션 시작한다. -->
    <listener>
        <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
    </listener>
 
    <!-- Spring MVC DispatcherServlet 시작 -->
    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <!-- 기본 XmlWebApplicationContext 대신 AnnotationConfigWebApplicationContext를 사용한 DispatcherServlet 설정한다. -->
        <init-param>
            <param-name>contextClass</param-name>
            <param-value>
                org.springframework.web.context.support.AnnotationConfigWebApplicationContext
            </param-value>
        </init-param>
        <!-- 다시한번, 설정 위치는 반드시 콤마나 공백을 구분자로 사용하는 하나 이상의 정규화된 @Configuration 클래스들로 구성되어야 한다. -->
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>com.acme.web.MvcConfig</param-value>
        </init-param>
    </servlet>
 
    <!-- /app/*에 대한 모든 요청을 디스패쳐 서블릿에 매핑한다. -->
    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/app/*</url-pattern>
    </servlet-mapping>
</web-app>
```

### @Bean 어노테이션 사용

 @Bean은 메소드 레벨 어노테이션이며 XML &lt;bean/&gt; 요소와 동일하며 &lt;bean/&gt;에서 제공하는 일부 속성을 지원한다. 또한, @Configuration 어노테이션 또는 @Component 어노테이션 클래스에서 @Bean 어노테이션을 사용할 수 있다.

#### Bean 선언

 메소드에 @Bean 어노테이션을 사용하면 Bean으로 선언된다. 이 메서드를 사용하여 메서드의 반환 값으로 지정된 유형의 ApplicationContext 내에 Bean 정의를 등록되며 Bean 이름은 메서드 이름과 동일하다.  
다음 예제에서 @Bean 메소드 선언을 확인할 수 있다.

 ```java
@Configuration
public class AppConfig {
    @Bean
    public TransferServiceImpl transferService() {
        return new TransferServiceImpl();
    }
}
```

 위 예제는 다음 Spring XML과 정확히 동일하다.

 ```xml
<beans>
    <bean id="transferService" class="com.acme.TransferServiceImpl"/>
</beans>
```

#### Bean 종속성

 @Bean 어노테이션 메서드는 해당 Bean을 빌드하는 데 필요한 종속성을 설명하는 임의 개수의 매개변수를 가질 수 있다.  
예를 들어 TransferService에 AccountRepository가 필요한 경우 다음 예제와 같이 메서드 매개 변수를 사용하여 해당 종속성을 구체화할 수 있다.

 ```java
@Configuration
public class AppConfig {
    @Bean
    public TransferService transferService(AccountRepository accountRepository) {
        return new TransferServiceImpl(accountRepository);
    }
}
```

#### @Scope 어노테이션 사용

 @Bean 어노테이션으로 정의된 Bean이 특정 범위를 갖도록 지정할 수 있으며, 선언된 Bean의 범위는 [Bean scope](./ioc-container-bean_scope.md)에 지정된 표준 범위를 사용할 수 있다.
기본 범위는 싱글톤이지만 다음 예제와 같이 @Scope 어노테이션으로 이를 재정의할 수 있다.

 ```java
@Configuration
public class MyConfiguration {
    @Bean
    @Scope("prototype")
    public Encryptor encryptor() {
        // ...
    }
}
```

### @Configuration 어노테이션 사용

 @Configuration은 객체가 Bean 정의의 소스임을 나타내는 클래스 수준 어노테이션이며 @Configuration 클래스는 @Bean 어노테이션 메서드를 통해 빈을 선언한다.  
@Configuration 클래스의 @Bean 메소드에 대한 호출은 bean 간 종속성을 정의하는 데에도 사용할 수 있다.

 ```java
@Configuration
public class AppConfig {
    @Bean
    public BeanOne beanOne() {
        return new BeanOne(beanTwo());
    }
 
    @Bean
    public BeanTwo beanTwo() {
        return new BeanTwo();
    }
}
```

### Java 기반 설정 구성

 Spring의 Java 기반 설정 기능을 사용하면 구성의 복잡성을 줄일 수 있는 어노테이션을 작성할 수 있다.

#### @Import 어노테이션 사용

 스프링 XML 파일에서 설정 모듈화에 &lt;import/&gt;요소를 사용하기는 하지만 @Import 어노테이션은 다른 설정 클래스에서 @Bean 설정을 로딩한다.

 ```java
@Configuration
public class ConfigA {
    @Bean
    public A a() {
        return new A();
    }
}
 
@Configuration
@Import(ConfigA.class)
public class ConfigB {
    @Bean
    public B b() {
        return new B();
    }
}
```

 이제 컨텍스트를 인스턴스화 할 때 ConfigA.class와 ConfigB.class를 둘 다 지정해야하는 대신 ConfigB만 명시적으로 제공하면 된다.

 ```java
public static void main(String[] args) {
    ApplicationContext ctx = new AnnotationConfigApplicationContext(ConfigB.class);
 
    // now both beans A and B will be available...
    A a = ctx.getBean(A.class);
    B b = ctx.getBean(B.class);
}
```

 이 접근방식은 설정을 구성하는 동안 잠재적으로 많은 수의 @Configuration 클래스들을 기억해야 하는 대신 하나의 클래스만 다루면 되므로 컨테이너 인스턴스화를 단순화한다.

#### 임포트한 @Bean 정의에 의존성 주입

 위의 예제는 작동하지만 단순하다. 대부분의 실제 시나리오에서 Bean은 다른 설정 클래스들에 대한 의존성을 가지게 된다.  
XML을 사용할 때 컴파일러가 관여하지 않고 그냥 ref=“someBean”만 선언한 뒤 스프링이 컨테이너를 인스턴스화 하면 제대로 동작하기를 믿으면 되기 때문에 의존성 자체는 이슈가 아니었다.  
@Configuration를 사용할 때 자바 컴파일러는 다른 빈에 대한 참조는 유효한 자바문법이어야 한다는 제약을 설정 모델에 둔다.

 다행히도 이 문제를 해결하는 것은 간단하다. 이미 논의한 것처럼 @Bean 메소드는 Bean 종속성을 설명하는 임의의 수의 매개변수를 가질 수 있다.  
각각 다른 클래스에서 선언된 Bean에 따라 여러 @Configuration 클래스가 있는 다음과 같이 구성할 수 있다.

 ```java
@Configuration
public class ServiceConfig {
    @Bean
    public TransferService transferService(AccountRepository accountRepository) {
        return new TransferServiceImpl(accountRepository);
    }
}
 
@Configuration
public class RepositoryConfig {
    @Bean
    public AccountRepository accountRepository(DataSource dataSource) {
        return new JdbcAccountRepository(dataSource);
    }
}
 
@Configuration
@Import({ServiceConfig.class, RepositoryConfig.class})
public class SystemTestConfig {
    @Bean
    public DataSource dataSource() {
        // return new DataSource
    }
}
 
public static void main(String[] args) {
    ApplicationContext ctx = new AnnotationConfigApplicationContext(SystemTestConfig.class);
    // everything wires up across configuration classes...
    TransferService transferService = ctx.getBean(TransferService.class);
    transferService.transfer(100.00, "A123", "C456");
}
```

## 참고자료

- [Spring Framework - Reference Document / 1.12. Java-based Container Configuration](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-java)