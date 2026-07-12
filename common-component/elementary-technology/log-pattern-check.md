---
title: "로그패턴검사"
linkTitle: "로그패턴검사"
description: "로그패턴검사"
url: /common-component/elementary-technology/system/log-pattern-check/
menu:
  depth:
    name: "로그패턴검사"
    weight: 13
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

로그패턴검사(로그패턴분석)는 로그파일을 분석하여 특정 문자열 등 패턴과 일치하는 내용을 추출하는 기능을 제공한다.

## 설명

찾을로그(패턴)명, 로그파일경로명(서버), 인코딩형식 정보를 입력·선택하여 로그 정보를 검색·분석하고, 결과를 텍스트 파일로 다운로드할 수 있다.

서버 보안을 위해 관리자가 허가한 디렉토리만 분석할 수 있다. 기본 허용 디렉토리는 `C:\WindowsLog`, `/product/jeus2/logs/was2/`이며,
필요시 `EgovLogPattrnAnals.jsp`의 허용 경로 배열을 수정한다.

```java
String[] arrPath = {"C:\\\\WindowsLog", "/product/jeus2/logs/was2/"};
```

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovLogPattrnAnals.jsp` | 로그패턴분석을 위한 jsp 페이지 |

## 관련화면 및 수행매뉴얼

### 로그패턴분석

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 로그패턴분석 | /EgovPageLink.do?link=cmm/utl/EgovLogPattrnAnals | moveToPage | |

로그패턴을 분석하고 텍스트 파일로 다운로드할 수 있는 화면을 제공한다.

- **찾을로그(패턴)명**: 정규표현식을 포함하여 입력할 수 있다.
- **로그파일경로명(서버)**: 공통컴포넌트가 설치된 서버의 경로를 입력한다.
- 검색: 로그패턴을 검색·분석한다.
- 다운로드: 검색·분석된 로그패턴 정보를 다운로드한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
