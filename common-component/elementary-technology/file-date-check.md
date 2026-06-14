---
title: "파일일자체크"
linkTitle: "파일일자체크"
description: "파일일자체크"
url: /common-component/elementary-technology/system/file-date-check/
menu:
  depth:
    name: "파일일자체크"
    weight: 42
    parent: "system"
---

## 개요

파일의 최종 수정일자를 확인하거나, 수정일자 조건별로 파일 목록을 조회하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일일자체크에서 제공하는 기능은 다음과 같다.

1. 특정 파일의 최종 수정일자를 확인하는 기능
2. 특정 일자에 수정된 파일 목록을 조회하는 기능
3. 수정 기간(from~to) 내에 수정된 파일 목록을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileDtCeck.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일일자체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getUpdtDate(String file)` | 수정일자 조회 | 파일의 최종 수정일자를 조회한다. 성공 시 8자리 날짜(yyyyMMdd), 실패 시 빈 문자열 리턴 |
| ArrayList | `getFileListByDate(String dir, String date)` | 특정 일자별 파일 목록 조회 | 지정한 디렉토리 내에서 특정 수정일자에 해당하는 파일 목록을 반환한다. |
| ArrayList | `getFileListByUpdtPd(dir, from, to)` | 수정 기간별 파일 목록 조회 | 지정한 디렉토리 내에서 수정 기간(from~to)에 해당하는 파일 목록을 반환한다. |

#### 파라미터 정의 (Input)

- `file` / `dir`: String 타입의 절대경로
- `date`: 조회 기준 일자 (String 타입, `yyyyMMdd` 형식, 예: `"20260614"`)
- `from`, `to`: 조회 기간 시작·종료 일자 (String 타입, `yyyyMMdd` 형식)

#### 반환값 정의 (Output)

- String 타입: 파일 최종 수정일자 (8자리, `yyyyMMdd` 형식)
- ArrayList 타입: 조건에 해당하는 파일 경로 목록

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;
import java.util.ArrayList;

String filePath = "/user/com/test/sample.txt";

// 1. 파일 최종 수정일자 확인
String lastModifiedDate = EgovFileTool.getUpdtDate(filePath);
System.out.println("최종 수정일자: " + lastModifiedDate); // 예: 20260614

// 2. 특정 일자에 수정된 파일 목록 조회
String dir  = "/user/com/test";
String date = "20260614";
ArrayList fileList = EgovFileTool.getFileListByDate(dir, date);

// 3. 수정 기간 내 파일 목록 조회
String fromDate = "20260601";
String toDate   = "20260614";
ArrayList periodFileList = EgovFileTool.getFileListByUpdtPd(dir, fromDate, toDate);
```

## 참고자료

- N/A
