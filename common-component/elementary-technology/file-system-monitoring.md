---
title: "파일시스템모니터링"
linkTitle: "파일시스템모니터링"
description: "파일시스템모니터링"
url: /common-component/elementary-technology/system/file-system-monitoring/
menu:
  depth:
    name: "파일시스템모니터링"
    weight: 26
    parent: "system"
---

<!-- markdownlint-disable MD013 -->

## 개요

파일시스템모니터링은 파일시스템 상태를 주기적으로 모니터링하는 기능을 제공한다.
모니터링하고자 하는 파일시스템은 파일시스템대상목록으로 시스템에 등록되어 있어야 한다.
등록한 임계치를 초과하는 경우 관리자 메일주소로 모니터링 정보를 발송한다.

## 설명

파일시스템모니터링을 등록하기 위한 목적으로 파일시스템모니터링의 등록, 수정, 삭제, 조회, 목록조회의 기능을 수반한다.

1. **파일시스템모니터링목록조회**: 파일시스템모니터링으로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
2. **파일시스템모니터링등록**: 파일시스템모니터링정보를 등록하고, 등록 결과를 조회한다.
3. **파일시스템모니터링수정**: 기 등록된 파일시스템모니터링정보의 항목들을 수정한다.
4. **파일시스템모니터링삭제**: 기 등록된 파일시스템모니터링정보를 삭제한다.
5. **파일시스템모니터링조회**: 등록된 파일시스템모니터링정보를 조회한다.
6. **파일시스템모니터링로그목록조회**: 파일시스템모니터링로그로 정의된 정보를 최근 등록 순서대로 조회하고, 그 결과 목록을 화면에 반영한다.
7. **파일시스템모니터링로그조회**: 등록된 파일시스템모니터링로그정보를 조회한다.

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | `egovframework.com.utl.sys.fsm.web.EgovFileSysMntrngController.java` | 파일시스템모니터링을 위한 컨트롤러 클래스 |
| Service | `egovframework.com.utl.sys.fsm.service.EgovFileSysMntrngService.java` | 파일시스템모니터링을 위한 서비스 인터페이스 |
| ServiceImpl | `egovframework.com.utl.sys.fsm.service.impl.EgovFileSysMntrngServiceImpl.java` | 파일시스템모니터링을 위한 서비스 구현 클래스 |
| DAO | `egovframework.com.utl.sys.fsm.service.impl.FileSysMntrngDAO.java` | 파일시스템모니터링을 위한 데이터처리 클래스 |
| Model | `egovframework.com.utl.sys.fsm.service.FileSysMntrng.java` | 파일시스템모니터링을 위한 Model 클래스 |
| Model | `egovframework.com.utl.sys.fsm.service.FileSysMntrngLog.java` | 파일시스템모니터링로그정보를 위한 Model 클래스 |
| VO | `egovframework.com.utl.sys.fsm.service.FileSysMntrngVO.java` | 파일시스템모니터링을 위한 VO 클래스 |
| VO | `egovframework.com.utl.sys.fsm.service.FileSysMntrngLogVO.java` | 파일시스템모니터링로그정보를 위한 VO 클래스 |
| Scheduling | `egovframework.com.utl.sys.fsm.service.EgovFileSystemMntrngScheduling.java` | 파일시스템모니터링 스케줄링 클래스 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngList.jsp` | 파일시스템모니터링 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngRegist.jsp` | 파일시스템모니터링 등록 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngUpdt.jsp` | 파일시스템모니터링 수정 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngDetail.jsp` | 파일시스템모니터링 상세조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngLogList.jsp` | 파일시스템모니터링로그 목록조회 페이지 |
| JSP | `/WEB-INF/jsp/egovframework/utl/sys/fsm/EgovFileSysMntrngLogDetail.jsp` | 파일시스템모니터링로그 상세조회 페이지 |
| XML | `/egovframework/sqlmap/com/utl/sys/fsm/EgovFileSysMntrng_SQL_*.xml` | 파일시스템모니터링 QUERY XML |

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 파일시스템모니터링 | COMTNFILESYSMNTRNG | 파일시스템모니터링정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |
| 파일시스템모니터링로그정보 | COMTNFILESYSMNTRNGLOGINFO | 파일시스템모니터링로그정보를 관리하기 위한 속성정보를 정의하고, 관리한다. |

### ID Generation

ID Generation Service를 활용하기 위해서 Sequence 저장테이블인 COMTECOPSEQ에 `FILESYS_MNTRNG` 항목과 `FILESYS_LOGID` 항목을 추가한다.

```sql
INSERT INTO COMTECOPSEQ VALUES('FILESYS_MNTRNG','0');
INSERT INTO COMTECOPSEQ VALUES('FILESYS_LOGID','0');
```

### 스케줄러 등록

파일시스템모니터링 스케줄러를 등록하기 위해서 `context-scheduling.xml` 파일에 다음과 같이 등록한다.
`startDelay`는 서버 시작 후 몇 초 뒤에 시작할지를, `repeatInterval`은 몇 초에 한 번씩 실행될지를 설정한다(ms 단위).

```xml
<!-- 파일시스템모니터링 -->
<bean id="fileSysMntrng"
    class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="egovFileSysMntrngScheduling" />
    <property name="targetMethod" value="monitorFileSys" />
    <property name="concurrent" value="false" />
</bean>

<!-- 파일시스템모니터링 트리거 -->
<bean id="fileSysMntrngTrigger"
    class="org.springframework.scheduling.quartz.SimpleTriggerBean">
    <property name="jobDetail" ref="fileSysMntrng" />
    <!-- 시작하고 1분 후에 실행한다. (milisecond) -->
    <property name="startDelay" value="60000" />
    <!-- 매 10분마다 실행한다. (milisecond) -->
    <property name="repeatInterval" value="600000" />
</bean>

<!-- 모니터링 스케줄러 -->
<bean id="mntrngScheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
    <property name="triggers">
        <list>
            <ref bean="fileSysMntrngTrigger" />
        </list>
    </property>
</bean>
```

## 관련화면 및 수행매뉴얼

### 파일시스템모니터링 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/fsm/selectFileSysMntrngList.do | selectFileSysMntrngList | FileSysMntrngDAO.selectFileSysMntrngList |
| 조회 | /utl/sys/fsm/selectFileSysMntrngList.do | selectFileSysMntrngList | FileSysMntrngDAO.selectFileSysMntrngListCnt |

파일시스템모니터링 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
검색조건은 파일시스템명, 파일시스템관리명, 관리자명, 상태에 대해서 수행된다.

### 파일시스템모니터링 등록

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 등록 | /utl/sys/fsm/addFileSysMntrng.do | insertFileSysMntrng | FileSysMntrngDAO.insertFileSysMntrng |

파일시스템모니터링의 속성정보를 입력한 뒤 등록한다. **임계치** 필드는 등록한 파일시스템의 크기에서 위험을 알리는 경계 수치로,
임계치를 초과할 경우 관리자 메일주소로 모니터링 정보를 보낸다.

### 파일시스템모니터링 수정

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 수정 | /utl/sys/fsm/modifyFileSysMntrng.do | updateFileSysMntrng | FileSysMntrngDAO.updateFileSysMntrng |

파일시스템모니터링의 속성정보를 변경한 후 저장한다.

### 파일시스템모니터링 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/fsm/selectFileSysMntrng.do | selectFileSysMntrng | FileSysMntrngDAO.selectFileSysMntrng |
| 삭제 | /utl/sys/fsm/deleteFileSysMntrng.do | deleteFileSysMntrng | FileSysMntrngDAO.deleteFileSysMntrng |

파일시스템모니터링의 속성정보를 조회하며, 수정 화면으로 이동하거나 등록된 정보를 삭제할 수 있다.

### 파일시스템모니터링로그 목록조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 조회 | /utl/sys/fsm/selectFileSysMntrngLogList.do | selectFileSysMntrngLogList | FileSysMntrngDAO.selectFileSysMntrngLogList |
| 조회 | /utl/sys/fsm/selectFileSysMntrngLogList.do | selectFileSysMntrngLogList | FileSysMntrngDAO.selectFileSysMntrngLogListCnt |

파일시스템모니터링로그 목록은 페이지당 10건씩 조회되며 페이징은 10페이지씩 이루어진다.
검색조건은 파일시스템명, 파일시스템관리명, 관리자명, 상태, 모니터링시각에 대해서 수행된다.

### 파일시스템모니터링로그 상세조회

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /utl/sys/fsm/selectFileSysMntrngLog.do | selectFileSysMntrngLog | FileSysMntrngDAO.selectFileSysMntrngLog |

파일시스템모니터링로그의 속성정보를 조회한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
