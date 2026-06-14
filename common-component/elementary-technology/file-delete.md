---
title: "파일삭제"
linkTitle: "파일삭제"
description: "파일삭제"
url: /common-component/elementary-technology/system/file-delete/
menu:
  depth:
    name: "파일삭제"
    weight: 32
    parent: "system"
---

<!-- markdownlint-disable-file MD025 -->

# 파일삭제

## 개요

비즈니스 로직을 처리하면서 필요시 파일을 삭제할 수 있는 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 주요 개념

입력받은 파일 경로를 기준으로 시스템 상의 물리적 원본 파일을 삭제하는 기능을 수행한다.

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryFileDelete.jsp` | 테스트 페이지 | |

### 메소드 설명

`String deleteFile(String fileDeletePath)` 메소드를 통해 파일을 삭제한다.

#### 파라미터 (Input)

- `fileDeletePath`: `String` 타입의 절대경로를 포함하는 삭제 대상 파일 경로 (예: `/product/jeus/egovProps/tmp/file1.txt`)

#### 반환값 (Output)

- `String`: 삭제 처리가 완료된 대상 파일의 절대경로를 반환하며, 실패 시 빈 문자열을 반환한다.

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String fileDeletePath = "/user/com/file1.txt";
String result = EgovFileTool.deleteFile(fileDeletePath);
```

## 참고자료

- N/A
