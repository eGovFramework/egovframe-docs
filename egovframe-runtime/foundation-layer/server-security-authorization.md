---
title: Authorization
linkTitle: "- Authorization"
description: 전자정부 표준프레임워크의 권한 부여(Authorization)는 XML 또는 DB에서 권한을 관리하며 계층적 권한을 지원한다. Spring Security의 FilterSecurityInterceptor를 통해 보호 자원에 대한 접근 권한을 관리하고, DB 기반의 보호 자원 맵핑 정보를 동적으로 반영할 수 있다. 또한, 역할 계층은 XML 또는 DB에서 관리하며, 사용자는 세션을 통해 권한 정보를 가져와 처리할 수 있다.
url: /egovframe-runtime/foundation-layer/server-security/server-security-authorization/
menu:
    depth:
        name: Authorization
        weight: 3
        parent: "serverSecurity"
---
# Authorization

## 개요
웹 사이트에 존재하는 모든 사용자들은 사이트 정책에 따라 그 부류 별로 컨텐츠에 대한 접근이 제한 되는데 이것을 권한 부여(authorization)라 한다.
즉, 권한은 특정 사용자가 웹 사이트에서 제공하는 컨텐츠(정보 또는 기능)에 접근 가능한지를 판단하는 과정을 의미한다.

## 설명
Authorization은 <Acronym title="Extensible Markup Language">XML</Acronym> 또는 DB에서 권한을 관리하며 계층적 권한을 지원한다.

Server Security에서는 Filter Security Interceptor에 의해 처리되며, DB로부터 권한 정보를 처리하기 위해 다음과 같이 설정된다.

```xml
<http ...>
...
	<!-- for authorization -->
	<custom-filter before="FILTER_SECURITY_INTERCEPTOR" ref="filterSecurityInterceptor"/>
</http>
 
<beans:bean id="filterSecurityInterceptor" class="org.springframework.security.web.access.intercept.FilterSecurityInterceptor">	
	<beans:property name="authenticationManager" ref="org.springframework.security.authenticationManager" />
	<beans:property name="accessDecisionManager" ref="org.springframework.security.access.vote.AffirmativeBased#0" />
	<beans:property name="securityMetadataSource" ref="databaseSecurityMetadataSource" />
</beans:bean>
...
 
<beans:bean id="databaseSecurityMetadataSource" class="egovframework.rte.fdl.security.intercept.EgovReloadableFilterInvocationSecurityMetadataSource">
	<beans:constructor-arg ref="requestMap" />	
	<beans:property name="securedObjectService" ref="securedObjectService"/>
</beans:bean>
 
<!--  url  -->
<beans:bean id="requestMap" 	class="egovframework.rte.fdl.security.intercept.UrlResourcesMapFactoryBean" init-method="init">
	<beans:property name="securedObjectService" ref="securedObjectService"/>
</beans:bean>
 
<beans:bean id="securedObjectService" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectServiceImpl">
	<beans:property name="securedObjectDAO" ref="securedObjectDAO"/>
	<beans:property name="requestMatcherType" value="regex"/>	<!--  default : ant -->
</beans:bean>
 
<beans:bean id="securedObjectDAO" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectDAO" >
	<beans:property name="dataSource" ref="dataSource"/>
</beans:bean>
```

- authenticationManager : \<authentication-manager> 설정의 의해 자동으로 생성되는 bean ID를 지정(“org.springframework.security.authenticationManager”)
- accessDecisionManager : 권한 부여 여부를 결정하는 Access Decision Manager로서 자동으로 생성되기 때문에 해당 bean ID를 지정하면 됨(“org.springframework.security.access.vote.AffirmativeBased#0”)
- securityMetadataSource : 권한 설정 정보에 대한 처리 담당
참고로 자동으로 등록되는 AccessDecisionManager는 다음과 같은 설정을 갖는다.

```xml
<beans:bean id="accessDecisionManager" class="org.springframework.security.access.vote.AffirmativeBased">
	<beans:property name="allowIfAllAbstainDecisions" value="false" />
	<beans:property name="decisionVoters">
		<beans:list>
			<beans:bean class="org.springframework.security.access.vote.RoleVoter">
				<beans:property name="rolePrefix" value="ROLE_" />
			</beans:bean>
			<beans:bean class="org.springframework.security.access.vote.AuthenticatedVoter" />
		</beans:list>
	</beans:property>
</beans:bean>
```

- org.springframework.security.vote.AffirmativeBased : 단 한 개의 오브젝트라도 허락하면 허가하는 방식으로 처리(기본 처리)
- org.springframework.security.vote.UnanimousBased : 모든 오브젝트가 허락해야 허가하는 방식으로 처리
- decisionVoters : 허가 오브젝트에 대한 목록을 설정함

### 자원 관리

#### url
요청되는 웹 url을 점검하여 DB에 저장된 url과 비교하여 접근권한을 지정할 수 있다.
```
\A/sale/.*\.do\Z
\A/cvpl/((?!EgovCvplLogin\.do).)*\Z
```

##### filterSecurityInterceptor
FilterSecurityInterceptor는 <Acronym title="Hyper Text Transfer Protocol">HTTP</Acronym> 자원의 보안을 처리할 책임이 있다.
다른 보안 인터셉터와 유사하게 FilterSecurityInterceptor는 AuthenticationManager와 AccessDecisionManager에 대한 참조를 필요로 한다.
또한 FilterSecurityInterceptor는 서로 다른 <Acronym title="Hyper Text Transfer Protocol">HTTP</Acronym> <Acronym title="Uniform Resource Locator">URL</Acronym> 요청에 적용되는 설정 속성도 설정한다.

```xml
<beans:bean id="filterSecurityInterceptor" class="org.springframework.security.web.access.intercept.FilterSecurityInterceptor">	
	<beans:property name="authenticationManager" ref="org.springframework.security.authenticationManager" />
	<beans:property name="accessDecisionManager" ref="org.springframework.security.access.vote.AffirmativeBased#0" />
	<beans:property name="securityMetadataSource" ref="databaseSecurityMetadataSource" />
</beans:bean>
```

##### databaseSecurityMetadataSource
DB 기반으로 현재 시점의 url 보호자원-권한의 맵핑 정보를 Runtime 에 동적으로 변경 반영하기 위한 Spring Security 의 FilterInvocationSecurityMetadataSource 확장 클래스이다.

```xml
<beans:bean id="databaseSecurityMetadataSource" class="egovframework.rte.fdl.security.intercept.EgovReloadableFilterInvocationSecurityMetadataSource">
	<beans:constructor-arg ref="requestMap" />	
	<beans:property name="securedObjectService" ref="securedObjectService"/>
</beans:bean>
```

##### requestMap
DB 기반의 보호자원 맵핑 정보를 얻어 이를 참조하는 빈의 초기화 데이터로 제공한다.
securedObjectService의 getRolesAndUrl()를 호출하여 DB에서 역할과 url의 매핑정보를 얻어온다.

```xml
<beans:bean id="requestMap" class="egovframework.rte.fdl.security.intercept.UrlResourcesMapFactoryBean" init-method="init">
	<beans:property name="securedObjectService" ref="securedObjectService"/>
</beans:bean>
```

#### method
Spring Security는 Spring의 DefaultAdvisorAutoProxyCreator와 함께 사용될 수 있는 MethodSecurityMetadataSourceAdvisor 처리를 제공하며, 이것을 이용하여 자동적으로 보안 인터셉터를 MethodSecurityInterceptor를 정의한 빈의 앞부분에 연결한다.

##### methodSecurityMetadataSourceAdvisor
```xml
<beans:bean id="methodSecurityMetadataSourceAdvisor" class="org.springframework.security.access.intercept.aopalliance.MethodSecurityMetadataSourceAdvisor">
	<beans:constructor-arg value="methodSecurityInterceptor" />
	<beans:constructor-arg ref="delegatingMethodSecurityMetadataSource" />
	<beans:constructor-arg value="delegatingMethodSecurityMetadataSource" />
</beans:bean>
```

##### methodSecurityInterceptor
메소드 요청에 대한 자원을 보호하기 위해 MethodSecurityInterceptor를 어플리케이션 Context에 추가해야하며 보안을 필요로 하는 빈이 인터셉터에 연결(chaining)된다.
이러한 연결은 Spring의 ProxyFactoryBean이나 BeanNameAutoProxyCreator를 이용하여 만들어지며, Spring의 여러 다른 부분들이 통상적으로 이용되는 방식과 유사하다.
MethodSecurityInterceptor 는 다음과 같이 설정한다.

```xml
<beans:bean id="methodSecurityInterceptor" class="org.springframework.security.access.intercept.aopalliance.MethodSecurityInterceptor">
	<beans:property name="validateConfigAttributes" value="false" />
	<beans:property name="authenticationManager" ref="org.springframework.security.authenticationManager"/>
	<beans:property name="accessDecisionManager" ref="org.springframework.security.access.vote.AffirmativeBased#0"/>
	<beans:property name="securityMetadataSource" ref="delegatingMethodSecurityMetadataSource" />
</beans:bean>
```

```xml
<beans:bean id="delegatingMethodSecurityMetadataSource" class="org.springframework.security.access.method.DelegatingMethodSecurityMetadataSource">
	<beans:constructor-arg>
		<beans:list>
			<beans:ref bean="methodSecurityMetadataSources" />
			<beans:bean class="org.springframework.security.access.annotation.SecuredAnnotationSecurityMetadataSource" />
			<beans:bean class="org.springframework.security.access.annotation.Jsr250MethodSecurityMetadataSource" />
		</beans:list>
	</beans:constructor-arg>
</beans:bean>
methodSecurityMetadataSources
<beans:bean id="methodSecurityMetadataSources" class="org.springframework.security.access.method.MapBasedMethodSecurityMetadataSource">
	<beans:constructor-arg ref="methodMap" />
</beans:bean>
```

##### methodSecurityMetadataSources
```xml
<beans:bean id="methodSecurityMetadataSources" class="org.springframework.security.access.method.MapBasedMethodSecurityMetadataSource">
	<beans:constructor-arg ref="methodMap" />
</beans:bean>
```

##### methodMap
DB 기반의 보호자원 맵핑 정보를 얻어 이를 참조하는 빈의 초기화 데이터로 제공한다.
resourceType을 method로 설정하여 securedObjectService의 getRolesAndMethod()를 호출하여 DB에서 역할과 메소드의 매핑정보를 얻어온다.

```xml
<beans:bean id="methodMap" class="egovframework.rte.fdl.security.intercept.MethodResourcesMapFactoryBean" init-method="init">
	<beans:property name="securedObjectService" ref="securedObjectService"/>
	<beans:property name="resourceType" value="method"/>
</beans:bean>
```

#### pointcut
DB 기반의 보호자원 맵핑 정보를 얻어 이를 참조하는 빈의 초기화 데이터로 제공한다.
resourceType을 pointcut으로 설정하여 securedObjectService의 getRolesAndPointcut()를 호출하여 DB에서 역할과 Pointcut의 매핑정보를 얻어온다. ex: execution(* egovframework.rte.security..service.\*Service.insert*(..))

```xml
<beans:bean id="protectPointcutPostProcessor" class="org.springframework.security.config.method.ProtectPointcutPostProcessor">
	<beans:constructor-arg ref="methodSecurityMetadataSources" />
	<beans:property name="pointcutMap" ref="pointcutMap"/>
</beans:bean>
 
<beans:bean id="pointcutMap" class="egovframework.rte.fdl.security.intercept.MethodResourcesMapFactoryBean" init-method="init">
	<beans:property name="securedObjectService" ref="securedObjectService"/>
	<beans:property name="resourceType" value="pointcut"/>
</beans:bean>
```

### 역할 관리
역할은 상하 계층으로 관리하며 어플리케이션 Context 또는 DB에 저장하여 관리한다.

#### XMl Context에 계층 역할을 등록하여 관리할 경우
```xml
<beans:bean id="roleHierarchy" 
		class="org.springframework.security.access.hierarchicalroles.RoleHierarchyImpl" >
	<beans:property name="hierarchy">
		<beans:value>
			ROLE_ADMIN > ROLE_USER
			ROLE_USER > ROLE_RESTRICTED
			ROLE_RESTRICTED > IS_AUTHENTICATED_FULLY
			IS_AUTHENTICATED_REMEMBERED > IS_AUTHENTICATED_ANONYMOUSLY
		</beans:value>
	</beans:property>
</beans:bean>
```

#### DB에서 계층 역할을 관리할 경우
```xml
<beans:bean id="roleHierarchy" 
		class="org.springframework.security.access.hierarchicalroles.RoleHierarchyImpl" >
	<beans:property name="hierarchy" ref="hierarchyStrings"/>
</beans:bean>
```
 
```xml
<beans:bean id="hierarchyStrings" class="egovframework.rte.fdl.security.userdetails.hierarchicalroles.HierarchyStringsFactoryBean" init-method="init">
	<beans:property name="securedObjectService" ref="securedObjectService"/>
</beans:bean>
	<beans:bean id="jdbcUserService" class="egovframework.rte.fdl.security.userdetails.jdbc.EgovJdbcUserDetailsManager" >
		<beans:property name="usersByUsernameQuery" value="SELECT USER_ID,PASSWORD,ENABLED,USER_NAME,BIRTH_DAY,SSN FROM USERS WHERE USER_ID = ?"/>
		<beans:property name="authoritiesByUsernameQuery" value="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>
		<beans:property name="roleHierarchy" ref="roleHierarchy"/>
		<beans:property name="dataSource" ref="dataSource"/>
		<beans:property name="mapClass" value="egovframework.rte.fdl.security.userdetails.EgovUserDetailsMapping"/>
	</beans:bean>
```

- class : egovframework.rte.fdl.security.userdetails.jdbc.EgovJdbcUserDetailsManager
- usersByUsernameQuery : 사용자 인증을 위해 사용자 테이블에서 사용자정보를 조회한다.
- authoritiesByUsernameQuery : 사용자 인증을 위해 사용자권한 테이블에서 사용자권한정보를 조회한다.
- roleHierarchy : 역할의 계층적 관리를 위해 계층 역할을 설정한다.
- mapClass : 세션 사용을 위한 세션 쿼리 및 세션VO간의 매핑 클래스를 설정한다.
- dataSource : JDBC 서비스를 위한 dataSource를 설정한다.
  
#### Configuration
```xml
<beans:bean id="securedObjectService" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectServiceImpl">
	<beans:property name="securedObjectDAO" ref="securedObjectDAO"/>
	<beans:property name="requestMatcherType" value="regex"/>	<!--  default : ant -->
</beans:bean>
 
<beans:bean id="securedObjectDAO" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectDAO" >
	<beans:property name="dataSource" ref="dataSource"/>
</beans:bean>
```
아래의 속성쿼리는 SecuredObjectDAO 빈에 기본으로 내장되었으며 DBMS 벤더에 따른 SQL문 차이 또는 DB 스키마 차이로 인한 변경된 쿼리를 직접 반영할 수 있다.
내장된 기본 쿼리는 다음과 같다.

- sqlHierarchicalRoles
```SQL
SELECT a.child_role child, a.parent_role parent
FROM ROLES_HIERARCHY a LEFT JOIN ROLES_HIERARCHY b on (a.child_role = b.parent_role)
```
- sqlRolesAndUrl
```SQL
SELECT a.resource_pattern url, b.authority authority
FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
WHERE a.resource_id = b.resource_id
AND a.resource_type = 'url' ORDER BY a.sort_order
```
- sqlRolesAndMethod
```SQL
SELECT a.resource_pattern method, b.authority authority
FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
WHERE a.resource_id = b.resource_id
AND a.resource_type = 'method' ORDER BY a.sort_order
```
- sqlRolesAndPointcut
```SQL
SELECT a.resource_pattern pointcut, b.authority authority
FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
WHERE a.resource_id = b.resource_id
AND a.resource_type = 'pointcut' ORDER BY a.sort_order
```
SecuredObjectDAO 빈에 내장된 SQL을 사용하지 않을 경우 아래와 같이 SQL을 지정하여 설정한다.
```XML
<beans:bean id="securedObjectDAO" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectDAO" >
	<beans:property name="dataSource" ref="dataSource"/>
	<beans:property name="sqlHierarchicalRoles">
		<beans:value>
			SELECT a.child_role child, a.parent_role parent
			FROM ROLES_HIERARCHY a LEFT JOIN ROLES_HIERARCHY b on (a.child_role = b.parent_role)
		</beans:value>
	</beans:property>
	<beans:property name="sqlRolesAndUrl">
		<beans:value>
			SELECT a.resource_pattern url, b.authority authority
			FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
			WHERE a.resource_id = b.resource_id
			AND a.resource_type = 'url' ORDER BY a.sort_order
		</beans:value>
	</beans:property>
	<beans:property name="sqlRolesAndMethod">
		<beans:value>
	    SELECT a.resource_pattern method, b.authority authority
			FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
			WHERE a.resource_id = b.resource_id
			AND a.resource_type = 'method' ORDER BY a.sort_order
		</beans:value>
	</beans:property>
	<beans:property name="sqlRolesAndPointcut">
		<beans:value>
			SELECT a.resource_pattern pointcut, b.authority authority
			FROM SECURED_RESOURCES a, SECURED_RESOURCES_ROLE b
			WHERE a.resource_id = b.resource_id
			AND a.resource_type = 'pointcut' ORDER BY a.sort_order
		</beans:value>
	</beans:property>
</beans:bean>
```
### 세션사용

#### 역할 가져오기
```java
List<String> authorities = EgovUserDetailsHelper.getAuthorities();
 
// 1. authorites 에  권한이 있는지 체크 TRUE/FALSE
assertTrue(authorities.contains("ROLE_USER"));
assertTrue(authorities.contains("ROLE_RESTRICTED"));
assertTrue(authorities.contains("IS_AUTHENTICATED_ANONYMOUSLY"));
assertTrue(authorities.contains("IS_AUTHENTICATED_FULLY"));
assertTrue(authorities.contains("IS_AUTHENTICATED_REMEMBERED"));
 
// 2. authorites 에  ROLE 이 여러개 설정된 경우
for (Iterator<String> it = authorities.iterator(); it.hasNext();) {
	String auth = it.next();
}
 
// 3. authorites 에  ROLE 이 하나만 설정된 경우
String auth = (String) authorities.toArray()[0];
```