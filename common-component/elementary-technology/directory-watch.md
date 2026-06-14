---
title: "디렉토리감시"
linkTitle: "디렉토리감시"
description: "디렉토리감시"
url: /common-component/elementary-technology/system/directory-watch/
menu:
  depth:
    name: "디렉토리감시"
    weight: 3
    parent: "system"
---

## 개요

특정 디렉토리를 대상으로 디렉토리 내의 시스템에 존재하는 파일과 디렉토리의 변동 내역을 모니터링한다.
특정 디렉토리에 대한 모니터링을 시작하게 되면 정해진 위치에 해당 디렉토리에 대한 로그 파일을 자동생성하고
모니터링된 내역을 기록한다. (로그 파일 설정 관련된 사항은 환경설정 항목을 참조)

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

1. 디렉토리 내의 변화 감시를 시작하는 기능
2. 디렉토리 내의 변화를 조회하는 기능
3. 디렉토리 내의 변화 감시를 종료하는 기능

### 관련소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.service.EgovFileTool.java` | 시스템 정보 확인 요소기술 클래스 | |
| Service | `egovframework.com.utl.service.EgovFileMntrg.java` | 디렉토리 감시 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryMntrg.jsp` | 테스트 페이지 | |

### 메소드

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| `boolean` | `startDirectoryMonitering(String targetDirPath)` | 디렉토리 감시 | 특정 디렉토리에 대한 변화정보 감시를 시작한다. 로그기록 폴더에 로그정보를 기록할 파일을 디렉토리명으로 생성한다(이미 존재하는 경우는 로그를 이어서 기록). 감시 시작 시 true, 실패 시 false 리턴 |
| `StringBuffer` | `getDirectoryMoniteringInfo(String targetDirPath)` | 디렉토리 감시 | 특정 디렉토리 감시로그 정보를 조회한다. 로그기록 폴더에서 대상 디렉토리에 대한 로그 파일을 읽어서 리턴 |
| `boolean` | `stopDirectoryMonitering(String targetDirPath)` | 디렉토리 감시 | 특정 디렉토리에 대한 변화정보 감시를 종료한다. 감시기능을 중단한다. 감시 종료 시 true, 실패 시 false 리턴 |
<!-- markdownlint-enable MD013 -->

### Input

- `targetDirPath`: String 타입의 절대경로를 포함하는 감시시작대상 디렉토리명 (예: `/product/jeus/egovProps/tmp`)

### Output

- `boolean` 타입: 실행여부 `true` / `false`
- `StringBuffer` 타입: 로그정보

## 환경설정

디렉토리 감시기능 사용 시 로그기록 파일 위치에 대한 설정은 `globals.properties`에 등록한다.

- `globals.properties`

```properties
#로그파일 위치 경로
Globals.ConfPath = /product/jeus/egovProps/conf
```

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

String dirTargetPath1 = "/product/jeus/egovProps/tmp";
boolean result1       = EgovFileTool.startDirectoryMonitering(dirTargetPath1);

String dirTargetPath2 = "/product/jeus/egovProps/tmp";
StringBuffer logInfo2 = EgovFileTool.getDirectoryMoniteringInfo(dirTargetPath2);

String dirTargetPath3 = "/product/jeus/egovProps/tmp";
boolean result3       = EgovFileTool.stopDirectoryMonitering(dirTargetPath3);
```

## 참고자료

- N/A
