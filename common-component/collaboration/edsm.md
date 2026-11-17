---
title: "전자결재"
linkTitle: "전자결재"
description: "전자결재"
url: /common-component/collaboration/edsm/
menu:
  depth:
    weight: 7
    parent: "collaboration"
    identifier: "edsm"
---

# 전자결재

## 개요

전자결재는 업무 처리에 필요한 결재 정보를 지정하고 결재권자가 승인 또는 반려하는 흐름을 지원하는 협업 서비스 컴포넌트이다. 공통컴포넌트에서는 약식결재가 이 메뉴의 하위 기능이며, 소스는 `egovframework.com.uss.ion.ism` 패키지에 위치한다.

## 관련 문서

- [약식결재](./brief-approval.md) — 약식결재 정보의 등록, 삭제, 상세조회, 승인, 반려 기능을 제공한다.

## 설명

### 패키지 구조

약식결재의 소스는 `egovframework.com.uss.ion.ism` 패키지에 위치하며, Controller(EgovInfrmlSanctnController)–Service(EgovInfrmlSanctnService)–ServiceImpl(EgovInfrmlSanctnServiceImpl)–DAO(InfrmlSanctnDAO) 계층과 Model/VO(InfrmlSanctn, Sanctner, SanctnerVO), JSP, DB별 Query XML(`EgovInfrmlSanctn_SQL_*.xml`)로 구성된다.

### 패키지 참조 관계

약식결재 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가지며, 배포 시 패키지 간 참조 관계에 따라 관련 패키지와 함께 구성한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
