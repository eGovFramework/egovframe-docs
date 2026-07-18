---
title: "문자열변환"
linkTitle: "문자열변환"
description: "문자열변환"
url: /common-component/elementary-technology/formatter-util/string-conversion/
menu:
  depth:
    name: "문자열변환"
    weight: 9
    parent: "formatter-util"
---

# 문자열 변환

## 개요

문자열 변환은 대소문자 변환, 문자셋 변환, `null` 값 처리, 문자열 길이 처리 등 다양한 문자열 변환 기능을 제공하는 요소기술이다.
`EgovStringUtil`에서 제공하는 정적 메서드를 통해 문자열 데이터를 목적에 맞게 변환할 수 있다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `lowerCase(String str)` | `String` | 입력된 문자열을 소문자로 변환한다. |
| `upperCase(String str)` | `String` | 입력된 문자열을 대문자로 변환한다. |
| `getEncdDcd(String srcString, String srcCharsetNm, String cnvrCharsetNm)` | `String` | 지정한 문자셋을 기준으로 문자열의 인코딩을 변환한다. |
| `isNullToString(Object object)` | `String` | 객체가 null인지 확인하고 null인 경우 "" 로 바꾸는 메서드 |
| `nullConvert(Object src)` | `String` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `nullConvert(String src)` | `String` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `zeroConvert(Object src)` | `int` | 인자로 받은 String이 null일 경우 &quot;0&quot;로 리턴한다 |
| `zeroConvert(String src)` | `int` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `cutString(String source, String output, int slength)` | `String` | 문자열을 지정한 길이에 맞게 처리한다. |
| `cutString(String source, int slength)` | `String` | 문자열이 지정한 길이를 초과했을때 해당 문자열을 삭제하는 메서드 |
| `decode(String sourceStr, String compareStr, String returnStr, String defaultStr)` | `String` | 오라클의 decode 함수와 동일한 기능을 가진 메서드이다 |
| `decode(String sourceStr, String compareStr, String returnStr)` | `String` | 오라클의 decode 함수와 동일한 기능을 가진 메서드이다 |

## 사용 예

```java
String lower = EgovStringUtil.lowerCase("EgovFrame");            // egovframe
String safe  = EgovStringUtil.isNullToString(nullableValue);      // null이면 ""
String cut   = EgovStringUtil.cutString("표준프레임워크", "…", 4); // 지정 길이 절단
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
