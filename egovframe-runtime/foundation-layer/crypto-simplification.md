---
title: Crypto 간소화 서비스
linkTitle: "Crypto 간소화"
description: 표준프레임워크 3.8부터 ARIA 알고리즘을 기반으로 XML Schema와 properties 파일을 통해 간편하게 암/복호화 설정과 중요한 정보 보호를 지원한다.
url: /egovframe-runtime/foundation-layer/crypto/crypto-simplification/
menu:
    depth:
        name: Crypto 간소화 서비스
        weight: 2
        parent: "crypto"
---
# Crypto 간소화 서비스

## 개요

표준프레임워크 3.8 부터 ARIA 블록암호 알고리즘 기반 암/복호화 설정을 간소화 할 수 있는 방법을 제공한다.
내부적으로 필요한 설정을 가지고 있고, <acronym title="Extensible Markup Language">XML</acronym> Schema를 통해 필요한 설정만을 추가할 수 있도록 제공한다.
또한 globals.properties 설정 파일의 중요 정보 Url, UserName, Password 항목을 암/복호화 처리 할 수 있도록 제공한다.
그외에 정보는 properties 파일에 암호화 데이터 설정후 #{egovEnvCryptoService.decrypt('…')} 복호화 기능을 제공한다.

## XML namespace 및 schema 설정

설정 간소화 기능을 사용하기 위해서는 다음과 같은 xml 선언이 필요하다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:egov-crypto="http://maven.egovframe.go.kr/schema/egov-crypto"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://maven.egovframe.go.kr/schema/egov-crypto http://maven.egovframe.go.kr/schema/egov-crypto/egov-crypto-4.2.0.xsd">
```

## Crypto Config 설정

Security에 대한 기본 설정 정보를 제공한다.
**algorithmKey**, **algorithmKeyHash** 값을 하단 <b>[Crypto algorithmKey, algorithmKeyHash 생성]에 의해 생성된 값을 입력</b>한다.
algorithmKey, algorithmKeyHash 키의 노출을 피하고 싶다면 설정 파일에서 해당 항목 삭제 후
하단 [WAS VM arguments 환경 변수 등록(옵션)]을 참고하여 진행한다.

예:

```xml
<egov-crypto:config id="egovCryptoConfig"
	initial="true"
	crypto="true"
	algorithm="SHA-256"
	algorithmKey="(생성값)"
	algorithmKeyHash="(생성값)"
	cryptoBlockSize="1024"
/>
```

### 속성 설명

|    속성                        |     설명                                                               |     필수여부      |     비고                                                            |
|------------------------------|----------------------------------------------------------------------|---------------|-------------------------------------------------------------------|
|    initial                   |  globals.properties 연계 Url, UserName, Password 값 로드 여부(true, false)  |   필수          |                                                                   |
|    crypto                    |  계정 암호화 여부(true, false)                                              |   필수          |                                                                   |
|    algorithm                 |  계정 암호화 알고리즘                                                         |   필수          |                                                                   |
|    algorithmKey              |  계정 암호화키 키                                                           |   필수          |                                                                   |
|    algorithmKeyHash          |  계정 암호화 키 해쉬값                                                        |   필수          |                                                                   |
|    cryptoBlockSize           |  계정 암호화키 블록사이즈                                                       |   필수          |                                                                   |
|    cryptoPropertyLocation    |  설정파일 암복호화 경로                                                        |   선택          |  default=“classpath:/egovframework/egovProps/globals.properties”  |

## Crypto algorithmKey, algorithmKeyHash 생성

Crypto Config 설정에 algorithmKey, algorithmKeyHash 인코딩 키 생성 방법을 제공한다.
**하단 코드에서 계정암호화키 키 값을 원하는 값으로 설정한다.**

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.egovframe.rte.fdl.cryptography.EgovPasswordEncoder;
 
public class EgovEnvCryptoAlgorithmCreateTest {
 
	private static final Logger LOGGER = LoggerFactory.getLogger(EgovEnvCryptoAlgorithmCreateTest.class);
 
	//계정암호화키 키
	public String algorithmKey = "(사용자정의 값)";
 
	//계정암호화 알고리즘(MD5, SHA-1, SHA-256)
	public String algorithm = "SHA-256";
 
	//계정암호화키 블럭사이즈
	public int algorithmBlockSize = 1024;
 
	public static void main(String[] args) {
		EgovEnvCryptoAlgorithmCreateTest cryptoTest = new EgovEnvCryptoAlgorithmCreateTest();
 
		EgovPasswordEncoder egovPasswordEncoder = new EgovPasswordEncoder();
		egovPasswordEncoder.setAlgorithm(cryptoTest.algorithm);
 
		LOGGER.info("------------------------------------------------------");
		LOGGER.info("알고리즘(algorithm) : "+cryptoTest.algorithm);
		LOGGER.info("알고리즘 키(algorithmKey) : "+cryptoTest.algorithmKey);
		LOGGER.info("알고리즘 키 Hash(algorithmKeyHash) : "+egovPasswordEncoder.encryptPassword(cryptoTest.algorithmKey));
		LOGGER.info("알고리즘 블럭사이즈(algorithmBlockSize)  :"+cryptoTest.algorithmBlockSize);
	}
}
```

## 환경설정 파일(globals.properties) 암호화

### 환경설정 파일(globals.properties)의 데이터베이스 연결 항목(Url, UserName, Password) 인코딩 값 생성

환경설정 파일에서 데이터베이스 연결 항목(Url, UserName, Password) 인코딩 키 생성 방법을 제공한다.

```xml
<!-- EgovEnvCryptoUserTest.java 설정 파일 -->
<!-- context-crypto-test.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:egov-crypto="http://maven.egovframe.go.kr/schema/egov-crypto"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://maven.egovframe.go.kr/schema/egov-crypto http://maven.egovframe.go.kr/schema/egov-crypto/egov-crypto-4.1.0.xsd">
 
<bean name="messageSource" class="org.springframework.context.support.ResourceBundleMessageSource">
	<property name="useCodeAsDefaultMessage">
		<value>true</value>
	</property>
	<property name="basenames">
		<list>
			<value>classpath:/egovframework/egovProps/globals</value>
		</list>
	</property>
</bean>
 
<egov-crypto:config id="egovCryptoConfig"
	initial="false"
	crypto="true"
	algorithm="SHA-256"
	algorithmKey="(사용자정의 값)"
	algorithmKeyHash="(생성값)"
	cryptoBlockSize="1024"
/>
</beans>
```

```java
// 데이터베이스 연결 항목(Url, UserName, Password) 인코딩 값 생성 JAVA
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
 
import org.egovframe.rte.fdl.cryptography.EgovEnvCryptoService;
import org.egovframe.rte.fdl.cryptography.impl.EgovEnvCryptoServiceImpl;
 
public class EgovEnvCryptoUserTest {
 
	private static final Logger LOGGER = LoggerFactory.getLogger(EgovEnvCryptoUserTest.class);
 
	public static void main(String[] args) {
 
		String[] arrCryptoString = { 
			"userId",         //데이터베이스 접속 계정 설정
			"userPassword",   //데이터베이스 접속 패드워드 설정
			"url",            //데이터베이스 접속 주소 설정
			"databaseDriver"  //데이터베이스 드라이버
		};
 
		LOGGER.info("------------------------------------------------------");		
		ApplicationContext context = new ClassPathXmlApplicationContext(new String[]{"classpath:/context-crypto-test.xml"});
		EgovEnvCryptoService cryptoService = context.getBean(EgovEnvCryptoServiceImpl.class);
		LOGGER.info("------------------------------------------------------");
 
		String label = "";
		try {
			for(int i=0; i < arrCryptoString.length; i++) {		
				if(i==0)label = "사용자 아이디";
				if(i==1)label = "사용자 비밀번호";
				if(i==2)label = "접속 주소";
				if(i==3)label = "데이터 베이스 드라이버";
				LOGGER.info(label+" 원본(orignal):" + arrCryptoString[i]);
				LOGGER.info(label+" 인코딩(encrypted):" + cryptoService.encrypt(arrCryptoString[i]));
				LOGGER.info("------------------------------------------------------");
			}
		} catch (IllegalArgumentException e) {
			LOGGER.error("["+e.getClass()+"] IllegalArgumentException : " + e.getMessage());
		} catch (Exception e) {
			LOGGER.error("["+e.getClass()+"] Exception : " + e.getMessage());
		}
 
	}
 
}
```

### 환경설정 파일(globals.properties) 인코딩 값 설정

* 앞에서 생성된 데이터베이스 연결 항목(Url, UserName, Password)을 (생성값)에 입력

```properties
......
 
#mysql
Globals.mysql.DriverClassName = (생성값)
Globals.mysql.Url = (생성값)
Globals.mysql.UserName = (생성값)
Globals.mysql.Password = (생성값)
 
......
```

### context-datasource.xml 파일의 데이터베이스 연결 항목(Url, UserName, Password) 디코딩 연결 설정

데이터베이스 설정 파일에서 데이터베이스 연결 항목을 디코딩 하는 설정 방법을 제공한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans 
	xmlns="http://www.springframework.org/schema/beans" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:util="http://www.springframework.org/schema/util" 
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.0.xsd 
	http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.0.xsd">
 
......
 
	<!-- MySQL -->
	<beans profile="mysql">  
	<bean id="dataSource" class="org.apache.commons.dbcp2.BasicDataSource" destroy-method="close">
		<property name="driverClassName" value="#{egovEnvCryptoService.decrypt('${Globals.mysql.DriverClassName}')}"/>
		<property name="url" value="#{egovEnvCryptoService.getUrl()}" />
		<property name="username" value="#{egovEnvCryptoService.getUsername()}" />
		<property name="password" value="#{egovEnvCryptoService.getPassword()}" />
	</bean>
	</beans>
 
......
```

### WAS VM arguments 환경 변수 등록(옵션)

- 간소화 설정 파일에서 algorithmKey, algorithmKeyHash 키의 노출을 피하고 싶다면
  - 간소화 설정 파일에서 algorithmKey, algorithmKeyHash 키를 삭제 하고 WAS VM arguments 환경 변수를 등록 한다.
  - globals.properties 설정 파일의 중요 정보 Url, UserName, Password 항목에 대해 암/복호화 처리 할 수 있도록 제공한다.


```
-Degov.crypto.algorithmKey="(사용자정의 값)" -Degov.crypto.algorithmKeyHash="(생성값)"
```