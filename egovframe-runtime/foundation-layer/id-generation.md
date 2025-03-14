---
title: Id Generation 서비스
linkTitle: "Id Generation"
description: ID Generation 서비스는 UUID, Sequence, Table 기반의 고유 ID 생성을 지원하며, UUID는 MAC/IP 주소 또는 랜덤 방식으로, Sequence는 DB 시퀀스를 사용해 ID를 생성한다. Table ID Generation은 별도의 테이블을 사용해 ID를 관리하며, Strategy 설정을 통해 ID 생성 규칙을 지정할 수 있다. 다양한 설정을 통해 ID를 쉽게 생성하고 관리할 수 있도록 지원한다.
url: /egovframe-runtime/foundation-layer/id-generated/
menu:
    depth:
        name: Id Generation 서비스
        weight: 5
        parent: "foundation-layer"
---

# Id Generation 서비스

## 개요
시스템을 개발할 때 필요한 유일한 ID를 생성하기 위해 사용하도록 서비스한다.

## 주요 개념

### Universally Unique Identifier(UUID)

UUID는 OSF(Open Software Foundation)에 의해 제정된 고유식별자(Identifier)에 대한 표준이다. UUID는 16-byte (128-bit)의 숫자로 구성된다.

UUID를 표현하는 방식에 대한 특별한 규정은 없으나, 일반적으로 아래와 같이 16진법으로 8-4-4-4-12 형식으로 표현한다.

`550e8400-e29b-41d4-a716-446655440000`

UUID 표준은 아래 문서에 기술되어 있다.

- [ISO/IEC 11578:1996 "Information technology -- Open Systems Interconnection -- Remote Procedure Call (RPC)"](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=2229)
- [ITU-T Rec. X.667 | ISO/IEC 9834-8:2005](http://www.itu.int/ITU-T/studygroups/com17/oid.html)
- [IETF Proposed Standard RFC 4122](http://tools.ietf.org/html/rfc4122)

UUID는 다음 5개의 Version이 존재한다.

- Version 1 (MAC Address)
  - UUID를 생성시키는 컴퓨터의 MAC 어드레스와 시간 정보를 이용하여 UUID를 생성한다.
  - 컴퓨터의 MAC 어드레스를 이용하므로 어떤 컴퓨터에서 생성했는지 정보가 남기 때문에 보안에 문제가 있다.
- Version 2 (DCE Security)
  - POSIX UID를 이용하여 UUID를 생성한다.
- Version 3 (MD5 Hash)
  - URL로부터 MD5를 이용하여 UUID를 생성한다.
- Version 4 (Random)
  - Random Number를 이용하여 UUID를 생성한다.
- Version 5 (SHA-1 Hash)
  - SHA-1 Hashing을 이용하여 UUID를 생성한다.

## 설명
ID 생성 방식으로는 [UUID](#Universally-Unique-Identifier(UUID))를 생성하는 [UUID Generation Service](#UUID-Generation-Service)와 sequence를 활용하는 [Sequence Id Generation Service](#Sequence-Id-Generation-Service), 그리고 키제공을 위한 테이블을 지정하여 생성하는 [Table Id Generation Service](#Table-Id-Generation-Service) 3가지가 있다.

### UUID Generation Service

새로운 ID를 생성하기 위해 UUID 생성 알고리즘을 이용하여 16 바이트 길이의 ID를 생성한다.

String 타입의 ID 생성과 BigDecimal 타입의 ID 생성 두가지 유형 ID 생성을 지원한다.

지원하는 방법은 설정에 따라서 [Mac Address Base Service](#Mac-Address-Base-Service), [IP Address Base Service](#IP-Address-Base-Service), [No Address Base Service](#No-Address-Base-Service) 세가지 유형이 있다.

#### Mac Address Base Service

MAC Address를 기반으로 유일한 Id를 생성하는 UUIdGenerationService

##### Configuration

```xml
<bean name="UUIdGenerationService" class="org.egovframe.rte.fdl.idgnr.impl.EgovUUIdGnrServiceImpl">
    <property name="address">
        <value>00:00:F0:79:19:5B</value>
    </property>
</bean>
```

##### Sample Source

```java
@Resource(name="UUIdGenerationService")
private EgovIdGnrService uUidGenerationService;
 
@Test
public void testUUIdGeneration() throws Exception {
   assertNotNull(uUidGenerationService.getNextStringId());
   assertNotNull(uUidGenerationService.getNextBigDecimalId());
}
```

#### IP Address Base Service

IP Address를 기반으로 유일한 Id를 생성하는 UUIdGenerationService

##### Configuration

```xml
<bean name="UUIdGenerationServiceWithIP" class="org.egovframe.rte.fdl.idgnr.impl.EgovUUIdGnrServiceImpl">
    <property name="address">
        <value>100.128.120.107</value>
    </property>
</bean>
```

##### Sample Source

```java
@Resource(name="UUIdGenerationServiceWithIP")
private EgovIdGnrService uUIdGenerationServiceWithIP; 
 
@Test
public void testUUIdGenerationIP() throws Exception {
   assertNotNull(uUIdGenerationServiceWithIP.getNextStringId());
   assertNotNull(uUIdGenerationServiceWithIP.getNextBigDecimalId());
}
```

#### No Address Base Service

IP Address 설정없이 `Math.random()`을 이용하여 주소정보를 생성하고 유일한 Id를 생성하는 UUIdGenerationService

##### Configuration

```xml
<bean name="UUIdGenerationServiceWithoutAddress" class="org.egovframe.rte.fdl.idgnr.impl.EgovUUIdGnrServiceImpl">
</bean>
```

##### Sample Source

```java
@Resource(name="UUIdGenerationServiceWithoutAddress")
private EgovIdGnrService uUIdGenerationServiceWithoutAddress; 
 
@Test
public void testUUIdGenerationNoAddress() throws Exception {
   assertNotNull(uUIdGenerationServiceWithoutAddress.getNextStringId());
   assertNotNull(uUIdGenerationServiceWithoutAddress.getNextBigDecimalId());
}
```

### Sequence Id Generation Service

새로운 ID를 생성하기 위해 Database의 SEQUENCE를 사용하는 서비스이다. 서비스를 이용하는 시스템에서 Query를 지정하여 아이디를 생성할 수 있도록 하고 [Basic Type Service](#Basic-Type-Service)와 [BigDecimal Type Service](#BigDecimal-Type-Service) 두가지를 지원한다.

#### Basic Type Service

기본타입 ID를 제공하는 서비스로 `int`, `short`, `byte`, `long` 유형의 ID를 제공한다.

##### DB Schema

```sql
CREATE SEQUENCE idstest MINVALUE 0;
```

##### Configuration

```xml
<bean name="primaryTypeSequenceIds" class="org.egovframe.rte.fdl.idgnr.impl.EgovSequenceIdGnrServiceImpl" destroy-method="destroy">
  <property name="dataSource" ref="dataSource"/>
  <property name="query" value="SELECT idstest.NEXTVAL FROM DUAL"/>
</bean>
```

##### Sample Source

```java
@Resource(name="primaryTypeSequenceIds")
private EgovIdGnrService primaryTypeSequenceIds;
 
@Test
public void testPrimaryTypeIdGeneration() throws Exception {
   //int
   assertNotNull(primaryTypeSequenceIds.getNextIntegerId());
   //short
   assertNotNull(primaryTypeSequenceIds.getNextShortId());
   //byte
   assertNotNull(primaryTypeSequenceIds.getNextByteId());
   //long
   assertNotNull(primaryTypeSequenceIds.getNextLongId());
}
```

#### BigDecimal Type Service

BigDecimal ID를 제공하는 서비스로 [기본타입 ID 제공 서비스](#Basic-Type-Service) 설정에 추가적으로 `useBigDecimals`을 `true`로 설정하여 BigDecimal 사용하도록 한다.

##### DB Schema

```sql
CREATE SEQUENCE idstest MINVALUE 0;
```

##### Configuration

```xml
<bean name="bigDecimalTypeSequenceIds" class="org.egovframe.rte.fdl.idgnr.impl.EgovSequenceIdGnrServiceImpl" destroy-method="destroy">
  <property name="dataSource" ref="dataSource"/>
  <property name="query" value="SELECT idstest.NEXTVAL FROM DUAL"/>
  <property name="useBigDecimals" value="true"/>
</bean>
```

##### Sample Source

```java
@Resource(name="bigDecimalTypeSequenceIds")
private EgovIdGnrService bigDecimalTypeSequenceIds;
 
@Test
public void testBigDecimalTypeIdGeneration() throws Exception {
   //BigDecimal
   assertNotNull(bigDecimalTypeSequenceIds.getNextBigDecimalId());
}
```

#### Database 별 설정

##### Oracle

- DB Schema
```sql
CREATE SEQUENCE <sequence name> [START WITH <start value>] [INCREMENT BY <increment value>] [MINVALUE <min value>] [MAXVALUE <max value>]
```
- Query
```sql
SELECT <sequence name>.NEXTVAL FROM DUAL
```

##### HSQL

- DB Schema
```sql
CREATE SEQUENCE <sequence name> [AS {INTEGER | BIGINT}] [START WITH <start value>] [INCREMENT BY <increment value>]
```
- Query
```sql
SELECT NEXT VALUE FOR <sequence name> FROM DUAL
-- HSQL DB는 DUAL 테이블을 제공하지 않기 때문에 하나의 row를 가진 DUAL 테이블을 수동으로 생성해야 한다.
```

##### IBM DB2

- DB Schema
```sql
CREATE SEQUENCE <sequence name> [START WITH <start value>] [INCREMENT BY <increment value>] [MINVALUE <min value>] [MAXVALUE <max value>]
```
- Query
```sql
SELECT NEXT VALUE FOR <sequence name> FROM SYSIBM.SYSDUMMY1
```

##### Sybase
- Sybase는 Sequence를 지원하지 않는다.

##### MS SQL Server
- MS SQL Server는 Sequence를 지원하지 않는다.

##### MySQL
- MySQL은 Sequence를 지원하지 않는다.

### Table Id Generation Service

새로운 아이디를 얻기 위해 별도의 테이블을 생성, 키값과 키값에 해당하는 아이디값을 입력하여 관리를 제공하는 서비스이다.

table_name(`CHAR` 또는 `VARCHAR`타입), next_id(`integer` 또는 `DECIMAL` type)와 같이 두 칼럼을 필요로 한다.

별도의 테이블에 설정된 정보만을 사용하여 제공하는 [Basic Service](#Basic-Service), prefix와 채울 문자열을 지정하여 String ID를 생성할 수 있는 [Strategy Base Service](#Strategy-Base-Service)를 제공한다.

#### Basic Service

테이블에 지정된 정보에 의해서 아이디를 생성하는 서비스로 사용하고자 하는 시스템에서 테이블을 생성해서 사용할 수 있다.

##### DB Schema

```sql
CREATE TABLE ids (
  table_name varchar(16) NOT NULL, 
  next_id DECIMAL(30) NOT NULL,
  PRIMARY KEY (table_name)
);
INSERT INTO ids VALUES('id','0');
-- ID Generation 서비스를 쓰고자 하는 시스템에서 미리 생성해야 할 DB Schema 정보이다.
```

##### Configuration
```xml
<bean name="basicService" class="org.egovframe.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
  <property name="dataSource" ref="dataSource"/>
  <property name="blockSize" value="10"/>
  <property name="table" value="ids"/>
  <property name="tableName" value="id"/>
</bean>
```
- blockSize
  - Id Generation 내부적으로 사용하는 정보로 ID 요청시마다 DB접속을 하지 않기 위한 정보
    - 지정한 횟수 마다 DB 접속 처리
- table
  - 생성하는 테이블 정보로 사용처에서 테이블명 변경 가능
- tableName
  - 사용하고자 하는 아이디 개별 인식을 위한 키 값
    - 테이블 별로 아이디가 필요하기에 `tableName`이라고 지정함

##### Sample Source

```java
@Resource(name="basicService")
private EgovIdGnrService basicService;
 
@Test
public void testBasicService() throws Exception {
   //int
   assertNotNull(basicService.getNextIntegerId());
   //short
   assertNotNull(basicService.getNextShortId());
   //byte
   assertNotNull(basicService.getNextByteId());
   //long
   assertNotNull(basicService.getNextLongId());
   //BigDecimal
   assertNotNull(basicService.getNextBigDecimalId());
   //String
   assertNotNull(basicService.getNextStringId());
}
```

#### Strategy Base Service

아이디 생성을 위한 룰을 등록하고 룰에 맞는 아이디를 생성할 수 있도록 지원하는 서비스이다.

위의 [Basic Service](#Basic-Service)에서 추가적으로 Strategy 정보 설정을 추가하여 사용 할 수 있다.

단, 이 서비스는 `String` 타입의 `ID`만을 제공한다.

##### DB Schema
```sql
CREATE TABLE idttest(
  table_name varchar(16) NOT NULL, 
  next_id DECIMAL(30) NOT NULL,
  PRIMARY KEY (table_name)
);
INSERT INTO idttest VALUES('test','0');
-- ID Generation 서비스를 쓰고자 하는 시스템에서 미리 생성해야 할 DB Schema 정보이다.
```

##### Configuration
```xml
<bean name="Ids-TestWithGenerationStrategy" class="org.egovframe.rte.fdl.idgnr.impl.EgovTableIdGnrServiceImpl" destroy-method="destroy">
  <property name="dataSource" ref="dataSource"/>
  <property name="strategy" ref="strategy"/>
  <property name="blockSize" value="1"/>
  <property name="table" value="idttest"/>
  <property name="tableName" value="test"/>		
</bean>	

<bean name="strategy" class="org.egovframe.rte.fdl.idgnr.impl.strategy.EgovIdGnrStrategyImpl">
  <property name="prefix" value="TEST-"/>
  <property name="cipers" value="5"/>
  <property name="fillChar" value="*"/>
</bean>
```
- strategy
  - 아래에 정의된 MixPrefix 의 bean name 설정
- prefix
  - 아이디의 앞에 고정적으로 붙이고자 하는 설정값 지정
- cipers
  - prefix를 제외한 아이디의 길이 지정
- fillChar
  - 0을 대신하여 표현되는 문자

##### Sample Source
```java
@Resource(name="Ids-TestWithGenerationStrategy")
private EgovIdGnrService idsTestWithGenerationStrategy;
 
@Test
public void testIdGenStrategy() throws Exception {
 
   initializeNextLongId("test", 1);
 
   // prefix : TEST-, cipers : 5, fillChar :*)
   for (int i = 0; i < 5; i++)
      assertEquals("TEST-****" + (i + 1), idsTestWithGenerationStrategy.getNextStringId());
}
```




