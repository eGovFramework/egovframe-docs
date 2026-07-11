---
title: "디렉토리이동"
linkTitle: "디렉토리이동"
description: "디렉토리이동"
url: /common-component/elementary-technology/system/directory-move/
menu:
  depth:
    name: "디렉토리이동"
    weight: 10
    parent: "system"
---

## 개요

비즈니스 로직을 처리하면서 필요시 디렉토리를 이동할 수 있는 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

디렉토리이동에서 제공하는 기능은 다음과 같다.

1. 원본 디렉토리를 타겟 디렉토리로 이동하는 기능
2. 원본 디렉토리의 최종수정일자가 특정 구간 내에 포함되는 경우에 한해서 타겟 디렉토리로 이동하는 기능
3. 원본 디렉토리가 특정 소유자인 경우에 한해서 타겟 디렉토리로 이동하는 기능 (WINDOWS 시스템에서는 지원하지 않음)

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryMvmn.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

디렉토리이동 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `moveFile(String dirOriginalPath, String dirTargetPath)` | 디렉토리 이동 | 원본디렉토리경로(`dirOriginalPath`)를 입력받아 타겟디렉토리(`dirTargetPath`)로 이동한다. 타겟디렉토리가 이미 존재하는 경우는 실패로 처리된다. 성공 시 `true`, 실패 시 `false` 리턴 |
| boolean | `moveFile(String dirOriginalPath, String dirTargetPath, String fromDate, String toDate)` | 디렉토리 이동 (일자 조건) | 원본디렉토리의 생성일자가 조건구간(`fromDate`과 `toDate` 사이) 내에 포함되는 경우 타겟디렉토리로 이동한다. 성공 시 `true`, 실패 시 `false` 리턴 |
| boolean | `moveFile(String dirOriginalPath, String dirTargetPath, String owner)` | 디렉토리 이동 (소유자 조건) | 원본디렉토리가 소유자조건(`owner`)에 일치하는 경우 타겟디렉토리로 이동한다. 성공 시 `true`, 실패 시 `false` 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `dirOriginalPath`: String 타입의 절대경로를 포함하는 원본디렉토리 경로 (예: `/product/jeus/egovProps/tmp/dir1`)
- `dirTargetPath`: String 타입의 절대경로를 포함하는 타겟디렉토리 경로 (예: `/product/jeus/egovProps/tmp/move1`)
- `fromDate` / `toDate`: String 타입의 날짜정보 (예: `20090101`, YYYYMMDD 형태)
- `owner`: String 타입의 사용자계정명 (예: `jeus`)

#### 반환값 정의 (Output)

- boolean 타입: 이동 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 1. 디렉토리 이동
boolean result1 = EgovFileTool.moveFile("/user/com/dir1", "/user/com/move1");

// 2. 일자 조건 디렉토리 이동
boolean result2 = EgovFileTool.moveFile("/user/com/dir2", "/user/com/move2", "20090101", "20090131");

// 3. 소유자 조건 디렉토리 이동
boolean result3 = EgovFileTool.moveFile("/user/com/dir3", "/user/com/move3", "com");
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
