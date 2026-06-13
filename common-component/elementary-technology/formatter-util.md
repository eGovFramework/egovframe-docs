---
title: "포맷/계산/변환"
linkTitle: "포맷/계산/변환"
description: "포맷/계산/변환"
url: /common-component/elementary-technology/formatter-util/
menu:
  depth:
    weight: 9
    parent: "elementary-technology"
    identifier: "formatter-util"
---

## 개요

포맷/계산/변환(Format/Calc/Convert) 요소기술 패키지는 공통컴포넌트 내에서 데이터의 형식을 조정하거나, 날짜, 숫자, 문자열 등에 대한 계산 및 변환 작업을 수행하는 유틸리티 기능을 제공한다.
게시판, 커뮤니티, 시스템 이력 관리 등 표준프레임워크의 다양한 공통컴포넌트에서 공통적으로 참조하여 사용하는 필수 요소기술이다.

## 주요 개념

### 날짜/시간/요일 처리

- **계산**: 날짜 및 시간의 가감 연산(연, 월, 일, 시, 분 계산)과 요일 계산을 수행한다.
- **변환**: 날짜/시간을 문자열이나 정수형(int) 타입으로 변환한다.
- **포맷 변경**: 입력된 날짜/시간을 지정한 포맷(예: `yyyy년 MM월 dd일`)으로 변경하고, 영문 요일을 한글로 변환한다.
- **유효성 체크**: 주어진 날짜, 시간, 요일 데이터의 형식과 유효성을 검증한다.

### 숫자 처리

- **변환**: 숫자 타입을 문자열 등 다른 데이터 타입으로 안전하게 변환한다.
- **치환 및 검증**: 특정 숫자 집합 간 치환 및 유효성 검증을 수행한다.

### 문자열 처리

- **변환**: 대문자/소문자 상호 변환, HTML 특수문자 처리 등을 수행한다.
- **치환 및 검색**: 특정 문자열의 치환, 추출 및 검색 기능을 제공한다.
- **유효성 체크**: 이메일, 전화번호, 휴대폰번호 등 다양한 문자열 형식에 대한 유효성 체크를 수행한다.

### 기타 유틸리티

- **환율 계산**: 외부 연계 등을 활용하여 지정된 환율 정보 기반으로 환율을 계산한다.
- **단위 변환**: 각종 측정 단위 및 수치 변환 기능을 제공한다.
- **랜덤 값 생성**: 무작위적인 날짜, 문자열, 난수를 생성한다.

## 관련 클래스 및 패키지 구조

해당 모듈은 `egovframework.com.utl.fcc` (Format/Calc/Convert) 패키지에 구현되어 있으며, 주요 핵심 유틸리티 클래스는 다음과 같다.

| 클래스명 | 설명 | 비고 |
| --- | --- | --- |
| `EgovDateUtil` | 날짜 및 시간 처리 관련 유틸리티 | |
| `EgovNumberUtil` | 숫자 데이터 처리 및 변환 유틸리티 | |
| `EgovStringUtil` | 문자열 처리 및 변환 유틸리티 | |
| `EgovFormatCheckUtil` | 이메일, 전화번호 등 포맷 유효성 체크 유틸리티 | |
| `EgovEhgtCalcUtil` | 환율 계산 처리 유틸리티 | |

## 설명

### 유효성 체크 예시 (EgovFormatCheckUtil)

전화번호, 휴대폰번호, 이메일 등을 입력받아 형식을 검증하는 기능을 제공하며, 구분 입력(배열/다중 파라미터)과 단일 문자열 입력을 모두 지원한다.

#### 전화번호 유효성 체크 메소드

- `checkFormatTell(String tell1, String tell2, String tell3)`: 입력된 전화번호의 앞, 중간, 뒤 문자열을 각각 받아서 검증한다. 유효한 전화번호인지 체크하여 `boolean` 값을 반환한다.
- `checkFormatTell(String tellNumber)`: 하이픈(`-`)을 제외한 하나의 연결된 문자열을 받아서 유효한 전화번호인지 체크한다.

```java
// 다중 파라미터를 이용한 검증
boolean isValidePhone = EgovFormatCheckUtil.checkFormatTell("02", "1234", "5678");

// 단일 문자열을 이용한 검증
boolean isValidePhone2 = EgovFormatCheckUtil.checkFormatTell("0212345678");
```

## 참고자료

- [표준프레임워크 포털](https://www.egovframe.go.kr)
