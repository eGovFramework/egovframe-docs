---
title: 템플릿 기반 Code Generation
linkTitle: 템플릿 기반 Code Gen
description: "DB Table 기반 Code Gen 기능과 Configuration 파일 생성 기능을 제공한다."
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/
menu:
  depth:
    weight: 1
    parent: "code-generation"
    identifier: "template-based-code-generation"
---

# 템플릿 기반 Code Generation

## 개요

미리 정의된 템플릿을 사용하여 eGovFrame 기반 CRUD 프로그램을 생성하거나 필요한 Configuration/Property 파일을 쉽게 작성할 수 있는 기능이다.
eGovFrame의 개발환경의 구현도구에서는 다음과 같은 Template 기반 Code Generation 기능을 제공한다.

## 설명

**CRUD 프로그램 자동 생성 기능**

데이터베이스 테이블을 참조하여 실행 가능한 CRUD Java Code 및 Jsp, SqlMapConfig 파일, SqlMap 파일 자동 생성.

**Configuration 자동 생성 기능**

전자정부 eGovFrame Framework 실행환경의 Configuration/Property 파일 작성 기능

* Data Source
* Transaction
* Cache
* Id Generation
* Logging
* Property
* Scheduling

**사용자 정의 템플릿 추가 기능**

프로젝트 환경 및 사용자 환경에 필요한 Configuration 파일을 사용자가 직접 작성하여 구현도구 내 추가하는 기능

## 사용법

* [CRUD 프로그램 자동 생성 기능](./code-generation-template-crud.md)
* [Configuration 자동 생성 기능](./code-generation-template-configuration.md)
* [사용자 정의 템플릿 추가 기능](./code-generation-template-custom.md)