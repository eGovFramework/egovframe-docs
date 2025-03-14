---
title: SLF4J
linkTitle: "SLF4J"
description: SLF4J는 다양한 로깅 프레임워크와 연계할 수 있는 추상화 계층을 제공하며, Log4j 2 또는 Logback과 함께 사용 가능하다. 기존의 Log4j 1.x나 Commons Logging을 SLF4J로 마이그레이션하려면, Bridge jar를 추가하고 logback.xml로 설정 파일을 변경해야 한다.
url: /egovframe-runtime/foundation-layer/logging/logging-slf4j/
menu:
    depth:
        name: SLF4J
        parent: "logging"
        weight: 1
---
## SLF4J

### Getting Started

SLF4J(Simple Logging Facade For Java)는 특정 Logging 서비스 구현체에 종속되지 않도록 추상화 계층을 제공하며,  
Jakarta Commons Logging(JCL), Log4j, Logback 등과 함께 사용할 수 있다.  
다음은 SLF4J 샘플 예제이다.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Slf4JLoggerTest {

   // SLF4J를 이용한 Logger 오브젝트 생성
   private static final Logger LOGGER = LoggerFactory.getLogger(Slf4JLoggerTest.class);

   // Parameterized logging - String 타입
   String message = "Hello, eGovFrame 3.0";
   String message2 = "Welcome to eGovFrame 3.0";

   LOGGER.debug("SLF4J Logger - {}", message); // 출력결과 - SLF4J Logger - Hello, eGovFrame 3.0
   LOGGER.debug("SLF4J Logger - {} and {}", message, message2); // 출력결과 - SLF4J Logger - Hello, eGovFrame 3.0 and Welcome to eGovFrame 3.0

   // Parameterized logging - Object 타입
   Object[] args = new Object[3];
   args[0] = "1";
   args[1] = Integer.valueOf("2");
   args[2] = new Date().toString();

   LOGGER.debug("SLF4J Logger - {}, {}, {}", args); // 출력결과 - SLF4J Logger - 1, 2, Fri Mar 23 11:08:28 KST 2014
}
```

#### 1. SLF4J 기본 설정

1) SLF4J API를 사용하기 위해 **slf4j-api.jar를 추가**한다.

```xml
<!-- SLF4J -->
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-api</artifactId>
  <version>x.x.x</version>
</dependency>
```

2) Logging 충돌 방지를 위해 Spring의 Default Logging Framework인 **commons-logging.jar를 제거**하되,  
기존 Commons Logging API가 적절하게 변환되어 처리될 수 있도록 SLF4j JCL Bridge인 **jcl-over-slf4j.jar를 추가**한다.

```xml
<!-- Exclude Commons Logging in favor of SLF4J -->
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-context</artifactId>
  <version>${spring.maven.artifact.version}</version>
  <exclusions>
    <exclusion>
      <groupId>commons-logging</groupId>
      <artifactId>commons-logging</artifactId>
    </exclusion>
  </exclusions>
</dependency>

<!-- SLF4J JCL Bridge -->
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>jcl-over-slf4j</artifactId>
  <version>x.x.x</version>
</dependency>
```

#### 2. Logging 구현체 설정

1) SLF4J가 컴파일 시에 Logging 구현체를 사용할 수 있도록 구현체별 **SLF4J Binding jar와 Implementation jar를 추가**한다.

| Logging 구현체 | SLF4J Binding jar |
| --- | --- |
| Log4j 2 | log4j-slf4j-impl.jar |
| Log4j 1.2 | slf4j-log4j12.jar |
| JDK 1.x Logging | slf4j-jdk14.jar |
| NOP | slf4j-nop.jar |
| JCL | slf4j-jcl.jar |
| Logback | logback-classic.jar, logback-core.jar |

- Log4j 1.2 구현체 사용 시

```xml
<!--  SLF4J Log4j1.2 Binding -->
<dependency> 
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-log4j12</artifactId>
  <version>x.x.x</version>
</dependency>

<!-- Log4j 1.2 -->
<dependency>
  <groupId>log4j</groupId>
  <artifactId>log4j</artifactId>
  <version>1.2</version>
</dependency>
```

- Log4j 2 구현체 사용 시

```xml
<!-- Log4j2 SLF4J Binding -->
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-slf4j-impl</artifactId>
  <version>x.x.x</version>
</dependency>

<!-- Log4j 2 -->
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-api</artifactId>
  <version>x.x.x</version>
</dependency>
```

#### 3. SLF4J Logger 객체 생성과 메서드 사용

1) Logger 객체 생성

```java
  private static final Logger LOGGER = LoggerFactory.getLogger(Slf4JLoggerTest.class);
```

2) 로깅 메서드 호출  

```java
  // {}-placeholder를 이용한 Parameterized Logging
  String message = "Hello, eGovFrame 3.0";

  LOGGER.debug("SLF4J Logger - {}", message);
```

### Migration to SLF4J from Legacy APIs

기존 Legacy API을 유지한 채 SLF4J를 함께 사용하려면, SLF4J와 레거시 API를 연결할 수 있는 Bridge jar가 필요하다.  
아래에서는 Log4j 1.x와 JCL 레거시를 기준으로 설명한다.

#### 1. Logging 구현체 jar를 SLF4J Bridge jar로 대체

이는 각 구현체의 Logging 제어권을 SLF4J로 넘긴다는 것을 의미하며, 레거시 API를 유지하기 위해서 필요한 작업이다.

1) Log4j 1.x 유지 시, log4j.jar를 log4j-over-slf4j.jar로 대체

```xml
<!-- Log4j 1.x -->
<!-- 
<dependency>
  <groupId>log4j</groupId>
  <artifactId>log4j</artifactId>
  <version>x.x.x</version>
</dependency>
-->

<!-- SLF4J Log4j 1.x Bridge -->  
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>log4j-over-slf4j</artifactId>
  <version>x.x.x</version>
</dependency>
```

(주의) log4j-over-slf4j.jar는 slf4j-log4j12.jar(SLF4j Binding)과 동시에 사용할 수 없다.

2) JCL(Jakarta Commons Logging) 유지 시, commons-logging.jar를 jcl-over-slf4j.jar로 대체

```xml
<!-- Commons Logging -->
<!--
<dependency>
  <groupId>commons-logging</groupId>
  <artifactId>commons-logging</artifactId>
  <version>1.1.1</version>
</dependency>
-->

<!-- SLF4j JCL Bridge -->
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>jcl-over-slf4j</artifactId>
  <version>x.x.x</version>
</dependency>
```

#### 2. 환경설정 파일을 logback으로 변경

log4j 환경설정 파일은 SLF4J가 인식할 수 없기 때문에, 기존 환경설정을 logback으로 변경해야한다.  
[log4j properties file translator](http://logback.qos.ch/translator/) 를 이용하거나 [logback manual](http://logback.qos.ch/manual/index.html) 을 참조하여 변경할 수 있다.

다음은 logback.xml 샘플이다.

```xml
<configuration>
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <!-- encoders are assigned the type
         ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="debug">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

## 참고 자료

- [SLF4J](http://www.slf4j.org/)
- [Logback](http://logback.qos.ch/)