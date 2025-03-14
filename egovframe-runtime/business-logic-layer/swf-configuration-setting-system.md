---
title: Spring Web Flow 환경 설정
linkTitle: "시스템 설정"
description: Spring Web Flow를 사용하기 위해서는 Flow 정의를 위한 XML 문서를 작성하고, FlowRegistry와 FlowExecutor를 설정해야 한다. FlowRegistry는 flow XML을 가져오는 역할을, FlowExecutor는 이를 실행하는 역할을 담당한다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-configuration-setting-system/
menu:
  depth:
    name: 시스템 설정
    weight: 1
    parent: "swf-configuration"
---
# Spring Web Flow 환경 구성하기

Spring Web Flow를 사용하기 위한 Web 개발 환경에 대한 세팅을 설명한다.

## 설정

Spring Web Flow의 Flow 정의를 위한 XML 문서는 아래와 같은 Schema를 갖는다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:webflow="http://www.springframework.org/schema/webflow-config"
	xsi:schemaLocation="
http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
http://www.springframework.org/schema/webflow-config
http://www.springframework.org/schema/webflow-config/spring-webflow-config-2.0.xsd">
 
	<!-- Setup Web Flow here -->
</beans>
```

### 기본적인 설정

Spring Web Flow를 사용하려면 FlowRegistry  FlowExecutor를 설정해야 한다.

FlowRegistry는 등록될 시나리오에 따라 작성된 flow xml 을 가져오는 역할[1]을 수행한다.
FlowExecutor는 등록된 flow 설정 xml을 실행[2]한다. 차후 Spring MVC 와 결합하여 Web Flow 시스템이 실행되는 부분에 대해 다루겠다.


```xml
<!-- [1] Flow 설정 파일 등록-->
<webflow:flow-registry id="flowRegistry">
  <webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
</webflow:flow-registry>
 
<!-- [2] Flow 실행의 중추 역할을 하는 서비스 제공-->
<webflow:flow-executor id="flowExecutor" />
```

### flow-registry 옵션

flow-registry는 아래 보는 것과 같이 설정할 수 있다.

```xml
<!-- [1]기본은 이름-flow.xml이지만, 직접 지정할 수도 있다. -->
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
 
<!-- [2]id로 식별이 가능하도록 할 수도 있다 -->
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" id="bookHotel" />
 
<!-- [3]메타 정보도 등록할 수 있다. -->
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml">
	<flow-definition-attributes>
		<attribute name="caption" value="Books a hotel" />
	</flow-definition-attributes>
</webflow:flow-location>
 
<!-- [4]ANT 패턴을 지정할 수도 있다. -->
<webflow:flow-location-pattern value="/WEB-INF/flows/**/*-flow.xml" />
 
<!--
	[5]기본 앞 첨자 경로를 지정해서 위치를 조합해서 사용할 수도 있다. 
	    Flow 정의 파일은 모듈화를 높이기 위해서 관련 있는 폴더에 각각 위치해 있는게 가장 좋다.	-->
<webflow:flow-registry id="flowRegistry" base-path="/WEB-INF">
	<webflow:flow-location path="/hotels/booking/booking.xml" />
</webflow:flow-registry>
 
<!-- [6]Flow 상속 구조 구성 가능 -->
<!-- my-system-config.xml -->
<webflow:flow-registry id="flowRegistry" parent="sharedFlowRegistry">
	<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
</webflow:flow-registry>
 
<!-- shared-config.xml -->
<webflow:flow-registry id="sharedFlowRegistry">
	<!-- Global flows shared by several applications -->
</webflow:flow-registry>
```

### 커스텀 FlowBuilder 서비스 설정

flow-registry는 아래 보는 것과 같이 설정할 수 있다.

flow-registry에서 flow-builder-services는 flow를 구축하는 데 사용되는 서비스나 설정 등을 커스터마이징할 수 있다.
지정하지 않는 경우에는 기본 서비스가 사용된다.

```xml
<webflow:flow-registry id="flowRegistry" 	flow-builder-services="flowBuilderServices">
	<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
</webflow:flow-registry>
 
<webflow:flow-builder-services id="flowBuilderServices" />
```

#### 구성 가능한 서비스

##### conversion-service

SWF 시스템에서 사용하는 ConversionService를 커스터마이징. Flow 실행 동안에 필요한 경우 특정 타입을 다른 타입으로 변환해 줌(propertyEditor 성격)

##### expression-parser

ExpressionParser 커스터마이징하는데 사용. 기본은 Unified EL이 사용되며, 사용하는 영역은 classpath 이다. 다른 ExpressionParser로는 OGNL이 사용 됨.

##### view-factory-creator

ViewFactoryCreator를 커스터마이징. 디폴트 ViewFactoryCreator는 JSP, Velocity, Freemaker 등을 화면에 보여주게 해주는 Spring MVC ViewFactories로 되어 있음.

##### development

Flow 개발 모드 설정. true인 경우, Flow 정의가 변경되면 hot-reloading 적용(message bundles 과 같은 리소스 포함).

##### 별도로 커스터마이징 된경우

```xml
<webflow:flow-builder-services id="flowBuilderServices"
	conversion-service="conversionService" 
	expression-parser="expressionParser"
	view-factory-creator="viewFactoryCreator" />           
 
<bean id="conversionService" class="..." />
<bean id="expressionParser" class="..." />
<bean id="viewFactoryCreator" class="..." />
```

### flow-executor 옵션

#### Flow 실행 리스너 붙이기

Flow 실행의 Lifecycle에 관련된 리스너(listener)는 flow-execution-listeners를 이용하여 등록한다.

```xml
<flow-execution-listeners>
	<listener ref="securityListener" />
	<listener ref="persistenceListener" />
</flow-execution-listeners>
```

또한 특정 흐름에 대해서만 적용 가능하다.

```xml
<listener ref="securityListener" criteria="securedFlow1,securedFlow2"/>
```

#### FlowExecution persistence 조정

```xml
<flow-execution-repository max-executions="5" max-execution-snapshots="30" />
```

##### max-executions

사용자 세션 당 생성될 수 있는 Flow 실행 개수 지정

##### max-execution-snapshots

Flow 실행 당 받을 수 있는 이력 snapshot 개수 지정. snapshot을 사용하지 못하게 하려면, 0으로 지정. 제한이 없게 하려면 -1로 설정.

## 참고자료

- [Spring Web Flow reference](https://docs.spring.io/spring-webflow/docs/2.3.3.RELEASE/reference/html/)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
