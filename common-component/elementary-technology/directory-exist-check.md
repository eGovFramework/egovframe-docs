---
title: "디렉토리존재체크"
linkTitle: "디렉토리존재체크"
description: "디렉토리존재체크"
url: /common-component/elementary-technology/system/directory-exist-check/
menu:
  depth:
    name: "디렉토리존재체크"
    weight: 15
    parent: "system"
---

## 개요

비즈니스 로직을 처리하면서 필요시 디렉토리의 존재를 확인할 수 있는 공통 기능을 제공한다.

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

디렉토리 존재 체크 기능은 다음과 같은 상황에서 활용할 수 있다.

- 파일 업로드 경로가 존재하는지 확인하는 경우
- 애플리케이션 실행 전 필수 디렉토리의 존재 여부를 점검하는 경우
- 특정 조건에 맞는 디렉토리를 검색하는 경우
- 디렉토리 생성 또는 삭제 작업 전에 대상 경로를 확인하는 경우

## 설명

지정한 디렉토리의 존재 여부를 확인하거나, 특정 조건을 만족하는 디렉토리를 검색하는 기능을 제공한다.
날짜, 소유자 등의 조건을 함께 사용하여 필요한 디렉토리를 선택적으로 조회할 수 있다.

1. 대상 디렉토리가 존재하는지 확인하는 기능
2. 특정 위치 이하로 대상 디렉토리가 존재하는지 확인하는 기능
3. 대상 디렉토리의 최종수정일자가 특정 구간 내에 포함되는 경우에 한해서 존재 여부를 확인하는 기능
4. 대상 디렉토리가 특정 소유자에 의해 생성된 경우에 한해서 존재 여부를 확인하는 기능(WINDOWS 시스템에서는 지원하지 않음)

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryExst.jsp` | 테스트 페이지 | |

### 메소드

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `getExistDirectory(String targetDirPath)` | 디렉토리 확인 | 대상 디렉토리경로(`targetDirPath`)를 입력받아 확인한다. 성공 시 `true`, 실패 시 `false`를 리턴 |
| ArrayList | `getExistDirectory(String baseDirPath, String targetDirName, int cnt)` | 디렉토리 확인 | 확인할 위치기준 디렉토리경로(`baseDirPath`)를 입력받아 하위 디렉토리 중 대상 디렉토리(`targetDirPath`)가 존재하는지 확인한다. 성공 시 확인된 절대경로를 문자열 정보로 LIST에 담아서 리턴 |
| boolean | `getExistDirectory(String targetDirPath, String fromDate, String toDate)` | 디렉토리 확인 | 대상 디렉토리경로(`targetDirPath`)를 입력받아 생성일자가 조건구간(`fromDate`과 `toDate` 사이) 내에 포함되는지 확인한다. 성공 시 `true`, 실패 시 `false`를 리턴 |
| boolean | `getExistDirectory(String targetDirPath, String owner)` | 디렉토리 확인 | 대상 디렉토리경로(`targetDirPath`)를 입력받아 디렉토리 소유자조건(`owner`)에 일치하는지 확인한다. 성공 시 `true`, 실패 시 `false` 리턴 |
<!-- markdownlint-restore -->

### Input

* **targetDirPath**: String 타입의 절대경로를 포함하는 확인대상 디렉토리경로 (예: `/product/jeus/egovProps/tmp/dir1`)
* **baseDirPath**: String 타입의 절대경로를 포함하는 확인할 위치기준 디렉토리경로 (예: `/product/jeus/egovProps/tmp`)
* **targetDirName**: String 타입의 확인대상 디렉토리명 (예: `dir1`)
* **cnt**: int 타입의 디렉토리 존재 확인할 반복 횟수 (예: `10`)
* **fromDate**: String 타입의 날짜 정보 (예: `20090101`)
* **toDate**: String 타입의 날짜 정보 (예: `20090731`)
* **owner**: String 타입의 사용자 계정명 (예: `jeus`)

### Output

* **boolean** 타입: 존재 여부 `true` / `false`
* **ArrayList** 타입: 기준 경로 이하로 존재하는 디렉토리 목록 (예: `{"/user/com", "user/com/com", "user/adt/com"}`)

> [!NOTE]
> 메소드의 입력 항목 중에서 `fromDate`, `toDate` 항목은 Validation 체크가 적용된다
> ([요소기술 validation 체크](/common-component/elementary-technology/validation-check/) 참조).

## 환경설정

N/A

### 사용 시 주의사항

- 조회 대상 디렉토리 경로가 올바른지 확인해야 한다.
- `fromDate`와 `toDate`는 `yyyyMMdd` 형식으로 입력해야 한다.
- 소유자 조건을 사용하는 기능은 Windows 환경에서는 지원되지 않는다.
- 검색 범위가 넓은 경우 조회 시간이 증가할 수 있다.    

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String targetDirPath1 = "/user/com/dir1";
boolean result1 = EgovFileTool.getExistDirectory(targetDirPath1);

String baseDirPath2 = "/user/com/dir2";
String targetDirPath2 = "dir22";
int matchCnt = 1; 
ArrayList result2 = EgovFileTool.getExistDirectory(baseDirPath2, targetDirPath2, matchCnt);

String targetDirPath3 = "/user/com/dir3";
String fromDate3 = "20090101";
String toDate3 = "20090131";
boolean result3 = EgovFileTool.getExistDirectory(targetDirPath3, fromDate3, toDate3);

String targetDirPath4 = "/user/com/dir4";
String ownerName4 = "com";
boolean result4 = EgovFileTool.getExistDirectory(targetDirPath4, ownerName4);
```

## 참고자료

N/A
