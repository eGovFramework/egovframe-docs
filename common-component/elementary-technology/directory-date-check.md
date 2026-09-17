---
title: "디렉토리일자체크"
linkTitle: "디렉토리일자체크"
description: "디렉토리일자체크"
url: /common-component/elementary-technology/system/directory-date-check/
menu:
  depth:
    name: "디렉토리일자체크"
    weight: 14
    parent: "system"
---

<!-- markdownlint-disable MD025 -->

# 디렉토리일자체크

> **5.0 적용 범위:** 이전 가이드의 `EgovFileTool.getLastModifiedDateFromFile` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 최종 수정일자는 `java.io.File.lastModified()`로 확인한다.

## 개요

디렉토리의 최종 수정일자를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

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

File dir = new File("/user/com/sample");
long lastModified = dir.lastModified();
LocalDate date = Instant.ofEpochMilli(lastModified)
        .atZone(ZoneId.systemDefault())
        .toLocalDate();
```

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
