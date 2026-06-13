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

## 설명

파일 또는 디렉토리 경로를 문자열로 입력받아 압축 또는 압축 해제하는 기능이다.

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

## 환경설정

N/A

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
