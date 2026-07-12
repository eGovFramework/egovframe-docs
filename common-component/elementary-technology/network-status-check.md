---
title: "네트워크상태체크"
linkTitle: "네트워크상태체크"
description: "네트워크상태체크"
url: /common-component/elementary-technology/system/network-status-check/
menu:
  depth:
    name: "네트워크상태체크"
    weight: 1
    parent: "system"
---

## 개요

Ping Test를 통해 네트워크 통신가능 여부를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

네트워크상태체크에서 제공하는 기능은 다음과 같다.

1. 네트워크 사용가능 상태 여부를 확인하는 기능 (`true` / `false`)

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovNetworkState.java` | 네트워크 상태 체크 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovNetworkState.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

네트워크상태체크 기능은 `EgovNetworkState` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `getPingTest(String source)` | 네트워크 상태체크 | Ping Test를 통해 통신 가능 여부(`true`/`false`)를 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `source`: String 타입의 IP 주소 (예: `192.168.100.21`)

#### 반환값 정의 (Output)

- boolean 타입: 통신 가능 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovNetworkState;

// 네트워크 상태 체크 (Ping Test)
boolean status = EgovNetworkState.getPingTest("192.168.100.21");
```

내부적으로 `InetAddress.getByName(ip).isReachable(timeout)` 방식으로 도달 가능 여부를 확인한다.

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
