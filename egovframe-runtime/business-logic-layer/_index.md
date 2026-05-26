---
title: 업무처리
linkTitle: 업무처리
description: 업무처리 서비스는 업무 프로그램의 업무 로직을 담당하는 서비스로 업무 흐름제어, 예외 처리 등의 기능을 제공한다. Spring Framework 6.2 기반의 Core(IoC, AOP), Web MVC, 예외 처리와 정합성을 유지한다.
url: /egovframe-runtime/business-logic-layer/
menu:
    depth:
        weight: 5
        parent: "egovframe-runtime"
        identifier: "business-logic-layer"
---
# 업무처리

업무처리 서비스는 업무 프로그램의 업무 로직을 담당하는 서비스로, **업무 흐름 제어**, **예외 처리** 등의 기능을 제공한다. 전자정부 표준프레임워크 업무처리 계층은 [Spring Framework 6.2](https://docs.spring.io/spring-framework/reference/6.2/index.html)를 기반으로 하며, 본 문서는 Spring Framework 6.2 Reference를 참고하여 구성하였다.

## 문서 구성

- **Exception Handling**: AOP 기반 예외 후처리(After throwing advice), Handler 패턴, Trace 처리. Spring Framework의 [AOP](https://docs.spring.io/spring-framework/reference/6.2/core/aop.html) 및 [Controller Advice](https://docs.spring.io/spring-framework/reference/6.2/web/webmvc/mvc-controller/ann-advice.html)와 연계하여 이해할 수 있다.
- **Spring Web Flow(SWF)**: 웹 애플리케이션 내 페이지 흐름(flow) 정의·수행. [Spring MVC](https://docs.spring.io/spring-framework/reference/6.2/web/webmvc.html)와의 통합, DispatcherServlet, Flow 설정, 뷰 렌더링, 액션 실행, Flow 상속 등.

## Spring Framework 6.2와의 관계

Spring Framework 6.2는 **Java 17+**을 요구하며, 다음 모듈들이 업무처리 계층과 관련이 있다.

- **Core**: [IoC 컨테이너](https://docs.spring.io/spring-framework/reference/6.2/core/beans.html), Bean, [의존성 주입](https://docs.spring.io/spring-framework/reference/6.2/core/beans/dependencies.html), **AOP**(관점 지향 프로그래밍). 예외 후처리 등 횡단 관심사는 Spring AOP(schema 기반 또는 @AspectJ)로 구현할 수 있다.
- **Web Servlet**: Spring MVC, DispatcherServlet, Annotated Controllers, **Controller Advice**(전역 예외 처리·모델/바인더 공통 설정). SWF는 Spring MVC 위에서 Flow를 핸들러로 동작시킨다.
- **Design Philosophy**: 설계 결정 지연, 다양한 관점 수용, 하위 호환성, API 설계·코드 품질 중시. 업무 로직과 인프라(예외 처리, 흐름 제어) 분리에 적용할 수 있다.

자세한 내용은 [Spring Framework 6.2 Documentation](https://docs.spring.io/spring-framework/reference/6.2/index.html) 및 [Overview](https://docs.spring.io/spring-framework/reference/6.2/overview.html)를 참고한다.