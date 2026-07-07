---
title: "부서일정관리"
linkTitle: "부서일정관리"
description: "부서일정관리"
url: /common-component/collaboration/schedule-manage/department-schedule/
menu:
  depth:
    name: "부서일정관리"
    weight: 1
    parent: "schedule-manage"
---


# 부서일정관리

## 개요

부서원들의 /세미나/강의/교육/회의/기타 일정에 대한 계획을 쉽고 편하게 관리 할 수 있는 서비스로 월별일정보기, 주간별일정보기, 일별일정보기 기능을 제공한다.

## 설명

### 패키지 참조 관계

부서일정관리 패키지는 요소기술의 공통(cmm) 패키지에 대해서만 직접적인 함수적 참조 관계를 가진다. 하지만, 컴포넌트 배포 시 오류 없이 실행되기 위하여 패키지 간의 참조관계에 따라 개인일정관리, 일지관리, 전체일정 패키지와 함께 배포 파일을 구성한다.

- 패키지 간 참조 관계 : [협업-일정관리, 문자메시지, 주소록 외 Package Dependency](../intro/package-reference.md/#협업)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.smt.sdm.web.EgovDeptSchdulManageController.java | 부서일정관리 Controller Class |
| Service | egovframework.com.cop.smt.sdm.service.EgovDeptSchdulManageService.java | 부서일정관리 Service Class |
| ServiceImpl | egovframework.com.cop.smt.sdm.service.impl.EgovDeptSchdulManageServiceImpl.java | 부서일정관리 ServiceImpl Class |
| VO | egovframework.com.cop.smt.sdm.service.DeptSchdulManageVO.java | 부서일정관리 VO Class |
| VO | egovframework.com.cmm.ComDefaultVO.java | 검색 VO Class |
| DAO | egovframework.com.cop.smt.sdm.service.impl.DeptSchdulManageDao.java | 부서일정관리 Dao Class |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageMainList.jsp | 부서일정관리 조회 메인페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageList.jsp | 부서일정관리 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageDailyList.jsp | 부서일정관리(일별) 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageWeekList.jsp | 부서일정관리(주간별) 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageMonthList.jsp | 부서일정관리(월별) 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageRegist.jsp | 부서일정관리 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageModify.jsp | 부서일정관리 수정 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageDetail.jsp | 부서일정관리 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageAuthorGroupPopup.jsp | 부서 검색 팝업 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageEmpLyrPopup.jsp | 사용자 검색 팝업 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/sdm/EgovDeptSchdulManageListPopup.jsp | 일정관리 팝업 페이지 |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_altibase.xml | 부서일정관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_cubrid.xml | 부서일정관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_maria.xml | 부서일정관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_mysql.xml | 부서일정관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_oracle.xml | 부서일정관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_postgres.xml | 부서일정관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_tibero.xml | 부서일정관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/cop/smt/sdm/EgovDeptSchdulManage_SQL_goldilocks.xml | 부서일정관리를 위한 Goldilocks용 Query XML |
| Validator XML | resources/egovframework/validator/com/cop/smt/sdm/EgovDeptSchdulManage.xml | 부서일정관리 Validator XML |
| Message properties | resources/egovframework/message/com/cop/smt/sdm/message_ko.properties | 마이페이지 Message properties(한글) |
| Message properties | resources/egovframework/message/com/cop/smt/sdm/message_en.properties | 마이페이지 Message properties(영문) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgen-deptSchdulManage.xml | 부서일정관리 Id생성 Idgen XML |

### 클래스 다이어그램

![클래스 다이어그램](./images/department-schedule-class-diagram.png)

### ID Generation

#### ID Generation 관련 DDL 및 DML

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 SCHDUL_ID 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ (TABLE_NAME VARCHAR(20) NOT NULL, 
  		                    NEXT_ID NUMERIC(30) NULL,
  		                    PRIMARY KEY (TABLE_NAME));
 
INSERT INTO COMTECOPSEQ VALUES('SCHDUL_ID','1');
```

#### ID Generation 환경설정(context-idgen-deptSchdulManage.xml)

```xml
<bean name="deptSchdulManageIdGnrService" class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
    <property name="dataSource" ref="egov.dataSource" />
    <property name="strategy"   ref="DeptSchdulManageStrategy" />
    <property name="blockSize"  value="10"/>
    <property name="table"      value="COMTECOPSEQ"/>
    <property name="tableName"  value="SCHDUL_ID"/>
</bean>
<bean name="DeptSchdulManageStrategy" class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
    <property name="prefix"   value="SCHDUL_" />
    <property name="cipers"   value="13" />
    <property name="fillChar" value="0" />
</bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 부서일정관리관리 | COMTNMTGINFO | 부서일정관리를 관리 한다. |

## 관련기능

부서일정관리관리기능은 부서일정관리 월별목록, 부서일정관리 주간별목록, 부서일정관리 일별목록, 부서일정관리 상세조회, 부서일정관리 등록, 부서일정관리 수정 기능으로 구성되어 있다.

### 부서일정관리 월별목록

#### 비즈니스 규칙

관리자가 기(記) 등록된 부서일정관리 정보를 리스트 형태로 조회 할 수 있고, 등록버튼을 클릭하여 등록화면으로 이동할 수 있다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 월별목록조회 | /cop/smt/sdm/EgovDeptSchdulManageMonthList.do | egovDeptSchdulManageMonthList | “DeptSchdulManage” | “selectDeptSchdulManageRetrieve” |

![부서일정관리 월별목록](./images/department-schedule-month-list.jpg)

일정구분 클릭 : 선택한 일정구분으로 이동 한다.

일자클릭 : 일자를 클릭하면 해당 일자의 부서일정관리 등록 화면으로 이동한다.

일정클릭 : 부서일정관리 상세조회 화면으로 이동한다.

### 부서일정관리 주간별목록

#### 비즈니스 규칙

관리자가 기(記) 등록된 부서일정관리 정보를 리스트 형태로 조회 할 수 있고, 등록버튼을 클릭하여 등록화면으로 이동할 수 있다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 주간별 목록조회 | /cop/smt/sdm/EgovDeptSchdulManageWeekList.do | egovDeptSchdulManageWeekList | “DeptSchdulManage” | “selectDeptSchdulManageRetrieve” |

![부서일정관리 주간별목록](./images/department-schedule-week-list.jpg)

일정클릭 : 부서일정관리 상세조회 화면으로 이동한다.

### 부서일정관리 일별목록

#### 비즈니스 규칙

관리자가 기(記) 등록된 부서일정관리 정보를 리스트 형태로 조회 할 수 있고, 등록버튼을 클릭하여 등록화면으로 이동할 수 있다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 일별 목록조회 | /cop/smt/sdm/EgovDeptSchdulManageDailyList.do | egovDeptSchdulManageDailyList | “DeptSchdulManage” | “selectDeptSchdulManageRetrieve” |

![부서일정관리 일별목록](./images/department-schedule-daily-list.jpg)

일정클릭 : 부서일정관리 상세조회 화면으로 이동한다.

### 부서일정관리 상세조회 및 삭제

#### 비즈니스 규칙

부서일정관리 목록에서 목록 클릭 시 이동되는 화면으로 부서일정관리에 대한 상세정보를 보여준다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 상세조회 | /cop/smt/sdm/EgovDeptSchdulManageDetail.do | egovDeptSchdulManageDetail | “DeptSchdulManage” | “selectDeptSchdulManageDetailVO” |
| 부서일정 삭제 | /cop/smt/sdm/EgovDeptSchdulManageDetail.do | egovDeptSchdulManageDetail | “DeptSchdulManage” | “deleteDeptSchdulManage” |

![부서일정관리 상세조회 및 삭제](./images/department-schedule-detail.jpg)

수정 : 수정버튼 클릭 시 부서일정관리 수정 화면으로 이동한다.

삭제 : 삭제버튼 클릭 시 삭제처리를 할 수 있다.

일지관리 : 일지관리 클릭 시 일지관리를 할 수 있는 목록으로 이동한다.

목록 : 부서일정관리 목록 화면으로 이동한다.

### 부서일정관리 등록

#### 비즈니스 규칙

부서일정관리에 관한 기본정보를 입력 저장처리한다. 입력명 우측의 빨간* 표시는 반드시 입력해야할 항목을 표시한다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 등록화면 | /cop/smt/sdm/EgovDeptSchdulManageRegist.do | deptSchdulManageRegist | | |
| 등록 | /cop/smt/sdm/EgovDeptSchdulManageRegistActor.do | deptSchdulManageRegistActor | “DeptSchdulManage” | “insertDeptSchdulManage” |

![부서일정관리 등록](./images/department-schedule-regist.jpg)

등록 : 입력한 부서일정관리 정보들이 저장 처리된다.

목록 : 부서일정관리 목록 화면으로 이동한다.

### 부서일정관리 수정

#### 비즈니스 규칙

입력한 부서일정관리 정보를(을) 저장 처리한다. 입력명 우측의 빨간* 표시는 수정 시 반드시 입력해야 할 항목을 표시한다.

#### 관련코드

N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 수정화면 | /cop/smt/sdm/EgovDeptSchdulManageModify.do | deptSchdulManageModify | | |
| 수정 | /cop/smt/sdm/EgovDeptSchdulManageModifyActor.do | deptSchdulManageModifyActor | “DeptSchdulManage” | “updateDeptSchdulManage” |

![부서일정관리 수정](./images/department-schedule-modify.jpg)

저장 : 수정된 정보들이 저장 처리된다.

목록 : 부서일정관리 목록 화면으로 이동한다.