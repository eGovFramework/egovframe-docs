---
title: "메모보고"
linkTitle: "메모보고"
description: "메모보고"
url: /common-component/collaboration/schedule-manage/memo-report/
menu:
  depth:
    name: "메모보고"
    weight: 9
    parent: "schedule-manage"
---

# 메모보고

## 개요

메모보고는 보고자를 지정해 메모 형식의 보고를 등록·조회·수정·삭제하고, 보고에 대한 지시사항 등록과 보고자 조회일시 관리를 지원하는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 협업(일정관리) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.smt.mrm.web.EgovMemoReprtController.java | 메모보고 Controller Class |
| Service | egovframework.com.cop.smt.mrm.service.EgovMemoReprtService.java | 메모보고 Service Interface |
| ServiceImpl | egovframework.com.cop.smt.mrm.service.impl.EgovMemoReprtServiceImpl.java | 메모보고 ServiceImpl Class |
| VO | egovframework.com.cop.smt.mrm.service.MemoReprt.java / MemoReprtVO.java | 메모보고 VO Class |
| VO | egovframework.com.cop.smt.mrm.service.Reportr.java / ReportrVO.java | 보고자 VO Class |
| DAO | egovframework.com.cop.smt.mrm.service.impl.MemoReprtDAO.java | 메모보고 DAO Class |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mrm/EgovMemoReprtList.jsp | 메모보고 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mrm/EgovMemoReprtRegist.jsp | 메모보고 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mrm/EgovMemoReprtUpdt.jsp | 메모보고 수정 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mrm/EgovMemoReprtDetail.jsp | 메모보고 상세조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mrm/EgovReportrList.jsp, EgovReportrListPopup.jsp | 보고자 목록/선택 팝업 페이지 |
| Query XML | resources/egovframework/mapper/com/cop/smt/mrm/EgovMemoReprt_SQL_*.xml | DB별(altibase·cubrid·goldilocks·maria·mysql·oracle·postgres·tibero) Query XML |
| Message properties | resources/egovframework/message/com/cop/smt/mrm/message_ko.properties, message_en.properties | 메모보고 메시지 리소스 |

### 주요 메서드 (EgovMemoReprtService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectMemoReprtList(MemoReprtVO)` | `Map<String, Object>` | 메모보고 목록을 조회한다 |
| `selectMemoReprt(MemoReprtVO)` | `MemoReprtVO` | 메모보고 정보를 조회한다 |
| `insertMemoReprt(MemoReprt)` | `void` | 메모보고 정보를 등록한다 |
| `updateMemoReprt(MemoReprt)` | `void` | 메모보고 정보를 수정한다 |
| `updateMemoReprtDrctMatter(MemoReprt)` | `void` | 메모보고 정보의 지시사항을 등록한다 |
| `readMemoReprt(MemoReprt)` | `void` | 메모보고 정보의 보고자 조회일시를 수정한다 |
| `deleteMemoReprt(MemoReprtVO)` | `void` | 메모보고 정보를 삭제한다 |
| `selectReportrList(ReportrVO)` | `Map<String, Object>` | 보고자 목록을 조회한다 |
| `selectWrterClsfNm(String)` | `String` | 사용자 직위명 정보를 조회한다 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
