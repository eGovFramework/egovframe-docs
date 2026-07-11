---
title: "파일권한체크"
linkTitle: "파일권한체크"
description: "파일권한체크"
url: /common-component/elementary-technology/system/file-permission-check/
menu:
  depth:
    name: "파일권한체크"
    weight: 23
    parent: "system"
---

## 개요

비즈니스 로직을 처리하면서 필요한 파일의 접근 권한을 확인하기 위한 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일권한체크에서 제공하는 기능은 다음과 같다.

1. 파일의 읽기 권한을 조회하는 기능
2. 파일의 쓰기 권한을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileAuthor.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일권한체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `canRead(String filePath)` | 읽기권한 체크 | 파일경로를 입력받아 읽기 가능하면 `true`를 리턴한다. 권한이 없거나 파일이 없는 경우는 `false`를 리턴 |
| boolean | `canWrite(String filePath)` | 쓰기권한 체크 | 파일경로를 입력받아 쓰기 가능하면 `true`를 리턴한다. 권한이 없거나 파일이 없는 경우는 `false`를 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `filePath`: String 타입의 절대경로를 포함한 파일명 (예: `/user/com/test/file1.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 권한 보유 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String filePath = "/user/com/sample/test.txt";

// 읽기 권한 확인
boolean readVal = EgovFileTool.canRead(filePath);

// 쓰기 권한 확인
boolean writeVal = EgovFileTool.canWrite(filePath);
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
