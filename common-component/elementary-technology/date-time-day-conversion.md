---
title: "날짜/시간/요일 변환"
linkTitle: "날짜/시간/요일 변환"
description: "날짜/시간/요일 변환"
url: /common-component/elementary-technology/formatter-util/date-time-day-conversion/
menu:
  depth:
    name: "날짜/시간/요일 변환"
    weight: 2
    parent: "formatter-util"
---

<!-- markdownlint-disable MD025 -->

# 날짜/시간/요일 변환

## 개요

날짜/시간/요일 변환은 주어진 날짜와 시간 정보를 원하는 포맷의 문자열로 변환하거나,
날짜/시간 문자열을 정수(int)형으로 변환하는 등의 편의 기능을 제공하는 요소기술이다.

## 주요 개념

날짜/시간/요일 변환 유틸리티 클래스인 `EgovDateUtil`은 공통컴포넌트 내에서 날짜 데이터를 효율적으로
다루기 위해 다음과 같은 기능을 핵심 개념으로 구현하고 있다.

### 날짜/시간 포맷 변환

8자리 날짜 문자열(yyyyMMdd)과 4자리 또는 6자리 시간 문자열(HHmm/HHmmss)을 사용자가 원하는
포맷 형식(예: `yyyy-MM-dd HH:mm:ss`)으로 재구성하여 반환한다.

### 타임존 및 포맷 변환

원본 날짜 문자열의 포맷을 지정하고, 이를 다른 포맷으로 변환함과 동시에 원하는 타임존(TimeZone)
정보를 반영하여 날짜를 변환하는 기능을 제공한다.

### 데이터 타입 변환

날짜 문자열이나 시간 문자열을 데이터베이스 쿼리 연산이나 크기 비교에 유용하도록 정수(`int`) 타입으로
변환하는 기능을 제공한다.

### 요일 명칭 변환

영문 요일명(예: `SUN`, `MON` 등)을 한글 요일명(예: `일요일`, `월요일` 등)으로 변환하여
화면에 출력하기 적절한 형태로 제공한다.

## 관련 문서

- [날짜/시간/요일 계산](./date-time-day-calculation.md) — 주어진 일자, 시간을 계산하는 기능을 제공한다.
- [날짜/시간/요일 검증](./date-time-day-validation.md) — 주어진 일자, 시간, 요일이 유효한 형식 및 값인지 확인하는 기능을 제공한다.
- [날짜/시간/요일 포맷](./date-time-day-format.md) — 날짜/시간/요일 포맷변경 기능은 입력받은 일자와 시간을 특정 포맷의 문자열로 변환하거나 정수(int) 형태로 변환하여 제공하는 기능이다.
- [랜덤날짜 구하기](./random-date.md) — 랜덤 날짜는 지정한 두 일자 사이의 임의의 일자를 생성하는 요소기술이다. 테스트 데이터 생성 등에 활용할 수 있다.

## 설명

날짜/시간/요일 변환 요소기술은 `egovframework.com.utl.fcc.service.EgovDateUtil` 클래스 내의
정적 메서드를 통해 사용 가능하다. 주요 제공 메서드 및 사용 방법은 다음과 같다.

### 주요 클래스 및 파일

- **유틸리티 클래스**: `egovframework.com.utl.fcc.service.EgovDateUtil.java`
- **테스트 JSP 페이지**: `/WEB-INF/jsp/egovframework/com/cmm/utl/EgovDateCnvr.jsp`

### 메서드 상세 설명

#### 1. 날짜 및 시간 포맷 변환 (convertDate)

입력받은 날짜와 시간 문자열을 지정된 형식의 문자열로 변환한다.

##### convertDate 메서드 정의

```java
public static String convertDate(String sDate, String sTime, String sFormatStr)
```

##### convertDate 매개변수

- `sDate`: 변환 대상 날짜 문자열 (예: `"20080820"`)
- `sTime`: 변환 대상 시간 문자열 (예: `"2030"`)
- `sFormatStr`: 적용할 포맷 형식 스트링 (예: `"yyyy-MM-dd HH:mm"`, `"yyyy년 MM월 dd일 HH시 mm분"`)

##### convertDate 반환값

포맷이 적용된 날짜/시간 문자열

##### convertDate 예제

```java
String date = "20080820";
String time = "2030";
String format = "yyyy년 MM월 dd일 HH시 mm분 ss초";

String result = EgovDateUtil.convertDate(date, time, format);
// 결과: "2008년 08월 20일 20시 30분 00초"
```

#### 2. 원본 포맷 정의 및 타임존 변환 (convertDate)

특정 포맷을 가진 원본 날짜 문자열을 다른 포맷으로 변환하며, 지정된 타임존으로 시간을 변환한다.

##### convertDate (타임존) 메서드 정의

```java
public static String convertDate(String strSource, String fromDateFormat, String toDateFormat, String strTimeZone)
```

##### convertDate (타임존) 매개변수

- `strSource`: 변환 대상 원본 날짜 문자열 (예: `"20130820"`)
- `fromDateFormat`: 원본 날짜 문자열의 포맷 (예: `"yyyyMMdd"`)
- `toDateFormat`: 변환하고자 하는 타임존 반영 포맷 (예: `"yyyy-MM-dd HH:mm:ss"`)
- `strTimeZone`: 대상 타임존 아이디 (예: `"GMT+9"`, `"America/New_York"`. 빈 문자열일 경우 기본 타임존 유지)

##### convertDate (타임존) 반환값

타임존 및 변경된 포맷이 적용된 날짜 문자열

##### convertDate (타임존) 예제

```java
String src = "20130820120000";
String fromFormat = "yyyyMMddHHmmss";
String toFormat = "yyyy-MM-dd HH:mm:ss";
String timeZone = "America/New_York";

String result = EgovDateUtil.convertDate(src, fromFormat, toFormat, timeZone);
```

#### 3. 영문 요일명의 국문 변환 (convertWeek)

영문으로 표현된 3자리 요일 문자열을 해당하는 한글 요일 명칭으로 변환한다. 대소문자를 구분하지 않는다.

##### convertWeek 메서드 정의

```java
public static String convertWeek(String sWeek)
```

##### convertWeek 매개변수

- `sWeek`: 영문 요일명 문자열 (`"SUN"`, `"MON"`, `"TUE"`, `"WED"`, `"THU"`, `"FRI"`, `"SAT"`)

##### convertWeek 반환값

변환된 한글 요일 문자열 (예: `"일요일"`, `"월요일"` 등. 유효하지 않은 입력의 경우 빈 문자열 반환)

##### convertWeek 예제

```java
String engWeek = "SUN";
String korWeek = EgovDateUtil.convertWeek(engWeek);
// 결과: "일요일"
```

#### 4. 날짜 문자열의 정수형 변환 (datetoInt)

`"yyyyMMdd"` 형태의 8자리 날짜 문자열을 크기 비교 연산 등에 용이하도록 `int` 타입으로 변환한다.

##### datetoInt 메서드 정의

```java
public static int datetoInt(String sDate)
```

##### datetoInt 매개변수

- `sDate`: 변환할 날짜 문자열 (예: `"20080820"`)

##### datetoInt 반환값

정수형 날짜 데이터

##### datetoInt 예제

```java
String dateStr = "20080820";
int dateInt = EgovDateUtil.datetoInt(dateStr);
// 결과: 20080820
```

#### 5. 시간 문자열의 정수형 변환 (timetoInt)

`"HHmmss"` 형태의 시간 문자열을 크기 비교 연산 등에 용이하도록 `int` 타입으로 변환한다.

##### timetoInt 메서드 정의

```java
public static int timetoInt(String sTime)
```

##### timetoInt 매개변수

- `sTime`: 변환할 시간 문자열 (예: `"143022"`)

##### timetoInt 반환값

정수형 시간 데이터

##### timetoInt 예제

```java
String timeStr = "143022";
int timeInt = EgovDateUtil.timetoInt(timeStr);
// 결과: 143022
```

## 참고자료

- [전자정부 표준프레임워크 포털 공식 위키](https://www.egovframe.go.kr/wiki/)
