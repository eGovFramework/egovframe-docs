---
title: "프로그램관리"
linkTitle: "프로그램관리"
description: "프로그램관리"
url: /common-component/system-management/program-manage/program-management/
menu:
  depth:
    name: "프로그램관리"
    weight: 1
    parent: "program-manage"
---

## 개요

시스템을 구성하는 개별 화면(JSP) 또는 백엔드 컨트롤러 URL 등의 단위 프로그램 정보를 시스템에 등록하여 인가(Authorization) 및 메뉴 매핑의 기준으로 삼는 컴포넌트입니다.

## 주요 기능

* **프로그램 목록 등록**: 시스템 내에 존재하는 모든 단위 기능의 URL 경로(예: `/sys/prog/selectList.do`), 프로그램명, 프로그램 설명을 등록합니다.
* **URL 권한 매핑 기초**: 등록된 프로그램 정보를 기반으로 롤(Role) 및 메뉴 구성을 수행합니다.
* **일괄 등록 (엑셀/초기화)**: 수백 개의 프로그램 URL을 엑셀 파일 등을 통해 일괄적으로 업로드하거나 기존 데이터를 검증하는 기능을 제공합니다.

## 데이터 구조 (테이블)

* `COMTNPROGRMLIST`: 프로그램 파일명(URL), 프로그램명, 설명 정보 등을 저장하는 마스터 테이블

## 활용 방안

스프링 시큐리티(Spring Security)나 인터셉터를 통한 권한 제어 과정에서, "요청된 URL이 시스템에 등록된 프로그램인지",
"이 프로그램에 접근 가능한 권한이 무엇인지"를 판단하는 가장 기초적인 원천 메타 데이터입니다.
