---
title: JobExplorer
linkTitle: JobExplorer
description: JobExplorer는 실행 중인 Job 및 Step을 검색하기 위한 시작지점으로서, Repository에 접근하여 배치 메타데이터를 조회한다. JobRepository의 읽기 전용 버전이다.
url: /egovframe-runtime/batch-layer/batch-core-job_explorer/
menu:
    depth:
        name: JobExplorer
        weight: 11
        parent: "batch-layer"
---
# JobExplorer

본 문서는 [Spring Batch 5.2 - Advanced Metadata Usage (Querying the Repository)](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html#queryingRepository)와 정합성을 유지한다.

## 개요

고급 메타데이터 기능을 쓰기 전에, 기존 실행(execution) 정보를 **조회**할 수 있어야 한다. 이 역할을 하는 것이 `JobExplorer` 인터페이스이다. 메서드 시그니처만 보아도 `JobExplorer`는 `JobRepository`의 **읽기 전용** 버전이며, `JobRepository`와 마찬가지로 팩토리 빈으로 쉽게 설정할 수 있다.

## JobExplorer 인터페이스

```java
public interface JobExplorer {

    List<JobInstance> getJobInstances(String jobName, int start, int count);

    JobExecution getJobExecution(Long executionId);

    StepExecution getStepExecution(Long jobExecutionId, Long stepExecutionId);

    JobInstance getJobInstance(Long instanceId);

    List<JobExecution> getJobExecutions(JobInstance jobInstance);

    Set<JobExecution> findRunningJobExecutions(String jobName);
}
```

| 메서드 | 설명 |
|--------|------|
| `getJobInstances(String jobName, int start, int count)` | Job 이름별 JobInstance 목록을 페이징 조회 |
| `getJobExecution(Long executionId)` | 실행 ID로 JobExecution 조회 |
| `getStepExecution(Long jobExecutionId, Long stepExecutionId)` | Job 실행 ID와 Step 실행 ID로 StepExecution 조회 |
| `getJobInstance(Long instanceId)` | JobInstance ID로 JobInstance 조회 |
| `getJobExecutions(JobInstance jobInstance)` | 특정 JobInstance의 모든 JobExecution 목록 조회 |
| `findRunningJobExecutions(String jobName)` | 해당 Job 이름으로 **실행 중인** JobExecution 집합 조회 |

## 설정

### Java 설정

`DefaultBatchConfiguration`을 상속한 설정 클래스에서 `JobExplorer` 빈을 정의한다. `@EnableBatchProcessing` 사용 시 필요한 인프라 빈이 제공되므로, DataSource만 설정하면 된다.

```java
@Bean
public JobExplorer jobExplorer() throws Exception {
    JobExplorerFactoryBean factoryBean = new JobExplorerFactoryBean();
    factoryBean.setDataSource(this.dataSource);
    return factoryBean.getObject();
}
```

`JobRepository`에 테이블 접두어를 사용하는 경우, `JobExplorer`도 동일한 접두어를 사용해야 같은 메타데이터 테이블을 참조한다.

```java
@Bean
public JobExplorer jobExplorer() throws Exception {
    JobExplorerFactoryBean factoryBean = new JobExplorerFactoryBean();
    factoryBean.setDataSource(this.dataSource);
    factoryBean.setTablePrefix("SYSTEM.");
    return factoryBean.getObject();
}
```

### XML 설정

```xml
<bean id="jobExplorer" class="org.springframework.batch.core.explore.support.JobExplorerFactoryBean"
      p:dataSource-ref="dataSource" />
```

테이블 접두어를 지정할 때:

```xml
<bean id="jobExplorer" class="org.springframework.batch.core.explore.support.JobExplorerFactoryBean"
      p:dataSource-ref="dataSource"
      p:tablePrefix="SYSTEM." />
```

> `JobRepository`에서 테이블 접두어를 바꾼 경우, `JobExplorer`에도 같은 접두어를 설정해야 한다. 두 컴포넌트가 동일한 배치 메타데이터 테이블을 사용하기 때문이다.

## JobOperator와의 관계

`JobExplorer`는 읽기 전용 조회용으로 쓰이고, **JobOperator**는 이 메타데이터를 활용해 Job 시작·재시작·정지·요약 등 제어 및 모니터링 작업을 수행한다. `SimpleJobOperator`는 내부적으로 `JobExplorer`를 사용한다. 자세한 내용은 [JobOperator](./batch-core-job_operator.md)를 참고한다.

## 참고 문서

- [Spring Batch 5.2 - Advanced Metadata Usage](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html)
- [Spring Batch 5.2 - Querying the Repository](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html#queryingRepository)
- [JobOperator](./batch-core-job_operator.md)
