---
title: Server Security 업그레이드
linkTitle: "업그레이드"
description: 표준프레임워크 2.7에서 3.0으로 Server Security 업그레이드 시, Spring Security 패키지와 API 변경, dependencies 수정, web.xml 수정 등이 필요하다. 주요 API 변경 사항에는 SpringSecurityException 삭제, ConfigAttributeDefinition 변경, SavedRequest 인터페이스화 등이 있으며, 패키지 경로 변경과 GrantedAuthority 방식의 변경도 적용해야 한다. 인증 및 GET 방식 호출 방지 처리, Mapping 클래스 변경,불필요한 클래스 삭제 등 여러 단계에서 소스 코드와 설정의 수정을 요구한다.
url: /egovframe-runtime/foundation-layer/server-security/server-security-upgrade/
menu:
    depth:
        name: Server Security 업그레이드
        weight: 5
        parent: "serverSecurity"
---
# Server Security 업그레이드

## 개요

표준프레임워크 2.7(Spring Security 2.0.4)에서 3.0(Spring Security 3.2.3)로 업그레이드 Server security의 경우 설정 변경뿐만 아니라 소스 상의 변경 작업이 필요하다.  

## 주요 변경내용 (Spring Security 부분)

### dependencies 및 패키지 변경

- spring-security-core (org.springframework.security.core, org.springframework.security.access, etc.)
- spring-security-web (org.springframework.security.web)
- spring-security-config (org.springframework.security.config)

### API 변경

- SpringSecurityException 삭제
- ConfigAttributeDefinition ⇒ Collection<ConfigAttribute>
- SavedRequest : class ⇒ interface (DefaultSavedRequest 대체)

### 기타

- 다중 http elements 지원
- stateless 인증 지원
- DebugFilter 추가 (debugging용)
- hasPermission 표현식 지원 (authorize JSP tag)
- 등등

## 실행환경 부분 업그레이드 절차

### 1. dependency 수정

```xml
<dependency>
    <groupId>egovframework.rte</groupId>
    <artifactId>egovframework.rte.fdl.security</artifactId>
    <version>3.0.0</version>
</dependency>
```

- 적용 버전은 최신 버전 확인 후 적용(patch 버전 등)

### 2. web.xml 수정

접속 제한을 사용하는 경우 web.xml 상에 HttpSessionEventPublisher listener의 패키지 변경 필요

- 기존 :
  
```xml
<listener>
	<listener-class>org.springframework.security.ui.session.HttpSessionEventPublisher</listener-class>
</listener>
```

- 변경 :
  
```xml
<listener>
	<listener-class>org.springframework.security.web.session.HttpSessionEventPublisher</listener-class>
</listener>
```

### 3. Spring Security 설정 수정

다음 설정을 참조하여 관련 설정을 변경한다. (Spring Security쪽 패키지 등)

```xml
<beans:beans  xmlns="http://www.springframework.org/schema/security"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
						http://www.springframework.org/schema/security http://www.springframework.org/schema/security/spring-security-3.2.xsd
						http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-3.2.xsd">
 
	<beans:bean id="securedObjectService" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectServiceImpl">
		<beans:property name="securedObjectDAO" ref="securedObjectDAO"/>
		<beans:property name="requestMatcherType" value="regex"/>	<!--  default : ant -->
	</beans:bean>
 
	<beans:bean id="securedObjectDAO" class="egovframework.rte.fdl.security.securedobject.impl.SecuredObjectDAO" >
		<beans:property name="dataSource" ref="dataSource"/>
		<!--
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
		-->
	</beans:bean>
 
	<!-- 불필요 삭제 -->
	<!--   
	<beans:bean id="userDetailsServiceWrapper" class="org.springframework.security.userdetails.hierarchicalroles.UserDetailsServiceWrapper">
		<beans:property name="roleHierarchy" ref="roleHierarchy"/>
		<beans:property name="userDetailsService" ref="jdbcUserService"/>
	</beans:bean>
	-->
 
	<beans:bean id="roleHierarchy" class="org.springframework.security.access.hierarchicalroles.RoleHierarchyImpl" >
		<!-- XML 사용 
		<beans:property name="hierarchy">
			<beans:value>
				ROLE_ADMIN > ROLE_USER
				ROLE_USER > ROLE_RESTRICTED
				ROLE_RESTRICTED > IS_AUTHENTICATED_FULLY
				IS_AUTHENTICATED_REMEMBERED > IS_AUTHENTICATED_ANONYMOUSLY
			</beans:value>
		</beans:property>
		-->
		<!-- DB 사용 -->
		<beans:property name="hierarchy" ref="hierarchyStrings"/>
	</beans:bean>
 
	<beans:bean id="hierarchyStrings" class="egovframework.rte.fdl.security.userdetails.hierarchicalroles.HierarchyStringsFactoryBean" init-method="init">
		<beans:property name="securedObjectService" ref="securedObjectService"/>
	</beans:bean>
 
	<!-- 
	Access Decision Manager는 자동으로 생성되기 때문에 선언 불필요 
	bean id : org.springframework.security.access.vote.AffirmativeBased#0
	※ #0 부분은 숫자 부분은 선언 순으로 순차적으로 생성됨
	-->
	<!--
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
	-->
 
	<beans:bean id="filterSecurityInterceptor" class="org.springframework.security.web.access.intercept.FilterSecurityInterceptor">	
		<beans:property name="authenticationManager" ref="org.springframework.security.authenticationManager" />
		<beans:property name="accessDecisionManager" ref="org.springframework.security.access.vote.AffirmativeBased#0" />
		<beans:property name="securityMetadataSource" ref="databaseSecurityMetadataSource" />
	</beans:bean>
 
	<beans:bean id="databaseSecurityMetadataSource" class="egovframework.rte.fdl.security.intercept.EgovReloadableFilterInvocationSecurityMetadataSource">
		<beans:constructor-arg ref="requestMap" />	
		<beans:property name="securedObjectService" ref="securedObjectService"/>
	</beans:bean>
 
	<!--  url  -->
	<beans:bean id="requestMap" 	class="egovframework.rte.fdl.security.intercept.UrlResourcesMapFactoryBean" init-method="init">
		<beans:property name="securedObjectService" ref="securedObjectService"/>
	</beans:bean>
 
	<!-- 지정 불필요 : request-matcher 참조 -->
	<!-- 
	<beans:bean id="regexUrlPathMatcher" class="org.springframework.security.web.util.matcher.RegexRequestMatcher" />	
 	-->
 
 	<http pattern="/css/＊＊" security="none"/>    
    <http pattern="/images/＊＊" security="none"/>
 	<http pattern="/js/＊＊" security="none"/>
 	<http pattern="\A/WEB-INF/jsp/.*\Z" request-matcher="regex" security="none"/> 	
 
	<http access-denied-page="/system/accessDenied.do" request-matcher="regex">
		<form-login login-processing-url="/j_spring_security_check"
					authentication-failure-url="/cvpl/EgovCvplLogin.do?login_error=1"
					default-target-url="/index.jsp?flag=L"
					login-page="/cvpl/EgovCvplLogin.do" />
		<anonymous/>
		<logout logout-success-url="/cvpl/EgovCvplLogin.do"/>
 
		<!-- for authorization -->
		<custom-filter before="FILTER_SECURITY_INTERCEPTOR" ref="filterSecurityInterceptor"/>
	</http>
 
	<!--
	authentication-manager 기본 생성 bean id :  org.springframework.security.authenticationManager
		(alias로 변경할 수 있음)
	-->
	<authentication-manager>
		<authentication-provider user-service-ref="jdbcUserService">
			<password-encoder  hash="sha-256" base64="true"/>
		</authentication-provider>		
	</authentication-manager>	
 
	<!-- userDetailsServiceWrapper -->
	<!-- customizing user table, authorities table -->
 
	<!--<jdbc-user-service id="jdbcUserService" data-source-ref="dataSource"
		users-by-username-query="SELECT USER_ID,PASSWORD,ENABLED,BIRTH_DAY FROM USERS WHERE USER_ID = ?"
		authorities-by-username-query="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>-->
 
	<beans:bean id="jdbcUserService" class="egovframework.rte.fdl.security.userdetails.jdbc.EgovJdbcUserDetailsManager" >
		<beans:property name="usersByUsernameQuery" value="SELECT USER_ID,PASSWORD,ENABLED,USER_NAME,BIRTH_DAY,SSN FROM USERS WHERE USER_ID = ?"/>
		<beans:property name="authoritiesByUsernameQuery" value="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>
		<beans:property name="roleHierarchy" ref="roleHierarchy"/>
		<beans:property name="dataSource" ref="dataSource"/>
		<beans:property name="mapClass" value="egovframework.rte.fdl.security.userdetails.EgovUserDetailsMapping"/>
	</beans:bean>
 
	<!-- method -->
	<beans:bean id="methodSecurityMetadataSourceAdvisor" class="org.springframework.security.access.intercept.aopalliance.MethodSecurityMetadataSourceAdvisor">
		<beans:constructor-arg value="methodSecurityInterceptor" />
		<beans:constructor-arg ref="delegatingMethodSecurityMetadataSource" />
		<beans:constructor-arg value="delegatingMethodSecurityMetadataSource" />
	</beans:bean>
 
	<beans:bean id="methodSecurityInterceptor" class="org.springframework.security.access.intercept.aopalliance.MethodSecurityInterceptor">
		<beans:property name="validateConfigAttributes" value="false" />
		<beans:property name="authenticationManager" ref="org.springframework.security.authenticationManager"/>
		<beans:property name="accessDecisionManager" ref="org.springframework.security.access.vote.AffirmativeBased#0"/>
		<beans:property name="securityMetadataSource" ref="delegatingMethodSecurityMetadataSource" />
	</beans:bean>
 
    <beans:bean id="delegatingMethodSecurityMetadataSource" class="org.springframework.security.access.method.DelegatingMethodSecurityMetadataSource">
        <beans:constructor-arg>
            <beans:list>
                <beans:ref bean="methodSecurityMetadataSources" />
                <beans:bean class="org.springframework.security.access.annotation.SecuredAnnotationSecurityMetadataSource" />
                <beans:bean class="org.springframework.security.access.annotation.Jsr250MethodSecurityMetadataSource" />
            </beans:list>
        </beans:constructor-arg>
    </beans:bean>
 
	<beans:bean id="methodSecurityMetadataSources" class="org.springframework.security.access.method.MapBasedMethodSecurityMetadataSource">
		<beans:constructor-arg ref="methodMap" />
	</beans:bean>
 
	<beans:bean id="methodMap" class="egovframework.rte.fdl.security.intercept.MethodResourcesMapFactoryBean" init-method="init">
		<beans:property name="securedObjectService" ref="securedObjectService"/>
		<beans:property name="resourceType" value="method"/>
	</beans:bean>
 
	<!-- pointcut -->
	<!-- if no map, there is a error that "this map must not be empty; it must contain at least one entry" -->
	<!-- // so there is dummy entry
	<beans:bean id="protectPointcutPostProcessor" class="org.springframework.security.config.method.ProtectPointcutPostProcessor">
		<beans:constructor-arg ref="methodSecurityMetadataSources" />
		<beans:property name="pointcutMap" ref="pointcutMap"/>
	</beans:bean>
 
	<beans:bean id="pointcutMap" class="egovframework.rte.fdl.security.intercept.MethodResourcesMapFactoryBean" init-method="init">
		<beans:property name="securedObjectService" ref="securedObjectService"/>
		<beans:property name="resourceType" value="pointcut"/>
	</beans:bean>
	-->
</beans:beans>
```

### 4. 불필요 class 삭제

자체 적용된 server security에 대한 소스 삭제 정리
Ex:

- org.springframework.security.intercept.web.EgovReloadableDefaultFilterInvocationDefinitionSource : 패키지 변경으로 인하여 불필요 (egovframework.rte.fdl.security.intercept.EgovReloadableFilterInvocationSecurityMetadataSource)
- …security.intercept.\*, …security.securedobject.securedobject.\*, …security.securedobject.userdetails.\* 등 : 업그레이된 실행환경쪽 패키지(egovframework.rte.fdl.security.\*)를 참조하기 때문에 불필요

### 5. Mapping 클래스 mapRow 메소드 변경

jdbcUserService(egovframework.rte.fdl.security.userdetails.jdbc.EgovJdbcUserDetailsManager)에 의해 지정된 mapClass는 EgovUsersByUsernameMapping 클래스를 extend 하도록 되어 있는데, 해당 EgovUsersByUsernameMapping의 mapRow() 메소드의 return 타입이 Object에서 EgovUserDtails로 변경되었다.

- 기존 :

```java
public class EgovSessionMapping extends EgovUsersByUsernameMapping {
    ...
 
    @Override
    protected Object mapRow(ResultSet rs, int rownum) throws SQLException {
        ...
    }
}
```

- 변경 : 
  
```java
public class EgovSessionMapping extends EgovUsersByUsernameMapping {
    ...
 
    @Override
    protected EgovUserDetails mapRow(ResultSet rs, int rownum) throws SQLException {
        ...
    }
}
```
### 6. 참조 패키지 및 클래스 변경

Spring security 관련 패키지 변경 등에 따라 일부 참조 클래스에 대한 패키지 변경 필요

- org.springframework.security.Authentication → org.springframework.security.core.Authentication
- org.springframework.security.GrantedAuthority → org.springframework.security.core.GrantedAuthority
- org.springframework.security.context.SecurityContext → org.springframework.security.core.context.SecurityContext
- org.springframework.security.context.SecurityContextHolder → org.springframework.security.core.context.SecurityContextHolder
- 등등

### 7. GrantedAuthority 방식 변경 (array -> collection 타입)

GrantedAuthority[] → Collection\<GrantedAuthority\> 변경 적용

- 이전 코드 :

```java
GrantedAuthority[] authorities = authentication.getAuthorities();
 
for (int i = 0; i < authorities.length; i++) {
	listAuth.add(authorities[i].getAuthority());
}
```

- 변경 코드 :

```java
Collection<GrantedAuthority> authorities = (Collection<GrantedAuthority>) authentication.getAuthorities();
 
for (GrantedAuthority authority : authorities) {
	listAuth.add(authority.getAuthority());
}
```

### 8. SecurityContext의 getAuthentication() 방식 변경

기존의 경우 로그인되지 않은 경우 SecurityContext의 getAuthentication()의 리턴 값이 null이었으나,

```java
SecurityContext context = SecurityContextHolder.getContext();
Authentication authentication = context.getAuthentication();
if (EgovObjectUtil.isNull(authentication)) {
	return null;
}
```

신규 버전의 경우는 null이 아닌 값으로 처리된다.

```java
SecurityContext context = SecurityContextHolder.getContext();
Authentication authentication = context.getAuthentication();
 
if (EgovObjectUtil.isNull(authentication)) {
	log.debug("## authentication object is null!!");
	return null;
}
 
if (authentication.getPrincipal() instanceof EgovUserDetails) {
	EgovUserDetails details = (EgovUserDetails) authentication.getPrincipal();
 
 
	log.debug("## EgovUserDetailsHelper.getAuthenticatedUser : AuthenticatedUser is {}", details.getUsername());
 
	return details.getEgovUserVO();
} else {
	return authentication.getPrincipal();
}
```

따라서 사용자 정보를 취득하는 부분은 자체 적용 부분이 아닌 실행환경 제공 부분(egovframework.rte.fdl.security.userdetails.util.EgovUserDetailsHelper)을 사용한다.

### 9. GET 방식 인증 불가 처리

신규 버전의 경우는 GET 방식으로 j_spring_security_check를 호출할 수 없게 되었다.(j_spring_security_check URL을 내부적으로 redirect 호출하는 경우에만 해당)
오류 메시지 : Authentication request failed: org.springframework.security.authentication.AuthenticationServiceException: Authentication method not supported: GET

이 경우 다음 코드와 같이 GET 방식이 아닌 filter chain 호출 방식으로 변경해주어야 한다

- 기존 코드 :

```java
return "redirect:/j_spring_security_check?j_username=" + resultVO.getUserSe() + resultVO.getId() + "&j_password=" + resultVO.getUniqId();
```

- 변경 코드 (일반 Controller인 경우) :
  
```java
@RequestMapping(value="/uat/uia/actionSecurityLogin.do")
public String actionSecurityLogin(@ModelAttribute("loginVO") LoginVO loginVO, 
	HttpServletRequest request, HttpServletResponse response,
	ModelMap model)
		throws Exception {
	...
 
	UsernamePasswordAuthenticationFilter springSecurity = null;
 
	ApplicationContext act = WebApplicationContextUtils.getRequiredWebApplicationContext(request.getSession().getServletContext());
	@SuppressWarnings("rawtypes")
	Map beans = act.getBeansOfType(UsernamePasswordAuthenticationFilter.class);
	if (beans.size() > 0) {
		springSecurity = (UsernamePasswordAuthenticationFilter)beans.values().toArray()[0];
	} else {
		throw new IllegalStateException("No AuthenticationProcessingFilter");
	}
 
	springSecurity.setContinueChainBeforeSuccessfulAuthentication(false);	// false 이면 chain 처리 되지 않음.. (filter가 아닌 경우 false로...)
 
	springSecurity.doFilter(
		new RequestWrapperForSecurity(request, resultVO.getUserSe() + resultVO.getId() , resultVO.getUniqId()), 
		response, null);
 
	return "forward:/cmm/main/mainPage.do";	// 성공 시 페이지.. (redirect 불가)
 
	...
}
 
...
class RequestWrapperForSecurity extends HttpServletRequestWrapper {	
	private String username = null;
	private String password = null;
 
	public RequestWrapperForSecurity(HttpServletRequest request, String username, String password) {
		super(request);
 
		this.username = username;
		this.password = password;
	}
 
	@Override
	public String getRequestURI() {
		return ((HttpServletRequest)super.getRequest()).getContextPath() + "/j_spring_security_check";
	}
 
	@Override
	public String getParameter(String name) {
        if (name.equals("j_username")) {
        	return username;
        }
 
        if (name.equals("j_password")) {
        	return password;
        }
 
        return super.getParameter(name);
    }
}
```

- 변경 코드 (Filter인 경우) :
  
```java
public class EgovSpringSecurityLoginFilter implements Filter{
	private FilterConfig config;
 
	public void init(FilterConfig filterConfig) throws ServletException {
		this.config = filterConfig;
	}
 
 
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		...
 
		HttpServletRequest httpRequest = (HttpServletRequest)request;
		HttpServletResponse httpResponse = (HttpServletResponse)response;
 
		...
 
		UsernamePasswordAuthenticationFilter springSecurity = null;
 
		ApplicationContext act = WebApplicationContextUtils.getRequiredWebApplicationContext(config.getServletContext());
		@SuppressWarnings("rawtypes")
		Map beans = act.getBeansOfType(UsernamePasswordAuthenticationFilter.class);
		if (beans.size() > 0) {
			springSecurity = (UsernamePasswordAuthenticationFilter)beans.values().toArray()[0];
		} else {
			throw new IllegalStateException("No AuthenticationProcessingFilter");
		}
 
		//springSecurity.setContinueChainBeforeSuccessfulAuthentication(false);	// false 이면 chain 처리 되지 않음.. (filter가 아닌 경우 false로...)
 
		springSecurity.doFilter(
			new RequestWrapperForSecurity(request, resultVO.getUserSe() + resultVO.getId() , resultVO.getUniqId()), 
			response, chain);
 
		...
	}
 
	...
}
 
class RequestWrapperForSecurity extends HttpServletRequestWrapper {	
	private String username = null;
	private String password = null;
 
	public RequestWrapperForSecurity(HttpServletRequest request, String username, String password) {
		super(request);
 
		this.username = username;
		this.password = password;
	}
 
	@Override
	public String getRequestURI() {
		return ((HttpServletRequest)super.getRequest()).getContextPath() + "/j_spring_security_check";
	}
 
	@Override
	public String getParameter(String name) {
        if (name.equals("j_username")) {
        	return username;
        }
 
        if (name.equals("j_password")) {
        	return password;
        }
 
        return super.getParameter(name);
    }
}
```

