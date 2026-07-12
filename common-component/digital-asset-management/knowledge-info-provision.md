---
title: "지식정보제공"
linkTitle: "지식정보제공"
description: "지식정보제공"
url: /common-component/digital-asset-management/knowledge-map/knowledge-info-provision/
menu:
  depth:
    name: "지식정보제공"
    weight: 3
    parent: "knowledge-map"
---

# 지식정보제공

## 개요

지식정보제공은 지식전문가에게 지식정보를 요청하고, 요청된 지식정보를 제공(답변)하는 기능이다. 소스는 디지털자산관리(`egovframework.com.dam.spe.req`) 패키지에 위치하며, 지식전문가 관리 기능과 연계되어 동작한다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.dam.spe.req.web.EgovRequestOfferController.java | EgovRequestOfferController Class |
| Service | egovframework.com.dam.spe.req.service.EgovRequestOfferService.java | Service Interface |
| ServiceImpl | egovframework.com.dam.spe.req.service.impl.EgovRequestOfferServiceImpl.java |  |
| VO | egovframework.com.dam.spe.req.service.RequestOfferVO.java |  |
| Class | egovframework.com.dam.spe.req.service.RequestOffer.java |  |
| DAO | egovframework.com.dam.spe.req.service.impl.RequestOfferDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/req/EgovComDamRequestOfferDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/req/EgovComDamRequestOfferList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/req/EgovComDamRequestOfferRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/dam/spe/req/EgovComDamRequestOfferUpdt.jsp |  |
| Query XML | resources/egovframework/mapper/com/dam/spe/req/EgovDamRequestOffer_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovRequestOfferService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectRequestOfferDelCnt(Map<?, ?>)` | `int` | 목록/기본 기능을 처리한다 |
| `selectRequestOfferSpeCheck(Map<?, ?>)` | `boolean` | 등록된 지식전문가 건수를 조회한다. |
| `selectRequestOfferList(RequestOfferVO)` | `List<EgovMap>` | 지식정보제공/지식정보요청 목록을 조회한다. |
| `selectRequestOfferListCnt(RequestOfferVO)` | `int` | 지식정보제공/지식정보요청를(을) 목록 전체 건수를(을) 조회한다. |
| `selectRequestOfferDetail(RequestOfferVO)` | `RequestOfferVO` | 지식정보제공/지식정보요청를(을) 상세조회 한다. |
| `insertRequestOffer(RequestOfferVO)` | `void` | 지식정보제공/지식정보요청를(을) 등록한다. |
| `updateRequestOffer(RequestOfferVO)` | `void` | 지식정보제공/지식정보요청를(을) 수정한다. |
| `deleteRequestOffer(RequestOfferVO)` | `void` | 지식정보제공/지식정보요청를(을) 삭제한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
