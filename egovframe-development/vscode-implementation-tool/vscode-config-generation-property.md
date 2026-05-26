---
title: Property Configuration
linkTitle: "Property Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Property 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-property/
menu:
  depth:
    weight: 6
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-property"
---
# Property Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Property** 카테고리의 설정 유형을 안내한다.

eGovFrame의 Property 서비스는 시스템 환경 변수, 데이터베이스 접속 정보 등 외부에서 관리해야 하는 설정값을 프로퍼티 파일로 분리하여 관리한다.

Property 카테고리는 다음 1가지 설정 유형을 제공한다.

| 설정 유형 | 설명 |
|---|---|
| New Property | 프로퍼티 서비스 설정 파일 생성 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common)을 참고한다.

---

## New Property

시스템 환경 변수 등의 정보를 외부 프로퍼티 파일로 분리하여 관리할 수 있는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-properties` |
| JavaConfig | `EgovPropertyConfig` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML 또는 JavaConfig |
| File Name / Class Name | ✓ | 생성될 파일명 또는 클래스명 |
| Package Name | ✓ (JavaConfig) | Java 패키지명 (JavaConfig 선택 시 표시) |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Property Service Name | ✓ | 프로퍼티 서비스 빈 이름. 예) `propertiesService` |
| Property Type | | 프로퍼티 유형 |
| Key | | 프로퍼티 키 |
| Value | | 프로퍼티 값 |
| Encoding | | 프로퍼티 파일 인코딩. 예) `UTF-8` |
| Property File | | 외부 프로퍼티 파일 경로. 예) `classpath:egovframework/egovProps/globals.properties` |
