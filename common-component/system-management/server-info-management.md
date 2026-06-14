---
title: "서버정보관리"
linkTitle: "서버정보관리"
description: "서버정보관리"
url: /common-component/system-management/system-manage/server-info-management/
menu:
  depth:
    name: "서버정보관리"
    weight: 2
    parent: "system-manage"
---

## 개요

시스템 운영에 사용되는 웹 서버(WEB), 웹 애플리케이션 서버(WAS), 데이터베이스 서버(DB) 등 각종 하드웨어 및 소프트웨어 서버의 자원 정보를 등록하고 관리하는 컴포넌트입니다.

## 주요 기능

* **서버 자원 등록**: 서버 명칭, 용도, IP 주소, 운영체제(OS) 버전, 하드웨어 스펙(CPU, RAM 등) 및 설치된 미들웨어 정보를 등록합니다.
* **상태 모니터링 연계**: (서버 보안 및 모니터링 솔루션과 연계 시) 서버의 현재 가동 상태 및 자원 사용률의 메타 데이터로 활용됩니다.

## 데이터 구조 (테이블)

* `COMTNSERVERINFO`: 서버 ID, 명칭, IP, OS 정보, 등록일 등을 저장하는 마스터 테이블

## 활용 방안

데이터센터나 클라우드 환경에서 다수의 서버 인스턴스를 운영할 때, 인프라 자원의 현황을 일목요연하게 파악하고 시스템 구조도(Architecture)를 관리하기 위한 구성 관리(CM) 데이터로 사용됩니다.
