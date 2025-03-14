---
title: Spring-iBATIS Integration
linkTitle: "Spring-iBATIS Integration"
description: Spring은 iBATIS와의 통합을 통해 IoC 및 예외 계층 구조를 활용한 템플릿 스타일 프로그래밍을 지원하며, Spring의 유연한 트랜잭션 처리와 DataSource 설정을 그대로 사용할 수 있다. SqlMapClientFactoryBean은 iBATIS의 SqlMapClient를 생성하고 Spring 컨텍스트에 설정하는 데 사용된다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-spring_ibatis_integration/
menu:
    depth:
        name: Spring-iBATIS Integration
        weight: 2
        parent: dataaccess-ibatis
---
# Spring-iBATIS Integration

 Spring 프레임워크는 iBATIS SQL Map 을 이미 잘 통합하고 있으며, JDBC/Hibernate 에 대한 연동과 동일하게 template 스타일 프로그래밍이 가능토록 지원한다. 이러한 지원으로 Spring 의 특징인 IoC 의 장점과 Exception 계층 구조의 처리가 iBATIS 통합 환경에서도 쉽게 사용되고 있으며, iBATIS 단독 사용 시에 트랜잭션 관리 및 DataSource 에 대한 설정 및 관리가 별도로 필요했던 것에 비해 Spring-iBATIS 통합 환경에서는 Spring 의 유연한 트랜잭션 처리와 dataSource 를 그대로 사용할 수 있다.

## Spring 의 SqlMapClientFactoryBean 설정

 SqlMapClientFactoryBean 은 iBATIS 의 SqlMapClient 를 생성하는 FactoryBean 구현체로, Spring 의 context 에 iBATIS 의 SqlMapClient 를 셋업하는 일반적인 방법으로 사용된다. 여기서 얻어진 SqlMapClient 는 iBATIS 기반 DAO 에 dependency injection 을 통해 넘겨지게 된다.

### Sample Configuration

```xml
	<!-- dataSource 설정 -->
	<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
		<property name="driverClassName" value="${driver}"/>
		<property name="url" value="${dburl}"/>
		<property name="username" value="${username}"/>
		<property name="password" value="${password}"/>
		<property name="defaultAutoCommit" value="false"/>
		<property name="poolPreparedStatements" value="true"/>
	</bean>
 
	<!-- SqlMap setup for iBATIS Database Layer -->
	<bean id="sqlMapClient" class="egovframework.rte.psl.orm.ibatis.SqlMapClientFactoryBean">
		<property name="configLocation" value="classpath:/META-INF/sqlmap/sql-map-config.xml"/>
		<property name="dataSource" ref="dataSource"/>
	</bean>
```

- dataSource : 데이터베이스 연결 추상화를 제공하는 DataSource 설정. 위에서는 Apache Commons DBCP 를 사용하였으며 DB 접속과 관련된 설정은 property-placeholder 를 사용하여 외부화 하였다.
- sqlMapClient : Spring의 iBATIS 연동을 위한 SqlMapClientFactoryBean 설정으로 configLocation 속성을 통해 지정한 iBATIS 메인 설정 파일인 sql-map-config.xml 에 대해 iBATIS 의 SqlMapClient instance 를 생성하여 Spring 환경에서 사용 가능토록 한다. Spring 의 dataSource 를 iBATIS 에 넘길 수 있도록 injection 을 지시하고 있으며 이로 인해 iBATIS 설정 파일 자체에서는 dataSource 및 transaction 설정 필요없이(Spring 환경에서는 iBATIS 기반 DAO 호출 이전에 서비스 단에서 선언적인 트랜잭션 처리를 해주었을 것임) Spring 이 제공하는 유연한 dataSource 및 트랜잭션 처리를 사용하게 된다.

 Spring 현재 버전에서는 configLocations 속성을 추가하여 sql-map-config.xml 에 대한 패턴 표현식이나 복수 연동(런타임에 하나의 통합 설정으로 merge 됨)도 지원하고 있다. useTransactionAwareDataSource 속성으로 SqlMapClient 에 대해 Spring 이 관리하는 transaction timeout 을 함께 적용할 수 있는 transaction-aware DataSource 를 사용하도록 설정 가능하며(default), lobHandler 속성을 통해 Spring 의 lobHandler 를 설정할 수도 있다.

#### mappingLocations 지원

 또한 iBATIS 사용 환경에서의 중요한 개선 사항으로 mappingLocations 속성을 통해 기존에 iBATIS 메인 설정 파일 내에서 sqlMap 태그로 일일이 지정하여야만 했던 sql 매핑 파일에 대해 Spring 의 SqlMapClientFactoryBean 빈 설정파일에서 Spring 의 유연한 리소스 추상화를 적용하여 리소스 패턴 형태로 일괄 지정이 가능하다. 이 경우 sql 매핑 파일들의 위치는 sql-map-config 설정 파일과 런타임에 merge 되도록 세팅된다. 이 방법은 **Spring 2.5.5 이상, iBATIS 2.3.2 이상**에서만 지원됨에 유의한다.

```xml
	<!-- SqlMap setup for iBATIS Database Layer -->
	<bean id="sqlMapClient" class="egovframework.rte.psl.orm.ibatis.SqlMapClientFactoryBean">
		<property name="configLocation"
			value="classpath:/META-INF/sqlmap/sql-map-config.xml" />
		<property name="mappingLocations"
			value="classpath:/META-INF/sqlmap/mappings/testcase-*.xml" />
		<property name="dataSource" ref="dataSource" />
	</bean>
```

 단 위와 같이 일괄 sql 매핑 파일 지정을 Spring 설정 파일에 지시하였더라도 iBATIS 의 sql-map-config.xml 의 DTD([http://ibatis.apache.org/dtd/sql-map-config-2.dtd](http://ibatis.apache.org/dtd/sql-map-config-2.dtd)) 에 sqlMap 태그가 최소 1개 이상이 나타나야 하도록 지정되어 있으므로 아래와 같이 dummy sql 매핑 파일 하나를 지정하는 sql-map-config.xml 로 작성하면 편할 것이다.

## iBATIS 의 설정 변경

- sqlMap 설정을 제거한(dummy 하나는 설정 필요) sql-map-config.xml

```xml
 
<!DOCTYPE sqlMapConfig PUBLIC "-//ibatis.apache.org//DTD SQL Map Config 2.0//EN"
"http://ibatis.apache.org/dtd/sql-map-config-2.dtd">
<sqlMapConfig>
	<settings useStatementNamespaces="false" 
				defaultStatementTimeout="10"
	/>
 
	<typeHandler javaType="java.util.Calendar" jdbcType="TIMESTAMP"
		callback="egovframework.rte.psl.dataaccess.typehandler.CalendarTypeHandler" />
 
	<!-- Spring 2.5.5 이상, iBATIS 2.3.2 이상에서는 iBATIS 연동을 위한 SqlMapClientFactoryBean 정의 시 
               mappingLocations 속성으로 Sql 매핑 파일의 일괄 지정이 가능하다. 
	    ("sqlMapClient" bean 설정 시  
                       mappingLocations="classpath:/META-INF/sqlmap/mappings/testcase-*.xml" 로 지정하였음)
	    단, sql-map-config-2.dtd 에서 sqlMap 요소를 하나 이상 지정하도록 되어 있으므로 
              아래의 dummy 매핑 파일을 설정하였다.
	-->
	<sqlMap resource="META-INF/sqlmap/mappings/testcase-dummy.xml" />
 
</sqlMapConfig>
```

- testcase-dummy.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE sqlMap PUBLIC "-//iBATIS.com//DTD SQL Map 2.0//EN" "http://www.ibatis.com/dtd/sql-map-2.dtd">
 
<sqlMap namespace="Dummy"/>
```

## iBATIS-based DAO

 Spring 의 SqlMapClientDaoSupport 클래스는 iBATIS 의 SqlMapClient data access object 를 위한 편리한 수퍼 클래스로 이를 extends 하는 서브 클래스에 SqlMapClientTemplate 를 제공한다. SqlMapClientTemplate 는 iBATIS 를 통한 data access 를 단순화하는 헬퍼 클래스로 SQLException 을 Spring dao 의 exception Hierarchy 에 맞게 unchecked DataAccessException 으로 변환해 주며 Spring 의 JdbcTemplate 과 동일한 처리 구조의 SQLExceptionTranslator 를 사용할 수 있게 해준다. 또한 iBATIS 의 SqlMapExecutor 의 실행 메서드에 대한 편리한 mirror 메서드를 다양하게 제공하므로 일반적인 쿼리나 insert/update/delete 처리에 대해 편리하게 사용할 수 있도록 권고된다. 그러나 batch update 와 같은 복잡한 수행에 대해서는 Spring 의 SqlMapClientCallback 에 대한 명시적인 구현(보통 anonymous inner class 로 작성)이 필요하다.

```java
public class SqlMapAccountDao extends SqlMapClientDaoSupport implements AccountDao {
 
    public Account getAccount(String email) throws DataAccessException {
        return (Account) getSqlMapClientTemplate().queryForObject("getAccountByEmail", email);
    }
 
    public void insertAccount(Account account) throws DataAccessException {
        getSqlMapClientTemplate().update("insertAccount", account);
    }
}
```

 iBATIS 연동 DAO 는 SqlMapClientDaoSupport 를 extends 하고 있으며, getSqlMapClientTemplate() 를 통해 SqlMapClientTemplate 를 얻어 iBATIS 의 data access 처리를 래핑하여 실행토록 처리하고 있다.

```xml
  <bean id="accountDao" class="example.SqlMapAccountDao">
    <property name="sqlMapClient" ref="sqlMapClient"/>
  </bean>
```

 iBATIS 연동 DAO 에 sqlMapClient 빈을 주입해 주어야 한다.

 위의 처리는 Annotation 을 사용한 빈 생성 및 dependency 처리 시 sqlMapClient 의 DAO 주입 설정에 어려움이 존재한다. 이의 손쉬운 해결을 위해 전자정부 프레임워크는 EgovAbstractDAO 를 확장하여 제공하고 있다.