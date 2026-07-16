---
title: "날짜/시간/요일 계산"
linkTitle: "날짜/시간/요일 계산"
description: "날짜/시간/요일 계산"
url: /common-component/elementary-technology/formatter-util/date-time-day-calculation/
menu:
  depth:
    name: "날짜/시간/요일 계산"
    weight: 1
    parent: "formatter-util"
---

<!-- markdownlint-disable MD013 MD025 -->

# 날짜/시간/요일 계산

## 개요

주어진 일자, 시간을 계산하는 기능을 제공한다.

## 주요 개념

### EgovDateUtil 클래스

`EgovDateUtil`은 날짜 및 시간 데이터 처리를 위해 전자정부 표준프레임워크에서 제공하는 유틸리티 클래스다.
주로 문자열 형태의 날짜와 시간에 대한 가감 연산 및 요일 확인 등의 작업을 수행한다.

### 날짜/시간 계산

지정된 날짜(`yyyyMMdd`)와 시간(`HHmm`) 문자열에 대해 연, 월, 일, 시, 분 단위를 지정된 수치만큼 가감하고, 계산된 결과를 원하는 포맷의 문자열로 반환하는 기능이다.

### 요일 계산

지정된 날짜 문자열에 대해 연, 월, 일 단위를 지정된 수치만큼 계산한 후, 해당 일자의 요일을 확인하는 기능이다.

## 관련 문서

- [포맷터/유틸리티 개요](./formatter-util.md) — 포맷/계산/변환(Format/Calc/Convert) 요소기술 패키지는 공통컴포넌트 내에서 데이터의 형식을 조정하거나, 날짜, 숫자, 문자열 등에 대한 계산 및 변환 작업을 수행하는 유틸리티 기능을 제공한다.
- [날짜/시간/요일 변환](./date-time-day-conversion.md) — 날짜/시간/요일 변환은 주어진 날짜와 시간 정보를 원하는 포맷의 문자열로 변환하거나, 날짜/시간 문자열을 정수(int)형으로 변환하는 등의 편의 기능을 제공하는 요소기술이다.
- [날짜/시간/요일 포맷변경](./date-time-day-format.md) — 날짜/시간/요일 포맷변경 기능은 입력받은 일자와 시간을 특정 포맷의 문자열로 변환하거나 정수(int) 형태로 변환하여 제공하는 기능이다.
- [날짜/시간/요일 유효성체크](./date-time-day-validation.md) — 주어진 일자, 시간, 요일이 유효한 형식 및 값인지 확인하는 기능을 제공한다.

## 설명

입력일시에 계산될 연, 월, 일, 시간을 가감하여 계산하는 기능을 제공한다.

### 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| :--- | :--- | :--- | :--- |
| Service | `egovframework.com.utl.fcc.service.EgovDateUtil.java` | Date 처리 관련 유틸리티 클래스 | |
| Controller | `egovframework.com.utl.fcc.web.EgovDateUtilController.java` | 테스트용 Controller 클래스 | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovWeekCalc.jsp` | 테스트 페이지 | |

### 주요 메소드

| 결과값 | 메소드 | 설명 |
| :--- | :--- | :--- |
| `String` | `addYMDtoDayTime(String sDate, String sTime, int year, int month, int day, int hour, int minute, String formatStr)` | 입력일시에 연, 월, 일, 시, 분을 가감하여 계산된 결과를 포맷팅된 문자열로 반환한다. |
| `String` | `addYMDtoWeek(String sDate, int year, int month, int day)` | 입력일자에 연, 월, 일을 가감한 후 최종 일자의 요일을 반환한다. |

### 입력 매개변수 (Input)

- **일자 (`sDate`)**: `String` 타입의 날짜 문자열 (예: `"20090501"`)
- **시간 (`sTime`)**: `String` 타입의 시간 문자열 (예: `"2035"`)
- **연 (`year`)**: `int` 타입의 가감할 연도 수 (예: `1`)
- **월 (`month`)**: `int` 타입의 가감할 월 수 (예: `2`)
- **일 (`day`)**: `int` 타입의 가감할 일 수 (예: `10`)
- **시 (`hour`)**: `int` 타입의 가감할 시간 수 (예: `5`)
- **분 (`minute`)**: `int` 타입의 가감할 분 수 (예: `30`)
- **포맷 스트링 (`formatStr`)**: `String` 타입의 Date 포맷 스트링 (예: `"yyyy년 MM월 dd일 HH시 mm분 ss초"`)

### 반환값 (Output)

- `String`: 가감 연산이 완료되어 지정한 포맷으로 변환된 날짜/시간 또는 요일 문자열

## 사용 방법

`EgovDateUtil` 클래스를 이용하여 다음과 같이 날짜/시간의 가감 연산 및 요일을 계산할 수 있다.

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

// 1. 날짜 가감 계산 (예: 2008년 8월 20일에 5일을 더함)
String sDate = "20080820";
int sDay = 5;
String resDate = EgovDateUtil.addYMDtoDayTime(sDate, "0000", 0, 0, sDay, 0, 0, "yyyyMMdd");

// 2. 시간 가감 계산 (예: 2008년 8월 20일 20시 30분에 2시간을 더함)
String sTime = "2030";
int sHour = 2;
String resDateTime = EgovDateUtil.addYMDtoDayTime(sDate, sTime, 0, 0, 0, sHour, 0, "yyyyMMddHHmm");

// 3. 요일 계산 (예: 2008년 8월 20일에 1년 5일을 더한 후 요일 계산)
int sYear = 1;
int sMonth = 0;
int sDayOffset = 5;
String resWeek = EgovDateUtil.addYMDtoWeek(sDate, sYear, sMonth, sDayOffset);
```

## 참고자료

- [전자정부 표준프레임워크 DokuWiki](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EB%82%A0%EC%A7%9C_%EC%8B%9C%EA%B0%84_%EC%9A%94%EC%9D%BC%EA%B3%84%EC%82%B0)
