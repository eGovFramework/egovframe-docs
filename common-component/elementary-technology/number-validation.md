---
title: "숫자유효성체크"
linkTitle: "숫자유효성체크"
description: "숫자유효성체크"
url: /common-component/elementary-technology/formatter-util/number-validation/
menu:
  depth:
    name: "숫자유효성체크"
    weight: 16
    parent: "formatter-util"
---

# 숫자 유효성체크

## 개요

숫자 유효성체크는 입력값이 숫자인지 여부를 검사하는 요소기술이다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getNumberValidCheck(String checkStr)` | `Boolean` | 체크할 숫자 중에서 숫자인지 아닌지 체크하는 기능 |

## 사용 예

```java
boolean ok = EgovNumberUtil.getNumberValidCheck("12345"); // 숫자 여부
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
