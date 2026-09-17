---
title: "디렉토리복사"
linkTitle: "디렉토리복사"
description: "디렉토리복사"
url: /common-component/elementary-technology/system/directory-copy/
menu:
  depth:
    name: "디렉토리복사"
    weight: 5
    parent: "system"
---

<!-- markdownlint-disable-file MD025 -->

# 디렉토리복사

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.copyDirectory` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 디렉토리 복사는 `java.nio.file.Files`로 처리한다.

## 개요

지정한 디렉토리를 다른 경로로 복사하는 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.nio.file.Files` | 디렉토리·파일 복사 | 5.0 `EgovFileTool`에는 복사 메소드가 없음 |

### 사용 방법

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.stream.Stream;

Path source = Path.of("/user/com/dir1");
Path target = Path.of("/user/com/copy1");

try (Stream<Path> walk = Files.walk(source)) {
    walk.forEach(from -> {
        Path to = target.resolve(source.relativize(from));
        try {
            if (Files.isDirectory(from)) {
                Files.createDirectories(to);
            } else {
                Files.createDirectories(to.getParent());
                Files.copy(from, to, StandardCopyOption.REPLACE_EXISTING);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    });
}
```

새 디렉토리만 만들면 되는 경우에는 [디렉토리생성](directory-create)의 `EgovFileTool.createNewDirectory`를 사용한다.

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
