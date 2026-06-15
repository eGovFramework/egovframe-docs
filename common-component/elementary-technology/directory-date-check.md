---
title: "디렉토리일자체크"
linkTitle: "디렉토리일자체크"
description: "디렉토리일자체크"
url: /common-component/elementary-technology/system/directory-date-check/
menu:
  depth:
    name: "디렉토리일자체크"
    weight: 14
    parent: "system"
---

<!-- markdownlint-disable MD025 -->

# 디렉토리일자체크

## 개요

비즈니스 로직을 처리하면서 필요 시 디렉토리의 일자 정보를 확인하기 위해 제공되는 공통컴포넌트 요소기술 중 하나이다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

1. 대상 디렉토리의 최종 수정일자를 확인하는 기능
2. 디렉토리의 최종 수정일자가 특정 기간 내에 포함되는지 확인하여 해당 디렉토리 목록을 조회하는 기능

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryCreate.jsp` | 테스트 페이지 | |

### 메소드

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getLastModifiedDateFromFile(String targetDirPath)` | 디렉토리 일자 확인 | 대상 디렉토리경로(`targetDirPath`)를 입력받아 최종 수정일자를 확인한다. 성공 시 `yyyyMMdd` 형식의 8자리 날짜 문자열, 실패 시 블랭크(`""`)를 리턴 |
| ArrayList | `getLastModifiedDateFromFile(String targetDirPath, String fromDate, String toDate)` | 디렉토리 일자 구간 확인 | 대상 디렉토리경로(`targetDirPath`)를 입력받아 하위 경로 중 최종 수정일자가 지정된 기간(`fromDate` ~ `toDate`) 내에 포함되는 디렉토리 목록을 리턴 |
<!-- markdownlint-restore -->

### Input

* **targetDirPath**: String 타입의 절대경로를 포함하는 확인대상 디렉토리경로 (예: `/tmp/dir1`)
* **fromDate**: String 타입의 시작 날짜 (예: `20090101`)
* **toDate**: String 타입의 종료 날짜 (예: `20090731`)

### Output

* **String** 타입: `yyyyMMdd` 형식의 8자리 날짜 문자열 (예: `20090115`)
* **ArrayList** 타입: 지정한 기간 내에 해당하는 디렉토리 경로 목록 (예: `{"/tmp/dir1", "/tmp/dir2"}`)

> [!NOTE]
> 메소드의 입력 항목 중에서 `fromDate`, `toDate` 항목은 Validation 체크가 적용된다
> (요소기술 validation 체크 참조).

## 환경설정

N/A

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 1. 단일 디렉토리 일자 확인
String targetDirPath1 = "/product/jeus/egovProps/tmp/dir1";
String lastModifiedDate = EgovFileTool.getLastModifiedDateFromFile(targetDirPath1);

// 2. 특정 기간 내 수정된 디렉토리 목록 조회
String targetDirPath2 = "/product/jeus/egovProps/tmp";
String fromDate = "20090101";
String toDate = "20090731";
ArrayList list = EgovFileTool.getLastModifiedDateFromFile(targetDirPath2, fromDate, toDate);
```

## 참고자료

N/A
