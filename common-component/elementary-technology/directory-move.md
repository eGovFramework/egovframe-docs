---
title: "디렉토리이동"
linkTitle: "디렉토리이동"
description: "디렉토리이동"
url: /common-component/elementary-technology/system/directory-move/
menu:
  depth:
    name: "디렉토리이동"
    weight: 10
    parent: "system"
---

## 개요

지정한 경로의 디렉토리를 다른 경로로 이동하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

디렉토리이동에서 제공하는 기능은 다음과 같다.

1. 디렉토리를 지정한 타겟 경로로 이동하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryMv.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

디렉토리이동 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `moveFile(dirOriginalPath, dirTargetPath)` | 디렉토리 이동 | 원본 디렉토리를 타겟 경로로 이동한다. 성공 시 true, 실패 시 false 리턴 |

#### 파라미터 정의 (Input)

- `dirOriginalPath`: 이동할 원본 디렉토리의 절대경로 (String 타입)
  (예: `/user/com/dir1`)
- `dirTargetPath`: 이동할 대상 디렉토리의 절대경로 (String 타입)
  (예: `/user/com/dir2`)

#### 반환값 정의 (Output)

- boolean 타입: 이동 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String dirOriginalPath = "/user/com/dir1";
String dirTargetPath   = "/user/com/dir2";

// 디렉토리 이동
boolean result = EgovFileTool.moveFile(dirOriginalPath, dirTargetPath);
if (result) {
    System.out.println("디렉토리 이동 성공");
} else {
    System.out.println("디렉토리 이동 실패");
}
```

## 참고자료

- N/A
