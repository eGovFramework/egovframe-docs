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

지정된 디렉토리에 파일을 업로드하는 기능을 제공하는 요소기술이다. 멀티 파트 파일을 파싱하여 서버의 로컬 저장소에 저장하고 파일 사이즈, 확장자 등의 제한을 처리한다.

## 주요 기능

* **다중 파일 업로드**: 여러 개의 파일을 동시에 업로드 처리한다.
* **파일 확장자 제한**: 보안에 취약한 파일(JSP, EXE 등)의 업로드를 차단한다.
* **파일 사이즈 제한**: 업로드 파일의 최대 크기를 검증한다.
* **중복 파일명 처리**: 동일한 파일명이 존재할 경우 고유한 파일명으로 변환하여 저장한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `List<EgovFormBasedFileVo>` | `uploadFiles(request, where, maxFileSize)` | HTTP 요청을 파싱하여 첨부파일들을 지정 경로에 업로드한다. |

```java
import egovframework.com.utl.fcc.service.EgovFormBasedFileUtil;

public class FileUploadExample {
    public void uploadFileExample(HttpServletRequest request) throws Exception {
        String storePath = "/user/local/uploads";
        long maxFileSize = 1024 * 1024 * 10; // 10MB
        
        List<EgovFormBasedFileVo> list = EgovFormBasedFileUtil.uploadFiles(request, storePath, maxFileSize);
        for (EgovFormBasedFileVo vo : list) {
            System.out.println("Uploaded File : " + vo.getPhysicalName());
        }
    }
}
```
