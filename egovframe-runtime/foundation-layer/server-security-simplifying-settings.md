---
title: 설정 간소화
linkTitle: "설정 간소화"
description: 전자정부 표준프레임워크 3.0부터 Server Security 설정을 간소화할 수 있는 기능을 제공하며, XML Schema를 통해 필요한 설정만 추가하면 된다. **Security Config**는 로그인, 로그아웃, 권한 관리, 동시 세션, 패스워드 해시 방식 등 다양한 보안 설정을 간단히 설정할 수 있게 해준다. 또한, **Security Object Config**를 통해 URL, Method, Pointcut 방식의 권한 설정과 계층적 역할 관리도 쉽게 구성할 수 있다.
url: /egovframe-runtime/foundation-layer/server-security/server-security-simplifying-settings/
menu:
    depth:
        name: 설정 간소화
        weight: 4
        parent: "serverSecurity"
---
# 설정 간소화

## 개요
표준프레임워크 3.0부터 Server security에 대하여 설정을 간소화 할 수 있는 방법을 제공한다.
내부적으로 필요한 설정을 가지고 있고, XML Schema를 통해 필요한 설정만을 추가할 수 있도록 제공한다.

## XML namespace 및 schema 설정
설정 간소화 기능을 사용하기 위해서는 다음과 같은 xml 선언이 필요하다.
**4.1 > 4.2 업그레이드 시 xsd 변경(egov-security-4.1.0.xsd > egov-security-4.2.0.xsd)**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:egov-security="http://maven.egovframe.go.kr/schema/egov-security"
	xmlns:security="http://www.springframework.org/schema/security"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.0.xsd
		http://www.springframework.org/schema/security http://www.springframework.org/schema/security/spring-security.xsd
		http://maven.egovframe.go.kr/schema/egov-security http://maven.egovframe.go.kr/schema/egov-security/egov-security-4.2.0.xsd">
```

## Security Config 설정
Security에 대한 기본 설정 정보를 제공한다.

예:
```xml
<egov-security:config id="securityConfig"
	loginUrl="/uat/uia/egovLoginUsr.do"
	logoutSuccessUrl="/EgovContent.do"
	loginFailureUrl="/uat/uia/egovLoginUsr.do?login_error=1"
	accessDeniedUrl="/sec/ram/accessDenied.do"
 
	dataSource="egov.dataSource"
	jdbcUsersByUsernameQuery="SELECT USER_ID, ESNTL_ID AS PASSWORD, 1 ENABLED, USER_NM, USER_ZIP,
                                  USER_ADRES, USER_EMAIL, USER_SE, ORGNZT_ID, ESNTL_ID,
                                  (select a.ORGNZT_NM from COMTNORGNZTINFO a where a.ORGNZT_ID = m.ORGNZT_ID) ORGNZT_NM
                                  FROM COMVNUSERMASTER m WHERE CONCAT(USER_SE, USER_ID) = ?"
	jdbcAuthoritiesByUsernameQuery="SELECT A.SCRTY_DTRMN_TRGET_ID USER_ID, A.AUTHOR_CODE AUTHORITY
                                        FROM COMTNEMPLYRSCRTYESTBS A, COMVNUSERMASTER B
                                        WHERE A.SCRTY_DTRMN_TRGET_ID = B.ESNTL_ID AND B.USER_ID = ?"
	jdbcMapClass="egovframework.com.sec.security.common.EgovSessionMapping"
 
	requestMatcherType="regex"
	hash="plaintext"
	hashBase64="false"
 
	concurrentMaxSessons="1"
	concurrentExpiredUrl="/EgovContent.do"
	errorIfMaximumExceeded="false"
 
	defaultTargetUrl="/EgovContent.do"
	alwaysUseDefaultTargetUrl="true"
 
	sniff="true"
	xframeOptions="SAMEORIGIN" 
	xssProtection="true" 
	cacheControl="false"
	csrf="false"
	csrfAccessDeniedUrl="/egovCSRFAccessDenied.do"
/>
```

### 속성 설명
| 속성                             | 설명                                                    | 필수여부 | 비고                                                                                   |
| ------------------------------ |-------------------------------------------------------| ---- | ------------------------------------------------------------------------------------ |
| loginUrl                       | 로그인 페이지 URL                                           | 필수   |                                                                                      |
| logoutSuccessUrl               | 로그아웃 처리 시 호출되는 페이지 URL                                | 필수   |                                                                                      |
| loginFailureUrl                | 로그인 실패 시 호출되는 페이지 URL                                 | 필수   |                                                                                      |
| accessDeniedUrl                | 권한이 없는 경우 호출되는 페이지 URL                                | 필수   |                                                                                      |
| dataSource                     | DBMS 설정 dataSource                                    | 선택   | 미지정시 'dataSource' bean name 사용                                                       |
| jdbcUsersByUsernameQuery       | 인증에 사용되는 query                                        | 선택   | default : “select user_id, password, enabled, users.\* from users where user_id = ?” |
| jdbcAuthoritiesByUsernameQuery | 인증된 사용자의 권한(authority) 조회 query                       | 선택   | default : “select user_id, authority from authorites where user_id = ?”              |
| jdbcMapClass                   | 사용자 정보 mapping 처리 class                               | 선택   | default : egovframework.rte.fdl.security.userdetails.DefaultMapUserDetailsMapping    |
| requestMatcherType             | 패턴 매칭 방식(regex, ant, ciRegex: case-insensitive regex) | 선택   | default : regex                                                                      |
| hash                           | 패스워드 저장 방식 (sha-256, plaintext, sha, md5, bcrypt)     | 선택   | default : sha-256                                                                    |
| hashBase64                     | hash값 base64 인코딩 사용 여부                                | 선택   | default : true                                                                       |
| concurrentMaxSessons           | 동시 접속가능 연결 수                                          | 선택   | default : 999                                                                        |
| concurrentExpiredUrl           | expired된 경우 redirect되는 페이지 URL                        | 선택   |                                                                                      |
| errorIfMaximumExceeded         | 중복 로그인 방지 옵션                                          | 필수   | default : false                                                                      |
| defaultTargetUrl               | 로그인 성공시 redirect되는 페이지 URL                            | 선택   | 미지정시 처음 접속하고자 했던 페이지 URL로 redirect됨                                                  |
| alwaysUseDefaultTargetUrl      | 로그인 이후 설정한 페이지로 이동하게 하는 옵션                            | 필수   | default : true                                                                       |
| sniff                          | 선언된 콘텐츠 유형으로부터 벗어난 응답에 대한 브라우저의 MIME 가로채기를 방지 여부      | 필수   | default : true                                                                       |
| xframeOptions                  | sniff 옵션 이 ture 일때 X-Frame-Options 범위설정               | 선택   | DENY, SAMEORIGIN                                                                     |
| xssProtection                  | XSS Protection 기능의 사용 여부                              | 필수   | default : true                                                                       |
| cacheControl                   | 캐쉬 비활성화 여부 옵션                                         | 필수   | default : false                                                                      |
| csrf                           | spring security의 csrf 기능 사용 여부                        | 필수   | default : false                                                                      |
| csrfAccessDeniedUrl            | 토큰 검증이 실패했을 경우 호출되는 페이지 URL                           | 필수   |                                                                                      |
| useExpressions                 | Spring 표현 언어(SpEL) 설정 옵션                              | 선택   | default : false                                                                      |

- DefaultMapUserDetailsMapping : VO 없이 Map 방식으로 매핑을 처리함 (jdbcUsersByUsernameQuery 상에 지정된 컬럼에 대하여 camel case 방식으로 Hash Map 키 생성 처리)
- useExpressions 속성은 사용할 경우 설정 추가 필요
  
## Security Config Initializer 설정
Security에 대한 초기화 처리 정보를 제공한다.

예:

```xml
<egov-security:initializer
	id="initializer"
	supportPointcut="true"
/>
```

### 속성 설명
| 속성              | 설명                | 필수여부 | 비고              |
| --------------- | ----------------- | ---- | --------------- |
| supportPointcut | pointcut 방식 지원 여부 | 선택   | default : false |
| supportMethod   | method 방식 지원 여부   | 선택   | default : true  |

## Security Object Config 설정
Security에 대한 기본 query 설정 정보를 제공한다.

예:

```xml
<egov-security:secured-object-config
	id="securedObjectConfig"
	roleHierarchyString="
			ROLE_ADMIN > ROLE_USER
			ROLE_USER > ROLE_RESTRICTED
			ROLE_RESTRICTED > IS_AUTHENTICATED_FULLY
			IS_AUTHENTICATED_FULLY >	IS_AUTHENTICATED_REMEMBERED
			IS_AUTHENTICATED_REMEMBERED > IS_AUTHENTICATED_ANONYMOUSLY"
	sqlRolesAndUrl="
			SELECT auth.URL url, code.CODE_NM authority
			FROM RTETNAUTH auth, RTETCCODE code
			WHERE code.CODE_ID = auth.MNGR_SE"
/>
```
### 속성 설명
| 속성                            | 설명                                         | 필수여부 | 비고                                   |
| ----------------------------- | ------------------------------------------ | ---- | ------------------------------------ |
| roleHierarchyString           | 계층처리를 위한 설정 문자열 지정                         | 선택   | 미지정시 DB로부터 지정된 설정정보 지정               |
| sqlRolesAndUrl                | URL 방식 role 지정 query                       | 선택   | 미지정시 SecuredObjectDAO의 기본 query가 처리됨 |
| sqlRolesAndMethod             | method 방식 role 지정 query                    | 선택   | 〃                                    |
| sqlRolesAndPointcut           | pointcut 방식 role 지정 query                  | 선택   | 〃                                    |
| sqlRegexMatchedRequestMapping | request 마다 best matching url 보호자원 지정 query | 선택   | 〃                                    |
| sqlHierarchicalRoles          | 계층처리를 위한 query                             | 선택   | 〃                                    |