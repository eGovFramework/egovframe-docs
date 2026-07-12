---
title: "사이트맵"
linkTitle: "사이트맵"
description: "사이트맵"
url: /common-component/user-support/information-provided/sitemap/
menu:
  depth:
    name: "사이트맵"
    weight: 3
    parent: "information-provided"
---

# 사이트맵

## 개요

사이트맵은 메뉴 정보를 기반으로 사이트맵 정보를 생성·조회하는 기능이다. 소스는 시스템관리 메뉴관리(`egovframework.com.sym.mnu.stm`) 패키지에 위치하며, 메뉴생성관리의 사이트맵 생성 기능과 연계된다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.sym.mnu.stm.web.EgovSiteMapngController.java | EgovSiteMapngController Class |
| Service | egovframework.com.sym.mnu.stm.service.EgovSiteMapngService.java | Service Interface |
| ServiceImpl | egovframework.com.sym.mnu.stm.service.impl.EgovSiteMapngServiceImpl.java |  |
| VO | egovframework.com.sym.mnu.stm.service.SiteMapngVO.java |  |
| DAO | egovframework.com.sym.mnu.stm.service.impl.SiteMapngDAO.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/mnu/stm/EgovSiteMap.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/mnu/stm/EgovSiteMapng.jsp |  |
| Query XML | resources/egovframework/mapper/com/sym/mnu/stm/EgovSiteMapng_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovSiteMapngService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectSiteMapng(ComDefaultVO)` | `SiteMapngVO` | 메뉴사이트맵에 관한 서비스 인터페이스 클래스를 정의한다. |

사이트맵 화면 생성은 메뉴생성관리 기능(`sym.mnu.mcm`의 `MenuSiteMap`, `EgovMenuCreatSiteMap.jsp`)과 연계되어 동작한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
