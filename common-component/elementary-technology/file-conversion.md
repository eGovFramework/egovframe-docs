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
| Service | `egovframework.com.utl.sim.service.EgovPdfCnvr.java` | 파일변환 요소기술 클래스 | |
| JSP | `WEB-INF/jsp/egovframework/cmm/utl/EgovFileCnvr.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일변환 기능은 `EgovPdfCnvr` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `getPDF(targetPdf, request, response)` | 파일 PDF 변환 | 요청에 첨부된 파일을 PDF로 변환한다. 성공 시 true, 실패 시 false 리턴 |

#### 파라미터 정의 (Input)

- `targetPdf`: 생성할 PDF 파일명 (확장자 제외, String 타입)
  (예: `report`)
- `request`: 변환할 파일이 첨부된 요청 (`HttpServletRequest` 타입)
- `response`: 응답 객체 (`HttpServletResponse` 타입)

#### 반환값 정의 (Output)

- boolean 타입: 변환 성공 여부 (`true` / `false`)
- 메소드가 `throws Exception`으로 선언되어 있어 호출부에서 예외를 처리해야 한다.

### 환경 설정

파일변환 기능은 서버에 OpenOffice가 포트 8100으로 기동되어 있어야 한다. 접속 포트는 소스에 고정되어 있어 별도로 등록하지 않는다.
첨부된 파일을 임시로 저장할 경로는 `globals.properties`의 `Globals.fileStorePath`를 사용한다.

#### globals.properties

```properties
# 파일 저장 경로
Globals.fileStorePath = /upload/allinone
```

#### 의존 라이브러리

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.artofsolving</groupId>
    <artifactId>jodconverter</artifactId>
    <version>2.2.1</version>
</dependency>
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovPdfCnvr;

// 요청에 첨부된 파일을 report.pdf 로 변환한다.
try {
    boolean result = EgovPdfCnvr.getPDF("report", request, response);

    if (result) {
        System.out.println("파일 변환 성공");
    } else {
        System.out.println("파일 변환 실패");
    }
} catch (Exception e) {
    System.out.println("파일 변환 중 오류 발생");
}
```

## 참고자료

- N/A
