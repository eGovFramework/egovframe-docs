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

① 클라이언트(Client)의 IP 주소를 가지고 오는 기능.
② 클라이언트(Client)의 운영체제 종류 및 버전을 가지고 오는 기능
③ 클라이언트(Client)의 웹 브라우저 종류 및 버전을 가지고 오는 기능

### 관련소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.service.EgovClntInfo.java` | 클라이언트 정보확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovClntInfo.jsp` | 테스트 페이지 | |

### 메소드

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getClntIP(HttpServletRequest request)` | IP주소조회 | 요청 정보를 통해 클라이언트 IP주소 리턴 |
| String | `getClntOsInfo(HttpServletRequest request)` | OS정보조회 | 요청 정보를 통해 클라이언트 OS정보 리턴 |
| String | `getClntWebKind(HttpServletRequest request)` | 브라우저종류조회 | 요청 정보를 통해 클라이언트 브라우저 종류 리턴 |
| String | `getClntWebVer(HttpServletRequest request)` | 브라우저버전조회 | 요청 정보를 통해 클라이언트 브라우저 버전 리턴 |

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
