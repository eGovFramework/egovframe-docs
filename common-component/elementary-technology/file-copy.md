---
title: "파일복사"
linkTitle: "파일복사"
description: "파일복사"
url: /common-component/elementary-technology/system/file-copy/
menu:
  depth:
    name: "파일복사"
    weight: 30
    parent: "system"
---

## 개요

지정한 경로의 파일을 다른 경로로 복사하는 기능을 제공한다. 단일 파일 복사 및 다중 파일 복사를 지원하며,
확장자·수정일자·사이즈·소유자별 조건 복사 기능도 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일복사에서 제공하는 기능은 다음과 같다.

1. 단일 파일을 지정한 경로로 복사하는 기능
2. 다수의 파일을 지정한 디렉토리로 복사하는 기능
3. 확장자 조건별 파일 복사 기능
4. 수정일자 조건별 파일 복사 기능
5. 파일 사이즈 조건별 파일 복사 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileCopy.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일복사 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `copyFile(String source, String target)` | 단일 파일 복사 | 원본 파일을 대상 경로로 복사한다. 성공 시 true, 실패 시 false 리턴 |
| boolean | `copyFiles(String[] source, String target)` | 다중 파일 복사 | 여러 파일을 대상 디렉토리로 복사한다. 성공 시 true, 실패 시 false 리턴 |
| boolean | `copyFilesByExt(String sourceDir, String targetDir, String ext)` | 확장자별 파일 복사 | 지정한 확장자에 해당하는 파일만 복사한다. |
| boolean | `copyFilesByDate(sourceDir, targetDir, fromDate, toDate)` | 일자별 파일 복사 | 지정한 수정일자 범위에 해당하는 파일만 복사한다. |

#### 파라미터 정의 (Input)

- `source`: 복사할 원본 파일의 절대경로 (String 타입)
- `target`: 복사 대상 경로 (String 타입)

#### 반환값 정의 (Output)

- boolean 타입: 복사 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 단일 파일 복사
String sourcePath = "/user/com/source.txt";
String targetPath = "/user/com/backup/source.txt";

boolean result = EgovFileTool.copyFile(sourcePath, targetPath);
if (result) {
    System.out.println("파일 복사 성공");
}

// 다중 파일 복사
String[] sourceFiles = {
    "/user/com/file1.txt",
    "/user/com/file2.txt"
};
String targetDir = "/user/com/backup/";

boolean multiResult = EgovFileTool.copyFiles(sourceFiles, targetDir);
```

## 참고자료

- N/A
