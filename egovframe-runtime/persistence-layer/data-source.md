---
title: DataSource 서비스
linkTitle: DataSource
description: DataSource 서비스는 데이터베이스 연결을 제공하며, 추상화 계층을 통해 업무 로직과 데이터베이스 연결 방식 간의 종속성을 제거한다. 이를 통해 다양한 방식의 데이터베이스 연결을 지원하고 유연성을 제공한다.
url: /egovframe-runtime/persistence-layer/data-source/
menu:
    depth:
        name: DataSource
        weight: 1
        parent: "persistence-layer"
---
# DataSource 서비스

## 개요

 데이터베이스에 대한 연결을 제공하는 서비스이다. 다양한 방식의 데이터베이스 연결을 제공하고,이에 대한 추상화계층을 제공함으로써, 업무 로직과 데이터베이스 연결 방식 간의 종속성을 배제한다.

## 설명

### Connection Provider 별 DataSource implementions

 Connection Provider별 Connection 객체를 얻기 위한 로직을 구현한 DataSource 구현체를 사용한다.

#### JDBCDataSource

 JDBC driver를 이용하여 Database Connection을 생성한다.

##### Configuration

```xml
<bean id="dataSource"
	class="org.springframework.jdbc.datasource.DriverManagerDataSource">
	<property name="driverClassName" value="${driver}" />
	<property name="url" value="${dburl}" />
	<property name="username" value="${username}" />
	<property name="password" value="${password}" />
</bean>
```

| PROPERTIES | 설 명 |
| --- | --- |
| driverClassName | JDBC driver class name설정 |
| url | Database에 접근하기 위한 JDBC URL |
| username | Database 접근하기 위한 사용자명 |
| password | Database 접근하기 위한 암호 |

##### Sample Source

```java
@Resource(name = "dataSource")
DataSource dataSource;
 
@Resource(name = "jdbcProperties")
Properties jdbcProperties;
 
boolean isHsql = true;
 
@Test
public void testJdbcDataSource() throws Exception {
 
        assertNotNull(dataSource);
        assertEquals("org.springframework.jdbc.datasource.DriverManagerDataSource", 
                                                        dataSource.getClass().getName());
 
        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;
 
        try {
            con = dataSource.getConnection();
            assertNotNull(con);
            stmt = con.createStatement();
            rs = stmt.executeQuery("select 'x' as x from dual");
            while (rs.next()) {
                assertEquals("x", rs.getString(1));
            }
           ........
    
```

#### DBCPDataSource

 JDBC driver를 이용한 Database Connection 구현체이다.[Commons DBCP](http://commons.apache.org/dbcp/)라 불리는 Jakarta의 Database Connection Pool이다.

##### Configuratioin

```xml
<bean id="dataSource" class="org.apache.commons.dbcp2.BasicDataSource" destroy-method="close">
	<property name="driverClassName" value="${driver}"/>
	<property name="url" value="${dburl}"/>
	<property name="username" value="${username}"/>
	<property name="password" value="${password}"/>
	<property name="defaultAutoCommit" value="false"/>
	<property name="poolPreparedStatements" value="true"/>
</bean>
```

| PROPERTIES | 설 명 |
| --- | --- |
| driverClassName | jdbc driver의 class name 설정 |
| url | Database url을 설정 |
| username | Database 접근하기 위한 사용자명 |
| password | Database 접근하기 위한 암호 |
| defaultAutoCommit | datasource로부터 리턴된 connection에 대한 auto-commit 여부를 설정 |
| poolPreparedStatements | PreparedStatement 사용여부 |
| initialSize | Connection pool에 생성될 초기 connection size 설정 |
| maxTotal  <br/> (1.x에서는 maxActive) | 동시에 할당할 수 있는 active connection 최대 갯수를 설정 |
| maxIdle | pool에 남겨놓을 수 있는 idle connection 최대 갯수를 설정 |
| minIdle | 최소한으로 유지할 connection 갯수를 설정 |
| maxWaitMillis  <br/> (1.x에서는 maxWait) | 모든 Connection이 사용중일 경우 최대 대기 시간을 설정 |
| defaultReadOnly | Connection Pool에 의해 생성된 Connection에 read-only 속성 부여 |
| defaultTransactionIsolation | 리턴된 connection에 대한 transaction isolation 속성 부여 |
| defaultCatalog | Connection의 catlog 설정 |
| testOnBorrow | Connection pool에서 객체를 가지고 오기 전에 그 객체의 유효성을 확인할 것인지 결정 |
| testOnReturn | 객체를 return하기 전에 객체의 유효성을 확인할 것인지 결정 |
| validationQuery | validationQuery를 설정 |
| loginTimeout | Database에 연결하기 위한 login timeout(in seconds)을 설정 |
| timeBetweenEvictionRunsMillis | 놀고 있는 connection을 pool에서 제거하는 시간기준(기본 -1) 단위 1/1000초 |

##### Sample Source

```java
@Resource(name = "dataSource")
DataSource dataSource;
 
@Resource(name = "jdbcProperties")
Properties jdbcProperties;
 
boolean isHsql = true;
 
@Test
public void testDbcpDataSource() throws Exception 
{
 
  assertNotNull(dataSource);
  assertEquals("org.apache.commons.dbcp.BasicDataSource", dataSource.getClass().getName());
 
  Connection con = null;
  Statement stmt = null;
  ResultSet rs = null;
 
  try 
  {
    con = dataSource.getConnection();
    assertNotNull(con);
    stmt = con.createStatement();
    rs = stmt.executeQuery("select 'x' as x from dual");
    while (rs.next()) {
        assertEquals("x", rs.getString(1));
    }
   } catch (Exception e) {
    fail("Jdbc DataSource Test Failed! : " + e.getMessage());
    e.printStackTrace();
   } 
   ........
}
```

#### C3P0DataSource

 JDBC driver를 이용한 Database Connection를 생성하는 구현체. C3P0 Library에 관련 사항은 [C3P0 Configuration](http://www.mchange.com/projects/c3p0/index.html#c3p0-config.xml)에서 확인할 수 있다.

##### Configuration

```xml
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource"
	destroy-method="close">
	<property name="driverClass" value="${driver}" />
	<property name="jdbcUrl" value="${dburl}" />
	<property name="user" value="${username}" />
	<property name="password" value="${password}" />
	<property name="initialPoolSize" value="3" />
	<property name="minPoolSize" value="3" />
	<property name="maxPoolSize" value="50" />
	<!-- <property name="timeout" value="0" /> -->   <!-- 0 means: no timeout -->
	<property name="idleConnectionTestPeriod" value="200" />
	<property name="acquireIncrement" value="1" />
	<property name="maxStatements" value="0" />  <!-- 0 means: statement caching is turned off.  -->
	<!-- c3p0 is very asynchronous. Slow JDBC operations are generally performed 
                by helper threads that don't hold contended locks. 
		Spreading these operations over multiple threads can significantly improve performance 
		by allowing multiple operations to be performed simultaneously -->
	<property name="numHelperThreads" value="3" />  <!-- 3 is default -->
</bean>
```

| PROPERTIES | 설 명 |
| --- | --- |
| driverClass | jdbc driver |
| jdbcUrl | DB URL |
| user | 사용자명 |
| password | 패스워드 |
| initialPoolSize | 풀 초기값 |
| minPoolSize | 풀 최소값 |
| maxPoolSize | 풀 최대값 |
| idleConnectionTestPeriod | idle상태 점검시간 |
| acquireIncrement | 증가값 |
| maxStatements | 캐쉬유지여부 |
| numHelperThreads | HelperThread 개수 |

##### Sample Source

```java
@Resource(name = "dataSource")
DataSource dataSource;
 
@Resource(name = "jdbcProperties")
Properties jdbcProperties;
 
@Test
public void testC3p0DataSource() throws Exception 
{
 
        assertNotNull(dataSource);
        assertEquals("com.mchange.v2.c3p0.ComboPooledDataSource", dataSource.getClass().getName());
 
        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;
 
        try {
            con = dataSource.getConnection();
            assertNotNull(con);
            stmt = con.createStatement();
            rs = stmt.executeQuery("select 'x' as x from dual");
            while (rs.next()) {
                assertEquals("x", rs.getString(1));
            }
        } catch (Exception e) {
            fail("Jdbc DataSource Test Failed! : " + e.getMessage());
            e.printStackTrace();
        }
  ...................
}
```

#### JNDIDataSource

 JNDIDataSource는 JNDI Lookup을 이용하여 Database Connection을 생성한다. JNDIDataSource는 대부분 Enterprise application server에서 제공되는 JNDI tree로 부터 DataSource를 가져온다.

##### Configuration

 jee tag를 사용하기 위해서는 Spring XML Configuration 파일의 머릿말에 namespace와 schemaLocation를 추가해야 한다.

- namespace : xmlns:jee="http://www.springframework.org/schema/jee"
- schemaLocation : http://www.springframework.org/schema/jee http://www.springframework.org/schema/jee/spring-jee-2.5.xsd

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:jee="http://www.springframework.org/schema/jee"
       xsi:schemaLocation="
http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
http://www.springframework.org/schema/jee http://www.springframework.org/schema/jee/spring-jee-2.5.xsd">
 
    <!-- <bean/> definitions here -->
 
</beans>
```

 Jeus 설정

```xml
<jee:jndi-lookup id="dataSource" jndi-name="${jndiName}" resource-ref="true">
     <jee:environment>
	  java.naming.factory.initial=${jeus.java.naming.factory.initial}
	  java.naming.provider.url=${jeus.java.naming.provider.url}
    </jee:environment>
</jee:jndi-lookup>
```

 Weblogic 설정

```xml
<util:properties id="jndiProperties" location="classpath:/META-INF/spring/jndi.properties" />
<jee:jndi-lookup id="dataSource" jndi-name="${jndiName}" resource-ref="true" environment-ref="jndiProperties" />
```

| PROPERTIES | 설 명 |
| --- | --- |
| jndiTemplate | JNDI 검색을 위해 JNDI 템플릿을 설정 |
| jndiEnvironment | JNDI를 검색하기 위해 JNDI 환경을 설정 |
| resourceRef | J2EE 컨테이너에서 검색할 수 있는지 설정 |
| expectedType | JNDI 객체의 타입을 지정 |
| jndiName | 검색을 위해 JNDI 이름을 설정 |
| proxyInterface | JNDI 객체를 사용하기 위해 proxy 인터페이스를 설정 |
| lookupOnStartup | starup시에 JNDI object를 검색할 지 여부를 설정 |
| cache | JNDI 객체를 캐싱할 것인지 설정 |
| defaultObject | JNDI lookup에 실패하였을 경우 전달할 default object를 지정 |

##### Sample Source

```java
@Resource(name = "dataSource")
DataSource dataSource;
 
@Resource(name = "jdbcProperties")
Properties jdbcProperties;
 
@Test
public void testJndiJeusDataSource() throws Exception 
{
 
        assertNotNull(dataSource);
        assertEquals("jeus.jdbc.connectionpool.DataSourceWrapper", dataSource.getClass().getName());
 
        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;
 
        try {
            con = dataSource.getConnection();
            assertNotNull(con);
            stmt = con.createStatement();
            rs = stmt.executeQuery("select 'x' as x from dual");
            while (rs.next()) {
                assertEquals("x", rs.getString(1));
            }
        } catch (Exception e) {
            fail("Jdbc DataSource Test Failed! : " + e.getMessage());
            e.printStackTrace();
        } 
        ...................
}
```

- Jeus5.0 datasource : jeus.jdbc.driver.oracle.OracleConnectionPool
- Jeus6.0 datasource : jeus.jdbc.connectionpool.DataSourceWrapper

```java
@Resource(name = "dataSource")
DataSource dataSource;
 
@Resource(name = "jdbcProperties")
Properties jdbcProperties;
 
@Test
public void testJndiDataSource() throws Exception 
{
 
        assertNotNull(dataSource);
        assertEquals("weblogic.jdbc.common.internal.RmiDataSource_922_WLStub", dataSource.getClass().getName());
 
        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;
 
        try {
            con = dataSource.getConnection();
            assertNotNull(con);
            stmt = con.createStatement();
            rs = stmt.executeQuery("select 'x' as x from dual");
            while (rs.next()) {
                assertEquals("x", rs.getString(1));
            }
        } catch (Exception e) {
            fail("Jdbc DataSource Test Failed! : " + e.getMessage());
            e.printStackTrace();
        } 
        ...................
}
```

- Weblogic datasource

## 참고자료
