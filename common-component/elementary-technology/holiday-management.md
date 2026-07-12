---
title: "공휴일관리(달력)"
linkTitle: "공휴일관리(달력)"
description: "공휴일관리(달력)"
url: /common-component/elementary-technology/calendar/holiday-management/
menu:
  depth:
    name: "공휴일관리(달력)"
    weight: 1
    parent: "calendar"
---

<!-- markdownlint-disable MD013 -->

## 개요

공휴일관리(휴일관리)는 휴일의 등록, 수정, 삭제, 목록조회, 상세조회 기능을 제공한다.
등록된 휴일 정보는 일반달력·행정달력 팝업 및 일간/주간/월간/연간 달력 화면에 반영된다.

## 설명

휴일의 관리는 목록조회, 상세조회, 등록, 수정, 삭제 처리를 할 수 있도록 구성되어 있다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.sym.cal.web.EgovCalRestdeManageController.java` | 달력, 휴일관리를 위한 컨트롤러 클래스 |
| Service | `egovframework.com.sym.cal.service.EgovCalRestdeManageService.java` | 달력, 휴일관리를 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.sym.cal.service.impl.EgovCalRestdeManageServiceImpl.java` | 달력, 휴일관리를 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.sym.cal.service.impl.RestdeManageDAO.java` | 휴일 정보 관리를 위한 데이터처리 클래스 |
| Model | `egovframework.com.sym.cal.service.Restde.java` | 휴일 정보 Model 클래스 |
| VO | `egovframework.com.sym.cal.service.RestdeVO.java` | 달력, 휴일관리를 위한 VO 클래스 |
| JS | `/js/egovframework/cmm/sym/cal/EgovCalPopup.js` | 일반달력·행정달력 팝업 호출 JavaScript |
| JSP | `/WEB-INF/jsp/egovframework/cmm/sym/cal/EgovRestdeList.jsp` 외 | 휴일 목록/등록/수정/상세 및 일반·행정달력(팝업/일간/주간/월간/연간) JSP 페이지 일체 |

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 휴일 | COMTNRESTDE | 휴일 정보를 관리 |

### ID Generation (`context-idgen.xml`)

```xml
<bean name="egovRestDeIdGnrService"
    class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrService"
    destroy-method="destroy">
    <property name="dataSource" ref="dataSource" />
    <property name="blockSize" value="10"/>
    <property name="table" value="COMTECOPSEQ"/>
    <property name="tableName" value="RESTDE_ID"/>
</bean>
```

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 `RESTDE_ID` 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('RESTDE_ID','0');
```

## 관련화면 및 수행매뉴얼

### 휴일 관리

| 기능 | URL | Controller method | 화면(URL) |
| --- | --- | --- | --- |
| 목록조회 | /sym/cal/EgovRestdeList.do | selectRestdeList | /cmm/sym/cal/EgovRestdeList |
| 등록 | /sym/cal/EgovRestdeRegist.do | insertRestde | /cmm/sym/cal/EgovRestdeRegist |
| 수정 | /sym/cal/EgovRestdeModify.do | updateRestde | /cmm/sym/cal/EgovRestdeModify |
| 상세조회 | /sym/cal/EgovRestdeDetail.do | selectRestdeDetail | /cmm/sym/cal/EgovRestdeDetail |
| 삭제 | /sym/cal/EgovRestdeRemove.do | deleteRestde | /cmm/sym/cal/EgovRestdeDetail |

휴일 목록은 페이지당 10건씩 조회되며 검색조건은 휴일일자·휴일명에 대해 수행된다.

### 달력 팝업 사용

일반달력·행정달력 팝업 호출을 위하여 `EgovCalPopup.js`를 해당 페이지에 등록한다.

```html
<script type="text/javascript" src="<c:url value='/js/egovframework/cmm/sym/cal/EgovCalPopup.js' />"></script>

<form name="Form1" action="<c:url value='/sym/cmm/EgovNormalCalPopup.do'/>" method="post">
    <input type="hidden" name="sDate" value="" size="8" readonly
        onClick="javascript:fn_egov_NormalCalendar(document.Form1, document.Form1.sDate, document.Form1.vDate);" />
    <input type="text" name="vDate" value="" size="10" readonly
        onClick="javascript:fn_egov_NormalCalendar(document.Form1, document.Form1.sDate, document.Form1.vDate);" />
</form>
```

`sDate`는 연월일 8자리를, `vDate`는 `-`를 포함한 날짜를 받는다. 행정달력은 `fn_egov_AdministCalendar`를 사용한다.

### 달력 조회

| 기능 | URL (일반달력) | URL (행정달력) |
| --- | --- | --- |
| 일간조회 | /sym/cal/EgovNormalDayCalendar.do | /sym/cal/EgovAdministDayCalendar.do |
| 주간조회 | /sym/cal/EgovNormalWeekCalendar.do | /sym/cal/EgovAdministWeekCalendar.do |
| 월간조회 | /sym/cal/EgovNormalMonthCalendar.do | /sym/cal/EgovAdministMonthCalendar.do |
| 연간조회 | /sym/cal/EgovNormalYearCalendar.do | /sym/cal/EgovAdministYearCalendar.do |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
