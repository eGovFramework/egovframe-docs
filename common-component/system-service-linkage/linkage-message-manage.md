---
title: "연계메시지관리"
linkTitle: "연계메시지관리"
description: "연계메시지관리"
url: /common-component/system-service-linkage/linkage-message-manage/
menu:
  depth:
    name: "연계메시지관리"
    weight: 2
    parent: "system-service-linkage"
---

## 개요

내부 시스템과 외부 기관(또는 타 시스템) 간에 데이터를 주고받기 위해 사용되는 전문(메시지)의 레이아웃 구조, 전문 코드, 헤더 및 바디 항목 등을 마스터로 정의하고 관리하는 컴포넌트입니다.

## 주요 기능

* **전문(Message) 레이아웃 정의**: 송수신할 데이터 전문의 총 길이, 각 필드의 명칭, 타입(String, Number), 길이(Byte), 필수 여부 등 상세 스펙을 등록합니다.
* **연계 코드 매핑**: 내부 시스템에서 사용하는 공통 코드와 외부 시스템에서 요구하는 코드가 다를 경우, 이를 자동으로 변환(Mapping)해주기 위한 변환 규칙을 설정합니다.
* **전문 이력 관리**: 시스템 고도화 등에 따라 전문 레이아웃이 변경되었을 때, 이전 버전과 최신 버전의 전문 규격을 이력으로 관리합니다.

## 데이터 구조 (테이블)

* `COMTNCNTCMSGE`: 연계 메시지 고유 ID, 메시지 명칭, 메시지 설명 등을 저장하는 마스터 테이블
* `COMTNCNTCMSGEIEM`: 해당 메시지를 구성하는 개별 필드(항목)의 명칭, 길이, 타입 등 상세 구조를 저장하는 테이블

## 활용 방안

EAI(Enterprise Application Integration)나 ESB(Enterprise Service Bus) 솔루션을 도입하지 않은 환경에서도
전문 파싱(Parsing) 및 생성 로직을 하드코딩하지 않고 DB 메타데이터 기반으로 유연하게 처리하기 위한 표준 모델로 사용됩니다.
