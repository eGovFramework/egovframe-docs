---
title: "파일다운로드"
linkTitle: "파일다운로드"
description: "파일다운로드"
url: /common-component/elementary-technology/system/file-download/
menu:
  depth:
    name: "파일다운로드"
    weight: 27
    parent: "system"
---

## 개요

서버에 저장된 파일을 사용자가 웹 브라우저를 통해 다운로드할 수 있는 기능을 제공한다.
한글 파일명 처리 및 대용량 파일 스트리밍 다운로드를 지원한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일다운로드에서 제공하는 기능은 다음과 같다.

1. 서버에 저장된 파일을 클라이언트로 전송하는 기능
2. 한글 파일명이 포함된 파일을 정상적으로 다운로드하는 기능
3. 스트리밍 방식으로 대용량 파일을 다운로드하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.sim.web.EgovFileDownloadController.java` | 파일다운로드 컨트롤러 | |
| Util | `egovframework.com.utl.sim.service.EgovFileMngUtil.java` | 파일 처리 유틸리티 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileDownload.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일다운로드 기능은 `EgovFileMngUtil` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| void | `fileDownload(filePath, fileName, response)` | 파일 다운로드 | 파일을 HTTP 응답으로 전송한다. Response Header로 파일명 인코딩을 처리한다. |

#### 파라미터 정의 (Input)

- `filePath`: 다운로드할 파일의 서버 절대경로 (String 타입)
- `fileName`: 다운로드 시 사용자에게 표시할 파일명 (String 타입)
- `response`: HTTP 응답 객체 (`HttpServletResponse` 타입)

### 환경 설정

`globals.properties`에 파일 저장 경로를 등록한다.

#### globals.properties

```properties
# 파일 저장 경로
Globals.fileStorePath = /product/jeus/egovProps/upload/
```

### 사용 방법

#### Controller 구현 예시

```java
import egovframework.com.utl.sim.service.EgovFileMngUtil;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@GetMapping("/file/download")
public void downloadFile(
        @RequestParam String filePath,
        @RequestParam String fileName,
        HttpServletResponse response) throws Exception {

    // 파일 경로 유효성 검증 (Directory Traversal 방지)
    // EgovWebUtil.filePathBlackList(filePath);

    // 파일 다운로드 처리
    EgovFileMngUtil.fileDownload(filePath, fileName, response);
}
```

#### Response Header 설정 예시

```java
// Content-Type 설정
response.setContentType("application/octet-stream");

// Content-Disposition 설정 (한글 파일명 인코딩)
String encodedFileName = new String(fileName.getBytes("UTF-8"), "ISO-8859-1");
response.setHeader("Content-Disposition",
    "attachment; filename=\"" + encodedFileName + "\"");

// Content-Length 설정
response.setContentLength((int) file.length());
```

## 참고자료

- N/A
