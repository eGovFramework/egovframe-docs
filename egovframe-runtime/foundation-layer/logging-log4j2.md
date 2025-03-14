---
title: Log4j2
linkTitle: "Log4j2"
description: Log4j 2는 Log4j의 차세대 버전으로서 비동기 로깅을 지원하여 애플리케이션의 성능에 미치는 영향을 최소화하고, 플러그인 아키텍처로 커스터마이징이 용이하며 다양한 출력 포맷과 로깅 레벨을 세밀하게 제어할 수 있다. XML, JSON, YAML 등 다양한 구성 파일 형식을 지원하여 설정이 유연하고, 구성 변경 시 서버를 재시작할 필요 없이 동적으로 적용할 수 있어 대규모 엔터프라이즈 애플리케이션에서도 널리 사용된다.
url: /egovframe-runtime/foundation-layer/logging/logging-log4j2/
menu:
    depth:
        name: Log4j2
        weight: 1
        parent: "logging"
        identifier: "log4j2"
---
## 설명

### Log4j 2 변경사항

- Java 6 이상 필요
- XML 환경설정 단순화 (Log4j 1.x 와 호환되지 않음)
- Property 파일을 통한 환경설정을 지원하지 않음
- JSON을 통한 환경설정 지원
- 파라미터 방식으로 Log Message 출력
- 환경설정 변경시 서버 재기동 없이 자동 재호출
- 필터링 기능 향상
- NoSQLAppender 등의 다양한 Appender 제공

### Log4j 2 추가기능

#### 1. Substituting Parameters

로그 메시지를 구성하는 방법으로, 기존 문자열 결합 방식과 달리 {} 안에 파라미터를 대입하여 로그 메시지를 생성하는 방법이다.  
아래 코드는 출력할 로그 메시지를 완성하기 전에 Log Level을 체크하고, isDebugEnabled인 경우에만 메서드를 수행한다.  

```java
logger.debug("Logging in user {} with birthday {}", user.getName(), user.getBirthdayCalendar());
```

#### 2. Formatting Parameters

Substituting Parameters 로깅 방식을 사용하면 코드 내에서 직접 formatting이 가능하다.  
이 기능을 사용하려면 getFormatterLogger() 메서드를 통해 Logger 오브젝트를 생성해야 한다.  
포맷 변환 문자와 형식은 Java.util.Formatter 클래스를 참조한다.

```java
public static Logger logger = LogManager.getFormatterLogger("egovframework");

logger.debug("Logging in user %1$s with birthday %2$tm %2$te,%2$tY", user.getName(), user.getBirthdayCalendar());
logger.debug("Integer.MAX_VALUE = %,d", Integer.MAX_VALUE);
logger.debug("Long.MAX_VALUE = %,d", Long.MAX_VALUE);

// 출력결과
// User John Smith with birthday 05 23, 1995
// Integer.MAX_VALUE = 2,147,483,647
// Long.MAX_VALUE = 9,223,372,036,854,775,807
```

#### 3. Flow Tracing

Log4j 2는 trace(), debug(), info() 등과 같은 로깅 메서드 뿐 아니라, 어플리케이션 실행 순서를 좀 더 쉽게 파악할 수 있도록 하는 추가적인 메서드를 제공한다.  

| 메서드 | 기능 | 위치 | 사용 |
| --- | --- | --- | --- |
| entry() | 로그의 시작을 표시, 전달된 메서드 파라미터 출력 | 로깅 메서드 시작부분 | logger.entry() or logger.entry(Object… params) |
| exit() | 로그의 끝을 표시, 리턴값 출력 | return문 or 로깅 메서드 끝부분 | logger.exit() or logger.exit(Object… result) |
| throwing() | 예외나 에러가 발생했을 때, 해당 예외/에러정보를 출력 | 예외발생 시 | throw logger.throwing(new MyException); |
| catching() | 예외을 catch했을 때, 해당 예외정보를 출력 | catch문 | logger.catching(e); |  

이러한 메서드들이 만드는 로깅 이벤트가 기본적인 로깅 이벤트와 분리될 수 있도록 디폴트 Log Level와 Marker가 설정되어 있다.  
이에 따라 entry와 exit 메서드는 TRACE 레벨에서만 출력되며 FLOW Marker를 통해 다른 로그 메세지로부터 분리(필터링)할 수 있고,  
throwing과 catching 메서드는 ERROR 레벨에서만 출력되며 EXCEPTION Marker를 통해 필터링할 수 있다.

| 메서드 | Log Level | Marker |
| --- | --- | --- |
| entry() | TRACE | ENTER or FLOW |
| exit() | TRACE | EXIT or FLOW |
| throwing() | ERROR | THROWING or EXCEPTION |
| catching() | ERROR | CATCHING or EXCEPTION |

```java
   public String saveDept(String deptNo) {

     logger.entry(deptNo); // 메서드 시작부분에 명시, 전달받은 파라미터 출력

     Dept dept = service.saveDept(deptNo);

     String nextPg = "redirect:/dept/deptList.do";

     return logger.exit(nextPg); // 메서드 종료부분에 명시, 리턴할 파라미터 출력
   }

   public static void main(String[] args) {
     saveDept("20");

     // 출력결과
     // TRACE saveDept - entry(20)
     // TRACE saveDept - exit(redirect:/dept/deptList.do)
   }
```

#### 4. Markers

한꺼번에 다량의 로그가 출력되면 어느 위치에서 문제가 발생했는지 정확하게 예측할 수 없다.  
또한 Log4j와 같은 Logging Framework를 사용하는 이유는 어플리케이션에서 발생하는 문제를 확인하고 디버깅 하기 위한 것이다.  
이는 원하는 시점에서 로그 정보의 필터링이 가능해야함을 뜻한다.

이미 로깅 메서드와 Logger의 Log Level 설정을 통해 출력할 로그를 필터링 할 수 있지만,  
Log4j 2에서는 Marker 기능을 통해 좀 더 상세한 필터링을 지원한다. 예를 들어, Flow Tracing 메서드와 기본적인 로깅 이벤트를 분리하고 싶거나, SQL문만 별도로 출력하고 싶은 경우에는 Marker 설정을 통해 기능을 구현할 수 있다.

Marker는 다음과 같은 특징을 갖는다.

- Marker name은 유일해야 한다.
- Marker는 final로 선언되어야 하며, 오직 하나의 Parent Marker를 갖는다.

```java
public class MyClass {
  private static final Logger LOGGER = LogManager.getLogger(MyClass.class);

  // Marker name = "SQL"
  private static final Marker SQL_MARKER = MarkerManager.getMarker("SQL");

  // Marker name = "SQL_UPDATE", Parent marker = SQL_MARKER
  private static final Marker UPDATE_MARKER = MarkerManager.getMarker("SQL_UPDATE", SQL_MARKER);

  // Marker name = "SQL_QUERY", Parent marker = SQL_MARKER
  private static final Marker QUERY_MARKER = MarkerManager.getMarker("SQL_QUERY", SQL_MARKER);

  public String doQuery(String table) {

    LOGGER.entry(table);

    LOGGER.debug(QUERY_MARKER, "SELECT * FROM {}", table); // select.log 파일에 출력됨

    return LOGGER.exit();
}

public String doUpdate(String table, Map<String, String> params) {

    LOGGER.entry(table);

    LOGGER.debug(UPDATE_MARKER, "UPDATE {} SET {}", table, formatCols()); // update.log 파일에 출력됨

    return logger.exit();
}
```

```xml
...
<Appenders>
  <File name="fileQuery" fileName="./logs/file/select.log">
    <MarkerFilter marker="SQL_QUERY" onMatch="ACCEPT" onMismatch="DENY" />
    <PatternLayout pattern="%level %m%n" />
  </File>
  <File name="fileUpdate" fileName="./logs/file/update.log">
    <MarkerFilter marker="SQL_UPDATE" onMatch="ACCEPT" onMismatch="DENY" />
    <PatternLayout pattern="%level %m%n" />
  </File>
  ...
</Appenders>
...
```

#### 참고자료

[Flow Tracing](http://logging.apache.org/log4j/2.x/manual/flowtracing.html)  
[Markers](http://logging.apache.org/log4j/2.x/manual/markers.html)

### Migration to Log4j 2 from Log4j 1.x

#### 1. Log4j 2 jar 추가 (log4j-api.jar, log4j-core.jar) + Log4j 1.x jar 제거

```xml
<!-- Log4j 1.2 -->
<!--
<dependency>
  <groupId>log4j</groupId>
  <artifactId>log4j</artifactId>
  <version>1.2</version>
</dependency>
-->

<!-- Log4j 2 -->
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-api</artifactId>
  <version>x.x.x</version>
</dependency>
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-core</artifactId>
  <version>x.x.x</version>
</dependency>
```

#### 2. Log4j 1.x -> Log4j 2 변환 Bridge jar 추가 (log4j-1.2-api.jar)

기존 Log4j 1.x API가 Log4j 2 API로 변환 처리될 수 있도록 Log4j 2 Bridge를 추가한다.

```xml
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-1.2-api</artifactId>
  <version>x.x.x</version>
</dependency>
```

#### 3. Log4j 1.x의 Logger API 변경

Log4j 2의 Logger 객체를 생성할 수 있도록, Logger 생성 메서드를 다음과 같이 변경한다.

|  | Log4j 1.x | Log4j 2 |
| --- | --- | --- |
| Package | **org.apache.log4j** | **org.apache.logging.log4j** |
| Logger 생성 | org.apache.log4j.Logger logger = org.apache.log4j.**Logger.getLogger();** | org.apache.logging.log4j.Logger logger = org.apache.logging.log4j.**LogManager.getLogger();** |

#### 4. Log4j 2 설정 추가 (log4j2.xml)

Log4j 2에서는 설정 태그들이 직관적이고 간단하게 변경되었다. 더 자세한 설명은 [Log4j 2 상세 설정](./logging-log4j2_configuration_file.md) 을 참조하도록 한다.

- Log4j 1.x

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE log4j:configuration PUBLIC "-//APACHE//DTD LOG4J 1.2//EN" "log4j.dtd">
<log4j:configuration xmlns:log4j='http://jakarta.apache.org/log4j/'>
  <appender name="STDOUT" class="org.apache.log4j.ConsoleAppender">
    <layout class="org.apache.log4j.PatternLayout">
      <param name="ConversionPattern" value="%d %-5p [%t] %C{2} (%F:%L) - %m%n"/>
    </layout>
  </appender>
  <category name="org.apache.log4j.xml">
    <priority value="info" />
  </category>
  <Root>
    <priority value ="debug" />
    <appender-ref ref="STDOUT" />
  </Root>
</log4j:configuration>
```

- Log4j 2

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
  <Appenders>
    <Console name="STDOUT" target="SYSTEM_OUT">
      <PatternLayout pattern="%d %-5p [%t] %C{2} (%F:%L) - %m%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="org.apache.log4j.xml" level="info"/>
    <Root level="debug">
      <AppenderRef ref="STDOUT"/>
    </Root>
  </Loggers>
</Configuration>
```

#### 참고자료

[Migration to Log4j 2](http://logging.apachttp://logging.apache.org/log4j/2.x/manual/migration.html)  
[Log4j 2 API Documentation](http://logging.apache.org/log4j/2.x/log4j-api/apidocs/index.html)  
[Log4j 2 Implementation Documentation](http://logging.apache.org/log4j/2.x/log4j-core/apidocs/index.html)