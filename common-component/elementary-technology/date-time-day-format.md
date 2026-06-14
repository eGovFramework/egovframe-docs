---
title: "날짜/시간/요일 포맷변경"
linkTitle: "날짜/시간/요일 포맷변경"
description: "날짜/시간/요일 포맷변경"
url: /common-component/elementary-technology/formatter-util/date-time-day-format/
menu:
  depth:
    name: "날짜/시간/요일 포맷변경"
    weight: 4
    parent: "formatter-util"
---

## 개요

날짜/시간/요일 포맷변경 기능은 입력받은 일자와 시간을 특정 포맷의 문자열로 변환하거나 정수(int) 형태로 변환하여 제공하는 기능이다.

## 주요 개념

### EgovDateUtil 클래스

`EgovDateUtil`은 날짜 및 시간 데이터 처리를 위해 전자정부 표준프레임워크에서 제공하는 유틸리티 클래스다.
주로 문자열 형태의 날짜와 시간을 포맷팅하거나 정수형으로 변환하는 등의 작업을 수행한다.

### 포맷 변환

지정된 날짜(`yyyyMMdd`)와 시간(`HHmm`) 문자열을 입력받아 Java의 `SimpleDateFormat`에 정의된 형식으로 변환한다.
예를 들어 `yyyy-MM-dd`나 `HH:mm` 등 원하는 형태로 변환할 수 있다.

## 관련 문서

- [달력](./calendar.md)

## 설명

### 관련 소스

| 유형 | 대상 소스 | 설명 |
| :--- | :--- | :--- |
| Service | `egovframework.com.utl.fcc.service.EgovDateUtil.java` | Date 처리 관련 유틸리티 클래스 |
| Controller | `egovframework.com.utl.fcc.web.EgovDateUtilController.java` | 테스트용 Controller |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovDateCnvr.jsp` | 테스트 페이지 |

### 주요 메소드

| 결과값 | 메소드 | 설명 |
| :--- | :--- | :--- |
| `String` | `convertDate(String sDate, String sTime, String sFormatStr)` | 입력된 날짜와 시간을 지정한 포맷의 문자열로 변환한다. |
| `int` | `datetoInt(String sDate)` | 입력받은 일자 문자열을 `int` 형으로 변환한다. |
| `int` | `timetoInt(String sTime)` | 입력받은 시간 문자열을 `int` 형으로 변환한다. |

### 입력 파라미터 (Input)

- **일자 (`sDate`)**: String 타입의 날짜 (예: `20090501`)
- **시간 (`sTime`)**: String 타입의 시간 (예: `2035`)
- **포맷 스트링 (`sFormatStr`)**: String 타입의 Date 포맷 스트링 (예: `yyyy년 MM월 dd일 HH시 mm분 ss초`)

### 사용법

`EgovDateUtil` 클래스를 이용하여 다음과 같이 날짜/시간 포맷을 변환할 수 있다.

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

// 1. 날짜와 시간을 원하는 포맷으로 변환
String sDate = "20080820";
String resDate = EgovDateUtil.convertDate(sDate, "0000", "yyyy-MM-dd");

// 2. 시간만 원하는 포맷으로 변환
String sTime = "2030";
String resTime = EgovDateUtil.convertDate("00000101", sTime, "HH:mm");

// 3. 일자 문자열을 정수형(int)으로 변환
int resDateInt = EgovDateUtil.datetoInt(sDate);

// 4. 시간 문자열을 정수형(int)으로 변환
int resTimeInt = EgovDateUtil.timetoInt(sTime);
```

## 참고자료

- [전자정부 표준프레임워크 DokuWiki](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EB%82%A0%EC%A7%9C_%EC%8B%9C%EA%B0%84_%EC%9A%94%EC%9D%BC%EB%B3%80%ED%99%98)
