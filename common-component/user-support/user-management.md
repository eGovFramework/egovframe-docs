---
title: "사용자 관리"
linkTitle: "사용자 관리"
description: "사용자 관리는 사용자목록 조회기능과 신규등록기능, 상세조회기능, 사용자정보수정기능, 사용자암호수정기능, 사용자정보삭제기능을 제공한다."
url: /common-component/user-support/user-manage/user-management/
menu:
    depth:
        name: "사용자 관리"
        weight: 2
        parent: "user-manage"
        identifier: "user-management"
---

# 사용자 관리


## 개요

사용자 관리는 업무사용자(내부 직원)의 등록·조회·수정·삭제, 아이디 중복확인, 비밀번호 관리, 소속 부서 관리 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(사용자관리) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.umt.web.EgovDeptManageController.java | EgovDeptManageController Class |
| Controller | egovframework.com.uss.umt.web.EgovEmplyrManageController.java | EgovEmplyrManageController Class |
| Service | egovframework.com.uss.umt.service.EgovDeptManageService.java | Service Interface |
| Service | egovframework.com.uss.umt.service.EgovEmplyrManageService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.umt.service.impl.EgovDeptManageServiceImpl.java |  |
| ServiceImpl | egovframework.com.uss.umt.service.impl.EgovEmplyrManageServiceImpl.java |  |
| VO | egovframework.com.uss.umt.service.DeptManageVO.java |  |
| VO | egovframework.com.uss.umt.service.EmplyrManageInsertVO.java |  |
| VO | egovframework.com.uss.umt.service.EmplyrManageVO.java |  |
| VO | egovframework.com.uss.umt.service.EmplyrPasswordManageVO.java |  |
| DAO | egovframework.com.uss.umt.service.impl.DeptManageDAO.java |  |
| DAO | egovframework.com.uss.umt.service.impl.EmplyrManageDAO.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEmplyrInsert.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEmplyrManage.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEmplyrPasswordUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEmplyrSelectUpdt.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/umt/EgovDeptManage_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/umt/EgovEmplyrManage_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovEmplyrManageService (업무사용자))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `checkIdDplct(String)` | `int` | 사용자관리에 관한 인터페이스클래스를 정의한다. |
| `deleteEmplyr(String)` | `void` | 화면에 조회된 사용자의 정보를 데이터베이스에서 삭제 |
| `insertEmplyr(EmplyrManageVO)` | `String` | - |
| `selectEmplyr(String)` | `EmplyrManageVO` | 기 등록된 사용자 중 검색조건에 맞는 사용자의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `selectEmplyrList(UserDefaultVO)` | `List<EgovMap>` | 기 등록된 특정 사용자의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `selectEmplyrListTotCnt(UserDefaultVO)` | `int` | 기 등록된 특정 사용자목록의 전체수를 확인 |
| `updateEmplyr(EmplyrManageVO)` | `void` | 화면에 조회된 사용자의 기본정보를 수정하여 항목의 정합성을 체크하고 수정된 데이터를 데이터베이스에 반영 |
| `insertEmplyrHistory(EmplyrManageVO)` | `String` | 사용자정보 수정시 히스토리 정보를 추가 |
| `updatePassword(EmplyrPasswordManageVO)` | `void` | 업무사용자 암호 수정 |
| `selectPassword(EmplyrPasswordManageVO)` | `EmplyrPasswordManageVO` | 사용자가 비밀번호를 기억하지 못할 때 비밀번호를 찾을 수 있도록 함 |
| `updateLockIncorrect(EmplyrManageVO)` | `void` | 로그인인증제한 해제 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
