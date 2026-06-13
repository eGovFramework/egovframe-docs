---
title: "숫자변환"
linkTitle: "숫자변환"
description: "숫자 타입을 문자열이나 데이터 타입으로 변환하는 기능을 제공한다."
url: /common-component/elementary-technology/formatter-util/number-conversion/
menu:
  depth:
    name: "숫자변환"
    weight: 15
    parent: "formatter-util"
---

## 개요

숫자 타입을 문자열이나 데이터 타입으로 변환하는 기능을 제공한다.

## 설명

숫자 타입을 문자열로 변환하는 기능 및 숫자 타입을 데이터 타입으로 변환하는 기능으로 구성되어 있다.

### 관련 소스

| 유형 | 대상 소스 | 설명 |
| --- | --- | --- |
| Service | `egovframework.com.utl.fcc.service.EgovNumberUtil.java` | Number 관련 유틸리티 |
| Controller | `egovframework.com.cmm.web.EgovComUtlController.java` | 테스트용 Controller |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovNumberCnvr.jsp` | 숫자변환 테스트 페이지 |

### 주요 메서드

| 결과값 | 메서드 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getNumToStrCnvr(int srcNumber)` | 문자열 변환 | 숫자 타입을 문자열 타입으로 변환한다. |
| String | `getNumToDateCnvr(int srcNumber)` | 날짜 변환 | 숫자 타입을 날짜 데이터 타입으로 변환한다. |

### 입력 (Input)

- 변환하고자 하는 숫자: `Integer` 타입의 숫자
- Validation 체크: 요소기술 validation 체크

### 출력 (Output)

- `String`

## 사용 방법

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;
...

// 숫자 타입을 문자열 타입으로 변환
int cnvrNumber = Integer.parseInt(safeGetParameter(request,"cnvrNumber"));

String resultStr = EgovNumberUtil.getNumToStrCnvr(cnvrNumber);

// 숫자 타입을 Date 타입으로 변환
int cnvrNumber = Integer.parseInt(safeGetParameter(request,"cnvrNumber"));

// Date 형식으로 변환 후 다시 String 형태로 변환("YYYY-MM-DD")
String resultStr = EgovNumberUtil.getNumToDateCnvr(cnvrNumber);
```

## 참고자료

- N/A
