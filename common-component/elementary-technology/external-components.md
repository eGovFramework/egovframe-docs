---
title: "외부 추가 컴포넌트"
linkTitle: "외부 추가 컴포넌트"
description: "외부 추가 컴포넌트"
url: /common-component/elementary-technology/external-components/
menu:
  depth:
    weight: 2
    parent: "elementary-technology"
    identifier: "external-components"
---

## 개요

전자정부 표준프레임워크 공통컴포넌트의 기본 제공 범위를 넘어, 외부 시스템 연동 및 특수 목적의 기능을 추가로
제공하는 컴포넌트 집합이다. 소셜 로그인(OAuth), LDAP 조직도 연동 등 외부 서비스 및 표준과 연계하는 기능을
포함한다.

## 설명

### 주요 컴포넌트 목록

외부 추가 컴포넌트에서 제공하는 주요 기능은 다음과 같다.

| 컴포넌트 | 패키지 경로 | 설명 |
| --- | --- | --- |
| 소셜 로그인 (OAuth) | `egovframework.com.ext.oauth` | 네이버, 구글, 카카오 등 OAuth 2.0 기반 소셜 계정 로그인 연동 기능 |
| LDAP 조직도 관리 | `egovframework.com.ext.ldapumt` | LDAP 서버와 연동하여 조직도 정보(조회/추가/수정/삭제)를 관리하는 기능 |

### 소셜 로그인 (OAuth)

네이버, 구글, 카카오 등 외부 OAuth 2.0 인증 서버를 통해 사용자 로그인을 처리한다.
별도의 회원가입 절차 없이 기존 소셜 계정으로 시스템에 로그인할 수 있다.

#### 소셜 로그인 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.ext.oauth.web.EgovSignupController.java` | 소셜 로그인 가입 처리 컨트롤러 | |
| Service | `egovframework.com.ext.oauth.service.OAuthLogin.java` | OAuth 인증 처리 서비스 | |
| Config | `context-oauth.xml` | OAuth 인증 설정 파일 | |

#### 소셜 로그인 환경 설정

소셜 로그인 사용을 위해 `globals.properties`에 아래 정보를 등록한다.

```properties
# 네이버 OAuth 설정
Globals.naver.client.id     = {naver_client_id}
Globals.naver.client.secret = {naver_client_secret}
Globals.naver.redirect.url  = {redirect_url}

# 구글 OAuth 설정
Globals.google.client.id     = {google_client_id}
Globals.google.client.secret = {google_client_secret}
Globals.google.redirect.url  = {redirect_url}

# 카카오 OAuth 설정
Globals.kakao.client.id    = {kakao_client_id}
Globals.kakao.redirect.url = {redirect_url}
```

### LDAP 조직도 관리

LDAP(Lightweight Directory Access Protocol) 서버와 연동하여 조직도 정보를 조회하고 관리한다.
행정안전부의 유통표준 LDAP 스키마(UCORG2)를 지원한다.

#### LDAP 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.ext.ldapumt.service.EgovOrgManageLdapService.java` | LDAP 조직도 관리 서비스 인터페이스 | |
| ServiceImpl | `egovframework.com.ext.ldapumt.service.impl.EgovOrgManageLdapServiceImpl.java` | LDAP 조직도 관리 서비스 구현체 | |

#### LDAP 환경 설정

`globals.properties`에 LDAP 서버 접속 정보를 등록한다.

```properties
# LDAP 서버 설정
Globals.ldap.url      = ldap://ldap.example.go.kr:389
Globals.ldap.baseDn   = dc=example,dc=go,dc=kr
Globals.ldap.userDn   = cn=admin,dc=example,dc=go,dc=kr
Globals.ldap.password = {ldap_password}
```

## 참고자료

- [소셜 로그인 (네이버/구글/카카오)](./social_login_naver_google_kakao.md)
- [LDAP](./ldap.md)
