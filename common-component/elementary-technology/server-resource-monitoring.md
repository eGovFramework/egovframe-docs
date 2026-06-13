---
title: "서버자원모니터링"
linkTitle: "서버자원모니터링"
description: "서버자원모니터링"
url: /common-component/elementary-technology/system/server-resource-monitoring/
menu:
  depth:
    name: "서버자원모니터링"
    weight: 49
    parent: "system"
---

<!-- markdownlint-disable MD025 -->
# 서버자원모니터링
<!-- markdownlint-enable MD025 -->

## 개요

서버자원모니터링은 시스템의 서버 자원(CPU, Memory 등) 상태를 모니터링하고 그 결과를 로그로 등록하여 관리하는 공통컴포넌트이다.
스케줄러를 통해 주기적으로 서버의 자원 상태를 확인하고, 이를 시스템에 기록함으로써 관리자가 서버의 부하 상태를 파악하도록 돕는다.

## 주요 개념

### 모니터링 결과 등록

- 스케줄러(Scheduler)를 사용하여 정해진 주기마다 서버자원모니터링 결과(로그) 정보를 자동으로 시스템에 등록한다.
- 배치 스케줄링 설정을 위해 `context-scheduling-utl-sys-srm.xml` 파일을 사용한다.

### 모니터링 목록 조회

- 등록된 서버 자원의 모니터링 결과 로그를 목록 형태로 조회한다.
- 기간, 서버명 등 검색 조건을 활용하여 원하는 모니터링 기록을 조회할 수 있다.

### 모니터링 상세 조회

- 모니터링 결과 목록에서 특정 건을 선택하여 상세한 서버 자원 상태 정보를 확인한다.

## 설명

### 컴포넌트 구조

해당 기능은 `egovframework.com.utl.sys.srm` 패키지 하위에 구성되어 있으며, 서버 H/W 정보 관리와 연동되어 동작한다.
표준프레임워크 공통컴포넌트 버전에 따라 `egovframework-serverresrcemntrng-[버전].zip` 형태의 파일로 배포된다.

### 스케줄러 설정

서버자원모니터링을 주기적으로 실행하려면 스프링 스케줄링 설정 파일(`context-scheduling-utl-sys-srm.xml`)에 정의가 필요하다.

```xml
<!-- 서버자원모니터링 스케줄러 작업 설정 예시 -->
<bean id="serverResrceMntrng" class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="egovServerResrceMntrngScheduling" />
    <property name="targetMethod" value="insertServerResrceMntrng" />
    <property name="concurrent" value="false" />
</bean>

<!-- 10분마다 모니터링 결과를 등록하는 트리거 설정 예시 -->
<bean id="serverResrceMntrngTrigger" class="org.springframework.scheduling.quartz.SimpleTriggerFactoryBean">
    <property name="jobDetail" ref="serverResrceMntrng" />
    <property name="startDelay" value="60000" />
    <property name="repeatInterval" value="600000" />
</bean>
```

### 모니터링 Agent 연동

대상 서버의 자원을 정확히 수집하기 위해 JMX(Java Management Extensions) MBean 기반의 모니터링 Agent 예제가
연동될 수 있다. 시스템은 지정된 Agent와 통신하여 실시간 메모리나 CPU 사용량 등을 수집한 뒤 로그로 기록한다.

## 참고자료

- [전자정부 표준프레임워크 공통컴포넌트 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.1)
