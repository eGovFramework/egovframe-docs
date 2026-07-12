---
title: "랜덤문자열구하기"
linkTitle: "랜덤문자열구하기"
description: "랜덤문자열구하기"
url: /common-component/elementary-technology/formatter-util/random-string/
menu:
  depth:
    name: "랜덤문자열구하기"
    weight: 6
    parent: "formatter-util"
---

# 랜덤 문자열

## 개요

랜덤 문자열은 시작 문자와 종료 문자 사이의 임의의 문자열을 생성하는 요소기술이다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | String 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getRandomStr(char startChr, char endChr)` | `String` | 문자열 A에서 Z사이의 랜덤 문자열을 구하는 기능을 제공 시작문자열과 종료문자열 사이의 랜덤 문자열을 구하는 기능 |

## 사용 예

```java
String s = EgovStringUtil.getRandomStr('A', 'Z'); // A~Z 사이 임의 문자열
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
