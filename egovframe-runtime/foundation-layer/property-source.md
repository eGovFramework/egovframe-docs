---
title: Property Source
linkTitle: "Property Source"
description: Property Source는 Spring에서 properties 파일이나 DB 테이블에서 key-value 형식의 설정 값을 가져올 수 있도록 하는 기능이다. **Property-placeholder**는 XML 설정 파일에서 `${}`를 사용해 외부 설정 값을 참조하며, Spring 3.1 이후에는 **PropertySourcesPlaceholderConfigurer**가 사용된다. **DB PropertySource**는 DB 테이블에서 설정 값을 가져오는 기능을 제공하며, `DBPropertySourceInitializer`를 통해 WAS 기동 시 설정 값을 로드할 수 있다.
url: /egovframe-runtime/foundation-layer/property/property-source/
menu:
    depth:
        name: Property Source
        weight: 2
        parent: "Property"
---
# Property Source

## 개요

Property Source는 property place-holder를 이용하여 xml의 bean설정에서 key값을 통해 가져올 수 있으며 코드상에서는 Environment를 이용하여 해당값을 가져올 수 있다.

기본적으로 properties파일을 통한 기능을 제공하고 있으며 추가적인 설정을 통해 DB의 테이블에서 property값을 가져오는 PropertySource를 제공하고 있다. 또한 사용자가 추가로 PropertySource를 정의할 수 있다.

## Property-placeholder와 PropertySource

### Property-placeholder

bean을 정의할 때 `${…}`의 내용을 property placeholder를 이용하여 대체할 수 있었다.
해당 코드는 다음과 같다.

```xml
<context:property-placeholder location="com/bank/config/datasource.properties"/>
 
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
    <property name="driverClass" value="${database.driver}"/>
    <property name="jdbcUrl" value="${database.url}"/>
    <property name="username" value="${database.username}"/>
    <property name="password" value="${database.password}"/>
</bean>
```

Spring 3.1이전에는 `<context:property-placeholder>`를 정의하면 PropertyPlaceholderConfigurer를 사용하였다. 그러나 Spring 3.1이후부터 PropertySourcesPlaceholderConfigurer를 내부에서 사용하고 있으며 위에서 ${database.*}값을 datasource.properties에서 찾지 못하면 Environment의 Property를 사용하도록 하고 있다.
PropertySource는 Environment를 통해 접근 가능하다. 즉, 사용자가 정의한 PropertySource 또한 Spring 3.1부터 property-placeholder를 통해 사용할 수 있는 것이다.

### 사용자 정의 PropertySource

Spring 3.1에서는 사용자가 직접 PropertySource를 정의할 수 있는 방법을 제시한다.
ApplicationContextInitializer인터페이스와 web.xml에 contextInitializerClasses서블릿 컨텍스트 파라미터, Environment를 이용하여 정의가 가능하다.

ApplicationContextInitializer인터페이스를 구현하여 ApplicationContext초기화 로직을 직접 등록할 수 있으며 이 때 contextInitializerClasses 서블릿 컨텍스트 파라미터에 이 구현클래스를 등록한다.

web.xml의 정의 예이다.

```xml
<context-param>
    <param-name>contextInitializerClasses</param-name>
    <param-value>com.bank.MyInitializer</param-value>
</context-param>
```

이 때 ApplicationContextInitializer 구현 클래스인 MyInitializer 예이다.

```java
public class MyInitializer implements ApplicationContextInitializer<ConfigurableWebApplicationContext> {
    public void initialize(ConfigurableWebApplicationContext ctx) {
        PropertySource ps = new MyPropertySource();
        ctx.getEnvironment().getPropertySources().addFirst(ps);
        // perform any other initialization of the context ...
    }
}
```

위와 같이 등록하면 ApplicationContext가 로딩되거나 refresh되는 시점에 ApplicationContextInitializer구현체가 동작한다.
ApplicationContextInitializer구현체의 initialize메소드에서 사용자가 정의한 PropertySource(PropertySource를 상속)를 Environment내부의 propertySources에 (getPropertySources함수를 이용하여) 추가한다.

사용자 정의 PropertySource를 등록하면 Environment를 통해 직접 Property를 가져오는 방법이나 Property-placeholder를 통해서 모두 해당 Property를 가져올 수 있다.

### DB PropertySource

전자정부 3.0에서는 DB의 테이블에서 Property값을 가져오는 DBPropertySource를 제공하고 있다.

### DB PropertySource이용을 위한 설정

DB기반의 PropertySource를 적용하기 위해서는 다음과 같이 설정한다.

- DB TABLE과 데이터 생성
  - 칼럼명을 PKEY, PVALUE로 갖는 DB TABLE을 생성한다.
- BEAN 정의
  - dataSource와 dbPropertySource를 빈으로 정의한 xml을 설정한다.
- web.xml설정
  - web.xml에 위에서 정의한 xml path와 DBPropertySourceInitializer를 설정한다.

#### DB설정

WAS가 기동될 때 DB를 연결하여 테이블에서 property값들을 가져올 수 있도록 하는 xml을 설정한다. DB property값을 담을 table을 만든다. 이 때, 칼럼명은 PKEY, PVALUE로 만들도록 한다.

```sql
CREATE TABLE PROPERTY (
  PKEY VARCHAR(20) NOT NULL  PRIMARY KEY ,
  PVALUE VARCHAR(20) NOT NULL
);
 
commit;
```

```sql
INSERT INTO PROPERTY (PKEY, PVALUE) VALUES ('egov.test.sample01', 'db-property-sample01');
INSERT INTO PROPERTY (PKEY, PVALUE) VALUES ('egov.test.sample02', 'db-property-sample02');
 
...
 
commit;
```

다음은 db설정 xml의 예이다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xmlns:p="http://www.springframework.org/schema/p"
		xmlns:jdbc="http://www.springframework.org/schema/jdbc"
		xmlns:context="http://www.springframework.org/schema/context"
		xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
			http://www.springframework.org/schema/jdbc http://www.springframework.org/schema/jdbc/spring-jdbc-3.2.xsd">
 
	<jdbc:embedded-database id="dataSource" type="HSQL">
		<jdbc:script location="classpath:db/ddl.sql" />
		<jdbc:script location="classpath:db/dml.sql" />
	</jdbc:embedded-database>
 
	<bean id="dbPropertySource" class="egovframework.rte.fdl.property.db.DbPropertySource">
		<constructor-arg value="dbPropertySource"/>
		<constructor-arg ref="dataSource"/>
		<constructor-arg value="SELECT PKEY, PVALUE FROM PROPERTY"/>
	</bean>
</beans>
```

#### web.xml설정

WAS 기동 시에 DB값을 가져오도록 web.xml에 추가설정이 필요하다. egov에서 제공해주는 DBPropertySourceInitializer를 추가해주고, 앞에서 설정한 xml의 path를 설정해준다.

```xml
<context-param>
    <param-name>contextInitializerClasses</param-name>
    <param-value>egovframework.rte.fdl.property.db.initializer.DBPropertySourceInitializer</param-value>
</context-param>
<context-param>
    <param-name>propertySourceConfigLocation</param-name>
    <param-value>classpath:/initial/propertysource-context.xml</param-value>
</context-param>
```

### DB PropertySource접근

#### xml에서 DBPropertySource이용

xml에서 정의된 PropertySource를 사용하기 위해서 property-placeholder만 설정해주면 된다.

```xml
...
<context:property-placeholder/>
 
<!-- 메시지소스빈 설정 -->
<bean id="propertyTest" class="egov.sample.property.PropertyTest">
  <property name="sample01" value="${egov.test.sample01}"/>
  <property name="sample02" value="${egov.test.sample02}"/>
</bean>
...
```

#### 코드상에서 DBPropertySource이용

코드상에서 PropertySource에 접근하기 위해서는 egov 3.0부터 제공하는 Environment abstraction을 이용한다. 자세한 내용은 Environment를 참조하도록 한다.

## 참고자료

[Spring 3.1 M1: Unified Property Management](http://spring.io/blog/2011/02/15/spring-3-1-m1-unified-property-management/)






