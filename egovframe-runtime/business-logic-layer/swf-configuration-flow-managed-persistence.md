---
title: Flow가 관리하는 영속성(Flow Managed Persistence)
linkTitle: "Flow Managed Persistence"
description: Web Flow는 Flow 실행 중에 PersistenceContext를 생성하고, Flow가 종료될 때 데이터를 commit하여 영속성 관리를 지원하며, 주로 하이버네이트와 JPA와 연동된다. 이 패턴은 동시에 수정되는 데이터를 보호하기 위해 optimistic locking과 함께 사용되며, HTTP 세션 기반 저장 방법과는 달리 Flow 범위 내에서 영속성을 관리한다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-configuration-flow-managed-persistence/
menu:
    depth:
        name: Flow Managed Persistence
        weight: 4
        parent: "swf-configuration"
---
# Flow가 관리하는 영속성(Flow Managed Persistence)

## 개요

대부분의 애플리케이션은 여러 방법으로 데이터에 접근한다. 여러 사용자가 공유하는 데이터를 동시에 수정한다.
따라서 트랜잭션 데이터 접근 속성이 필요하다. 관계형 데이터 집합을 도메인 객체로 변환하여 애플리케이션 처리를 도와준다.
Web Flow는 “Flow가 관리하는 영속성”(flow managed persistence)을 제공하여 Flow가 객체 영속성 문맥을 만들고, commit 하고, 닫을 수 있도록 한다.
Web Flow는 하이버네이트와 JPA 객체 영속화 기술과 연동한다.

Flow-관리 영속성과 별도로 PesistenceContext 관리를 애플리케이션의 서비스 계층에서 완전히 캡슐화하는 패턴이 있다.
이런 경우 Web 계층은 영속화에 관여하지 않는다. 그 대신 서비스 계층으로 념주겨거나 반환받은 detached object를 가지고 동작한다.
이번 장은 Flow-관리 영속성에 초점을 맞추고 이 기능을 언제 어떻게 사용하는지 살펴보겠다.

## 설명

### Flow 범위(FlowScoped) PersistenceContext

이 패턴은 Flow 시작 시에 flowScope으로 PersistenceContext를 생성해 준다.
이 persistence context는 Flow 실행 과정 동안에 데이터 접근을 하는데 사용하며,
Flow가 종료될 때 persistent entity에서 변경된 내용을 반영(commit) 한다.
이 패턴은 대부분 다중 사용자에 의해서 동시에 수정되는 데이터의 정합성을 보호하고자 optimistic locking 전략과 함께 사용된다.

저장이나 재시작 능력이 필요 없다면, Flow 상태를 표준 HTTP 세션 기반 저장 방법이 충분하다.
이 때 커밋 전 세션 만료나 종료(termination)는 잠재적으로 변경 사항을 손실할 수 있다.
FlowScoped PersistenceContext 패턴을 사용하려면 먼저 persistence-context로 Flow를 식별하게 해야 한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
	<persistence-context />
</flow>
```

그 다음으로 이 패턴을 적용할 Flow에 적절한 FlowExecutionListener를 설정하자.
하이버네이트를 사용한다면, HibernateFlowExecutionListener를 등록하고, JPA를 사용한다면, JpaFlowExecutionListener를 등록하자.

```xml
<webflow:flow-executor id="flowExecutor"
		flow-registry="flowRegistry">
	<webflow:flow-execution-listeners>
		<webflow:listener ref="jpaFlowExecutionListener" />
	</webflow:flow-execution-listeners>
</webflow:flow-executor>
 
<bean id="jpaFlowExecutionListener" class="org.springframework.webflow.persistence.JpaFlowExecutionListener">
  <constructor-arg ref="entityManagerFactory" />
  <constructor-arg ref="transactionManager" />
</bean>
```

Flow가 종료되는 시점에 커밋이 일어나게 하려면, end-state의 commit 속성을 입력하자.

```xml
<end-state id="bookingConfirmed" commit="true" />
```

이걸로 끝이다.

이제 Flow가 시작할 때 리스너가 flowScope에 새로운 EntityManager를 할당해서 제어하게 된다.
Flow 내에서 스프링 기반 데이터 접근 객체를 사용해서 발생하는 데이터 접근 시에는 항상 이 EntityManager를 자동으로 사용하게 된다.
이러한 데이터 접근 연산은 중간 수정 내용의 고립성 유지를 위해 항상 트랜잭션 처리 대상이 되지 않고, 읽기 전용 트랜잭션에서만 실행되어야 한다.

## 참고자료

- [Spring Web Flow reference](https://docs.spring.io/spring-webflow/docs/2.3.3.RELEASE/reference/html/)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
- ~~[Whiteship's Note](http://whiteship.me/2146)~~ (만료됨)