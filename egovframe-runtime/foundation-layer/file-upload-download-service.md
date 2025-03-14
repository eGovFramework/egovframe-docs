---
title: File Upload/Download 서비스
linkTitle: "File Upload/Download"
description: Commons FileUpload를 사용해 파일 업로드 API를 제공하며, 멀티 파일 업로드 문제와 해결 방법을 설명한다.
url: /egovframe-runtime/foundation-layer/file-upload-download-service/
menu:
    depth:
        name: File Upload/Download
        weight: 16
        parent: "foundation-layer"
        identifier: "fileUpload-download"
---
# File Upload/Download 서비스

## 개요

**전자정부 프레임워크**에서는 다양한 파일 업로드 API를 제공하는 Commons FileUpload를 오픈 소스로 채택하였다.

Spring 에서는 [Commons FileUpload](http://commons.apache.org/fileupload/)를 사용하여 싱글 파일 업로드에 대하여 가이드 하고 있다.
현재 Spring에서 싱글 파일 업로드에 대해서 매우 좋은 api를 제공해주고 있으나 **멀티플 파일 업로드**시에 동일한 이름의 여러 개의 파일을 올리려고 할 때 오류가 발생한다.

오류 사항에 대해서는 [multipart multi file upload](file-upload-service-multi-file-support.md) 지원 문제를 참고.

본 매뉴얼에서는 싱글 파일 업로드 보다 **멀티플 파일 업로드**를 가능하도록 그 대안에 대하여 설명하고자 한다.

## 설명

#### 데이터 전송방식

데이터를 전송하는 방식에는 GET 방식과 POST 방식, 그리고 ENCTYPE 속성의 "multipart/form-data"이 있다.

- GET
  - URL에 폼데이터가 노출되기 때문에 입력 내용의 길이 제한이 있고 256byte~4096byte 까지의 데이터를 전송할 수 있다.
- POST
  - URL에 노출되지 않고 데이터를 전송하기 때문에 입력 내용의 길이에 제한을 받지 않는다. 

이렇게 데이터를 전송하는데 아무 문제 없을 것 처럼 보이지만, 이 둘은 보낼 수 있는 데이터 양에 한계가 있다.

파일이나 용량이 큰 데이터를 전송할 때 문제가 생기는 것이다.

그 때 쓰는 폼 데이터 전송방식이 바로 **ENCTYPE** 속성의 **multipart/form-data** 이다.

**전자정부 프레임워크**에서는 스프링에서 제공하는 Apache Commons FileUpload API를 이용하여 파일 업로드를 처리하는 [CommonsMultipartResolver](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/commons/CommonsMultipartResolver.html) 클래스를 제공하고 다음과 같이 설정파일에 CommonsMultipartResolver를 빈으로 등록하여 준다.

Apache Commens FileUpload 에서 싱글 파일 업로드에 대해서 매우 좋은 api를 제공해주고 있다. 하지만 멀티플 파일 업로드시 동일한 이름의 여러 개의 파일을 올리려고 할 때 오류가 발생한다.

여러 개의 파일을 올리려고 할 때 오류가 발생하는 문제에 대해서는 [multipart multi file upload 지원 문제](file-upload-service-multi-file-support.md)를 참고.

Spring에서 multipart를 사용한 파일 업로드에 대해서는 [Spring's multipart (fileupload) support](http://static.springframework.org/spring/docs/2.5.x/reference/mvc.html#mvc-multipart) 에서 자세하게 가이드 하였으므로 본 메뉴얼에서는 다루지 않는다.

기능 실행에 대한 이해를 돕기 위해 컨텐츠와 함께 컨텐츠에서 제시한 샘플 코드를 포함하고 있는 이클립스 프로젝트 형태의 웹 애플리케이션 샘플 프로젝트를 다운로드할 수 있다.

### File Upload / Download

File Upload / Download 에 대한 설명은 아래 상세 페이지를 참고하라.

- [File Upload](./file-upload-service.md)
- [multipart multi file upload 지원 문제](./file-upload-service-multi-file-support.md)
- [File Download](./file-download-service.md)
- [Tomcat에서 한글이 깨지는 문제 해결](./file-download-service-tomcat-encoding.md)

### 예제 Sample 실행

1. utilappSample.zip([utilappsample.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:rte2:fdl:utilappsample.zip)) 파일을 다운로드 받는다.
2. 이클립스에서 다운로드 받은 폴더를 선택하여 프로젝트를 Import 한다.
3. lib에 라이브러리 파일이 있는지 확인한다.
4. src 폴더 아래에 Index.jsp를 선택하여 마우스 오른쪽 클릭하여 Run As > Run On Server를 실행한다.
5. Console 창에서 정상적으로 Tomcat이 실행된 것을 확인한다.
6. 본 샘플에서는 CommonsMultipartResolver를 보완한 MultiCommonsMultipartResolver를 사용하고 있으나 **CommonsMultipartResolver** 사용을 권장함.

multiple files with a single file(한단 샘플)에서 사용한 JavaScript를 사용하여 추가 시 다른 form name을 추가하여 처리하는 방식을 가이드 하였으니 참고하기 바란다.

**샘플 utilappSample의 Index.jsp 실행하였을 경우 브라우저에서 실행되는 화면**

![file-updown-service-sample-screenshot](./images/file-updown-service-sample-screenshot.png)

## 참고자료

- [Spring's multipart (fileupload) support {mvc-multipart}](http://static.springframework.org/spring/docs/2.5.x/reference/mvc.html#mvc-multipart)
- [Spring's multipart (fileupload) support {CommonsMultipartResolver.html}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/commons/CommonsMultipartResolver.html)
- [Spring's multipart (fileupload) support {RequestFacade}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/MultipartResolver.html)
- [Spring's multipart (fileupload) support {MultipartHttpServletRequest}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/MultipartHttpServletRequest.html)
- [Spring's multipart (fileupload) support {CommonsFileUploadSupport}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/commons/CommonsFileUploadSupport.html)
- [Spring's multipart (fileupload) support {CommonsFileUploadSupport}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/servlet/mvc/SimpleFormController.html)
- [Spring's multipart (fileupload) support {parseFileItems}](http://static.springframework.org/spring/docs/2.5.x/api/org/springframework/web/multipart/commons/CommonsFileUploadSupport.html#parseFileItems(java.util.List,%20java.lang.String))
- [commons.apache.org {fileupload}](http://commons.apache.org/fileupload/)
- [commons.apache.org{empty-parse}](http://commons.apache.org/fileupload/faq.html#empty-parse)

## 예제
- [파일업로드 예제](../../runtime-example/individual-example/foundation-layer/file-upload-example.md)