---
title: "파일존재체크"
linkTitle: "파일존재체크"
description: "파일존재체크"
url: /common-component/elementary-technology/system/file-exist-check/
menu:
  depth:
    name: "파일존재체크"
    weight: 43
    parent: "system"
---

## 개요

특정 디렉토리 내에 파일이 존재하는지 파일명·확장자·수정기간·사이즈·소유자(Owner) 등 다양한 조건으로
확인하는 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일존재체크에서 제공하는 기능은 다음과 같다.

1. 파일명 기준으로 파일 존재 여부를 확인하는 기능
2. 확장자 기준으로 파일 존재 여부를 확인하는 기능
3. 수정 기간 기준으로 파일 존재 여부를 확인하는 기능
4. 파일 사이즈 기준으로 파일 존재 여부를 확인하는 기능
5. 소유자(Owner) 기준으로 파일 존재 여부를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileExst.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일존재체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `checkFileExstByName(dir, file)` | 파일명 기준 존재 확인 | 지정한 디렉토리에 해당 파일명이 존재하는지 확인한다. |
| boolean | `checkFileExstByExtnt(dir, eventn)` | 확장자 기준 존재 확인 | 지정한 확장자에 해당하는 파일이 존재하는지 확인한다. |
| boolean | `checkFileExstByUpdtPd(dir, from, to)` | 수정기간 기준 존재 확인 | 수정 기간(from~to) 내에 수정된 파일이 존재하는지 확인한다. |
| boolean | `checkFileExstBySize(dir, sizeFrom, sizeTo)` | 사이즈 기준 존재 확인 | 지정한 사이즈 범위에 해당하는 파일이 존재하는지 확인한다. |
| boolean | `checkFileExstByOwner(dir, owner)` | 소유자 기준 존재 확인 | 지정한 소유자의 파일이 존재하는지 확인한다. |

#### 파라미터 정의 (Input)

- `dir`: 검색 대상 디렉토리 절대경로 (String 타입)
- `file`: 확인할 파일명 (String 타입)
- `eventn`: 확장자 (String 타입, 예: `"txt"`)
- `from`, `to`: 수정 기간 시작·종료 일자 (String 타입, `yyyyMMdd` 형식)
- `sizeFrom`, `sizeTo`: 파일 사이즈 범위 (long 타입, byte 단위)
- `owner`: 소유자 계정명 (String 타입)

#### 반환값 정의 (Output)

- boolean 타입: 파일 존재 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String dir = "/user/com/test";

// 파일명 기준 존재 확인
boolean byName = EgovFileTool.checkFileExstByName(dir, "sample.txt");

// 확장자 기준 존재 확인
boolean byExt = EgovFileTool.checkFileExstByExtnt(dir, "txt");

// 수정 기간 기준 존재 확인
boolean byDate = EgovFileTool.checkFileExstByUpdtPd(dir, "20260601", "20260614");

// 사이즈 기준 존재 확인 (1KB ~ 1MB)
boolean bySize = EgovFileTool.checkFileExstBySize(dir, 1024L, 1048576L);

// 소유자 기준 존재 확인
boolean byOwner = EgovFileTool.checkFileExstByOwner(dir, "jeus");
```

## 참고자료

- N/A
