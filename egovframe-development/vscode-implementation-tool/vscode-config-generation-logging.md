---
title: Logging Configuration
linkTitle: "Logging Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Logging 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-logging/
menu:
  depth:
    weight: 5
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-logging"
---
# Logging Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Logging** 카테고리의 설정 유형을 안내한다.

Log4j2 기반의 로깅 설정 파일을 생성한다. JDBC Appender를 제외한 모든 유형은 XML, YAML, Properties 형식을 지원한다.

| 설정 유형 | 설명 |
|---|---|
| New Console Appender | 콘솔 출력 Appender 설정 |
| New File Appender | 파일 출력 Appender 설정 |
| New Rolling File Appender | 파일 크기 기반 롤링 Appender 설정 |
| New Time-Based Rolling File Appender | 시간 기반 롤링 Appender 설정 |
| New JDBC Appender | 데이터베이스 저장 Appender 설정 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common)을 참고한다.

### 요구 사양 (공통)

- Spring Framework 6.x
- JDK 17+
- Log4j 2.x (2.20.0+)

### 필요 의존성 (공통)

- `log4j-api`
- `log4j-core`
- `log4j-slf4j2-impl` (SLF4J bridge)

---

## New Console Appender

콘솔(표준 출력)에 로그를 출력하는 Appender 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `log4j2-console` |
| YAML | `log4j2-console` |
| Properties | `log4j2-console` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML / YAML / Properties |
| File Name | ✓ | 생성될 파일명 |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Appender Name | ✓ | Appender 이름. 기본값: `console` |
| Conversion Pattern | ✓ | 로그 출력 패턴. 기본값: `%d %5p [%c] %m%n` |

---

## New File Appender

지정한 파일 경로에 로그를 기록하는 Appender 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `log4j2-file` |
| YAML | `log4j2-file` |
| Properties | `log4j2-file` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML / YAML / Properties |
| File Name | ✓ | 생성될 파일명 |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Appender Name | ✓ | Appender 이름. 기본값: `file` |
| Conversion Pattern | ✓ | 로그 출력 패턴. 기본값: `%d %5p [%c] %m%n` |
| Log File Name | ✓ | 로그 파일 저장 경로. 예) `./logs/file/sample.log` |
| Append | | 기존 파일에 이어쓰기 여부. 기본값: `true` |

---

## New Rolling File Appender

파일 크기가 지정한 최대 크기에 도달하면 새 파일로 전환(롤링)하는 Appender 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `log4j2-rollingFile` |
| YAML | `log4j2-rollingFile` |
| Properties | `log4j2-rollingFile` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML / YAML / Properties |
| File Name | ✓ | 생성될 파일명 |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Appender Name | ✓ | Appender 이름. 기본값: `rolling-file` |
| Conversion Pattern | ✓ | 로그 출력 패턴. 기본값: `%d %5p [%c] %m%n` |
| Log File Name | ✓ | 현재 로그 파일 경로. 예) `./logs/rolling/rollingSample.log` |
| Log File Name Pattern | ✓ | 롤링 파일명 패턴. 예) `./logs/rolling/rollingSample.%i.log` |
| Max Index | ✓ | 최대 롤링 파일 인덱스. 예) `20` |
| Max File Size | ✓ | 롤링 기준 최대 파일 크기 (KB). 예) `3000` |

---

## New Time-Based Rolling File Appender

지정한 시간 주기가 경과하면 새 파일로 전환(롤링)하는 Appender 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `log4j2-timeBasedRollingFile` |
| YAML | `log4j2-timeBasedRollingFile` |
| Properties | `log4j2-timeBasedRollingFile` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML / YAML / Properties |
| File Name | ✓ | 생성될 파일명 |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Appender Name | ✓ | Appender 이름. 기본값: `rolling-file-time` |
| Conversion Pattern | ✓ | 로그 출력 패턴. 기본값: `%d %5p [%c] %m%n` |
| Log File Name | ✓ | 현재 로그 파일 경로. 예) `./logs/time/timeBasedRollingSample.log` |
| Log File Name Pattern | ✓ | 롤링 파일명 패턴 (날짜 포함). 예) `./logs/time/timeBasedRollingSample.%d{yyyy-MM-dd_HH-mm}.log` |
| Interval | ✓ | 롤링 주기. 예) `1` (파일명 패턴의 날짜 단위 기준) |
| Modulate | | 롤링 주기 정규화 여부. `true`이면 자정·정시 등 경계 시각에 맞게 조정. 기본값: `true` |

---

## New JDBC Appender

데이터베이스 테이블에 로그를 저장하는 Appender 설정 파일을 생성한다. Connection Type으로 `DriverManager` 또는 `ConnectionFactory`를 선택할 수 있다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `log4j2-jdbc` |
| YAML | `log4j2-jdbc` |

### 추가 필요 의존성

- `log4j-jdbc-appender`
- 데이터베이스 JDBC 드라이버 (예: `mysql-connector-j`)

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML 또는 YAML |
| File Name | ✓ | 생성될 파일명 |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Appender Name | ✓ | Appender 이름. 기본값: `jdbc` |
| Table Name | ✓ | 로그를 저장할 데이터베이스 테이블 이름. 예) `LOG` |
| Connection Type | ✓ | DB 연결 방식: `DriverManager` 또는 `ConnectionFactory` |

**DriverManager 선택 시 추가 항목**

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Driver | ✓ | JDBC 드라이버 클래스명. 예) `com.mysql.cj.jdbc.Driver` |
| URL | ✓ | 데이터베이스 URL. 예) `jdbc:mysql://localhost:3306/log` |
| User | ✓ | 데이터베이스 사용자명 |
| Password | ✓ | 데이터베이스 비밀번호 |

**ConnectionFactory 선택 시 추가 항목**

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Connection Factory Class | ✓ | 연결 팩토리 클래스명. 예) `org.egovframe.rte.fdl.logging.db.EgovConnectionFactory` |
| Connection Factory Method | ✓ | 연결 팩토리 메서드명. 예) `getDatabaseConnection` |
