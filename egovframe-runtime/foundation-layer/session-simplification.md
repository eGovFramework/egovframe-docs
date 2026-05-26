---
title: Session 방식 접근제어
linkTitle: "Session 방식 접근제어"
description: 전자정부 표준프레임워크의 Session 방식 접근제어 간소화서비스를 사용한 세션 기반 인증 및 URL 패턴 기반 권한 관리를 제공한다.
url: /egovframe-runtime/foundation-layer/session-simplification/
menu:
    depth:
        name: Session 방식 접근제어
        weight: 2
        parent: "foundation-layer"
---
# Session 방식 접근제어 간소화서비스

전자정부 표준프레임워크 실행환경 구성요소인 Session 방식 접근제어 간소화서비스를 사용한 세션 방식 접근제어 설정 및 사용법을 정리한 문서입니다.

## 개요

Session 방식 접근제어 간소화서비스는 **Session 방식**으로 URL 패턴별 접근제어 권한관리를 제공합니다. HttpSession 기반 인증과 DB의 역할(Role)-URL 매핑을 이용해 요청 URL에 대한 접근 권한을 검사합니다.

## 라이브러리 적용

### pom.xml 의존성 추가

```xml
<dependency>
    <groupId>org.egovframe.rte</groupId>
    <artifactId>egovframe-rte-fdl-access</artifactId>
</dependency>
```

- 전자정부 Maven 저장소(`https://maven.egovframe.go.kr/maven/`)에서 의존성 해결
- parent POM의 `egovframe.rte.version`에 따라 버전 관리

## 설정 방법

### 1. globals.properties

**경로:** `src/main/resources/egovframework/egovProps/globals.properties`

```properties
# 권한 인증방식 - session 설정 시 egovframe-rte-fdl-access 사용
Globals.Auth = session

# 접근제어 설정 파일 경로 (egov-access 모듈이 참조)
Globals.AccessConfigPath = egovframework/egovProps/conf/egov-access-config.properties
```

### 2. egov-access-config.properties

**경로:** `src/main/resources/egovframework/egovProps/conf/egov-access-config.properties`

| 항목 | 필수 | 설명 |
|------|------|------|
| `id` | O | 접근제어 설정 빈 식별자 |
| `globalAuthen` | O | `session` (Globals.Auth와 동일하게 설정) |
| `mappingPath` | O | 접근제어 적용 URL 패턴 (예: `/**/*.do`) |
| `dataSource` | O | 권한/역할 조회용 DataSource 빈 이름 |
| `loginUrl` | O | 비인증 시 리다이렉트할 로그인 페이지 URL |
| `accessDeniedUrl` | O | 권한 부족 시 리다이렉트할 URL |
| `sqlAuthorityUser` | O | 인증된 사용자의 권한(authority) 조회 쿼리 |
| `sqlRoleAndUrl` | O | Role 및 URL 패턴 매핑 조회 쿼리 |
| `requestMatcherType` | O | 패턴 매칭 방식: `regex`, `ant`, `ciRegex` |
| `excludeList` | O | 접근제어 제외 URL (쉼표 구분) |

**예시 설정:**

```properties
id = egovAccessConfig
globalAuthen = session
mappingPath = /**/*.do
dataSource = dataSource
loginUrl = /uat/uia/egovLoginUsr.do
accessDeniedUrl = /uat/uia/egovLoginUsr.do?auth_error=1
sqlAuthorityUser = select concat(b.user_se, b.user_id) userid, a.author_code authority from comtnemplyrscrtyestbs a, comvnusermaster b where a.scrty_dtrmn_trget_id = b.esntl_id
sqlRoleAndUrl = select a.role_pttrn url, b.author_code authority from comtnroleinfo a, comtnauthorrolerelate b where a.role_code = b.role_code and a.role_ty = 'url' order by a.role_sort
requestMatcherType = regex
excludeList = /css/**, /html/**, /images/**, /js/**, /resource/**, /index.do, /EgovLeft.do, /EgovContent.do, /EgovTop.do, /EgovBottom.do, /uat/uia/**, /validator.do, /uss/umt/**, /EgovModal.do
```

### 3. XML 설정 (대안)

properties 대신 XML namespace로 설정할 경우:

```xml
<beans xmlns:egov-access="http://maven.egovframe.go.kr/schema/egov-access"
       xsi:schemaLocation="...
           http://maven.egovframe.go.kr/schema/egov-access
           http://maven.egovframe.go.kr/schema/egov-access/egov-access-3.10.0.xsd">

    <egov-access:config id="egovAccessConfig"
        globalAuthen="session"
        mappingPath="/**/*.do"
        dataSource="dataSource"
        loginUrl="/uat/uia/egovLoginUsr.do"
        accessDeniedUrl="/uat/uia/egovLoginUsr.do?auth_error=1"
        sqlAuthorityUser="..."
        sqlRoleAndUrl="..."
        requestMatcherType="regex"
        excludeList="/uat/uia/**, /index.do, ..." />
</beans>
```

## Spring 설정

### egov-com-servlet.xml - Component Scan

egovframe-rte-fdl-access 설정 빈을 로드하기 위해 `org.egovframe.rte.fdl.access.config` 패키지를 스캔합니다.

```xml
<context:component-scan base-package="egovframework, org.egovframe.rte.fdl.access.config, org.egovframe.rte.fdl.security">
```

- `Globals.AccessConfigPath`에 지정된 properties 파일을 읽어 접근제어 설정 빈 생성

### egov-com-interceptor.xml - session 프로파일

세션 방식 사용 시 `IpObtainInterceptor`로 로그인 사용자 IP를 기록합니다. URL별 접근제어는 egovframe-rte-fdl-access가 담당합니다.

```xml
<beans profile="session">
    <mvc:interceptors>
        <bean class="egovframework.com.cmm.interceptor.IpObtainInterceptor" />
    </mvc:interceptors>
</beans>
```

### EgovWebServletContextListener - 프로파일 활성화

`Globals.Auth` 값을 Spring Profile에 반영합니다.

```java
System.setProperty("spring.profiles.active", 
    EgovProperties.getProperty("Globals.DbType") + "," + EgovProperties.getProperty("Globals.Auth"));
```

- 예: `mysql,session` → DB 프로파일 + session 프로파일 활성화

### EgovWebApplicationInitializer - session 모드 필터

`Globals.Auth = session`일 때 `EgovLoginPolicyFilter`가 로그인 요청에 적용됩니다.

```java
} else if("session".equals(EgovProperties.getProperty("Globals.Auth").trim())) {
    FilterRegistration.Dynamic egovLoginPolicyFilter = 
        servletContext.addFilter("LoginPolicyFilter", new EgovLoginPolicyFilter());
    egovLoginPolicyFilter.addMappingForUrlPatterns(null, false, "/uat/uia/actionLogin.do");
}
```

## 사용법

### 1. 인증 여부 및 사용자 정보 조회

`EgovUserDetailsHelper`(org.egovframe.rte.fdl.access.service)로 세션의 인증 정보를 조회합니다.

```java
import org.egovframe.rte.fdl.access.service.EgovUserDetailsHelper;

// 인증 여부
boolean isAuthenticated = EgovUserDetailsHelper.isAuthenticated();

// 인증된 사용자 객체 (LoginVO 등)
Object user = EgovUserDetailsHelper.getAuthenticatedUser();

// 사용자 권한 목록 (authority 코드 목록)
List<String> authorities = EgovUserDetailsHelper.getAuthorities();
```

### 2. URL-권한 매칭 (EgovAccessUtil)

컨트롤러나 서비스에서 URL 패턴과 권한 매칭이 필요할 때 사용합니다.

```java
import org.egovframe.rte.fdl.access.interceptor.EgovAccessUtil;

// Ant 패턴 매칭
boolean antMatch = EgovAccessUtil.antMatcher(rolePattern, requestUrl);

// Regex 패턴 매칭
boolean regexMatch = EgovAccessUtil.regexMatcher(rolePattern, requestUrl);
```

### 3. 접근제어 메타데이터 재로딩

권한-롤 매핑 변경 후 서버 재기동 없이 적용하려면 `AuthorityResourceMetadata.reload()`를 호출합니다.

```java
import org.egovframe.rte.fdl.access.bean.AuthorityResourceMetadata;

@Autowired(required = false)
private AuthorityResourceMetadata authorityResourceMetadata;

@RequestMapping("/sec/ram/insertAuthorRole.do")
public String insertAuthorRole(...) {
    // 권한-롤 등록/수정 처리
    ...
    if (authorityResourceMetadata != null) {
        authorityResourceMetadata.reload();
    }
    return "redirect:...";
}
```

### 4. 컨트롤러에서 인증 사용자 주입

`EgovSecurityArgumentResolver`로 메서드 파라미터에 인증 사용자를 주입할 수 있습니다 (egov-com-servlet.xml에 등록됨).

## 관련 DB 테이블

| 테이블 | 용도 |
|--------|------|
| COMTNEMPLYRSCRTYESTBS | 사용자별 권한(authority) 매핑 |
| COMVNUSERMASTER | 사용자 마스터 |
| COMTNROLEINFO | 역할 정보 (URL 패턴: role_pttrn, role_ty='url') |
| COMTNAUTHORROLERELATE | 권한-역할 매핑 |

## excludeList 예시

접근제어에서 제외할 URL 패턴 예시:

| 용도 | 패턴 |
|------|------|
| 정적 리소스 | `/css/**`, `/html/**`, `/images/**`, `/js/**`, `/resource/**` |
| 공통 레이아웃 | `/index.do`, `/EgovLeft.do`, `/EgovContent.do`, `/EgovTop.do`, `/EgovBottom.do`, `/EgovModal.do` |
| 로그인/인증 | `/uat/uia/**` |
| 회원관리 | `/uss/umt/**` |
| 기타 | `/validator.do` |

## 세션 방식 활성화 절차

1. **globals.properties**: `Globals.Auth = session` 설정
2. **egov-access-config.properties**: URL, SQL, excludeList 등 확인
3. **애플리케이션 재시작**: `EgovWebServletContextListener`가 `session` 프로파일 활성화

## 참고

- [전자정부 위키 - Session 방식 접근제어](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte4.2:fdl:access)
- `requestMatcherType`의 `ciRegex`: 대소문자 구분 없는 정규식 매칭
