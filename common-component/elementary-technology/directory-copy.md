---
title: "디렉토리복사"
linkTitle: "디렉토리복사"
description: "디렉토리복사"
url: /common-component/elementary-technology/system/directory-copy/
menu:
  depth:
    name: "디렉토리복사"
    weight: 5
    parent: "system"
---

<!-- markdownlint-disable-file MD025 -->

# 디렉토리복사

## 개요

비즈니스 로직을 처리하면서 필요시 디렉토리의 전체 구조와 파일을 복사하는 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 주요 개념

* **전체 구조 복사**: 원본 디렉토리 하위의 모든 파일과 서브 디렉토리 구조를 대상 디렉토리로 동일하게 복사한다.
* **조건부 복사**: 복사 과정에서 생성일자(또는 최종 수정일자)가 특정 날짜 범위에 포함되거나, 디렉토리(또는 파일)의 소유자가 지정한 조건과 일치할 때만 복사를 선택적으로 수행할 수 있다.

## 관련 문서

* [디렉토리 존재 체크](./directory-exist-check.md)
* [디렉토리 생성](./directory-create.md)
* [디렉토리 삭제](./directory-delete.md)
* [디렉토리 이동](./directory-move.md)
* [파일 복사](./file-copy.md)

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryCopy.jsp` | 테스트 페이지 | |

### 메소드 설명

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `copyDirectory(String dirOriginalPath, String dirTargetPath)` | 기본 디렉토리 복사 | 원본 디렉토리 경로(`dirOriginalPath`)에서 대상 디렉토리 경로(`dirTargetPath`)로 복사한다. 성공 시 `true`, 실패 시 `false`를 리턴한다. |
| boolean | `copyDirectory(String dirOriginalPath, String dirTargetPath, String fromDate, String toDate)` | 날짜 조건부 복사 | 원본 디렉토리 경로(`dirOriginalPath`)에서 대상 디렉토리 경로(`dirTargetPath`)로 복사하되, 생성일자가 조건구간(`fromDate`과 `toDate` 사이) 내에 포함되는 디렉토리(또는 파일)만 복사한다. 성공 시 `true`, 실패 시 `false`를 리턴한다. |
| boolean | `copyDirectory(String dirOriginalPath, String dirTargetPath, String owner)` | 소유자 조건부 복사 | 원본 디렉토리 경로(`dirOriginalPath`)에서 대상 디렉토리 경로(`dirTargetPath`)로 복사하되, 소유자가 조건(`owner`)에 일치하는 디렉토리(또는 파일)만 복사한다. 성공 시 `true`, 실패 시 `false`를 리턴한다. (WINDOWS 시스템에서는 지원하지 않는다.) |
<!-- markdownlint-restore -->

### 파라미터 (Input)

* **dirOriginalPath**: String 타입의 절대경로를 포함하는 복사 원본 디렉토리 경로 (예: `/product/jeus/egovProps/tmp/dir1`)
* **dirTargetPath**: String 타입의 절대경로를 포함하는 복사 대상 디렉토리 경로 (예: `/product/jeus/egovProps/tmp/dir2`)
* **fromDate**: String 타입의 날짜 정보 (예: `20090101`)
* **toDate**: String 타입의 날짜 정보 (예: `20090731`)
* **owner**: String 타입의 사용자 계정명 (예: `jeus`)

### 반환값 (Output)

* **boolean** 타입: 복사 성공 여부 `true` / `false`

> [!NOTE]
> 메소드의 입력 항목 중에서 `fromDate`, `toDate` 항목은 Validation 체크가 적용된다
> (요소기술 validation 체크 참조).

## 환경설정

N/A

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 1. 기본 디렉토리 복사
String dirOriginalPath = "/user/com/dirOriginal";
String dirTargetPath = "/user/com/dirTarget";
boolean result1 = EgovFileTool.copyDirectory(dirOriginalPath, dirTargetPath);

// 2. 날짜 조건부 디렉토리 복사
String fromDate = "20090101";
String toDate = "20090731";
boolean result2 = EgovFileTool.copyDirectory(dirOriginalPath, dirTargetPath, fromDate, toDate);

// 3. 소유자 조건부 디렉토리 복사
String owner = "jeus";
boolean result3 = EgovFileTool.copyDirectory(dirOriginalPath, dirTargetPath, owner);
```

## 참고자료

* N/A
