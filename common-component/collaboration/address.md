---
title: "주소록/명함록"
linkTitle: "주소록/명함록"
description: "주소록/명함록"
url: /common-component/collaboration/address/
menu:
  depth:
    weight: 6
    parent: "collaboration"
    identifier: "address"
---

# 주소록/명함록

## 개요

주소록/명함록 컴포넌트는 조직 구성원이 개인 또는 공용 주소록과 명함 정보를 등록·조회·관리할 수 있는 협업 서비스 컴포넌트이다.

## 주요 개념

주소록은 구성원(사용자)과 명함 정보를 항목으로 구성하며, 목록 조회·등록·수정과 팝업을 통한 선택 기능을 제공한다. 주소록과 명함 관리는 동일한 `cop.adb` 패키지의 소스를 공유한다.

## 관련 문서

- [명함관리](./business-card-management.md) — 명함 정보 등록·관리
- [주소록관리](./address-book.md) — 주소록 등록·관리

## 설명

### 패키지 구조

주소록/명함록 컴포넌트의 소스는 `egovframework.com.cop.adb` 패키지에 위치하며, Controller(EgovAddressBookController)–Service(EgovAddressBookService)–ServiceImpl–DAO(AddressBookDAO) 계층과 Model/VO(AddressBook, AddressBookUser 등), JSP, DB별 Query XML(EgovAdbk_SQL_*.xml)로 구성된다.

### 패키지 참조 관계

주소록 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가지며, 배포 시 패키지 간 참조 관계에 따라 관련 패키지와 함께 구성한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
