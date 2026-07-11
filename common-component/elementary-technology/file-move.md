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

## 개요

비즈니스 로직을 처리하면서 필요시 파일을 이동할 수 있는 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일이동에서 제공하는 기능은 다음과 같다.

1. 원본 파일을 타겟 파일로 이동하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryMvmn.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일이동 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `moveFile(String fileOriginalPath, String fileTargetPath)` | 파일 이동 | 원본파일(`fileOriginalPath`)을 입력받아 타겟파일(`fileTargetPath`)로 이동한다. 타겟파일이 이미 존재하는 경우는 실패로 처리된다. 성공 시 `true`, 실패 시 `false` 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `fileOriginalPath`: String 타입의 절대경로를 포함하는 원본파일 경로 (예: `/product/jeus/egovProps/tmp/file1.txt`)
- `fileTargetPath`: String 타입의 절대경로를 포함하는 타겟파일 경로 (예: `/product/jeus/egovProps/tmp/move1.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 이동 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String fileOriginalPath = "/user/com/file1.txt";
String fileTargetPath   = "/user/com/move1.txt";

boolean result = EgovFileTool.moveFile(fileOriginalPath, fileTargetPath);
if (result) {
    System.out.println("파일 이동 성공");
}
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
