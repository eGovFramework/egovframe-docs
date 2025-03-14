---
title: Cassandra
linkTitle: "Cassandra"
description: Spring Data Cassandra는 Cassandra 데이터베이스와의 연동을 위한 고수준 추상화 템플릿을 제공하며, Spring의 JDBC 지원 방식과 유사하다. 비동기적인 상호 작용을 위해 DefaultBridgedReactiveSession 클래스를 사용하여 Cassandra 클러스터에 연결하고, 비동기 쿼리를 실행 및 관리할 수 있다.
url: /egovframe-runtime/persistence-layer/reactive/reactive-cassandra/
menu:
    depth:
        name: Cassandra
        weight: 3
        parent: "reactive"
---
# Cassandra

## 개요

 Cassandra를 위한 Spring 데이터 프로젝트는 핵심 Spring 개념을 Cassandra 컬럼형 데이터 저장소를 사용하는 솔루션 개발에 적용하여 문서를 저장하고 쿼리하기 위한 높은 수준의 추상화 템플릿을 제공한다. Spring 프레임워크에서 제공하는 JDBC 지원과 유사하다는 것을 알 수 있다.

## 설명

### 데이터베이스 연동

 Spring Data Cassandra와 Spring WebFlux를 함께 사용하여 Cassandra 데이터베이스와의 비동기적인 상호 작용을 지원하기 위해 Spring Data Cassandra에서 제공하는 DefaultBridgedReactiveSession 클래스를 사용한다. 해당 클래스를 사용하여 Cassandra 클러스터에 대한 연결을 설정하고, 세션을 관리하며 비동기 쿼리를 실행하고 결과를 처리할 수 있다.

#### 실행환경 라이브러리

```java
package org.egovframe.rte.psl.reactive.cassandra.connect;
 
public class EgovCassandraConfiguration {
 
    public ReactiveSession reactiveSession() {
        return new DefaultBridgedReactiveSession(
            CqlSession.builder()
                .withLocalDatacenter(getDataCenterName())
                .withKeyspace(getKeyspaceName())
                .addContactPoint(InetSocketAddress.createUnresolved(getContactPoint(), getPort()))
                .withAuthCredentials(getUsername(), getPassword())
                .build()
        );
    }
}
```

#### 적용 예제

```java
package egovframework.webflux.config;
 
import org.egovframe.rte.psl.reactive.cassandra.connect.EgovCassandraConfiguration;
......
 
@Configuration
public class EgovCassandraConfig {
 
    @Bean(name="reactiveSession")
    public ReactiveSession reactiveSession() {
        EgovCassandraConfiguration egovCassandraConfiguration = new EgovCassandraConfiguration();
        egovCassandraConfiguration.setDataCenterName(this.dataCenterName);
        egovCassandraConfiguration.setKeyspaceName(this.keyspaceName);
        egovCassandraConfiguration.setContactPoint(this.contactPoints);
        egovCassandraConfiguration.setPort(this.port);
        egovCassandraConfiguration.setUsername(this.username);
        egovCassandraConfiguration.setPassword(this.password);
        return egovCassandraConfiguration.reactiveSession();
    }
}
```

### Repository 구성

 Spring WebFlux와 ReactiveCassandraTemplate을 사용하면 비동기, 논블로킹 처리와 높은 가용성을 통한 효율적인 Cassandra 데이터베이스 상호 작용을 달성할 수 있으며 확장성, 효율성, 그리고 반응형 스트리밍을 통해 데이터베이스 처리를 최적화할 수 있다. 또한 Flux 및 Mono와 같은 리액티브 타입을 사용하여 스트림 데이터를 다룰 수 있으며, 실시간 데이터 처리 및 웹 소켓과 같은 실시간 기능을 구현하기가 용이하다.

#### 실행환경 라이브러리

 @Repository 클래스에 EgovCassandraRepository 클래스를 extends 하여 insertData, updateData, deleteData, selectAllData 메소드를 활용한다.

```java
package org.egovframe.rte.psl.reactive.cassandra.repository;
 
public class EgovCassandraRepository<T> extends ReactiveCassandraTemplate {
    public EgovCassandraRepository(ReactiveSession reactiveSession) {
        super(reactiveSession);
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

- [Spring Data for Apache Cassandra - Reference Documentation](https://docs.spring.io/spring-data/cassandra/docs/3.4.12/reference/html/)