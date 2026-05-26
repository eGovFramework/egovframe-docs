---
title: Datasource Configuration
linkTitle: "Datasource Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Datasource 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-datasource/
menu:
  depth:
    weight: 3
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-datasource"
---
# Datasource Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Datasource** 카테고리의 설정 유형을 안내한다.

Datasource 카테고리는 다음 2가지 설정 유형을 제공한다.

| 설정 유형 | 설명 |
|---|---|
| New Datasource | DBCP, C3P0, JDBC 기반 데이터소스 설정 파일 생성 |
| New JNDI Datasource | JNDI 기반 데이터소스 설정 파일 생성 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common)을 참고한다.

---

## New Datasource

DBCP, C3P0, JDBC 중 하나의 드라이버 유형을 선택하여 데이터소스 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-datasource` |
| JavaConfig | `EgovDataSourceConfig` |

### 요구 사양

- Spring Framework 6.x
- JDK 17+
- Jakarta EE 9

### 필요 의존성

| Driver Type | 의존성 |
|---|---|
| DBCP | `commons-dbcp2:2.13.0` |
| C3P0 | `c3p0:0.10.1` |
| JDBC Driver | `mysql-connector-j`, `mariadb-java-client`, `postgresql` 등 |

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
| DataSource Name | ✓ | 데이터소스 빈 이름. 예) `dataSource` |
| Driver Type | ✓ | 드라이버 유형 선택: `DBCP` / `C3P0` / `JDBC` |
| Driver | ✓ | JDBC 드라이버 클래스명. 예) `com.mysql.cj.jdbc.Driver` |
| URL | ✓ | 데이터베이스 URL. 예) `jdbc:mysql://127.0.0.1:3306/myDB` |
| User | ✓ | 데이터베이스 사용자명. 예) `root` |
| Password | | 데이터베이스 비밀번호 |

---

## New JNDI Datasource

WAS(Web Application Server)의 JNDI(Java Naming and Directory Interface)를 통해 데이터소스를 참조하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-datasource` |
| JavaConfig | `EgovDataSourceConfig` |

### 요구 사양

- Spring Framework 6.x
- JDK 17+
- Jakarta EE 9
- WAS JNDI 설정 완료 (Tomcat `context.xml` 등)

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
| DataSource Name | ✓ | 데이터소스 빈 이름. 예) `dataSource` |
| JNDI Name | ✓ | WAS에 등록된 JNDI 이름. 예) `java:comp/env/jdbc/myDB` |
