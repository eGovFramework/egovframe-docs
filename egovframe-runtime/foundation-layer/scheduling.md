---
title: Scheduling 서비스
linkTitle: "Scheduling 서비스"
description: Scheduling 서비스는 주기적 작업을 관리하는 기능으로, Quartz 스케줄러와 Spring을 통합하여 사용된다. Quartz는 작업(Job), 스케줄(Trigger)을 분리해 유연성을 제공하며, Spring에서 JobDetailBean과 MethodInvokingJobDetailFactoryBean을 통해 작업을 생성하고, SimpleTriggerBean과 CronTriggerBean으로 작업을 스케줄링한다.
url: /egovframe-runtime/foundation-layer/scheduling/
menu:
    depth:
        name: Scheduling 서비스
        weight: 3
        parent: "foundation-layer"
---
# Scheduling 서비스

## 개요

Scheduling 서비스는 어플리케이션 서버 내에서 주기적으로 발생하거나 반복적으로 발생하는 작업을 지원하는 기능으로서 유닉스의 크론(Cron) 명령어와 유사한 기능을 제공한다.  
실행환경 Scheduling 서비스는 오픈소스 소프트웨어로 Quartz 스케쥴러를 사용한다. 본 장에서는 Quartz 스케쥴러의 기본 개념을 살펴본 후, IoC 서비스를 제공하는 Spring과 Quartz 스케쥴러를 통합하여 사용하는 방법을 살펴본다.

## 설명

### Quartz 스케쥴러

Quartz 스케쥴러 실행과 관계된 주요 요소는 Scheduler, Job, JobDetail, Trigger 가 있다.

- **Scheduler** 는 Quartz 실행 환경을 관리하는 핵심 개체이다.
- **Job** 은 사용자가 수행할 작업을 정의하는 인터페이스로서 Trigger 개체를 이용하여 스케쥴할 수 있다.
- **JobDetail** 는 작업명과 작업그룹과 같은 수행할 Job에 대한 상세 정보를 정의하는 개체이다.
- **Trigger** 는 정의한 Job 개체의 실행 스케쥴을 정의하는 개체로서 Scheduler 개체에게 Job 수행시점을 알려주는 개체이다.

Quartz 스케쥴러는 수행 작업을 정의하는 Job과 실행 스케쥴을 정의하는 Trigger를 분리함으로써 유연성을 제공한다. Job 과 실행 스케쥴을 정의한 경우, Job은 그대로 두고 실행 스케쥴만을 변경할 수 있다. 또한 하나의 Job에 여러 개의 실행 스케쥴을 정의할 수 있다.

#### Quartz 스케쥴러 사용 예제

Quartz 스케쥴러의 이해를 돕기 위해 간단한 예제를 살펴본다. 다음 예는 Quartz 매뉴얼에서 참조한 것으로 Quartz를 사용하는 방법과 사용자 Job을 설정하는 방법을 보여준다.

##### 사용자 정의 Job

사용자는 Job 개체를 생성하기 위해 org.quartz.Job 인터페이스를 구현하고 심각한 오류가 발생한 경우 JobExecutionException 예외를 던질 수 있다. Job 인터페이스는 단일 메소드로 execute()을 정의한다.

```java
public class DumbJob implements Job {
	public void execute(JobExecutionContext context) throws JobExecutionException {
		System.out.println("DumbJob is executing.");
	}
}
```

- DumbJob은 Job 인터페이스의 execute() 메소드를 구현한다.
- execute() 메소드는 단순히 Job이 수행됨을 표시하는 메시지를 출력한다.

##### Quartz 사용 코드

```java
  JobDetail jobDetail = 
            new JobDetail("myJob",// Job 명
              sched.DEFAULT_GROUP,  // Job 그룹명('null' 값인 경우 DEFAULT_GROUP 으로 정의됨)
              DumbJob.class);       // 실행할 Job 클래스

  Trigger trigger = TriggerUtils.makeDailyTrigger(8, 30);  // 매일 08시 30분 실행
  trigger.setStartTime(new Date()); // 즉시 시작
  trigger.setName("myTrigger");

  sched.scheduleJob(jobDetail, trigger);
```

- 우선 Job 설정을 위해 JobDetail 클래스를 정의한다.
- TriggerUtils을 이용하여 매일 8시30분 실행하는 Trigger를 생성한다.
- 마지막으로, Scheduler에 JobDetail과 Trigger를 등록한다.

### Spring 과 Quartz 통합

Spring은 Scheduling 지원을 위한 통합 클래스를 제공한다. Spring Framework는 JDK 1.3 버전부터 포함된 Timer 와 오픈소스 소프트웨어인 Quartz 스케쥴러를 지원한다. 여기서는 Quartz 스케쥴러와 Spring을 통합하여 사용하는 방법을 살펴본다.  
Quartz 스케쥴러와의 통합을 위해 Spring은 Spring 컨텍스트 내에서 Quart Scheduler와 JobDetail, Trigger 를 빈으로 설정할 수 있도록 지원한다. 다음은 예제를 중심으로 Quartz 작업 생성과 작업 스케쥴링, 작업 시작 방법을 살펴본다.

#### 작업 생성

 Spring은 작업 생성을 위한 방법으로 다음 두 가지 방식을 제공한다.

- JobDetailBean을 이용한 방법으로, QuartzJobBean을 상속받아 Job 클래스를 생성하는 방법
- MethodInvokingJobDetailFactoryBean을 이용하여 Bean 객체의 메소드를 직접 호출하는 방법

##### JobDetailBean을 이용한 작업 생성

JobDetail는 작업 실행에 필요한 정보를 담고 있는 객체이다. Spring은 JobDetail 빈 생성을 위해 JobDetailBean을 제공한다. 예를 들면 다음과 같다.

##### JobDetailBean 소스 코드

```java
package egovframework.rte.fdl.scheduling.sample;

public class SayHelloJob extends QuartzJobBean {

	private String name;

	public void setName (String name) {
		this.name = name;	
	}

	@Override
	protected void executeInternal (JobExecutionContext ctx) throws JobExecutionException {
		System.out.println("Hello, " + name);
	}
}
```

- SayHelloJob 클래스는 작업 생성을 위해 QuartzJobBean의 executeInternal(..) 함수를 오버라이드한다.

##### JobDetailBean 설정

```xml
<bean id="jobDetailBean"
	class="org.springframework.scheduling.quartz.JobDetailBean">
	<property name="jobClass" value="egovframework.rte.fdl.scheduling.sample.SayHelloJob" />
	<property name="jobDataAsMap">
		<map>
			<entry key="name" value="JobDetail"/>
		</map>
	</property>
</bean>
```

- jobDataAsMap 개체를 이용하여 JobDetail 개체에 Job 설정에 필요한 속성 정보를 전달한다.

##### MethodInvokingJobDetailFactoryBean을 이용한 작업 생성

##### 소스 코드

```java
package egovframework.rte.fdl.scheduling.sample;

public class SayHelloService {

	private String name;

	public void setName (String name) {
		this.name = name;	
	}

	public void sayHello () {
		System.out.println("Hello, " + this.name);
	}
}
```

- 작업 수행을 할 Bean 클래스를 정의한다.

##### 설정

```xml
<bean id="sayHelloService" class="egovframework.rte.fdl.scheduling.sample.SayHelloService">
	<property name="name" value="FactoryBean"/>
</bean>

<bean id="jobDetailFactoryBean" class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
	<property name="targetObject" ref="sayHelloService" />
	<property name="targetMethod" value="sayHello" />
	<property name="concurrent" value="false" />
</bean>
```

- 정의한 Bean 객체의 메소드를 직접 호출하는 작업을 생성하기 위해 MethodInvokingJobDetailFactoryBean을 정의한다.

#### 작업 스케쥴링

Spring에서 주로 사용되는 Trigger타입은 SimpleTriggerBean과 CronTriggerBean 이 있다. SimpleTrigger 는 특정 시간, 반복 회수, 대기 시간과 같은 단순 스케쥴링에 사용된다. CronTrigger 는 유닉스의 Cron 명령어와 유사하며, 복잡한 스케쥴링에 사용된다. CronTrigger 는 달력을 이용하듯 특정 시간, 요일, 월에 Job 을 수행하도록 설정할 수 있다. 다음은 SimpleTriggerBean과 CronTriggerBean을 이용하여 앞서 생성한 작업을 스케쥴링하는 방법을 살펴본다.

##### SimpleTriggerBean을 이용한 설정

```xml
<bean id="simpleTrigger" class="org.springframework.scheduling.quartz.SimpleTriggerBean">
	<property name="jobDetail" ref="jobDetailBean" />
        <!-- 즉시 시작 -->
	<property name="startDelay" value="0" />
   	<!-- 매 10초마다 실행 -->
	<property name="repeatInterval" value="10000" />
</bean>
```

- 앞서 JobDetailBean 을 이용하여 생성한 작업을 스케쥴링을 위한 Trigger 에 등록한다. SimpleTriggerBean은 즉시 시작하고 매 10초마다 실행하도록 설정하였다.

##### CronTriggerBean을 이용한 설정

```xml
<bean id="cronTrigger" class="org.springframework.scheduling.quartz.CronTriggerBean">
   	<property name="jobDetail" ref="jobDetailFactoryBean" />
   	<!-- 매 10초마다 실행 -->
   	<property name="cronExpression" value="*/10 * * * * ?" />
</bean>
```

- 앞서 MethodInvokingJobDetailFactoryBean 을 이용하여 생성한 작업을 스케쥴링을 위한 Trigger 에 등록한다. CronTriggerBean은 매 10초마다 실행하도록 설정하였다. 크론 표현식에 대한 자세한 설명은 [Quartz Cron 표현식](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html)를 참조한다.

#### 작업 시작하기

스케쥴링한 작업의 시작을 위해 Spring 은 SchedulerFactoryBean을 제공한다.

##### 설정

```xml
<bean id="scheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
	<property name="triggers">
		<list>
			<ref bean="simpleTrigger" />
			<ref bean="cronTrigger" />
		</list>
	</property>
</bean>
```

- SchedulerFactoryBean 을 이용하여 SimpleTriggerBean 과 CronTriggerBean 기반의 각 Trigger 작업을 시작한다.

## 참고자료

- [Quartz 매뉴얼](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/quick-start.html)
- [Spring Scheduling 매뉴얼](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/integration.html#scheduling)
- [Quartz API](http://www.quartz-scheduler.org/api/2.3.0/index.html)
- [Spring API](https://docs.spring.io/spring-framework/docs/5.3.27/javadoc-api)
- [Quartz Cron 표현식](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html)