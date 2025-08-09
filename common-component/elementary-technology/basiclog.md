---
  title: Basic 로그
  linkTitle: Basic 로그
  description: "JDK에서 제공하는 Logger 클래스를 이용하여 3가지 레벨로 로그를 남길 수 있는 기능을 제공한다."
  url: /common-component/elementary-technology/basiclog/
  menu:
    depth:
      name: Basic 로그
      weight: 10
      parent: "new-components-v3.2"
      identifier: "basiclog"
---



# 요소기술 - Basic 로그

## 개요

 JDK에서 제공하는 Logger 클래스를 이용하여 3가지 레벨로 로그를 남길 수 있는 기능을 제공한다.

## 설명

 사용법이 간단하며 로그를 콘솔에 출력 할 수 있고 파일로도 저장이 가능하다.  
OFF, FINEST, INFO 세 개의 레벨을 제공하며 레벨에 따라 메소드를 이용하여 간단하게 로그를 관리 할 수 있다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | egovframework.com.cmm.util.EgovBasicLogger.java | Basic 로그 처리 관련 유틸리티 |  |

## 환경설정

 EgovBasicLogger를 통해 로그를 파일로 저장하기 위해서는 %JAVA\_HOME%/jre/lib에 저장되어 있는 logging.properties 파일에 있는  
handlers 값을 다음과 같이 주어야 한다.

```bash
  	############################################################
  	#  	Default Logging Configuration File
  	#
  	# You can use a different file by specifying a filename
  	# with the java.util.logging.config.file system property.  
  	# For example java -Djava.util.logging.config.file=myfile
  	############################################################
 
  	############################################################
  	#  	Global properties
  	############################################################
 
 
  	# log를 파일로 저장하지 않고 콘솔에 출력 할 경우 handlers 값
        handlers= java.util.logging.ConsoleHandler
 
  	# log를 파일에 저장하고 콘솔에 출력 할 경우 handlers 값
        handlers= java.util.logging.FileHandler, java.util.logging.ConsoleHandler
```

## 사용방법

 EgovBasicLogger는 다음과 같은 메소드를 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| void | ignore(String message, Exception exception) | 기록이나 처리가 불필요한 경우 사용 |  |
| void | ignore(String message) | 기록이나 처리가 불필요한 경우 사용 |  |
| void | debug(String message, Exception exception) | 디버그 정보를 기록하는 경우 사용 |  |
| void | debug(String message) | 디버그 정보를 기록하는 경우 사용 |  |
| void | info(String message)) | 일반적이 정보를 기록하는 경우 사용 |  |

 다음은 ignore(String message)메소드를 이용하여 log를 콘솔에 출력하는 방법이다.

```java
import egovframework.com.cmm.util.EgovBasicLogger;
 
try{
 
   // 업무관련 로직
   ...
 
}
catch(Exception e){
 
   // Exception이 발생했을 경우 ignore메소드를 이용하여 OFF레벨로 콘솔에 log출력하기
   EgovBasicLogger.ignore("Test ignore!!!!");
}
```

## 참고자료

 **해당없음**