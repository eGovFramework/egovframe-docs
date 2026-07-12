---
title: "회원 관리"
linkTitle: "회원 관리"
description: "회원 관리는 회원목록을 조회기능과 신규등록기능, 상세조회기능, 회원정보수정기능, 회원암호수정기능, 회원정보삭제기능, 회원가입신청기능을 제공한다."
url: /common-component/user-support/user-manage/member-management/
menu:
    depth:
        name: "회원 관리"
        weight: 3
        parent: "user-manage"
        identifier: "member-management"
---

# 회원 관리

# 회원 관리

## 개요

회원 관리는 일반회원과 기업회원의 가입·조회·수정·탈퇴(삭제), 아이디 중복확인, 비밀번호 관리, 회원 상태 변경 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(사용자관리) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.umt.web.EgovEntrprsManageController.java | EgovEntrprsManageController Class |
| Controller | egovframework.com.uss.umt.web.EgovMberManageController.java | EgovMberManageController Class |
| Service | egovframework.com.uss.umt.service.EgovEntrprsManageService.java | Service Interface |
| Service | egovframework.com.uss.umt.service.EgovMberManageService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.umt.service.impl.EgovEntrprsManageServiceImpl.java |  |
| ServiceImpl | egovframework.com.uss.umt.service.impl.EgovMberManageServiceImpl.java |  |
| VO | egovframework.com.uss.umt.service.EntrprsManageInsertVO.java |  |
| VO | egovframework.com.uss.umt.service.EntrprsManageVO.java |  |
| VO | egovframework.com.uss.umt.service.EntrprsPasswordManageVO.java |  |
| VO | egovframework.com.uss.umt.service.MberManageInsertVO.java |  |
| VO | egovframework.com.uss.umt.service.MberManageVO.java |  |
| VO | egovframework.com.uss.umt.service.MberPasswordManageVO.java |  |
| DAO | egovframework.com.uss.umt.service.impl.EntrprsManageDAO.java |  |
| DAO | egovframework.com.uss.umt.service.impl.MberManageDAO.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsInsert.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsManage.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsPasswordUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsSbscrb.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsSelectUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovEntrprsUserInsert.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovMberInsert.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovMberManage.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovMberPasswordUpdt.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovMberSbscrb.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/umt/EgovMberSelectUpdt.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/umt/EgovEntrprsManage_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/uss/umt/EgovMberManage_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovMberManageService (일반회원))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `insertMber(MberManageVO)` | `String` | 일반회원관리에 관한 인터페이스클래스를 정의한다. |
| `selectMber(String)` | `MberManageVO` | 기 등록된 사용자 중 검색조건에 맞는 일반회원의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `selectMberList(UserDefaultVO)` | `List<MberManageVO>` | 기 등록된 회원 중 검색조건에 맞는 회원들의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `selectMberListTotCnt(UserDefaultVO)` | `int` | 일반회원 총 개수를 조회한다. |
| `updateMber(MberManageVO)` | `void` | 화면에 조회된 일반회원의 기본정보를 수정하여 항목의 정합성을 체크하고 수정된 데이터를 데이터베이스에 반영 |
| `deleteMber(String)` | `void` | 화면에 조회된 사용자의 정보를 데이터베이스에서 삭제 |
| `selectStplat(String)` | `List<StplatVO>` | 일반회원 약관확인 |
| `updatePassword(MberPasswordManageVO)` | `void` | 일반회원암호수정 |
| `selectPassword(MberPasswordManageVO)` | `MberPasswordManageVO` | 일반회원이 비밀번호를 기억하지 못할 때 비밀번호를 찾을 수 있도록 함 |
| `updateLockIncorrect(MberManageVO)` | `void` | 로그인인증제한 해제 |

### 주요 메서드 (EgovEntrprsManageService (기업회원))

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `insertEntrprsmber(EntrprsManageVO)` | `String` | 기업회원관리에 관한 인터페이스클래스를 정의한다. |
| `selectEntrprsmber(String)` | `EntrprsManageVO` | 기 등록된 사용자 중 검색조건에 맞는기업회원의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `updateEntrprsmber(EntrprsManageVO)` | `void` | 화면에 조회된 기업회원의 기본정보를 수정하여 항목의 정합성을 체크하고 수정된 데이터를 데이터베이스에 반영 |
| `deleteEntrprsmber(String)` | `void` | 화면에 조회된 기업회원의 정보를 데이터베이스에서 삭제 |
| `selectStplat(String)` | `List<StplatVO>` | 기업회원용 약관정보 조회 |
| `updatePassword(EntrprsPasswordManageVO)` | `void` | 기업회원암호수정 |
| `selectPassword(EntrprsPasswordManageVO)` | `EntrprsPasswordManageVO` | 기업회원이 비밀번호를 기억하지 못할 때 비밀번호를 찾을 수 있도록 함 |
| `selectEntrprsMberList(UserDefaultVO)` | `List<EntrprsManageVO>` | 기 등록된기업 회원 중 검색조건에 맞는 회원들의 정보를 데이터베이스에서 읽어와 화면에 출력 |
| `selectEntrprsMberListTotCnt(UserDefaultVO)` | `int` | 기업회원 총 개수를 조회한다. |
| `updateLockIncorrect(EntrprsManageVO)` | `void` | 로그인인증제한 해제 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
