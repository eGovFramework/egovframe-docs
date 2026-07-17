---
title: "협업"
linkTitle: "협업"
description: "협업"
url: /common-component/collaboration/
menu:
  depth:
    weight: 5
    parent: "common-component"
    identifier: "collaboration"
---

# 협업

## 개요

협업 카테고리는 조직 구성원 간의 정보 공유와 의사소통을 지원하는 공통컴포넌트 모음이다. 게시판, 커뮤니티, 일정관리, 전자우편, 주소록/명함록, 전자결재 연계 등 조직의 일상적인 협업 업무에 필요한 기능을 제공한다.

## 주요 개념

협업 컴포넌트의 소스는 주로 `egovframework.com.cop.*` 패키지에 위치하며, 요소기술의 공통 패키지(cmm)에 대해 직접적인 함수적 참조 관계를 가진다. 게시판과 커뮤니티처럼 컴포넌트 간에 연계되는 기능(커뮤니티 게시판 등)이 있어, 배포 시 패키지 간 참조 관계에 따라 관련 패키지를 함께 구성한다.

## 관련 문서

- [게시판](./board.md) — 게시판 생성·관리와 게시물 등록·조회 (통합게시판, 블로그형, 방명록)
- [커뮤니티](./community.md) — 커뮤니티 생성관리·회원관리·사용관리
- 일정관리 — [전체일정](./all-schedule.md), [부서일정](./department-schedule.md), [간부일정](./executive-schedule.md)
- [전자우편](./email.md) — 전자우편 발송 연계
- [주소록/명함록](./address.md) — 주소록 및 명함록 관리
- [전자결재](./edsm.md) — 전자결재 시스템 연계

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
- [게시판, 커뮤니티, 동호회 Package Dependency](../intro/package-reference.md#협업)
