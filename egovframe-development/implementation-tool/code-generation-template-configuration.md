---
title: Configuration Generation
linkTitle: Config Gen
description: "Configuration 자동 생성 기능"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-config-generation/
menu:
  depth:
    weight: 2
    parent: "template-based-code-generation"
    identifier: "eclipse-config-generation"
---

# Configuration Generation

## 개요

전자정부 프레임워크를 사용하여 프로그램을 개발할 때 주로 사용되는 설정 파일(XML)을 설정파일 마법사를 통하여 자동으로 생성하는 기능이다. 제공하는 설정파일 Template은 다음과 같다.

## 사용법

1. **Data Source** : 데이터베이스 연결을 설정.

   * [New DataSource Configuration Code Gen](./code-generation-template-configuration-folder/config-gen-datasource.md) : DBCP, JDBC Driver Type의 DataSource 설정.
   * [New JNDI DataSource Configuration Code Gen](./code-generation-template-configuration-folder/config-gen-jndi-datasource.md) : JNDI Lookup을 이용하여 Database Connection을 생성하는 DataSource 설정 (Weblogic, Jeus 설정 제공)

2. **Transaction** : 전자정부 프레임워크 Transaction 관리 설정

   * [DataSource Transaction Code Gen](./code-generation-template-configuration-folder/config-gen-datasource-transaction.md) : DataSource를 사용하여 Local Transaction 관리 설정.
   * [JPA Transaction Code Gen](./code-generation-template-configuration-folder/config-gen-jpa-transaction.md) : JPA EntityManagerFactory를 이용한 Transaction 관리 설정.
   * [JTA Transaction Code Gen](./code-generation-template-configuration-folder/config-gen-jta-transaction.md) : JTA를 이용한 Global Transaction 관리 설정.

3. **Cache** : 전자정부 프레임워크 Cache Service를 설정.

   * [Cache Configuration Code Gen](./code-generation-template-configuration-folder/config-gen-cache.md) : 기본 Cache, Custom Cache 설정.
   * [Ehcache Configuration Code Gen](./code-generation-template-configuration-folder/config-gen-ehcache.md) : Ehcache 설정.

4. **Id Generation** : 시스템을 개발할 때 필요한 유일한 ID를 생성하기 위한 설정.

   * [Sequence ID Generation Code Gen](./code-generation-template-configuration-folder/config-gen-sequence-id-generation.md) : Database의 SEQUENCE를 사용하는 서비스 설정.
   * [Table ID Generation Code Gen](./code-generation-template-configuration-folder/config-gen-table-id-generation.md) : 별도의 테이블을 이용한 ID 생성 서비스 설정
   * [UUID Generation Code Gen](./code-generation-template-configuration-folder/config-gen-uuid-generation.md) : Universally Unique Identifier(UUID) 생성 서비스 설정

5. **Logging** : logging 관련 설정 파일 작성

   * [Console Appender Code Gen](./code-generation-template-configuration-folder/config-gen-logging-console-appender.md) : log를 콘솔화면으로 출력하기 위한 appender 설정
   * [File Appender Code Gen](./code-generation-template-configuration-folder/config-gen-logging-file-appender.md) : log를 file로 출력하기 위한 appender 설정
   * [Rolling File Appender Code Gen](./code-generation-template-configuration-folder/config-gen-logging-rolling-file-appender.md) : 로그파일이 특정 크기 이상으로 커지지 않도록 백업 기능을 수행하는 RollingFileAppender 설정.
   * [Time Based Rolling File Appender Code Gen](./code-generation-template-configuration-folder/config-gen-logging-time-based-rolling-file-appender.md) : 설정한 시간 조건에 맞춰 로깅을 수행하는 TimeBasedRollingFileAppender 설정.
   * [JDBC Appender Code Gen](./code-generation-template-configuration-folder/config-gen-logging-jdbc-appender.md) : DB에 로그를 출력하기 위한 Appender 설정.

6. **Property**

   * [Property Code Gen](./code-generation-template-configuration-folder/config-gen-property.md) : Property Service 설정

7. **Scheduling** : 실행환경의 Scheduling 서비스 관련 XML 파일 작성

   * [Detail Bean Job Scheduling Code Gen](./code-generation-template-configuration-folder/config-gen-detail-bean-job-scheduling.md) : JobDetailBean을 이용한 작업 생성
   * [Method Invoking Job Scheduling Code Gen](./code-generation-template-configuration-folder/config-gen-method-invoking-job-scheduling.md) : MethodInvokingJobDetailFactoryBean을 이용한 작업 생성
   * [Simple Trigger Code Gen](./code-generation-template-configuration-folder/config-gen-simple-trigger.md) : SimpleTriggerBean을 이용한 설정
   * [Cron Trigger Code Gen](./code-generation-template-configuration-folder/config-gen-cron-trigger.md) : CronTriggerBean을 이용한 설정
   * [Scheduler Code Gen](./code-generation-template-configuration-folder/config-gen-scheduler.md) : SchedulerFactoryBean을 이용한 스케줄링한 작업의 시작 설정