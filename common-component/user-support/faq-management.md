---
title: "FAQ관리"
linkTitle: "FAQ관리"
description: "FAQ관리"
url: /common-component/user-support/online-help/faq-management/
menu:
  depth:
    name: "FAQ관리"
    weight: 3
    parent: "online-help"
---

# FAQ관리

## 개요
시스템 또는 서비스 이용 시 많은 사람들이 빈번히 하는 질문들에 대해 별도로 관리하여 이에 관한 응답을 쉽게 찾아볼 수 있도록 구성되어 있다

## 설명

### 패키지 참조 관계
FAQ관리 패키지는 요소기술의 공통 패키지(cmm)에 대해서만 직접적인 함수적 참조 관계를 가진다. 

- 패키지 간 참조 관계 : [사용자지원 Package Dependency](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v2:init_pkg_dependency#사용자지원)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.olh.faq.web.EgovFaqController.java | FAQ관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.uss.olh.faq.service.EgovFaqService.java | FAQ관리를 위한 서비스 인터페이스 |
| ServiceImpl | egovframework.com.uss.olh.faq.service.impl.EgovFaqServiceImpl.java | FAQ관리를 위한 서비스 구현 클래스 |
| VO | egovframework.com.uss.olh.faq.service.FaqVO.java | FAQ관리를 위한 VO 클래스 |
| VO | egovframework.com.uss.olh.faq.service.FaqDefaultVO.java | FAQ관리를 위한 SearchVO 클래스 |
| DAO | egovframework.com.uss.olh.faq.service.imp.EgovFaqDAO.java | FAQ관리를 위한 데이터처리 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/faq/EgovFaqList.jsp | FAQ관리를 위한 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/faq/EgovFaqDetail.jsp | FAQ관리를 위한 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/faq/EgovFaqRegist.jsp | FAQ관리를 위한 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olh/faq/EgovFaqUpdt.jsp | FAQ관리를 위한 수정 페이지 |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_altibase.xml | FAQ관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_cubrid.xml | FAQ관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_maria.xml | FAQ관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_mysql.xml | FAQ관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_oracle.xml | FAQ관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_postgres.xml | FAQ관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_tibero.xml | FAQ관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olh/faq/EgovFaqManage_SQL_goldilocks.xml | FAQ관리를 위한 Goldilocks용 Query XML |
| Validator XML | resources/egovframework/validator/com/uss/olh/faq/EgovFaqRegist.xml | FAQ관리를 위한 Validator XML |
| Message properties | resources/egovframework/message/com/uss/olh/faq/message_ko.properties | FAQ관리를 위한 Message properties(Korean) |
| Message properties | resources/egovframework/message/com/uss/olh/faq/message_en.properties | FAQ관리를 위한 Message properties(English) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-FaqManage.xml | FAQ등록을 위한 Id생성 Idgen XML |

### 클래스다이어그램
![클래스다이어그램](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?w=740&media=egovframework:com:v2:uss:faq%EA%B4%80%EB%A6%AC_%ED%81%B4%EB%9E%98%EC%8A%A4%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.jpg)

### ID Generation

#### ID Generation 관련 DDL 및 DML
- ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 **FAQ_ID** 항목을 추가해야 한다. 

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
           next_id DECIMAL(30) NOT NULL,
           PRIMARY KEY (table_name));
 
INSERT INTO COMTECOPSEQ VALUES('FAQ_ID','0');
```

#### ID Generation 환경설정(context-idgn-FaqManage.xml)
```xml
<bean name="egovFaqManageIdGnrService"
    class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrService"
    destroy-method="destroy">
    <property name="dataSource" ref="egov.dataSource" />
    <property name="strategy"   ref="faqManageStrategy" />
    <property name="blockSize"  value="10"/>
    <property name="table"      value="COMTECOPSEQ"/>
    <property name="tableName"  value="FAQ_ID"/>
</bean>

<bean name="faqManageStrategy"
    class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
    <property name="prefix" value="FAQ_" />
    <property name="cipers" value="16" />
    <property name="fillChar" value="0" />
</bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| FAQ정보 | COMTNFAQINFO | 서비스 이용 시 빈번히 하는 질문 및 이에 대한 답변 관리한다. |

## 관련기능
FAQ관리기능은 크게 **FAQ목록조회**, **FAQ상세조회**, **FAQ내용등록**, **FAQ내용수정** 기능으로 구성되어 있다.

### FAQ 목록조회

#### 비즈니스 규칙
조회조건으로 목록조회를 할 수 있고, 등록버튼을 클릭하여 FAQ등록 화면으로 이동하여 FAQ를 등록 처리 할 수 있다.

#### 관련코드
N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 목록조회 | /uss/ion/faq/selectFaqList.do | selectFaqList | "FaqManage" | "selectFaqList" |
| | | | "FaqManage" | "selectFaqListCnt" |

FAQ 목록은 페이지 당 10건씩 조회되며 페이징은 10페이지씩 이루어진다. 
검색조건은 용어명, 영문명에 대해서 수행된다.
페이지 당 검색 범위를 변경하고자 하는 경우 
context-properties.xml 파일의 pageUnit, pageSize를 변경한다.(단 해당 설정은 전체 공통서비스 기능에 영향을 미친다.)

![FAQ 목록조회](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3.6:uss:olh:faq:faq_list.png)

조회: FAQ를 조회하기 위해서는 상단의 검색조건을 선택 후 해당하는 검색문자를 입력 후 조회 버튼을 클릭한다.
등록: FAQ를 등록하기 위해서는 상단의 등록 버튼을 통해서 **FAQ등록** 화면으로 이동한다. 
목록클릭: **FAQ상세조회** 화면으로 이동한다.

### FAQ상세조회

#### 비즈니스 규칙
FAQ목록조회에서 목록 클릭 시 이동되는 화면으로 FAQ에 대한 상세정보를 보여준다.

#### 관련코드
N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 상세조회 | /uss/ion/faq/selectFaqDetail.do | selectFaqDetail | "FaqManage" | "selectFaqDetail" |
| 삭제 | /uss/olh/faq/deleteFaq.do | deleteFaq | "FaqManage" | "deleteFaq" |

FAQ 상세조회화면은 FAQ내용수정, FAQ내용삭제, FAQ목록조회를 할 수 있다.

![FAQ 상세조회](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3.6:uss:olh:faq:faq_detail.png)

수정: 수정버튼 클릭 시 FAQ를 수정할 수 있는 화면으로 이동한다. 
삭제: 삭제버튼 클릭 시 삭제여부를 확인하는 메세지를 보여주고 삭제처리를 할 수 있다. 
목록: **FAQ목록조회** 화면으로 이동한다.

### FAQ내용등록

#### 비즈니스 규칙
FAQ에 관한 기본정보를 입력 저장처리한다. 입력명 우측의 빨간* 표시는 반드시 입력해야할 항목을 표시한다. 

#### 관련코드
N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 등록화면 | /uss/ion/faq/insertFaqView.do | insertFaqView | | |
| 등록 | /uss/olh/faq/insertFaq.do | insertFaq | "FaqManage" | "insertFaq" |

![FAQ 등록](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3.6:uss:olh:faq:faq_regist.png)

파일첨부 시 찾아보기를 클릭하여 파일을 첨부할 수 있다(최대 3개 가능 - 설정가능)

![파일첨부](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:uss:olh:faq:atchfile2.gif)

목록: **FAQ목록조회** 화면으로 이동한다. 
저장: 입력한 FAQ정보들이 저장 처리된다. 

### FAQ내용수정

#### 비즈니스 규칙
입력한 FAQ정보들을 저장 처리한다. 입력명 우측의 빨간* 표시는 수정 시 반드시 입력해야 할 항목을 표시한다. 

#### 관련코드
N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | SQL Namespace | SQL QueryID |
| --- | --- | --- | --- | --- |
| 수정화면 | /uss/ion/faq/updateFaqView.do | updateFaqView | "FaqManage" | "selectFaqDetail" |
| 수정 | /uss/olh/faq/updateFaq.do | updateFaq | "FaqManage" | "updateFaq" |

![FAQ 수정](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3.6:uss:olh:faq:faq_updt.png)

파일첨부 시 찾아보기를 클릭하여 파일을 첨부할 수 있다(최대 3개 가능 - 설정가능)

![파일첨부](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:uss:olh:faq:atchfile2.gif)

수정: 수정 입력한 FAQ정보들이 저장 처리된다. 
목록: **FAQ목록조회** 화면으로 이동한다. 

