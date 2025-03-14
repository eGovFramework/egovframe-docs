---
title: 파일업로드 예제(File upload example)
linkTitle: "파일업로드 예제"
description: Apache Commons FileUpload의 CommonsMultipartResolver를 사용한 파일 업로드 예제로, 이미지 파일을 업로드하고 화면에 표시하는 기능을 설명한다.
url: /runtime-example/individual-example/foundation-layer/file-upload-example/
menu:
    depth:
        name: 파일업로드 예제
        weight: 5
        parent: "foundationLayer"
---
# 파일업로드 예제(File upload example)

## 개요
Apache Commens FileUpload에서 제공하는 CommonsMultipartResolver를 사용한 예제이다.

## 설명
1. 해당 예제를 실행하면 간단한 파일업로드 페이지가 호출된다.

![fileupload-1](./images/fileupload-1.png)

2. 선택버튼을 눌러 업로드할 이미지파일을 선택한다.

![fileupload-2](./images/fileupload-2.png)

3. 업로드버튼을 누르면 예제의 루트디렉토리에 있는 image폴더에 파일이 업로드되고 화면에 표시된다.

![fileupload-3](./images/fileupload-3.png)

## 참고자료
- [File Upload/Downlowd 서비스](../../../egovframe-runtime/foundation-layer/file-upload-download-service.md)
- [File Upload 서비스](../../../egovframe-runtime/foundation-layer/file-upload-service.md)