---
title: "파일비교"
linkTitle: "파일비교"
description: "파일비교"
url: /common-component/elementary-technology/system/file-compare/
menu:
  depth:
    name: "파일비교"
    weight: 31
    parent: "system"
---

<!-- markdownlint-disable MD025 -->

# 파일비교

## 개요

파일비교(File Compare) 기능은 공통컴포넌트의 요소기술 중 하나로, 서버 및 클라이언트 응용 애플리케이션에서 두 파일의 정보를
비교하는 기능을 제공한다.

### 활용 예시

파일 비교 기능은 다음과 같은 상황에서 활용할 수 있다.

- 백업 파일과 원본 파일의 동일 여부를 확인하는 경우
- 파일 변경 여부를 점검하는 경우
- 배포 전 파일 무결성을 확인하는 경우
- 두 파일의 내용이나 속성을 비교하여 차이를 확인하는 경우

## 주요 개념

두 개의 파일을 지정하여 다음과 같은 파일 속성을 비교할 수 있다.

- 사이즈 비교: 두 파일의 크기가 동일한지 확인한다.
- 수정일자 비교: 두 파일의 마지막 수정 날짜가 동일한지 확인한다.
- 내용 비교: 두 파일(주로 TXT 파일)의 텍스트 내용이 동일한지 확인한다.
- 생성자 비교: 두 파일의 소유자(생성자)가 동일한지 확인한다.

## 설명

파일비교 기능은 `EgovFileTool` 클래스에서 제공하는 다양한 비교 메소드를 이용하여
두 파일의 속성 또는 내용을 비교하는 기능을 제공한다.

비교 결과는 `boolean` 타입으로 반환되며, 비교 항목에 따라 파일 크기, 수정일자,
내용 및 소유자 정보를 확인할 수 있다.

### 파일 사이즈 비교

두 파일의 크기(Size)가 동일한지 비교한다. 파일 크기 바이트(byte) 수가 같으면 `true`를 반환한다.

```java
boolean isSameSize = EgovFileTool.cmprFilesBySize(cmprFile1, cmprFile2);
```

### 파일 수정일자 비교

두 파일의 최종 수정일자(Last Modified Date)가 동일한지 비교한다.

```java
boolean isSameUpdtPd = EgovFileTool.cmprFilesByUpdtPd(cmprFile1, cmprFile2);
```

### 파일 내용 비교

두 파일의 내용(Content)이 동일한지 텍스트 기반으로 비교한다.

```java
boolean isSameContent = EgovFileTool.cmprFilesByContent(cmprFile1, cmprFile2);
```

### 파일 생성자 비교

두 파일의 소유자(Owner) 정보가 동일한지 비교한다.

```java
boolean isSameOwner = EgovFileTool.cmprFilesByOwner(cmprFile1, cmprFile2);
```

## 사용 시 주의사항

- 비교 대상 파일이 모두 존재해야 한다.
- 내용 비교는 텍스트 기반 파일을 대상으로 사용하는 것이 적합하다.
- 파일의 소유자 비교 기능은 운영체제 및 권한 설정에 따라 결과가 달라질 수 있다.

## 참고자료

- [EgovFileTool JavaDoc](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
