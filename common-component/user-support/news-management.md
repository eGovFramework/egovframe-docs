---
title: "뉴스관리"
linkTitle: "뉴스관리"
description: "뉴스관리"
url: /common-component/user-support/information-provided/news-management/
menu:
  depth:
    name: "뉴스관리"
    weight: 1
    parent: "information-provided"
---


# 뉴스관리

## 개요

 새로운 소식이나 정보를 게시판 형태로 제공한다.

## 설명

### 패키지 참조 관계

 뉴스관리 패키지는 요소기술의 공통 패키지(cmm)에 대해서만 직접적인 함수적 참조 관계를 가진다.
- 패키지 간 참조 관계 : [사용자지원 Package Dependency](../intro/package-reference.md#사용자지원)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.nws.web.EgovNewsController.java | 뉴스관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.uss.ion.nws.service.EgovNewsService.java | 뉴스관리를 위한 서비스 인터페이스 |
| ServiceImpl | egovframework.com.uss.ion.nws.service.impl.EgovNewsServiceImpl.java | 뉴스관리를 위한 서비스 구현 클래스 |
| VO | egovframework.com.uss.ion.nws.service.NewsVO.java | 뉴스관리를 위한 VO 클래스 |
| DAO | egovframework.com.uss.ion.nws.service.impl.EgovNewsDAO.java | 뉴스 관리를 위한 데이터처리 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nws/EgovNewsList.jsp | 뉴스관리를 위한 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nws/EgovNewsDetail.jsp | 뉴스관리를 위한 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nws/EgovNewsRegist.jsp | 뉴스관리를 위한 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/nws/EgovNewsUpdt.jsp | 뉴스관리를 위한 수정 페이지 |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_altibase.xml | 뉴스관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_cubrid.xml | 뉴스관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_maria.xml | 뉴스관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_mysql.xml | 뉴스관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_oracle.xml | 뉴스관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_postgres.xml | 뉴스관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_tibero.xml | 뉴스관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/nws/EgovNews\_SQL\_goldilocks.xml | 뉴스관리를 위한 Goldilocks용 Query XML |
| Message properties | resources/egovframework/message/com/uss/ion/nws/message\_ko.properties | 뉴스관리를 위한 Message properties(한글) |
| Message properties | resources/egovframework/message/com/uss/ion/nws/message\_en.properties | 뉴스관리를 위한 Message properties(영문) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-NewsManage.xml | 뉴스 등록을 위한 Id생성 Idgen XML |

### 클래스다이어그램

 ![image](./images/uss-news-뉴스관리_클래스다이어그램.jpg)

### ID Generation

#### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 NEWS_ID 항목을 추가해야 한다.

```sql
  CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
  		   next_id DECIMAL(30) NOT NULL,
  		   PRIMARY KEY (table_name));
  INSERT INTO COMTECOPSEQ VALUES('NEWS_ID','0');
```

#### ID Generation 환경설정(context-idgn-NewsManage.xml)

```xml
	<bean name="egovNewsManageIdGnrService"
		class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrService"
		destroy-method="destroy">
		<property name="dataSource" ref="egov.dataSource" />
		<property name="strategy"   ref="newsManageStrategy" />
		<property name="blockSize" 	value="10"/>
		<property name="table"	   	value="COMTECOPSEQ"/>
		<property name="tableName"	value="NEWS_ID"/>
	</bean>
 
	<bean name="newsManageStrategy"
		class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
		<property name="prefix" value="NEWS_" />
		<property name="cipers" value="15" />
		<property name="fillChar" value="0" />
	</bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 뉴스정보 | COMTNNEWSINFO | 뉴스에 대한 제목, 설명을 관리한다. |

## 관련기능

 뉴스관리기능은 크게 뉴스정보목록조회, 뉴스정보상세조회, 뉴스정보등록, 뉴스정보수정 기능으로 구성되어 있다.

### 뉴스정보목록조회

#### 비즈니스 규칙

 조회조건으로 목록조회를 할 수 있고, 등록버튼을 클릭하여 뉴스정보등록 화면으로 이동하여 뉴스정보를 등록 처리 할 수 있다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 목록조회 | /uss/ion/nws/selectNewsList.do | selectNewsList | "NewsManage" | "selectNewsList" |
|  |  |  | "NewsManage" | "selectNewsListCnt" |

 뉴스정보 목록은 페이지 당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
 검색조건은 뉴스제목, 뉴스출처에 대해서 수행된다.
 페이지 당 검색 범위를 변경하고자 하는 경우
 context-properties.xml 파일의 pageUnit, pageSize를 변경한다.(단 해당 설정은 전체 공통서비스 기능에 영향을 미친다.)

 ![image](./images/uss-news-news_list.png)

 조회: 뉴스정보를 조회하기 위해서는 상단의 검색조건을 선택 후 해당하는 검색문자를 입력 후 조회 버튼을 클릭한다.
 등록: 뉴스정보를 등록하기 위해서는 상단의 등록 버튼을 통해서 뉴스정보등록 화면으로 이동한다.
 목록클릭: 뉴스정보상세조회 화면으로 이동한다.

### 뉴스정보상세조회

#### 비즈니스 규칙

 뉴스정보목록조회에서 목록 클릭 시 이동되는 화면으로 뉴스정보에 대한 상세정보를 보여준다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 상세조회 | /uss/ion/nws/selectNewsDetail.do | selectNewsDetail | "NewsManage" | "selectNewsDetail" |
| 삭제 | /uss/ion/nws/deleteNews.do | deleteNews | "NewsManage" | "deleteNews" |

 뉴스정보 상세조회화면은 뉴스정보수정, 뉴스정보삭제, 뉴스정보목록조회를 할 수 있다.

 ![image](./images/uss-news-news_detail.png)

 수정: 수정버튼 클릭 시 뉴스정보를 수정할 수 있는 화면으로 이동한다.
 삭제: 삭제버튼 클릭 시 삭제여부를 확인하는 메시지를 보여주고 삭제처리를 할 수 있다.
 목록: 뉴스정보목록조회 화면으로 이동한다.

### 뉴스정보등록

#### 비즈니스 규칙

 뉴스정보에 관한 기본정보를 입력 저장처리한다. 입력명 우측의 빨간* 표시는 반드시 입력해야할 항목을 표시한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 등록화면 | /uss/ion/nws/insertNewsView.do | insertNewsView |  |  |
| 등록 | /uss/ion/nws/insertNews.do | insertNews | "NewsManage" | "insertNews" |

 ![image](./images/uss-news-news_regist.png)

 파일첨부 시 파일선택 버튼을 클릭하여 파일을 첨부할 수 있다(최대 3개 가능 - 설정가능)

 ![image](./images/uss-news-atchfile2.gif)

 저장: 입력한 뉴스정보정보들이 저장 처리된다.
 목록: 뉴스정보목록조회 화면으로 이동한다.

### 뉴스정보수정

#### 비즈니스 규칙

 입력한 뉴스정보정보들을 저장 처리한다. 입력명 우측의 빨간* 표시는 수정 시 반드시 입력해야 할 항목을 표시한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 수정화면 | /uss/ion/nws/updateNewsView.do | updateNewsView | "NewsManage" | "selectNewsDetail" |
| 수정 | /uss/ion/nws/updateNews.do | updateNews | "NewsManage" | "updateNews" |

 ![image](./images/uss-news-news_updt.png)

 파일첨부 시 파일선택 버튼을 클릭하여 파일을 첨부할 수 있다(최대 3개 가능 - 설정가능)

 ![image](./images/uss-news-atchfile2.gif)

 수정: 수정 입력한 뉴스정보정보들이 저장 처리된다.
 목록: 뉴스정보목록조회 화면으로 이동한다.

