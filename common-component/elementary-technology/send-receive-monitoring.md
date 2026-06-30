---
title: "송수신모니터링"
linkTitle: "송수신모니터링"
description: "송수신모니터링"
url: /common-component/elementary-technology/system/send-receive-monitoring/
menu:
  depth:
    name: "송수신모니터링"
    weight: 11
    parent: "system"
---

<!-- markdownlint-disable MD013 MD025 -->

# 송수신모니터링

## 개요

송수신모니터링은 연계기관과의 송수신 상태를 주기적으로 모니터링하는 기능을 제공한다.
모니터링하고자 하는 연계는 시스템연계관리를 통해 시스템에 등록되어 있어야 한다. 모니터링 시에 사용되는 송수신상태를 체크하는 테스트 클래스는 `egovframework.com.utl.sys.trm.service.TrsmrcvMntrngChecker` 인터페이스를 구현하여 모니터링 대상 등록 시 해당 클래스를 테스트 클래스명으로 등록해야 한다.

## 설명

송수신모니터링을 등록하기 위한 목적으로 송수신모니터링의 등록, 수정, 삭제, 조회, 목록조회의 기능을 수반한다.

1. **송수신모니터링목록조회**: 송수신모니터링으로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
2. **송수신모니터링등록**: 송수신모니터링정보를 등록하고, 등록 결과를 조회한다.
3. **송수신모니터링수정**: 기 등록된 송수신모니터링정보의 항목들을 수정한다.
4. **송수신모니터링삭제**: 기 등록된 송수신모니터링정보를 삭제한다.
5. **송수신모니터링조회**: 등록된 송수신모니터링정보를 조회한다.
6. **송수신모니터링로그목록조회**: 송수신모니터링로그로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
7. **송수신모니터링로그조회**: 등록된 송수신모니터링로그정보를 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.trm.web.EgovTrsmrcvMntrngController.java` | 송수신모니터링을 위한 컨트롤러 클래스 |
| Service | `egovframework.com.utl.sys.trm.service.EgovTrsmrcvMntrngService.java` | 송수신모니터링을 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.utl.sys.trm.service.impl.EgovTrsmrcvMntrngServiceImpl.java` | 송수신모니터링을 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.utl.sys.trm.service.impl.TrsmrcvMntrngDAO.java` | 송수신모니터링을 위한 데이터처리 클래스 |
| Model | `egovframework.com.utl.sys.trm.service.TrsmrcvMntrng.java` | 송수신모니터링을 위한 Model 클래스 |
| Model | `egovframework.com.utl.sys.trm.service.TrsmrcvMntrngLog.java` | 송수신모니터링로그정보를 위한 Model 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngList.jsp` | 송수신모니터링목록조회를 위한 JSP 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngRegist.jsp` | 송수신모니터링 등록을 위한 JSP 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngUpdt.jsp` | 송수신모니터링 수정을 위한 JSP 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngDetail.jsp` | 등록된 송수신모니터링을 조회하기 위한 JSP 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngLogList.jsp` | 송수신모니터링로그목록조회를 위한 JSP 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/trm/EgovTrsmrcvMntrngLogDetail.jsp` | 등록된 송수신모니터링로그을 조회하기 위한 JSP 페이지 |
| XML | `/egovframework/sqlmap/com/utl/sys/trm/EgovTrsmrcvMntrng_SQL_*.xml` | 송수신모니터링 QUERY XML |

### 클래스 다이어그램

![송수신모니터링 클래스 다이어그램](./images/send-receive-monitoring-class.png)

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 송수신모니터링 | `COMTNTRSMRCVMNTRNG` | 송수신모니터링정보를 관리하기 위한 속성정보를 정의하고 관리한다. |
| 송수신모니터링로그정보 | `COMTHTRSMRCVMNTRNGLOGINFO` | 송수신모니터링로그정보를 관리하기 위한 속성정보를 정의하고 관리한다. |

### ID Generation

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 `COMTECOPSEQ`에 `TR_MNTRNG_LOG_ID` 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('TR_MNTRNG_LOG_ID', '0');
```

### 스케줄러 등록

송수신모니터링 스케줄러를 등록하기 위해서 `context-scheduling.xml` 파일에 다음과 같이 등록한다.

```xml
<!-- 송수신모니터링 스케줄링 -->
<bean id="trsmrcvMntrng" class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="egovTrsmrcvMntrngScheduling" />
    <property name="targetMethod" value="monitor" />
    <property name="concurrent" value="false" />
</bean>

<!-- 송수신모니터링 트리거 -->
<bean id="trsmrcvMntrngTrigger" class="org.springframework.scheduling.quartz.SimpleTriggerBean">
    <property name="jobDetail" ref="trsmrcvMntrng" />
    <property name="startDelay" value="60000" />
    <property name="repeatInterval" value="600000" />
</bean>
```

- `startDelay`는 서버 시작 후 몇 초 뒤에 시작할지를 설정한다. (ms 단위: 현재 1분)
- `repeatInterval`은 몇 초에 한 번씩 실행될지를 설정한다. (ms 단위: 현재 10분)

```xml
<!-- 모니터링 스케줄러 -->
<bean id="mntrngScheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
    <property name="triggers">
        <list>
            <ref bean="trsmrcvMntrngTrigger" />
        </list>
    </property>
</bean>
```

## 관련화면 및 수행매뉴얼

### 송수신모니터링 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | `/utl/sys/trm/selectTrsmrcvMntrngList.do` | `selectTrsmrcvMntrngList` | `TrsmrcvMntrngDAO.selectTrsmrcvMntrngList`<br>`TrsmrcvMntrngDAO.selectTrsmrcvMntrngListCnt` |

송수신모니터링 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다. 검색조건은 연계명, 관리자명에 대해서 수행된다.

![송수신모니터링 목록조회](./images/send-receive-monitoring-list.png)

- **조회**: 기 등록된 송수신모니터링의 목록을 조회한다.
- **등록**: 신규 송수신모니터링을 등록하기 위해서는 상단의 등록 버튼을 통해서 **송수신모니터링 등록** 화면으로 이동한다.

### 송수신모니터링 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | `/utl/sys/trm/addTrsmrcvMntrng.do` | `insertTrsmrcvMntrng` | `TrsmrcvMntrngDAO.insertTrsmrcvMntrng` |

송수신모니터링의 속성정보를 입력한 뒤 등록한다.

![송수신모니터링 등록](./images/send-receive-monitoring-create.png)

- **저장**: 신규 송수신모니터링을 등록하기 위해서는 송수신모니터링 속성을 입력한 뒤 상단의 **저장 버튼**을 통해서 송수신모니터링을 등록한다.
- **목록**: 송수신모니터링 목록조회 화면으로 이동한다.

### 송수신모니터링 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | `/utl/sys/trm/updateTrsmrcvMntrng.do` | `updateTrsmrcvMntrng` | `TrsmrcvMntrngDAO.updateTrsmrcvMntrng` |

송수신모니터링의 속성정보를 변경한 후 저장한다.

![송수신모니터링 수정](./images/send-receive-monitoring-update.png)

- **저장**: 기 등록된 송수신모니터링 속성을 수정한 뒤 상단의 **저장 버튼**을 통해서 송수신모니터링정보를 수정한다.
- **목록**: 송수신모니터링 목록조회 화면으로 이동한다.

### 송수신모니터링 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | `/utl/sys/trm/getTrsmrcvMntrng.do` | `selectTrsmrcvMntrng` | `TrsmrcvMntrngDAO.selectTrsmrcvMntrng` |
| 삭제 | `/utl/sys/trm/deleteTrsmrcvMntrng.do` | `deleteTrsmrcvMntrng` | `TrsmrcvMntrngDAO.deleteTrsmrcvMntrng` |

송수신모니터링의 속성정보를 조회한다.

![송수신모니터링 상세조회](./images/send-receive-monitoring-detail.png)

- **수정**: 기 등록된 송수신모니터링 속성을 수정한 뒤 상단의 **수정 버튼**을 통해서 송수신모니터링수정화면으로 이동한다.
- **삭제**: 기 등록된 송수신모니터링정보를 삭제한다.
- **목록**: 송수신모니터링 목록조회 화면으로 이동한다.

### 송수신모니터링로그 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | `/utl/sys/trm/selectTrsmrcvMntrngLogList.do` | `selectTrsmrcvMntrngLogList` | `TrsmrcvMntrngDAO.selectTrsmrcvMntrngLogList`<br>`TrsmrcvMntrngDAO.selectTrsmrcvMntrngLogListCnt` |

송수신모니터링로그 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다. 검색조건은 연계명, 관리자명, 모니터링시각에 대해서 수행된다.

![송수신모니터링로그 목록조회](./images/send-receive-monitoring-log-list.png)

- **조회**: 기 등록된 송수신모니터링로그의 목록을 조회한다.

### 송수신모니터링로그 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | `/utl/sys/trm/getTrsmrcvMntrngLog.do` | `selectTrsmrcvMntrngLog` | `TrsmrcvMntrngDAO.selectTrsmrcvMntrngLog` |

송수신모니터링로그의 속성정보를 조회한다.

![송수신모니터링로그 상세조회](./images/send-receive-monitoring-log-detail.png)

- **목록**: 송수신모니터링로그 목록조회 화면으로 이동한다.
