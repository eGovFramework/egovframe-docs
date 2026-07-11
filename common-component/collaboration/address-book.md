---
title: "주소록관리"
linkTitle: "주소록관리"
description: "주소록관리"
url: /common-component/collaboration/address/address-book/
menu:
  depth:
    name: "주소록관리"
    weight: 2
    parent: "address"
---

# 주소록관리

## 개요

주소록관리는 개인 또는 공용 주소록을 등록하고, 구성원과 명함 정보를 항목으로 담아 목록을 조회·수정할 수 있는 기능을 제공한다.

## 설명

### 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.adb.web.EgovAddressBookController.java | 주소록 관리 컨트롤러 |
| Service | egovframework.com.cop.adb.service.EgovAddressBookService.java | 주소록 관리 서비스 인터페이스 |
| ServiceImpl | egovframework.com.cop.adb.service.impl.EgovAddressBookServiceImpl.java | 주소록 관리 서비스 구현 클래스 |
| DAO | egovframework.com.cop.adb.service.impl.AddressBookDAO.java | 주소록 데이터처리 클래스 |
| Model/VO | egovframework.com.cop.adb.service.AddressBook.java, AddressBookVO.java, AddressBookUser.java, AddressBookUserVO.java | 주소록·구성원 모델 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/adb/EgovAddressBookList.jsp | 주소록 목록 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/adb/EgovAddressBookRegist.jsp | 주소록 등록 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/adb/EgovAddressBookUpdt.jsp | 주소록 수정 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/adb/EgovAddressBookPopup.jsp | 주소록 선택 팝업 |
| Query XML | resources/egovframework/mapper/com/cop/adb/EgovAdbk_SQL_*.xml | DB별(MySQL·Oracle·Tibero·Altibase·Cubrid·MariaDB·PostgreSQL·Goldilocks) Query XML |
| Message properties | resources/egovframework/message/com/cop/adb/message_ko.properties, message_en.properties | 메시지 리소스 |

### 패키지 참조 관계

주소록 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가진다.

## 참고자료

- [주소록/명함록 개요](./address.md)
