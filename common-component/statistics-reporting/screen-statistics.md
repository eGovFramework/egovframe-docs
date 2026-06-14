---
title: "화면통계"
linkTitle: "화면통계"
description: "화면통계"
url: /common-component/statistics-reporting/screen-statistics/
menu:
  depth:
    name: "화면통계"
    weight: 3
    parent: "statistics-reporting"
---

## 개요

시스템을 구성하는 개별 메뉴(화면 URL)들에 대한 사용자의 접근 빈도를 측정하여, '가장 많이 쓰이는 기능'과 '방치된 기능'을 식별하는 메뉴 단위의 사용성 분석 컴포넌트입니다.

## 주요 기능

* **메뉴별 사용량 통계**: 대메뉴, 중메뉴, 소메뉴 단위로 사용자의 클릭(페이지 뷰) 횟수를 집계하여 화면 이동 경로와 이용 빈도를 도출합니다.
* **권한별 접근 분석**: 관리자 권한, 일반 사용자 권한 등 사용자 그룹(Role)에 따라 선호하는 메뉴가 어떻게 다른지 비교 분석합니다.

## 데이터 구조 (테이블)

* `COMTNWEBLOG` / `COMTNSUSELOG`: 개별 사용자의 URL 접근 원천 로그 데이터
* `COMTNSCREENSTATS`: 메뉴 단위로 요약 집계된 화면 사용 빈도 데이터를 저장하는 테이블

## 활용 방안

차세대 시스템 개편이나 UI/UX 고도화 사업을 진행할 때, 거의 사용되지 않는 불필요한 화면을 통폐합(Sunset)하고
트래픽이 집중되는 핵심 화면의 접근성을 강화하는 등 데이터 기반의 설계(Data-Driven Design) 근거로 활용됩니다.
