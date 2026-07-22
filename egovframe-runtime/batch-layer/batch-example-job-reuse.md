---
title: 기존 업무 재사용 예제
linkTitle: Ex-JobReuse
description: 기존 서비스 메서드를 ItemReader와 ItemWriter로 연결하여 배치 작업에서 재사용하는 설정과 검증 방법을 설명한다.
url: /egovframe-runtime/batch-layer/batch-example-job-reuse/
menu:
    depth:
        name: 기존 업무 재사용 예제
        weight: 18
        parent: "batch-layer"
---
# 기존 업무 재사용 예제

## 개요

기존 업무 서비스를 배치의 `ItemReader` 또는 `ItemWriter`로 재사용하는 예제이다. Spring Batch가 제공하는 어댑터를 이용하면 별도의 배치 전용 클래스를 작성하지 않고 XML 설정만으로 기존 서비스 메서드를 Step에 연결할 수 있다.

이 문서는 [eGovFrame 공식 위키의 기존 업무 재사용 예제](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_example:job_reuse)를 저장소 문서 형식으로 정리한 것이다.

## 구성

예제는 기존 `PersonService`를 다음과 같이 재사용한다.

| 역할 | 어댑터 | 호출 메서드 |
|---|---|---|
| ItemReader | `ItemReaderAdapter` | `PersonService.getData()` |
| ItemWriter | `PropertyExtractingDelegatingItemWriter` | `PersonService.processPerson(...)` |

## Job 설정

기존 업무 재사용 예제의 Job 설정 파일인 `delegatingJob.xml`을 확인한다.

`reader`와 `writer`가 동일한 `delegateObject`를 참조한다. Writer는 `Person`의 `firstName`과 중첩 속성인 `address.city`를 추출해 `processPerson` 메서드의 인자로 전달한다.

```xml
<job id="delegateJob" xmlns="http://www.springframework.org/schema/batch">
    <step id="delegateStep1">
        <tasklet>
            <chunk reader="reader" writer="writer" commit-interval="3" />
        </tasklet>
    </step>
</job>

<bean id="reader"
      class="org.springframework.batch.item.adapter.ItemReaderAdapter">
    <property name="targetObject" ref="delegateObject" />
    <property name="targetMethod" value="getData" />
</bean>

<bean id="writer"
      class="org.springframework.batch.item.adapter.PropertyExtractingDelegatingItemWriter">
    <property name="targetObject" ref="delegateObject" />
    <property name="targetMethod" value="processPerson" />
    <property name="fieldsUsedAsTargetMethodArguments">
        <list>
            <value>firstName</value>
            <value>address.city</value>
        </list>
    </property>
</bean>

<bean id="delegateObject"
      class="egovframework.brte.sample.common.domain.person.PersonService" />
```

## 기존 서비스 구현

Reader 역할을 하는 대상 메서드는 `ItemReader.read()`와 같은 종료 규칙을 따라야 한다.

- 한 번 호출될 때 하나의 Item을 반환한다.
- 더 이상 반환할 Item이 없으면 반드시 `null`을 반환한다.
- 종료 조건 없이 객체를 계속 반환하면 Step이 끝나지 않을 수 있다.

다음 예제는 최대 10개의 `Person` 객체를 반환하고 Writer가 처리한 개수를 기록한다.

```java
public class PersonService {

    private static final int GENERATION_LIMIT = 10;

    private int generatedCounter;
    private int processedCounter;

    public Person getData() {
        if (generatedCounter >= GENERATION_LIMIT) {
            return null;
        }

        Person person = new Person();
        // firstName과 address.city 등 예제 데이터를 설정한다.

        generatedCounter++;
        return person;
    }

    public void processPerson(String firstName, String city) {
        // 기존 업무 로직을 수행한다.
        processedCounter++;
    }

    public int getReturnedCount() {
        return generatedCounter;
    }

    public int getReceivedCount() {
        return processedCounter;
    }
}
```

## JUnit 테스트

`JobLauncherTestUtils`로 Job을 실행하고 다음 항목을 검증한다.

1. Job 상태가 `COMPLETED`인지 확인한다.
2. Reader가 하나 이상의 Item을 반환했는지 확인한다.
3. Reader 반환 건수와 Writer 처리 건수가 같은지 확인한다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {
    "/egovframework/batch/simple-job-launcher-context.xml",
    "/egovframework/batch/jobs/delegatingJob.xml",
    "/egovframework/batch/job-runner-context.xml"
})
public class EgovDelegatingJobFunctionalTests {

    @Autowired
    private JobLauncherTestUtils jobLauncherTestUtils;

    @Autowired
    private PersonService personService;

    @Test
    public void testLaunchJob() throws Exception {
        JobExecution jobExecution = jobLauncherTestUtils.launchJob();

        assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus());
        assertTrue(personService.getReturnedCount() > 0);
        assertEquals(
            personService.getReturnedCount(),
            personService.getReceivedCount()
        );
    }
}
```

## 적용 시 고려사항

- 어댑터의 `targetMethod` 이름과 실제 서비스 메서드 이름이 일치해야 한다.
- `fieldsUsedAsTargetMethodArguments`의 순서는 대상 메서드 인자 순서와 같아야 한다.
- 중첩 속성은 `address.city`처럼 경로로 지정할 수 있다.
- 재시작 또는 병렬 실행을 적용할 때는 기존 서비스의 상태 보관 방식과 스레드 안전성을 함께 검토한다.
- 최신 Spring Batch에서는 패키지 또는 설정 방식이 달라질 수 있으므로 프로젝트에 적용된 버전의 API를 확인한다.

## 참고자료

- [동기/비동기 처리 예제](./batch-example-sync_async_v3.7.md)
- [Spring Batch - Reusing Existing Services](https://docs.spring.io/spring-batch/reference/readers-and-writers/reusing-existing-services.html)
