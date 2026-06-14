---
title: "파일파싱"
linkTitle: "파일파싱"
description: "파일파싱"
url: /common-component/elementary-technology/system/file-parsing/
menu:
  depth:
    name: "파일파싱"
    weight: 44
    parent: "system"
---

## 개요

서버에 저장된 텍스트 파일을 구분자(Delimiter) 또는 고정길이(Fixed-length) 기준으로 파싱하여
데이터를 추출하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일파싱에서 제공하는 기능은 다음과 같다.

1. 구분자(`,`, `|`, `TAB` 등) 기준으로 파일을 파싱하는 기능
2. 고정길이(Fixed-length) 기준으로 파일을 파싱하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFilePars.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일파싱 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Vector | `parsFileByChar(parFile, parChar, parField)` | 구분자 파싱 | 구분자(parChar) 기준으로 파일을 파싱한다. |
| Vector | `parsFileBySize(parFile, parLen, parLine)` | 고정길이 파싱 | 고정길이(parLen) 기준으로 파일을 파싱한다. |

#### 파라미터 정의 (Input)

**구분자 파싱 (`parsFileByChar`)**

- `parFile`: 파싱할 파일 경로 (String 타입)
- `parChar`: 구분자 문자열 (String 타입, 예: `","`, `"|"`, `"TAB"`)
- `parField`: 파싱할 필드 수 (int 타입)

**고정길이 파싱 (`parsFileBySize`)**

- `parFile`: 파싱할 파일 경로 (String 타입)
- `parLen`: 각 필드의 길이 배열 (int[] 타입, 예: `{3, 5, 10}`)
- `parLine`: 읽을 라인 수 (int 타입)

#### 반환값 정의 (Output)

- `Vector<List<String>>` 타입: 파싱된 데이터의 행·열 구조

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;
import java.util.List;
import java.util.Vector;

// 1. 구분자(,) 기준 파싱
String parFile    = "/user/com/sample.csv";
String parChar    = ",";
int    parField   = 3;

Vector<List<String>> resultByChar = EgovFileTool.parsFileByChar(parFile, parChar, parField);

// 2. 고정길이 기준 파싱
int[] parLen  = {3, 5, 10};  // 각 필드 길이
int   parLine = 100;         // 읽을 라인 수

Vector<List<String>> resultBySize = EgovFileTool.parsFileBySize(parFile, parLen, parLine);
```

## 참고자료

- N/A
