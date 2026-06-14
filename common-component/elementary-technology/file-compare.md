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

## 주요 개념

두 개의 파일을 지정하여 다음과 같은 파일 속성을 비교할 수 있다.

- 사이즈 비교: 두 파일의 크기가 동일한지 확인한다.
- 수정일자 비교: 두 파일의 마지막 수정 날짜가 동일한지 확인한다.
- 내용 비교: 두 파일(주로 TXT 파일)의 텍스트 내용이 동일한지 확인한다.
- 생성자 비교: 두 파일의 소유자(생성자)가 동일한지 확인한다.

## 설명

파일비교 기능은 `egovframework.com.utl.sim.service.EgovFileTool` 클래스를 통해 제공되며, 목적에 맞는
다양한 비교 메서드를 사용하여 두 파일의 동일성 여부(`boolean`)를 확인할 수 있다.

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

## 참고자료

- [EgovFileTool JavaDoc](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
