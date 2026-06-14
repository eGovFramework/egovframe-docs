---
title: "파일동기화"
linkTitle: "파일동기화"
description: "파일동기화"
url: /common-component/elementary-technology/system/file-sync/
menu:
  depth:
    name: "파일동기화"
    weight: 46
    parent: "system"
---

## 개요

다중 애플리케이션 서버(AP Server) 환경에서 파일 저장·삭제 시 대상 서버 목록을 관리하고, 변경사항을 각
서버에 동기화하는 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일동기화에서 제공하는 기능은 다음과 같다.

1. 동기화 대상 서버 목록을 조회하는 기능
2. 동기화 대상 서버를 등록·수정·삭제하는 기능
3. 파일 저장·삭제 시 대상 서버들에 자동으로 동기화를 처리하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.sys.sync.web.EgovSynchrnServerController.java` | 동기화 서버 관리 컨트롤러 | |
| Service | `egovframework.com.utl.sys.sync.service.EgovSynchrnServerService.java` | 동기화 서비스 인터페이스 | |
| ServiceImpl | `egovframework.com.utl.sys.sync.service.impl.EgovSynchrnServerServiceImpl.java` | 동기화 서비스 구현체 | |

### 환경 설정

`globals.properties`에 동기화 서버 경로를 등록한다.

#### globals.properties

```properties
# 파일동기화 서버 경로 (절대경로, 끝에 '/' 필수)
Globals.SynchrnServerPath = /product/jeus/egovProps/sync/
```

### 사용 방법

파일동기화 기능은 파일 업로드·삭제 서비스와 연계하여 동기화 처리를 자동으로 수행한다.
동기화 대상 서버는 관리자 화면을 통해 등록·관리하며, 파일 저장·삭제 이벤트 발생 시
등록된 모든 서버에 동일한 작업이 처리된다.

```java
import egovframework.com.utl.sys.sync.service.EgovSynchrnServerService;

// 동기화 서버 목록 조회 (스프링 DI 활용)
List<SynchrnServerVO> serverList = egovSynchrnServerService.selectSynchrnServerList();

// 파일 저장 및 동기화 처리 (서비스 레이어에서 자동 처리)
egovSynchrnServerService.syncFile(filePath, syncTargetServers);
```

## 참고자료

- N/A
