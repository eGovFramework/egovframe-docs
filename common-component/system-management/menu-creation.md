---
title: "메뉴생성"
linkTitle: "메뉴생성"
description: "메뉴생성"
url: /common-component/system-management/menu-manage/menu-creation/
menu:
  depth:
    name: "메뉴생성"
    weight: 2
    parent: "menu-manage"
---

## 개요

`프로그램관리`를 통해 등록된 개별 단위 프로그램(화면)들을 조합하여, 특정 사용자 그룹(권한)별로 실제 화면에 노출될 메뉴 트리(Navigation Tree) 구조를 생성하고 매핑하는 컴포넌트입니다.

## 주요 기능

* **권한별 메뉴 구성**: 관리자 권한, 일반 사용자 권한 등 권한 그룹(Role)에 따라 접근 가능한 메뉴 목록을 다르게 생성합니다.
* **메뉴 트리 배치**: 프로그램들을 대메뉴, 중메뉴, 소메뉴 형태의 계층 구조로 배치하고 정렬 순서를 지정합니다.
* **메뉴 생성 처리**: 구성이 완료된 메뉴 트리를 시스템에 반영(생성)하여 로그인한 사용자의 권한에 맞게 UI가 그려지도록 합니다.

## 데이터 구조 (테이블)

* `COMTNMENUCREATDTLS`: 권한 그룹(Author Code)별로 매핑된 메뉴 식별자 리스트를 저장하는 테이블

## 활용 방안

인가(Authorization) 시스템의 핵심으로, 사용자의 역할에 따라 보여줄 기능과 감출 기능을 동적으로 제어하는 RBAC(Role-Based Access Control) 구현의 중추적인 역할을 합니다.
