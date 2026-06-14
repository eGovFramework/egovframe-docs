---
title: "개요"
linkTitle: "개요"
description: "실행환경 통합 예제의 목적과 아키텍처 개요를 설명합니다."
url: /runtime-example/integrated-example/intro/
menu:
  depth:
    name: "개요"
    weight: 1
    parent: "integrated-example"
---

## 개요

실행환경 통합 예제는 eGovFrame의 핵심 기능들이 어떻게 상호작용하는지 보여주기 위해 만들어진 참조 모델입니다.

## 아키텍처 구성

* **Presentation Layer**: Spring MVC 기반 웹 요청 처리 및 화면 응답
* **Business Logic Layer**: Spring Web Flow 및 서비스 컴포넌트 로직
* **Persistence Layer**: MyBatis 또는 JPA를 이용한 데이터베이스 접근
* **Foundation Layer**: 로깅, 보안, 암호화 등 공통 기반 유틸리티 적용
