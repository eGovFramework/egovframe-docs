---
title: Authentication
linkTitle: "Authentication"
description: 전자정부 표준프레임워크의 인증은 DB 기반의 JDBC 인증을 사용하며, Spring Security의 `AuthenticationManager`와 `AuthenticationProvider`를 설정하여 사용한다. 최소한의 환경설정으로 XML 또는 DB에서 사용자 정보를 관리할 수 있으며, JDBC 인증을 통해 사용자 정보와 권한을 쿼리로 관리한다. 또한, 세션 관리를 통해 사용자 세션을 확장하고, 동시 세션 제어를 통해 동일한 ID로의 동시 접속을 제한할 수 있다.
url: /egovframe-runtime/foundation-layer/server-security/server-security-authentication/
menu:
    depth:
        name: Authentication
        weight: 2
        parent: "serverSecurity"
---
# Authentication

## 개요

허락된 사용자에게만 공개되는 컨텐츠(정보 또는 기능)에 접근하기 위해 반드시 아이디와 암호를 입력하는 로그인 과정을 거치는데 이러한 과정이 인증(authentication)이다.  
즉, 인증은 특정 사용자가 유효한 사용자인지를 판단하는 과정을 의미한다.  
본 가이드에서는 인증을 위한 기본적인 환경 및 전자정부 표준프레임워크에서 사용된 인증 방법을 설명한다.

## 설명

 전자정부 표준프레임워크의 인증은 XML기반의 인증이 아닌 DB기반의 JDBC인증을 사용한다.  
기본적인 인증 메커니즘은 인증 주체가 인증을 시도하는 초기에 오직 한 번만 인증 메커니즘이 사용되며 그 이후로는 인증 메커니즘이 정보를 필터에 유지하여 요구되는 요청을 필터 체인상의 다음 필터로 전달하기만 한다.  
Spring Security에서 제공하는 인증을 사용하기 위해서는 AuthenticationManager와 실제 인증에 대한 정보를 제공하는 AuthenticationProvider의 설정이 필요하다.  
AuthenticationManager는 요청을 AuthenticationProvider 체인에 전달해야 할 임무가 있다.  
AuthenticationProvider는 기본적으로 UserDetails와 UserDetailsService인터페이스를 이용한다.  
UserDetailsService 인터페이스 내 loadUserByUsername 메소드의 리턴된 UserDetails은 사용자명(username), 패스워드(password), 허가권한(GrantedAuthority\[\]) 및 사용여부(enabled)와 같은 기초적인 인증 정보들을 제공한다.  
이에 전자정부 표준프레임워크에서는 UserDetails 인터페이스를 확장하였으며 JDBC 기반으로 사용자 테이블로부터 사용자 정보를 Map 또는 VO형태로 사용할 수 있도록 하였다.  

### 최소환경설정

 최소환경설정으로 사용자 인증을 설정하는 예제이다.

##### Configuration

```xml
<http>
	<intercept-url pattern="/**" access="ROLE_USER"/>
	<form-login />
	<logout />
</http>
```

- <intercept-url> 은 여러 개를 정의할 수 있으며, 위에서부터 차례로 해당되는 url pattern이 적용된다. 정규식을 사용하여 접근 url을 정의한다. “access”속성은 접근할 수 있는 사용자 권한을 나타낸다.
- <form-login> 을 지정하지 않을 경우나 기본 형식(<form-login />)으로 등록된 경우 Spring Security에서 제공하는 기본 로그인 폼을 사용한다.

 인증요청을 처리하기 위해 authentication manager가 xml(또는 DB, LDAP 등)에 정의된 사용자 정보를 사용한다.

```xml
<authentication-manager>
	<authentication-provider>
		<user-service>
			<user name="jimi" password="jimispassword" authorities="ROLE_USER, ROLE_ADMIN" />
			<user name="bob" password="bobspassword" authorities="ROLE_USER" />
		</user-service>
	</authentication-provider>
</authentication-manager>
```

- user-service : 사용자 정보(사용자 ID, 사용자 암호, 권한 등)를 얻어오는 서비스

### JDBC 인증

 표준프레임워크에서는 JdbcUserDetailsManager(org.springframework.security.provisioning)를 통해 인증 처리 부분을 JDBC 방식으로 확장하였다.  

 관련된 설정은 다음과 같이 지정한다.

##### Configuration

```xml
<authentication-manager>
	<authentication-provider user-service-ref="jdbcUserService">
		<password-encoder hash="sha-256" base64="true"/>
	</authentication-provider>		
</authentication-manager>
 
 
<beans:bean id="jdbcUserService" class="egovframework.rte.fdl.security.userdetails.jdbc.EgovJdbcUserDetailsManager" >
	<beans:property name="usersByUsernameQuery" value="SELECT USER_ID,PASSWORD,ENABLED,USER_NAME,BIRTH_DAY,SSN FROM USERS WHERE USER_ID = ?"/>
	<beans:property name="authoritiesByUsernameQuery" value="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>
	<beans:property name="roleHierarchy" ref="roleHierarchy"/>
	<beans:property name="dataSource" ref="dataSource"/>
	<beans:property name="mapClass" value="egovframework.rte.fdl.security.userdetails.EgovUserDetailsMapping"/>
</beans:bean>
```

- usersByUsernameQuery : 사용자 인증을 위한 query로 처음 3개 column은 인증시 사용되는 정보로 각각 user id, 패스워드, 활성화 여부를 나타낸다. 나머지 column의 경우 인증시에는 사용되지 않지만, 지정된 mapClass에 의해 사용되어 인증된 사용자 정보라 이후 참조될 수 있다.
- authoritiesByUsernameQuery : 인증된 사용자에게 부여되는 role(authorites)로 user id와 부여된 authority 2개의 column 지정이 필요하다.

 ※ 기타 설정들은 하단 “세션관리” 참조

### HTTP Form 인증 메카니즘

 HTTP 폼 인증은 AuthenticationProcessingFilter를 이용하여 로그인 폼을 처리하는 것을 수반한다.  
HTTP 폼 인증은 어플리케이션에서 가장 널리 사용되는 최종 사용자에 대한 인증 방법이다.  
로그인 폼은 단순히 j\_username과 j\_password 입력 필드를 포함하며, 필터에 의해 모니터링되고 있는 URL로 게시한다.기본값은 j\_spring\_security\_check 이다.

### 기타 인증

BASIC 인증  
다이제스트 인증  
익명 인증  
Remember-Me 인증  
X509 인증  
LDAP 인증  
CAS 인증  
컨테이너 어댑터 인증

### Sample Configuration

##### WEB Security service

```xml
<http pattern="/css/＊＊" security="none"/>    
<http pattern="/images/＊＊" security="none"/>
<http pattern="/js/＊＊" security="none"/>
<http pattern="A/WEB-INF/jsp/.*Z" request-matcher="regex" security="none"/> 	
 
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
```

- &lt;http&gt; 설정으로 허용된 사용자만 접근이 가능하게 할 수 있다.
- &lt;form-login&gt; 을 지정할 경우 개발자가 직접 지정한 로그인 화면 등을 지정할 수 있다.

```xml
	<authentication-manager>
		<authentication-provider user-service-ref="jdbcUserService">
			<password-encoder  hash="sha-256" base64="true"/>
		</authentication-provider>		
	</authentication-manager>
```

- 사용자 정보(사용자 ID, 사용자 암호, 권한 등)를 얻어오는 기능은 jdbcUserService 에서 담당한다.
- password-encoder : 저장된 패스워드의 암호화 알고리즘은 sha-256를 사용한다.

##### JDBC User Service

 사용자 정보를 얻어오는 **user service**를 DB에 저장된 사용자 정보를 이용하여 인증할 수 있다.

```xml
<jdbc-user-service id="jdbcUserService" data-source-ref="dataSource"
	users-by-username-query="SELECT USER_ID,PASSWORD,ENABLED,BIRTH_DAY FROM USERS WHERE USER_ID = ?"
	authorities-by-username-query="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>
```

##### Sample Source

```xml
<form action="<s:url value='/j_spring_security_check'/>" method="POST">
	<table>
		<tr><td>User:</td><td><input type='text' name='j_username'></td></tr>
		<tr><td>Password:</td><td><input type='password' name='j_password'></td></tr>
		<tr><td colspan='2' align="center"><input name="submit" type="submit" value="로그인">
			         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                         <input name="reset" type="reset" value="취소"></td></tr>
	</table>
</form>
```

### 세션관리

 Security Service의 세션 기능은 Spring Security의 JdbcUserDetailsManager 인터페이스를 확장하여 EgovJdbcUserDetailsManager 클래스를 구현하였으며  
기본 테이블에 기재된 username, password, enabled 필드 외에 다른 사용자 정보를 추가하여 세션정보를 관리할 수 있다.

#### 세션설정

##### Configuration

 세션 기능을 사용하기 위해서는 JDBC 인증의 환경설정 부분을 전자정부 개발프레임워크 Server Security의 환경으로 수정해야한다.  
변경전(사용안함)

```xml
<jdbc-user-service id="jdbcUserService" data-source-ref="dataSource"
	users-by-username-query="SELECT USER_ID,PASSWORD,ENABLED FROM USERS WHERE USER_ID = ?"
	authorities-by-username-query="SELECT USER_ID,AUTHORITY FROM AUTHORITIES WHERE USER_ID = ?"/>
```

 변경후(사용)

```xml
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
- mapClass : 세션 사용을 위한 세션 쿼리 및 세션 VO 간의 매핑 클래스를 설정한다.
- dataSource : JDBC 서비스를 위한 dataSource를 설정한다.

##### VO Class (ex)

```java
public class EgovUserDetailsVO {
	private String userId;
	private String passWord;
	private String userName;
	private String ssn;
	private String lsYn;
	private String birthDay;
	private Integer age;
	private String cellPhone;
	private String addr;
	private String email;
 
	public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getPassWord() {
		return passWord;
	}
	public void setPassWord(String passWord) {
		this.passWord = passWord;
	}
	public String getUserName() {
		return userName;
	}
	public void setUserName(String userName) {
		this.userName = userName;
	}
	public String getSsn() {
		return ssn;
	}
	public void setSsn(String ssn) {
		this.ssn = ssn;
	}
 
	.
	.
	.
```

##### Mapping Class

```java
public class EgovUserDetailsMapping extends EgovUsersByUsernameMapping {
	public EgovUserDetailsMapping(DataSource ds, String usersByUsernameQuery) {
		super(ds, usersByUsernameQuery);
	}
 
	@Override
	protected Object mapRow(ResultSet rs, int rownum) throws SQLException {
		String userid = rs.getString("user_id");
		String password = rs.getString("password");
		boolean enabled = rs.getBoolean("enabled");
 
		String username = rs.getString("user_name");
		String birthDay = rs.getString("birth_day");
		String ssn = rs.getString("ssn");
 
		EgovUserDetailsVO userVO = new EgovUserDetailsVO();
		userVO.setUserId(userid);
		userVO.setPassWord(password);
		userVO.setUserName(username);
		userVO.setBirthDay(birthDay);
		userVO.setSsn(ssn);
 
		return new EgovUserDetails(userid, password, enabled, userVO);
	}
}
```

- EgovUsersByUsernameMapping 클래스 상속
- mapRow 메소드 재정의
- ResultSet 클래스에서 작성된 VO로 데이터 매핑
- VO 객체를 EgovUserDetails(userid, password, enabled, userVO) 에 담아서 리턴

#### 세션사용

##### 세션 가져오기

```java
import egovframework.rte.fdl.security.userdetails.util.EgovUserDetailsHelper;
  .
  .
  .
 
EgovUserDetailsVO user = 
	(EgovUserDetailsVO)EgovUserDetailsHelper.getAuthenticatedUser();
 
assertEquals("jimi",		user.getUserId());
assertEquals("jimi test",	user.getUserName());
assertEquals("19800604",	user.getBirthDay());
assertEquals("1234567890123",	user.getSsn());
```

##### 인증되지 않은 경우 처리

```java
Boolean isAuthenticated = EgovUserDetailsHelper.isAuthenticated();
assertFalse(isAuthenticated.booleanValue());
```

 또는

```java
assertNull(EgovUserDetailsHelper.getAuthenticatedUser());
```

### 동시 세션처리

 Server security에서는 동일한 ID에 대하여 동시 접속을 제한할 수 있다.

 이를 위하여 우선 web.xml에 다음과 같이 HttpSessionEventPublisher listener를 등록해 주어야 한다.

#### web.xml 설정

```xml
<listener>
  <listener-class>
    org.springframework.security.web.session.HttpSessionEventPublisher
  </listener-class>
</listener>
```

#### security 설정

```xml
<http access-denied-page="/system/accessDenied.do" request-matcher="regex">
	<form-login login-processing-url="/j_spring_security_check"
		authentication-failure-url="/cvpl/EgovCvplLogin.do?login_error=1"
		default-target-url="/index.jsp?flag=L"
		login-page="/cvpl/EgovCvplLogin.do" />
	<anonymous/>
	<logout logout-success-url="/cvpl/EgovCvplLogin.do"/>
 
	<session-management>
		<concurrency-control max-sessions="1" error-if-maximum-exceeded="true" />
	</session-management>
 
</http>
```

 concurrent-session-control

- max-sessions : 최대 허용 세션 수
- exception-if-maximum-exceeded : true ⇒ 최대 세션 수 초과할 경우 Exception 발생 , false ⇒ 최대 세션 수 초과할 경우 강제 로그아웃

## 참고자료