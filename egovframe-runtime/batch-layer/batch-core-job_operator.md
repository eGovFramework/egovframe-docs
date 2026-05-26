---
title: JobOperator
linkTitle: JobOperator
description: JobOperator는 Job을 제어하는 모니터링 작업을 위해 사용된다. JobOperator는 JobRegistry, JobExplorer, JobLauncher, JobRepository 클래스의 설정이 필수적이며, Job의 InstanceId, ExecutionId, JobName을 이용하여 Job을 제어한다.
url: /egovframe-runtime/batch-layer/batch-core-job_operator/
menu:
    depth:
        name: JobOperator
        weight: 12
        parent: "batch-layer"
---
# JobOperator

본 문서는 [Spring Batch 5.2 - Advanced Metadata Usage (JobOperator)](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html#JobOperator)와 정합성을 유지한다.

## 개요

`JobRepository`는 메타데이터에 대한 CRUD 연산을, `JobExplorer`는 메타데이터에 대한 읽기 전용 연산을 제공한다. 이 연산들은 **Job 중지, 재시작, 요약** 같은 배치 운영자(batch operator)가 수행하는 일반적인 모니터링 작업을 함께 사용할 때 유용하다. Spring Batch는 이러한 기능을 `JobOperator` 인터페이스로 제공한다.

## JobOperator 인터페이스

`JobOperator`는 `JobLauncher`, `JobRepository`, `JobExplorer`, `JobRegistry` 등 여러 인터페이스의 메서드를 한데 모은 것이다. 제공 구현체인 `SimpleJobOperator`는 이에 필요한 의존성을 모두 주입받아 사용한다.

| 메서드 | 설명 |
|--------|------|
| `getExecutions(long instanceId)` | JobInstance의 실행 ID 목록 반환 |
| `getJobInstances(String jobName, int start, int count)` | Job 이름별 JobInstance ID 목록 조회 |
| `getRunningExecutions(String jobName)` | 실행 중인 Job의 Execution ID 집합 반환 |
| `getParameters(long executionId)` | 해당 실행의 JobParameters 문자열 반환 |
| `start(String jobName, String parameters)` | Job 시작 |
| `restart(long executionId)` | 실패한 실행 재시작 |
| `startNextInstance(String jobName)` | 동일 Job의 다음 JobInstance 시작 (JobParametersIncrementer 사용) |
| `stop(long executionId)` | 실행 중인 Job 정지 요청 |
| `getSummary(long executionId)` | 실행 요약 문자열 반환 |
| `getStepExecutionSummaries(long executionId)` | Step 실행 요약 맵 반환 |
| `getJobNames()` | 등록된 Job 이름 집합 반환 |

## 설정

### Java 설정

5.0부터 `@EnableBatchProcessing`을 사용하면 JobOperator 빈이 자동으로 등록된다. 직접 정의할 경우 다음처럼 `SimpleJobOperator`에 `JobExplorer`, `JobRepository`, `JobRegistry`, `JobLauncher`를 주입한다.

```java
/**
 * @EnableBatchProcessing 사용 시 필요한 의존성은 인프라에서 제공된다.
 */
@Bean
public SimpleJobOperator jobOperator(JobExplorer jobExplorer,
                                     JobRepository jobRepository,
                                     JobRegistry jobRegistry,
                                     JobLauncher jobLauncher) {
    SimpleJobOperator jobOperator = new SimpleJobOperator();
    jobOperator.setJobExplorer(jobExplorer);
    jobOperator.setJobRepository(jobRepository);
    jobOperator.setJobRegistry(jobRegistry);
    jobOperator.setJobLauncher(jobLauncher);
    return jobOperator;
}
```

### XML 설정

```xml
<bean id="jobOperator" class="org.springframework.batch.core.launch.support.SimpleJobOperator">
    <property name="jobExplorer">
        <bean class="org.springframework.batch.core.explore.support.JobExplorerFactoryBean">
            <property name="dataSource" ref="dataSource" />
        </bean>
    </property>
    <property name="jobRepository" ref="jobRepository" />
    <property name="jobRegistry" ref="jobRegistry" />
    <property name="jobLauncher" ref="jobLauncher" />
</bean>
```

> JobRepository에 테이블 접두어(table prefix)를 설정했다면, JobExplorer에도 동일한 접두어를 설정해야 한다.

## JobParametersIncrementer

`startNextInstance(String jobName)`은 항상 **새 JobInstance**로 Job을 시작한다. `JobExecution`에 문제가 있어 처음부터 다시 실행해야 할 때 유용하다. `JobLauncher`는 새 `JobParameters`로 새 `JobInstance`를 만들지만, `startNextInstance`는 Job에 연결된 `JobParametersIncrementer`를 사용해 “다음” 파라미터를 만들어 새 인스턴스를 시작한다.

```java
public interface JobParametersIncrementer {
    JobParameters getNext(JobParameters parameters);
}
```

예: `run.id`를 1씩 증가시키는 구현

```java
public class SampleIncrementer implements JobParametersIncrementer {

    @Override
    public JobParameters getNext(JobParameters parameters) {
        if (parameters == null || parameters.isEmpty()) {
            return new JobParametersBuilder().addLong("run.id", 1L).toJobParameters();
        }
        long id = parameters.getLong("run.id", 1L) + 1;
        return new JobParametersBuilder().addLong("run.id", id).toJobParameters();
    }
}
```

Job에 incrementer를 연결하려면:

- **Java**: `JobBuilder`의 `incrementer(sampleIncrementer())` 사용
- **XML**: `<job id="footballJob" incrementer="sampleIncrementer">` 처럼 `incrementer` 속성 지정

## Job 정지

실행 중인 Job을 정지할 때 `JobOperator`를 사용한다.

```java
Set<Long> executions = jobOperator.getRunningExecutions("sampleJob");
jobOperator.stop(executions.iterator().next());
```

프레임워크가 제어하지 않는 비즈니스 코드 내에서는 즉시 중단할 수 없으므로, 정지는 “요청”이며 완료 시점은 제어가 프레임워크로 돌아온 이후이다. 그 시점에 현재 `StepExecution`과 `JobExecution`의 상태가 `BatchStatus.STOPPED`로 저장된다.

## Job 중단(Abort)

- **FAILED**: 재시작 가능한 Job이면 `restart(long executionId)`로 재시작할 수 있다.
- **ABANDONED**: 프레임워크는 `ABANDONED` 상태의 Job 실행을 재시작하지 않는다. Step 실행을 “재시작 시 스킵”으로 표시할 때도 이 상태를 사용한다.

프로세스가 비정상 종료(`kill -9` 또는 서버 장애)된 경우, `JobRepository`는 실행이 끝났는지 알 수 없다. 이때는 수동으로 해당 실행을 **FAILED** 또는 **ABANDONED**로 변경해야 한다. 재시작할 계획이고 재시작 데이터가 유효할 때만 **FAILED**로 두고, 그렇지 않으면 **ABANDONED**로 변경하는 것이 일반적이다.

## 참고 문서

- [Spring Batch 5.2 - Advanced Metadata Usage](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html)
- [Spring Batch 5.2 - JobOperator](https://docs.spring.io/spring-batch/reference/5.2/job/advanced-meta-data.html#JobOperator)
- [JobExplorer](./batch-core-job_explorer.md)
