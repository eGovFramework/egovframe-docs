---
title: Spring Web Flow에서 보안 적용
linkTitle: "Securing Flows"
description: Spring Security를 통해 Flow 실행에 보안을 적용하려면 인증 및 권한 규칙을 설정하고, Flow 정의에 secured 구성요소를 추가하며, SecurityFlowExecutionListener를 사용하여 보안 규칙을 처리한다. 보안 규칙은 Flow, state, transition 단계에서 적용 가능하다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-configuration-securing-flows/
menu:
  depth:
    name: Securing Flows
    weight: 3
    parent: swf-configuration
---
# Flow에 보안 적용하기(Securing Flows)

## 개요

보안은 어플리케이션 에서 매우 중요한 이슈이다.
Spring Security는 어플리케이션과 결합하여 여러 수준에서 보안을 책임지는 플랫폼의 기능을 수행한다.
여기서는 Web Flow에 적용되는 Spring Security에 대해 알아보겠다.

### 어떻게 Flow를 안전하게 할 수 있을까?

Flow 실행에 보안을 적용시키고 싶다면 다음 단계에 따르자.

1. Spring Security에서 인증(authentication)과 권한(authorization) 규칙을 설정한다.
2. secured 구성요소로 Flow 정의에 보안 규칙을 추가한다.
3. 보안 규칙을 처리해주는 SecurityFlowExecutionListener 추가한다.
   
### secured 구성요소

secured 구성 요소는 접근하기 전에 권한 확인을 적용해 주며, Flow 실행 단계마다 한 번 이상은 나올 수 없다.
Flow 실행에서 세 단계로 보안을 적용할 수 있다. Flow, state, transition에 보안 적용이 가능하다.
사용되는 문법은 동일하다. secured 구성요소는 보안이 적용되어야 하는 구성 요소 내에 위치하면 된다.
예를 들어 view state에 보안을 적용하고자 하면,

```xml
<view-state id="secured-view">
 <secured attributes="ROLE_USER" />
 ...
</view-state>
```
#### 속성에 보안 적용

attributes 속성은 ','(콤마)로 구분해서 SS의 권한 속성을 리스트로 입력할 수 있다. 이 속성은 대부분 허가된 보안 롤(role)을 명시하게 된다.
스프링 시큐리티 접근 결정 매니저(access decision manager)에 의해 이 속성에 입력한 값과 사용자가 가지고 있는 값을 비교한다.

```xml
<secured attributes="ROLE_USER" />
```

기본적으로, 롤 기반 접근 결정 관리자를 사용하여 사용자가 접근할 수 있는지 확인한다.
만약 애플리케이션이 권한 룰을 사용하지 않는다면 이 부분을 오버라이딩할 필요가 있다.

#### 타입 맞춰보기

두 가지 유형의 일치 유형 제공: any, all.

```xml
<secured attributes="ROLE_USER, ROLE_ANONYMOUS" match="any" />
```

이 속성은 필수가 아니다. 정의하지 않으면 기본 값은 any다.

### SecurityFlowExecutionListener

Web Flow 설정에 추가한다.
SecurityFlowExecutionListener가 Web Flow 설정에 정의되어 있어야 플로우 실행기(executor)에 적용된다.

```xml
<webflow:flow-executor id="flowExecutor"
	flow-registry="flowRegistry">
	<webflow:flow-execution-listeners>
		<webflow:listener ref="securityFlowExecutionListener" />
	</webflow:flow-execution-listeners>
</webflow:flow-executor>
<bean id="securityFlowExecutionListener"
	class="org.springframework.webflow.security.SecurityFlowExecutionListener" />
```

보안 설정에 의해서 접근이 거절되면, AccessDeniedException이 발생한다.
기본으로 롤 기반 의사결정이 이루어 지지만, 커스텀 의사결정 관리자를 지정할 수 있다.

```xml
<bean id="securityFlowExecutionListener" 	class="org.springframework.webflow.security.SecurityFlowExecutionListener">
	<property name="accessDecisionManager" ref="myCustomAccessDecisionManager" />
</bean>
```

### Spring Security 환경 구성

#### 스프링 환경 구성

http와 authentication-provider로 정의하면 된다.

```xml 
<security:http auto-config="true">
	<security:form-login login-page="/spring/login"
		login-processing-url="/spring/loginProcess" default-target-url="/spring/main"
		authentication-failure-url="/spring/login?login_error=1" />
	<security:logout logout-url="/spring/logout" logout-success-url="/spring/logout-success" />
</security:http>
 
<security:authentication-provider>
	<security:password-encoder hash="md5" />
	<security:user-service>
		<security:user name="keith" password="417c7382b16c395bc25b5da1398cf076"	authorities="ROLE_USER,ROLE_SUPERVISOR" />
		<security:user name="erwin" password="12430911a8af075c6f41c6976af22b09"	authorities="ROLE_USER,ROLE_SUPERVISOR" />
		<security:user name="jeremy" password="57c6cbff0d421449be820763f03139eb" authorities="ROLE_USER" />
		<security:user name="scott" password="942f2339bf50796de535a384f0d1af3e"	authorities="ROLE_USER" />
	</security:user-service>
</security:authentication-provider>
```

#### web.xml 환경 구성

필터 설정.(SS 기본)

```xml
<filter>
	<filter-name>springSecurityFilterChain</filter-name>
	<filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class>
</filter>
<filter-mapping>
	<filter-name>springSecurityFilterChain</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```

## 참고자료

- [Spring Web Flow reference](https://docs.spring.io/spring-webflow/docs/2.3.3.RELEASE/reference/html/)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
- ~~[Whiteship's Note](http://whiteship.me/2146)~~ (만료됨)