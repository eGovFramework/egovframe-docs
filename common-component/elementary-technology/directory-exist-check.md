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

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.getExistDirectory` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 디렉토리 존재 여부는 `java.io.File`로 확인한다.

## 개요

비즈니스 로직을 처리하면서 필요시 디렉토리의 존재를 확인할 수 있는 공통 기능을 제공한다.

## 설명

### 기능 설명

디렉토리존재체크에서 제공하는 기능은 다음과 같다.

1. 지정한 경로가 디렉토리로 존재하는지 확인하는 기능
2. 존재하는 디렉토리의 하위 파일 목록을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 디렉토리 존재 여부 확인 | |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 하위 파일 목록 조회 | `getSubFilesByAll` |

### 클래스 및 메소드 설명

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `File.exists()` | 존재 여부 | 경로가 존재하면 `true` |
| boolean | `File.isDirectory()` | 디렉토리 여부 | 디렉토리면 `true` |
| List | `EgovFileTool.getSubFilesByAll(File[] fileArray)` | 하위 파일 목록 | 디렉토리 아래 모든 파일의 절대경로 목록 |
<!-- markdownlint-restore -->

### 사용 방법

```java
import java.io.File;
import java.util.List;

import egovframework.com.utl.sim.service.EgovFileTool;

File dir = new File("/user/com/sample");
boolean exists = dir.exists() && dir.isDirectory();

if (exists) {
    List<String> files = EgovFileTool.getSubFilesByAll(dir.listFiles());
}
```

디렉토리 생성이 필요하면 [디렉토리생성](directory-create)의 `EgovFileTool.createNewDirectory`를 사용한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
