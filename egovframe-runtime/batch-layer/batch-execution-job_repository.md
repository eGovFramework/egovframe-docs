---
title: JobRepository
linkTitle: JobRepository
description: JobRepository는 배치 작업 중의 정보를 저장하는 역할을 한다. 어떠한 Job이 언제 수행되었고, 언제 끝났으며, 몇 번이 실행되었고 실행에 대한 결과가 어떤지 등의 배치 작업의 수행과 관련된 모든 meta data가 저장되어 있다.
url: /egovframe-runtime/batch-layer/batch-execution-job_repository/
menu:
    depth:
        name: JobRepository
        weight: 7
        parent: "batch-layer"
---
# JobRepository

## 개요
JobRepository는 배치 작업 중의 정보를 저장하는 역할을 한다. 어떠한 Job이 언제 수행되었고, 언제 끝났으며, 몇 번이 실행되었고 실행에 대한 결과가 어떤지 등의 배치 작업의 수행과 관련된 모든 meta data가 저장되어 있다.

## 설명
JobRepository은 수행되는 Job에 대한 정보를 담고 있는 저장소로 배치작업의 지속성 메커니즘이다. JobRepository는 Spring Batch에서 JobExecution와 StepExecution 등과 같은 지속성을 가진 정보의 기본 CRUD작업에 사용된다. 배치작업이 처음 실행되면 JobRepository에서 JobExecution이 생성되고 배치작업이 실행되는 동안 StepExecution 및 JobExecution의 정보들이 JobRepository에 저장되고 갱신되어 지속된다.

JobRepository는 배치 네임 스페이스를 통해서나 JobRepositoryFactoryBean 클래스를 사용하여 아래와 같이 설정할 수 있다.

```xml
<job-repository id="jobRepository"
    data-source="dataSource"
    transaction-manager="transactionManager"
    isolation-level-for-create="SERIALIZABLE"
    table-prefix="BATCH_"
    max-varchar-length="1000"
/>
```

```xml
<bean id="jobRepository" class="org.springframework.batch.core.repository.support.JobRepositoryFactoryBean"
		p:dataSource-ref="dataSource" p:transactionManager-ref="transactionManager" p:isolation-level-for-create="ISOLATION_DEFAULT"
	       p:table-prefix="BATCH_" p:max-var-char-length="1000"/>
```

### 트랜잭션 설정(Transaction Configuration for the JobRepository)
네임 스페이스를 사용하는 경우, transactional advice가 자동으로 Repository 주위에 생성된다. 배치작업의 실패 후 다시 시작할 필요있는가의 상태를 포함하고 있는 메타 데이터가 제대로 지속되어 있는지 확인한다. repository이 트랜잭션 처리를 하지 않는다면 프레임 워크의 처리가 잘 정의되지 않는다. 기본적인 isolation level은 가장 격리 수준이 높은 serializable이고 재정의도 가능하다.

```xml
<job-repository id="jobRepository"
                isolation-level-for-create="REPEATABLE_READ" />
```

네임스페이스나 Bean 정의를 사용하지 않는 경우에는 AOP를 이용하여 Repository에 대한 트랜잭션의 관리할 수 있도록 설정해야 한다.

```xml
<aop:config>
    <aop:advisor 
           pointcut="execution(* org.springframework.batch.core..*Repository+.*(..))"/>
    <advice-ref="txAdvice" />
</aop:config>
 
<tx:advice id="txAdvice" transaction-manager="transactionManager">
    <tx:attributes>
        <tx:method name="*" />
    </tx:attributes>
</tx:advice>
```

위의 설정은 거의 변경없이 사용할 수 있다.다만, 네임 스페이스의 선언을 포함하고 있는지 Spring-aop, Spring-tx이 classpath에 있는지 확인하여야 한다.

### 테이블접두사 변경(Changing the Table Prefix)
JobRepository는 메타 데이터 테이블의 테이블 접두사 수정도 가능하다. 기본적으로 모든 데이터 테이블은 BATCH_JOB_EXECUTION 와 BATCH_STEP_EXECUTION 등과 같이 BATCH_로 시작한다.하지만 테이블명 앞에 스키마명을 추가하거나, 같은 스키마 내에서 메타 데이터 테이블의 하나 이상의 세트가 필요하면 테이블 접두사 수정이 필요하다.

```xml
<job-repository id="jobRepository"
                table-prefix="SYSTEM.TEST_" />
```

위와 같이 설정한다면 모든 쿼리에 메타 데이터 테이블명이 SYSTEM.TEST_”로 시작된다. BATCH_JOB_EXECUTION은 SYSTEM.TEST_JOB_EXECUTION으로 변경될 것이다.

✔오직 테이블의 접두사만 변경가능하다. 테이블명과 컬럼명은 수정할 수 없다.

### 메모리 Repository(In-Memory Repository)
Spring 배치는 jobRepository를 데이터베이스가 아닌 메모리로 설정할 수 있다. 작업에 대한 상태를 유지하지 않아도 되는 배치작업의 도메인 개체를 데이터 베이스에 저장할 경우, 각각의 커밋 시점에 추가 시간이 걸린다. 이 경우, 메모리 Repository를 통해 잡을 실행한다.

```xml
<bean id="jobRepository" 
  class="org.springframework.batch.core.repository.support.MapJobRepositoryFactoryBean">
    <property name="transactionManager" ref="transactionManager"/>
</bean>
```

메모리는 JVM 인스턴스가 다시 시작하는 것을 허용하지 않으며, 휘발성을 가진 jobRepository이다. 또한 동일한 매개 변수 두 작업 인스턴스가 동시에 실행되는 것을 보장 할 수 없다. multi-threaded 배치작업이나 파티션 작업에 적합하지 않을 수 있다.그러므로 JobRepository는 데이터베이스을 사용하여야 한다.

하지만 repository내에서 rollback이 있으므로 트랜잭션 manager의 설정이 필요하다.그리고 테스트를 위해 많은 사람들이 비즈니스 논리상 여전히 트랜잭션이 있기 때문에 ResourcelessTransactionManager가 유용하다.

### 비표준 데이터 베이스 타입(Non-standard Database Types in a Repository)
Spring Batch에서 지원되는 데이터베이스 목록이외의 데이터베이스를 사용하는 경우,비슷하게 지원하는 하는 데이터베이스가 있다면 그것을 사용할 수 있다. 이 작업을 수행하려면 네임 스페이스 사용하는 대신에 JobRepositoryFactoryBean를 사용하여 가장 가깝게 일치하는 데이터베이스 유형을 설정 할 수 있다

- Spring Batch에서 지원되는 데이터베이스 타입 : DERBY, DB2, DB2ZOS, HSQL, SQLSERVER, MYSQL, ORACLE, POSTGRES, SYBASE, H2

```xml
<bean id="jobRepository" class="org.springframework.batch.core.repository.support.JobRepositoryFactoryBean">
    <property name="databaseType" value="db2"/>
    <property name="dataSource" ref="dataSource"/>
</bean>
```

주의

✔ **altibase**나 **tibero**는 지원되는 데이터베이스 타입이 아니다. altibase나 tibero 연결시에는 jobRepository에 databaseType으로 oracle을 추가 설정해야 한다.

```xml
<bean id="jobRepository"
		class="org.springframework.batch.core.repository.support.JobRepositoryFactoryBean"
		p:dataSource-ref="dataSource" p:databaseType="oracle" p:transactionManager-ref="transactionManager" p:lobHandler-ref="lobHandler"/>
```

## 참고자료
- JobRepository :http://static.springsource.org/spring-batch/reference/html/configureJob.html#configuringJobRepository
- [declarative_transaction_management](../persistence-layer/transaction-declarative-transaction-management.md)
- Meta-Data Schema :http://static.springsource.org/spring-batch/reference/html/metaDataSchema.html
