---
title: "날짜/시간/요일 유효성체크"
linkTitle: "날짜/시간/요일 유효성체크"
description: "날짜/시간/요일 유효성체크"
url: /common-component/elementary-technology/formatter-util/date-time-day-validation/
menu:
  depth:
    name: "날짜/시간/요일 유효성체크"
    weight: 3
    parent: "formatter-util"
---

<!-- markdownlint-disable MD025 -->

# 날짜/시간/요일 유효성체크

## 개요

주어진 일자, 시간, 요일이 유효한 형식 및 값인지 확인하는 기능을 제공한다.

## 설명

입력된 날짜, 시간, 요일이 실제로 존재하는 유효한 값인지, 혹은 특정 날짜의 요일과 일치하는지 등을 검증한다.

### 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.fcc.service.EgovDateUtil.java | 날짜/시간 관련 처리 유틸리티 클래스 | |
| Controller | egovframework.com.utl.fcc.web.EgovDateUtilController.java | 테스트용 Controller 클래스 | |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovDateValidCeck.jsp | 테스트용 JSP 페이지 | |

### 메소드

| 결과값 | 메소드 | 설명 |
| --- | --- | --- |
| boolean | validDate(String sDate) | 입력일자가 유효한 날짜인지 확인한다. (예: "20090501") |
| boolean | validTime(String sTime) | 입력시간이 유효한 시간인지 확인한다. (예: "2035") |
| boolean | validDate(String sDate, int sWeek) | 입력일자의 요일이 지정한 요일(1~7: 일~토)과 일치하는지 확인한다. |

### 입력 매개변수 (Input)

- **일자**: `String` 타입의 날짜 문자열 (예: "20090501")
- **시간**: `String` 타입의 시간 문자열 (예: "2035")
- **요일**: `int` 타입의 요일 (1~7: 일요일~토요일) (예: 1은 일요일을 의미함)

### 반환값 (Output)

- `boolean`: 유효성 검증 통과 여부 (유효하면 `true`, 그렇지 않으면 `false` 반환)

## 사용 방법

`EgovDateUtil` 클래스의 정적 메소드를 호출하여 날짜, 시간, 요일의 유효성을 검증한다.

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

// 1. 날짜 유효성 체크
String sDate = "20080820";
boolean resultDate = EgovDateUtil.validDate(sDate);

// 2. 시간 유효성 체크
String sTime = "2030";
boolean resultTime = EgovDateUtil.validTime(sTime);

// 3. 요일 유효성 체크 (1: 일요일 ~ 7: 토요일)
int iWeek = 1; 
boolean resultWeek = EgovDateUtil.validDate(sDate, iWeek);
```

## 관련 문서

- [포맷터/유틸리티 개요](./formatter-util.md) — 포맷/계산/변환(Format/Calc/Convert) 요소기술 패키지는 공통컴포넌트 내에서 데이터의 형식을 조정하거나, 날짜, 숫자, 문자열 등에 대한 계산 및 변환 작업을 수행하는 유틸리티 기능을 제공한다.
- [날짜/시간/요일 계산](./date-time-day-calculation.md) — 주어진 일자, 시간을 계산하는 기능을 제공한다.
- [날짜/시간/요일 변환](./date-time-day-conversion.md) — 날짜/시간/요일 변환은 주어진 날짜와 시간 정보를 원하는 포맷의 문자열로 변환하거나, 날짜/시간 문자열을 정수(int)형으로 변환하는 등의 편의 기능을 제공하는 요소기술이다.
- [날짜/시간/요일 포맷변경](./date-time-day-format.md) — 날짜/시간/요일 포맷변경 기능은 입력받은 일자와 시간을 특정 포맷의 문자열로 변환하거나 정수(int) 형태로 변환하여 제공하는 기능이다.
