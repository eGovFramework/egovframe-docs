---
title: "온라인POLL관리"
linkTitle: "온라인POLL관리"
description: "온라인POLL관리"
url: /common-component/user-support/online-participate/online-poll/
menu:
  depth:
    name: "온라인POLL관리"
    weight: 9
    parent: "online-participate"
---

# 온라인POLL관리

## 개요

온라인POLL관리는 온라인 POLL(찬반투표)의 등록·조회·수정·삭제와 항목 관리, 사용자 참여(응답) 처리, 결과 집계·조회 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(온라인참여) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.olp.opm.web.EgovOnlinePollManageController.java | EgovOnlinePollManageController Class |
| Controller | egovframework.com.uss.olp.opp.web.EgovOnlinePollPartcptnController.java | EgovOnlinePollPartcptnController Class |
| Controller | egovframework.com.uss.olp.opr.web.EgovOnlinePollResultController.java | EgovOnlinePollResultController Class |
| Service | egovframework.com.uss.olp.opm.service.EgovOnlinePollManageService.java | Service Interface |
| Service | egovframework.com.uss.olp.opp.service.EgovOnlinePollPartcptnService.java | Service Interface |
| Service | egovframework.com.uss.olp.opr.service.EgovOnlinePollResultService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.olp.opm.service.impl.EgovOnlinePollManageServiceImpl.java |  |
| ServiceImpl | egovframework.com.uss.olp.opp.service.impl.EgovOnlinePollPartcptnServiceImpl.java |  |
| ServiceImpl | egovframework.com.uss.olp.opr.service.impl.EgovOnlinePollResultServiceImpl.java |  |
| Class | egovframework.com.uss.olp.opm.service.OnlinePollItem.java |  |
| Class | egovframework.com.uss.olp.opm.service.OnlinePollManage.java |  |
| Class | egovframework.com.uss.olp.opp.service.OnlinePollPartcptn.java |  |
| Class | egovframework.com.uss.olp.opr.service.OnlinePollResult.java |  |
| DAO | egovframework.com.uss.olp.opm.service.impl.OnlinePollManageDao.java |  |
| DAO | egovframework.com.uss.olp.opp.service.impl.OnlinePollPartcptnDao.java |  |
| DAO | egovframework.com.uss.olp.opr.service.impl.OnlinePollResultDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opm/EgovOnlinePollItemList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opm/EgovOnlinePollManageDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opm/EgovOnlinePollManageList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opm/EgovOnlinePollManageRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opm/EgovOnlinePollManageUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opp/EgovOnlinePollPartcptnList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opp/EgovOnlinePollPartcptnMainList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opp/EgovOnlinePollPartcptnRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opp/EgovOnlinePollPartcptnStatistics.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/olp/opr/EgovOnlinePollResultList.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/olp/opm/EgovOnlinePollManage_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olp/opp/EgovOnlinePollPartcptn_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/olp/opr/EgovOnlinePollResult_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovOnlinePollManageService (관리))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectOnlinePollManageList(ComDefaultVO)` | `List<EgovMap>` | 목록을 조회한다 |
| `selectOnlinePollManageDetail(OnlinePollManage)` | `OnlinePollManage` | 온라인POLL관리를(을) 상세조회 한다. |
| `selectOnlinePollManageListCnt(ComDefaultVO)` | `int` | 온라인POLL관리를(을) 목록 전체 건수를(을) 조회한다. |
| `insertOnlinePollManage(OnlinePollManage)` | `void` | 온라인POLL관리를(을) 등록한다. |
| `updateOnlinePollManage(OnlinePollManage)` | `void` | 온라인POLL관리를(을) 수정한다. |
| `deleteOnlinePollManage(OnlinePollManage)` | `void` | 온라인POLL관리를(을) 삭제한다. |
| `selectOnlinePollManageStatistics(OnlinePollManage)` | `List<?>` | 온라인POLL관리를(을) 통계를 조회 한다. |
| `selectOnlinePollItemList(OnlinePollItem)` | `List<EgovMap>` | 온라인POLL항목를(을) 조회한다. |
| `insertOnlinePollItem(OnlinePollItem)` | `void` | 온라인POLL항목를(을) 등록한다. |
| `updateOnlinePollItem(OnlinePollItem)` | `void` | 온라인POLL항목를(을) 수정한다. |
| `deleteOnlinePollItem(OnlinePollItem)` | `void` | 온라인POLL항목를(을) 삭제한다. |

### 주요 메서드 (EgovOnlinePollPartcptnService (참여))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectOnlinePollManageList(ComDefaultVO)` | `List<EgovMap>` | 목록을 조회한다 |
| `selectOnlinePollManageListCnt(ComDefaultVO)` | `int` | 온라인POLL관리를(을) 목록 전체 건수를(을) 조회한다. |
| `selectOnlinePollManageDetail(OnlinePollPartcptn)` | `List<EgovMap>` | 온라인POLL관리를(을) 상세조회 한다. |
| `selectOnlinePollItemDetail(OnlinePollPartcptn)` | `List<EgovMap>` | 온라인POLL항목를(을) 상세조회 한다. |
| `insertOnlinePollResult(OnlinePollPartcptn)` | `void` | 온라인POLL참여를(을) 등록한다. |
| `selectOnlinePollManageStatistics(OnlinePollPartcptn)` | `List<EgovMap>` | 온라인POLL참여 통계를 조회한다. |
| `selectOnlinePollResult(OnlinePollPartcptn)` | `int` | 온라인POLL참여 여부를 조회한다. |

### 주요 메서드 (EgovOnlinePollResultService (결과))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectOnlinePollResultList(OnlinePollResult)` | `List<?>` | 목록을 조회한다 |
| `deleteOnlinePollResult(OnlinePollResult)` | `void` | 온라인POLL결과를(을) 삭제 한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
