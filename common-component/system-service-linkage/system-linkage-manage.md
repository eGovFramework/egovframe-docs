---
title: "시스템연계관리"
linkTitle: "시스템연계관리"
description: "시스템연계관리"
url: /common-component/system-service-linkage/system-linkage-manage/
menu:
  depth:
    weight: 1
    parent: "system-service-linkage"
    identifier: "system-linkage-manage"
---


# 시스템연계관리

## 개요

 시스템의 연계에 관한 정보를 등록하고 관리하는 기능을 수행한다.
 기능흐름

 ![image](./images/ssi-system-cntc-function-flow.png)

## 설명

### 패키지 참조 관계

 시스템연계관리 패키지는 요소기술의 공통(cmm) 패키지에만 직접적인 함수적 참조 관계를 가진다. 하지만, 컴포넌트 배포 시 오류 없이 실행되기 위하여 패키지 간의 참조관계에 따라 연계기관관리, 연계메시지관리, 연계현황관리, 달력 패키지와 함께 배포 파일을 구성한다.
 패키지 간 참조 관계 : [시스템관리 Package Dependency](../intro/package-reference.md#시스템관리)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.ssi.syi.sim.web.EgovSystemCntcController.java | 시스템연계 관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.ssi.syi.sim.service.EgovSystemCntcService.java | 시스템연계 관리를 위한 서비스 인터페이스 |
| ServiceImpl | egovframework.com.ssi.syi.sim.service.impl.EgovSystemCntcServiceImpl.java | 시스템연계 관리를 위한  서비스구현 클래스 |
| Model | egovframework.com.ssi.syi.sim.service.SystemCntc.java | 시스템연계 정보 Model 클래스 |
| VO | egovframework.com.ssi.syi.sim.service.SystemCntcVO.java | 시스템연계 관리를 위한 VO 클래스 |
| DAO | egovframework.com.ssi.syi.sim.service.impl.SystemCntcDAO.java | 시스템연계 정보 관리를 위한 데이터처리 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/ssi/syi/sim/EgovSystemCntcList.jsp | 시스템연계 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/ssi/syi/sim/EgovSystemCntcRegist.jsp | 시스템연계 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/ssi/syi/sim/EgovSystemCntcUpdt.jsp | 시스템연계 수정 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/ssi/syi/sim/EgovSystemCntcDetail.jsp | 시스템연계 상세조회 페이지 |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_altibase.xml | 시스템연계 관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_cubrid.xml | 시스템연계 관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_maria.xml | 시스템연계 관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_mysql.xml | 시스템연계 관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_oracle.xml | 시스템연계 관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_postgres.xml | 시스템연계 관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_tibero.xml | 시스템연계 관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/ssi/syi/sim/EgovSystemCntc\_SQL\_goldilocks.xml | 시스템연계 관리를 위한 Goldilocks용 Query XML |
| Message properties | resources/egovframework/message/com/ssi/syi/sim/message\_en.properties | 시스템연계 관리를 위한 Message properties(영문) |
| Message properties | resources/egovframework/message/com/ssi/syi/sim/message\_ko.properties | 시스템연계 관리를 위한 Message properties(한글) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-SystemCntc.xml | 시스템연계 관리 Id생성 Idgen XML |

### 클래스 다이어그램

 ![image](./images/ssi-system-cntc-cdd.png)

### ID Generation

#### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 CNTC_ID 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
                               next_id DECIMAL(30) NOT NULL,
                               PRIMARY KEY (table_name)
    );
 
    INSERT INTO COMTECOPSEQ VALUES ('CNTC_ID','0');
```

#### ID Generation 환경설정(context-idgn-SystemCntc.xml)

```xml
<bean name="egovSystemCntcIdGnrService" class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
        <property name="dataSource" ref="egov.dataSource" />
        <property name="strategy"   ref="egovSystemCntcIdMsgtrategy" />
        <property name="blockSize"  value="10" />
        <property name="table"      value="COMTECOPSEQ" />
        <property name="tableName"  value="CNTC_ID" />
    </bean>
    <bean name="egovSystemCntcIdMsgtrategy" class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
        <property name="prefix"     value="CNTC" />
        <property name="cipers"     value="4" />
        <property name="fillChar"   value="0" />
    </bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 시스템연계 | COMTNSYSTEMCNTC | 시스템연계에 대한 정보 |

## 관련기능

 시스템연계 관리는 시스템연계 정보를 등록하여 시스템의 연계현황을 확인할 수 있도록 하기위하여  시스템연계 등록, 수정, 목록조회, 상세조회의 기능으로 구성되어 있다.

### 시스템연계 목록조회

#### 비즈니스 규칙

 시스템연계 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
 검색조건은 시스템연계명에 대해서 수행된다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 목록조회 | /ssi/syi/sim/getSystemCntcList.do | selectSystemCntcList | "SystemCntcDAO.selectSystemCntcList" |

 페이지당 검색 범위를 변경하고자 하는 경우
 context-properties.xml 파일의 pageUnit, pageSize를 변경한다.(단 해당 설정은 전체 공통서비스 기능에 영향을 미친다.)

 ![image](./images/ssi-system-cntc-list.png)

 조회: 조회하기 위해서는 상단의 검색조건을 선택 후 해당하는 검색문자를 입력 후 조회 버튼을 클릭한다.
 등록: 등록하기 위해서는 상단의 등록 버튼을 통해서 시스템연계 등록 화면으로 이동한다.
 목록클릭: 시스템연계 상세조회 화면으로 이동한다.

### 시스템연계 등록

#### 비즈니스 규칙

 시스템연계에 대한 상세내용을 등록한다.
 등록이 성공하면 시스템연계목록 화면으로 이동한다.
 시스템연계 등록 시 선행작업으로 연계기관, 연계시스템, 연계서비스, 연계메시지, 연계메시지항목이 등록되어 있어야 한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /ssi/syi/sim/addSystemCntc.do | insertSystemCntc | "SystemCntcDAO.insertSystemCntc" |

 ![image](./images/ssi-system-cntc-insert.png)

 저장: 입력한 시스템연계 정보들이 저장 처리된다.
 목록: 시스템연계 목록 화면으로 이동한다.

### 시스템연계 수정

#### 비즈니스 규칙

 수정이 성공하면 시스템연계목록 화면으로 이동한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /ssi/syi/sim/updateSystemCntc.do | updateSystemCntc | "SystemCntcDAO.updateSystemCntc" |

 ![image](./images/ssi-system-cntc-update.png)

 저장: 수정된 정보들이 저장 처리된다.
 목록: 시스템연계 목록 화면으로 이동한다.

### 시스템연계 상세 조회

#### 비즈니스 규칙

 상세조회에는 삭제 처리가 포함되어 있고 삭제가 성공하면 시스템연계목록 화면으로 이동한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /ssi/syi/sim/getSystemCntcDetail.do | selectSystemCntcDetail | "SystemCntcDAO.selectSystemCntcDetail" |
| 삭제 | /ssi/syi/sim/removeSystemCntc.do | deleteSystemCntc | "SystemCntcDAO.deleteSystemCntc" |

 ![image](./images/ssi-system-cntc-detail.png)

 수정: 수정버튼 클릭 시 시스템연계 수정 화면으로 이동한다.
 삭제: 삭제버튼 클릭 시 삭제여부를 확인하는 메시지를 보여주고 삭제처리를 할 수 있다.
 목록: 시스템연계 목록 화면으로 이동한다.

## 참고자료

 공통컴포넌트 참조 : 연계기관, 연계시스템, 연계서비스 및 연계메시지, 연계메시지항목
 실행환경 참조 : [ID Generation Service](/egovframe-runtime/foundation-layer/id-generation.md)
