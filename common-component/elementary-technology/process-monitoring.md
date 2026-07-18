---
title: "프로세스모니터링"
linkTitle: "프로세스모니터링"
description: "프로세스모니터링"
url: /common-component/elementary-technology/system/process-monitoring/
menu:
  depth:
    name: "프로세스모니터링"
    weight: 24
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

프로세스모니터링은 특정 프로세스가 기동 중인지 주기적으로 점검을 수행하고, 문제 발생 시 해당 정보를 관리자에게 통보하는 기능을 제공한다.
WINDOWS 및 UNIX 환경을 모두 지원하며, `globals.properties`의 `Globals.OsType`으로 운영체제를 설정한다.

### 활용 예시

프로세스모니터링 기능은 다음과 같은 상황에서 활용할 수 있다.

- 주요 서버 프로세스의 정상 실행 여부를 주기적으로 확인하는 경우
- 특정 프로세스의 비정상 상태를 감지하고 관리자에게 알림을 전달하는 경우
- 프로세스 상태 점검 결과를 로그로 기록하고 이력을 확인하는 경우
- 운영 중인 애플리케이션의 주요 프로세스를 지속적으로 관리하는 경우

## 설명

프로세스모니터링을 등록하기 위한 목적으로 프로세스모니터링의 등록, 수정, 삭제, 조회, 목록조회의 기능을 수반한다.

1. **프로세스모니터링목록조회**: 프로세스모니터링으로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
2. **프로세스모니터링등록**: 프로세스모니터링정보를 등록하고, 등록 결과를 조회한다.
3. **프로세스모니터링수정**: 기 등록된 프로세스모니터링정보의 항목들을 수정한다.
4. **프로세스모니터링삭제**: 기 등록된 프로세스모니터링정보를 삭제한다.
5. **프로세스모니터링조회**: 등록된 프로세스모니터링정보를 조회한다.
6. **프로세스모니터링로그목록조회**: 프로세스모니터링로그로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
7. **프로세스모니터링로그조회**: 등록된 프로세스모니터링로그정보를 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.prm.web.EgovProcessMonController.java` | 프로세스모니터링을 위한 컨트롤러 클래스 |
| Service | `egovframework.com.utl.sys.prm.service.EgovProcessMonService.java` | 프로세스모니터링을 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.utl.sys.prm.service.impl.EgovProcessMonServiceImpl.java` | 프로세스모니터링을 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.utl.sys.prm.service.impl.ProcessMonDAO.java` | 프로세스모니터링을 위한 데이터처리 클래스 |
| Model | `egovframework.com.utl.sys.prm.service.ProcessMon.java` | 프로세스모니터링을 위한 Model 클래스 |
| Model | `egovframework.com.utl.sys.prm.service.ProcessMonLog.java` | 프로세스모니터링로그정보를 위한 Model 클래스 |
| Scheduling | `egovframework.com.utl.sys.prm.service.EgovProcessMonScheduling.java` | 프로세스모니터링 스케줄링 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonList.jsp` | 프로세스모니터링 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonRegist.jsp` | 프로세스모니터링 등록 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonUpdt.jsp` | 프로세스모니터링 수정 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonDetail.jsp` | 프로세스모니터링 상세조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonLogList.jsp` | 프로세스모니터링로그 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/prm/EgovProcessMonLogDetail.jsp` | 프로세스모니터링로그 상세조회 페이지 |
| XML | `/egovframework/sqlmap/com/utl/sys/prm/EgovProcessMon_SQL_*.xml` | 프로세스모니터링 QUERY XML |

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 프로세스모니터링 | COMTNPROCESSMON | 프로세스모니터링정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |
| 프로세스모니터링로그정보 | COMTNPROCESSMONLOGINFO | 프로세스모니터링로그정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |

### ID Generation

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 `PROC_ID`·`PROL_ID` 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('PROC_ID','0');
INSERT INTO COMTECOPSEQ VALUES('PROL_ID','0');
```

### 프로퍼티 설정

운영체제 유형을 `globals.properties`에 설정한다.

```properties
# UNIX인 경우
Globals.OsType = UNIX
# WINDOWS인 경우
# Globals.OsType = WINDOWS
```

### 스케줄러 등록

프로세스모니터링 스케줄러를 `context-scheduling.xml`에 등록한다. `startDelay`는 서버 시작 후 시작 시점,
`repeatInterval`은 실행 주기를 설정한다(ms 단위).

```xml
<!-- 프로세스모니터링 -->
<bean id="processMntrng"
    class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="egovProcessMonScheduling" />
    <property name="targetMethod" value="monitorProcess" />
    <property name="concurrent" value="false" />
</bean>

<!-- 프로세스모니터링 트리거 -->
<bean id="processMntrngTrigger"
    class="org.springframework.scheduling.quartz.SimpleTriggerBean">
    <property name="jobDetail" ref="processMntrng" />
    <property name="startDelay" value="60000" />
    <property name="repeatInterval" value="600000" />
</bean>

<!-- 모니터링 스케줄러 -->
<bean id="mntrngScheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
    <property name="triggers">
        <list>
            <ref bean="processMntrngTrigger" />
        </list>
    </property>
</bean>
```

### 설정 시 주의사항

- `Globals.OsType`은 실제 서버의 운영체제 환경에 맞게 설정해야 한다.
- 프로세스 정보를 조회할 수 있도록 애플리케이션 실행 계정의 권한을 확인해야 한다.
- `repeatInterval`은 밀리초(ms) 단위이므로 운영 환경에 적절한 모니터링 주기를 설정해야 한다.
- 관리자 알림을 사용하는 경우 이메일 발송을 위한 관련 설정이 정상적으로 구성되어 있어야 한다.

## 관련화면 및 수행매뉴얼

### 프로세스모니터링 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/prm/selectProcessMonList.do | selectProcessMonList | ProcessMonDAO.selectProcessMonList |
| 조회 | /utl/sys/prm/selectProcessMonList.do | selectProcessMonList | ProcessMonDAO.selectProcessMonListCnt |

목록은 페이지당 10건씩 조회되며 검색조건은 상태·관리자명에 대해 수행된다. 상태가 비정상일 때 관리자에게 이메일을 발송한다.

### 프로세스모니터링 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /utl/sys/prm/addProcessMon.do | insertProcessMon | ProcessMonDAO.insertProcessMon |

프로세스모니터링의 속성정보를 입력한 뒤 등록한다. 프로세스명은 공통컴포넌트가 설치된 서버의 프로세스명을 의미한다.

### 프로세스모니터링 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /utl/sys/prm/updateProcessMon | updateProcessMon | ProcessMonDAO.updateProcessMon |

### 프로세스모니터링 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/prm/getProcessMon.do | selectProcessMon | ProcessMonDAO.selectProcessMon |
| 삭제 | /utl/sys/prm/deleteProcessMon.do | deleteProcessMon | ProcessMonDAO.deleteProcessMon |

### 프로세스모니터링로그 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/prm/selectProcessMonLogList.do | selectProcessMonLogList | ProcessMonDAO.selectProcessMonLogList |
| 조회 | /utl/sys/prm/selectProcessMonLogList.do | selectProcessMonLogList | ProcessMonDAO.selectProcessMonLogListCnt |

검색조건은 상태·관리자명·모니터링시각에 대해 수행된다.

### 프로세스모니터링로그 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/prm/getProcessMonLog.do | selectProcessMonLog | ProcessMonDAO.selectProcessMonLog |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
