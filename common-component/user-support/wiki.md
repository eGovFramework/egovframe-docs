---
title: "Wiki기능"
linkTitle: "Wiki기능"
description: "Wiki기능"
url: /common-component/user-support/information-provided/wiki/
menu:
  depth:
    name: "Wiki기능"
    weight: 17
    parent: "information-provided"
---

## 개요

조직 내부의 지식, 업무 매뉴얼, 프로젝트 문서 등을 임직원들이 공동으로 작성하고 수정할 수 있는 위키(Wiki) 형태의 협업 문서 도구 컴포넌트입니다.

## 주요 기능

* **문서 공동 편집**: 권한을 가진 누구나 새로운 문서를 생성하거나 기존 문서를 수정할 수 있습니다.
* **버전(History) 관리**: 문서가 수정될 때마다 과거 버전이 기록되어, 누가 언제 어떤 내용을 수정했는지 추적하고 이전 버전으로 복구(Rollback)할 수 있습니다.
* **문서 간 링크 연결**: 위키 문법을 사용하여 시스템 내 다른 위키 문서로 쉽게 하이퍼링크를 연결할 수 있습니다.

## 데이터 구조 (테이블)

* `COMTNWIKIBKMK`: 위키 문서의 마스터 정보 및 북마크를 관리하는 테이블
* `COMTNWIKIHISTORY`: 문서의 본문 내용과 수정될 때마다의 변경 이력을 저장하는 테이블

## 활용 방안

업무 인수인계, 사내 지식 베이스(KB), 프로젝트 산출물 관리 등 구성원들의 집단 지성을 활용하여 지속적으로 업데이트되어야 하는 사내 문서 저장소로 활용됩니다.
