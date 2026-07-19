---
title: "지식전문가관리"
linkTitle: "지식전문가관리"
description: "지식전문가관리"
url: /common-component/digital-asset-management/knowledge-expert-manage/
menu:
  depth:
    weight: 3
    parent: "digital-asset-management"
    identifier: "knowledge-expert-manage"
---


# 지식전문가관리

## 개요

 지식전문가관리는 해당지식의 전문가를 선정하고 등록 관리 할 수 있는 기능을 제공한다.

## 설명

 지식전문가관리는 해당지식의 전문가를 선정하고 등록 관리 하기 위한 목적으로 지식전문가의 등록, 수정, 삭제, 상세조회, 목록조회의 기능을 수반한다.

 ① 지식전문가목록조회 : 지식전문가 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
 ② 지식전문가등록 : 지식전문가 정보를 등록하고, 등록 결과를 조회한다.
 ③ 지식전문가수정 : 기 등록된 지식전문가정보의 항목들을 수정한다.
 ④ 지식전문가삭제 : 기 등록된 지식전문가정보를 삭제한다.
 ⑤ 지식전문가상세조회 : 등록된 지식전문가정보를 상세 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.dam.spe.spe.web.EgovKnoSpecialistController.java | 지식전문가 관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.dam.spe.spe.service.EgovKnoSpecialistService.java | 지식전문가 관리를 위한  서비스 인터페이스 |
| ServiceImpl | egovframework.com.dam.spe.spe.service.impl.EgovKnoSpecialistServiceImpl.java | 지식전문가 관리를 위한 서비스 구현 클래스 |
| DAO | egovframework.com.dam.spe.spe.service.impl.KnoSpecialistDAO.java | 지식전문가 관리를 위한 데이터처리 클래스 |
| Model | egovframework.com.dam.spe.spe.service.KnoSpecialist.java | 지식전문가 관리를 위한 Model 클래스 |
| VO | egovframework.com.dam.spe.spe.service.KnoSpecialistVO.java | 지식전문가 관리를 위한 VO 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/spe/EgovComDamSpecialistList.jsp | 지식전문가 목록조회를 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/spe/EgovComDamSpecialistRegist.jsp | 지식전문가 등록을 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/spe/EgovComDamSpecialistModify.jsp | 지식전문가 수정을 위한 jsp페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/spe/EgovComDamSpecialistDetail.jsp | 등록된 지식전문가를 조회하기 위한 jsp페이지 |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_altibase.xml | 지식전문가 관리를 위한 Altibase용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_cubrid.xml | 지식전문가 관리를 위한 Cubrid용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_maria.xml | 지식전문가 관리를 위한 MariaDB용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_mysql.xml | 지식전문가 관리를 위한 MySQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_oracle.xml | 지식전문가 관리를 위한 Oracle용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_postgres.xml | 지식전문가 관리를 위한 PostgreSQL용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_tibero.xml | 지식전문가 관리를 위한 Tibero용 Query XML |
| Query XML | resources/egovframework/mapper/com/dam/spe/spe/EgovDamKnoSpecialistList\_SQL\_goldilocks.xml | 지식전문가 관리를 위한 Goldilocks용 Query XML |
| Message properties | resources/egovframework/message/com/dam/spe/spe/message\_en.properties | 지식전문가  관리를 위한 Message properties(영문) |
| Message properties | resources/egovframework/message/com/dam/spe/spe/message\_ko.properties | 지식전문가 관리를 위한 Message properties(한글) |

### 클래스 다이어그램

 ![image](./images/dam-specialist-specialist_class.png)

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 지식전문가 | COMTNDAMPRO | 지식전문가정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |

## 관련화면 및 수행매뉴얼

### 지식전문가 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /dam/spe/spe/EgovComDamSpecialistList.do | selectKnoSpecialistList | "KnoSpecialistDAO.selectKnoSpecialistList" |
| 상세조회 | /dam/spe/spe/EgovComDamSpecialist.do | selectKnoSpecialist | "KnoSpecialistDAO.selectKnoSpecialist" |

 지식전문가관리 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
 검색조건은 전문가성명, 지식유형명에 대해서 수행된다.

 ![image](./images/dam-specialist-list.png)

 조회 : 기 등록된 지식전문가의 목록을 조회한다.
 등록 : 신규 지식전문가를 등록하기 위해서는 상단의 등록 버튼을 통해서 지식전문가관리 등록 화면으로 이동한다.
 상세조회 : 목록중 전문가성명을 클릭하여 지식전문가 상세조회 화면으로 이동한다.

### 지식전문가 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /dam/spe/spe/EgovComDamSpecialistRegist.do | insertKnoSpecialist | "KnoSpecialistDAO.insertKnoSpecialist" |

 지식전문가의 속성정보를 입력한 뒤 등록한다.

 ![image](./images/dam-specialist-insert.png)

 저장 : 신규 지식전문가를 등록하기 위해서는 지식전문가 속성을 입력한 뒤 하단의 저장 버튼을 통해서 지식전문가를 등록한다.
 목록 : 지식전문가 목록조회 화면으로 이동한다.

### 지식전문가 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /dam/spe/spe/EgovComDamSpecialistModify.do | updateKnoSpecialist | "KnoSpecialistDAO.updateKnoSpecialist" |

 지식전문가의 속성정보를 변경한 후 저장한다.

 ![image](./images/dam-specialist-update.png)

 저장 : 기 등록된 지식전문가 속성을 수정한 뒤 하단의 저장 버튼을 통해서 지식전문가정보를 수정한다.
 목록 : 지식전문가 목록조회 화면으로 이동한다.

### 지식전문가 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /dam/spe/spe/EgovComDamSpecialist.do | selectKnoSpecialist | "KnoSpecialistDAO.selectKnoSpecialist" |
| 삭제 | /dam/spe/spe/EgovComDamSpecialistRemove.do | deleteKnoSpecialist | "KnoSpecialistDAO.deleteKnoSpecialist" |

 지식전문가의 속성정보를 조회한다.

 ![image](./images/dam-specialist-detail.png)

 수정 : 기 등록된 지식전문가 속성을 수정한 뒤 하단의 수정 버튼을 통해서 지식전문가관리수정화면으로 이동한다.
 삭제 : 기 등록된 지식전문가정보를 삭제한다.
 목록 : 지식전문가관리 목록조회 화면으로 이동한다.
