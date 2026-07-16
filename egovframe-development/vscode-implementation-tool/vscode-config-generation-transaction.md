---
title: Transaction Configuration
linkTitle: "Transaction Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Transaction 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-transaction/
menu:
  depth:
    weight: 8
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-transaction"
---
# Transaction Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Transaction** 카테고리의 설정 유형을 안내한다.

Transaction 카테고리는 다음 3가지 설정 유형을 제공한다.

| 설정 유형 | 설명 |
|---|---|
| New Datasource Transaction | Datasource 기반 선언적 트랜잭션 관리 설정 |
| New JPA Transaction | JPA 환경 트랜잭션 관리 설정 |
| New JTA Transaction | 분산 트랜잭션(JTA) 관리 설정 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common.md)을 참고한다.

---

## New Datasource Transaction

AOP 또는 `@Transactional` 어노테이션을 사용하여 Datasource의 트랜잭션을 선언적으로 관리하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-transaction` |
| JavaConfig | `EgovTransactionConfig` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML 또는 JavaConfig |
| File Name / Class Name | ✓ | 생성될 파일명 또는 클래스명 |
| Package Name | ✓ (JavaConfig) | Java 패키지명 (JavaConfig 선택 시 표시) |

#### Configuration — 기본 설정

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Transaction Name | ✓ | 트랜잭션 매니저 빈 이름. 예) `transactionManager` |
| DataSource Name | ✓ | 연결할 데이터소스 빈 이름. 예) `dataSource` |
| AOP Config Transaction | | AOP 기반 트랜잭션 설정 포함 여부. 체크 시 AOP 관련 항목이 추가로 표시된다. |
| Annotation Transaction | | `@Transactional` 어노테이션 기반 트랜잭션 활성화 여부 |

#### Configuration — AOP 기반 트랜잭션 (AOP Config Transaction 체크 시)

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Point Cut Name | ✓ | AOP 포인트컷 빈 이름. 예) `transactionPointcut` |
| Point Cut Expression | ✓ | 포인트컷 표현식. 예) `execution(* egovframework.example..impl.*Impl.*(..))` |
| Advice Name | ✓ | 트랜잭션 어드바이스 빈 이름. 예) `transactionAdvice` |

**트랜잭션 속성 설정 (메서드 단위)**

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Method Name | | 트랜잭션을 적용할 메서드 패턴. 예) `*`, `insert*`, `update*` |
| Propagation | | 트랜잭션 전파 방식. 기본값: `REQUIRED` |
| Isolation | | 트랜잭션 격리 수준. 기본값: `DEFAULT` |
| Timeout | | 트랜잭션 타임아웃 (초). `-1`이면 제한 없음 |
| Read Only | | 읽기 전용 여부. 읽기 전용 시 최적화 가능 |
| Rollback For | | 롤백을 유발할 예외 클래스. 예) `Exception` |
| No Rollback For | | 롤백을 유발하지 않을 예외 클래스 |

#### 전파 방식(Propagation) 옵션

| 옵션 | 설명 |
|---|---|
| `REQUIRED` | 트랜잭션이 없으면 새로 생성, 있으면 참여 (기본값) |
| `REQUIRES_NEW` | 항상 새 트랜잭션 생성. 기존 트랜잭션은 일시 중단 |
| `SUPPORTS` | 트랜잭션이 있으면 참여, 없으면 트랜잭션 없이 실행 |
| `NOT_SUPPORTED` | 트랜잭션 없이 실행. 기존 트랜잭션은 일시 중단 |
| `MANDATORY` | 반드시 기존 트랜잭션에 참여. 없으면 예외 발생 |
| `NEVER` | 트랜잭션 없이 실행. 기존 트랜잭션이 있으면 예외 발생 |
| `NESTED` | 중첩 트랜잭션 생성 (Savepoint 활용) |

#### 격리 수준(Isolation) 옵션

| 옵션 | 설명 |
|---|---|
| `DEFAULT` | 데이터베이스 기본 격리 수준 사용 |
| `READ_UNCOMMITTED` | 커밋되지 않은 데이터 읽기 허용 (Dirty Read 가능) |
| `READ_COMMITTED` | 커밋된 데이터만 읽기 (Oracle 기본값) |
| `REPEATABLE_READ` | 반복 읽기 보장 (MySQL 기본값) |
| `SERIALIZABLE` | 완전한 격리. 성능 저하 가능 |

---

## New JPA Transaction

JPA(Java Persistence API) 환경에서 `JpaTransactionManager`를 사용하여 트랜잭션을 관리하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-transaction` |
| JavaConfig | `EgovJpaTransactionConfig` |

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
| Transaction Name | ✓ | 트랜잭션 매니저 빈 이름. 예) `transactionManager` |
| Entity Manager Factory | ✓ | EntityManagerFactory 빈 이름. 예) `entityManagerFactory` |
| Packages To Scan | | JPA 엔티티를 스캔할 패키지 경로. 예) `egovframework.example.domain` |
| Dialect Name | | JPA Dialect 클래스명. 예) `org.hibernate.dialect.MySQLDialect` |
| Spring Data JPA Repositories Package | | Spring Data JPA 리포지토리 인터페이스 스캔 패키지. 예) `egovframework.example.repository` |

---

## New JTA Transaction

여러 데이터베이스 또는 메시지 브로커에 걸친 분산 트랜잭션을 JTA(Java Transaction API)를 기반으로 관리하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-transaction` |
| JavaConfig | `EgovJtaTransactionConfig` |

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
| Transaction Name | ✓ | 트랜잭션 매니저 빈 이름. 예) `transactionManager` |
| JTA Implementation | | JTA 구현체 클래스명. 예) `com.atomikos.icatch.jta.UserTransactionManager` |
| Global Timeout | | 전역 트랜잭션 타임아웃 (초). 예) `300` |
