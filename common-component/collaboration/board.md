---
title: "게시판"
linkTitle: "게시판"
description: "게시판"
url: /common-component/collaboration/board/
menu:
  depth:
    weight: 1
    parent: "collaboration"
    identifier: "board"
---

# 게시판

## 개요

게시판 컴포넌트는 사용자 간 정보 공유를 위한 게시판의 생성부터 게시물의 등록·조회·수정·삭제까지 지원하는 협업 서비스 컴포넌트이다. 관리자는 게시판 생성 관리 기능으로 업무 특성에 맞는 게시판을 만들고 속성을 관리하며, 사용자는 생성된 게시판 유형(통합게시판, 블로그형게시판, 방명록)에 따라 게시물을 작성하고 조회한다.

본 문서는 게시판 컴포넌트 전체의 구조와 공통 개념을 설명하는 개요 문서이다. 기능별 상세 내용은 관련 문서의 하위 문서를 참조한다.

## 주요 개념

### 게시판 유형

게시판 생성 시 게시판유형 코드(COM101)로 유형을 지정하며, 유형에 따라 화면 형태와 제공 기능이 달라진다.

| 게시판유형 | 코드ID | 설명 |
| --- | --- | --- |
| 통합게시판 | BBST01 | 일반적으로 사용되는 게시판. 익명 게시판, 갤러리 형태(첨부 이미지 본문 표시) 등 속성에 따라 다른 형태로 표시된다. |
| 블로그형게시판 | BBST02 | 블로그 형태의 디자인을 채택한 게시판 |
| 방명록 | BBST03 | 방명록 형태의 게시판 |

### 게시판 생성 위치

게시판을 생성할 수 있는 위치는 시스템과 동호회/커뮤니티 두 가지로 나뉜다. 시스템에서 생성한 게시판은 시스템의 모든 사용자가 활용할 수 있으며, 커뮤니티에서 생성한 게시판은 커뮤니티ID가 연결되어 해당 커뮤니티에서만 사용할 수 있다.

### 게시판 속성과 게시물

게시판 컴포넌트는 게시판 자체의 속성 정보(BoardMaster)와 개별 게시물 정보(Board)를 분리하여 관리한다. 게시물의 수정과 삭제는 글을 게시한 당사자만 가능하다.

## 관련 문서

- [게시판관리](./board-management.md) — 게시판 생성과 속성 관리
- [게시판(통합 게시판)](./board-integrated.md) — 게시물 등록·조회·수정·답변
- [게시판(방명록)](./board-guestbook.md) — 방명록 등록·확인·수정
- [블로그관리](./blog-management.md) — 블로그형 게시판 관리

## 설명

### 패키지 구조

게시판 컴포넌트의 소스는 `egovframework.com.cop.bbs` 패키지에 위치하며, Controller–Service–ServiceImpl–DAO 계층과 Model/VO, JSP, DB별 Query XML(MySQL, Oracle, Tibero, Altibase, Cubrid, MariaDB, PostgreSQL, Goldilocks)로 구성된다. 클래스 목록은 각 하위 문서의 관련 소스 절을 참조한다.

### 패키지 참조 관계

게시판 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가진다. 컴포넌트 배포 시 오류 없이 실행되기 위하여 패키지 간의 참조 관계에 따라 협업의 공통기능(com), 디자인 템플릿과 함께 배포 파일을 구성한다.

- 패키지 간 참조 관계 : [게시판, 커뮤니티, 동호회 Package Dependency](../intro/package-reference.md/#협업)

### 관련 테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 게시판속성 | COMTNBBSMASTER | 게시판의 속성 정보를 관리한다. |
| 게시물 정보 | COMTNBBS | 게시물 정보를 관리한다. |
| 코드정보 | COMTCCMMNDETAILCODE | 게시판유형 등 코드 정보를 관리한다. |
| 시퀀스 | COMTECOPSEQ | ID Generation Service가 사용하는 시퀀스 저장 테이블 |

### ID Generation

게시판ID와 게시물ID는 실행환경의 ID Generation Service로 생성한다. 시퀀스 저장 테이블 COMTECOPSEQ에 BBS_ID 항목을 추가해야 하며, 설정 파일은 `resources/egovframework/spring/com/idgn/context-idgn-bbs.xml`이다. DDL과 설정 상세는 [게시판관리](./board-management.md)의 ID Generation 절을 참조한다.

## 참고자료

- [게시판, 커뮤니티, 동호회 Package Dependency](../intro/package-reference.md/#협업)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
