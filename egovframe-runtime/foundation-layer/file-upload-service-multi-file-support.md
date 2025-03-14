---
title: Spring mvc Multipart Multi file upload 지원 문제
linkTitle: "Multipart"
description: Spring MVC 2.5.5에서 동일한 이름의 여러 파일을 업로드할 때 발생하는 MultipartResolver 오류 문제를 설명한다.
url: /egovframe-runtime/foundation-layer/file-upload-download-service/file-upload/file-upload-service-multi-file-support/
menu:
    depth:
        name: "Multipart"
        weight: 1
        parent: "fileUpload"
---
# Spring mvc Multipart Multi file upload 지원 문제

## 개요

Spring mvc 2.5.5 Multipart Multi file upload 지원부분에서 동일한 이름의 여러개의 파일을 올리려고 할 때 에러가 발생한다. 본 가이드에서는 이러한 문제가 발생하여 아직 Spring쪽에서 답변이 없는 상황이다. 이부분에 대하여 개발시 참고 하기바란다.

## 설명

업로드 갯수를 고려하지 않고 동적으로 upload 폼을 추가할 경우 오류 메시지가 나온다.

```java
org.springframework.web.multipart.MultipartException: Multiple files for field name [files] found - not supported by MultipartResolver
org.springframework.web.multipart.commons.CommonsFileUploadSupport.parseFileItems(CommonsFileUploadSupport.java:254)
org.springframework.web.multipart.commons.CommonsMultipartResolver.parseRequest(CommonsMultipartResolver.java:166)
org.springframework.web.multipart.commons.CommonsMultipartResolver.resolveMultipart(CommonsMultipartResolver.java:149)
org.springframework.web.servlet.DispatcherServlet.checkMultipart(DispatcherServlet.java:1015)
org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:851)
org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:807)
org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:571)
org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:511)
javax.servlet.http.HttpServlet.service(HttpServlet.java:637)
javax.servlet.http.HttpServlet.service(HttpServlet.java:717)
```

이러한 문제에 대해서 아래의 참고 자료를 참고하기 바란다.

## 참고자료

- (deplicated) Implementing single and multiple file multipart uploads using Spring 2.5
- (deplicated) 동일한 form name upload 문제
- (deplicated) spring mvc 2.5.5 multipart multi file upload 지원