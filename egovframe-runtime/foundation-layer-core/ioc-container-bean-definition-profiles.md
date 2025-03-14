---
title: "Bean Definition Profiles"
linkTitle: "Profiles"
description: Spring Framework 3.1부터 추가된 Bean의 Profile은 동일한 id의 bean을 여러 개 정의하고, 활성화된 Profile에 따라 해당 bean이 Runtime 시에 동작하도록 하는 기능이다. 주로 개발 환경과 운영 환경에서 Profile 설정을 변경해 Spring Container에서 서로 다른 Bean을 적용하는 데 사용된다. Profile을 설정할 때는 반드시 활성화해야 하며, 활성화하지 않으면 `NoSuchBeanDefinitionException`이 발생한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-bean-definition-profiles/"
menu:
    depth:
        name: Profiles
        weight: 5
        parent: "ioc-container"
---
# Bean Definition Profiles

## 개요

Bean의 Profile은 Spring f/w ver. 3.1부터 추가되었으며 동일한 id의 bean을 여러 개 정의하여 사용자의 설정으로 활성화시킨 Profile의 해당 bean이 Runtime시에 동작하도록 하는 기능이다. 보통 개발시점과 운영시점에 bean의 Profile설정 변경만으로 Spring Container에서 Bean적용이 달리 적용되도록 하는데 쓰인다.

Profile설정 시, 반드시 Profile을 활성화해야만 사용가능하다. 만약 Profile만 설정하고 활성화하지 않으면 Exeption(NoSuchBeanDefinitionException)이 발생한다.

## 설명

아래에서 Profile을 설정하는 방법과 Profile을 활성화(Active Profile)하는 방법에 대하여 알아본다.

### Profile 설정 방법

Profile의 설정방법에는 XML설정과 Annotation설정으로 나뉜다.

#### XML Profile설정

기존의 전형적인 XML Bean설정에 대하여 알아보고 새로 추가된 Profiles설정에 대하여 살펴본다. 동일한 Bean id를 Profile별로 XML에 설정하는 방법에는 XML을 나누는 방법, 하나의 XML에서 관리하는 방법이 있다

##### A typical XML Configuration

기존에는 Bean id설정은 반드시 유일해야 하며 Bean설정을 변경하기 위해서는 다른 id를 가진 Bean을 새로 설정하거나 동일 Bean의 내부설정을 변경해주어야했다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:jdbc="http://www.springframework.org/schema/jdbc"
    xsi:schemaLocation="...">
 
    <bean id="transferService" class="com.bank.service.internal.DefaultTransferService">
        <constructor-arg ref="accountRepository"/>
        <constructor-arg ref="feePolicy"/>
    </bean>
 
    <bean id="accountRepository" class="com.bank.repository.internal.JdbcAccountRepository">
        <constructor-arg ref="dataSource"/>
    </bean>
 
    <bean id="feePolicy" class="com.bank.service.internal.ZeroFeePolicy"/>
 
    <jdbc:embedded-database id="dataSource">
        <jdbc:script location="classpath:com/bank/config/sql/schema.sql"/>
        <jdbc:script location="classpath:com/bank/config/sql/test-data.sql"/>
    </jdbc:embedded-database>
</beans>
```

**1. Bean Profiles - Xml을 분리하여 설정하는 방법**

\<transfer-service-config.xml>

아래는 "dataSource" bean을 사용하는 "accountRepository" bean 설정한 XML이다. 어떤 Profile의 bean인지 여부와 상관없이 Spring container기동시점에는 dataSource라는 bean id를 가진 유일한 bean을 가져오기 때문에 이전 설정과 똑같이 bean id값만 쓰면 된다.

```xml
<beans ...>
    <bean id="transferService" ... />
 
    <bean id="accountRepository" class="com.bank.repository.internal.JdbcAccountRepository">
        <constructor-arg ref="dataSource"/>
    </bean>
 
    <bean id="feePolicy" ... />
</beans>
```

\<standalone-datasource-config.xml>

개발시점에 사용하는 "dataSource" bean을 정의하는 XML. Profile명은 "dev"로 정의하고 있으며 Embedded DB를 DataSource로 설정하고 있다. "dev" Profile을 활성화시키면 해당Bean이 동작한다.

```xml
<beans profile="dev">
    <jdbc:embedded-database id="dataSource">
        <jdbc:script location="classpath:com/bank/config/sql/schema.sql"/>
        <jdbc:script location="classpath:com/bank/config/sql/test-data.sql"/>
    </jdbc:embedded-database>
</beans>
```

\<jndi-datasource-config.xml>

운영시점에 사용하는 "dataSource" bean을 정의하는 XML. Profile명은 "production"으로 정의하고 있으며 JDNI를 DataSource로 설정하고 있다. "production" Profile을 활성화시키면 해당 Bean이 동작한다.

```xml
<beans profile="production">
    <jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/datasource"/>
</beans>
```

**2. Bean Profiles - XML을 한 파일에서 설정**
 
\<beans> element를 하나의 XML파일에서 profile값과 함께 여러 번 정의할 수도 있다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:jdbc="http://www.springframework.org/schema/jdbc"
    xmlns:jee="http://www.springframework.org/schema/jee"
    xsi:schemaLocation="...">
 
    <bean id="transferService" class="com.bank.service.internal.DefaultTransferService">
        <constructor-arg ref="accountRepository"/>
        <constructor-arg ref="feePolicy"/>
    </bean>
 
    <bean id="accountRepository" class="com.bank.repository.internal.JdbcAccountRepository">
        <constructor-arg ref="dataSource"/>
    </bean>
    <bean id="feePolicy" class="com.bank.service.internal.ZeroFeePolicy"/>
    <beans profile="dev">
        <jdbc:embedded-database id="dataSource">
            <jdbc:script location="classpath:com/bank/config/sql/schema.sql"/>
            <jdbc:script location="classpath:com/bank/config/sql/test-data.sql"/>
        </jdbc:embedded-database>
    </beans>
    <beans profile="production">
        <jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/datasource"/>
    </beans>
</beans>
```
#### Annotation Profile설정

Profile의 Annotation설정은 @Profile을 통해서 설정 가능하다. @Configuration과 함께 @Profile("Profile명")을 클래스에 쓰게 되면 내부 메소드에 붙은 @Bean을 통해 Bean들이 등록된다.

기존 @Configuration class에 대하여 살펴보고 @Profile을 통해 Bean을 설정하는 방법에 대하여 살펴본다.

##### A typical @Configuration Class

Class위에 @Configuration을 붙이면 @Bean과 함께 정의한 메소드 명이 bean id로 등록된다.

```java
@Configuration
public class TransferServiceConfig {
 
    @Bean
    public TransferService transferService() {
        return new DefaultTransferService(accountRepository(), feePolicy());
    }
 
    @Bean
    public AccountRepository accountRepository() {
        return new JdbcAccountRepository(dataSource());
    }
 
    @Bean
    public FeePolicy feePolicy() {
        return new ZeroFeePolicy();
    }
 
    @Bean
    public DataSource dataSource() {
        return new EmbeddedDatabaseBuilder()
            .setType(EmbeddedDatabaseType.HSQL)
            .addScript("classpath:com/bank/config/sql/schema.sql")
            .addScript("classpath:com/bank/config/sql/test-data.sql")
            .build();
    }
}
```

##### @Profile 설정

위에서 살펴봤던 Bean Profile XML 설정을 Annotation(@Profile)으로 설정하면 다음과 같다. @Profile은 XML의 beans profile의 설정과 똑같이 동작하며 @Bean은 XML의 bean설정과 매칭된다.

다음은 "dev" Profile을 정의했을 때의 Java코드이다. Profile명이 dev인 "dataSource" Bean을 정의하고 있다.

```java
@Configuration
@Profile("dev")
public class StandaloneDataConfig {
    @Bean
    public DataSource dataSource() {
        return new EmbeddedDatabaseBuilder()
            .setType(EmbeddedDatabaseType.HSQL)
            .addScript("classpath:com/bank/config/sql/schema.sql")
            .addScript("classpath:com/bank/config/sql/test-data.sql")
            .build();
    }
}
```

다음은 "production" Profile을 정의했을 때의 Java코드이다. Profile명이 production인 "dataSource" Bean을 정의하고 있다.

```java
@Configuration
@Profile("production")
public class JndiDataConfig {
 
    @Bean
    public DataSource dataSource() throws Exception {
        Context ctx = new InitialContext();
        return (DataSource) ctx.lookup("java:comp/env/jdbc/datasource");
    }
}
```

### Profile 활성화 (Active Profile)

설정한 Profile을 활성화 하는 방법에는 선언적인 Profile활성화, Java코드를 통한 Profile활성화가 있다.

#### 1. 선언적인 Profile 활성화(web.xml, 환경변수, 프로퍼티 등..)

web.xml 또는 JVM실행 시 환경변수, Property값 등으로 Profile을 활성화시킬 수 있다. Java코드를 통해서도 가능하나 실행환경이 war파일로 제공되거나 배포시점의 경우에는 관리의 불편함이 있으므로 web.xml을 통한 Profile활성화를 추천한다.

\<web.xml로 Profile활성화>

```xml
<servlet>
      <servlet-name>dispatcher</servlet-name>
      <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
      <init-param>
          <param-name>spring.profiles.active</param-name>
          <param-value>production</param-value>
      </init-param>
  </servlet>
```

\<JVM실행 시 환경변수로 Profile활성화>

```java
java -Dspring.profiles.active="production"
```

#### 2. Java 코드를 통한 Profile 활성화

Spring 3.1부터 Environment라는 인터페이스를 통해서 해당프로파일을 활성화시킬 수 있다.

\<XML로 profile을 설정한 경우, Java코드로 Profile활성화> Profile명이 dev로 설정되어있는 bean을 활성화시킨다. GenericXmlApplicationContext에서 가져온 Environment를 통해 setActiveProfiles메소드로 Profile을 활성화시키고 해당 configuration xml을 로딩한다.

다음 예시에서는 Profile명이 production로 설정되어있는 bean이 활성화되며 Profile명이 dev으로 설정되어있는 bean은 Skip된다.

```java
GenericXmlApplicationContext ctx = new GenericXmlApplicationContext();
ctx.getEnvironment().setActiveProfiles("production");
ctx.load("classpath:/com/bank/config/xml/*-config.xml");
ctx.refresh();
```

\<@Profile로 Profile을 설정한 경우, Java코드로 Profile활성화 > 활성화하고자하는 Profile명을 setActiveProfiles메소드로 활성화시키고 "com.bank.config.code"패키지 내의 모든 @Configuration class를 스캔한다. Profile이 dev로 설정되어있는 bean이 활성화되며 Profile이 Production으로 설정되어있는 bean은 Skip된다.

```java
AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext();
ctx.getEnvironment().setActiveProfiles("dev");
ctx.scan("com.bank.config.code"); // find and register all @Configuration classes within
ctx.refresh();
```

#### 3. JUnit4테스트의 @ActiveProfile 어노테이션을 통한 Profile활성화

JUnit4에서 Test class에 @ActiveProfile을 붙임으로써 Profile활성화가 가능하다. @ContextConfiguration과 함께 쓰며, @ActiveProfile뒤에 Profile명을 붙이면 해당 Profile이 활성화된다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(loader=AnnotationConfigContextLoader.class)
@ActiveProfiles("annotationProfile")
public class SpringAnnotationProfileTest {
}
```

## 참고자료

- [Spring Framework - Reference Document / 3.2 Bean Definition Profiles](http://docs.spring.io/spring/docs/3.2.6.RELEASE/spring-framework-reference/htmlsingle/#new-in-3.1-bean-definition-profiles)
- [Spring team blog - XML profiles](http://spring.io/blog/2011/02/11/spring-framework-3-1-m1-released/)
- [Spring team blog - introducing @Profile](http://spring.io/blog/2011/02/14/spring-3-1-m1-introducing-profile/)