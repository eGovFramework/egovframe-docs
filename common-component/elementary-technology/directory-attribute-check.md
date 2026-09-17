---
title: "디렉토리속성정보체크"
linkTitle: "디렉토리속성정보체크"
description: "디렉토리속성정보체크"
url: /common-component/elementary-technology/system/directory-attribute-check/
menu:
  depth:
    name: "디렉토리속성정보체크"
    weight: 8
    parent: "system"
---

> **5.0 적용 범위:** 이전 가이드의 `canRead`, `canWrite`, `getAccess`, `getDirectorySize`, `getLastModifiedDateFromFile`, `getName`, `getOwner` 메소드는
> [공통컴포넌트 5.0의 EgovFileTool](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.6/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)에 없다.
> 디렉토리명, 수정일자, 권한은 `java.io.File`로 확인한다.

## 개요

디렉토리 속성정보인 디렉토리명, 최종수정일자, 읽기권한, 쓰기권한을 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

- 애플리케이션이 사용하는 디렉토리의 존재 여부와 상태를 확인하는 경우
- 파일 업로드 또는 로그 저장 경로의 읽기·쓰기 권한을 점검하는 경우

## 설명

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| JDK | `java.io.File` | 디렉토리 속성 조회 | 5.0 `EgovFileTool`에는 속성 조회 메소드가 없음 |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 하위 파일 목록 조회 | `getSubFilesByAll` |

### 클래스 및 메소드 설명

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `File.getName()` | 디렉토리명 조회 | 경로의 마지막 이름 |
| long | `File.lastModified()` | 수정일자 조회 | 최종 수정 시각(epoch millisecond) |
| boolean | `File.canRead()` | 읽기권한 조회 | 읽기 가능 여부 |
| boolean | `File.canWrite()` | 쓰기권한 조회 | 쓰기 가능 여부 |
| List | `EgovFileTool.getSubFilesByAll(File[] fileArray)` | 하위 파일 목록 | 용량 합산이 필요하면 이 목록을 순회한다 |

소유자·접근권한 문자열을 조회하던 쉘 스크립트 기반 메소드는 5.0에서 제거되었다.

### 사용 방법

```java
import java.io.File;
import java.util.List;

import egovframework.com.utl.sim.service.EgovFileTool;

File dir = new File("/user/com/jeus");
String directoryName = dir.getName();
long lastModified = dir.lastModified();
boolean canRead = dir.canRead();
boolean canWrite = dir.canWrite();

long dirSize = 0L;
if (dir.isDirectory()) {
    List<String> files = EgovFileTool.getSubFilesByAll(dir.listFiles());
    for (String path : files) {
        dirSize += new File(path).length();
    }
}
```

## 참고자료

- [EgovFileTool 소스](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
