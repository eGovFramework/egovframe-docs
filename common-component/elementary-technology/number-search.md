---
title: "숫자검색"
linkTitle: "숫자검색"
description: "숫자검색"
url: /common-component/elementary-technology/formatter-util/number-search/
menu:
  depth:
    name: "숫자검색"
    weight: 14
    parent: "formatter-util"
---

# 숫자검색

## 개요

숫자검색은 숫자 집합에서 특정 숫자의 존재 여부 확인, 특정 숫자의 치환 등 숫자 검색성 기능을 제공하는 요소기술이다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getNumSearchCheck(int sourceInt, int searchInt)` | `Boolean` | 특정 숫자 집합에서 특정 숫자가 있는지 체크하는 기능 12345678에서 7이 있는지 없는지 체크하는 기능을 제공함 |
| `getNumberCnvr(int srcNumber, int cnvrSrcNumber, int cnvrTrgtNumber)` | `int` | 특정숫자를 다른 숫자로 치환하는 기능 숫자 12345678에서 123를 999로 변환하는 기능을 제공(99945678) |

## 사용 예

```java
boolean has7 = EgovNumberUtil.getNumSearchCheck(12345678, 7); // 7 포함 여부
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
