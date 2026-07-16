---
title: ID Generation Configuration
linkTitle: "ID Generation Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 ID Generation 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-id-generation/
menu:
  depth:
    weight: 4
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-id-generation"
---
# ID Generation Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **ID Generation** 카테고리의 설정 유형을 안내한다.

eGovFrame의 ID Generation 서비스는 데이터베이스 Sequence, 테이블, 또는 UUID를 사용하여 고유한 ID를 생성하는 서비스다.

ID Generation 카테고리는 다음 3가지 설정 유형을 제공한다.

| 설정 유형 | 설명 |
|---|---|
| New Sequence ID Generation | DB Sequence 기반 ID 생성 서비스 설정 파일 생성 |
| New Table ID Generation | DB 테이블 기반 ID 생성 서비스 설정 파일 생성 |
| New UUID Generation | UUID 기반 ID 생성 서비스 설정 파일 생성 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common.md)을 참고한다.

---

## New Sequence ID Generation

데이터베이스 Sequence 객체를 조회하여 순차적인 ID를 생성하는 서비스 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-idgen` |
| JavaConfig | `EgovIdGenSequenceConfig` |

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
| ID Service Name | ✓ | ID 생성 서비스 빈 이름. 예) `egovIdGnrService` |
| DataSource Name | ✓ | 데이터소스 빈 이름. 예) `dataSource` |
| ID Type | ✓ | 생성할 ID의 Java 타입: `Long` / `String` |
| Query | | Sequence 조회 SQL. 예) `SELECT NEXTVAL('SEQ_ID')` |
| Strategy Name | | ID 가공 전략 빈 이름 |
| Prefix | | ID 앞에 붙일 접두사 |
| Ciphers | | 암호화 방식 |
| Fill Char | | ID 길이 맞춤에 사용할 채움 문자 |

---

## New Table ID Generation

데이터베이스 테이블을 사용하여 채번 방식으로 ID를 생성하는 서비스 설정 파일을 생성한다. 지정한 블록 크기만큼 ID를 한 번에 채번하여 성능을 향상시킨다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-idgen` |
| JavaConfig | `EgovIdGenTableConfig` |

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
| ID Service Name | ✓ | ID 생성 서비스 빈 이름. 예) `egovIdGnrService` |
| DataSource Name | ✓ | 데이터소스 빈 이름. 예) `dataSource` |
| ID Type | ✓ | 생성할 ID의 Java 타입: `Long` / `String` |
| Table | | ID 채번 테이블 이름. 예) `IDS` |
| Table Name Field Value | | 채번 테이블 내 ID 식별자 값 |
| Block Size | | 한 번에 채번할 블록 크기. 예) `10` |
| Strategy Name | | ID 가공 전략 빈 이름 |
| Prefix | | ID 앞에 붙일 접두사 |

---

## New UUID Generation

UUID(Universally Unique Identifier) 알고리즘을 사용하여 전역 고유 ID를 생성하는 서비스 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-idgen` |
| JavaConfig | `EgovIdGenUUIDConfig` |

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
| ID Service Name | ✓ | ID 생성 서비스 빈 이름. 예) `egovIdGnrService` |
| Address | | UUID 생성에 사용할 MAC 주소 또는 IP 주소. 예) `00:00:00:00:00:00` |
