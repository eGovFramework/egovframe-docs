---
title: "파일생성"
linkTitle: "파일생성"
description: "파일생성"
url: /common-component/elementary-technology/system/file-create/
menu:
  depth:
    name: "파일생성"
    weight: 33
    parent: "system"
---

## 개요

지정한 경로에 새로운 텍스트 파일을 생성하는 기능을 제공한다. 대상 경로에 디렉토리가 존재하지 않을 경우
자동으로 디렉토리를 생성하여 파일을 만든다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일생성에서 제공하는 기능은 다음과 같다.

1. 지정한 절대경로에 새로운 파일을 생성하는 기능
2. 파일 경로에 디렉토리가 없을 경우 자동으로 디렉토리를 생성하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileCre.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일생성 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `createNewFile(String fileCreationPath)` | 파일 생성 | 지정한 절대경로에 새로운 파일을 생성한다. 성공 시 생성된 파일의 절대경로, 실패 시 빈 문자열 리턴 |

#### 파라미터 정의 (Input)

- `fileCreationPath`: 생성할 파일의 절대경로 및 파일명 (String 타입)
  (예: `/user/com/file1.txt`)

#### 반환값 정의 (Output)

- String 타입: 생성 성공 시 생성된 파일의 절대경로, 실패 시 빈 문자열(`""`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 생성할 파일의 절대경로 설정
String fileCreationPath = "/user/com/sample/file1.txt";

// 파일 생성 실행
String result = EgovFileTool.createNewFile(fileCreationPath);

// 결과 확인
if (!"".equals(result)) {
    System.out.println("파일 생성 성공: " + result);
} else {
    System.out.println("파일 생성 실패");
}
```

## 참고자료

- N/A
