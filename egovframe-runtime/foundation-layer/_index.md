---
title: 공통기반
linkTitle: 공통기반
description: 공통기반 서비스는 실행환경 서비스 간에 공통적으로 사용되는 기능을 제공한다. Spring Framework 6.2 기반의 Core(IoC, Resources, SpEL), Data Access, Web, Integration과 정합성을 유지한다.
url: /egovframe-runtime/foundation-layer/
menu:
    depth:
        weight: 3
        parent: "egovframe-runtime"
        identifier: "foundation-layer"
---
# 공통기반

공통기반 서비스는 실행환경 서비스 간에 공통적으로 사용되는 기능을 제공한다. 전자정부 표준프레임워크 공통기반 계층은 [Spring Framework 6.2](https://docs.spring.io/spring-framework/reference/6.2/index.html)를 기반으로 하며, 본 문서는 Spring Framework 6.2 Reference를 참고하여 구성하였다.

## Spring Framework 6.2와의 관계

Spring Framework 6.2 문서 구조에 대응하는 공통기반 항목은 다음과 같다.

- **Core**: [IoC 컨테이너](https://docs.spring.io/spring-framework/reference/6.2/core/beans.html), Bean, [의존성 주입](https://docs.spring.io/spring-framework/reference/6.2/core/beans/dependencies.html), **Resources**, **Validation/Data Binding/Type Conversion**, **SpEL**, AOP. 공통기반의 환경(Environment), 프로퍼티(Property), 문자열 유틸 등은 Core 및 [Environment Abstraction](https://docs.spring.io/spring-framework/reference/6.2/core/environment.html)과 연관된다.
- **Data Access**: 트랜잭션, JDBC, ORM. 공통기반의 DB 기반 보안·ID 생성 등은 Data Access 계층과 연동된다.
- **Web Servlet**: Spring MVC, **Multipart**(파일 업로드), 필터, 뷰 기술. 공통기반의 파일 업로드/다운로드 서비스는 [Multipart Resolver](https://docs.spring.io/spring-framework/reference/6.2/web/webmvc/mvc-controller/multipart.html) 및 HTTP 메시지 변환과 연관된다.
- **Integration**: **Task Execution and Scheduling**, **Cache Abstraction**, JMS, JMX, Email 등. 공통기반의 [Scheduling](./scheduling.md), [Cache](./cache.md) 서비스는 [Task Execution and Scheduling](https://docs.spring.io/spring-framework/reference/6.2/integration/scheduling.html), [Cache Abstraction](https://docs.spring.io/spring-framework/reference/6.2/integration/cache.html)과 정합성을 유지한다.

**Server Security**는 Spring Security 프로젝트를 확장한 것이며, Spring Framework 6.2의 Web 보안·필터 체인과 함께 동작한다. 자세한 내용은 각 하위 문서 및 [Spring Framework 6.2 Documentation](https://docs.spring.io/spring-framework/reference/6.2/index.html), [Overview](https://docs.spring.io/spring-framework/reference/6.2/overview.html)를 참고한다.