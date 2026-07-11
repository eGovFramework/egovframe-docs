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

# 특수문자처리

## 개요

특수문자처리는 HTML 등 웹 표시 환경에서 특수문자가 깨지거나 스크립트로 해석되지 않도록 변환·복원하는 기능을 제공하는 요소기술이다. `EgovStringUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getSpclStrCnvr(String srcString)` | `String` | 특수문자를 웹 브라우저에서 정상적으로 보이기 위해 특수문자를 처리(' & lT)하는 기능이다 |
| `getHtmlStrCnvr(String srcString)` | `String` | html의 특수문자를 표현하기 위해 |
| `checkHtmlView(String strString)` | `String` | Html 코드가 들어간 문서를 표시할때 태그에 손상없이 보이기 위한 메서드 |

## 사용 예

```java
String esc = EgovStringUtil.getSpclStrCnvr("<script>");  // &lt;script&gt; 형태로 변환
String htm = EgovStringUtil.getHtmlStrCnvr(escapedText);  // HTML 특수문자 복원
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
