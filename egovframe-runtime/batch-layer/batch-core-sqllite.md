---
title: SQLite
linkTitle: "SQLite"
description: SQLite를 이용한 경량화된 Repository를 사용하기 위한 사용법에 대해 설명한다.
url: /egovframe-runtime/batch-layer/intro/batch-core-sqllite/
menu:
    depth:
        name: SQLite
        weight: 1
        parent: "intro"
---
# SQLite

## 개요

배치 처리시 경량화된 Repository를 사용을 위한 SQLite 처리를 지원한다.

## 설명

### SQLite pom.xml 설정

sqlite 라이브러리 사용을 위해 dependency를 추가 한다.

```xml
<dependency>
	<groupId>org.xerial</groupId>
	<artifactId>sqlite-jdbc</artifactId>
	<version>x.x.x</version>
</dependency>
```
### SQLite 사용

SQLite 사용을 위해 데이터베이스 설정을 하고 repository 생성을 위한 기초데이터를 설정 한다.

```xml
<!-- SQLite database  설정 -->
<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
	<property name="driverClassName" value="org.sqlite.JDBC" />
	<property name="url" value="jdbc:sqlite:repository.sqlite" />
	<property name="username" value="" />
	<property name="password" value="" />
</bean>

<!-- SQLite 기초데이터 설정 -->
<jdbc:initialize-database data-source="dataSource">
	<jdbc:script location="org/springframework/batch/core/schema-drop-sqlite.sql" />
	<jdbc:script location="org/springframework/batch/core/schema-sqlite.sql" />
 </jdbc:initialize-database>
```