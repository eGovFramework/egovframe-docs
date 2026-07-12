---
title: "포맷유효성체크"
linkTitle: "포맷유효성체크"
description: "포맷유효성체크"
url: /common-component/elementary-technology/formatter-util/format-validation/
menu:
  depth:
    name: "포맷유효성체크"
    weight: 18
    parent: "formatter-util"
---

# 포맷유효성체크

## 개요

포맷유효성체크는 주어진 전화번호, 휴대폰번호, 이메일의 유효성을 체크하여 `true`/`false`를 반환하는 요소기술이다.
각 입력마다 구분 입력(앞·중간·뒤 분리)과 하나의 문자열 입력 두 가지 방식을 지원한다.
`EgovFormatCheckUtil` 유틸리티의 정적 메서드로 사용한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovFormatCheckUtil.java | 포맷 유효성 체크 유틸리티 클래스 |
| Controller | egovframework.com.utl.fcc.web.EgovFormatCheckUtilController.java | 테스트용 Controller |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovFormatCheck.jsp | 테스트 페이지 |

## 주요 메서드

<!-- markdownlint-disable MD013 -->
| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `checkFormatTell(String tell1, String tell2, String tell3)` | `boolean` | 전화번호 앞·중간·뒤 문자열을 받아 유효한 전화번호인지 체크 |
| `checkFormatTell(String tellNumber)` | `boolean` | `-`를 제외한 하나의 문자열을 받아 유효한 전화번호인지 체크 |
| `checkFormatCell(String cell1, String cell2, String cell3)` | `boolean` | 휴대폰번호 앞·중간·뒤 문자열을 받아 유효한 휴대폰번호인지 체크 |
| `checkFormatCell(String cellNumber)` | `boolean` | `-`를 제외한 하나의 문자열을 받아 유효한 휴대폰번호인지 체크 |
| `checkFormatMail(String mail1, String mail2)` | `boolean` | 이메일의 앞·뒤 문자열을 받아 유효한 이메일인지 체크 |
| `checkFormatMail(String mail)` | `boolean` | `@`를 포함한 하나의 문자열을 받아 유효한 이메일인지 체크 |
<!-- markdownlint-restore -->

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovFormatCheckUtil;

// 전화번호 유효성 체크
boolean tel1 = EgovFormatCheckUtil.checkFormatTell("070", "4448", "2678");
boolean tel2 = EgovFormatCheckUtil.checkFormatTell("07044482678");

// 휴대폰번호 유효성 체크
boolean cell1 = EgovFormatCheckUtil.checkFormatCell("010", "1111", "1111");
boolean cell2 = EgovFormatCheckUtil.checkFormatCell("01011111111");

// 이메일 유효성 체크
boolean mail1 = EgovFormatCheckUtil.checkFormatMail("example", "example.com");
boolean mail2 = EgovFormatCheckUtil.checkFormatMail("example@example.com");
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
