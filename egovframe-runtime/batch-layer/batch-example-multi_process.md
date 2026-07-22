---
title: 대용량 처리를 위한 멀티스레드 기반 병행처리 예제
linkTitle: Ex-MultiProcess
description: 배치 작업을 멀티스레드, Parallel Step, 파티셔닝 방식으로 병행처리하는 설정과 JUnit 검증 방법을 예제로 설명한다.
url: /egovframe-runtime/batch-layer/batch-example-multi_process/
menu:
  depth:
    name: 대용량 병행처리 예제
    weight: 17
    parent: batch-layer
---

# 대용량 처리를 위한 멀티스레드 기반 병행처리 예제

## 개요

배치 수행 시 대용량 데이터를 빠르게 처리할 수 있도록 Job을 병행처리하는 예제를 설명한다. 실행 유형별로 멀티스레드 방식, Parallel Step 방식, 파티셔닝 방식이 있다.

> 이 문서는 전자정부 표준프레임워크 위키의 [대용량 처리를 위한 멀티스레드 기반의 병행처리 예제](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_example:multi_process)를 저장소 문서 형식으로 변환한 것이다.

## 멀티스레드(Multi-threaded Step) 예제

멀티스레드 방식은 하나의 Step을 여러 스레드가 Chunk 단위로 병행처리한다. 각 Chunk의 처리 순서는 보장되지 않으므로 Reader, Processor, Writer가 스레드 안전한지도 함께 확인해야 한다.

### Job 설정

멀티스레드로 처리할 Step의 `tasklet`에 `task-executor`를 지정한다.

`parallelJob.xml`:

```xml
<job id="parallelJob" xmlns="http://www.springframework.org/schema/batch">
    <step id="staging" next="loading">
        <tasklet>
            <chunk reader="fileItemReader"
                   processor="validatingProcessor"
                   writer="stagingItemWriter"
                   commit-interval="2" />
        </tasklet>
    </step>
    <step id="loading">
        <tasklet task-executor="taskExecutor">
            <chunk reader="stagingReader"
                   processor="stagingProcessor"
                   writer="tradeWriter"
                   commit-interval="3" />
        </tasklet>
    </step>
</job>

<bean id="taskExecutor"
      class="org.springframework.core.task.SimpleAsyncTaskExecutor" />
```

### JUnit 테스트

Job 실행 상태가 `COMPLETED`인지 확인하고, Step의 읽기 건수와 실제 적재 건수를 비교한다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {
    "/egovframework/batch/simple-job-launcher-context.xml",
    "/egovframework/batch/jobs/parallelJob.xml",
    "/egovframework/batch/job-runner-context.xml"
})
public class EgovParallelJobFunctionalTests {

    @Autowired
    private JobLauncherTestUtils jobLauncherTestUtils;

    private SimpleJdbcTemplate jdbcTemplate;

    @Test
    public void testLaunchJob() throws Exception {
        int before = SimpleJdbcTestUtils.countRowsInTable(
            jdbcTemplate, "BATCH_STAGING");

        JobExecution execution = jobLauncherTestUtils.launchJob();

        int after = SimpleJdbcTestUtils.countRowsInTable(
            jdbcTemplate, "BATCH_STAGING");

        assertEquals(BatchStatus.COMPLETED, execution.getStatus());
        assertEquals(
            after - before,
            execution.getStepExecutions().iterator().next().getReadCount());
    }
}
```

처리 결과는 `TRADE` 데이터와 StepExecution의 읽기 건수를 확인한다. 스레드별 처리 속도가 다르므로 입력 순서와 결과 순서가 같지 않을 수 있다.

## Parallel Step 예제

Parallel Step은 분리된 Flow를 각 스레드에서 병행처리한다. 다음 설정에서는 첫 번째 Flow의 `step1`·`step2`와 두 번째 Flow의 `step3`이 병행 실행되고, 두 Flow가 모두 끝난 뒤 `step4`가 실행된다.

### Job 설정

`parallelStep.xml`:

```xml
<job id="parallelStep" xmlns="http://www.springframework.org/schema/batch">
    <split id="split1" task-executor="taskExecutor" next="step4">
        <flow>
            <step id="step1" next="step2">
                <tasklet>
                    <chunk reader="itemReader"
                           writer="itemWriter1"
                           commit-interval="1" />
                </tasklet>
            </step>
            <step id="step2">
                <tasklet>
                    <chunk reader="itemReader"
                           writer="itemWriter2"
                           commit-interval="2" />
                </tasklet>
            </step>
        </flow>
        <flow>
            <step id="step3">
                <tasklet>
                    <chunk reader="itemReader"
                           writer="itemWriter3"
                           commit-interval="2" />
                </tasklet>
            </step>
        </flow>
    </split>
    <step id="step4">
        <tasklet>
            <chunk reader="itemReader"
                   writer="itemWriter4"
                   commit-interval="2" />
        </tasklet>
    </step>
</job>

<bean id="taskExecutor"
      class="org.springframework.core.task.SimpleAsyncTaskExecutor" />
```

### JUnit 테스트

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {
    "/egovframework/batch/simple-job-launcher-context.xml",
    "/egovframework/batch/jobs/parallelStep.xml",
    "/egovframework/batch/job-runner-context.xml"
})
public class EgovParallelStepFunctionalTests {

    @Autowired
    private JobLauncherTestUtils jobLauncherTestUtils;

    @Test
    public void testLaunchJob() throws Exception {
        JobExecution execution = jobLauncherTestUtils.launchJob(
            getUniqueJobParameters());

        assertEquals(BatchStatus.COMPLETED, execution.getStatus());
    }

    private JobParameters getUniqueJobParameters() {
        return new JobParametersBuilder()
            .addString("inputFile",
                "/egovframework/data/input/delimited.csv")
            .addString("outputFile1",
                "file:./target/test-outputs/parallelStep/delimitedOutput1.csv")
            .addString("outputFile2",
                "file:./target/test-outputs/parallelStep/delimitedOutput2.csv")
            .addString("outputFile3",
                "file:./target/test-outputs/parallelStep/delimitedOutput3.csv")
            .addString("outputFile4",
                "file:./target/test-outputs/parallelStep/delimitedOutput4.csv")
            .addLong("timestamp", System.currentTimeMillis())
            .toJobParameters();
    }
}
```

실행 로그에서 `step1`과 `step3`이 서로 다른 `SimpleAsyncTaskExecutor` 스레드에서 수행되는지 확인한다. 출력 파일은 `target/test-outputs/parallelStep` 디렉터리에서 확인할 수 있다.

## 파티셔닝(Partitioning) 예제

파티셔닝은 입력 데이터를 여러 파티션으로 나누고 각 파티션을 별도 StepExecution으로 실행하는 방식이다. 입력 리소스와 출력 구조에 따라 다음 예제를 참고한다.

| 입력 리소스 | 관계 | 예제 |
|---|---|---|
| DB | DB | [DB Partition 예제](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_example:db_partition) |
| File | N:N | [N:N Partition 예제](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_example:file_partition) |
| File | N:1 | [N:1 Partition 예제](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_example:single_file_partition) |

## 참고자료

- [병행처리](./batch-core-parallel_process.md)
- [Spring Batch Scaling and Parallel Processing](https://docs.spring.io/spring-batch/reference/scalability.html)
