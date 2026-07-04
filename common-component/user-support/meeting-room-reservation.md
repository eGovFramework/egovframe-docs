---
title: "회의실예약관리"
linkTitle: "회의실예약관리"
description: "회의실예약관리"
url: /common-component/user-support/information-provided/meeting-room-reservation/
menu:
  depth:
    name: "회의실예약관리"
    weight: 16
    parent: "information-provided"
---


# 개요

 회의실별 예약현황 및 관리하는 기능을 제공한다.

### 기능 설명

 회의실예약 목록 : 회의실예약 목록을 일간 시간 리스트로 보여준다.
 회의실예약 상세 : 회의실예약 상세 내용을 보여준다.
 회의실예약 등록 : 회의실예약 화면으로 이동한다.
 회의실예약 수정 : 회의실예약 수정 화면으로 이동한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.mtg.web.EgovMtgPlaceManageController.java | 회의실예약관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.uss.ion.mtg.service.EgovMtgPlaceManageService.java | 회의실예약관리를 위한  서비스 인터페이스 |
| ServiceImpl | egovframework.com.uss.ion.mtg.service.impl.EgovMtgPlaceManageServiceImpl.java | 회의실예약관리를 위한 서비스 구현 클래스 |
| DAO | egovframework.com.uss.ion.mtg.service.impl.MtgPlaceManageDAO.java | 회의실예약관리를 위한 데이터처리 클래스 |
| VO | egovframework.com.uss.ion.mtg.service.MtgPlaceResveVO.java | 회의실예약관리를 위한 VO 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/mtg/EgovMtgPlaceResveManageList.jsp | 회의실예약관리 목록조회를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/mtg/EgovMtgPlaceResveDetail.jsp | 회의실예약관리 상세화면을 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/mtg/EgovMtgPlaceResveRegist.jsp | 회의실예약관리 등록를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/mtg/EgovMtgPlaceResveUpdt.jsp | 회의실예약관리 수정를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/mtg/EgovMtgPlaceResveDplactCeck.jsp | 회의실예약관리 중복등록 확인을 위한 jsp페이지 |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_altibase.xml | 회의실예약관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_cubrid.xml | 회의실예약관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_maria.xml | 회의실예약관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_mysql.xml | 회의실예약관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_oracle.xml | 회의실예약관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_postgres.xml | 회의실예약관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_tibero.xml | 회의실예약관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/mtg/EgovMtgPlaceManage\_SQL\_goldilocks.xml | 회의실예약관리를 위한 Goldilocks용 Query XML |
| Message properties | resources/egovframework/message/com/uss/ion/mtg/message\_en.properties | 회의실예약관리를 위한 Message properties(영문) |
| Message properties | resources/egovframework/message/com/uss/ion/mtg/message\_ko.properties | 회의실예약관리를 위한 Message properties(한글) |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-MtgPlaceManage.xml | 회의실예약관리를 위한 Id생성 Idgen XML |

### 클래스 다이어그램

 ![image](./images/uss-mtgresve-cdd.png)

### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 RESVE_ID 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL, 
                               next_id DECIMAL(30) NOT NULL,
                               PRIMARY KEY (table_name)
    );
 
    INSERT INTO COMTECOPSEQ VALUES ('RESVE_ID','0');
```

### ID Generation 환경설정(context-idgn-MtgPlaceManage.xml)

```xml
<bean name="egovMtgPlaceResveIdGnrService" class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
        <property name="dataSource" ref="egov.dataSource" />
        <property name="strategy"   ref="mtgPlaceResveIdStrategy" />
        <property name="blockSize"  value="10"/>
        <property name="table"      value="COMTECOPSEQ"/>
        <property name="tableName"  value="RESVE_ID"/>
    </bean>
    <bean name="mtgPlaceResveIdStrategy" class="egovframework.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
        <property name="prefix"     value="RESVE_" />
        <property name="cipers"     value="14" />
        <property name="fillChar"   value="0" />
    </bean>
```


# 화면 설명

## 회의실예약현황 리스트

 회의실예약 목록을 리스트로 보여준다.

 ![image](./images/uss-mtgresve-reserve_list.png)

 회의일자 : 해당일자(년,월,일) 조회한다.
 등록 : 색이 없는 빈 시간을 클릭하면 회의실예약 화면으로 이동한다.
 상세 : 그래프 클릭하면 회의실예약 상세 화면으로 이동한다.

## 회의실예약 상세

 회의실예약 상세 내역을 볼 수 있다.

 ![image](./images/uss-mtgresve-reserve_detail.png)

 수정 : 회의실예약 정보를 수정할 수 있는 편집 가능한 화면으로 이동한다. 단, 자신이 등록한 회의실예약만 수정 가능하다.
 삭제 : 등록한 회의실예약을 삭제 한다. 단, 자신이 등록한 회의실예약만 삭제 가능하다.
 목록 : 회의실예약 목록 조회 화면으로 이동한다.

## 회의실예약 등록

 회의실예약 내용을 등록할 수 있는 기능을 제공한다.

 ![image](./images/uss-mtgresve-reserve_insert.png)

 저장 : 입력한 회의실예약 내용을 등록한다.
 목록 : 회의실예약 목록 조회 화면으로 이동한다.

 ![image](./images/uss-mtgresve-reserve_check.png)

 예약중복체크: 입력한 회의실예약 시간이 중복되었는지 확인하는 팝업이 뜬다.   확인 버튼을 눌러야만 중복 검사가 완료된다.

## 회의실예약 수정

 회의실예약 내용을 수정할 수 있는 기능을 제공한다.

 ![image](./images/uss-mtgresve-reserve_update.png)

 저장 : 입력한 회의실예약 내용을 수정한다.
 목록 : 회의실예약 목록 조회 화면으로 이동한다.


# 관련 기능

 해당 내용 없음


# 참고

 회의실관리

