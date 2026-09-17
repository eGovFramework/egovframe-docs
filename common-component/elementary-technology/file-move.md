---
title: "파일이동"
linkTitle: "파일이동"
description: "파일이동"
url: /common-component/elementary-technology/system/file-move/
menu:
  depth:
    name: "파일이동"
    weight: 41
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.moveFile` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 파일 이동은 `java.nio.file.Files.move`를 사용한다.

## 개요

비즈니스 로직을 처리하면서 필요시 파일을 이동할 수 있는 공통 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.nio.file.Files` | 파일 이동 | 5.0 `EgovFileTool`에는 이동 메소드가 없음 |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Path | `Files.move(Path source, Path target, CopyOption... options)` | 파일 이동 | 원본 파일을 대상 경로로 이동한다 |

### 사용 방법

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

Path source = Path.of("/user/com/file1.txt");
Path target = Path.of("/user/com/move/file1.txt");
Files.createDirectories(target.getParent());
Files.move(source, target, StandardCopyOption.REPLACE_EXISTING);
```

파일을 삭제만 하면 되는 경우에는 [파일삭제](file-delete)의 `EgovFileTool.deleteFile`을 사용한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
