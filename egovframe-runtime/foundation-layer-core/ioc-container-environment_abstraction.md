---
title: Environment Abstraction
linkTitle: "Environment Abstraction"
description: Environment Abstraction은 Spring에서 프로파일과 속성을 관리하기 위한 `Environment` 인터페이스를 통해 애플리케이션 환경을 추상화하고 제어하는 기능이다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-enviroment_abstraction"
menu:
    depth:
        name: Environment Abstraction
        weight: 13
        parent: "ioc-container"
---
# Environment Abstraction

## 개요

 Environment Abstraction은 환경에 대한 추상화로 Spring에서 제공하는 Environment 인터페이스를 이용한다.  
Environment 인터페이스는 애플리케이션 환경의 두 가지 주요 측면을 모델링하는 컨테이너에 통합된 추상화로, profiles 나 properties처럼 프로그램의 환경 변수나 Application의 프로필을 관리할 때 사용하게 된다.

 Profile은 지정된 프로파일이 활성화된 경우에만 컨테이너에 등록되는 명명된 빈 정의의 논리적 그룹이다.  
Bean은 XML 또는 주석으로 정의된 프로필에 할당될 수 있다. 프로필과 관련된 환경 개체의 역할은 현재 활성화된 Profile(있는 경우)과 기본적으로 활성화되어야 하는 Profile(있는 경우)을 결정하는 것이다.

 Properties는 거의 모든 애플리케이션에서 중요한 역할을 하며 특성 파일, JVM 시스템 특성, 시스템 환경 변수, JNDI, 서블릿 컨텍스트 매개변수, 임시 특성 오브젝트, 맵 오브젝트 등 다양한 소스에서 생성될 수 있다.  
속성과 관련된 환경 개체의 역할은 사용자에게 속성 소스를 구성하고 속성을 해결하기 위한 편리한 서비스 인터페이스를 제공하는 것이다.

## 설명

### Bean 정의 Profile

 Bean 정의 프로파일은 아래와 같은 상황에서 코어 컨테이너에서 서로 다른 환경에서 서로 다른 Bean을 등록할 수 있는 메커니즘을 제공한다.

- QA 또는 생산 시 JNDI에서 동일한 데이터 소스를 조회하는 것과 개발 중인 메모리 내 데이터 소스에 대해 작업
- 애플리케이션을 성능 환경에 배포할 때만 모니터링 인프라를 등록
- 고객 A 대 고객 B 배치를 위한 Bean의 사용자 정의된 구현을 등록

#### @Profile 사용

 @Profile 어노테이션을 사용하면 하나 이상의 지정된 프로필이 활성 상태일 때 구성 요소가 등록에 적합함을 나타낼 수 있다. @Profile를 사용하여 아래와 같이 데이터소스를 구성할 수 있다.

 ```java
// standaloneDataSource는 development profile 에서만 사용
@Configuration
@Profile("development")
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
 
// jndiDataSource는 production profile 에서만 사용
@Configuration
@Profile("production")
public class JndiDataConfig {
    @Bean(destroyMethod="")
    public DataSource dataSource() throws Exception {
        Context ctx = new InitialContext();
        return (DataSource) ctx.lookup("java:comp/env/jdbc/datasource");
    }
}
```

#### XML Profile 설정

 XML &lt;bean/&gt; 에서 제공하는 profile 요소를 이용하여 Profile을 구성할 수 있다. 위의 데이터소스 예제를 아래와 같이 변경할 수 있다.

 ```xml
<beans profile="development"
    xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:jdbc="http://www.springframework.org/schema/jdbc"
    xsi:schemaLocation="...">
    <jdbc:embedded-database id="dataSource">
        <jdbc:script location="classpath:com/bank/config/sql/schema.sql"/>
        <jdbc:script location="classpath:com/bank/config/sql/test-data.sql"/>
    </jdbc:embedded-database>
</beans>
 
<beans profile="production"
    xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:jee="http://www.springframework.org/schema/jee"
    xsi:schemaLocation="...">
    <jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/datasource"/>
</beans>
```

 그리고, 아래와 같이 어떤 Profile을 활성화할지 설정할 수 있다.

 ```java
AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext();
ctx.getEnvironment().setActiveProfiles("development");
ctx.register(SomeConfig.class, StandaloneDataConfig.class, JndiDataConfig.class);
ctx.refresh();
```

### @PropertySource 사용

 @PropertySource 어노테이션은 PropertySource를 Spring의 환경에 추가하기 위한 편리하고 선언적인 메커니즘을 제공한다. testbean.name=myTestBean(키-값)을 포함하는 app.properties라는 파일이 주어지면 @Configuration 클래스는 testBean.getName()에 대한 호출이 myTestBean을 반환하는 방식으로 @PropertySource를 사용한다.

 ```java
@Configuration
@PropertySource("classpath:/com/myco/app.properties")
public class AppConfig {
 
    @Autowired
    Environment env;
 
    @Bean
    public TestBean testBean() {
        TestBean testBean = new TestBean();
        testBean.setName(env.getProperty("testbean.name"));
        return testBean;
    }
}
```

 이미 등록된 속성(예: 시스템 속성 또는 환경 변수)이 있는 경우 기본값과 함께 ${…} 자리 표시자에 기술할 수 있다. 기본값이 지정되지 않고 속성을 확인할 수 없는 경우는 IllegalArgumentException이 발생한다. 아래 예제는 my.placeholder 속성이 있는 경우 my.placeholder 속성값을 사용하고 없을 경우 기본값인 default/path를 사용하겠다고 기술한 것이다.

 ```java
@Configuration
@PropertySource("classpath:/com/${my.placeholder:default/path}/app.properties")
public class AppConfig {
 
    @Autowired
    Environment env;
 
    @Bean
    public TestBean testBean() {
        TestBean testBean = new TestBean();
        testBean.setName(env.getProperty("testbean.name"));
        return testBean;
    }
}
```

## 참고자료

- [Spring Framework - Reference Document / 1.13 Environment Abstraction](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-environment)