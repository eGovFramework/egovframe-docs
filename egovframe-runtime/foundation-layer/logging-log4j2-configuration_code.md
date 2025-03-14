---
title: Log4j 2 환경설정 (코드 내에서 직접 설정 시)
linkTitle: "코드로 설정"
description: Log4j 2 환경설정을 코드 내에서 직접 제어하여 Logger 객체를 생성하고, 기본 설정을 수정할 수 있다. 예시에서는 ConsoleAppender를 FileAppender로 변경하고 로그 레벨을 DEBUG로 설정하는 방법을 설명한다. Logger 설정 관련 메서드들을 사용하여 Appender와 Layout, Log Level을 동적으로 변경할 수 있다.
url: /egovframe-runtime/foundation-layer/logging/logging-log4j2/logging-log4j2-configuration_code/
menu:
    depth:
        name: Log4j2 코드로 설정
        weight: 1
        parent: "log4j2"
---
# Log4j 2 환경설정 (코드 내에서 직접 설정 시)

## 개요

Log4j 2 환경 설정(Appender, Layout, Log Level 등)을 코드 내에서 직접 제어할 수 있다.  
아래는 별도의 외부 설정파일 없이도 로깅할 수 있는 방법을 설명한다.

## 설명

#### 사용 방법

별도의 Log4j 2 설정파일 없이도 코드 내에서 Logger 객체를 획득하여 로깅이 가능하다.  
LogManager.getLogger() 메서드를 통해 Logger 객체를 생성하며, Log4j 2는 디폴트로 설정된 Logger 객체를 반환한다.  
디폴트 Logger 객체의 기본적인 디폴트 설정은 다음과 같다.  

```properties
  Log Level : ERROR
  Appender  : ConsoleAppender
  Layout    : PatternLayout
  pattern   : %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
```

 위 Logger 객체를 org.apache.logging.log4j.core.Logger로 캐스팅하면, Log Level, Appender, Layout 등 설정을 변경할 수 있다.  
예시에서 사용된 설정 관련 메서드는 다음과 같다. 더 자세한 정보는 Log4j 2 API를 참조하도록 한다.  

```java
  LogManager.getLogger()                                                -- Logger 생성
  Logger.addAppender(), Logger.removeAppender(), Logger.getAppenders()  -- Logger에 Appender 추가 및 제거, 획득
  Layout.createLayout()                                                 -- Layout 생성
  Appender.createAppender(), Appender.removeAppender()                  -- Appender 생성 및 삭제
  Logger.setLevel(), Logger.getLevel()                                  -- Log Level 설정 및 획득
```

#### 사용 예시

```java
@Test
public void log4j2ConfigTest() {

	// 디폴트 Logger 생성
	Logger logger = (Logger) LogManager.getLogger();

	// 디폴트 설정 확인
	// Log Level: ERROR
	assertEquals(Level.ERROR, logger.getLevel());
	// Appender: Console
	Map<String, Appender> appenders = logger.getAppenders();
	assertEquals(1, appenders.size()); 
	assertEquals(ConsoleAppender.class, appenders.get("Console").getClass());
	// Layout: Pattern
	ConsoleAppender console = (ConsoleAppender) appenders.get("Console");
	assertEquals(PatternLayout.class, console.getLayout().getClass());
	PatternLayout pattern = (PatternLayout) console.getLayout();
	assertEquals("%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n", pattern.toString());

	// 설정 변경 전: ERROR Level 이상 로그만 출력됨
	logger.debug("변경 전: [DEBUG] Test log4j 2.");
	logger.info("변경 전: [INFO] Test log4j 2.");
	logger.warn("변경 전: [WARN] Test log4j 2.");
	logger.error("변경 전: [ERROR] Test log4j 2.");
	logger.fatal("변경 전: [FATAL] Test log4j 2.");

	/*
	출력결과
	===================
	14:17:09.930 [main] ERROR egovframework.rte.fdl.logging.LogTest - 변경 전: [ERROR] Test log4j 2.
	14:17:09.931 [main] FATAL egovframework.rte.fdl.logging.LogTest - 변경 전: [FATAL] Test log4j 2
	*/

	// 디폴트 설정 변경
	logger.removeAppender(console);
	// Appender: File
	PatternLayout layout = PatternLayout.createLayout("%m%n", null, null, null, null, null);
	FileAppender file = FileAppender.createAppender("./logs/file/promatic.log", "false", "false", "file", "false", "true", "false", null, layout, null, "false", null, null); 
	logger.addAppender(file);

	// Log Level: DEBUG
	logger.setLevel(Level.DEBUG);

	// 설정 변경 후: DEBUG Level 이상 로그가 file(promatic.log)에 출력됨
	logger.debug("변경 후: [DEBUG] Test log4j 2.");
	logger.info("변경 후: [INFO] Test log4j 2.");
	logger.warn("변경 후: [WARN] Test log4j 2.");
	logger.error("변경 후: [ERROR] Test log4j 2.");
	logger.fatal("변경 후: [FATAL] Test log4j 2.");

	/* 
	출력결과
	===================
	변경 후: [DEBUG] Test log4j 2.
	변경 후: [INFO] Test log4j 2.
	변경 후: [WARN] Test log4j 2.
	변경 후: [ERROR] Test log4j 2.
	변경 후: [FATAL] Test log4j 2. 
	*/

}
```

#### 참고자료

 [Apache Log4j Core 2.0-rc1 API](http://logging.apache.org/log4j/2.x/log4j-core/apidocs/index.html)