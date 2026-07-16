---
title: "파일동기화"
linkTitle: "파일동기화"
description: "파일동기화"
url: /common-component/elementary-technology/system/file-sync/
menu:
  depth:
    name: "파일동기화"
    weight: 38
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

파일동기화는 파일 저장 및 삭제에 대하여 여러 AP 서버에 동기화시키는 기능으로,
AP 서버들 간 동기화를 통해 파일 첨부 및 다운로드 기능을 제공한다.

## 설명

파일동기화는 파일 저장 및 삭제에 대하여 여러 AP 서버에 동기화시키기 위한 목적으로
동기화대상 서버정보의 등록, 수정, 삭제, 조회, 목록조회 기능 및 파일 동기화 처리 기능을 수반한다.

1. **동기화대상서버목록조회**: 동기화대상 서버정보를 최근 등록 순서대로 조회하고, 그 결과를 화면에 반영한다.
2. **동기화대상서버등록**: 동기화대상 서버정보를 등록하고, 등록한 결과를 조회한다.
3. **동기화대상서버수정**: 기 등록된 동기화대상 서버정보를 수정한다.
4. **동기화대상서버삭제**: 기 등록된 동기화대상 서버정보를 삭제한다.
5. **동기화대상서버상세조회**: 동기화대상 서버목록에서 선택한 서버의 상세정보를 보여준다.
6. **동기화대상파일등록**: 동기화대상 파일을 등록한다.
7. **동기화대상파일삭제**: 동기화대상 파일을 삭제한다.
8. **파일동기화처리**: 업로드 파일들에 대하여 동기화 처리를 수행한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.ssy.web.EgovSynchrnServerController.java` | 동기화대상 서버관리를 위한 컨트롤러 클래스 |
| Service | `egovframework.com.utl.sys.ssy.service.EgovSynchrnServerService.java` | 동기화대상 서버관리를 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.utl.sys.ssy.service.impl.EgovSynchrnServerServiceImpl.java` | 동기화대상 서버관리를 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.utl.sys.ssy.service.impl.SynchrnServerDAO.java` | 동기화대상 서버관리를 위한 데이터처리 클래스 |
| Model | `egovframework.com.utl.sys.ssy.service.SynchrnServer.java` | 동기화대상 서버관리를 위한 Model 클래스 |
| VO | `egovframework.com.utl.sys.ssy.service.SynchrnServer.java` | 동기화대상 서버관리를 위한 VO 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/ssy/EgovSynchrnServerList.jsp` | 동기화대상서버 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/ssy/EgovSynchrnServerDetail.jsp` | 동기화대상서버 상세조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/ssy/EgovSynchrnServerRegist.jsp` | 동기화대상서버 등록 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/ssy/EgovSynchrnServerUpdt.jsp` | 동기화대상서버 수정 페이지 |
| XML | `/egovframework/sqlmap/com/utl/sys/ssy/EgovSynchrnServer_SQL_*.xml` | 동기화대상서버정보 QUERY XML |

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 동기화서버정보 | COMTNSYNCHRNSERVERINFO | 파일 동기화대상 AP서버 정보를 관리한다. |

### 관련설정

`globals.properties` 파일에 `Globals.SynchrnServerPath` 경로가 없을 경우 에러가 발생하므로, 반드시 해당 디렉토리를 생성해야 한다.

```properties
# 파일 동기화 컴포넌트에서 사용할 파일 업로드 경로
# (경로 설정은 반드시 절대경로를 사용해야 하며, 경로 뒤에 /를 붙여 주어야 함)
Globals.SynchrnServerPath = C:/egovframework/upload/Synch/
```

## 관련화면 및 수행매뉴얼

### 동기화대상서버 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/ssy/selectSynchrnServerList.do | selectSynchrnServerList | synchrnServerDAO.selectSynchrnServerList |
| 조회 | /utl/sys/ssy/selectSynchrnServerList.do | selectSynchrnServerList | synchrnServerDAO.selectSynchrnServerListTotCnt |

동기화대상서버 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다. 검색조건은 서버명에 대해서 수행된다.

### 동기화대상서버 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 저장 | /utl/sys/ssy/addSynchrnServer.do | insertSynchrnServer | synchrnServerDAO.insertSynchrnServer |

동기화대상서버의 속성정보를 입력한 뒤 등록한다. 서버ID는 등록 시 자동으로 부여된다.

### 동기화대상서버 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 저장 | /utl/sys/ssy/updtSynchrnServer.do | updateSynchrnServer | synchrnServerDAO.updateSynchrnServer |
| 삭제 | /utl/sys/ssy/removeSynchrnServer.do | deleteSynchrnServer | synchrnServerDAO.deleteSynchrnServer |

동기화대상서버의 속성정보를 변경한 후 저장하거나, 기 등록된 동기화대상서버를 삭제한다.

### 동기화대상서버 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/ssy/getSynchrnServer.do | selectSynchrnServer | synchrnServerDAO.selectSynchrnServer |

동기화대상서버의 속성정보를 조회한다. 동기화대상서버에 등록되어 있는 파일을
동기화대상 컴포넌트가 설치된 서버로 다운로드하거나 삭제할 수 있다.

### 동기화대상 처리

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 파일등록 | /utl/sys/ssy/uploadFile.do | uploadFile | |
| 파일삭제 | /utl/sys/ssy/deleteFile.do | deleteFile | |
| 동기화 | /utl/sys/ssy/processSynchrn.do | processSynchrn | synchrnServerDAO.processSynchrn |

기 등록된 동기화대상서버를 대상으로 동기화 대상파일에 대하여 동기화 처리를 수행한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
