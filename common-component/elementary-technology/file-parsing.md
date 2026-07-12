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

사용자가 업로드한 파일 및 서버(Server)의 텍스트 파일을 특정 구분자(`,`, `|`, `TAB`)로 파싱하여 정보를 추출하는 기능을 제공한다.
또한 파일의 텍스트 라인을 일정 길이(Size)별로 파싱하여 정보를 추출할 수 있다.
사용자 정보, 제품목록 정보 등을 CSV 파일로 작성하여 서버에 업로드한 후 파싱하여 일괄적으로 데이터베이스에 입력하는 경우에 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일파싱에서 제공하는 기능은 다음과 같다.

1. 텍스트 파일을 구분자에 의해 파싱하는 기능
2. 텍스트 파일을 일정 길이에 의해 파싱하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFilePars.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일파싱 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Vector | `parsFileByChar(String parFile, String parChar, int parField)` | 특정구분자 파일파싱 | 파일을 특정 구분자(콤마, 파이프, TAB)로 파싱한다 |
| Vector | `parsFileBySize(String parFile, int[] parLen, int parLine)` | 일정길이 파일파싱 | 파일을 필드별 일정 길이로 파싱한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `parFile`: String 타입의 절대경로를 포함한 파일명 (예: `/user/com/test/file1.txt`)
- `parChar`: String 타입의 파싱 구분자 (예: `,`)
- `parField`: int 타입의 파싱 필드수 (예: `3`)
- `parLen`: int[] 타입의 각 필드 길이 (예: `{3, 3, 3}`)
- `parLine`: int 타입의 읽어낼 라인수 (예: `10`)

#### 반환값 정의 (Output)

- Vector 타입: 파싱 결과 구조체 (라인별 필드 목록)

### 사용 방법

```java
import java.util.List;
import java.util.Vector;

import egovframework.com.utl.sim.service.EgovFileTool;

// 1. 특정 구분자 파일파싱
String parFile = "/user/com/test/file1.txt";
Vector<List<String>> result1 = EgovFileTool.parsFileByChar(parFile, ",", 3);

// 2. 일정 길이 파일파싱
int[] parLen = {3, 3, 3};
int parLine = 10;
Vector<List<String>> result2 = EgovFileTool.parsFileBySize(parFile, parLen, parLine);
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
