---
title: "부서업무함관리"
linkTitle: "부서업무함관리"
description: "부서업무함관리"
url: /common-component/collaboration/schedule-manage/department-task-box/
menu:
  depth:
    name: "부서업무함관리"
    weight: 6
    parent: "schedule-manage"
---

# 부서업무함관리

## 개요

부서업무함관리는 부서별 업무함을 생성하고 부서 업무와 담당자를 등록·조회·관리할 수 있는 기능을 제공한다.

## 설명

부서업무함(DeptJobBx)을 단위로 부서의 업무(DeptJob)를 등록하고, 업무별 담당자(Charger)를 지정하여 관리한다. 부서 목록과 담당자 선택은 팝업 화면으로 제공된다.

### 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.smt.djm.web.EgovDeptJobController.java | 부서업무함/부서업무 관리 컨트롤러 |
| Service | egovframework.com.cop.smt.djm.service.EgovDeptJobService.java | 부서업무 서비스 인터페이스 |
| ServiceImpl | egovframework.com.cop.smt.djm.service.impl.EgovDeptJobServiceImpl.java | 서비스 구현 클래스 |
| DAO | egovframework.com.cop.smt.djm.service.impl.DeptJobDAO.java | 부서업무 데이터처리 클래스 |
| Model/VO | egovframework.com.cop.smt.djm.service.DeptJobBx.java, DeptJobBxVO.java, DeptJob.java, DeptJobVO.java, Dept.java, DeptVO.java, Charger.java, ChargerVO.java | 부서업무함·업무·부서·담당자 모델 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/djm/EgovDeptJobBxList.jsp 외 | 업무함 목록·등록·수정, 업무 목록·상세·등록·수정, 부서·담당자 팝업 |
| Query XML | resources/egovframework/mapper/com/cop/smt/djm/EgovDeptJob_SQL_*.xml | DB별 Query XML |
| Message properties | resources/egovframework/message/com/cop/smt/djm/message_ko.properties, message_en.properties | 메시지 리소스 |

### 패키지 참조 관계

부서업무함 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가진다.

## 참고자료

- [부서일정관리](./department-schedule.md)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
