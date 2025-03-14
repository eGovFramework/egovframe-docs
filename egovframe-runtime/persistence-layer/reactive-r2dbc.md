---
title: R2DBC
linkTitle: "R2DBC"
description: R2DBC는 비동기적 방식으로 관계형 데이터베이스와 상호작용하기 위한 자바 라이브러리로, Spring WebFlux와 함께 리액티브 애플리케이션을 구성할 수 있다. 데이터베이스에 액세스하려면 ConnectionFactory 객체를 생성하여 공통으로 사용하며, 데이터베이스 종류에 따라 다른 구현체를 사용한다.
url: /egovframe-runtime/persistence-layer/reactive/reactive-r2dbc/
menu:
    depth:
        name: R2DBC
        weight: 1
        parent: "reactive"
---
# R2DBC

## 개요

 R2DBC(Relational Reactive Database Connectivity)는 Reactive 프로그래밍 모델을 기반으로 하는 비동기적인 방식으로 관계형 데이터베이스와 상호 작용하기 위한 자바 라이브러리로 Spring WebFlux와 함께 사용하여 비동기 논블로킹 방식의 애플리케이션을 구성할 수 있다. 이를 통해 리액티브 애플리케이션 스택에서 관계형 데이터 액세스 기술을 사용하는 Spring 기반 애플리케이션을 더 쉽게 빌드할 수 있다.

## 설명

### 데이터베이스 연동

 R2DBC를 사용하여 데이터베이스에 액세스하기 위해 가장 먼저 해야 할 일은 JDBC의 DataSource와 비슷한 역할을 하는 ConnectionFactory 객체를 만드는 것이다.  
ConnectionFactory를 생성하는 가장 간단한 방법은 ConnectionFactories 클래스를 사용하는 것인데 이 클래스에는 ConnectionFactoryOptions 객체를 받아 ConnectionFactory를 반환하는 정적 메서드가 있다.  
ConnectionFactory의 인스턴스는 하나만 필요하며, 데이터베이스 종류 및 데이터베이스 드라이버에 따라 구현체가 다를 수 있으므로 공통으로 사용할 수 있게 실행환경에 구성하고 애플리케이션 구성에서 필요할 때마다 주입을 통해 사용할 수 있도록 제공한다.

#### 실행환경 라이브러리

```java
package org.egovframe.rte.psl.reactive.r2dbc.connect;
 
public class EgovR2dbcConnectionFactory {
    public ConnectionFactory connectionFactory() {
        return ConnectionFactories.get(this.r2dbcUrl);
    }
}
```

#### 적용 예제

```java
package egovframework.webflux.config;
 
import org.egovframe.rte.psl.reactive.r2dbc.connect.EgovR2dbcConnectionFactory;
......
 
@Configuration
public class EgovR2dbcConfig {
 
    @Bean(name="connectionFactory")
    public ConnectionFactory connectionFactory() {
        EgovR2dbcConnectionFactory egovR2dbcConnectionFactory = new EgovR2dbcConnectionFactory(this.r2dbcUrl);
        return egovR2dbcConnectionFactory.connectionFactory();
    }
}
```

### Repository 구성

 R2DBC는 스프링 생태계와 통합되어 있어 스프링 기반 애플리케이션에서 쉽게 사용할 수 있으며, 스프링 데이터 R2DBC 프로젝트를 통해 스프링의 강력한 기능과 R2DBC의 비동기 데이터베이스 액세스를 결합할 수 있다.  
R2dbcEntityTemplate은 객체와 관계형 데이터베이스 간의 매핑을 지원하므로 SQL 쿼리를 직접 작성하지 않고도 객체를 데이터베이스 테이블에 매핑할 수 있으며, CRUD 작업을 단순화하여 개발자는 복잡한 SQL 쿼리를 작성하는 대신 객체 지향적인 방식으로 데이터베이스와 상호 작용할 수 있어 코드 가독성이 향상되고 유지 보수가 용이해진다.

#### 실행환경 라이브러리

 @Repository 클래스에 EgovR2dbcRepository 클래스를 extends 하여 insertData, updateData, deleteData, selectAllData 메소드를 활용한다.

```java
package org.egovframe.rte.psl.reactive.r2dbc.repository;
 
public class EgovR2dbcRepository<T> extends R2dbcEntityTemplate {
 
    public EgovR2dbcRepository(ConnectionFactory connectionFactory) {
        super(connectionFactory);
    }
 
    public Flux<T> selectAllData(Query query, Class<T> entityClass) {
        return select(query, entityClass);
    }
 
    public Mono<T> selectOneData(Query query, Class<T> entityClass) {
        return selectOne(query, entityClass);
    }
 
    public Mono<Long> countData(Query query, Class<T> entityClass) {
        return count(query, entityClass);
    }
 
    public Mono<T> insertData(T entity) {
        return insert(entity);
    }
 
    public Mono<T> updateData(T entity) {
        return update(entity);
    }
 
    public Mono<T> deleteData(T entity) {
        return delete(entity);
    }
}
```

## 참고자료

- [Spring Data R2DBC - Reference Documentation](https://docs.spring.io/spring-data/r2dbc/docs/1.5.12/reference/html/)