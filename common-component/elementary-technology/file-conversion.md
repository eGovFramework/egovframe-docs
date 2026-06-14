---
title: "파일변환"
linkTitle: "파일변환"
description: "파일변환"
url: /common-component/elementary-technology/system/file-conversion/
menu:
  depth:
    name: "파일변환"
    weight: 28
    parent: "system"
---

## 개요

문서 파일(Doc, XLS, PPT 등)을 PDF 형식으로 변환하는 기능을 제공한다.
OpenOffice와 JODConverter 라이브러리를 활용하여 서버 환경에서 문서 변환을 처리한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일변환에서 제공하는 기능은 다음과 같다.

1. DOC(Word) 파일을 PDF로 변환하는 기능
2. XLS(Excel) 파일을 PDF로 변환하는 기능
3. PPT(PowerPoint) 파일을 PDF로 변환하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileConverter.java` | 파일변환 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileCnvr.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일변환 기능은 `EgovFileConverter` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `convertFileToPdf(src, target)` | 파일 PDF 변환 | 지정한 소스 파일을 PDF로 변환하여 대상 경로에 저장한다. 성공 시 true, 실패 시 false 리턴 |

#### 파라미터 정의 (Input)

- `sourcePath`: 변환할 원본 파일의 절대경로 (String 타입)
  (예: `/product/jeus/files/report.doc`)
- `targetPath`: 변환된 PDF 파일이 저장될 절대경로 (String 타입)
  (예: `/product/jeus/files/report.pdf`)

#### 반환값 정의 (Output)

- boolean 타입: 변환 성공 여부 (`true` / `false`)

### 환경 설정

파일변환 기능은 서버에 OpenOffice가 설치되어 있어야 하며, `globals.properties`에 OpenOffice 설치 경로 및 접속 포트를 등록한다.

#### globals.properties

```properties
# OpenOffice 설정
Globals.openoffice.home = /usr/lib/openoffice
Globals.openoffice.port = 8100
```

#### 의존 라이브러리

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.artofsolving</groupId>
    <artifactId>jodconverter</artifactId>
    <version>2.2.2</version>
</dependency>
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileConverter;

String sourcePath = "/product/jeus/files/report.doc";
String targetPath = "/product/jeus/files/report.pdf";

// 파일 변환 수행 (DOC → PDF)
boolean result = EgovFileConverter.convertFileToPdf(sourcePath, targetPath);

if (result) {
    System.out.println("파일 변환 성공: " + targetPath);
} else {
    System.out.println("파일 변환 실패");
}
```

## 참고자료

- N/A
