---
title: "문자열유효성체크"
linkTitle: "문자열유효성체크"
description: "문자열유효성체크"
url: /common-component/elementary-technology/formatter-util/string-validation/
menu:
  depth:
    name: "문자열유효성체크"
    weight: 10
    parent: "formatter-util"
---

# 문자열유효성체크

## 개요

문자열유효성체크는 두 개의 문자열을 비교하여 서로 값이 같은지를 확인하는 요소기술이다. 같은 값인지 다른 값인지에 따라
서로 다른 문자열을 리턴한다. `EgovStringUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | 문자열 처리 유틸리티 클래스 |

## 주요 메서드

<!-- markdownlint-disable MD013 -->
| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `decode(String source, String compare, String ret, String defaultValue)` | `String` | 오라클의 decode 함수와 동일한 기능 — `source`와 `compare`가 같으면 `ret`, 다르면 `defaultValue`를 반환 |
<!-- markdownlint-restore -->

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

// foo 출력 (null == null)
System.out.println(EgovStringUtil.decode(null, null, "foo", "bar"));
// bar 출력 ("" != null)
System.out.println(EgovStringUtil.decode("", null, "foo", "bar"));
// foo 출력 (같은 값)
System.out.println(EgovStringUtil.decode("하이", "하이", "foo", "bar"));
// bar 출력 (다른 값 — 공백 포함)
System.out.println(EgovStringUtil.decode("하이", "하이  ", "foo", "bar"));
```

## 참고자료

- [문자열변환](../string-conversion/), [문자열치환](../string-replacement/), [문자열검색](../string-search/)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
