---
title: 배치 Runner 예제
linkTitle: Runner
description: 배치 수행에 사용되는 EgovBatchRunner의 사용법을 보여주는 예제이다. 비동기 방식으로 실행하는 Job의 시작, 정지, 재시작 방법을 보여준다.
url: /runtime-example/individual-example/batch-layer/batch-example-batch_runner/
menu:
    depth:
        name: Runner
        weight: 2
        parent: "batchLayer"
---
# 배치 Runner 예제

## 개요

배치 수행에 사용되는 EgovBatchRunner의 사용법을 보여주는 예제이다. 비동기 방식으로 실행하는 Job의 시작, 정지, 재시작 방법을 보여준다.

## 설명

### 설정

#### EgovBatchRunner 설정

EgovBatchRunner의 설정 방법은 [배치 Runner](../../../egovframe-runtime/batch-layer/batch-execution-job_runner.md#egovbatchrunner)를 참고한다.

#### Launcher 설정

**배치 Runner 예제의 Job 설정 파일인 batchRunnerTest.xml을 확인한다.**

본 예제에서는 비동기 방식으로 Job을 수행한다. 이를 위해 JobLauncher의 TaskExecutor에 SimpleAsyncTaskExecutor 클래스를 지정한다.

```xml
<bean id="jobLauncher" class="org.springframework.batch.core.launch.support.SimpleJobLauncher">
	<property name="jobRepository" ref="jobRepository" />
	<property name="taskExecutor">
		<bean class="org.springframework.core.task.SimpleAsyncTaskExecutor"/>
	</property>
</bean>
```

#### Job 설정

**배치 Runner 예제의 Job 설정 파일인 batchRunnerTest.xml을 확인한다.**

✔ Job 재시작시, Job 시작에 사용되었던 JobParameter를 사용하기 위해 JobParametersIncrementer를 이용한다.  
✔ batchRunnerTestJob에서 JobParametersIncrementer 클래스를 사용하기 위해 simpleJob을 상속받는다. 이때 simpleJob은 restartable이 true로 설정된다.  
✔ Step도 simpleStep을 상속받아서 구현한다.  

```xml
<bean id="simpleJob" class="org.springframework.batch.core.job.SimpleJob" abstract="true">
	<property name="jobRepository" ref="jobRepository" />
	<property name="restartable" value="true" />
</bean>
 
<bean id="simpleStep" class="org.springframework.batch.core.step.item.FaultTolerantStepFactoryBean" abstract="true">
	<property name="transactionManager" ref="transactionManager" />
	<property name="jobRepository" ref="jobRepository" />
</bean>
 
<bean id="batchRunnerTestJob" parent="simpleJob">
	<property name="jobParametersIncrementer">
		<bean class="org.springframework.batch.core.launch.support.RunIdIncrementer" />	
	</property>
	<property name="steps">
		<bean id="infiniteStep" parent="simpleStep">
			<property name="itemReader">
				<bean id="reader" class="egovframework.brte.sample.common.domain.trade.GeneratingTradeItemReader">
					<property name="limit" value="1000000" />
				</bean>
			</property>
			<property name="itemWriter">
				<bean id="writer" class="egovframework.brte.sample.example.support.EgovDummyItemWriter" />
			</property>
		</bean>
	</property>
</bean>
```

### JunitTest 구성 및 수행

#### JunitTest 구성

**배치 Runner 설정과 관련 클래스들로 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.**

배치 실행 순서는 아래와 같다.

1. EgovBatchRunner의 start() 메소드에 Job의 이름, JobParameter를 전달하여 batchRunnerTestJob을 시작하고, executionId를 얻어온다.
2. executionId를 이용하여 실행 중인 Job의 이름, JobParameter가 일치하는지 확인한다.
3. stopAndCheckStatus()를 이용하여 실행 중인 Job을 정지한다.
4. EgovBatchRunner의 restart() 메소드에 처음 시작했던 Job의 executionId를 전달하여 batchRunnerTestJob을 재시작 한다.
5. 다시 한 번 stopAndCheckStatus()를 이용하여 실행 중인 Job을 정지한다.

```java
	@Test
	public void testStartStopResumeJob() throws Exception {
 
		String jobName = "batchRunnerTestJob";
		String jobParameters = egovBatchRunner.createUniqueJobParameters();
 
		long executionId = egovBatchRunner.start(jobName, jobParameters);
 
		assertEquals(jobName, egovBatchRunner.getJobInstance(executionId).getJobName());
		assertEquals(jobParameters.toString(), egovBatchRunner.getJobOperator().getParameters(executionId));
		stopAndCheckStatus(executionId);
 
		long resumedExecutionId = egovBatchRunner.restart(executionId);
		assertEquals(jobParameters.toString(), egovBatchRunner.getJobOperator().getParameters(resumedExecutionId));
		stopAndCheckStatus(resumedExecutionId);
 
	}
```

stopAndCheckStatus() 메소드는 Job 실행 정보를 확인하고 실행 중인 Job을 정지하는 역할을 한다.

1. 비동기 실행 중인 Job이 시작 상태로 들어갔는지 보장하기 위해, Thread.sleep()을 이용하여 1초간 대기한다.
2. 실행 정보를 확인하고, EgovBatchRunner의 stop() 메소드를 이용하여 실행 중인 Job을 정지한다.
3. 실행 중인 Job의 excutionId가 존재하는지 확인하고 0.1초간 대기한다.
4. 대기 후, 해당 Job의 Summary를 출력하고, BatchStatus가 Stopped 인지 확인한다.

```java
	private void stopAndCheckStatus(long executionId) throws Exception {
		String jobName = egovBatchRunner.getJobInstance(executionId).getJobName();
 
		// wait to the job to get up and running	
		Thread.sleep(1000);
 
		Set<Long> runningExecutions = egovBatchRunner.getJobOperator().getRunningExecutions(jobName);
		assertTrue("Wrong executions: " + runningExecutions + " expected: " + executionId, runningExecutions
				.contains(executionId));
		assertTrue("Wrong summary: " + egovBatchRunner.getJobOperator().getSummary(executionId), 
				egovBatchRunner.getJobOperator().getSummary(executionId).contains(BatchStatus.STARTED.toString()));
 
		egovBatchRunner.getJobOperator().stop(executionId);
 
		int count = 0;
		while (egovBatchRunner.getJobOperator().getRunningExecutions(jobName).contains(executionId) && count <= 10) {
			logger.info("Checking for running JobExecution: count=" + count);
			Thread.sleep(100);
			count++;
		}
 
		runningExecutions = egovBatchRunner.getJobOperator().getRunningExecutions(jobName);
		assertFalse("Wrong executions: " + runningExecutions + " expected: " + executionId, runningExecutions
				.contains(executionId));
		assertTrue("Wrong summary: " + egovBatchRunner.getJobOperator().getSummary(executionId), 
				egovBatchRunner.getJobOperator().getSummary(executionId).contains(BatchStatus.STOPPED.toString()));
 
		// there is just a single step in the test job
		Map<Long, String> summaries = egovBatchRunner.getJobOperator().getStepExecutionSummaries(executionId);
		System.err.println(summaries);
		assertTrue(summaries.values().toString().contains(BatchStatus.STOPPED.toString()));
	}
```

#### JunitTest 수행

수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.

### 결과확인

Console 창에서 Job Summary내용 중, BatchStatus가 Stopped 임을 확인한다.

![centercut-explain1](./images/centercut-explain1.png)

## 참고자료
* [Batch Runner](../../../egovframe-runtime/batch-layer/batch-execution-job_runner.md#egovbatchrunner)