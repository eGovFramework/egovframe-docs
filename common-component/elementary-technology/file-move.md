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

지정한 경로의 파일을 다른 경로로 이동하는 기능을 제공한다. 대상 경로에 동일한 파일이 존재할 경우
이동이 실패 처리된다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일이동에서 제공하는 기능은 다음과 같다.

1. 파일을 지정한 타겟 경로로 이동하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileMv.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일이동 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `moveFile(fileOriginalPath, fileTargetPath)` | 파일 이동 | 원본 파일을 타겟 경로로 이동한다. 성공 시 true, 실패 시 false 리턴 |

#### 파라미터 정의 (Input)

- `fileOriginalPath`: 이동할 원본 파일의 절대경로 (String 타입)
  (예: `/user/com/file1.txt`)
- `fileTargetPath`: 이동할 대상 파일의 절대경로 (String 타입)
  (예: `/user/com/move/file1.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 이동 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String fileOriginalPath = "/user/com/file1.txt";
String fileTargetPath   = "/user/com/move1.txt";

// 파일 이동
boolean result = EgovFileTool.moveFile(fileOriginalPath, fileTargetPath);
if (result) {
    System.out.println("파일 이동 성공");
} else {
    System.out.println("파일 이동 실패");
}
```

## 참고자료

- N/A
