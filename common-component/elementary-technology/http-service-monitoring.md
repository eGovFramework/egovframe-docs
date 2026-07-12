---
title: "HTTP서비스모니터링"
linkTitle: "HTTP서비스모니터링"
description: "HTTP서비스모니터링"
url: /common-component/elementary-technology/system/http-service-monitoring/
menu:
  depth:
    name: "HTTP서비스모니터링"
    weight: 51
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

HTTP서비스모니터링은 웹 서비스(웹서버 및 WAS)가 정상적인지 주기적인 점검을 수행하고, 문제 발생 시 해당 정보를 관리자에게 통보하는 기능을 제공한다.

## 설명

HTTP서비스모니터링을 등록하기 위한 목적으로 HTTP서비스모니터링의 등록, 수정, 삭제, 조회, 목록조회의 기능을 수반한다.

1. **HTTP서비스모니터링목록조회**: HTTP서비스모니터링으로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
2. **HTTP서비스모니터링등록**: HTTP서비스모니터링정보를 등록하고, 등록 결과를 조회한다.
3. **HTTP서비스모니터링수정**: 기 등록된 HTTP서비스모니터링정보의 항목들을 수정한다.
4. **HTTP서비스모니터링삭제**: 기 등록된 HTTP서비스모니터링정보를 삭제한다.
5. **HTTP서비스모니터링조회**: 등록된 HTTP서비스모니터링정보를 조회한다.
6. **HTTP서비스모니터링로그목록조회**: HTTP서비스모니터링로그로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
7. **HTTP서비스모니터링로그조회**: 등록된 HTTP서비스모니터링로그정보를 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.htm.web.EgovHttpMonController.java` | HTTP서비스모니터링을 위한 컨트롤러 클래스 |
| Service | `egovframework.com.utl.sys.htm.service.EgovHttpMonService.java` | HTTP서비스모니터링을 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.utl.sys.htm.service.impl.EgovHttpMonServiceImpl.java` | HTTP서비스모니터링을 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.utl.sys.htm.service.impl.HttpMonDAO.java` | HTTP서비스모니터링을 위한 데이터처리 클래스 |
| Model | `egovframework.com.utl.sys.htm.service.HttpMon.java` | HTTP서비스모니터링을 위한 Model 클래스 |
| Model | `egovframework.com.utl.sys.htm.service.HttpMonLog.java` | HTTP서비스모니터링로그정보를 위한 Model 클래스 |
| Scheduling | `egovframework.com.utl.sys.htm.service.HttpMntrngScheduling.java` | HTTP서비스모니터링 스케줄링 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonList.jsp` | HTTP서비스모니터링 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonRegist.jsp` | HTTP서비스모니터링 등록 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonUpdt.jsp` | HTTP서비스모니터링 수정 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonDetail.jsp` | HTTP서비스모니터링 상세조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonLogList.jsp` | HTTP서비스모니터링로그 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/htm/EgovHttpMonLogDetail.jsp` | HTTP서비스모니터링로그 상세조회 페이지 |
| XML | `/egovframework/sqlmap/com/utl/sys/htm/EgovHttpMon_SQL_*.xml` | HTTP서비스모니터링 QUERY XML |

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| HTTP서비스모니터링 | COMTNHTTPMON | HTTP서비스모니터링정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |
| HTTP서비스모니터링로그정보 | COMTHHTTPMONLOGINFO | HTTP서비스모니터링로그정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |

### ID Generation

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 `HTTP_ID`·`HTTL_ID` 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('HTTP_ID','0');
INSERT INTO COMTECOPSEQ VALUES('HTTL_ID','0');
```

### 스케줄러 등록

HTTP서비스모니터링 스케줄러를 `context-scheduling.xml`에 등록한다. `startDelay`는 서버 시작 후 시작 시점,
`repeatInterval`은 실행 주기를 설정한다(ms 단위).

```xml
<!-- HTTP서비스모니터링 -->
<bean id="httpMon"
    class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="httpMntrngScheduling" />
    <property name="targetMethod" value="monitorHttp" />
    <property name="concurrent" value="false" />
</bean>

<!-- HTTP서비스모니터링 트리거 -->
<bean id="httpMntrngTrigger"
    class="org.springframework.scheduling.quartz.SimpleTriggerBean">
    <property name="jobDetail" ref="httpMon" />
    <!-- 시작하고 1분 후에 실행한다. (milisecond) -->
    <property name="startDelay" value="60000" />
    <!-- 매 10분마다 실행한다. (milisecond) -->
    <property name="repeatInterval" value="600000" />
</bean>

<!-- 모니터링 스케줄러 -->
<bean id="mntrngScheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
    <property name="triggers">
        <list>
            <ref bean="httpMntrngTrigger" />
        </list>
    </property>
</bean>
```

## 관련화면 및 수행매뉴얼

### HTTP서비스모니터링 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/htm/selectHttpMonList.do | selectHttpMonList | HttpMonDAO.selectHttpMonList |
| 조회 | /utl/sys/htm/selectHttpMonList.do | selectHttpMonList | HttpMonDAO.selectHttpMonListCnt |

목록은 페이지당 10건씩 조회되며 검색조건은 상태·관리자명에 대해 수행된다. 상태가 비정상일 때 관리자에게 이메일을 발송한다.

### HTTP서비스모니터링 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /utl/sys/htm/addHttpMon.do | insertHttpMon | HttpMonDAO.insertHttpMon |

### HTTP서비스모니터링 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /utl/sys/htm/updateHttpMon | updateHttpMon | HttpMonDAO.updateHttpMon |

### HTTP서비스모니터링 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/htm/getHttpMon.do | selectHttpMon | HttpMonDAO.selectHttpMon |
| 삭제 | /utl/sys/htm/deleteHttpMon.do | deleteHttpMon | HttpMonDAO.deleteHttpMon |

### HTTP서비스모니터링로그 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/htm/selectHttpMonLogList.do | selectHttpMonLogList | HttpMonDAO.selectHttpMonLogList |
| 조회 | /utl/sys/htm/selectHttpMonLogList.do | selectHttpMonLogList | HttpMonDAO.selectHttpMonLogListCnt |

검색조건은 상태·관리자명·모니터링시각에 대해 수행된다.

### HTTP서비스모니터링로그 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/htm/getHttpMonLog.do | selectHttpMonLog | HttpMonDAO.selectHttpMonLog |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
