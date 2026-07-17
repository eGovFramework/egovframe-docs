---
title: "커뮤니티"
linkTitle: "커뮤니티"
description: "커뮤니티"
url: /common-component/collaboration/community/
menu:
  depth:
    weight: 2
    parent: "collaboration"
    identifier: "community"
---

# 커뮤니티

## 개요

커뮤니티 컴포넌트는 공통의 관심사를 가진 사용자들이 정보를 공유할 수 있는 커뮤니티 공간을 제공하는 협업 서비스 컴포넌트이다. 커뮤니티의 생성과 속성 관리, 회원의 신청·승인·탈퇴 관리, 커뮤니티 메인화면 구성과 커뮤니티 게시판 운영 기능을 제공한다.

본 문서는 커뮤니티 컴포넌트 전체의 구조와 공통 개념을 설명하는 개요 문서이다. 기능별 상세 내용은 관련 문서의 하위 문서를 참조한다.

## 주요 개념

### 기능 구성

| 기능 | 설명 |
| --- | --- |
| 커뮤니티생성관리 | 커뮤니티를 생성하고 등록된 커뮤니티의 속성 정보를 관리한다. 관리 기능은 별도의 관리 메뉴와 커뮤니티 내 관리 메뉴로 제공된다. |
| 커뮤니티회원관리 | 커뮤니티 사용자의 신청, 승인, 탈퇴 등 커뮤니티 회원을 관리한다. |
| 커뮤니티사용관리 | 커뮤니티 메인화면 구성과 커뮤니티 게시판 관리 기능을 제공한다. |

### 게시판과의 연계

커뮤니티 컴포넌트는 협업의 게시판 기능과 메인화면 구성을 통해 커뮤니티 서비스를 제공한다. 커뮤니티에서 생성한 게시판은 커뮤니티ID가 연결되어 해당 커뮤니티에서만 사용할 수 있다.

## 관련 문서

- [커뮤니티생성관리](./community-creation.md) — 커뮤니티 생성과 속성 관리
- [커뮤니티회원관리](./community-member.md) — 회원 신청·승인·탈퇴 관리
- [커뮤니티사용관리](./community-use.md) — 메인화면 구성과 커뮤니티 게시판 관리
- [게시판](./board.md) — 커뮤니티에서 연계 사용하는 게시판 컴포넌트

## 설명

### 패키지 구조

커뮤니티 컴포넌트의 소스는 `egovframework.com.cop.cmy` 패키지에 위치하며, Controller–Service–ServiceImpl–DAO 계층과 Model/VO, JSP, DB별 Query XML로 구성된다. 클래스 목록은 각 하위 문서의 관련 소스 절을 참조한다.

### 패키지 참조 관계

커뮤니티 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가진다. 컴포넌트 배포 시 오류 없이 실행되기 위하여 패키지 간의 참조 관계에 따라 게시판 등 관련 패키지와 함께 배포 파일을 구성한다.

- 패키지 간 참조 관계 : [게시판, 커뮤니티, 동호회 Package Dependency](../intro/package-reference.md#협업)

### ID Generation

커뮤니티ID는 실행환경의 ID Generation Service로 생성한다. 시퀀스 저장 테이블 COMTECOPSEQ에 CMMNTY_ID 항목을 추가해야 하며, DDL과 설정 상세는 [커뮤니티생성관리](./community-creation.md)의 ID Generation 절을 참조한다.

## 참고자료

- [게시판, 커뮤니티, 동호회 Package Dependency](../intro/package-reference.md#협업)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
