---
title: "양력/음력변환"
linkTitle: "양력/음력변환"
description: "양력/음력변환"
url: /common-component/elementary-technology/formatter-util/solar-lunar-conversion/
menu:
  depth:
    name: "양력/음력변환"
    weight: 20
    parent: "formatter-util"
---

# 양력/음력 변환

## 개요

양력/음력 변환은 양력과 음력 간의 날짜 변환을 지원하는 요소기술이다.
음력을 기준으로 하는 명절이나 기념일 등의 날짜를 처리하는 데 활용할 수 있다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovDateUtil.java | Date 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `toSolar(String sDate, int iLeapMonth)` | `String` | 입력받은 양력일자를 변환하여 음력일자로 반환 |

## 입력값 (Input)

- `sDate`: 변환할 날짜 문자열
- `iLeapMonth`: 윤달 여부를 나타내는 값

## 반환값 (Output)

- `String`: 변환된 날짜 문자열

## 사용 예

```java
String lunar = EgovDateUtil.toSolar("20260711", 0); // 양력 → 음력 변환
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
