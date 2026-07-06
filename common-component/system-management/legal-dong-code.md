---
title: "법정동코드"
linkTitle: "법정동코드"
description: "법정동코드"
url: /common-component/system-management/common-code-manage/legal-dong-code/
menu:
  depth:
    name: "법정동코드"
    weight: 8
    parent: "common-code-manage"
---


# 법정동코드

## 개요

 법정동코드수신은 법정동코드의 변경정보를 시스템에서 주기적으로 수신 반영하고 변경사항을 관리하는 기능으로 구성되어 있다.

## 설명

 기관코드수신 패키지는 요소기술의 공통 패키지(cmm)에 대해서만 직접적인 함수적 참조 관계를 가진다.
 패키지 간 참조 관계 : [시스템관리 Package Dependency](../intro/package-reference.md/#시스템관리)

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.sym.ccm.acr.web.EgovAdministCodeRecptnController.java | 법정동코드수신 관리를 위한 컨트롤러 클래스 |
| Service | egovframework.com.sym.ccm.acr.service.EgovAdministCodeRecptnService.java | 법정동코드수신 관리를 위한 서비스 인터페이스 |
| ServiceImpl | egovframework.com.sym.ccm.acr.service.impl.EgovAdministCodeRecptnServiceImpl.java | 법정동코드수신 관리를 위한  서비스구현 클래스 |
| Model | egovframework.com.sym.ccm.acr.service.AdministCodeRecptn.java | 법정동코드수신 정보 Model 클래스 |
| VO | egovframework.com.sym.ccm.acr.service.AdministCodeRecptnVO.java | 법정동코드수신 관리를 위한 VO 클래스 |
| DAO | egovframework.com.sym.ccm.acr.service.impl.AdministCodeRecptnDAO.java | 법정동코드수신 정보 관리를 위한 데이터처리 클래스 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/acr/EgovAdministCodeRecptnList.jsp | 법정동코드수신 목록조회 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/acr/EgovAdministCodeDetail.jsp | 법정동코드 상세조회 페이지 |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_mysql.xml | 법정동코드 MySQL용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_cubrid.xml | 법정동코드 Cubrid용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_oracle.xml | 법정동코드 Oracle용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_tibero.xml | 법정동코드 Tibero용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_altibase.xml | 법정동코드 Altibase용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_maria.xml | 법정동코드 MariaDB용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_postgres.xml | 법정동코드 PostgreSQL용 QUERY XML |
| QUERY XML | resources/egovframework/mapper/com/sym/ccm/acr/EgovAdministCodeRecptn\_SQL\_goldilocks.xml | 법정동코드 Goldilocks용 QUERY XML |
| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-AdministCodeRecptn.xml | 법정동코드 Id생성 Idgen XML |

### 클래스 다이어그램

 ![image](./images/sym-legaldong-법정동코드_클래스다이어그램.jpg)

### ID Generation

#### ID Generation 관련 DDL 및 DML

 ID Generation Service를 활용하기 위해서 Sequence 저장테이블인  COMTECOPSEQ에 ADMIN_CODE_OPERT 항목을 추가해야 한다.

```sql
CREATE TABLE COMTECOPSEQ ( table_name varchar(16) NOT NULL,
           next_id DECIMAL(30) NOT NULL,
           PRIMARY KEY (table_name));
 
  INSERT INTO COMTECOPSEQ VALUES('ADMIN_CODE_OPERT','0');
```

#### ID Generation 환경설정(context-idgn-AdministCodeRecptn.xml)

```xml
<bean name="egovAdministCodeRecptnIdGnrService"
		class="egovframework.rte.fdl.idgnr.impl.EgovTableIdGnrService"
		destroy-method="destroy">
		<property name="dataSource" ref="egov.dataSource" />
		<property name="blockSize" 	value="1"/>
		<property name="table"	   	value="COMTECOPSEQ"/>
		<property name="tableName"	value="ADMIN_CODE_OPERT"/>
	</bean>
```

### 관련테이블

| 테이블명 | 테이블명(영문) | 비고 |
| --- | --- | --- |
| 법정동코드 | COMTCADMINISTCODE | 법정동코드에 대한 정보 |
| 법정동코드수신로그 | COMTCADMINISTCODERECPTNLOG | 법정동코드수신로그에 대한 정보 |

### 환경설정

 법정동코드수신을 사용하기 위해서는 EDI 모듈을 실행시 필요한 정보를 설정하여야 한다.
 이를 지정하기 위해서는 globals.properties 속성 파일에 추가 속성을 설정하여야 한다.
 globals.properties에 관련된 내용은 요소기술 프로퍼티 및 명령어 쉘스크립트 부분을 참조한다.

#### 관련 설정 사항

 ...
 # 법정동코드수신용
 CNTC.ADMINISTCODE.DIR.rcv       = /home/gccedi/rcv/
 CNTC.ADMINISTCODE.DIR.rcvold    = /home/gccedi/rcvold/
 CNTC.ADMINISTCODE.DIR.bin       = /home/gccedi/bin/
 CNTC.ADMINISTCODE.CMD.edircv    = gcc_edircv
 CNTC.ADMINISTCODE.CMD.edircvmsg = gcc_edircvmsg
 CNTC.ADMINISTCODE.INFO.userid   = 서버인증서아이디
 CNTC.ADMINISTCODE.INFO.userpw   = 서버인증서패스워드
 ...

 EDI 모듈에 따라 cmd file 이 실행바이너리 파일이거나 쉘스크립트 파일이 올 수 있음.

#### 법정동코드수신 scheduler 등록

 법정동코드수신 및 반영은 스케줄러를 통해 반영된다. 해당 스케줄러를 등록하기 위해서는 …/spring/context-scheduling.xml(예시)에 다음과 같은 스케줄러를 등록한다.

```xml
<!-- 법정동코드수신 처리 -->
    <bean id="administCodeReceiver"
        class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
        <property name="targetObject" ref="AdministCodeRecptnService" />
        <property name="targetMethod" value="insertAdministCodeRecptn" />
        <property name="concurrent" value="false" />
    </bean>

    <bean id="administCodeReceiverTrigger"
        class="org.springframework.scheduling.quartz.SimpleTriggerBean">
        <property name="jobDetail" ref="administCodeReceiver" />
        <!-- 시작하고 1분후에 실행한다. (milisecond) -->
        <property name="startDelay" value="60000" />
        <!-- 매 60초마다 실행한다. (milisecond) 데몬 형식으로 계속 기동 중 -->
        <property name="repeatInterval" value="60000" />
    </bean>

    <bean id="administCodeReceiverScheduler" class="org.springframework.scheduling.quartz.SchedulerFactoryBean">
        <property name="triggers">
            <list>
                <ref bean="administCodeReceiverTrigger" />
            </list>
        </property>
    </bean>
```

## 관련기능

 법정동코드는 법정동코드 수신, 법정동코드수신 목록조회, 법정동코드 상세조회 기능으로 구분된다.

### 법정동코드수신

 법정동코드수신 연계시 연계항목에 따라 DB, Model, ServiceImpl…등 연계항목 관련사항을 수정하여야 한다.
 ServiceImpl 예시

 ...
 // 실제 연계 항목 Mapping 작업
 administCodeRecptn.setChangeSeCode          (strTmp       );    // 명령                 :: 변경구분코드
 administCodeRecptn.setOccrrDe               (tokenData[ 1]);    // 날짜                 :: 발생일자
 administCodeRecptn.setAdministZoneCode      (tokenData[ 2]);    // 행정구역코드         :: 행정구역코드
 administCodeRecptn.setAdministZoneNm        (tokenData[ 7]);    // 행정구역명           :: 행정구역명
 administCodeRecptn.setLowestAdministZoneNm  (tokenData[ 8]);    // 최하위행정구역명     :: 최하위행정구역명
 administCodeRecptn.setCtprvnCode            (tokenData[ 3]);    // 시도코드             :: 시도코드
 administCodeRecptn.setSignguCode            (tokenData[ 4]);    // 시군구코드           :: 시군구코드
 administCodeRecptn.setEmdCode               (tokenData[ 5]);    // 읍면동코드           :: 읍면동코드
 administCodeRecptn.setLiCode                (tokenData[ 6]);    // 리코드               :: 리코드
 administCodeRecptn.setCreatDe               (tokenData[ 9]);    // 생성일자             :: 생성일자
 administCodeRecptn.setAblDe                 (tokenData[10]);    // 폐지일자             :: 폐지일자
 administCodeRecptn.setAblEnnc               (tokenData[11]);    // 폐지유무             :: 폐지유무
 administCodeRecptn.setUseAt                 (tokenData[11]);    // 폐지유무             :: 사용여부
 ...

### 법정동코드수신 목록조회

#### 비즈니스 규칙

 법정동코드수신 목록은 페이지 당 10건씩 조회되며 페이징은 10페이지씩 이루어진다. 검색조건은 법정동코드수신명에 대해서 수행된다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 목록조회 | /sym/ccm/acr/getAdministCodeRecptnList.do | selectAdministCodeRecptnList | "AdministCodeRecptnDAO.selectAdministCodeRecptnList" |
|  |  |  | "AdministCodeRecptnDAO.selectAdministCodeRecptnListTotCnt" |

 페이지 당 검색 범위를 변경하고자 하는 경우
 context-properties.xml 파일의 pageUnit, pageSize를 변경한다.(단 해당 설정은 전체 공통서비스 기능에 영향을 미친다.)

 ![image](./images/sym-legaldong-법정동코드수신목록.png)

 조회: 조회하기 위해서는 상단의 검색조건을 선택 후 해당하는 검색문자를 입력 후 조회 버튼을 클릭한다.
 목록클릭: 법정동코드 상세조회 화면으로 이동한다.

### 법정동코드 상세 조회

#### 비즈니스 규칙

 상세조회에는 삭제 처리가 포함되어 있고 삭제가 성공하면 법정동코드수신 목록 화면으로 이동한다.

#### 관련코드

 N/A

#### 관련화면 및 수행매뉴얼

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 상세조회 | /sym/ccm/acr/getAdministCodeDetail.do | selectAdministCodeDetail | "AdministCodeRecptnDAO.insertAdministCode" |

 ![image](./images/sym-legaldong-법정동코드상세.png)

 목록: 법정동코드 목록 화면으로 이동한다.

