---
title: "디렉토리삭제"
linkTitle: "디렉토리삭제"
description: "디렉토리삭제"
url: /common-component/elementary-technology/system/directory-delete/
menu:
  depth:
    name: "디렉토리삭제"
    weight: 6
    parent: "system"
---

<!-- markdownlint-disable-file MD025 -->

# 디렉토리삭제

## 개요

비즈니스 로직을 처리하면서 필요 시 특정 디렉토리를 삭제할 수 있는 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

디렉토리 삭제 기능은 다음과 같은 상황에서 활용할 수 있다.

- 임시 디렉토리를 정리하는 경우
- 백업이 완료된 디렉토리를 삭제하는 경우
- 애플리케이션에서 생성한 작업 디렉토리를 제거하는 경우
- 더 이상 사용하지 않는 디렉토리를 정리하는 경우

## 주요 개념

입력받은 디렉토리 경로를 기준으로 시스템 상의 물리적 원본 디렉토리를 삭제하는 기능을 수행한다.
디렉토리 내에 파일이 존재하지 않는 빈 디렉토리여야 삭제가 성공적으로 완료된다.

## 설명

지정한 디렉토리 또는 파일 경로를 삭제하는 기능을 제공한다.
삭제 대상의 경로와 환경에 따라 적절한 메소드를 선택하여 사용할 수 있다.

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |

### 메소드 설명

`EgovFileTool` 클래스는 디렉토리와 파일을 구분하지 않고 지정된 경로를 삭제하는 `deletePath` 메소드를 제공한다.

#### 1. deletePath(String filePath)

- **설명**: 입력받은 경로의 디렉토리 또는 파일을 삭제한다. 기본 저장 경로(`Globals.fileStorePath`)를 기반으로 대상을 삭제한다.
- **파라미터 (Input)**:
    - `filePath`: `String` 타입의 삭제 대상 디렉토리 절대경로 (예: `/product/jeus/egovProps/tmp/dir1`)
- **반환값 (Output)**:
    - `String`: 삭제 완료된 대상 디렉토리의 절대경로를 반환하며, 실패 시 빈 문자열(`""`)을 반환한다.

#### 2. deletePath(String basePath, String filePath)

- **설명**: 기본 경로(`basePath`)와 대상 경로(`filePath`)를 결합한 위치의 디렉토리 또는 파일을 삭제한다.
- **파라미터 (Input)**:
    - `basePath`: `String` 타입의 기본 디렉토리 경로
    - `filePath`: `String` 타입의 삭제 대상 디렉토리 경로
- **반환값 (Output)**:
    - `String`: 삭제 완료된 대상 디렉토리의 절대경로를 반환하며, 실패 시 빈 문자열(`""`)을 반환한다.

> [!NOTE]
> 이전 버전에서는 수정일자나 소유자 조건에 따른 삭제 기능(`deleteDirectory`)이 제공되었으나,
> 최신 버전(v4.1 이상)에서는 시큐어코딩 준수 및 플랫폼 호환성을 위해 `deletePath`로 단순화되었다.

### 사용 시 주의사항

- 삭제 대상 경로가 존재해야 한다.
- 삭제 대상에 대한 쓰기 권한이 필요하다.
- 삭제된 디렉토리와 파일은 복구되지 않으므로 삭제 전에 경로를 반드시 확인해야 한다.
- 디렉토리가 비어 있지 않은 경우 삭제 여부를 사전에 확인하는 것이 좋다.

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 디렉토리 삭제 예시
String dirDeletePath = "/user/com/dir1";
String result = EgovFileTool.deletePath(dirDeletePath);
```

## 참고자료

- [파일삭제](./file-delete.md)
