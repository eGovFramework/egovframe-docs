---
title: Spring Data
linkTitle: "Spring Data - JPA"
description: Spring Data는 관계형 및 비관계형 데이터베이스, map-reduce 프레임워크, 클라우드 기반 데이터 서비스 등 다양한 데이터 액세스 기술을 쉽게 사용할 수 있도록 지원하는 오픈 소스 프로젝트이다. 이를 통해 새로운 데이터 기술뿐만 아니라 관계형 데이터베이스에 대한 향상된 지원도 제공한다.
url: /egovframe-runtime/persistence-layer/jpa-spring-data/
menu:
    depth:
        name: JPA
        weight: 5
        parent: "persistence-layer"
        identifier: "jpa-spring-data"
---
# Spring Data

Spring Data는 데이터베이스 관련 많은 하위 프로젝트를 포함하는 오픈 소스 프로젝트로, non-relational databases, map-reduce frameworks, and cloud based data services 등의 새로운 데이터 액세스 기술을 보다 쉽게 사용 할 수 있는 기능을 제공한다. 또한 관계형 데이터베이스 기술에 대한 향상된 지원도 제공한다.

### Spring Data Project
| Category              | Sub-Project     | Description                                                                                                                                                                                                                                                   |
| --------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Relational Databases  | JPA             | Spring Data JPA - Simplifies the development of creating a JPA-based data access layer                                                                                                                                                                        |
|                       | JDBC Extensions | Support for Oracle RAC, Advanced Queuing, and Advanced datatypes. Support for using QueryDSL with JdbcTemplate.                                                                                                                                               |
| Big Data              | Apache Hadoop   | The Apache Hadoop project is an open-source implementation of frameworks for reliable, scalable, distributed computing and data \\storage.                                                                                                                    |
| Data-Grid             | GemFire         | VMware vFabric GemFire is a distributed data management platform providing dynamic scalability, high performance, and database-like \\persistence. It blends advanced techniques like replication, partitioning, data-aware routing, and continuous querying. |
| HTTP                  | REST            | Spring Data REST - Perform CRUD operations of your persistence model using HTTP and Spring Data Repositories.                                                                                                                                                 |
| Key Value Stores      | Redis           | Redis is an open source, advanced key-value store.                                                                                                                                                                                                            |
| Document Stores       | MongoDB         | MongoDB is a scalable, high-performance, open source, document-oriented database.                                                                                                                                                                             |
| Graph Databases       | Neo4j           | Neo4j is a graph database, a fully transactional database that stores data structured as graphs.                                                                                                                                                              |
| Column Stores         | HBase           | Apache HBase is an open-source, distributed, versioned, column-oriented store modeled after Google' Bigtable. HBase functionality is part of the Spring for Apache Hadoop project.                                                                            |
| Common Infrastructure | Commons         | Provides shared infrastructure for use across various data access projects. General support for cross-database persistence is located here                                                                                                                    |

## 참고자료
- [http://projects.spring.io/spring-data](http://projects.spring.io/spring-data)