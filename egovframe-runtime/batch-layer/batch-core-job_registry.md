---
title: JobRegistry
linkTitle: JobRegistry
description: JobRegistry는 생성된 Job을 자동으로 Map형태로 저장하여 관리한다. JobRegistry는 context에서 Job을 추적하거나 다른 곳에서 생성된 Job을 application context의 중앙에 모을 때 유용하게 사용할 수 있다. 등록된 Job의 이름과 속성들을 조작할 수 있으며, job name과 job instance의 Map의 형태로 이루워져 있다.
url: /egovframe-runtime/batch-layer/batch-core-job_registry/
menu:
    depth:
        name: JobRegistry
        weight: 10
        parent: "batch-layer"
---
# JobRegistry

## 개요
JobRegistry는 생성된 Job을 자동으로 Map형태로 저장하여 관리(추가, 삭제 등)한다.

## 설명
JobRegistry는 필수는 아니지만 context에서 Job을 추적하거나 다른 곳에서 생성된 Job을 application context의 중앙에 모을 때 유용하다. 등록된 Job의 이름과 속성들을 조작할 수 있으며 job name과 job instance의 Map의 형태로 이루워져 있다.

```xml
<bean id="jobRegistry" class="org.springframework.batch.core.configuration.support.MapJobRegistry" />
```

JobRegistry에 Job을 자동으로 등록하는 방법은 두 가지가 있다.

- JobRegistryBeanPostProcessor 사용
- AutomaticJobRegistrar 사용

### JobRegistryBeanPostProcessor
이것은 Bean post-processor으로 Application Context가 올라가면서 bean 등록 시, 자동으로 JobRegistry에 Job을 등록 시켜준다.

```xml
<bean id="jobRegistryBeanPostProcessor" class="org.springframework.batch.core.configuration.support.JobRegistryBeanPostProcessor">
    <property name="jobRegistry" ref="jobRegistry"/>
</bean>
```

### AutomaticJobRegistrar
부모 context에서 자식 contexts에 생성된 Job들을 사용하기 위해 자동으로 부모 context의 JobRegistry에 Job들을 등록시킨다. AutomaticJobRegistrar을 사용하기 위해서는 아래와 같이 ApplicationContextFactory와 JobLoader의 설정은 필수이다. ApplicationContextFactory는 ClassPathXmlApplicationContextFactory를 이용하여 자식 context를 생성하고 JobLoader는 자식 context를 관리하고 JobRegistry에 Job 등록을 한다.

```xml
<bean class="org.spr...AutomaticJobRegistrar">
   <property name="applicationContextFactories">
      <bean class="org.spr...ClasspathXmlApplicationContextsFactoryBean">
         <property name="resources" value="classpath*:/config/job*.xml" />
      </bean>
   </property>
   <property name="jobLoader">
      <bean class="org.spr...DefaultJobLoader">
         <property name="jobRegistry" ref="jobRegistry" />
      </bean>
   </property>
</bean>
```

## 참고자료
* [http://static.springsource.org/spring-batch/reference/html/configureJob.html#d0e2232](http://static.springsource.org/spring-batch/reference/html/configureJob.html#d0e2232)