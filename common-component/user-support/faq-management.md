---
title: "FAQ관리"
linkTitle: "FAQ관리"
description: "FAQ관리"
url: /common-component/user-support/online-help/faq-management/
menu:
  depth:
    name: "FAQ관리"
    weight: 12
    parent: "online-help"
---

## 개요

사용자들이 서비스 이용 시 자주 묻는 질문(FAQ, Frequently Asked Questions)과 그에 대한 답변을 카테고리별로 등록하여 제공하는 컴포넌트입니다.

## 주요 기능

* **FAQ 등록 및 관리**: 질문(Q)과 답변(A)을 작성하고, 첨부파일을 포함시켜 등록/수정/삭제합니다.
* **조회수 관리**: 사용자들이 각 FAQ 항목을 조회한 횟수를 카운트하여, 인기 있는 질문을 상단에 노출할 수 있습니다.
* **목록 및 상세 조회**: 일반 사용자가 질문 목록을 검색하고 상세 답변을 확인할 수 있는 화면을 제공합니다.

## 데이터 구조 (테이블)

* `COMTNFAQINFO`: FAQ 제목, 내용, 조회수, 첨부파일 ID 등을 저장하는 테이블

## 활용 방안

고객센터, 도움말 센터 등에서 단순 반복적인 사용자 문의(상담)를 줄이고, 사용자가 스스로 문제를 빠르게 해결할 수 있도록 돕는 지식 베이스(Knowledge Base)로 활용됩니다.
