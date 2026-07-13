---
title: "Wiki기능"
linkTitle: "Wiki기능"
description: "Wiki기능"
url: /common-component/user-support/information-provided/wiki/
menu:
  depth:
    name: "Wiki기능"
    weight: 17
    parent: "information-provided"
---

# Wiki기능

## 개요

Wiki기능은 외부 위키 서비스 페이지를 북마크로 등록·조회·수정·삭제해 연동하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.wik.bmk.web.EgovWikiBookmarkController.java | EgovWikiBookmarkController Class |
| Service | egovframework.com.uss.ion.wik.bmk.service.EgovWikiBookmarkService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.ion.wik.bmk.service.impl.EgovWikiBookmarkServiceImpl.java |  |
| Class | egovframework.com.uss.ion.wik.bmk.service.WikiBookmark.java |  |
| DAO | egovframework.com.uss.ion.wik.bmk.service.impl.WikiBookmarkDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/wik/bmk/EgovWikiBookmarkList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/wik/bmk/EgovWikiBookmarkRegist.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/ion/wik/bmk/EgovWikiBookmark_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovWikiBookmarkService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectWikiBookmarkList(WikiBookmark)` | `List<?>` | 목록을 조회한다 |
| `selectWikiBookmarkListCnt(WikiBookmark)` | `int` | 위키북마크를(을) 목록 전체 건수를(을) 조회한다. |
| `selectWikiBookmarkDuplicationCnt(WikiBookmark)` | `int` | 위키북마크를(을) 중복을 조회한다. |
| `insertWikiBookmark(WikiBookmark)` | `void` | 위키북마크를(을) 등록한다. |
| `deleteWikiBookmark(WikiBookmark)` | `void` | 위키북마크를(을) 삭제한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
