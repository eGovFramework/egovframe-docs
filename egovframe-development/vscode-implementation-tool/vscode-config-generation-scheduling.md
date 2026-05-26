---
title: Scheduling Configuration
linkTitle: "Scheduling Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Scheduling 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-scheduling/
menu:
  depth:
    weight: 7
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-scheduling"
---
# Scheduling Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Scheduling** 카테고리의 설정 유형을 안내한다.

Quartz 기반의 스케줄링 설정 파일을 생성한다. Quartz 스케줄링은 **Job(작업)**, **Trigger(실행 조건)**, **Scheduler(스케줄러)** 세 요소로 구성된다.

| 설정 유형 | 유형 | 설명 |
|---|---|---|
| New Detail Bean Job | Job | 서비스 클래스를 직접 지정하는 Job Detail 설정 |
| New Method Invoking Job | Job | 특정 빈의 메서드를 호출하는 Job Detail 설정 |
| New Simple Trigger | Trigger | 반복 횟수·주기 기반 Trigger 설정 |
| New Cron Trigger | Trigger | Cron 표현식 기반 Trigger 설정 |
| New Scheduler | Scheduler | Job과 Trigger를 등록하는 Scheduler 설정 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common)을 참고한다.

---

## New Detail Bean Job

태스크 실행에 필요한 정보를 캡슐화한 `JobDetailFactoryBean` 설정 파일을 생성한다. 실행할 서비스 클래스를 직접 지정한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-scheduling` |
| JavaConfig | `EgovSchedulingBeanJobConfig` |

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
| Job Name | ✓ | Job 빈 이름. 예) `batchJob` |
| Service Class | ✓ | 실행할 서비스 클래스 전체 경로. 예) `egovframework.example.service.EgovSampleBatchJob` |
| Concurrent | | 동시 실행 허용 여부. 기본값: `false` (동시 실행 방지) |

---

## New Method Invoking Job

특정 빈 객체의 메서드를 주기적으로 호출하는 `MethodInvokingJobDetailFactoryBean` 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-scheduling` |
| JavaConfig | `EgovSchedulingMethodJobConfig` |

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
| Job Name | ✓ | Job 빈 이름. 예) `methodJob` |
| Service Name | ✓ | 호출할 서비스 빈 이름. 예) `egovSampleService` |
| Service Method | ✓ | 호출할 메서드 이름. 예) `execute` |
| Concurrent | | 동시 실행 허용 여부. 기본값: `false` |

---

## New Simple Trigger

지연 시간, 반복 횟수, 반복 간격을 기반으로 태스크를 실행하는 `SimpleTriggerFactoryBean` 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-scheduling` |
| JavaConfig | `EgovSchedulingSimpleTriggerConfig` |

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
| Trigger Name | ✓ | Trigger 빈 이름. 예) `simpleTrigger` |
| Job Detail Type | ✓ | 연결할 Job Detail 빈 유형 선택 |
| Start Delay | | 최초 실행 전 대기 시간 (ms). 예) `1000` |
| Repeat Interval | | 반복 실행 간격 (ms). 예) `5000` (5초마다 실행) |

---

## New Cron Trigger

Cron 표현식을 기반으로 특정 시간·요일·월에 태스크를 실행하는 `CronTriggerFactoryBean` 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-scheduling` |
| JavaConfig | `EgovSchedulingCronTriggerConfig` |

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
| Trigger Name | ✓ | Trigger 빈 이름. 예) `cronTrigger` |
| Job Detail Type | ✓ | 연결할 Job Detail 빈 유형 선택 |
| Cron Expression | ✓ | Cron 표현식. 예) `0 0/1 * * * ?` (매 1분마다 실행) |

#### Cron 표현식 형식

```
초 분 시 일 월 요일 [년]
```

| 필드 | 허용 값 | 허용 특수문자 |
|---|---|---|
| 초 | 0-59 | `, - * /` |
| 분 | 0-59 | `, - * /` |
| 시 | 0-23 | `, - * /` |
| 일 | 1-31 | `, - * ? / L W` |
| 월 | 1-12 또는 JAN-DEC | `, - * /` |
| 요일 | 0-7 또는 SUN-SAT | `, - * ? / L #` |

---

## New Scheduler

`SchedulerFactoryBean`을 사용하여 Job과 Trigger를 등록하고 스케줄 실행을 시작하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-scheduling` |
| JavaConfig | `EgovSchedulingSchedulerConfig` |

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
| Scheduler Name | ✓ | Scheduler 빈 이름. 예) `scheduler` |
| Trigger Type | ✓ | 등록할 Trigger 유형 선택 (Simple / Cron) |
