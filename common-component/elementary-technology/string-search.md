---
title: "문자열검색"
linkTitle: "문자열검색"
description: "문자열검색"
url: /common-component/elementary-technology/formatter-util/string-search/
menu:
  depth:
    name: "문자열검색"
    weight: 8
    parent: "formatter-util"
---

# 문자열검색

## 개요

문자열검색은 문자열 내 특정 문자열의 위치 확인, 분리자 기준 분할, 공백 여부 확인 등 검색성 기능을 제공하는 요소기술이다. `EgovStringUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `indexOf(String str, String searchStr)` | `int` | str 중 searchStr의 시작(index) 위치를 반환 |
| `split(String source, String separator)` | `String[]` | 문자열을 지정한 분리자에 의해 배열로 리턴하는 메서드 |
| `split(String source, String separator, int arraylength)` | `String[]` | 문자열을 지정한 분리자에 의해 지정된 길이의 배열로 리턴하는 메서드 |
| `isEmpty(String str)` | `boolean` | String이 비었거나("") 혹은 null 인지 검증한다 |

## 사용 예

```java
int pos = EgovStringUtil.indexOf("egovframework", "gov");   // 1
String[] parts = EgovStringUtil.split("a,b,c", ",");        // [a, b, c]
boolean empty = EgovStringUtil.isEmpty("");                   // true
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
