---
title: "문자열치환"
linkTitle: "문자열치환"
description: "문자열치환"
url: /common-component/elementary-technology/formatter-util/string-replacement/
menu:
  depth:
    name: "문자열치환"
    weight: 11
    parent: "formatter-util"
---

# 문자열치환

## 개요

문자열치환은 특정 문자열·문자 치환, 대상 문자 제거, 앞뒤 지정 문자 제거(strip), 공백 제거 등 치환·정리 기능을 제공하는 요소기술이다. `EgovStringUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `replace(String source, String subject, String object)` | `String` | 원본 문자열의 포함된 특정 문자열을 새로운 문자열로 변환하는 메서드 |
| `replaceOnce(String source, String subject, String object)` | `String` | 원본 문자열의 포함된 특정 문자열 첫번째 한개만 새로운 문자열로 변환하는 메서드 |
| `replaceChar(String source, String subject, String object)` | `String` | subject에 포함된 각각의 문자를 object로 변환한다 |
| `remove(String str, char remove)` | `String` | 기준 문자열에 포함된 모든 대상 문자(char)를 제거한다 |
| `removeCommaChar(String str)` | `String` | 문자열 내부의 콤마 character(,)를 모두 제거한다 |
| `removeMinusChar(String str)` | `String` | 문자열 내부의 마이너스 character(-)를 모두 제거한다 |
| `removeWhitespace(String str)` | `String` | 문자열에서 {@link Character#isWhitespace(char)}에 정의된 |
| `strip(String str, String stripChars)` | `String` | 입력된 String의 앞, 뒤에서 두번째 인자로 전달된 문자(stripChars)를 모두 제거한다 |
| `stripStart(String str, String stripChars)` | `String` | 입력된 String의 앞쪽에서 두번째 인자로 전달된 문자(stripChars)를 모두 제거한다 |
| `stripEnd(String str, String stripChars)` | `String` | 입력된 String의 뒤쪽에서 두번째 인자로 전달된 문자(stripChars)를 모두 제거한다 |
| `addMinusChar(String date)` | `String` | 날짜 형식의 문자열 내부에 마이너스 character(-)를 추가한다 |

## 사용 예

```java
String s1 = EgovStringUtil.replace("a-b-c", "-", ":");   // a:b:c
String s2 = EgovStringUtil.removeMinusChar("2026-07-11"); // 20260711
String s3 = EgovStringUtil.strip("  egov  ", " ");        // egov
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
