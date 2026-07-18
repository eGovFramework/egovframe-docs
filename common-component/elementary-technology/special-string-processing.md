---
title: "특수문자열처리"
linkTitle: "특수문자열처리"
description: "특수문자열처리"
url: /common-component/elementary-technology/formatter-util/special-string-processing/
menu:
  depth:
    name: "특수문자열처리"
    weight: 22
    parent: "formatter-util"
---

# 특수문자열 처리

## 개요

특수문자열 처리는 HTML 등의 웹 환경에서 특수문자를 안전하게 표시하고 처리하기 위한 요소기술이다.
`EgovStringUtil`에서 제공하는 메서드를 통해 문자열의 특수문자를 변환하거나 HTML 표시를 위한 문자열 처리를 수행할 수 있다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getSpclStrCnvr(String srcString)` | `String` | 입력된 문자열의 특수문자를 웹 화면에서 표시할 수 있는 형태로 변환한다. |
| `getHtmlStrCnvr(String srcString)` | `String` | HTML의 특수문자를 처리하여 변환된 문자열을 반환한다. |
| `checkHtmlView(String strString)` | `String` | HTML 코드가 포함된 문자열을 화면에 표시하기 위한 형태로 처리한다. |

## 입력값 (Input)

- `srcString`: 특수문자를 처리할 문자열
- `strString`: HTML 표시를 위해 처리할 문자열

## 반환값 (Output)

- `String`: 각 메서드의 처리 결과가 반영된 문자열

## 사용 예

```java
String esc = EgovStringUtil.getSpclStrCnvr("<script>");  // &lt;script&gt; 형태로 변환
String htm = EgovStringUtil.getHtmlStrCnvr(escapedText);  // HTML 특수문자 복원
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
