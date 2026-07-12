---
title: "로그인세션정보체크"
linkTitle: "로그인세션정보체크"
description: "로그인세션정보체크"
url: /common-component/elementary-technology/system/login-session-check/
menu:
  depth:
    name: "로그인세션정보체크"
    weight: 39
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

로그인세션정보체크는 로그인한 세션정보를 체크하여 정의한 페이지로 이동하게 하는 기능을 제공한다.

## 설명

로그인세션정보체크는 세션정보에 사용자 정의 페이지를 조회, 설정, 화면이동하는 기능을 수반한다.

1. **로그인세션정보체크**: 세션정보에 사용자 정의 페이지를 설정하고, 화면이동을 한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.rsc.web.EgovLoginSesionController.java` | 로그인세션정보체크를 위한 컨트롤러 클래스 |
| Util | `egovframework.com.utl.sys.rsc.service.EgovLoginSesionCeckUtil.java` | 로그인세션정보체크를 위한 Util 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/rsc/EgovLoginSesionCheck.jsp` | 로그인세션정보체크 페이지 |

## 관련화면 및 수행매뉴얼

### 로그인세션정보 체크

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/rsc/loginSessionView.do | checkLoginSessionView | |
| 설정 | /utl/sys/rsc/setLoginSession.do | setLoginSession | |

로그인세션정보는 현재 세션URL을 조회하고, URL 항목에 세션으로 설정할 URL을 입력한 후 설정 버튼을 선택하여 세션에 등록한다.
이동 버튼은 현재 설정된 세션URL로 새창을 띄워 해당 화면을 호출한다.

- 조회: 현재 설정된 세션정보를 조회한다.
- 설정: 세션정보에 새로운 URL을 설정한다.
- 이동: 기 설정된 세션 URL로 화면을 이동한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
