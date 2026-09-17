---
title: "디스크속성정보체크"
linkTitle: "디스크속성정보체크"
description: "디스크속성정보체크"
url: /common-component/elementary-technology/system/disk-attribute-check/
menu:
  depth:
    name: "디스크속성정보체크"
    weight: 16
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.getMountLc` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 디스크 용량과 저장소 정보는 `java.io.File` 또는 `java.nio.file.FileStore`로 확인한다.

## 개요

특정 경로가 위치한 디스크의 용량과 저장소 정보를 확인하는 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 디스크 용량 조회 | |
| JDK | `java.nio.file.FileStore` | 저장소(마운트) 정보 | |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| long | `File.getTotalSpace()` | 전체 용량 | 디스크 전체 크기(byte) |
| long | `File.getUsableSpace()` | 사용 가능 용량 | 사용 가능한 크기(byte) |
| String | `FileStore.name()` | 저장소 이름 | 파일이 위치한 저장소 이름 |

### 사용 방법

```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.FileStore;
import java.nio.file.Path;

File file = new File("/user/com/sample/file1.txt");
long total = file.getTotalSpace();
long usable = file.getUsableSpace();

FileStore store = Files.getFileStore(Path.of(file.getAbsolutePath()));
String storeName = store.name();
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
