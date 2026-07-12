---
title: "랜덤날짜구하기"
linkTitle: "랜덤날짜구하기"
description: "랜덤날짜구하기"
url: /common-component/elementary-technology/formatter-util/random-date/
menu:
  depth:
    name: "랜덤날짜구하기"
    weight: 5
    parent: "formatter-util"
---

# 랜덤 날짜

## 개요

랜덤 날짜는 지정한 두 일자 사이의 임의의 일자를 생성하는 요소기술이다. 테스트 데이터 생성 등에 활용할 수 있다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovDateUtil.java | Date 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getRandomDate(String sDate1, String sDate2)` | `String` | 입력받은 일자 사이의 임의의 일자를 반환 |

## 사용 예

```java
String d = EgovDateUtil.getRandomDate("20260101", "20261231"); // 기간 내 임의 일자
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
