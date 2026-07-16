---
title: "파일업로드"
linkTitle: "파일업로드"
description: "파일업로드"
url: /common-component/elementary-technology/system/file-upload/
menu:
  depth:
    name: "파일업로드"
    weight: 40
    parent: "system"
---

## 개요

첨부파일에 대한 업로드 기능을 제공한다. `MultipartHttpServletRequest` 및 `MultipartFile`을 통해 첨부된 파일 정보를
취득하고 서버에 저장하는 기능을 처리한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일업로드에서 제공하는 기능은 다음과 같다.

1. 첨부로 등록된 파일을 서버에 업로드하는 기능
2. 첨부로 등록된 파일에 대한 정보를 취득하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.cmm.service.EgovFileMngUtil.java` | 첨부파일 처리 공통 유틸리티 | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovFileUpload.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일업로드 기능은 `EgovFileMngUtil` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| HashMap | `uploadFile(MultipartFile file)` | 파일 업로드 | 첨부로 등록된 파일을 서버에 업로드한다 |
| List | `parseFileInf(Map<String, MultipartFile> files, String key, int fileKeyParam, String atchFileId, String storePath)` | 첨부파일 정보취득 | 첨부로 등록된 파일에 대한 정보(FileVO 목록)를 얻는다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `file`: `MultipartHttpServletRequest` 객체로부터 얻어진 `MultipartFile` 객체 (null이 아닌 유효 객체)
- `files`: 첨부파일 Map, `key`: 파일 구분 키, `atchFileId`: 첨부파일 ID, `storePath`: 저장 경로

#### 반환값 정의 (Output)

- HashMap 타입: 업로드된 파일 정보 (파일경로, 사이즈, 원본파일명, 업로드파일명, 확장자)
- List 타입: `FileVO` 객체 리스트

### 사용 방법

```java
import java.util.HashMap;
import java.util.Iterator;

import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import egovframework.com.cmm.service.EgovFileMngUtil;

MultipartHttpServletRequest mptRequest = (MultipartHttpServletRequest) request;

Iterator<String> fileIter = mptRequest.getFileNames();

while (fileIter.hasNext()) {
    MultipartFile mFile = mptRequest.getFile(fileIter.next());

    if (mFile.getSize() > 0) {
        HashMap<String, String> map = EgovFileMngUtil.uploadFile(mFile);
        // map에서 파일경로, 사이즈, 원본파일명, 업로드파일명, 확장자 정보를 취득
    }
}
```

## 환경설정

파일 저장 위치를 지정하기 위해서 `EgovPropertyService` 서비스를 사용한다.
`globals.properties` 파일의 `Globals.fileStorePath` 속성에 파일 저장 경로를 정의한다.

```properties
Globals.fileStorePath = C:/egovframework/upload/
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
- 파일다운로드 문서 참조: [파일다운로드](../file-download/)
