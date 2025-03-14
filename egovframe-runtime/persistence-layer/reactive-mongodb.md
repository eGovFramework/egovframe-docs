---
title: MongoDB
linkTitle: "MongoDB"
description: Spring Data MongoDB는 MongoDB 문서형 데이터 저장소와의 연동을 위한 고수준 추상화 템플릿을 제공하며, Spring JDBC 지원 방식과 유사하다. SimpleReactiveMongoDatabaseFactory 클래스를 사용해 MongoDB 연결을 관리하고, 데이터 액세스 작업에 집중할 수 있도록 지원한다.
url: /egovframe-runtime/persistence-layer/reactive/reactive-mongodb/
menu:
    depth:
        name: MongoDB
        weight: 2
        parent: "reactive"
---
# MongoDB

## 개요

 Spring Data MongoDB 프로젝트는 MongoDB 문서 스타일 데이터 저장소를 사용하는 솔루션 개발에 Spring의 핵심 개념을 적용하여 문서를 저장하고 쿼리하기 위한 높은 수준의 추상화 템플릿을 제공한다. Spring 프레임워크에서 제공하는 JDBC 지원과 유사하다는 것을 알 수 있다.

## 설명

### 데이터베이스 연동

 Spring WebFlux에서 MongoDB 데이터베이스와 연결을 설정하고 관리하기 위해서는 ReactiveMongoDatabaseFactory 인터페이스의 구현클래스인 SimpleReactiveMongoDatabaseFactory 클래스를 사용하여, 연결 풀링이나 커넥션 관리 기능 등을 추상화하여 데이터 액세스 작업에 집중할 수 있게 한다.

#### 실행환경 라이브러리

```java
package org.egovframe.rte.psl.reactive.mongodb.connect;
 
public class EgovMongoDbConnectionFactory {
    public ReactiveMongoDatabaseFactory reactiveMongoDatabaseFactory() {
        ConnectionString connectionString = new ConnectionString(this.mongoDbUrl);
        MongoClientSettings mongoClientSettings = MongoClientSettings.builder()
                .applyConnectionString(connectionString).build();
        return new SimpleReactiveMongoDatabaseFactory(
            MongoClients.create(mongoClientSettings), this.mongoDbName);
    }
}
```

#### 적용 예제

```java
package egovframework.webflux.config;
 
import org.egovframe.rte.psl.reactive.mongodb.connect.EgovMongoDbConnectionFactory;
......
 
@Configuration
public class EgovMongodbConfig {
 
    @Bean(name="reactiveMongoDatabaseFactory")
    public ReactiveMongoDatabaseFactory reactiveMongoDatabaseFactory() {
        EgovMongoDbConnectionFactory egovMongoDbConnectionFactory = new EgovMongoDbConnectionFactory(this.mongoDBName, this.mongoDBUrl);
        return egovMongoDbConnectionFactory.reactiveMongoDatabaseFactory();
    }
 
    @Bean
    public ReactiveMongoTransactionManager transactionManager(@Qualifier("reactiveMongoDatabaseFactory") ReactiveMongoDatabaseFactory reactiveMongoDatabaseFactory) {
        return new ReactiveMongoTransactionManager(reactiveMongoDatabaseFactory);
    }
}
```

### Repository 구성

 ReactiveMongoTemplate 클래스를 이용하여 Repository를 구성하면 MongoDB와 상호 작용하는 동안 Reactive 프로그래밍 모델을 활용할수 있고, Async Non-Blocking 데이터 처리가 가능하여 애플리케이션이 데이터베이스 작업을 대기하지 않고 다른 작업을 수행할 수 있도록 하며, 성능 향상을 실현할 수 있다. 또한 높은 동시 요청을 처리하기 위해 최적화되어 있어 논블로킹 작업을 통해 많은 동시 연결을 처리할 수 있으므로, 대규모 및 고트래픽 애플리케이션에 적합하다. 그리고 Reactive 프로그래밍은 자원을 효율적으로 사용할 수 있도록 도와준다. MongoDB 작업이 블로킹되지 않으므로 스레드 풀 및 메모리 자원을 효율적으로 관리할 수 있으며 MongoDB 연결을 관리하고 에러 처리를 담당하여 연결 풀링, 재시도 메커니즘 및 예외 처리를 제공하여 안정성을 향상시킨다.

#### 실행환경 라이브러리

 @Repository 클래스에 EgovMongoDbRepository 클래스를 extends 하여 insertData, updateData, deleteData, selectAllData 메소드를 활용한다.

```java
package org.egovframe.rte.psl.reactive.mongodb.repository;
 
public class EgovMongoDbRepository<T> extends ReactiveMongoTemplate {
    public EgovMongoDbRepository(ReactiveMongoDatabaseFactory reactiveMongoDatabaseFactory) {
        super(reactiveMongoDatabaseFactory);
    }
 
    public Flux<T> selectAllData(Query query, Class<T> entityClass) {
        return find(query, entityClass);
    }
 
    public Mono<T> selectOneData(Query query, Class<T> entityClass) {
        return findOne(query, entityClass);
    }
 
    public Mono<Long> countData(Query query, Class<T> entityClass) {
        return count(query, entityClass);
    }
 
    public Mono<T> insertData(T objectToSave) {
        return insert(objectToSave);
    }
 
    public Mono<T> updateData(Query query, Update update, Class<T> entityClass) {
        return findAndModify(query, update, entityClass);
    }
 
    public Mono<T> deleteData(Query query, Class<T> entityClass) {
        return findAndRemove(query, entityClass);
    }
}
```

## 참고자료

- [Spring Data MongoDB - Reference Documentation](https://docs.spring.io/spring-data/mongodb/docs/3.4.12/reference/html/)