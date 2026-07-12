---
title: "주간/월간보고관리"
linkTitle: "주간/월간보고관리"
description: "주간/월간보고관리"
url: /common-component/collaboration/schedule-manage/weekly-monthly-report/
menu:
  depth:
    name: "주간/월간보고관리"
    weight: 7
    parent: "schedule-manage"
---

# 주간/월간보고관리

## 개요

주간/월간보고관리는 주간·월간 단위의 업무 보고를 등록·조회·수정·삭제하고, 보고에 대한 승인 처리를 지원하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 협업(일정관리) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.smt.wmr.web.EgovWikMnthngReprtController.java | 주간/월간보고 Controller Class |
| Service | egovframework.com.cop.smt.wmr.service.EgovWikMnthngReprtService.java | 주간/월간보고 Service Interface |
| ServiceImpl | egovframework.com.cop.smt.wmr.service.impl.EgovWikMnthngReprtServiceImpl.java | 주간/월간보고 ServiceImpl Class |
| VO | egovframework.com.cop.smt.wmr.service.WikMnthngReprt.java / WikMnthngReprtVO.java | 주간/월간보고 VO Class |
| VO | egovframework.com.cop.smt.wmr.service.Reportr.java / ReportrVO.java | 보고자 VO Class |
| DAO | egovframework.com.cop.smt.wmr.service.impl.WikMnthngReprtDAO.java | 주간/월간보고 DAO Class |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/wmr/EgovWikMnthngReprtList.jsp | 주간/월간보고 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/wmr/EgovWikMnthngReprtRegist.jsp | 주간/월간보고 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/wmr/EgovWikMnthngReprtUpdt.jsp | 주간/월간보고 수정 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/wmr/EgovWikMnthngReprtDetail.jsp | 주간/월간보고 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/wmr/EgovReportrList.jsp, EgovReportrListPopup.jsp | 보고자 목록/선택 팝업 페이지 |
| Query XML | resources/egovframework/mapper/com/cop/smt/wmr/EgovWikMnthngReprt_SQL_*.xml | DB별(altibase·cubrid·goldilocks·maria·mysql·oracle·postgres·tibero) Query XML |
| Message properties | resources/egovframework/message/com/cop/smt/wmr/message_ko.properties, message_en.properties | 주간/월간보고 메시지 리소스 |

### 주요 메서드 (EgovWikMnthngReprtService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectWikMnthngReprtList(WikMnthngReprtVO)` | `Map<String, Object>` | 주간월간보고 목록을 조회한다 |
| `selectWikMnthngReprt(WikMnthngReprtVO)` | `WikMnthngReprtVO` | 주간월간보고 정보를 조회한다 |
| `insertWikMnthngReprt(WikMnthngReprt)` | `void` | 주간월간보고 정보를 등록한다 |
| `updateWikMnthngReprt(WikMnthngReprt)` | `void` | 주간월간보고 정보를 수정한다 |
| `confirmWikMnthngReprt(WikMnthngReprt)` | `void` | 주간월간보고 정보를 승인한다 |
| `deleteWikMnthngReprt(WikMnthngReprt)` | `void` | 주간월간보고 정보를 삭제한다 |
| `selectReportrList(ReportrVO)` | `Map<String, Object>` | 보고자 목록을 조회한다 |
| `selectWrterClsfNm(String)` | `String` | 사용자 직위명 정보를 조회한다 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
