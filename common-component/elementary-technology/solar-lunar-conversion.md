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

# 양음력변환

## 개요

양음력변환은 양력 일자를 음력 일자로 변환하는 요소기술이다. 명절·기념일 등 음력 기반 일자 처리에 활용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovDateUtil.java | Date 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `toSolar(String sDate, int iLeapMonth)` | `String` | 입력받은 양력일자를 변환하여 음력일자로 반환 |

## 사용 예

```java
String lunar = EgovDateUtil.toSolar("20260711", 0); // 양력 → 음력 변환
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
