---
title: "최근검색어조회"
linkTitle: "최근검색어조회"
description: "최근검색어조회"
url: /common-component/user-support/information-provided/recent-keyword/
menu:
  depth:
    name: "최근검색어조회"
    weight: 10
    parent: "information-provided"
---

# 최근검색어조회

## 개요

최근검색어조회는 사용자가 입력한 검색어를 기록하고 최근 검색어 목록을 조회·관리하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.rsm.web.AjaxXmlView.java | AjaxXmlView Class |
| Controller | egovframework.com.uss.ion.rsm.web.EgovRecentSrchwrdController.java | EgovRecentSrchwrdController Class |
| Service | egovframework.com.uss.ion.rsm.service.EgovRecentSrchwrdService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.ion.rsm.service.impl.EgovRecentSrchwrdServiceImpl.java |  |
| Class | egovframework.com.uss.ion.rsm.service.RecentSrchwrd.java |  |
| DAO | egovframework.com.uss.ion.rsm.service.impl.RecentSrchwrdDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsm/EgovRecentSrchwrdDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsm/EgovRecentSrchwrdList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsm/EgovRecentSrchwrdRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsm/EgovRecentSrchwrdResultList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsm/EgovRecentSrchwrdUpdt.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/ion/rsm/EgovRecentSrchwrd_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovRecentSrchwrdService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectRecentSrchwrdList(RecentSrchwrd)` | `List<EgovMap>` | 목록을 조회한다 |
| `selectRecentSrchwrdListCnt(RecentSrchwrd)` | `int` | 최근검색어관리를(을) 목록 전체 건수를(을) 조회한다. |
| `selectRecentSrchwrdDetail(RecentSrchwrd)` | `RecentSrchwrd` | 최근검색어관리를(을) 상세조회 한다. |
| `insertRecentSrchwrd(RecentSrchwrd)` | `void` | 최근검색어관리를(을) 등록한다. |
| `updateRecentSrchwrd(RecentSrchwrd)` | `void` | 최근검색어관리를(을) 수정한다. |
| `deleteRecentSrchwrd(RecentSrchwrd)` | `void` | 최근검색어관리를(을) 삭제한다. |
| `selectRecentSrchwrdResultInquire(RecentSrchwrd)` | `List<EgovMap>` | 최근검색어결과 목록을 조회한다. |
| `selectRecentSrchwrdResultList(RecentSrchwrd)` | `List<?>` | 최근검색어결과 목록을 조회한다. |
| `selectRecentSrchwrdResultListCnt(RecentSrchwrd)` | `int` | 최근검색어결과를(을) 목록 전체 건수를(을) 조회한다. |
| `insertRecentSrchwrdResult(RecentSrchwrd)` | `void` | 최근검색어결과를(을) 등록한다. |
| `deleteRecentSrchwrdResult(RecentSrchwrd)` | `void` | 최근검색어결과를(을) 건별로 삭제 한다. |
| `deleteRecentSrchwrdResultAll(RecentSrchwrd)` | `void` | 최근검색어결과를(을) 관리별로 삭제 한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
