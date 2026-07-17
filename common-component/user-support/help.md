---
title: "도움말"
linkTitle: "도움말"
description: "도움말"
url: /common-component/user-support/online-help/help/
menu:
  depth:
    name: "도움말"
    weight: 1
    parent: "online-help"
---


# 도움말

## 개요

 응용 프로그램의 기능사용에 관한 설명이나 지시 사항을 제공하고 응용 프로그램 사용에 필요한 정보 제공 및 도움을 주는 기능을 제공한다.

## 설명

### 패키지 참조 관계

 도움말 패키지는 요소기술의 공통 패키지(cmm)에 대해서만 직접적인 함수적 참조 관계를 가진다.
 패키지 간 참조 관계 : [사용자지원 Package Dependency](../intro/package-reference.md#사용자지원)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.olh.hpc.web.EgovHpcmController.java | 도움말관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.uss.olh.hpc.service.EgovHpcmService.java | 도움말관리를 위한 서비스 인터페이스 |
| ServiceImpl | egovframework.com.uss.olh.hpc.service.impl.EgovHpcmServiceImpl.java | 도움말관리를 위한 서비스 구현 클래스 |
| VO | egovframework.com.uss.olh.hpc.service.HpcmVO.java | 도움말관리를 위한 VO 클래스 |
| VO | egovframework.com.uss.olh.hpc.service.HpcmDefaultVO.java | 도움말관리를 위한 SearchVO 클래스 |
| DAO | egovframework.com.uss.olh.hpc.service.impl.EgovHpcmDAO.java | 도움말 관리를 위한 데이터처리 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/hpc/EgovHpcmList.jsp | 도움말관리를 위한 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/hpc/EgovHpcmDetail.jsp | 도움말관리를 위한 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/hpc/EgovHpcmRegist.jsp | 도움말관리를 위한 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/hpc/EgovHpcmUpdt.jsp | 도움말관리를 위한 수정 페이지 |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_altibase.xml | 도움말관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_cubrid.xml | 도움말관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_maria.xml | 도움말관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_mysql.xml | 도움말관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_oracle.xml | 도움말관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_postgres.xml | 도움말관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_tibero.xml | 도움말관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/hpc/EgovHpcm\_SQL\_goldilocks.xml | 도움말관리를 위한 Goldilocks용 Query XML |
| Message properties | resources/egovframework/message/com/uss/olh/hpc/message\_ko.properties | 도움말관리를 위한 Message properties(한글) |
| Message properties | resources/egovframework/message/com/uss/olh/hpc/message\_en.properties | 도움말관리를 위한 Message properties(영문) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-HpcmManage.xml | 도움말등록을 위한 Id생성 Idgen XML |

### 클래스다이어그램

 ![image](./images/uss-help-도움말_클래스다이어그램.jpg)

### ID Generation

#### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 HPCM_ID 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
  		   next_id DECIMAL(30) NOT NULL,
  		   PRIMARY KEY (table_name));
 
  INSERT INTO COMTECOPSEQ VALUES('HPCM_ID,'0');
```

#### ID Generation 환경설정(context-idgn-HpcmManage.xml)

```xml
<bean name="egovHpcmManageIdGnrService"
		class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrService"
		destroy-method="destroy">
		<property name="dataSource" ref="egov.dataSource" />
		<property name="strategy"   ref="hpcmManageStrategy" />
		<property name="blockSize" 	value="10"/>
		<property name="table"	   	value="COMTECOPSEQ"/>
		<property name="tableName"	value="HPCM_ID"/>
	</bean>
 
	<bean name="hpcmManageStrategy"
		class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
		<property name="prefix" value="HPCM_" />
		<property name="cipers" value="15" />
		<property name="fillChar" value="0" />
	</bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 도움말정보 | COMTNHPCMINFO | 사이트 내에 기능사용에 대한 기능설명이나  절차설명 관리한다. |

## 관련기능

 도움말관리기능은 크게 도움말목록조회, 도움말상세조회, 도움말등록, 도움말수정 기능으로 구성되어 있다.

### 도움말목록조회

#### 비즈니스 규칙

 일반사용자가 아닌 관리자가 사용하는 화면으로 조회조건으로 목록조회를 할 수 있고, 등록버튼을 클릭하여 도움말등록 화면으로 이동하여 도움말을 등록 처리 할 수 있다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 목록조회 | /uss/olh/hpc/selectHpcmList.do | selectHpcmList | "Hpcm" | "selectHpcmList" |
|  |  |  | "Hpcm" | "selectHpcmListCnt" |

 도움말 목록은 페이지 당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
 검색조건은 용어명, 영문명에 대해서 수행된다.
 페이지 당 검색 범위를 변경하고자 하는 경우
 context-properties.xml 파일의 pageUnit, pageSize를 변경한다.(단 해당 설정은 전체 공통서비스 기능에 영향을 미친다.)

 ![image](./images/uss-help-hpcm_list.png)

 조회: 도움말을 조회하기 위해서는 상단의 검색조건을 선택 후 해당하는 검색문자를 입력 후 조회 버튼을 클릭한다.
 등록: 도움말을 등록하기 위해서는 상단의 등록 버튼을 통해서 도움말등록 화면으로 이동한다.
 목록클릭: 도움말상세조회 화면으로 이동한다.

### 도움말상세조회

#### 비즈니스 규칙

 일반사용자가 아닌 관리자가 사용하는 화면으로 도움말목록조회에서 목록 클릭 시 이동되는 화면으로 도움말에 대한 상세정보를 보여준다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 상세조회 | /uss/olh/hpc/selectHpcmDetail.do | selectHpcmDetail | "Hpcm" | "selectHpcmDetail" |
| 삭제 | /uss/olh/hpc/deleteHpcm.do | deleteHpcm | "Hpcm" | "deleteHpcm" |

 도움말 상세조회화면은 도움말수정, 도움말삭제, 도움말목록조회를 할 수 있다.

 ![image](./images/uss-help-hpcm_detail.png)

 수정: 수정버튼 클릭 시 도움말을 수정할 수 있는 화면으로 이동한다.
 삭제: 삭제버튼 클릭 시 삭제여부를 확인하는 메시지를 보여주고 삭제처리를 할 수 있다.
 목록: 도움말목록조회 화면으로 이동한다.

### 도움말등록

#### 비즈니스 규칙

 새로운 도움말을 입력 처리한다. 입력명 우측의 빨간* 표시는 반드시 입력해야할 항목을 표시한다.

#### 관련코드

 도움말관리에서 사용되는 코드 및 그에 따른 설정 값의 반영사항은 다음과 같다.

| 코드분류 | 코드분류명 | 코드ID | 코드명 |
| --- | --- | --- | --- |
| COM021 | 도움말구분 | 1 | 기능설명 |
| COM021 | 도움말구분 | 2 | 절차설명 |

 도움말구분코드를 추가하여 사용 할 수 있다.

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 등록화면 | /uss/olh/hpc/insertHpcmView.do | insertHpcmView |  |  |
| 등록 | /uss/olh/hpc/insertHpcm.do | insertHpcm | "Hpcm" | "insertHpcm" |

 도움말에 관한 기본정보를 입력 저장처리한다.

 ![image](./images/uss-help-hpcm_regist.png)

 목록: 도움말목록조회 화면으로 이동한다.
 저장: 입력한 도움말정보들이 저장 처리된다.

### 도움말수정

#### 비즈니스 규칙

 입력한 도움말정보들을 저장 처리한다.
 입력명 우측의 빨간* 표시는 수정 시 반드시 입력해야 할 항목을 표시한다.

#### 관련코드

 도움말관리에서 사용되는 코드 및 그에 따른 설정 값의 반영사항은 다음과 같다.

| 코드분류 | 코드분류명 | 코드ID | 코드명 |
| --- | --- | --- | --- |
| COM021 | 도움말구분 | 1 | 기능설명 |
| COM021 | 도움말구분 | 2 | 절차설명 |

 도움말구분코드를 추가하여 사용 할 수 있다.

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 수정화면 | /uss/olh/hpc/updateHpcmView.do | updateHpcmView | "Hpcm" | "selectHpcmDetail" |
| 수정 | /uss/olh/hpc/updateHpcm.do | updateHpcm | "Hpcm" | "updateHpcm" |

 ![image](./images/uss-help-hpcm_updt.png)

 수정: 수정 입력한 도움말정보들이 저장 처리된다.
 목록: 도움말목록조회 화면으로 이동한다.
