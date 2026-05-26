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