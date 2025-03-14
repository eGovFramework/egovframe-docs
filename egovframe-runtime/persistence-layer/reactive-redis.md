---
title: Redis
linkTitle: "Redis"
description: Spring Data Redis는 키-값 데이터 저장소인 Redis와의 상호작용을 위해 높은 수준의 추상화 템플릿을 제공하며, Spring의 JDBC 지원 방식과 유사하다. LettuceConnectionFactory 클래스를 사용해 비동기적으로 Redis와 연결하고, 데이터베이스 세션 관리 및 쿼리 실행을 지원한다.
url: /egovframe-runtime/persistence-layer/reactive/reactive-redis/
menu:
    depth:
        name: Redis
        weight: 4
        parent: "reactive"
---
# Redis

## 개요

 Spring Data Redis 프로젝트는 키-값 스타일 데이터 저장소를 사용하여 솔루션 개발에 핵심 Spring 개념을 적용하여 메시지를 주고받기 위한 높은 수준의 추상화 템플릿을 제공한다. Spring 프레임워크의 JDBC 지원과 유사하다는 것을 알 수 있다.

## 설명

### 데이터베이스 연동

 Spring Data Redis와 Spring WebFlux를 함께 사용하여 Redis 데이터베이스와의 비동기적인 상호 작용을 지원하기 위해 Spring Data Redis에서 제공하는 ReactiveRedisConnectionFactory 인터페이스의 구현클래스인 LettuceConnectionFactory 클래스를 사용한다. 해당 클래스를 사용하여 데이터베이스 연결을 설정하고, 세션을 관리하며 비동기 쿼리를 실행하고 결과를 처리할 수 있다.

#### 실행환경 라이브러리

```java
package org.egovframe.rte.psl.reactive.redis.connect;
 
public class EgovRedisConfiguration {
    public ReactiveRedisConnectionFactory reactiveRedisConnectionFactory() {
        return new LettuceConnectionFactory(this.host, this.port);
    }
}
```

#### 적용 예제

```java
package egovframework.webflux.config;
 
@Configuration
public class EgovRedisConfig {
 
    @Bean(name="reactiveRedisConnectionFactory")
    public ReactiveRedisConnectionFactory reactiveRedisConnectionFactory() {
        EgovRedisConfiguration egovRedisConfiguration = new EgovRedisConfiguration(this.host, this.port);
        return egovRedisConfiguration.reactiveRedisConnectionFactory();
    }
 
    @Bean(name="idsSerializationContext")
    public RedisSerializationContext<String, Ids> idsReactiveRedisTemplate() {
        Jackson2JsonRedisSerializer<Ids> serializer = new Jackson2JsonRedisSerializer<>(Ids.class);
        RedisSerializationContext.RedisSerializationContextBuilder<String, Ids> builder =
                RedisSerializationContext.newSerializationContext(ew StringRedisSerializer());
        return builder.value(serializer).hashValue(serializer).hashKey(serializer).build();
    }
 
    @Bean(name="sampleSerializationContext")
    public RedisSerializationContext<String, Sample> sampleReactiveRedisTemplate() {
        Jackson2JsonRedisSerializer<Sample> serializer = new Jackson2JsonRedisSerializer<>(Sample.class);
        RedisSerializationContext.RedisSerializationContextBuilder<String, Sample> builder =
                RedisSerializationContext.newSerializationContext(new StringRedisSerializer());
        return builder.value(serializer).hashValue(serializer).hashKey(serializer).build();
    }
}
```

### Repository 구성

 Spring WebFlux와 ReactiveRedisTemplate을 이용을 사용하면 Async Non-Blocking 처리로 I/O 밀집적인 작업을 효율적으로 처리 가능하여 대량의 동시 요청을 효과적으로 처리하고 확장 가능한 애플리케이션을 개발할 수 있다. 또한, Redis 데이터베이스에 비동기 쿼리를 보내고 전반적인 성능을 향상시킬 수 있어 데이터 스트리밍과 실시간 데이터 처리에 적합하다. 그리고, Spring 프레임워크와의 원활한 통합으로 풍부한 개발 환경을 제공하며 모델의 일관성을 유지하고 유지 관리를 간편하게 할 수 있다.

#### 실행환경 라이브러리

 @Repository 클래스에 EgovRedisRepository 클래스를 extends 하여 insertData, updateData, deleteData, selectData 메소드를 활용한다.

```java
package org.egovframe.rte.psl.reactive.redis.repository;
 
public class EgovRedisRepository<T> extends ReactiveRedisTemplate {
    public EgovRedisRepository(ReactiveRedisConnectionFactory connectionFactory, RedisSerializationContext serializationContext) {
        super(connectionFactory, serializationContext);
    }
 
    public Flux<T> selectData(String redisKey) {
        return opsForList().range(redisKey, 0, -1);
    }
 
    public Mono<Long> findIndex(String redisKey, T entity) {
        return opsForList().indexOf(redisKey, entity);
    }
 
    public Mono<Long> countData(String redisKey) {
        return opsForList().size(redisKey);
    }
 
    public Mono<T> insertData(String redisKey, T entity) {
        return opsForList().leftPush(redisKey, entity);
    }
 
    public Mono<T> updateData(String redisKey, long idx, T entity) {
        return opsForList().set(redisKey, idx, entity);
    }
 
    public Mono<Boolean> deleteAllData(String redisKey) {
        return opsForList().delete(redisKey);
    }
 
    public Mono<Boolean> deleteData(String redisKey, T entity) {
        return opsForList().remove(redisKey, 0, entity);
    }
}
```

## 참고자료

- [Spring Data Redis](https://docs.spring.io/spring-data/redis/docs/2.7.12/reference/html/)