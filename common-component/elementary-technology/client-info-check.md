---
title: "클라이언트정보확인"
linkTitle: "클라이언트정보확인"
description: "클라이언트정보확인"
url: /common-component/elementary-technology/system/client-info-check/
menu:
  depth:
    name: "클라이언트정보확인"
    weight: 22
    parent: "system"
---

## 개요

리퀘스트(HttpServletRequest)를 요청한 클라이언트의 웹 브라우저 버전, 클라이언트 IP 주소를 리턴하는 기능을 제공한다.

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

클라이언트 정보 확인 기능은 `HttpServletRequest` 객체를 기반으로 요청을 보낸 클라이언트의 정보를 조회하는 기능을 제공한다.

제공하는 주요 기능은 다음과 같다.

- 클라이언트(Client)의 IP 주소 조회
- 클라이언트(Client)의 운영체제(OS) 종류 및 버전 조회
- 클라이언트(Client)의 웹 브라우저 종류 및 버전 조회

### 활용 예시

클라이언트 정보 확인 기능은 다음과 같은 상황에서 활용할 수 있다.

- 접속 사용자의 IP 주소를 기록하는 경우
- 운영체제(OS)에 따라 기능을 분기하는 경우
- 브라우저 종류에 따라 화면을 최적화하는 경우
- 접속 환경 분석 및 통계 정보를 수집하는 경우
- 보안 로그 및 접속 이력을 관리하는 경우

### 관련소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovClntInfo.java` | 클라이언트 정보확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovClntInfo.jsp` | 테스트 페이지 | |

### 메소드

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getClntIP(HttpServletRequest request)` | 클라이언트 IP 주소 조회 | 요청 정보를 기반으로 클라이언트의 IP 주소를 반환한다. |
| String | `getClntOsInfo(HttpServletRequest request)` | 운영체제 정보 조회 | 요청 정보를 기반으로 클라이언트의 운영체제 정보를 반환한다. |
| String | `getClntWebKind(HttpServletRequest request)` | 브라우저 종류 조회 | 요청 정보를 기반으로 클라이언트의 브라우저 종류를 반환한다. |
| String | `getClntWebVer(HttpServletRequest request)` | 브라우저 버전 조회 | 요청 정보를 기반으로 클라이언트의 브라우저 버전을 반환한다. |

## 환경설정

해당사항 없음

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovClntInfo;

// 1. IP 조회
String ipAddr = EgovClntInfo.getClntIP(request);
// 2. OS 정보 조회
String osInfo = EgovClntInfo.getClntOsInfo(request);
// 3. 브라우저 종류 조회
String webKind = EgovClntInfo.getClntWebKind(request);
// 4. 브라우저 버전 조회
String webVer = EgovClntInfo.getClntWebVer(request);
```

## 참고자료

해당사항 없음
