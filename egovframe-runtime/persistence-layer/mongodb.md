---
title: "Spring Data - MongoDB"
linkTitle: "Spring Data - MongoDB"
url: /egovframe-runtime/persistence-layer/mongodb/
menu:
    depth:
        name: "MongoDB"
        weight: 6
        parent: "persistence-layer"
        identifier: "mongodb"
---

## 개요

표준프레임워크 실행환경에서 NoSQL 데이터베이스인 MongoDB를 연동하여 데이터를 다루는 방법을 제공한다. Spring Data MongoDB 모듈을 기반으로 구성된다.

RDBMS와 달리 유연한 문서(Document) 지향 데이터 구조를 가지는 MongoDB와의 통합을 위해,
도메인 클래스 매핑과 Repository 인터페이스, `MongoTemplate` 등을 활용하여 빠르고 직관적인 CRUD 연산을 지원한다.

## 주요 기능

* **Document 매핑**: `@Document`, `@Id` 등의 어노테이션을 사용하여 자바 객체(Entity)와 MongoDB 컬렉션을 매핑
* **MongoTemplate**: 복잡한 쿼리, 업데이트, 집계(Aggregation) 기능을 수행할 수 있는 템플릿 클래스 지원
* **MongoRepository**: 인터페이스 선언만으로 기본적인 CRUD 및 쿼리 메서드 자동 생성
