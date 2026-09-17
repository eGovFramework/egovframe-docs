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

> **5.0 적용 범위:** 이전 가이드의 `checkFileExstByName`, `checkFileExstByExtnt`, `checkFileExstBySize`, `checkFileExstByUpdtPd` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 파일 존재 여부는 `java.io.File`로 확인하고, 하위 파일 목록은 `EgovFileTool.getSubFilesByAll`을 사용한다.

## 개요

디렉토리에 파일이 존재하는지 체크하는 기능을 제공한다. 서버 및 클라이언트 응용 애플리케이션에서 파일 존재 체크 시 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일존재체크에서 제공하는 기능은 다음과 같다.

1. 지정한 경로에 파일이 존재하는지 확인하는 기능
2. 디렉토리 하위 파일 목록을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 파일 존재 여부 확인 | |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 하위 파일 목록 조회 | `getSubFilesByAll` |

### 클래스 및 메소드 설명

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `File.exists()` | 존재 여부 | 경로가 존재하면 `true` |
| boolean | `File.isFile()` | 파일 여부 | 일반 파일이면 `true` |
| List | `EgovFileTool.getSubFilesByAll(File[] fileArray)` | 하위 파일 목록 | 디렉토리 아래 모든 파일의 절대경로 목록 |
<!-- markdownlint-restore -->

### 사용 방법

```java
import java.io.File;
import java.util.List;

import egovframework.com.utl.sim.service.EgovFileTool;

File file = new File("/user/com/test/file1.txt");
boolean exists = file.exists() && file.isFile();

File dir = new File("/user/com/test");
if (dir.isDirectory()) {
    List<String> files = EgovFileTool.getSubFilesByAll(dir.listFiles());
}
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
