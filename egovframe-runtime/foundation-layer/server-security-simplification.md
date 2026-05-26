---
title: 설정 간소화
linkTitle: "설정 간소화"
description: 전자정부 표준프레임워크의 Spring Security 설정 간소화서비스를 사용한 Spring Security 기반 인증 및 URL 패턴별 접근제어 설정을 제공한다.
url: /egovframe-runtime/foundation-layer/server-security/server-security-simplification/
menu:
    depth:
        name: 설정 간소화
        weight: 4
        parent: "serverSecurity"
---
# Spring Security 설정 간소화서비스

전자정부 표준프레임워크 실행환경 구성요소인 Spring Security 설정 간소화서비스를 사용한 Spring Security 기반 접근제어 설정 및 사용법을 정리한 문서입니다.

## 개요

Spring Security 설정 간소화서비스를 이용한 인증 및 URL 패턴별 접근제어를 제공합니다. JDBC 기반 사용자 인증과 DB의 역할(Role)-URL 매핑을 통해 요청에 대한 권한을 검사합니다.

## 라이브러리 적용

### pom.xml 의존성 추가

```xml
<dependency>
    <groupId>org.egovframe.rte</groupId>
    <artifactId>egovframe-rte-fdl-security</artifactId>
</dependency>
```

- 전자정부 Maven 저장소(`https://maven.egovframe.go.kr/maven/`)에서 의존성 해결
- parent POM의 `egovframe.rte.version`에 따라 버전 관리

## 설정 방법

### 1. globals.properties

**경로:** `src/main/resources/egovframework/egovProps/globals.properties`

```properties
# 권한 인증방식 - security 설정 시 egovframe-rte-fdl-security 사용
Globals.Auth = security

# Spring Security 설정 파일 경로 (egov-security 모듈이 참조)
Globals.SecurityConfigPath = egovframework/egovProps/conf/egov-security-config.properties
```

### 2. egov-security-config.properties

**경로:** `src/main/resources/egovframework/egovProps/conf/egov-security-config.properties`

| 항목 | 필수 | 설명 |
|------|------|------|
| `id` | O | Security 설정 빈 식별자 |
| `loginUrl` | O | 로그인 페이지 URL |
| `loginProcessUrl` | O | 로그인 처리 URL |
| `logoutUrl` | O | 로그아웃 처리 URL |
| `logoutSuccessUrl` | O | 로그아웃 성공 시 리다이렉트 URL |
| `loginFailureUrl` | O | 로그인 실패 시 리다이렉트 URL |
| `accessDeniedUrl` | O | 권한 부족 시 리다이렉트 URL |
| `dataSource` | O | 인증/권한 조회용 DataSource 빈 이름 |
| `jdbcUsersByUsernameQuery` | O | 사용자 인증 조회 쿼리 |
| `jdbcAuthoritiesByUsernameQuery` | O | 사용자 권한 조회 쿼리 |
| `jdbcMapClass` | O | ResultSet → UserDetails 매핑 클래스 |
| `requestMatcherType` | O | URL 매칭 방식: `regex`, `ant`, `ciRegex` |
| `hash` | O | 패스워드 저장 방식: `plaintext`, `sha-256`, `md5`, `bcrypt` 등 |
| `hashBase64` | O | hash 값 Base64 인코딩 여부 |
| `concurrentMaxSessons` | O | 동시 접속 허용 세션 수 |
| `concurrentExpiredUrl` | O | 세션 만료 시 리다이렉트 URL |
| `defaultTargetUrl` | O | 로그인 성공 시 기본 리다이렉트 URL |
| `permitAllList` | O | 인증 없이 허용할 URL 패턴 (쉼표 구분) |
| `sqlRolesAndUrl` | O | URL 패턴별 권한 매핑 조회 쿼리 |
| `sqlRegexMatchedRequestMapping` | O | Regex 방식 URL-권한 매핑 쿼리 |
| `sqlHierarchicalRoles` | O | 역할 계층 조회 쿼리 |

**예시 설정:**

```properties
id = egovSecurityConfig
loginUrl = /uat/uia/egovLoginUsr.do
loginProcessUrl = /uat/uia/actionSecurityProcess.do
logoutUrl = /uat/uia/actionSecurityLogout.do
logoutSuccessUrl = /uat/uia/egovLoginUsr.do
loginFailureUrl = /uat/uia/egovLoginUsr.do?login_error=1
accessDeniedUrl = /sec/ram/accessDenied.do
dataSource = egov.dataSource
jdbcUsersByUsernameQuery = SELECT USER_ID, ESNTL_ID AS PASSWORD, 1 ENABLED, USER_NM, USER_ZIP, USER_ADRES, USER_EMAIL, USER_SE, ORGNZT_ID, ESNTL_ID, (select a.ORGNZT_NM from COMTNORGNZTINFO a where a.ORGNZT_ID = m.ORGNZT_ID) ORGNZT_NM FROM COMVNUSERMASTER m WHERE CONCAT(USER_SE, USER_ID) = ?
jdbcAuthoritiesByUsernameQuery = SELECT A.SCRTY_DTRMN_TRGET_ID USER_ID, A.AUTHOR_CODE AUTHORITY FROM COMTNEMPLYRSCRTYESTBS A, COMVNUSERMASTER B WHERE A.SCRTY_DTRMN_TRGET_ID = B.ESNTL_ID AND B.USER_ID = ?
jdbcMapClass = egovframework.com.sec.security.common.EgovSessionMapping
requestMatcherType = regex
hash = plaintext
hashBase64 = false
concurrentMaxSessons = 1
concurrentExpiredUrl = /EgovContent.do
defaultTargetUrl = /EgovContent.do
alwaysUseDefaultTargetUrl = true
permitAllList = /css/**, /html/**, /images/**, /js/**, /resource/**, /uat/uia/**.do, /, /index.do, /EgovTop.do, /EgovBottom.do, /EgovLeft.do, /EgovContent.do, /sec/ram/accessDenied.do, ...
sqlRolesAndUrl = SELECT a.ROLE_PTTRN as url, b.AUTHOR_CODE authority FROM COMTNROLEINFO a, COMTNAUTHORROLERELATE b WHERE a.ROLE_CODE = b.ROLE_CODE AND a.ROLE_TY = 'url' ORDER BY a.ROLE_SORT
sqlRegexMatchedRequestMapping = SELECT a.ROLE_PTTRN as uri, b.AUTHOR_CODE authority FROM COMTNROLEINFO a, COMTNAUTHORROLERELATE b WHERE a.ROLE_CODE = b.ROLE_CODE AND a.ROLE_TY = 'regex' ORDER BY a.ROLE_SORT
sqlHierarchicalRoles = SELECT a.CHLDRN_ROLE as child, a.PARNTS_ROLE parent FROM COMTNROLES_HIERARCHY a LEFT JOIN COMTNROLES_HIERARCHY b on (a.CHLDRN_ROLE = b.PARNTS_ROLE)
```

## Spring 설정

### context-common.xml - Component Scan

egovframe-rte-fdl-security의 `@Configuration` 클래스를 스캔하여 `springSecurityFilterChain` 등 빈을 자동 등록합니다.

```xml
<context:component-scan base-package="egovframework, org.egovframe.rte.fdl.security, org.egovframe.rte.fdl.crypto">
```

- `Globals.SecurityConfigPath`에 지정된 properties 파일을 읽어 Spring Security 설정 빈 생성

### context-egovuserdetailshelper.xml - security 프로파일

`Globals.Auth = security`일 때 `EgovUserDetailsSecurityServiceImpl`이 `EgovUserDetailsHelper`에 주입됩니다.

```xml
<beans profile="security">
    <bean id="egovUserDetailsHelper" class="egovframework.com.cmm.util.EgovUserDetailsHelper">
        <property name="egovUserDetailsService" ref="egovUserDetailsSecurityService" />
    </bean>
    <bean id="egovUserDetailsSecurityService" class="egovframework.com.sec.ram.service.impl.EgovUserDetailsSecurityServiceImpl"/>
</beans>
```

### EgovSessionMapping - 사용자 정보 매핑

`jdbcMapClass`로 지정된 클래스. ResultSet을 `EgovUserDetails`(LoginVO 포함)로 매핑합니다.

```java
public class EgovSessionMapping extends EgovUsersByUsernameMapping {
    @Override
    protected EgovUserDetails mapRow(ResultSet rs, int rownum) throws SQLException {
        // user_id, password, enabled, user_nm, user_se, orgnzt_id, esntl_id 등 매핑
        return new EgovUserDetails(strUserId, strPassWord, strEnabled, loginVO);
    }
}
```

### EgovWebApplicationInitializer - Security 필터 등록

`Globals.Auth = security`일 때 `springSecurityFilterChain`과 `HttpSessionEventPublisher`가 등록됩니다.

```java
if("security".equals(EgovProperties.getProperty("Globals.Auth").trim())) {
    DelegatingFilterProxy securityFilter = new DelegatingFilterProxy("springSecurityFilterChain");
    securityFilter.setContextAttribute(FrameworkServlet.SERVLET_CONTEXT_PREFIX + "dispatcher");
    FilterRegistration.Dynamic security = servletContext.addFilter("springSecurityFilterChain", securityFilter);
    security.addMappingForUrlPatterns(null, false, "/*");

    servletContext.addListener(new org.springframework.security.web.session.HttpSessionEventPublisher());
}
```

- `HttpSessionEventPublisher`: 동시 세션 제어를 위해 세션 생성/소멸 이벤트를 Spring Security에 전달

### EgovWebServletContextListener - 프로파일 활성화

`Globals.Auth` 값을 Spring Profile에 반영합니다.

```java
System.setProperty("spring.profiles.active", 
    EgovProperties.getProperty("Globals.DbType") + "," + EgovProperties.getProperty("Globals.Auth"));
```

- 예: `mysql,security` → DB 프로파일 + security 프로파일 활성화

## 로그인/로그아웃 연동

### 로그인 처리

일반 로그인 성공 후 `Globals.Auth = security`이면 EgovWebApplicationInitializer 클래스에 정의된 `EgovSpringSecurityLoginFilter` 필터를 통해 인증인가를 진행합니다. 

```java
DelegatingFilterProxy LoginFilter = 
	new DelegatingFilterProxy("egovSpringSecurityLoginFilter");
LoginFilter.setContextAttribute(
	WebApplicationContext.ROOT_WEB_APPLICATION_CONTEXT_ATTRIBUTE);
FilterRegistration.Dynamic loginFormBridgeReg =
	servletContext.addFilter("egovSpringSecurityLoginFilter", LoginFilter);
loginFormBridgeReg.addMappingForUrlPatterns(null, false, "/*");
```

### 로그아웃

```java
// EgovLoginController.actionLogout
if("security".equals(EgovProperties.getProperty("Globals.Auth").trim())) {
    return "redirect:/uat/uia/actionSecurityLogout.do";
}
```

- `actionSecurityLogout.do`: egov-security가 처리하는 로그아웃 URL

## 사용법

### 인증 여부 및 사용자 정보 조회

`EgovUserDetailsHelper`(egovframework.com.cmm.util)로 인증 정보를 조회합니다.

```java
import egovframework.com.cmm.util.EgovUserDetailsHelper;

// 인증 여부
Boolean isAuthenticated = EgovUserDetailsHelper.isAuthenticated();

// 인증된 사용자 객체 (LoginVO)
LoginVO user = (LoginVO) EgovUserDetailsHelper.getAuthenticatedUser();

// 사용자 권한 목록 (ROLE_XXX 등)
List<String> authorities = EgovUserDetailsHelper.getAuthorities();
```

### 권한-롤 매핑 재로딩

권한-롤 매핑 변경 후 서버 재기동 없이 적용하려면 `EgovReloadableFilterInvocationSecurityMetadataSource.reload()`를 호출합니다.

```java
import org.egovframe.rte.fdl.security.bean.EgovReloadableFilterInvocationSecurityMetadataSource;

@Autowired(required = false)
private EgovReloadableFilterInvocationSecurityMetadataSource egovReloadableFilterInvocationSecurityMetadataSource;

@RequestMapping("/sec/ram/insertAuthorRole.do")
public String insertAuthorRole(...) {
    // 권한-롤 등록/수정 처리
    ...
    if (egovReloadableFilterInvocationSecurityMetadataSource != null) {
        egovReloadableFilterInvocationSecurityMetadataSource.reload();
    }
    return "redirect:...";
}
```

### 컨트롤러에서 인증 사용자 주입

`EgovSecurityArgumentResolver`로 메서드 파라미터에 인증 사용자를 주입할 수 있습니다 (egov-com-servlet.xml에 등록됨).

## 관련 DB 테이블

| 테이블 | 용도 |
|--------|------|
| COMVNUSERMASTER | 사용자 마스터 (USER_ID, ESNTL_ID, USER_NM 등) |
| COMTNORGNZTINFO | 조직 정보 |
| COMTNEMPLYRSCRTYESTBS | 사용자별 권한(authority) 매핑 |
| COMTNROLEINFO | 역할 정보 (URL 패턴: role_pttrn, role_ty='url'/'regex') |
| COMTNAUTHORROLERELATE | 권한-역할 매핑 |
| COMTNROLES_HIERARCHY | 역할 계층 (선택) |

## permitAllList 예시

인증 없이 허용할 URL 패턴:

| 용도 | 패턴 |
|------|------|
| 정적 리소스 | `/css/**`, `/html/**`, `/images/**`, `/js/**`, `/resource/**` |
| 공통 레이아웃 | `/`, `/index.do`, `/EgovTop.do`, `/EgovBottom.do`, `/EgovLeft.do`, `/EgovContent.do` |
| 로그인/인증 | `/uat/uia/**.do` |
| 접근 거부 페이지 | `/sec/ram/accessDenied.do` |
| 이미지/배너 | `/cmm/fms/getImage.do`, `/uss/ion/bnr/getBannerImage.do` |

## Security 방식 활성화 절차

1. **globals.properties**: `Globals.Auth = security` 설정
2. **egov-security-config.properties**: URL, SQL, permitAllList, jdbcMapClass 등 확인
3. **EgovSessionMapping**: `jdbcUsersByUsernameQuery` 컬럼과 매핑 일치 여부 확인
4. **애플리케이션 재시작**: `EgovWebServletContextListener`가 `security` 프로파일 활성화

## 참고

- [전자정부 위키 - Server Security Authentication](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.10:fdl:server_security:authentication)
- [전자정부 위키 - Server Security XML Schema](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3:fdl:server_security:xmlschema)
- `hash`: 운영 환경에서는 `sha-256`, `bcrypt` 등 암호화 저장 권장
