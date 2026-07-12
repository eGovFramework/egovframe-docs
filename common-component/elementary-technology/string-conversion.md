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

# 문자열변환

## 개요

문자열변환은 대소문자 변환, 문자셋 인코딩 변환, null 안전 변환, 지정 길이 절단 등 변환성 기능을 제공하는 요소기술이다. `EgovStringUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `lowerCase(String str)` | `String` | {@link String#toLowerCase()}를 이용하여 소문자로 변환한다 |
| `upperCase(String str)` | `String` | {@link String#toUpperCase()}를 이용하여 대문자로 변환한다 |
| `getEncdDcd(String srcString, String srcCharsetNm, String cnvrCharsetNm)` | `String` | 문자열을 다양한 문자셋(EUC-KR[KSC5601],UTF-8..)을 사용하여 인코딩하는 기능 역으로 디코딩하여 원래의 문자열을 |
| `isNullToString(Object object)` | `String` | 객체가 null인지 확인하고 null인 경우 "" 로 바꾸는 메서드 |
| `nullConvert(Object src)` | `String` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `nullConvert(String src)` | `String` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `zeroConvert(Object src)` | `int` | 인자로 받은 String이 null일 경우 &quot;0&quot;로 리턴한다 |
| `zeroConvert(String src)` | `int` | 인자로 받은 String이 null일 경우 &quot;&quot;로 리턴한다 |
| `cutString(String source, String output, int slength)` | `String` | 2009.01.13     박정규          최초 생성 |
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
