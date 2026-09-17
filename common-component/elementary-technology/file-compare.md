---
title: "파일비교"
linkTitle: "파일비교"
description: "파일비교"
url: /common-component/elementary-technology/system/file-compare/
menu:
  depth:
    name: "파일비교"
    weight: 31
    parent: "system"
---

<!-- markdownlint-disable MD025 -->

# 파일비교

> **5.0 적용 범위:** 이전 가이드의 `cmprFilesByContent`, `cmprFilesByOwner`, `cmprFilesBySize`, `cmprFilesByUpdtPd` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 크기·수정일자·내용 비교는 JDK API로 확인한다.

## 개요

파일비교 기능은 두 파일의 크기, 수정일자, 내용이 같은지 확인하는 기능을 제공한다.

### 활용 예시

- 백업 파일과 원본 파일의 동일 여부를 확인하는 경우
- 파일 변경 여부를 점검하는 경우

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 크기·수정일자 비교 | |
| JDK | `java.nio.file.Files` | 내용 비교 | `Files.mismatch` |

### 사용 방법

```java
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;

File file1 = new File("/user/com/file1.txt");
File file2 = new File("/user/com/file2.txt");

boolean isSameSize = file1.length() == file2.length();
boolean isSameUpdtPd = file1.lastModified() == file2.lastModified();
boolean isSameContent = Files.mismatch(file1.toPath(), file2.toPath()) == -1L;
```

`Files.mismatch`는 내용이 같으면 `-1`을 반환한다. 소유자 비교 메소드는 5.0에서 제공하지 않는다.

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
