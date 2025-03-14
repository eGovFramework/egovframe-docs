---
title: Logback logging
linkTitle: "Logback logging"
description: SQLite를 이용하여 경량화된 로깅 처리를 하는 기본 사용법에 대해 설명한다.
url: "/egovframe-runtime/batch-layer/intro/batch-support-logback_logging/"
menu:
    depth:
        name: Logback logging
        weight: 2
        parent: "intro"
---
# Logback logging

## 개요

배치 처리시 로깅 처리를 위해 log4j2를 지원하고 있지만 경량화된 로깅 처리를 위해 Logback 로깅 처리를 지원한다

## 설명

### Logback pom.xml 설정

log4j, commons-logging 관련 라이브러리를 exclusion 처리하고, Logback 라이브러리를 등록한다.

```xml
<!-- log4j 관련 exclusion -->
<dependency>
	<groupId>egovframework.rte</groupId>
	<artifactId>egovframework.rte.bat.core</artifactId>
	<version>${egovframework.rte.version}</version>
	<exclusions>
		<exclusion>
			<artifactId>log4j-core</artifactId>
			<groupId>org.apache.logging.log4j</groupId>
		</exclusion>
		<exclusion>
			<artifactId>log4j-slf4j-impl</artifactId>
			<groupId>org.apache.logging.log4j</groupId>
		</exclusion>
		<exclusion>
			<artifactId>log4j-over-slf4j</artifactId>
			<groupId>org.slf4j</groupId>
		</exclusion>
		<exclusion>
			<artifactId>commons-logging</artifactId>
			<groupId>commons-logging</groupId>
		</exclusion>
	</exclusions>
</dependency>
 
<!-- commons-logging 관련 exclusion -->
<exclusion>
	<artifactId>commons-logging</artifactId>
	<groupId>commons-logging</groupId>
</exclusion>
 
<!-- logback 관련 라이브러리 등록 -->
<dependency>
	<groupId>ch.qos.logback</groupId>
	<artifactId>logback-core</artifactId>
	<version>1.1.7</version>
</dependency>
<dependency>
	<groupId>ch.qos.logback</groupId>
	<artifactId>logback-classic</artifactId>
	<version>1.1.7</version>
</dependency>
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>jcl-over-slf4j</artifactId>
  <version>1.7.21</version>
</dependency>
```

### SQLite 사용

logback 사용을 위해 logback.xml를 설정이 선행 되어야 한다.
설정관련 자세한 사항을 아래 링크 참고
- [logback](https://logback.qos.ch/manual/introduction.html) 

```xml
<!-- 설정 예시 -->
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>[logback]%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
		</encoder>
	</appender>
	<logger name="java.sql" level="DEBUG" />
	<logger name="egovframework" level="DEBUG" />
	<logger name="jdbc.sqltiming" level="DEBUG" />
	<logger name="org.springframework" level="DEBUG" />
	<root level="DEBUG">
		<appender-ref ref="STDOUT" />
	</root>
</configuration>
```

## 참고자료
* [logback introduction](https://logback.qos.ch/manual/introduction.html)
* [The logback manual](https://logback.qos.ch/manual/introduction)
