---
title: "명함관리"
linkTitle: "명함관리"
description: "명함관리"
url: /common-component/collaboration/address/business-card-management/
menu:
  depth:
    name: "명함관리"
    weight: 1
    parent: "address"
---

# 명함관리

## 개요

명함관리는 명함 정보를 등록·조회하여 주소록의 항목으로 활용할 수 있는 기능을 제공한다.

## 설명

명함관리는 주소록관리와 동일한 `egovframework.com.cop.adb` 패키지의 소스를 공유한다. 명함 목록 조회 등 명함 관련 데이터 처리는 주소록 DAO(AddressBookDAO)의 명함(Card) 관련 질의로 수행되며, 등록된 명함은 주소록 구성 항목으로 선택할 수 있다.

### 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.adb.web.EgovAddressBookController.java | 주소록/명함 관리 컨트롤러 |
| Service | egovframework.com.cop.adb.service.EgovAddressBookService.java | 주소록/명함 서비스 인터페이스 |
| ServiceImpl | egovframework.com.cop.adb.service.impl.EgovAddressBookServiceImpl.java | 서비스 구현 클래스 |
| DAO | egovframework.com.cop.adb.service.impl.AddressBookDAO.java | 명함 목록·상세 조회 포함 데이터처리 클래스 |
| Query XML | resources/egovframework/mapper/com/cop/adb/EgovAdbk_SQL_*.xml | DB별 Query XML |

### 패키지 참조 관계

주소록 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가진다.

## 참고자료

- [주소록/명함록 개요](./address.md)
- [주소록관리](./address-book.md)
