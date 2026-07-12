---
title: "메모할일관리"
linkTitle: "메모할일관리"
description: "메모할일관리"
url: /common-component/collaboration/schedule-manage/memo-todo/
menu:
  depth:
    name: "메모할일관리"
    weight: 8
    parent: "schedule-manage"
---

# 메모할일관리

## 개요

메모할일관리는 개인의 할일을 메모 형식으로 등록·조회·수정·삭제하고, 오늘의 할일 목록을 별도로 확인할 수 있는 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 협업(일정관리) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.smt.mtm.web.EgovMemoTodoController.java | 메모할일 Controller Class |
| Service | egovframework.com.cop.smt.mtm.service.EgovMemoTodoService.java | 메모할일 Service Interface |
| ServiceImpl | egovframework.com.cop.smt.mtm.service.impl.EgovMemoTodoServiceImpl.java | 메모할일 ServiceImpl Class |
| VO | egovframework.com.cop.smt.mtm.service.MemoTodo.java / MemoTodoVO.java | 메모할일 VO Class |
| DAO | egovframework.com.cop.smt.mtm.service.impl.MemoTodoDAO.java | 메모할일 DAO Class |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mtm/EgovMemoTodoList.jsp | 메모할일 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mtm/EgovMemoTodoListToday.jsp | 오늘의 할일 목록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mtm/EgovMemoTodoRegist.jsp | 메모할일 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mtm/EgovMemoTodoUpdt.jsp | 메모할일 수정 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/smt/mtm/EgovMemoTodoDetail.jsp | 메모할일 상세조회 페이지 |
| Query XML | resources/egovframework/mapper/com/cop/smt/mtm/EgovMemoTodo_SQL_*.xml | DB별(altibase·cubrid·goldilocks·maria·mysql·oracle·postgres·tibero) Query XML |
| Message properties | resources/egovframework/message/com/cop/smt/mtm/message_ko.properties, message_en.properties | 메모할일 메시지 리소스 |

### 주요 메서드 (EgovMemoTodoService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `selectMemoTodoList(MemoTodoVO)` | `Map<String, Object>` | 메모할일 목록을 조회한다 |
| `selectMemoTodoListToday(MemoTodoVO)` | `List<MemoTodoVO>` | 메모할일 목록 중 오늘의 할일을 조회한다 |
| `selectMemoTodo(MemoTodoVO)` | `MemoTodoVO` | 메모할일 정보를 조회한다 |
| `insertMemoTodo(MemoTodo)` | `void` | 메모할일 정보를 등록한다 |
| `updateMemoTodo(MemoTodo)` | `void` | 메모할일 정보를 수정한다 |
| `deleteMemoTodo(MemoTodo)` | `void` | 메모할일 정보를 삭제한다 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
