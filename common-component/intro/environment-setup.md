---
title: "공통컴포넌트 환경설정"
linkTitle: "환경설정"
description: "공통컴포넌트의 개발 및 운영 환경 설정 방법에 대해 설명합니다."
url: /common-component/intro/environment-setup/
menu:
  depth:
    name: "공통컴포넌트 환경설정"
    weight: 2
    parent: "common-intro"
    identifier: "environment-setup"
---
# 공통컴포넌트 환경설정

## 개요

표준프레임워크 4.3에서는 다음과 같은 방법으로 환경설정을 할 수 있습니다:

- web.xml 및 context-egovuserdetailshelper.xml 파일을 통한 설정
- Servlet 3.1 기능을 활용한 globals.properties를 통한 설정 간소화

## 주요 개념

### 데이터베이스 설정

globals.properties 설정파일을 기준으로 spring profile 서비스를 이용하여 데이터베이스 환경을 설정합니다.

- Globals.DbType 기준으로 context-datasource.xml 파일에 설정된 Spring Profile 기능에 의해 dataSource 빈이 활성화됩니다.
- 이 기능을 통해 테스트DB, 검증DB, 운영DB로 분리가 가능합니다.

### 인증/권한방식 설정

표준프레임워크 3.5 이하 버전에서 개발자가 수동으로 관련 XML 설정하던 불편한 점을
표준프레임워크 3.6 이상 버전에서는 globals.properties 설정만으로 인증/권한방식을 설정할 수 있습니다.

- dummy: 더미 방식으로 사용자 권한을 인증
- session: 세션 방식으로 사용자 권한을 인증
- security: spring security 방식으로 사용자 권한을 인증

### 로그인 인증 제한

무차별적인 로그인 시도에 대한 차단 기능을 제공합니다.

- Globals.login.Lock: 사용/미사용 설정 (기본값: true)
- Globals.login.LockCount: 인증 시도 횟수 설정 (기본값: 5)

## 설정 방법

### 1. 데이터베이스 설정

```properties
# DB서버 타입(mysql, oracle, altibase, tibero, cubrid, mariadb, postgres, goldilocks) - datasource 및 sqlMap 파일 지정에 사용됨
Globals.DbType = mysql

# mysql 설정 예시
Globals.mysql.DriverClassName=net.sf.log4jdbc.DriverSpy
Globals.mysql.Url=jdbc:log4jdbc:mysql://127.0.0.1:3336/com
Globals.mysql.UserName = com
Globals.mysql.Password = 
 
                        .
                        .
                        .
#oracle
#altibase
#tibero
#cubrid
#mariadb
#postgres
#goldilocks
```

데이터베이스 변경 시 pom.xml에 해당 JDBC 드라이버 의존성을 추가해야 합니다
3rd party library의 경우에는 직접 Local Repository에 library를 넣어 주거나 Nexus서버를 구성하여 다운로드 받을 수 있습니다. Nexus에 대한 자세한 설정은 [개발환경의 Nexus 페이지](/egovframe-development/deployment-tool/nexus)를 참조합니다.

```xml
<!-- mysql -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
<!-- oracle 11g driver -->
<dependency>
    <groupId>project</groupId>
    <artifactId>ojdbc6</artifactId>
    <version>11.2.0.3</version>
</dependency>
<!-- altibase driver -->
	<dependency>
		 <groupId>project</groupId>
		 <artifactId>altibase</artifactId>
		 <version>7.1.0</version>
	</dependency>
	<!-- tibero driver -->
	<dependency>
		<groupId>project</groupId>
		<artifactId>tibero5</artifactId>
		<version>5.0.0</version>
	</dependency>
	<!-- cubrid driver -->
	<dependency>
		<groupId>project</groupId>
		<artifactId>cubrid</artifactId>
		<version>10.2.0</version>
	</dependency>
	<!-- mariadb driver -->
	<dependency>
		<groupId>org.mariadb.jdbc</groupId>
		<artifactId>mariadb-java-client</artifactId>
		<version>3.4.0</version>
	</dependency>
	<!-- postgres driver -->
	<dependency>
		 <groupId>org.postgresql</groupId>
		 <artifactId>postgresql</artifactId>
		 <version>42.7.3</version>
	</dependency>
	<!-- goldilocks driver -->
	<dependency>
		<groupId>project</groupId>
		<artifactId>goldilocks8</artifactId>
		<version>8.0.0</version>
	</dependency>
```

### 2. 인증/권한방식 설정

Servlet 3.1 도입으로 web.xml을 dynamic하게 설정 가능하여 간소화가 가능해 졌습니다.
WebApplicationInitializer를 통해 egovframework.com.cmm.config.EgovWebApplicationInitializer 클래스에 의하여 설정 파일이 동적으로 설정 됩니다.
security 모드일때 DelegatingFilterProxy, EgovSpringSecurityLoginFilter, EgovSpringSecurityLogoutFilter의 설정내역이 FilterRegistration 빈에 등록 됩니다.
Spring Profile 기능으로 인증/권한방식에 따라서 egovUserDetailsHelper 빈을 동적으로 생성 합니다.

globals.properties 파일에 다음과 같이 설정합니다:

```properties
# 인증/권한 인증방식(dummy, session, security)
# dummy : 더미 방식으로 사용자 권한을 인증함
# session : 세션 방식으로 사용자 권한을 인증함
# security : spring security 방식으로 사용자 권한을 인증함
Globals.Auth = session
```

### 3. 로그인 인증 제한

```properties
# 로그인 인증 제한(login authentication limit)
# (사용 여부 설정값 : true, false)
Globals.login.Lock = true
# 인증 재시도 횟수
Globals.login.LockCount = 5
```