---
title: "파일일자체크"
linkTitle: "파일일자체크"
description: "파일일자체크"
url: /common-component/elementary-technology/system/file-date-check/
menu:
  depth:
    name: "파일일자체크"
    weight: 42
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `getUpdtDate`, `getFileListByDate`, `getFileListByUpdtPd` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 최종 수정일자는 `java.io.File.lastModified()`로 확인한다.

## 개요

파일의 최종 수정일자를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일일자체크에서 제공하는 기능은 다음과 같다.

1. 파일의 최종 수정일자를 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 최종 수정일자 조회 | |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| long | `File.lastModified()` | 수정일자 조회 | 최종 수정 시각을 epoch millisecond로 반환한다 |

### 사용 방법

```java
import java.io.File;
import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;

File file = new File("/user/com/sample/file1.txt");
long lastModified = file.lastModified();
LocalDate date = Instant.ofEpochMilli(lastModified)
        .atZone(ZoneId.systemDefault())
        .toLocalDate();
```

하위 파일 목록이 필요하면 `EgovFileTool.getSubFilesByAll`로 경로를 구한 뒤 각 파일의 `lastModified()`를 비교한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
