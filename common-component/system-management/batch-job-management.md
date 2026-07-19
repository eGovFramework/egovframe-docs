---
title: "배치작업관리"
linkTitle: "배치작업관리"
description: "배치작업관리"
url: /common-component/system-management/batch-manage/batch-job-management/
menu:
  depth:
    name: "배치작업관리"
    weight: 1
    parent: "batch-manage"
---


# 배치작업관리

## 개요

 배치작업관리는 시스템에서 주기적으로 실행하는 배치작업을 등록하는 기능을 제공한다.

## 설명

 배치작업관리는 배치작업을 등록하기 위한 목적으로 배치작업의 등록, 수정, 삭제, 조회, 목록조회의 기능을 수반한다.

 ① 배치작업목록조회 : 배치작업으로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
 ② 배치작업등록 : 배치작업정보를 등록하고, 등록 결과를 조회한다.
 ③ 배치작업수정 : 기 등록된 배치작업정보의 항목들을 수정한다.
 ④ 배치작업삭제 : 기 등록된 배치작업정보를 삭제한다.
 ⑤ 배치작업조회 : 등록된 배치작업정보를 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.sym.bat.web.EgovBatchOpertController.java | 배치작업 관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.sym.bat.service.EgovBatchOpertService.java | 배치작업 관리를 위한  서비스 인터페이스 |
| ServiceImpl | egovframework.com.sym.bat.service.impl.EgovBatchOpertServiceImpl.java | 배치작업 관리를 위한 서비스 구현 클래스 |
| DAO | egovframework.com.sym.bat.service.impl.BatchOpertDao.java | 배치작업 관리를 위한 데이터처리 클래스 |
| Model | egovframework.com.sym.bat.service.BatchOpert.java | 배치작업 관리를 위한 Model 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/bat/EgovBatchOpertList.jsp | 배치작업 목록조회를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/bat/EgovBatchOpertRegist.jsp | 배치작업 등록을 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/bat/EgovBatchOpertUpdt.jsp | 배치작업 수정을 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/bat/EgovBatchOpertDetail.jsp | 등록된 배치작업을 조회하기 위한 jsp페이지 |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_mysql.xml | 배치작업관리 MySQL용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_oracle.xml | 배치작업관리 Oracle용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_tibero.xml | 배치작업관리 Tibero용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_altibase.xml | 배치작업관리 Altibase용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_cubrid.xml | 배치작업관리 Cubrid용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_maria.xml | 배치작업관리 Maria용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_postgres.xml | 배치작업관리 Postgres용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/bat/EgovBatchOpert\_SQL\_goldilocks.xml | 배치작업관리 Goldilocks용 QUERY XML |
| Message properties | resources/egovframework/message/com/message-common\_ko.properties | 배치작업관리 Message properties |
| Message properties | resources/egovframework/message/com/sym/bat/message\_ko.properties | 배치작업관리를 위한 Message properties(한글) |
| Message properties | resources/egovframework/message/com/sym/bat/message\_en.properties | 배치작업관리를 위한 Message properties(영문) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-BatchOpert.xml | 배치작업관리를 위한 Id생성 Idgen XML |

### 클래스 다이어그램

 ![image](./images/sym-batchjob-batchopert_class.png)

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 배치작업 | COMTNBATCHOPERT | 배치작업정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |

### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 BATCH_OPERT_ID 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
                               next_id DECIMAL(30) NOT NULL,
                               PRIMARY KEY (table_name)
    );
 
    INSERT INTO COMTECOPSEQ VALUES ('BATCH_OPERT_ID','0');
```

### ID Generation 환경설정(context-idgn-BatchOpert.xml)

```xml
<bean name="egovBatchOpertIdGnrService" class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
        <property name="dataSource" ref="egov.dataSource" />
        <property name="strategy"   ref="batchOpertIdStrategy" />
        <property name="blockSize"  value="10"/>
        <property name="table"      value="COMTECOPSEQ"/>
        <property name="tableName"  value="BATCH_OPERT_ID"/>
    </bean>
    <bean name="batchOpertIdStrategy" class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
        <property name="prefix"   value="BAT" />
        <property name="cipers"   value="17" />
        <property name="fillChar" value="0" />
    </bean>
```

## 관련화면 및 수행매뉴얼

### 배치작업 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /sym/bat/selectBatchOpertList.do | selectBatchOpertList | "BatchOpertDAO.selectBatchOpertList" |
| 조회 | /sym/bat/selectBatchOpertList.do | selectBatchOpertList | "BatchOpertDAO.selectBatchOpertListCnt" |

 배치작업 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
 검색조건은 배치작업명,배치프로그램에 대해서 수행된다.

 ![image](./images/sym-batchjob-batchopert_list.png)

 조회 : 기 등록된 배치작업의 목록을 조회한다.
 등록 : 신규 배치작업을 등록하기 위해서는 상단의 등록 버튼을 통해서 배치작업 등록 화면으로 이동한다.

### 배치작업 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /sym/bat/addBatchOpert.do | insertBatchOpert | "BatchOpertDAO.insertBatchOpert" |

 배치작업의 속성정보를 입력한 뒤 등록한다.

 ![image](./images/sym-batchjob-batchopert_regist.png)

 저장 : 신규 배치작업을 등록하기 위해서는 배치작업 속성을 입력한 뒤 상단의 저장 버튼을 통해서 배치작업을 등록한다. 배치프로그램은 서버의 경로명을 포함하여 존재하는 실행파일명이어야 한다.
 목록 : 배치작업 목록조회 화면으로 이동한다.

### 배치작업 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /sym/bat/updateBatchOpert | updateBatchOpert | "BatchOpertDAO.updateBatchOpert" |

 배치작업의 속성정보를 변경한 후 저장한다.

 ![image](./images/sym-batchjob-batchopert_update.png)

 저장 : 기 등록된 배치작업 속성을 수정한 뒤 상단의 저장 버튼을 통해서 배치작업정보를 수정한다.
 목록 : 배치작업 목록조회 화면으로 이동한다.

### 배치작업 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /sym/bat/getBatchOpert.do | selectBatchOpert | "BatchOpertDAO.selectBatchOpert" |
| 삭제 | /sym/bat/deleteBatchOpert.do | deleteBatchOpert | "BatchOpertDAO.deleteBatchOpert" |

 배치작업의 속성정보를 조회한다.

 ![image](./images/sym-batchjob-batchopert_detail.png)

 수정 : 기 등록된 배치작업 속성을 수정한 뒤 상단의 수정 버튼을 통해서 배치작업수정화면으로 이동한다.
 삭제 : 기 등록된 배치작업정보를 삭제한다.
 목록 : 배치작업 목록조회 화면으로 이동한다.
