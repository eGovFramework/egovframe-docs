---
title: 공통기반 핵심
linkTitle: 공통기반 핵심
description: Spring IoC Container, AOP, Resources, SpEL 등 Spring Framework 6.2 Core Technologies를 기반으로 한 공통기반 핵심 서비스를 다룬다.
url: /egovframe-runtime/foundation-layer-core/
menu:
    depth:
        name: 공통기반 핵심
        weight: 2
        parent: "egovframe-runtime"
        identifier: "foundation-layer-core"
---
# 공통기반 핵심

공통기반 핵심 서비스는 [Spring Framework 6.2 - Core Technologies](https://docs.spring.io/spring-framework/reference/6.2/core.html)를 기반으로 하며, 본 문서는 Spring Framework 6.2 Reference를 참고하여 구성하였다.

## 문서 구성

- **IoC Container**: 객체(빈) 관리, 의존성 주입(DI), Bean 스코프·생명주기·정의 상속, 컨테이너 확장점, ApplicationContext. [The IoC Container](https://docs.spring.io/spring-framework/reference/6.2/core/beans.html) 및 [Introduction to the Spring IoC Container and Beans](https://docs.spring.io/spring-framework/reference/6.2/core/beans/introduction.html) 하위 장과 대응한다.
- **Annotation-based / Java-based Configuration**: @Autowired, @Bean, @Configuration, 클래스패스 스캔, JSR 330, Environment 추상화.
- **Resources**: 리소스 추상화를 통한 메시지·설정 파일 접근. [Spring Framework 6.2 - Resources](https://docs.spring.io/spring-framework/reference/6.2/core/resources.html).
- **SpEL**: Spring Expression Language. [Spring Framework 6.2 - SpEL](https://docs.spring.io/spring-framework/reference/6.2/core/expressions.html).
- **AOP**: 관점 지향 프로그래밍, schema 기반 AOP, @AspectJ. [Spring Framework 6.2 - AOP](https://docs.spring.io/spring-framework/reference/6.2/core/aop.html).

Spring Framework 6.2는 **Java 17+**을 요구하며, IoC 컨테이너와 AOP는 Spring의 핵심 기술로 문서화되어 있다. 자세한 내용은 [Spring Framework 6.2 Documentation](https://docs.spring.io/spring-framework/reference/6.2/index.html) 및 [Core Technologies](https://docs.spring.io/spring-framework/reference/6.2/core.html)를 참고한다.
