---
title: "메인메뉴"
linkTitle: "메인메뉴"
description: "메인메뉴"
url: /common-component/elementary-technology/interface/main-menu/
menu:
  depth:
    name: "메인메뉴"
    weight: 1
    parent: "interface"
---

## 개요

클라이언트(Client)에서 서버(Server)의 데이터를 받아 메뉴 형태로 보여주는 기능을 제공한다.
메뉴의 추가, 수정, 삭제 기능을 지원하며, 저장된 정보는 트리메뉴 생성에 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

메인메뉴에서 제공하는 기능은 다음과 같다.

1. 서버의 메뉴 데이터(DAT 파일)를 읽어 메뉴 필드 형태로 파싱하는 기능
2. 메뉴관리 화면의 데이터(추가·수정·삭제)를 DAT 파일로 생성하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovMenuGov.java` | 메인메뉴 요소기술 클래스 | 메뉴파일 생성 |
| JSP | `WEB_INF/jsp/egovframework/cmm/EgovMenuGov.jsp` | 테스트 페이지 | 직접 생성 (사용방법 참고) |

### 클래스 및 메소드 설명

메인메뉴 기능은 `EgovMenuGov` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Vector | `parsFileByMenuChar(String parFile, String parChar, int parField)` | 메뉴테이블형태 파싱 | 데이터를 받아 구분값·필드수에 맞추어 메뉴필드 형태로 나눈다 |
| boolean | `setDataByDATFile(String parFile, String[] menuIDArray, String[] menuNameArray, String[] menuLevelArray, String[] menuURLArray)` | 메뉴 데이터 파일 생성 | 메뉴관리 화면의 데이터를 받아 서버 데이터 파일(DAT)을 생성한다 (수정·삭제 반영) |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `parFile`: String 타입의 절대경로를 포함한 메뉴변환파일 (예: `/user/com/test/file1.dat`)
- 메뉴ID / 상위메뉴ID: Number 타입의 숫자 (예: `1`, `10`, `100`)
- 메뉴명: String 타입 (예: `메뉴관리`), URL: String 타입의 URL 경로

#### 반환값 정의 (Output)

- boolean 타입: 생성 성공 여부 / Vector 타입: 파싱된 메뉴 목록

### 사용 방법

DAT 파일의 데이터 형식은 라인별 `nodeId|parentNodeId|nodeName|nodeUrl` 이다.

```java
import egovframework.com.utl.sim.service.EgovMenuGov;

// 1. 서버의 DAT 파일을 읽어 메뉴 필드 형태로 파싱
Vector result = EgovMenuGov.parsFileByMenuChar("/user/com/test/file1.dat", "|", 4);

// 2. 메뉴관리 화면의 데이터를 DAT 파일로 생성
String[] menuIDArray = {"1", "10", "100"};
String[] menuNameArray = {"메인메뉴", "메뉴관리", "하위메뉴"};
String[] menuLevelArray = {"0", "1", "10"};
String[] menuURLArray = {"/main.do", "/menu.do", "/sub.do"};

boolean result2 = EgovMenuGov.setDataByDATFile("/user/com/test/file1.dat",
        menuIDArray, menuNameArray, menuLevelArray, menuURLArray);
```

## 환경설정

해당 계정으로 서버(Server)의 데이터(File 형태)를 읽고 쓸 수 있는 권한을 가진 디렉토리가 지정되어 있어야 한다.

## 참고자료

- [트리메뉴](../tree-menu/) — 메인메뉴로 생성한 DAT 파일을 활용하여 트리메뉴를 표현
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
