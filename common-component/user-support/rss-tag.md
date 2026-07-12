---
title: "RSS태그관리"
linkTitle: "RSS태그관리"
description: "RSS태그관리"
url: /common-component/user-support/information-provided/rss-tag/
menu:
  depth:
    name: "RSS태그관리"
    weight: 18
    parent: "information-provided"
---

# RSS태그관리

## 개요

RSS태그관리는 게시판 등 콘텐츠를 RSS로 제공하기 위한 RSS 태그 정보를 등록·조회·수정·삭제하고 RSS 피드를 생성하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.rss.web.EgovRssTagManageController.java | EgovRssTagManageController Class |
| Controller | egovframework.com.uss.ion.rsn.web.EgovRssController.java | EgovRssController Class |
| Service | egovframework.com.uss.ion.rss.service.EgovRssTagManageService.java | Service Interface |
| Service | egovframework.com.uss.ion.rsn.service.EgovRssService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.ion.rss.service.impl.EgovRssTagManageServiceImpl.java |  |
| ServiceImpl | egovframework.com.uss.ion.rsn.service.impl.EgovRssServiceImpl.java |  |
| Class | egovframework.com.uss.ion.rss.service.RssManage.java |  |
| Class | egovframework.com.uss.ion.rsn.service.RssInfo.java |  |
| DAO | egovframework.com.uss.ion.rss.service.impl.RssTagManageDao.java |  |
| DAO | egovframework.com.uss.ion.rsn.service.impl.RssDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rss/EgovRssTagManageDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rss/EgovRssTagManageList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rss/EgovRssTagManageRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rss/EgovRssTagManageTableColumnList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rss/EgovRssTagManageUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsn/EgovRssTagService.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/rsn/EgovRssTagServiceList.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/ion/rss/EgovRssTagManage_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/ion/rsn/EgovRssTagService_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovRssTagManageService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectRssTagManageTableList()` | `List<?>` | 목록을 조회한다 |
| `selectRssTagManageTableColumnList(Map<?, ?>)` | `List<?>` | JDBC 테이블 컬럼 목록을 조회한다. |
| `selectRssTagManageList(RssManage)` | `List<?>` | RSS태그관리 목록을 조회한다. |
| `selectRssTagManageListCnt(RssManage)` | `int` | RSS태그관리를(을) 목록 전체 건수를(을) 조회한다. |
| `selectRssTagManageDetail(RssManage)` | `RssManage` | RSS태그관리를(을) 상세조회 한다. |
| `insertRssTagManage(RssManage)` | `void` | RSS태그관리를(을) 등록한다. |
| `updateRssTagManage(RssManage)` | `void` | RSS태그관리를(을) 수정한다. |
| `deleteRssTagManage(RssManage)` | `void` | RSS태그관리를(을) 삭제한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
