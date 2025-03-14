---
title: 배치실행환경 예제 JUnit Test 설명
linkTitle: JUnitTest
description: 배치실행환경 예제에서는 JUnit을 이용하여 배치를 수행하고 성공여부 판단 및 테스트 내용 확인을 한다. 초보 사용자의 이해를 돕기위해 예제에서 공통으로 사용하는 JUnitTest의 기본설정과 테스트 수행방법을 설명한다.
url: /runtime-example/individual-example/batch-layer/batch-example-run_junit_test/
menu:
    depth:
        name: JUnitTest
        weight: 24
        parent: "batchLayer"
---
# 배치실행환경 예제 JUnit Test 설명

## 개요
배치실행환경 예제에서는 JUnit을 이용하여 배치를 수행하고 성공여부 판단 및 테스트 내용 확인을 한다. 초보 사용자의 이해를 돕기위해 예제에서 공통으로 사용하는 JUnitTest의 기본설정과 테스트 수행방법을 설명한다.

## 설명
### 예제 JUnit Test 기본 구조
#### @ContextConfiguration

ContextConfiguration 은 컨텍스트를 얻어 그 내용을 참조하는 역할을 하며, 배치실행환경 예제에서는 배치수행에 필요한 설정파일들을 여기서 참조하도록 설정되어 있다.

✔ Launcher설정파일, Job설정파일, JobLauncherTestUtils를 사용하기 위한 별도의 설정파일(ex.job-runner-context.xml) 등이 명시된다.

```java
@ContextConfiguration(locations = { "/egovframework/batch/simple-job-launcher-context.xml", 
				"/egovframework/batch/jobs/parallelJob.xml",
				"/egovframework/batch/job-runner-context.xml" })
public class EgovParallelJobFunctionalTests {
	...
}
```

✔ 공통으로 사용되는 설정파일이 있을 경우, 다음과 같이 부모클래스에 담고 이를 상속받아 사용할 수 있다.

```
  부모클래스 : EgovAbstractIoSampleTests
  자식클래스 : EgovPreProcessorFunctionalTests
```

```java
@ContextConfiguration(locations = { "/egovframework/batch/simple-job-launcher-context.xml",
				"/egovframework/batch/job-runner-context.xml"})
public abstract class EgovAbstractIoSampleTests {
	...
}
```

```java
@ContextConfiguration(locations = { "/egovframework/batch/jobs/preProcessorJob.xml" })
public class EgovPreProcessorFunctionalTests extends 	EgovAbstractIoSampleTests {
	...
}
```

#### JobLauncherTestUtils
Spring 에서 제공하는 클래스로 배치수행에 필요한 메소드들이 포함되어 있다.

✔ JobLauncherTestUtils 클래스를 사용할 경우 ContextConfiguration 에서 job-runner-context.xml을 설정한다.

```java
@Autowired
private JobLauncherTestUtils jobLauncherTestUtils;
...
```

#### setDataSource(DataSource dataSource)
배치 수행 시, DB 연결을 위한 dataSource 정보를 셋팅하는 부분이다.

```java
// simpleJdbcTemplate 설정
private SimpleJdbcTemplate simpleJdbcTemplate;
// dataSource 설정
@Autowired
public void setDataSource(DataSource dataSource) {
	this.simpleJdbcTemplate = new SimpleJdbcTemplate(dataSource);
}
...
```

#### setUp()
예제에서 DB 관련한 데이터처리에 앞서 초기값을 셋팅하는 부분이다. 주로 테이블의 기존 내용을 Delete 하고 초기값을 Insert 한다.

```java
@Before
public void setUp() {
	simpleJdbcTemplate.update("DELETE from CUSTOMER");
 
	simpleJdbcTemplate.update("INSERT INTO CUSTOMER (ID, VERSION, NAME, CREDIT) VALUES  (1, 0, 'customer1', 100000)");
	simpleJdbcTemplate.update("INSERT INTO CUSTOMER (ID, VERSION, NAME, CREDIT) VALUES  (2, 0, 'customer2', 100000)");
	simpleJdbcTemplate.update("INSERT INTO CUSTOMER (ID, VERSION, NAME, CREDIT) VALUES  (3, 0, 'customer3', 100000)");
	simpleJdbcTemplate.update("INSERT INTO CUSTOMER (ID, VERSION, NAME, CREDIT) VALUES  (4, 0, 'customer4', 100000)");
}
```

#### @Test
배치를 실제로 수행하고, 테스트해야 하는 내용이 포함된 부분으로 예제별로 그 내용이 상이하다.

✔ 테스트 내용을 구성하는 방법은 참고차료를 활용한다.

```java
@Test
public void testUpdateCredit() throws Exception {
 
	// 배치 수행
	JobExecution jobExecution = jobLauncherTestUtils.launchJob(getUniqueJobParameters());
 
	// 테스트 내용 및 결과 확인
	assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus());
	assertEquals(inputs.size(), outputs.size());
}
```

### 예제 JUnit Test 수행 방법
#### JUnit 수행
수행방법은 [JunitTest 실행](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev2:tst:test_case)을 참고한다.

## 참고자료
- [Retry](../../../egovframe-runtime/batch-layer/batch-core-skip_repeat_retry.md)