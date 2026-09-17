---
title: "파일권한체크"
linkTitle: "파일권한체크"
description: "파일권한체크"
url: /common-component/elementary-technology/system/file-permission-check/
menu:
  depth:
    name: "파일권한체크"
    weight: 23
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.canRead`, `EgovFileTool.canWrite` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 파일 읽기·쓰기 권한은 `java.io.File`로 확인한다.

## 개요

비즈니스 로직을 처리하면서 필요한 파일의 접근 권한을 확인하기 위한 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일권한체크에서 제공하는 기능은 다음과 같다.

1. 파일의 읽기 권한을 조회하는 기능
2. 파일의 쓰기 권한을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 파일 읽기·쓰기 권한 확인 | 5.0 `EgovFileTool`에는 권한 조회 메소드가 없음 |

### 클래스 및 메소드 설명

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `File.canRead()` | 읽기권한 체크 | 읽기 가능하면 `true`, 권한이 없거나 파일이 없으면 `false` |
| boolean | `File.canWrite()` | 쓰기권한 체크 | 쓰기 가능하면 `true`, 권한이 없거나 파일이 없으면 `false` |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- 파일 경로: 절대경로를 포함한 파일명 (예: `/user/com/test/file1.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 권한 보유 여부 (`true` / `false`)

### 사용 방법

```java
import java.io.File;

String filePath = "/user/com/sample/test.txt";
File file = new File(filePath);

boolean readVal = file.canRead();
boolean writeVal = file.canWrite();
```

파일 생성·삭제가 필요하면 [파일생성](file-create), [파일삭제](file-delete)의 `EgovFileTool` 메소드를 사용한다.

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
