---
title: "파일존재체크"
linkTitle: "파일존재체크"
description: "파일존재체크"
url: /common-component/elementary-technology/system/file-exist-check/
menu:
  depth:
    name: "파일존재체크"
    weight: 43
    parent: "system"
---

## 개요

디렉토리에 파일이 존재하는지 체크하는 기능을 제공한다. 파일명뿐 아니라 확장자, 수정기간, 사이즈, 생성자(Owner)별 조건으로도
파일의 존재 여부를 확인할 수 있다. 서버(Server) 및 클라이언트(Client) 응용 애플리케이션에서 파일 존재 체크 시 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일존재체크에서 제공하는 기능은 다음과 같다.

1. 디렉토리에 특정 파일이 존재하는지 체크하는 기능
2. 파일 확장자별로 파일이 존재하는지 체크하는 기능
3. 파일 수정기간별로 파일이 존재하는지 체크하는 기능
4. 파일 사이즈별로 파일이 존재하는지 체크하는 기능
5. 파일 생성자(Owner)별로 파일이 존재하는지 체크하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileExst.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일존재체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `checkFileExstByName(String dir, String file)` | 파일존재확인 | 디렉토리에 파일이 존재하는지 체크한다 |
| boolean | `checkFileExstByExtnt(String dir, String eventn)` | 확장자별 파일존재확인 | 확장자별로 디렉토리에 파일이 존재하는지 체크한다 |
| boolean | `checkFileExstByOwner(String dir, String owner)` | 생성자별 파일존재확인 | 생성자별로 디렉토리에 파일이 존재하는지 체크한다 |
| boolean | `checkFileExstByUpdtPd(String dir, String updtFrom, String updtTo)` | 수정기간별 파일존재확인 | 수정기간별로 디렉토리에 파일이 존재하는지 체크한다 |
| boolean | `checkFileExstBySize(String dir, long sizeFrom, long sizeTo)` | 사이즈별 파일존재확인 | 사이즈별로 디렉토리에 파일이 존재하는지 체크한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `dir`: String 타입의 절대경로를 포함한 디렉토리 (예: `/user/com/test`)
- `file`: String 타입의 파일명 (예: `file1.txt`)
- `eventn`: String 타입의 확장자 (예: `.txt` 형태로 입력)
- `updtFrom` / `updtTo`: String 타입의 수정기간 시작/종료일자 (예: `20090501`, YYYYMMDD 형태)
- `sizeFrom` / `sizeTo`: long 타입의 사이즈 범위 (KB 단위)
- `owner`: String 타입의 파일 생성자 (예: `com`)

#### 반환값 정의 (Output)

- boolean 타입: 파일 존재 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 1. 파일 존재 확인
boolean result1 = EgovFileTool.checkFileExstByName("/user/com/test", "file1.txt");

// 2. 확장자별 파일 존재 확인
boolean result2 = EgovFileTool.checkFileExstByExtnt("/user/com/test", ".txt");

// 3. 수정기간별 파일 존재 확인
boolean result3 = EgovFileTool.checkFileExstByUpdtPd("/user/com/test", "20090501", "20090531");

// 4. 사이즈별 파일 존재 확인
boolean result4 = EgovFileTool.checkFileExstBySize("/user/com/test", 100L, 2000L);
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
