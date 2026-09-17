---
title: "파일속성정보체크"
linkTitle: "파일속성정보체크"
description: "파일속성정보체크"
url: /common-component/elementary-technology/system/file-attribute-check/
menu:
  depth:
    name: "파일속성정보체크"
    weight: 34
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `checkReadAuth`, `checkWriteAuth`, `getAccess`, `getFileName`, `getMountLc`, `getOwner`, `getUpdtDate` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 파일명, 수정일자, 권한은 `java.io.File`로 확인한다.

## 개요

파일 속성정보인 파일명, 최종수정일자, 읽기권한, 쓰기권한, 크기를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

- 파일의 존재 여부와 상태를 확인하는 경우
- 파일의 읽기 및 쓰기 권한을 점검하는 경우
- 파일의 최종 수정일자를 확인하는 경우

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 파일 속성 조회 | 5.0 `EgovFileTool`에는 속성 조회 메소드가 없음 |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `File.getName()` | 파일명 조회 | 경로의 마지막 이름 |
| long | `File.lastModified()` | 수정일자 조회 | 최종 수정 시각(epoch millisecond) |
| long | `File.length()` | 크기 조회 | 파일 크기(byte) |
| boolean | `File.canRead()` | 읽기권한 조회 | 읽기 가능 여부 |
| boolean | `File.canWrite()` | 쓰기권한 조회 | 쓰기 가능 여부 |

소유자·접근권한 문자열·마운트 경로를 조회하던 쉘 스크립트 기반 메소드는 5.0에서 제거되었다.

### 사용 방법

```java
import java.io.File;

File file = new File("/product/jeus/test/samples/common.xml");

String fileName = file.getName();
long updtDate = file.lastModified();
long size = file.length();
boolean canRead = file.canRead();
boolean canWrite = file.canWrite();
```

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
