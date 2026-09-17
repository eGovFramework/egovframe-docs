---
title: "파일복사"
linkTitle: "파일복사"
description: "파일복사"
url: /common-component/elementary-technology/system/file-copy/
menu:
  depth:
    name: "파일복사"
    weight: 30
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.copyFile`, `EgovFileTool.copyFiles` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 파일 복사는 `java.nio.file.Files.copy`를 사용한다.

## 개요

지정한 경로의 파일을 다른 경로로 복사하는 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.nio.file.Files` | 파일 복사 | 5.0 `EgovFileTool`에는 복사 메소드가 없음 |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Path | `Files.copy(Path source, Path target, CopyOption... options)` | 단일 파일 복사 | 원본 파일을 대상 경로로 복사한다 |

### 사용 방법

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

Path source = Path.of("/user/com/source.txt");
Path target = Path.of("/user/com/backup/source.txt");
Files.createDirectories(target.getParent());
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
```

새 파일을 만들기만 하면 되는 경우에는 [파일생성](file-create)의 `EgovFileTool.createNewFile`을 사용한다.

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
