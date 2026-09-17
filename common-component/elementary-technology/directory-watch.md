---
title: "디렉토리감시"
linkTitle: "디렉토리감시"
description: "디렉토리감시"
url: /common-component/elementary-technology/system/directory-watch/
menu:
  depth:
    name: "디렉토리감시"
    weight: 3
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `startDirectoryMonitering`, `getDirectoryMoniteringInfo`, `stopDirectoryMonitering` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 디렉토리 변경 감시는 `java.nio.file.WatchService`를 사용한다.

## 개요

특정 디렉토리 안의 파일과 하위 항목 변동을 모니터링하는 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.nio.file.WatchService` | 디렉토리 감시 | 5.0 `EgovFileTool`에는 감시 메소드가 없음 |

### 사용 방법

```java
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;

Path dir = Path.of("/user/com/watch");
WatchService watchService = FileSystems.getDefault().newWatchService();
dir.register(watchService,
        StandardWatchEventKinds.ENTRY_CREATE,
        StandardWatchEventKinds.ENTRY_MODIFY,
        StandardWatchEventKinds.ENTRY_DELETE);

WatchKey key = watchService.take();
```

감시 종료 시 `watchService.close()`를 호출한다. 일회성 목록 조회는 `EgovFileTool.getSubFilesByAll`을 사용한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
