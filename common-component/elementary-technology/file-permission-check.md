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

파일의 읽기 권한 및 쓰기 권한 유무를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일권한체크에서 제공하는 기능은 다음과 같다.

1. 파일의 읽기 권한 유무를 확인하는 기능
2. 파일의 쓰기 권한 유무를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileAuthor.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일권한체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `checkReadAuth(String file)` | 읽기권한 조회 | 파일의 읽기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |
| boolean | `checkWriteAuth(String file)` | 쓰기권한 조회 | 파일의 쓰기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |

#### 파라미터 정의 (Input)

- `file`: String 타입의 절대경로를 포함하는 확인 대상 파일 경로
  (예: `/user/com/sample/test.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 권한 유무 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String filePath = "/user/com/sample/test.txt";

// 읽기 권한 확인
boolean readVal  = EgovFileTool.checkReadAuth(filePath);

// 쓰기 권한 확인
boolean writeVal = EgovFileTool.checkWriteAuth(filePath);

System.out.println("읽기 권한: " + readVal);
System.out.println("쓰기 권한: " + writeVal);
```

## 참고자료

- N/A
