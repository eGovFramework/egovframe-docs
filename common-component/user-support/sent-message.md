---
title: "보낸쪽지함관리"
linkTitle: "보낸쪽지함관리"
description: "보낸쪽지함관리"
url: /common-component/user-support/information-provided/sent-message/
menu:
  depth:
    name: "보낸쪽지함관리"
    weight: 22
    parent: "information-provided"
---


# 보낸쪽지함관리

## 개요

 보낸쪽지함관리는 사용자가 보낸쪽지함 정보를 조회 및 관리 하고, 보낸쪽지 수신상태를 조회, 삭제 할 수 있는 기능을 제공한다.

## 설명

 보낸쪽지함관리는 보낸쪽지함관리는 목록조회, 상세조회, 수신상태조회, 삭제의 기능을 제공한다.

 ① 보낸쪽지함관리 목록 : 보낸쪽지함관리 정보를 최근 등록 순서대로 조회, 삭제 하고, 그 결과 목록을 화면에 반영한다.
 ② 보낸쪽지함관리 상세조회 : 등록된 보낸쪽지함관리 정보를 상세정보를 조회하고 삭제기능을 제공한다.
 ③ 수신상태 조회 : 보낸쪽지 수신상태 상세정보를 조회하고 삭제기능을 제공한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.nts.web.EgovNoteTrnsmitController.java | 보낸쪽지함관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.uss.ion.nts.service.EgovNoteTrnsmitService.java | 보낸쪽지함관리를 위한  서비스 인터페이스 |
| ServiceImpl | egovframework.com.uss.ion.nts.service.impl.EgovNoteTrnsmitServiceImpl.java | 보낸쪽지함관리를 위한 서비스 구현 클래스 |
| DAO | egovframework.com.uss.ion.nts.service.impl.NoteTrnsmitDao.java | 보낸쪽지함관리를 위한 데이터처리 클래스 |
| Model | egovframework.com.uss.ion.nts.service.NoteTrnsmit.java | 보낸쪽지함관리를 위한 Model 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nts/EgovNoteTrnsmitList.jsp | 보낸쪽지함관리 목록조회를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nts/EgovNoteTrnsmitDetail.jsp | 보낸쪽지함관리 상세조회를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nts/EgovNoteTrnsmitCnfirm.jsp | 수신상태 조회를 위한 jsp페이지 |
| Mapper | resources/egovframework/mapper/com/uss/ion/nts/EgovNoteTrnsmit\_SQL\_*.xml | 보낸쪽지함관리 QUERY XML |
| Idgnr | resources/egovframework/spring/com/idgn/context-idgn-NoteManage.xml | 보낸쪽지함관리를위한 Idgn |
| Properties | resources/egovframework/message/com/uss/ion/nts/message\_*.properties | 보낸쪽지함관리 국제화 |

 보낸쪽지함관리 QUERY XML의 경우 MySQL, Oracle, Cubrid, Altibase, Tibero, MariaDB, PostgreSQL, Goldilocks 지원하며, globals.properties에서 설정 가능
 국제화의 경우 한국어(ko)/영어(en) 2개국어 지원

### 클래스 다이어그램

 ![image](./images/uss-note-클래스다이어그램.jpg)

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 쪽지관리 | COMTNNOTE | 쪽지정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |
| 받은쪽지함관리 | COMTNNOTERECPTN | 받은쪽지함을 관리하기 위한 속성정보를 정의하고, 관리한다. |
| 보낸쪽지함관리 | COMTNNOTETRNSMIT | 보낸쪽지함을를 관리하기 위한 속성정보를 정의하고, 관리한다. |

### ID Generation

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 NOTE_ID, NOTE_TRNSMIT_ID, NOTE_RECPTN_ID 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('NOTE_ID',0);
INSERT INTO COMTECOPSEQ VALUES('NOTE_TRNSMIT_ID',0);
INSERT INTO COMTECOPSEQ VALUES('NOTE_RECPTN_ID',0);
```

## 관련화면 및 수행매뉴얼

### 보낸쪽지함관리 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 목록조회 | /uss/ion/nts/listNoteTrnsmit.do | EgovNoteTrnsmitList | "NoteTrnsmit.selectNoteTrnsmit" |
|  |  |  | "NoteTrnsmit.selectNoteTrnsmitCnt" |
|  |  |  | "NoteTrnsmit.deleteNoteTrnsmit" |
|  |  |  | "NoteTrnsmit.deleteNoteRecptn" |
|  |  |  | "NoteTrnsmit.deleteNoteManage" |
|  |  |  | "NoteTrnsmit.selectTrnsmitRelationCnt" |

 ![image](./images/uss-note-trnsmit-보낸쪽지함목록.jpg)

 조회 : 보낸날짜, 검색조건, 검색명으로 조회를 요청한다.
 삭제 : 선택된 보낸쪽지 정보를 삭제한다.
 목록 제목 클릭 :  보낸쪽지함관리 상세조회 화면으로 이동한다.
 목록 받는사람 클릭 :  수신상태 조회 화면으로 이동한다.
 목록 개봉/미개봉 클릭 :  수신상태 조회 화면으로 이동한다.

### 보낸쪽지함관리 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /uss/ion/nts/detailNoteTrnsmit.do | EgovNoteTrnsmitDetail | "NoteTrnsmit.selectNoteTrnsmitDetail" |
|  |  |  | "NoteTrnsmit.deleteNoteTrnsmit" |
|  |  |  | "NoteTrnsmit.deleteNoteRecptn" |
|  |  |  | "NoteTrnsmit.deleteNoteManage" |
|  |  |  | "NoteTrnsmit.selectTrnsmitRelationCnt" |

 ![image](./images/uss-note-trnsmit-보쪽함상조.jpg)

 삭제 : 선택된 보낸쪽지 정보를 삭제한다.
 목록 : 보낸쪽지함관리 목록조회 화면으로 이동한다.

### 수신상태 조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 목록조회 | /uss/ion/nts/selectNoteTrnsmitCnfirm.do | EgovNoteTrnsmitCnfirm | "NoteTrnsmit.selectNoteTrnsmitCnfirm" |
|  |  |  | "NoteTrnsmit.selectNoteTrnsmitCnt" |
|  |  |  | "NoteTrnsmit.deleteNoteTrnsmit" |
|  |  |  | "NoteTrnsmit.deleteNoteRecptn" |
|  |  |  | "NoteTrnsmit.deleteNoteManage" |
|  |  |  | "NoteTrnsmit.selectTrnsmitRelationCnt" |

 ![image](./images/uss-note-trnsmit-보쪽수목록.jpg)

 삭제 : 선택된 보낸쪽지 정보를 삭제한다.
 닫기 : 현재 팝업창을 닫는다.
