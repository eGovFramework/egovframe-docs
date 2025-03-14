---
title: 대용량 처리를 위한 멀티스레드 기반의 병행처리 예제
linkTitle: MultiProcess
description: 배치 수행 시, 대용량 처리를 위해 Job을 멀티스레드 기반으로 병행처리하는 과정을 보여준다. 실행 유형별로 멀티쓰레드 방식, Parallel 방식, 파티셔닝 방식 등이 있다.
url: /runtime-example/individual-example/batch-layer/batch-example-multi_process/
menu:
  depth:
    name: MultiProcess
    weight: 12
    parent: "batchLayer"
    identifier: "multiProcess"
---
# 대용량 처리를 위한 멀티스레드 기반의 병행처리 예제

## 개요

배치 수행 시, 대용량 처리를 위해 Job을 멀티스레드 기반으로 병행처리하는 과정을 보여준다. 실행 유형별로 멀티쓰레드 방식, Parallel 방식, 파티셔닝 방식 등이 있다.

## 설명

### 멀티쓰레드(Multi-threaded Step) 예제

병행처리멀티스레드(Multi-threaded Step)은 하나의 step을 멀티쓰레드로 처리하는 방식이다. chunk단위로 각 쓰레드에서 병행으로 처리한다.

#### Job설정

**병행처리멀티스레드 예제의 Job 설정파일인 parallelJob.xml을 확인한다.**

멀티스레드 처리를 원하는 step의 tasklet에 비동기 설정을 한다.

```xml
<job id="parallelJob" xmlns="http://www.springframework.org/schema/batch">
	<step id="staging" next="loading">
		<tasklet>
			<chunk reader="fileItemReader" processor="validatingProcessor" writer="stagingItemWriter" commit-interval="2"/>
		</tasklet>
	</step>
	<step id="loading">
		<tasklet task-executor="taskExecutor">
			<chunk reader="stagingReader" processor="stagingProcessor" writer="tradeWriter" commit-interval="3"/>
		</tasklet>
	</step>
</job>
 
<bean id="taskExecutor" class="org.springframework.core.task.SimpleAsyncTaskExecutor" />
```

#### JunitTest 구성 및 수행

##### JunitTest 구성

병행처리멀티스레드 설정과 관련 클래스들로 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.  

✔ JunitTest 클래스의 구조는 [배치실행환경 예제 Junit Test 설명](./batch-example-run_junit_test.md)을 참고한다.  
✔ assertEquals(BatchStatus.COMPLETED, execution.getStatus()) : 배치수행결과가 COMPLETED 인지 확인한다.  
✔ assertEquals(after - before, execution.getStepExecutions().iterator().next().getReadCount()) : BATCH_STAGING의 data와 stepexcution의 결과를 비교하여 staging의 step의 결과를 확인한다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = { "/egovframework/batch/simple-job-launcher-context.xml", "/egovframework/batch/jobs/parallelJob.xml",
		"/egovframework/batch/job-runner-context.xml"  })
public class EgovParallelJobFunctionalTests {
 
	//배치작업을  test하기 위한 JobLauncherTestUtils
	@Autowired
	private JobLauncherTestUtils jobLauncherTestUtils;
 
	//DB 사용을 위한  SimpleJdbcTemplate
	private SimpleJdbcTemplate jdbcTemplate;
 
	...
 
	@Test
	public void testLaunchJob() throws Exception {
		int before = SimpleJdbcTestUtils.countRowsInTable(jdbcTemplate, "BATCH_STAGING");
		JobExecution execution = jobLauncherTestUtils.launchJob();
		int after = SimpleJdbcTestUtils.countRowsInTable(jdbcTemplate, "BATCH_STAGING");
		assertEquals(BatchStatus.COMPLETED, execution.getStatus());
		assertEquals(after - before, execution.getStepExecutions().iterator().next().getReadCount());
	}
 
}
```

##### JunitTest 수행

수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.

#### 결과확인

**멀티쓰레드로 병행처리한 setp은 쓰레드마다의 처리 속도차이에 의해 순차적인 처리가 되지 않는다. loading의 step 결과인 TRADE의 data를 보면 확인할 수 있다.**

![multithread-data](./images/multithread-data.png)

### Parallel 예제

parallelStep이란 분리된 flow을 각 thread에서 병행으로 처리하는 방식이다. 두 개의 flow1, flow2 는 각각 thread에서 병행으로 처리된다.

#### Job설정

**ParallelStep 예제의 Job 설정파일인 parallelStep.xml을 확인한다.**

✔ split 태그에 비동기 설정이 있어야 병행처리가 가능하다.

```xml
<job id="parallelStep" xmlns="http://www.springframework.org/schema/batch">
	<split id="split1" task-executor="taskExecutor" next="step4">
		<flow>
			<step id="step1" next="step2">
				<tasklet>
					<chunk reader="itemReader" writer="itemWriter1" commit-interval="1" />
				</tasklet>
			</step>
			<step id="step2">
				<tasklet>
					<chunk reader="itemReader" writer="itemWriter2" commit-interval="2" />
				</tasklet>
			</step>
		</flow>
		<flow>
			<step id="step3">
				<tasklet>
					<chunk reader="itemReader" writer="itemWriter3" commit-interval="2" />
				</tasklet>
			</step>
		</flow>
	</split>
        <step id="step4">
		<tasklet>
			<chunk reader="itemReader" writer="itemWriter4" commit-interval="2" />
		</tasklet>
	</step>
</job>
 
<bean id="taskExecutor" class="org.springframework.core.task.SimpleAsyncTaskExecutor" />
```

#### JunitTest 구성 및 수행

##### JunitTest 구성

parallelstep 설정과 관련 클래스들로 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.  
✔ JunitTest 클래스의 구조는 [배치실행환경 예제 Junit Test 설명](./batch-example-run_junit_test.md)을 참고한다.  
✔ assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus()): 배치수행결과가 COMPLETED 인지 확인한다.  
✔ getUniqueJobParameters에서 JobParameter에 배치에 필요한 입력 리소스, 출력 리소스 위치정보를 넘긴다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations ={"/egovframework/batch/simple-job-launcher-context.xml", "/egovframework/batch/jobs/parallelStep.xml","/egovframework/batch/job-runner-context.xml"})
public class EgovParallelStepFunctionalTests{
 
	//배치작업을  test하기 위한 JobLauncherTestUtils
	@Autowired
	private JobLauncherTestUtils jobLauncherTestUtils;
 
	/**
	 * 배치작업 테스트
	 */
	@Test
	public void testLaunchJob() throws Exception {
		JobExecution jobExecution = jobLauncherTestUtils.launchJob(this.getUniqueJobParameters());
		assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus());
		// /target/test-outputs/parallelStep폴더의 output파일 확인
	}
 
	/**
     * 잡파라미터를 설정하기 위한 메소드 
     * @return jobParameters
     */
	protected JobParameters getUniqueJobParameters() {
		return new JobParametersBuilder().addString("inputFile","/egovframework/data/input/delimited.csv")
		.addString("outputFile1","file:./target/test-outputs/parallelStep/delimitedOutput1.csv")
		.addString("outputFile2","file:./target/test-outputs/parallelStep/delimitedOutput2.csv")
		.addString("outputFile3","file:./target/test-outputs/parallelStep/delimitedOutput3.csv")
		.addString("outputFile4","file:./target/test-outputs/parallelStep/delimitedOutput4.csv")
		.addParameter("timestamp", new JobParameter(new Date().getTime())).toJobParameters();
	}
}
```

##### JunitTest 수행

수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.

#### 결과확인

split된 두 개의 flow가 멀티쓰레드(SimpleAsyncTaskExecutor-1,SimpleAsyncTaskExecutor-2)로 실행한 결과는 콘솔창의 로그내용으로 확인할 수 있다. step1과 step3은 서로 다른 쓰레드에서 실행한 사실을 확인할 수 있다.

![parallelstep-step1](./images/parallelstep-step1.png)

...

![parallelstep-step3](./images/parallelstep-step3.png)

### 파티셔닝(Partitioning) 예제

파티션 정의 File, DB의 데이터를 처리하는 병행처리 방법의 하나로 File 데이터, DB 데이터를 Partition 하여 멀티쓰레드 방식으로 처리한다. 입력리소스에 따라 DB 파티셔닝예제와 과 File 파티셔닝예제를 보여주고, 여러리소스를 읽어 하나의 타켓파일에 쓰는 SingleFile 파티셔닝 예제를 보여준다.

| 입력 리소스 타입 | 관계  | 예제                                                           |   
|-----------|-----|--------------------------------------------------------------|
| DB        |     | [DB Partition 예제](./batch-example-db_partition.md)           |
| File      | N:N | [N:N Partition 예제](./batch-example-file_partition.md)        |
| File      | N:1 | [N:1 Partition 예제](./batch-example-single_file_partition.md) |

## 참고자료

* [병행처리](../../../egovframe-runtime/batch-layer/batch-core-parallel_process.md)