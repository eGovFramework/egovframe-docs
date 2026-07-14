---
title: 데이터처리
linkTitle: 데이터처리
description: 데이터처리 서비스는 데이터베이스에 대한 연결 및 영속성 처리, 선언적인 트랜잭션 관리를 지원한다.
url: /egovframe-runtime/persistence-layer/
menu:
    depth:
        weight: 6
        parent: "egovframe-runtime"
        identifier: "persistence-layer"
---
# 데이터처리

데이터처리 서비스는 데이터베이스에 대한 연결 및 영속성 처리, 선언적인 트랜잭션 관리를 지원한다. 전자정부 표준프레임워크의 데이터처리 계층은 [Spring Framework 6.2 - Data Access](https://docs.spring.io/spring-framework/reference/6.2/data-access.html)를 기반으로 하며, [Transaction Management](https://docs.spring.io/spring-framework/reference/6.2/data-access/transaction.html), [Data Access with JDBC](https://docs.spring.io/spring-framework/reference/6.2/data-access/jdbc.html), [ORM (JPA/Hibernate)](https://docs.spring.io/spring-framework/reference/6.2/data-access/orm/jpa.html) 등과 정합성을 유지한다.

## 개요

데이터처리 계층은 데이터베이스 연결부터 SQL 매핑, 객체-관계 매핑(ORM), 트랜잭션 관리까지 데이터 액세스에 필요한 기능을 제공한다. MyBatis 기반 Data Access 서비스와 JPA 기반 ORM 서비스를 중심으로, Spring Data를 통한 다양한 데이터 저장소 연동도 지원한다.

## 주요 개념

DataSource 서비스가 데이터베이스 연결을 추상화해 업무 로직과 연결 방식의 종속성을 제거하고, 그 위에서 Data Access 서비스(MyBatis) 또는 ORM 서비스(JPA)를 선택해 사용한다. 트랜잭션은 선언적(Declarative) 방식과 프로그래밍 방식으로 관리할 수 있다.

## 관련 문서

### DataSource

- [DataSource 서비스](./data-source.md) — 데이터베이스 연결 추상화
- [DB 다중 접속 가이드](./db-connection.md) — 다중 DB 접근 및 master/slave 분리 접속

### Data Access 서비스 (MyBatis)

- [Data Access 서비스](./dataaccess-ibatis.md) — 데이터 조회·입력·수정·삭제의 일관된 처리
- [MyBatis](./dataaccess-mybatis.md) · [MyBatis 시작하기](./dataaccess-getting_started.md) — SqlSessionFactory 기반 사용법
- [MyBatis 적용 가이드](./dataaccess-mybatis-guide.md) — 표준프레임워크 기반 적용 가이드
- [MyBatis Configuration XML File](./dataaccess-configuration_xml.md) — properties·settings·typeAliases·mappers 설정
- [Mapper XML Files](./dataaccess-mapper_xml_files.md) — SQL 정의와 Parameter/Result Object 매핑
- [Mapper Dynamic SQL](./dataaccess-mybatis-dynamic-sql.md) — OGNL 표현식 기반 동적 SQL
- [MyBatis 주요 변경점](./dataaccess-ibatis_vs_mybatis.md) — iBATIS 대비 패키지·용어 변경 사항

### iBATIS

- [iBATIS Configuration](./dataaccess-ibatis_configuration.md) · [Data Type 매핑](./dataaccess-data_type.md) · [Dynamic SQL](./dataaccess-dynamic_sql.md)
- [parameterMap](./dataaccess-parametermap.md) · [resultMap](./dataaccess-resultmap.md) · [Inline Parameters](./dataaccess-inline_parameters.md)
- [Spring-iBATIS Integration](./dataaccess-spring_ibatis_integration.md) — 템플릿 스타일 프로그래밍과 트랜잭션 연계

### ORM 서비스 (JPA)

- [ORM 서비스](./orm.md) — JPA·Hibernate 기반 객체-관계 매핑
- [Entities](./orm-entities.md) · [Entity Operation](./orm-entity_operation.md) — 엔티티 구성과 입력·수정·조회·삭제
- [JPA Configuration](./orm-jpa_configuration.md) — persistence.xml 기반 설정
- [JPA Query Language](./orm-query_language.md) · [Native SQL](./orm-native_sql.md) — QL과 Native SQL 실행
- [Association Mapping](./orm-association_mapping.md) · [Fetch Strategy](./orm-fetch_strategy.md) — 연관 관계와 로딩 전략
- [Cache Handling](./orm-cache_handling.md) · [Concurrency](./orm-concurrency.md) — 캐시와 동시성(Locking)
- [Spring과 JPA 통합](./orm-spring_integration.md) — Spring 연계 방식

### Spring Data

- [Spring Data](./jpa-spring-data.md) — 다양한 데이터 액세스 기술 지원
- [Spring Data Repository](./jpa-repository.md) · [Query Method](./jpa-querymethod.md) — Repository 추상화와 메소드 기반 쿼리
- [Spring Data - MongoDB](./mongodb.md) — [MongoDB support](./mongodb-support.md) · [MongoDB Repositories](./mongodb-repositories.md)
  (3.5.1 버전: [MongoDB support](./mongodb-support3_5_1.md) · [MongoDB Repositories](./mongodb-repositories3_5_1.md))
- [Spring Data - Reactive](./reactive.md) — [R2DBC](./reactive-r2dbc.md) · [MongoDB](./reactive-mongodb.md) · [Cassandra](./reactive-cassandra.md) · [Redis](./reactive-redis.md)

### Transaction

- [Transaction 서비스](./transaction.md) — DataSource·JTA·JPA 트랜잭션 지원
- [선언적 Transaction 관리](./transaction-declarative-transaction-management.md) — 애노테이션·XML 기반
- [프로그래밍 방식의 Transaction 관리](./transaction-programmatic-transaction-management.md) — TransactionTemplate·Transaction Manager

### 작성 규칙

- [SQL 작성 규칙](./sql-rule.md) — SQL 문법 통일과 가독성 향상 가이드

## 참고자료

- [표준프레임워크 실행환경 소개](../intro/overview.md)
