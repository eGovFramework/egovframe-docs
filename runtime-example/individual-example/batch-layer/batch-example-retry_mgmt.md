---
title: 재시도(Retry) 예제
linkTitle: Retry
description: 배치 수행 시, 데이터를 처리하는 과정에서 실패한 데이터처리를 재시도하는 과정을 보여주는 예제이다. EgovRetrySampleFunctionalTests 예제는 ItemProcessing, ItemWriting 에서 발생한 예외상황에 대해 정해진 설정대로 Retry를 수행하는 과정을 보여준다. 설정된 retry-limit 만큼 재시도를 허용함으로써 Job 전체의 실패를 줄일 수 있다.
url: /runtime-example/individual-example/batch-layer/batch-example-retry_mgmt/
menu:
    depth:
        name: Retry
        weight: 7
        parent: "batchLayer"
---
# 재시도(Retry) 예제

## 개요
배치 수행 시, 데이터를 처리하는 과정에서 실패한 데이터처리를 재시도하는 과정을 보여주는 예제이다. EgovRetrySampleFunctionalTests 예제는 ItemProcessing, ItemWriting 에서 발생한 예외상황에 대해 정해진 설정대로 Retry를 수행하는 과정을 보여준다. 설정된 retry-limit 만큼 재시도를 허용함으로써 Job 전체의 실패를 줄일 수 있다.

## 설명
### 설정
#### Job 설정
<b>재시도(Retry) 예제의 Job 설정 파일인 retrySample.xml을 확인한다.</b>

Job 의 구성을 보면 Chunk 설정에 아래와 같은 설정이 있다.
- retry-limit : Retry 할 수 있는 최대 횟수를 지정한다.
- \<retryable-exception-classes\> : Exception 범위를 지정한다. Rollback을 유발하므로, 너무 많은 retry 는 성능저하를 주의해야 한다.

```
  <include> : retry 해야하는 Exception 지정
  <exlclude> : include로 지정한 exception의 하위 exception 중, retry 하지 않을 Exception 지정
```

```xml
<job id="retrySample" xmlns="http://www.springframework.org/schema/batch">
	<step id="step1">
		<tasklet>
			<chunk reader="itemGenerator" writer="itemWriter" 
		               commit-interval="1" retry-limit="3">
			    <retryable-exception-classes>
			    	<include class="java.lang.Exception"/>
			    </retryable-exception-classes>
			</chunk>
		</tasklet>
	</step>
</job>
```

### JunitTest 구성 및 수행
#### JunitTest 구성
<b>retrySample 설정과 관련 클래스들로 Junit Test를 수행한다. 이 때 배치가 수행되고, 관련된 내용을 확인할 수 있다.</b>

✔ JunitTest 클래스의 구조는 [배치실행환경 예제 Junit Test 설명](./batch-example-run_junit_test.md)을 참고한다.

✔ assertEquals(itemGenerator.getLimit()+2, itemProcessor.getCounter()) : 두 번의 재시도가 일어나도록 설정되어 있으므로, 전체 Process 처리 수가 reader에서 읽힌 데이터 수보다 2가 커야한다.

```java
@ContextConfiguration(locations = { "/egovframework/batch/simple-job-launcher-context.xml", 
		"/egovframework/batch/job-runner-context.xml",
		"/egovframework/batch/jobs/retrySample.xml"})
public class EgovRetrySampleFunctionalTests {
 
	@Test
	public void testLaunchJob() throws Exception {
		jobLauncherTestUtils.launchJob();
		//items processed = items read + 2 exceptions
		assertEquals(itemGenerator.getLimit()+2, itemProcessor.getCounter());
	}
}
```

#### JunitTest 수행
수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.

## 참고자료
- [Retry](../../../egovframe-runtime/batch-layer/batch-core-skip_repeat_retry.md)