---
title: 단순처리(Tasklet) 예제
linkTitle: Tasklet
description: 배치 수행 시, Job의 실행중 itemReader와 ItemWriter 등의 인터페이스 사용이 필요없는 단순처리되는 작업(파일이동 등)을 보여주는 예제이다.
url: /runtime-example/individual-example/batch-layer/batch-example-tasklet_mgmt/
menu:
    depth:
        name: Tasklet
        weight: 10
        parent: "batchLayer"
---
# 단순처리(Tasklet) 예제

## 개요

배치 수행 시, Job의 실행중 itemReader와 ItemWriter 등의 인터페이스 사용이 필요없는 단순처리되는 작업(파일이동 등)을 보여주는 예제이다.

## 설명

### 설정

#### Job 설정

**단순처리(Tasklet) 예제의 Job 설정 파일인 taskletJob.xml 을 확인한다.**

Job 의 구성을 보면 다른 Job과 달리 Chunk 설정이 없고, \<tasklet>에서 참조하는 adapter 빈에서 jobParameters로 설정된 값을 targetObject 프로퍼티 값으로 넘겨주는 것을 확인할 수 있다.

```xml
<job id="loopJob" xmlns="http://www.springframework.org/schema/batch">
	<step id="step1">
		<tasklet ref="adapter">
			<transaction-attributes propagation="REQUIRED"/>
		</tasklet>
	</step>
</job>
 
<bean id="adapter" class="org.springframework.batch.core.step.tasklet.MethodInvokingTaskletAdapter">
	<property name="targetObject" ref="value" />
	<property name="targetMethod" value="execute" />
</bean>
 
<bean id="value" class="egovframework.brte.sample.example.test.EgovTaskletJobFunctionalTests$TestBean" scope="step">
	<property name="value" value="#{jobParameters[value]}" />
</bean>
```

### JunitTest 구성 및 수행

#### JunitTest 구성

**taskletJob 설정과 관련 클래스들로 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.**

✔ JunitTest 클래스의 구조는 [배치실행환경 예제 Junit Test 설명](./batch-example-run_junit_test.md)을 참고한다.   
✔ assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus()): 배치수행결과가 COMPLETED 인지 확인한다.  
✔ TestBean 클래스의 assertEquals(“foo”, value) : jobParameter에 value 로 저장한 “foo” 와 문자열 “foo” 가 같은지 판단한다. (jobParameter로 넣어준 값이 사용자가 지정한 값과 같은지 단순비교)  

```java
@ContextConfiguration(locations = { "/egovframework/batch/simple-job-launcher-context.xml", 
			"/egovframework/batch/jobs/taskletJob.xml",
			"/egovframework/batch/job-runner-context.xml" })
public class EgovTaskletJobFunctionalTests {
	...
	@Test
	public void testLaunchJob() throws Exception {
		JobExecution jobExecution = jobLauncherTestUtils.launchJob(new JobParametersBuilder().addString("value", "foo")
					.addParameter( "timestamp", new JobParameter(new Date().getTime())).toJobParameters());
		assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus());
	}
	public static class TestBean {
		//String value
		private String value;
 
       		public void setValue(String value) {
			this.value = value;
		}
 
		public void execute() {
			assertEquals("foo", value);
		}
	}
}
```

#### JunitTest 수행

수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.


## 참고자로

- [TaskletStep](../../egovframe-runtime/batch-layer/batch-core-step-#taskletstep)

