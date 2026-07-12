---
title: "유효메모리체크"
linkTitle: "유효메모리체크"
description: "유효메모리체크"
url: /common-component/elementary-technology/system/valid-memory-check/
menu:
  depth:
    name: "유효메모리체크"
    weight: 21
    parent: "system"
---

## 개요

시스템에서 사용 가능한 유효메모리를 체크하는 기능을 제공한다. 새로운 프로그램을 실행하기 전에 시스템의 유효 메모리를
체크하여 프로그램 실행 여부를 판단할 때 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

유효메모리체크에서 제공하는 기능은 다음과 같다.

1. 시스템에서 사용 가능한 유효메모리를 체크하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovSysInfo.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

유효메모리체크 기능은 `EgovSysInfo` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `checkMoryCpcty(long memory)` | 유효메모리체크 | 특정 프로그램을 실행시키기 위한 메모리용량이 충분한지 확인한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `memory`: long 타입의 사용할 메모리 사이즈 (MB 단위, 예: `300`)

#### 반환값 정의 (Output)

- boolean 타입: 유효메모리 충분 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

// 프로그램 실행을 위한 유효 메모리 체크
long memory = 300L;
boolean result = EgovSysInfo.checkMoryCpcty(memory);
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
