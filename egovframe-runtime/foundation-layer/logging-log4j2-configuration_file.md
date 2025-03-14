---
title: Log4j 2 환경설정 (설정 파일 사용 시)
linkTitle: "파일로 설정"
description: Log4j 2는 XML 형식의 설정 파일을 사용하여 Logger와 Appender, Layout 등을 정의할 수 있으며, 이를 통해 로그의 출력 위치와 형식을 설정할 수 있다. Logger는 로그 레벨과 Appender를 통해 로그의 출력 위치와 레벨을 제어하며, RollingFileAppender와 같은 다양한 Appender를 지원한다. Layout을 통해 로그 출력 형식을 지정하며, 특히 PatternLayout을 사용해 로그 메시지의 포맷을 세밀하게 설정할 수 있다.
url: /egovframe-runtime/foundation-layer/logging/logging-log4j2/logging-log4j2-configuration_file/
menu:
    depth:
        name: Log4j2 파일로 설정
        weight: 2
        parent: "log4j2"
---
# Log4j 2 환경설정 (설정 파일 사용 시)

## 개요

Log4j 2는 기존 Properties 파일 형식의 환경 설정을 지원하지 않으며,  
XML (log4j2.xml) 혹은 JSON (log4j2.json or log4j2.jsn) 파일 형식의 환경 설정만 가능하다.

아래는 XML 파일을 이용한 환경 설정에 대해서만 다루며, JOSN 방식은 Log4j 2 매뉴얼을 참고하도록 한다.

## 설명

### Log4j 2 XML Configuration

#### XML 파일 위치

XML 파일(log4j2.xml)을 작성하고, WEB-INF/classes 하위에 포함될 수 있도록 위치시킨다.  
Log4j 2가 초기화될 때 자동으로 위 설정 파일을 읽어들인다.

#### XML 파일 정의

Log4j 2에서는 XML 파일의 최상위 요소가 **&lt;Configuration&gt;** 으로 변경되었다.  
\<Configuration> 요소 아래에 Logger, Appender, Layout 설정 등과 관련한 하위 요소를 정의한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>

 <!-- Appender, Layout 설정 -->
 <Appenders>
  <Console name="console" target="SYSTEM_OUT">
   <PatternLayout/>
  </Console>
  <File name="file" fileName="./logs/file/sample.log" append="false">
   <PatternLayout pattern="%d %5p [%c] %m%n"/>
  </File>
 </Appenders>

 <!-- Logger 설정 -->
 <Loggers>
  <Logger name="egovLogger" level="DEBUG" additivity="false">
   <AppenderRef ref="console"/>
   <AppenderRef ref="file"/>
  </Logger>
  <Rootlevel="ERROR">
   <AppenderRef ref="console"/>
  </Root>
 </Loggers>

</Configuration>
```

#### 참고자료

[Log4j 2 Configuration](http://logging.apache.org/log4j/2.x/manual/configuration.html)  
[XML Syntax](http://logging.apache.org/log4j/2.x/manual/configuration.html#XML)  
[JSON Syntax](http://logging.apache.org/log4j/2.x/manual/configuration.html#JSON)

### Logger 설정

Logger는 로깅 작업을 수행하는 Log4j 주체로, Logger 설정을 제외한 모든 로깅 기능이 이 Logger를 통해 처리된다.  
사용자는 어플리케이션 내에서 사용할 Logger를 정의해야 하며, Log Level과 Appender 설정에 따라 출력 대상과 위치가 결정된다.

#### Logger 선언과 정의

Root Logger를 포함한 모든 Logger는 상위 요소인 **&lt;Loggers&gt;** 아래에 선언한다.  
Root Logger는 **&lt;Root&gt;** 요소로, 일반 Logger는 **&lt;Logger&gt;** 요소로 정의한다.  
Logger는 하나 이상 정의할 수 있으며, Root 요소를 반드시 정의해야 한다.

```xml
 <Loggers>
  <Logger>...</Logger>
  <Root>...</Root>
 </Loggers>
```

```xml
 <Loggers>
  <!-- attribute: name(Logger명), level(Log Level), additivity(중복로깅여부, true or false) -->
  <!-- element: AppenderRef(Appender명) -->
  <Logger name="X.Y" level="INFO" additivity="false">
   <AppenderRef ref="console"/>  
  </Logger>
  <Logger name="X" level="DEBUG" additivity="false">
   <AppenderRef ref="console"/>  
  </Logger>
  <Rootlevel="ERROR">
   <AppenderRef ref="console"/>
  </Root>
 </Loggers>
```

위에서 AppenderRef 요소에 지정한 "console" Appender가 없는 경우, 정상적인 로깅이 수행될 수 없다.

#### Logger 호출

Logger는 코드 내에서 다음과 같은 방법으로 호출할 수 있다.

```java
  package egovframe.sample;

  import org.apache.logging.log4j.LogManager;
  import org.apache.logging.log4j.Logger;

  public class LoggerTest {

   // (1) Logger Name이 "egovframe.sample.LoggerTest"인 Logger 설정을 따르는 Logger 객체 생성
   Logger logger1 = LogManager.getLogger();     
   // (2) 위와 동일             
   Logger logger2 = LogManager.getLogger(LoggerTest.class);  
   // (3) Logger Name이 "X"인 Logger설정을 따르는 Logger 객체 생성
   Logger logger3 = LogManager.getLogger("X");   

  }
```

(1), (2)과 같이 Logger Name에 해당하는 Logger가 설정 파일에 없는 경우, 다음 Logger Hierarchy 규칙에 따라 결정된다.  
결과적으로 (1), (2)에서 생성된 Logger 객체는 Root Logger 설정을 따른다.

#### Logger Hierarchy

사용자가 호출한 Logger 객체가 어떤 설정을 따르는지 이해하기 위해서는 Logger Hierarchy를 알고 있어야 한다.  
내부적으로 설정 파일에 정의된 각 Logger 설정에 따라 LoggerConfig 오브젝트가 생성되며,  
Logger Name에 따라 오브젝트 간 부모-자식 관계가 성립한다. 즉 부모 Logger의 설정을 자식 Logger가 상속받는다.  
예를 들어 "X.Y" Logger의 부모는 "X"이고, "X" Logger의 부모는 Root Logger(최상위)이다.

다음은 Hierarchy 규칙과 예시이다.

1) 호출한 Logger Name과 동일한 Logger가 있는 경우, 해당 Logger 설정을 따른다.  
2) 동일한 Logger는 없지만, Parent Logger가 존재하는 경우, Parent Logger 설정을 따른다.  
3) Parent Logger도 존재하지 않는 경우, Root Logger 설정을 따른다.  

| Logger Name | Assigned LoggerConfig | Level | Java Code | Description |
| --- | --- | --- | --- | --- |
| root | root | ERROR | LogManager.getLogger(“root”); | 설정 파일의 Root 설정을 따름 |
| X | X | DEBUG | LogManager.getLogger(“X”); | 설정 파일의 X Logger 설정을 따름 |
| X.Y | X.Y | INFO | LogManager.getLogger(“X.Y”); | 설정 파일의 X.Y Logger 설정을 따름 |
| X.Y.Z | X.Y | INFO | LogManager.getLogger(“X.Y.Z”); | X.Y.Z Logger 설정이 없으므로, 부모인 X.Y 설정을 따름 |
| X.YZ | X | DEBUG | LogManager.getLogger(“X.YZ”); | X.YZ Logger 설정이 없으므로, 부모인 X 설정을 따름 |
| Y | root | ERROR | LogManager.getLogger(“Y”); | Y Logger 설정이 없으므로, 부모인 Root 설정을 따름 |

#### Log Level

Log4j 2는 FATAL, ERROR, WARN, INFO, DEBUG, TRACE의 Log Level을 제공한다.  
각각 trace(), debug(), info(), warn(), error(), fatal()라는 로깅 메서드를 이용해 로그를 출력할 수 있다.  
로그 레벨은 다음과 같다. (FATAL &gt; ERROR &gt; WARN &gt; INFO &gt; DEBUG &gt; TRACE)

| 로그 레벨 | 설명 |
| --- | --- |
| FATAL | 아주 심각한 에러가 발생한 상태를 나타냄. 시스템적으로 심각한 문제가 발생해서 어플리케이션 작동이 불가능할 경우가 해당하는데, 일반적으로는 어플리케이션에서는 사용할 일이 없음. |
| ERROR | 요청을 처리하는중 문제가 발생한 상태를 나타냄. |
| WARN | 처리 가능한 문제이지만, 향후 시스템 에러의 원인이 될 수 있는 경고성 메시지를 나타냄. |
| INFO | 로그인, 상태변경과 같은 정보성 메시지를 나타냄. |
| DEBUG | 개발 시 디버그 용도로 사용한 메시지를 나타냄. |
| TRACE | 디버그 레벨이 너무 광범위한 것을 해결하기 위해서 좀더 상세한 상태를 나타냄. |

어플리케이션 수행 중 Log Level을 변경할 수도 있다. 이 때 Logger Configuration을 변경하는 것이므로, Logger 설정 정보를 참조하는 메서드를 호출할 수 있도록 org.apache.logging.log4j.Logger를 org.apache.logging.log4j.core.Logger로 캐스팅해야 한다.

Log Level 변경하려면 변경할 Level값을 파라미터로 setLevel() 메서드를 호출한다.  
setLevel() 호출 이후부터 Log Level이 변경되며, 지정된 로그레벨 이하의 Log Event는 무시된다.

```java
 package egovframe.sample;

 import org.apache.logging.log4j.LogManager;
 import org.apache.logging.log4j.Logger;

 public class LoggerTest {
  Logger logger = LogManager.getLogger(); // Root Logger 설정을 따름, Log Level: ERROR
  org.apache.logging.log4j.core.Logger targetLogger = (org.apache.logging.log4j.core.Logger) logger;

  targetLogger.debug("변경 전 - debug"); // 출력됨
  targetLogger.error("변경 전 - error"); // 출력 안됨


  targetLogger.setLevel(Level.DEBUG); // DEBUG, INFO, WARN, ERROR, FATAL 출력 가능
  targetLogger.debug("변경 후 - debug"); // 출력됨
  targetLogger.error("변경 후 - error"); // 출력됨	
}
```

자바에서는 C와 같이 전처리기의 기능이 없기 때문에 #ifdef DEBUG와 같은 형태와 같이 디버깅 때와 릴리즈 때의 디버깅코드를 각각 별도로 생성할 수가 없다. 따라서 Log4j의 이러한 기능은 로그관리에 있어서 상당히 편리하다.

#### 참고자료

자세한 설정은 [Log4j 2 Logger](http://logging.apache.org/log4j/2.x/manual/configuration.html#Loggers) 매뉴얼을 참고하도록 한다.

### Appender 설정

Appender는 로그가 출력되는 위치를 나타낸다.  
XXXAppender로 끝나는 클래스들의 이름을 보면, 출력 위치를 어느 정도 짐작할 수 있다.

Log4j 2는 Console, File, RollingFile, Socket, DB 등 다양한 로그 출력 위치와 방법을 지원한다.  
기존 Log4j 1.x와 크게 달라진 점은 Appender 종류를 class 속성값으로 구분한 것과 달리, Log4j 2에서는 태그로 구분한다.

#### Appender 선언과 정의

본 페이지에서는 자주 사용되는 Console, File, RollingFile, JDBC Appender에 대해서만 설명한다.  
출력 위치에 따라 Appender 종류와 설정 태그가 달라지며, 아래 표는 각 Appender 정의 태그와 출력 위치이다.

| Appenders           | 태그명          | 출력 위치             |
|---------------------|----------------|-----------------------|
| **ConsoleAppender**    | `<Console>`    | 콘솔에 출력           |
| **FileAppender**       | `<File>`       | 파일에 출력           |
| **RollingFileAppender**| `<RollingFile>`| 조건에 따라 파일에 출력 |
| **JDBCAppender**       | `<JDBC>`       | RDB Table에 출력      |

모든 Appender 요소는 상위 요소인 **&lt;Appenders&gt;** 아래에 선언한다.

```xml
 <Appenders>
  <Console>...</Console>
  <File>...</File>
  <RollingFile>...</RollingFile>
  <JDBC>...</JDBC>
 </Appenders>
```

Appender 요소는 name 속성값을 가지며, name 속성에 Appender 이름을 지정한다. name 속성값은 Logger가 로그 출력에 사용할 Appender를 참조하기 위해 사용한다. 또한 Appender 요소의 하위 요소로 로그 출력 패턴인 Layout을 정의한다.  
아래는 ConsoleAppender와 PatternLayout을 사용한 샘플코드이다.

```xml
 <Appenders>
   <Console name="console" target="SYSTEM_OUT">
    <PatternLayout /> <!-- 디폴트 패턴 적용, %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n -->
  </Console>
 </Appenders>
 <Loggers>
  <Logger name="egovLogger" level="DEBUG" additivity="false">
   <AppenderRef ref="console" />
  </Logger>
  <Rootlevel="ERROR">
   <AppenderRef ref="console" />
  </Root>
 </Loggers>
```

#### Appender 종류

다음은 각 Appender 정의 시 필요한 기본 설정에 대한 설명이다.  

##### ConsoleAppender

로그를 콘솔에 출력하기 위한 Appender

```xml
 <!-- attribute: name(Appender명), target(출력방향지정, "SYSTEM_OUT" or "SYSTEM_ERR"(default)), follow, ignoreExceptions -->
 <!-- element: Layout(출력패턴설정), Filters -->
 <Console name="console" target="SYSTEM_OUT">
  <PatternLayout pattern="%d %5p [%c] %m%n" />
 </Console>
```

##### FileAppender

로그를 파일에 출력하기 위한 Appender

```xml
 <!-- attribute: name(Appender명), fileName(target파일명), append(이어쓰기여부, true(default) or false), locking, immediateFlush, ignoreExceptions, bufferedIO -->
 <!-- element: Layout(출력패턴설정), Filters -->
 <!-- append="false"이면 매번 로깅 시 기존 로그 파일을 clear하고 새로 로깅 -->
 <File name="file" fileName="./logs/file/sample.log" append="false">
  <PatternLayout pattern="%d %5p [%c] %m%n" />
 </File>	
 <File name="mdcFile" fileName="./logs/file/mdcSample.log" append="false">
  <!-- Thread Context Map(also known as MDC) 객체의 key와 매칭되는 value를 로깅 - %X{key} -->
  <!-- ex) ThreadContext.put(“testKey”, “testValue”);인 경우, 레이아웃 패턴 %X{testKey}에 의해 “testValue” 로깅 -->
  <PatternLayout pattern="%d %5p [%c] [%X{class} %X{method} %X{testKey}] %m%n" />
 </File>
```

##### RollingFileAppender

TriggeringPolicy와 RolloverStrategy에 따라 로그를 파일에 출력하기 위한 Appender로,  
FileAppender는 지정한 파일에 로그가 계속 남으므로 한 파일의 크기가 지나치게 커질 수 있고, 계획적인 로그관리가 불가능해진다.  
그러나 RollingFileAppender는 파일의 크기 또는 파일 백업 인덱스 등의 지정을 통해서 특정 크기 이상으로 파일 크기가 커지게 되면,  
기존파일(target)을 백업파일(history)로 바꾸고, 다시 처음부터 로깅을 시작한다.

```xml
 <!-- attribute: name(Appender명), fileName(target파일명), filePattern(history파일명), append, immediateFlush, ignoreExceptions, bufferedIO -->
 <!-- element: Layout(출력패턴설정), Filters, Policy(file rolling 조건 설정), Strategy(file name과 location 관련 설정) -->
 <RollingFile name="rollingFile" fileName="./logs/rolling/rollingSample.log" filePattern="./logs/rolling/rollingSample.%i.log">
  <PatternLayout pattern="%d %5p [%c] %m%n" />
  <Policies>
   <!-- size 단위: Byte(default), KB, MB, or GB -->
   <SizeBasedTriggeringPolicy size="1000" />
  </Policies>
  <!-- 기존 maxIndex 속성이 Strategy 엘리먼트로 변경됨 -->
  <!-- index는 min(default 1)부터 max(default 7)까지 증가, 아래에는 max="3"으로 settting -->
  <!-- fileIndex="min"이므로 target file의 size가 1000 byte를 넘어가면, fileIndex가 1(min)인 history file에 백업 (fixed window strategy) -->
  <!-- 그 다음 1000 byte를 넘어가면, rollingSample.1.log을 rollingSample.2.log 파일에 복사하고, target 파일을 rollingSample.1.log에복사한 후 target 파일에 새로 로깅 -->
  <DefaultRolloverStrategy max="3" fileIndex="min" />
 </RollingFile>
```

- DailyRollingFileAppender  
기존 DailyRollingFileAppender가 삭제되고, RollingFileAppender에서 \<TimeBasedTriggeringPolicy> 엘리먼트로 설정 가능하도록 변경되었다. 설정한 날짜 또는 조건에 맞춰 로깅을 수행하며, interval 속성을 이용해 rolling 간격을 지정할 수 있다.

```xml
 <RollingFile name="rollingFile" fileName="./logs/rolling/dailyRollingSample.log" filePattern="./logs/daily/dailyRollingSample.log.%d{yyyy-MM-dd-HH-mm-ss}">
  <PatternLayout pattern="%d %5p [%c] %m%n" />
  <Policies>
   <!-- interval(default 1)이므로 1초 간격으로 rolling 수행 --> 
   <TimeBasedTriggeringPolicy />
  </Policies>
 </RollingFile>
```

##### JDBCAppender

로그를 RDB에 출력하기 위한 Appender로,  
Connection 객체를 제공하기 위한 JNDI DataSource 혹은 Connection Factory Method를 함께 정의해야한다.

```xml
 <!-- attribute: name(Appender명), tableName(RDB Table명), columnConfigs, filter, bufferSize, ignoreExceptions, connectionSource -->
 <!-- element: DataSource(jndi datasource 정보), ConnectionFactory(Connection Factory 정보), Column(Table Column명) -->
 <!-- 테이블명이 db_log인 테이블에 로깅됨 -->
 <JDBC name="db" tableName="db_log">
  <!-- DB Connection을 제공해줄 클래스와 메서드명 정의 -->
  <!-- JDBCAppender가 EgovConnectionFactory.getDatabaseConnection() 메서드를 호출 -->
  <ConnectionFactory class="egovframework.rte.fdl.logging.db.EgovConnectionFactory" method="getDatabaseConnection" />
   <!-- log event가 insert될 컬럼 설정, insert될 값은 PatternLayout의 pattern 사용 -->
   <Column name="eventDate" isEventTimestamp="true" />
   <Column name="level" pattern="%p" />
   <Column name="logger" pattern="%c" />
   <Column name="message" pattern="%m" />
   <Column name="exception" pattern="%ex{full}" />
 </JDBC>
```

표준프레임워크에서는 Connection Factory 역할을 하는 EgovConnectionFactory를 제공하고 있으며, 어플리케이션에서 설정한 dataSource 빈을 주입받아 싱글톤을 생성한다. 이를 위해 다음과 같이 빈정의를 추가해야한다.

```xml
 <bean id="egovConnectionFactory" class="egovframework.rte.fdl.logging.db.EgovConnectionFactory">
  <property name="dataSource" ref="dataSource" />
 </bean>
```

WAS에서 제공하는 DataSource를 사용하려면, 위 \<ConnectionFactory> 부분을 \<DataSource jndiName=”…” />으로 변경한다.

#### 참고자료

각 Appender 요소에서 정의할 수 있는 하위 요소와 속성이 다르므로, 자세한 설정은 각 매뉴얼을 참조하도록 한다.

[Log4j 2 Appneders](http://logging.apache.org/log4j/2.x/manual/appenders.html)  
[ConsoleAppender](http://logging.apache.org/log4j/2.x/manual/appenders.html#ConsoleAppender)  
[FileAppender](http://logging.apache.org/log4j/2.x/manual/appenders.html#FileAppender)  
[RollingFileAppender](http://logging.apache.org/log4j/2.x/manual/appenders.html#RollingFileAppender)  
[JDBCAppender](http://logging.apache.org/log4j/2.x/manual/appenders.html#JDBCAppender)

### Layout 설정

Layout은 발생한 로그 이벤트의 포맷을 지정하고, 원하는 형식으로 로그를 출력할 수 있다.  
Appenders 설정과 마찬가지로 Log4j 2에서는 Layout을 class 속성이 아닌 태그로 구분한다.

출력 형식에 따라 Layout의 종류가 달라지며, 아래와 같은 Layouts을 제공한다.

<table>
  <tr>
    <td colspan="6">내용</td>
  </tr>
  <tr>
    <td>HTMLLayout</td>
    <td><b>PatternLayout</b></td>
    <td>RFC5424Layout</td>
    <td>SerializedLayout</td>
    <td>SyslogLayout</td>
    <td>XMLLayout</td>
  </tr>
</table>

본페이지는 위의 Layouts 중 일반적으로 디버깅에 가장 적합한 PatternLayout만 설명한다.  

#### PatternLayout 선언과 정의

PatternLayout은 Appender 요소의 하위 요소로 정의한다.

```xml
 <Console>
  <!-- 디폴트 패턴 적용, "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n" -->
  <PatternLayout/>
 </Console>
```

\<PatternLayout/>을 선언하면 디폴트 pattern이 적용되며, pattern 속성을 이용하여 일자, 시간, 클래스, 로거명, 메시지 등 여러 정보를 선택하여 다양한 조합의 로그 메시지를 출력할 수 있다.

##### PatternLayout의 pattern

%로 시작하고 %뒤에는 format modifiers와 conversion character로 정의한다.  
예) %d{HH:mm:ss.SSS} \[%thread\] %-5level %logger{36} - %msg%n

| 패턴 | 설명 |
| --- | --- |
| c, logger | 로깅 이벤트를 발생시키기 위해 선택한 로거의 이름을 출력 |
| C, class | 로깅 이벤트가 발생한 클래스의 풀네임명을 출력 |
| M, method | 로깅 이벤트가 발생한 메서드명을 출력 |
| F, file | 로깅 이벤트가 발생한 클래스의 파일명을 출력 |
| l, location | 로깅 이벤트가 발생한 클래스의 풀네임명.메서드명(파일명:라인번호)를 출력 |
| d, date | 로깅 이벤트의 일자와 시간을 출력,\\\\SimpleDateFormat클래스에 정의된 패턴으로 출력 포맷 지정가능 |
| L, line | 로깅 이벤트가 발생한 라인 번호를 출력 |
| m, msg, message | 로그문에서 전달된 메시지를 출력 |
| n | 줄바꿈 |
| p, level | 로깅 이벤트의 레벨을 출력 |
| r, relative | 로그 처리시간 (milliseconds) |
| t, thread | 로깅 이벤트가 발생한 스레드명을 출력 |
| %% | %를 출력하기 위해 사용하는 패턴 |

#### 참고자료

[Log4j 2 Layouts](http://logging.apache.org/log4j/2.x/manual/layouts.html)  
[PatternLayout](http://logging.apache.org/log4j/2.x/manual/layouts.html#PatternLayout)

## 참고자료

[Apache Logging Services Project](http://logging.apache.org/index.html)