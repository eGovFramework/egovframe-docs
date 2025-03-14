---
title: Transaction 서비스
linkTitle: "Transaction"
description: Spring 트랜잭션 서비스는 DataSource, JTA, JPA 트랜잭션 서비스를 지원하며, 트랜잭션 관리는 선언적 방식(Declarative)과 프로그래밍 방식(Programmatic)으로 수행할 수 있다. DataSource 트랜잭션 서비스는 로컬 트랜잭션 관리를 위한 설정 및 사용법을 제공한다.
url: /egovframe-runtime/persistence-layer/transaction/
menu:
    depth:
        name: Transaction
        weight: 9
        parent: "persistence-layer"
        identifier: "transaction"
---
# Transaction 서비스

## 개요
트랜잭션 서비스는 Spring 트랜잭션 서비스를 채택하여 가이드한다. 트랜잭션 서비스에는 여러가지가 있지만 여기서는 DataSource Transaction Service, JTA Transaction Service, JPA Transaction Service에 대해서 설명하고 트랜잭션 활용에 대해서는 설정 및 Annotation을 통해서 활용할 수 있는 Declaration Transaction Management와 프로그램에서 직접 API를 호출하여 쓸 수 있도록 하는 Programmatic Transaction Management 두가지에 대해서 설명한다.

- [Declarative Transaction Management](./transaction-declarative-transaction-management.md)
- [Programmatic Transaction Management](./transaction-programmatic-transaction-management.md)

## 설명
### DataSource Transaction Service
DataSource를 사용하여 Local Transaction을 관리할 수 있다. 아래에서 예를 들어서 설정 방법과 사용법을 설명한다.

<b>Configuration</b>

```xml
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource"/>
</bean>

<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="dbc:mysql://db2:1621/rte"/>
    <property name="username" value="rte"/>
    <property name="password" value="xxx"/>
    <property name="defaultAutoCommit" value="false"/>
</bean>
```

| PROPERTIES        | 설 명         |
| ----------------- | ----------- |
| driverClassName   | jdbc driver |
| url               | db url      |
| username          | 사용자명        |
| password          | 패스워드        |
| defaultAutoCommit | 자동commit 설정 |

위의 설정을 보면 transactionManager의 property로 dataSource를 지정하고 그에 필요한 driver정보,Url정보등을 지정한 것을 확인 할 수 있다. 설정한 dataSource 기반하에서 트랜잭션 서비스를 제공한다. 사이트 환경에 맞추어 driverClassName,url,username,password는 변경해서 적용한다.

<b>Sample Source</b>

```java
    @Resource(name="transactionManager")
    PlatformTransactionManager transactionManager;
    ...
    TransactionStatus txStatus = transactionManager.getTransaction(txDefinition);
```

위의 예와 같이 transactionManager을 활용할 수 있다.

### JTA Transaction Service
자바 트랜잭션 API(Java Transaction API, JTA)는 XA 리소스(예, 데이터베이스) 간의 분산 트랜잭션을 처리하는 자바 API이다.

Java에서 제공되는 대부분의 API와 마찬가지로, JTA는 실제 구현은 다르지만 어플리케이션이 공통적으로 사용할 수 있는 하나의 인터페이스를 제공한다. 이 말은 트랜잭션 처리가 필요한 어플리케이션이 (API의 사용 방식 그대로만 사용한다면) 특정 벤더의 트랜잭션 매니저에 의존할 필요가 없음을 의미한다.

그에따라, JTA는 일반적으로 단일 데이터베이스 또는 여러 개의 데이터베이스를 이용할 경우 트랜잭션을 제어하기 위한 목적으로 사용된다.

JTA를 이용하여 Global Transation관리를 할 수 있도록 지원하는 것으로 아래에서 예를 들어서 설정 방법을 설명한다. 사용법은 DataSource Transaction Service와 동일하다.

<b>Configuration</b>

```xml
    <tx:jta-transaction-manager/>
    <jee:jndi-lookup id="dataSource" jndi-name="dbmsXADS" resource-ref="true">
      <jee:environment>
         java.naming.factory.initial=weblogic.jndi.WLInitialContextFactory
         java.naming.provider.url=t3://was:7002
      </jee:environment>
    </jee:jndi-lookup>
```
위의 설정예에서 jndi-name 과 java.naming.factory.initial,java.naming.provider.url은 사이트 환경에 맞추어 변경해야 한다. DataSource Transaction Service와는 달리 transationManager에 대해서 따로 bean 정의하지 않아도 된다.

### JPA Transaction Service

JPA Transaction 서비스는 JPA EntityManagerFactory를 이용하여 트랜잭션을 관리한다. JpaTransactionManager는 EntityManagerFactory에 의존성을 가지고 있으므로 반드시 EntityManagerFactory 설정과 함께 정의되어야 한다. 아래에서 예를 들어서 설정 방법을 설명한다. 사용법은 DataSource Transaction Service와 동일하다.

<b>Configuration</b>

```xml
<bean id="transactionManager" class="org.springframework.orm.jpa.JpaTransactionManager">
    <property name="entityManagerFactory" ref="entityManagerFactory"/>
</bean>

<bean id="entityManagerFactory" class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean">
<property name="persistenceUnitName" value="OraUnit"/>
<property name="persistenceXmlLocation" value="classpath:META-INF/persistence.xml"/>
<property name="dataSource" ref="dataSource"/>
</bean>

<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
<property name="driverClassName" value="com.mysql.jdbc.Driver"/>
<property name="url" value="dbc:mysql://db2:1621/rte"/>
<property name="username" value="rte"/>
<property name="password" value="xxx"/>
<property name="defaultAutoCommit" value="false"/>
</bean>
```

| PROPERTIES             | 설 명                 |
| ---------------------- | ------------------- |
| driverClassName        | jdbc driver         |
| url                    | db url              |
| username               | 사용자명                |
| password               | 패스워드                |
| defaultAutoCommit      | 자동commit 설정         |
| persistenceUnitName    | persistenceUnitName |
| persistenceXmlLocation | XML 위치              |
| dataSource             | 데이타소스               |

위의 설정을 보면 transactionManager의 property로 entiyManagerFactory로 지정하고 entityManagerFactory의 property로 dataSource를 지정하고 그에 필요한 driver정보,Url정보등을 지정한 것을 확인 할 수 있다. 설정한 dataSource 기반하에서 트랜잭션 서비스를 제공한다. 사이트 환경에 맞추어 driverClassName,url,username,password는 변경해서 적용한다. 또한 persistenceUnitName과 persistenceXmlLocation 정보를 지정하는 것을 알수 있다.

## 참고자료