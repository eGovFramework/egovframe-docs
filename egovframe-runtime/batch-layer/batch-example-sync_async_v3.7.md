---
title: 동기/비동기 처리 예제
linkTitle: Ex-SyncAsync
description: 일괄(배치)처리 작업 수행 시, 작업처리가 종료될 때까지 대기하는 동기방식 처리와 작업처리의 종료를 Callback매커니즘을 이용하여 전달받는 비동기처리에 대한 예제를 보여준다.
url: /egovframe-runtime/batch-layer/batch-example-sync_async_v3.7/
menu:
    depth:
        name: 동기/비동기 처리 예제
        weight: 16
        parent: "batch-layer"
---
# 동기/비동기 처리 예제

## 개요

일괄(배치)처리 작업 수행 시, 작업처리가 종료될 때까지 대기하는 동기방식 처리와 작업처리의 종료를 Callback매커니즘을 이용하여 전달받는 비동기처리에 대한 예제를 보여준다.

## 설명

### 설정

#### Launcher 설정

##### 동기/비동기 처리 예제의 Launcher 설정파일인 skipSample-job-launcher-context.xml 을 확인한다.

Job 수행시, 동기와 비동기 방식으로 데이터를 처리할 수 있으며, 이 예제에서는 동기 처리가 기본값으로 설정되어 있다. 설정위치는 Launcher 설정파일의 jobLauncher 빈에서 taskExecutor 프로퍼티이며, 참조하는 값으로 다음 두 가지를 설정할 수 있다.

- sync : 동기처리시 사용할 클래스 설정
- async : 비동기처리시 사용할 클래스 설정

```xml
<bean id="jobLauncher" class="org.springframework.batch.core.launch.support.SimpleJobLauncher">
	<property name="jobRepository" ref="jobRepository" />
	<property name="taskExecutor" ref="sync"/>  <!-- 비동기시 ref="async" -->
</bean>

<!-- 동기 처리시  sync -->
<bean id="sync" class="org.springframework.core.task.SyncTaskExecutor" />

<!-- 비동기  처리시 async -->
<bean id="async" class="org.springframework.core.task.SimpleAsyncTaskExecutor" />
```

#### Job 설정

##### 동기/비동기 처리 예제의 Job 설정 파일인 delegatingJob.xml을 확인한다.

동기/비동기 처리 예제를 위해 특별히 Job을 설정하는 내용은 없다. 이 예제에서 제공하는 Job의 상세 내용은 [기존 업무 재사용 예제](./batch-example-job-reuse.md)의 Job 설정과 같으므로 이를 참고한다.

```xml
<job id="delegateJob" xmlns="http://www.springframework.org/schema/batch">
	<step id="delegateStep1">
		<tasklet>
			<chunk reader="reader" writer="writer" commit-interval="3"/>
		</tasklet>
	</step>
</job>

<bean id="reader" class="org.springframework.batch.item.adapter.ItemReaderAdapter">
	<property name="targetObject" ref="delegateObject" />
	<property name="targetMethod" value="getData" />
</bean>

<bean id="writer" class="org.springframework.batch.item.adapter.PropertyExtractingDelegatingItemWriter">
	<property name="targetObject" ref="delegateObject" />
	<property name="targetMethod" value="processPerson" />
	<property name="fieldsUsedAsTargetMethodArguments">
		<list>
			<value>firstName</value>
			<value>address.city</value>
		</list>
	</property>
</bean>

<bean id="delegateObject" class="egovframework.brte.sample.common.domain.person.PersonService" />
```

### Async Item Processor 구성

Item Processor를 비동기 처리하기 위해 Spring Batch에서 AsyncItemProcessor 서비를 지원한다.  
AsyncItemProcessor 서비스를 이용한 설정은 아래와 같다.

```xml
<task:executor id="taskExecutor" pool-size="100"/>
<bean id="itemProcessorAsync" class="org.springframework.batch.integration.async.AsyncItemProcessor">
	<!-- delegate통해 실제 동작 할 Item Processor를 설정한다. -->
	<property name="delegate" ref="fixedLengthToFixedLengthJob.fixedLengthToFixedLengthStep.itemProcessor"/>
	<!-- Executor를 설정한다. -->	
	<property name="taskExecutor" ref="taskExecutor" />
</bean>
```

### JunitTest 구성 및 수행

#### JunitTest 구성

#### sync-job-launcher-context설정과 delegatingJob설정으로 구성된 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.

✔ JunitTest 클래스의 구조는 [배치실행환경 예제 Junit Test 설명](../../runtime-example/individual-example/batch-layer/batch-example-run-junit_test.md)을 참고한다.  
✔ assertEquals(“COMPLETED”, jobExecution.getExitStatus().getExitCode()) : 배치수행결과가 COMPLETED 인지 확인한다.  
✔ Thread.sleep(4000) : 비동기로 배치를 수행 시, DB에 배치상태(UNKNOWN)를 셋팅하고 DB연결이 종료되어 Job이 정상적으로 수행되더라도 종료상태(COMPLETED,FAILED)를 확인할 수 없다. 예제에서는 Job결과를 확인하기 위해 Thread를 적정시간동안 정지시켜 인위적으로 종료상태를 확인하도록 설정하였다.

```java
@ContextConfiguration(locations = { "/egovframework/batch/sync-job-launcher-context.xml", 
			"/egovframework/batch/jobs/delegatingJob.xml", 
			"/egovframework/batch/job-runner-context.xml" })
public class EgovSyncDelegatingJobFunctionalTests {
	...
	@Test
	public void testLaunchJob() throws Exception {
		JobExecution jobExecution=null;
		try{
			   jobExecution =jobLauncherTestUtils.launchJob();
			   //Async 로 수행되는 경우 Exit Status는 UNKNOWN으로 설정 됨
			   assertEquals("UNKNOWN", jobExecution.getExitStatus().getExitCode());
			   Thread.sleep(4000); 
 
		   }catch (InterruptedException ie){
			   ie.printStackTrace();
		   }
		 assertTrue(personService.getReturnedCount() > 0);
		 assertEquals(personService.getReturnedCount(), personService.getReceivedCount()) ;
		 assertEquals("COMPLETED", jobExecution.getExitStatus().getExitCode());	
	}
}
```

#### JunitTest 수행

##### AsyncItemWriter

수행방법은 [JunitTest 실행](https://www.egovframe.go.kr//wiki/doku.php?id=egovframework:dev2:tst:test_case#test_case_실행)을 참고한다.

## 참고자료

- [동기/비동기 예제](../../runtime-example/individual-example/batch-layer/batch-example-sync-async.md)
- [JobLauncher](./batch-execution-job-launcher.md)