---
title: "디렉토리 압축/해제"
linkTitle: "디렉토리 압축/해제"
description: "디렉토리 압축/해제"
url: /common-component/elementary-technology/system/directory-compress-extract/
menu:
  depth:
    name: "디렉토리 압축/해제"
    weight: 9
    parent: "system"
---

## 개요

비즈니스 로직을 처리하면서 필요한 파일 또는 디렉토리의 압축 및 압축 해제를 위한 공통 기능을 제공한다.

본 기능은 전자정부 표준프레임워크 공통서비스 요소기술 내에 구성되어 있다.

### 활용 예시

디렉토리 압축/해제 기능은 다음과 같은 상황에서 활용할 수 있다.

- 파일 백업 및 보관
- 로그 파일 또는 첨부파일 압축
- 대용량 파일 전송 전 용량 감소
- 압축 파일 업로드 후 서버에서 자동 압축 해제

## 설명

파일 또는 디렉토리 경로를 입력받아 ZIP 형식으로 압축하거나 기존 ZIP 파일을 지정한 경로에 압축 해제하는 기능을 제공한다.

Java의 `java.util.zip` 패키지를 기반으로 구현되어 파일 및 디렉토리의 압축과 복원을 수행한다.

자바 API `java.util.zip.*` 내에 `ZipOutputStream`, `ZipInputStream`을 이용하여 압축 또는 압축 해제 기능을 제공한다.

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileCmprs.java` | 파일 압축 및 해제 요소기술 클래스 | |
| JSP | `WEB-INF/jsp/egovframework/cmm/utl/EgovFileCmprs.jsp` | 테스트 페이지 | |

### 메소드

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| `boolean` | `cmprsFile(String source, String target)` | 압축 | 원본 파일명, 압축 파일명으로 압축 여부 리턴 |
| `boolean` | `decmprsFile(String source, String target)` | 압축 해제 | 압축 파일명, 해제 경로로 압축 해제 여부 리턴 |

### 입력 파라미터 (Input)

- `source` : 압축 대상 파일 또는 디렉토리 경로, 또는 압축 파일 경로
- `target` : 생성할 ZIP 파일 경로 또는 압축 해제 대상 디렉토리 경로

### 반환값 (Output)

- `boolean`
  - `true` : 압축 또는 압축 해제 성공
  - `false` : 압축 또는 압축 해제 실패

## 환경설정

N/A

### 사용 시 주의사항

- 압축 대상 파일 또는 디렉토리가 존재해야 한다.
- 대상 경로에 대한 읽기 및 쓰기 권한이 필요하다.
- 동일한 이름의 파일이 존재하는 경우 덮어쓰기 여부를 사전에 확인하는 것이 좋다.

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovFileCmprs;

String source = "/user/com/sample/test";
String target = "/user/com/sample/test.zip";

// 1. 파일 압축
boolean isCompressed = EgovFileCmprs.cmprsFile(source, target);

// 2. 파일 압축해제
if (isCompressed) {
    String src = target;
    String tar = "/user/com/sample/de_test/";
    boolean deCompressed = EgovFileCmprs.decmprsFile(src, tar);
}
```

## 참고자료

N/A
