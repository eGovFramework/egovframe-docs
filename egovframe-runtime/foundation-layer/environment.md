---
title: Environment
linkTitle: "Environment"
description: 표준프레임워크 3.0부터 Spring 3.1의 Environment 인터페이스를 통해 Profile과 Property에 접근할 수 있다.
url: /egovframe-runtime/foundation-layer/environment/
menu:
    depth:
        name: Environment
        weight: 7
        parent: "foundation-layer"
---
# Environment

## 개요

표준프레임워크 3.0부터는 (Spring 3.1부터) Environment interface를 제공한다.

Environment는 다음 기능의 접근을 제공한다.

- Profile
- Property

Environment는 ApplicationContext를 통해서 접근이 가능하며 다음과 같이 가져올 수 있다.

```java
ApplicationContext ctx = new GenericApplicationContext();
Environment env = ctx.getEnvironment();
```

### Profile 접근

- [Profile에 대한 자세한 설명](../foundation-layer-core/ioc-container-bean-definition-profiles.md)

Profile은 등록할 bean들이 정의되어있는 논리적인 그룹을 말한다. Bean은 XML또는 Annotation을 통해 정의된 Profile값 중 활성화된 Profile로 할당된다.
이 때 현재 사용하는 Profile을 활성화하는 것이 바로 Environment의 역할이다. 또한 Profile은 default값으로 설정이 되어있어야 한다.

Spring에서 Profile을 활성화 할 때 내부에서 Environment를 쓰고 있으며 활성화하는 방법은 코드상 변환, 명시적 설정, Annotation설정 등이 있다.

Environment를 이용하여 다음과 같이 사용할 경우 Profile이 dev로 정의되어있는 bean들이 활성화된다.

```java
GenericXmlApplicationContext ctx = new GenericXmlApplicationContext();
ctx.getEnvironment().setActiveProfiles("dev");
ctx.load("classpath:/com/bank/config/xml/*-config.xml");
ctx.refresh();
```

혹은 여러 개의 프로파일을 활성화 시킬 수도 있다.

```java
ctx.getEnvironment().setActiveProfiles("profile1", "profile2");
```

web.xml의 servlet 설정에서 다음과 같이 명시적으로 쓸 수도 있다. 다음의 경우 profile이 production으로 정의되어있는 bean들이 활성화된다.

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

### Property 접근

Environment abstract에서는 PropertySource의 계층구조를 통해 통합검색 기능을 지원하고 있다.

다음은 Environment를 통해 PropertySource에 접근할 수 있는 예를 보여준다.

```java
ApplicationContext ctx = new GenericApplicationContext();
Environment env = ctx.getEnvironment();
boolean containsFoo = env.containsProperty("foo");
System.out.println("Does my environment contain the 'foo' property? " + containsFoo);
```

PropertySource에서는 key-value쌍의 속성값에 접근할 수 있도록 기능을 제공하며 기본(default) Environment에는 두 개의 PropertySource객체로 구성되어있다.

- JVM 시스템 Properties (JVM system properties)
- 시스템 환경변수 (Systen environment variables)

Environment에서 PropertySource를 Hierarchical(계층구조)의 우선순위대로 검색한다.
위의 default environment에서 JVM 시스템 properties가 시스템 환경변수보다 우선순위가 높으므로 JVM 시스템 Properties에서 검색을 하고 다음 시스템 환경변수에서 Property값을 찾을 것이다.

위의 두 기본 PropertySource외에 사용자 정의 PropertySource를 만들 수 있다.

다음은 사용자가 정의한 MyPropertySource를 Environment의 Hierarchical PropertySource에 추가하기 위한 코드이다.

```java
ConfigurableApplicationContext ctx = new GenericApplicationContext();
MutablePropertySources sources = ctx.getEnvironment().getPropertySources();
sources.addFirst(new MyPropertySource());
```

위의 코드에서 MyPropertySource는 가장 높은 우선순위로 Environment에 추가된다.
만약 이전 코드와 같이 “foo”의 Property값을 가져오는 경우, MyPropertySource에 값이 있다면 그 값이 반환될 것이다.