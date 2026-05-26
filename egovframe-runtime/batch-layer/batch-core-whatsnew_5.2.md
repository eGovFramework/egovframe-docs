---
title: Spring Batch 5.2 신규 기능
linkTitle: "What's new in 5.2"
description: Spring Batch 5.2(5.2.3 호환)에서 도입된 주요 변경 사항을 한글로 정리한다. Spring Batch 5.2 Reference를 참고하였다.
url: /egovframe-runtime/batch-layer/batch-core-whatsnew_5.2/
menu:
    depth:
        name: Spring Batch 5.2 신규 기능
        weight: 5
        parent: "batch-layer"
        identifier: "batch-core-whatsnew_5.2"
---
# Spring Batch 5.2 신규 기능

본 문서는 [Spring Batch 5.2 Reference - What's new](https://docs.spring.io/spring-batch/reference/5.2/whatsnew.html)를 참고하여 Spring Batch 5.2에서 도입된 주요 변경 사항을 한글로 정리한다. 전체 변경 목록은 [Spring Batch 릴리스 노트](https://github.com/spring-projects/spring-batch/releases)를 참고한다.

## 의존성 업그레이드

Spring Batch 5.2에서 Spring 계열 의존성이 다음 버전으로 업그레이드되었다.

| 의존성 | 버전 |
|--------|------|
| Spring Framework | 6.2.0 |
| Spring Integration | 6.4.0 |
| Spring Data | 3.4.0 |
| Spring Retry | 2.0.10 |
| Spring LDAP | 3.2.8 |
| Spring AMQP | 3.2.0 |
| Spring Kafka | 3.3.0 |
| Micrometer | 1.14.1 |

## MongoDB Job Repository 지원

이번 릴리스에서 **NoSQL 기반 Job Repository**로 **MongoDB** 구현이 추가되었다. 관계형 Job Repository와 마찬가지로, Spring Batch는 MongoDB에 배치 메타데이터를 저장·조회하기 위한 컬렉션 생성 스크립트를 제공한다. MongoDB 4 이상이 필요하며, Spring Data MongoDB 기반이다.

사용 시 `MongoTemplate`과 `MongoTransactionManager`를 정의한 뒤, 새로 추가된 `MongoJobRepositoryFactoryBean`으로 JobRepository를 구성하면 된다. 자세한 예제는 [MongoDBJobRepositoryIntegrationTests](https://github.com/spring-projects/spring-batch/blob/main/spring-batch-core/src/test/java/org/springframework/batch/core/repository/support/MongoDBJobRepositoryIntegrationTests.java)를 참고한다.

## Resourceless Job Repository(신규)

Spring Batch 5에서는 메모리 기반 Map 방식의 Job Repository 구현이 제거되었다. 기존에는 JDBC 기반 Job Repository만 남아 데이터 소스가 필수였는데, 데이터 소스 없이 사용하던 사용자 요구에 맞춰 **5.2에서 리소스를 사용하지 않는 Job Repository**가 도입되었다.

이 구현은 배치 메타데이터를 **어떤 형태로도 저장하지 않으며**(메모리 포함), "NoOp" 방식으로 동작한다. 즉, 배치 메타데이터를 버리고 어떤 리소스와도 상호작용하지 않는다(이름은 "resourceless transaction manager"에서 유래). **재시작이 필요 없고**, ExecutionContext를 Step 간 데이터 공유나 파티션 메타데이터 공유 등에 사용하지 않는 경우에 적합하다. 한 번만 실행되는 Job, 단일 JVM 실행 환경에 적합하며, `DataSourceTransactionManager`를 사용하는 트랜잭션 Step 또는 `ResourcelessTransactionManager`를 사용하는 비트랜잭션 Step과 함께 사용할 수 있다. **스레드 안전하지 않으며** 동시 실행 환경에서는 사용하면 안 된다.

## Composite Item Reader

기존의 `CompositeItemProcessor`, `CompositeItemWriter`와 유사하게 **CompositeItemReader**가 추가되었다. 동일한 포맷의 데이터를 **여러 소스에서 순차적으로** 읽을 때 사용하며, 서로 다른 리소스에 흩어진 데이터를 커스텀 Reader 없이 처리할 수 있다. CompositeItemReader는 일반 ItemReader들을 순서대로 위임하여 읽기 작업을 수행한다. 예: 플랫 파일에서 Person을 읽은 뒤 DB 테이블에서 Person을 읽는 복합 Reader 구성.

## java.util.function API 어댑터

`FunctionItemProcessor`가 `java.util.function.Function`을 ItemProcessor에 적용한 것과 같이, 5.2에서는 **Supplier**, **Consumer**, **Predicate** 등 다른 `java.util.function` 인터페이스를 위한 어댑터가 추가되었다. 추가된 어댑터는 다음과 같다.

- **SupplierItemReader**
- **ConsumerItemWriter**
- **PredicateFilteringItemProcessor**

자세한 내용은 [org.springframework.batch.item.function](https://github.com/spring-projects/spring-batch/tree/main/spring-batch-infrastructure/src/main/java/org/springframework/batch/item/function) 패키지를 참고한다.

## BlockingQueue 기반 동시 Step(Item Reader/Writer)

[SEDA(Staged Event-Driven Architecture)](https://en.wikipedia.org/wiki/Staged_event-driven_architecture) 스타일은 큐로 연결된 단계별 데이터 처리에 적합하다. Spring Batch에서는 Job을 Step 시퀀스로 설계할 수 있어 이 패턴을 적용하기 쉽지만, **중간 큐에서 읽고 쓰는** ItemReader/ItemWriter가 없었다. 5.2에서는 **BlockingQueue**에서 데이터를 읽고 쓰는 **Item Reader**와 **Item Writer**가 추가되었다. 이를 통해 첫 번째 Step에서 큐에 데이터를 넣고, 두 번째 Step에서 같은 큐에서 소비하는 구조로 **두 Step이 동시에** 비차단·이벤트 기반으로 동작하도록 구성할 수 있다.

## JPA Item Reader의 쿼리 힌트 지원

5.1 이전에는 JPA Cursor/Paging Item Reader에서 fetch size, timeout 등의 **쿼리 힌트**를 지원하지 않아, 커스텀 쿼리 프로바이더를 제공해야 했다. 5.2부터 JPA Reader와 해당 Builder에서 **JPA 쿼리 정의 시 쿼리 힌트를 지정**할 수 있다.

## JDBC Item Reader의 Data Class 지원

JDBC Cursor/Paging Item Reader의 Builder에 **Data Class**(Java record 또는 Kotlin data class)를 대상 타입으로 지정할 수 있는 메서드가 추가되었다. `dataRowMapper(TargetType.class)` 메서드는 기존 `beanRowMapper(TargetType.class)`와 유사하며, 일반 Java Bean과 Data Class 간의 RowMapper 설정을 일관되게 한다.

## RecursiveCollectionLineAggregator의 라인 구분자 설정

이전에는 `RecursiveCollectionLineAggregator`의 라인 구분자가 시스템 라인 구분자로 고정되어 있었고, System 프로퍼티로만 변경할 수 있었다. 5.2에서는 **setter를 통해 라인 구분자를 설정**할 수 있어, 다른 배치 아티팩트와 동일한 방식으로 설정할 수 있다.

## Job 등록(Job Registry) 개선

5.1에서 배치 인프라 빈의 기본 설정이 JobRegistry를 자동으로 채우도록 `JobRegistryBeanPostProcessor`를 사용하도록 변경되었다. 이후 Spring Framework의 `BeanPostProcessorChecker` 로그 레벨 변경으로 인해 일반적인 Spring Batch 애플리케이션에서 `JobRegistryBeanPostProcessor` 관련 경고가 발생했다. 이는 BeanPostProcessor가 `JobRegistry` 빈에 의존하는 구조(권장되지 않으며 빈 생명주기 문제를 일으킬 수 있음) 때문이었다. 5.2에서는 **JobRegistry 채우기 방식이 BeanPostProcessor에서 SmartInitializingSingleton 사용**으로 바뀌어 해당 이슈가 해결되었다. `JobRegistryBeanPostProcessor`는 deprecated 되었으며, 새로 추가된 **JobRegistrySmartInitializingSingleton** 사용을 권장한다.

## 참고 문서

- [Spring Batch 5.2 - What's new](https://docs.spring.io/spring-batch/reference/5.2/whatsnew.html)
- [Spring Batch 5.2 Reference](https://docs.spring.io/spring-batch/reference/5.2/index.html)
