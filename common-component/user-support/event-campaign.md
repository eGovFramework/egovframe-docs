---
title: "행사/이벤트/캠페인"
linkTitle: "행사/이벤트/캠페인"
description: "행사/이벤트/캠페인"
url: /common-component/user-support/information-provided/event-campaign/
menu:
  depth:
    name: "행사/이벤트/캠페인"
    weight: 5
    parent: "information-provided"
---

# 행사/이벤트/캠페인

## 개요

행사/이벤트/캠페인은 조직에서 진행하는 행사·이벤트·캠페인 정보를 등록·조회·수정·삭제하고, 외부 인사 정보를 함께 관리하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.ecc.web.EgovEventCmpgnController.java | EgovEventCmpgnController Class |
| Service | egovframework.com.uss.ion.ecc.service.EgovEventCmpgnService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.ion.ecc.service.impl.EgovEventCmpgnServiceImpl.java |  |
| VO | egovframework.com.uss.ion.ecc.service.EventCmpgnVO.java |  |
| VO | egovframework.com.uss.ion.ecc.service.TnextrlHrVO.java |  |
| DAO | egovframework.com.uss.ion.ecc.service.impl.EgovEventCmpgnDAO.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovEventCmpgnDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovEventCmpgnList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovEventCmpgnListPopup.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovEventCmpgnRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovEventCmpgnUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovTnextrlHrDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovTnextrlHrList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovTnextrlHrRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/ecc/EgovTnextrlHrUpdt.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/ion/ecc/EgovEventCmpgn_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovEventCmpgnService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectEventCmpgnList(EventCmpgnVO)` | `List<EventCmpgnVO>` | 행사/이벤트/캠페인 목록을 조회한다 |
| `selectEventCmpgnListCnt(EventCmpgnVO)` | `int` | 행사/이벤트/캠페인 목록 총건수를 조회한다 |
| `insertEventCmpgn(EventCmpgnVO)` | `void` | 행사/이벤트/캠페인 정보를 등록한다 |
| `updateEventCmpgn(EventCmpgnVO)` | `void` | 행사/이벤트/캠페인 정보를 수정한다 |
| `deleteEventCmpgn(EventCmpgnVO)` | `void` | 행사/이벤트/캠페인 정보를 삭제한다 |
| `selectTnextrlHrList(TnextrlHrVO)` | `List<TnextrlHrVO>` | 외부 인사 목록을 조회한다 |
| `selectTnextrlHrListCnt(TnextrlHrVO)` | `int` | 외부 인사 목록 총건수를 조회한다 |
| `insertTnextrlHr(TnextrlHrVO)` | `void` | 외부 인사 정보를 등록한다 |
| `updateTnextrlHr(TnextrlHrVO)` | `void` | 외부 인사 정보를 수정한다 |
| `deleteTnextrlHr(TnextrlHrVO)` | `void` | 외부 인사 정보를 삭제한다 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
