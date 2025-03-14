---
title: Spring Web Flow(SWF) 개요
linkTitle: Spring Web Flow
description: Spring Web Flow는 웹 애플리케이션 내에서 논리적 페이지 흐름을 정의하고 수행하는 컴포넌트로, 단일 사용자의 대화를 비즈니스 프로세스와 함께 구현하여 안내한다. SWF는 Struts, Spring MVC 등과 통합되어 자족적인 페이지 흐름 엔진으로 작동하며, 선언적이고 관리하기 쉬운 방식으로 애플리케이션 흐름을 정의할 수 있다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/
menu:
    depth:
        name: Spring Web Flow
        weight: 2
        parent: "business-logic-layer"
        identifier: "spring-web-flow"
---
# Spring Web Flow


## 개요
Spring Web Flow(SWF)는 웹 애플리케이션 내 페이지 흐름(flow)의 정의와 수행에 집중하는 Spring 프레임워크 웹 스택의 컴포넌트이다.

시스템은 다른 위치에서 재사용될 수 있는 자족적 모듈처럼 웹 애플리케이션의 논리적 흐름(flow)을 획득하는 것을 허용한다.<br>
이러한 흐름(flow)은 비즈니스 프로세스의 구현을 통해 단일 사용자를 안내하고 단일 사용자 대화를 표현한다.<br>
흐름(flow)은 종종 HTTP 요청을 처리하고 상태를 가지며, 트랜잭션 특성을 보이고 동적이고/이거나 장시간 구동될 수 있다.

Spring Web Flow는 추상화의 좀 더 높은 레벨에 존재하고 Struts, Spring MVC, Portlet MVC, 그리고 JSF와 같은 기본 프레임워크 내에서 자족적인 페이지 흐름(flow) 엔진(page flow engine)처럼 통합된다.<br>
SWF는 선언적이고 높은 이식성을 가지며 뛰어난 관리능력을 가지는 형태로 명시적으로 애플리케이션의 페이지 흐름(flow)을 획득하는 기능을 제공한다.


## 설명
Spring Web Flow는 여타의 API에 대한 몇 가지 요구 의존성을 가진 자족적인 page flow engine처럼 구조화되었다. 모든 의존성은 주의 깊게 관리된다.

대부분의 사용자들은 좀 더 큰 웹 애플리케이션 개발 프레임워크 내 컴포넌트로 SWF를 끼워 넣을 것이다.<br>
SWF는 요청 맵핑과 응답 표현을 다루기 위한 호출 시스템을 기대하는 컨트롤러 기술에 집중한다.<br>
이 경우, 이러한 사용자는 환경을 위한 가는(thin) 통합 조각에 의존할 것이다.<br>
예를 들어, Servlet 내 수행 흐름(flow)은 SWF에 대한 요청에 대한 할당(dispatch)과 SWF view 선택을 책임지는 표현을 다루는 Spring MVC 통합을 사용한다.<br>

Spring과 마찬가지로, Spring Web Flow는 필요한 부분만 선택적으로 사용할 수 있는 계층화된(layered) 프레임워크로 패키징되어 있다.<br>
SWF의 중요한 이득은 어떤 환경에서도 수행될 수 있는 자족적인 컨트롤러의 모듈을 재사용하여 정의할 수 있도록 하는 것이다.

구체적인 내용을 살펴보기 전에 Hello World를 실행해 보자.
- [Hello world](./getting-started.md)

Spring Web Flow의 기본 샘플로 Spring Source에서는 Hotel Booking 을 제공하고 있다.<br>
우리는 Spring Web Flow 레퍼런스 문서를 기준으로 하고 샘플인 Hotel Booking 을 참고하는 형태로 설명하도록 하겠다.

Hotel Booking 샘플 데모 : 🌏 [http://richweb.springframework.org/swf-booking-faces/spring/intro](https://web.archive.org/web/20110615224534/http://richweb.springframework.org/swf-booking-faces/spring/intro)

### SWF Configuration

- [SWF 시스템 설정](./setting-system.md)
- [Spring Web Flow 와 MVC 연동](./with-spring-mvc.md)
- [Securing Flows](./securing-flows.md)
- [Flow Managed Persistence](./flow-managed-persistence.md)

### SWF

- [Getting Started -Hello world](./setting-system.md)
- [Flow Definition](./flow-definiton.md)
- [Expression Language](./expression-language.md)
- [Rendering Views](./rendering-views.md)
- [Executing actions](./executing_actions.md)
- [Flow Inheritance](./flow-inheritance.md)


## 참고 자료
- 🌏 [Spring Web Flow reference 2.3.x](https://docs.spring.io/spring-webflow/docs/2.3.x/reference/html/index.html)
- 🌏 [openframework swf 소개](https://web.archive.org/web/20060619222620/http://openframework.or.kr:80/framework_reference/spring-webflow/1.0RC1/html/introduction.html)
