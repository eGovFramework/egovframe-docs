---
title: iBATIS Configuration
linkTitle: "iBATIS Configuration"
description: iBATIS 의 메인 설정 파일인 SQL Map XML Configuration 파일(이하 sql-map-config.xml 설정 파일) 작성과 상세한 옵션 설정에 대해 알아본다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-ibatis_configuration/
menu:
    depth:
        name: iBATIS Configuration
        weight: 1
        parent: dataaccess-ibatis
---
# iBATIS Configuration

 iBATIS 의 메인 설정 파일인 SQL Map XML Configuration 파일(이하 sql-map-config.xml 설정 파일) 작성과 상세한 옵션 설정에 대해 알아본다.

## sql-map-config.xml

 SqlMapClient 설정관련 상세 내역을 제어할 수 있는 메인 설정 파일로 주로 transaction 관리 관련 설정 및 다양한 옵션 설정, Sql Mapping 파일들에 대한 path 설정 등을 포함한다.

#### Sample Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE sqlMapConfig PUBLIC "-//ibatis.apache.org//DTD SQL Map Config 2.0//EN"
"http://ibatis.apache.org/dtd/sql-map-config-2.dtd">

 
<sqlMapConfig>
 
	<properties resource="META-INF/spring/jdbc.properties" />
 
	<settings cacheModelsEnabled="true" enhancementEnabled="true"
		lazyLoadingEnabled="true" maxRequests="128" maxSessions="10"
		maxTransactions="5" useStatementNamespaces="false"
		defaultStatementTimeout="1" />
 
	<typeHandler javaType="java.util.Calendar" jdbcType="TIMESTAMP"
		callback="egovframework.rte.psl.dataaccess.typehandler.CalendarTypeHandler" />
 
	<transactionManager type="JDBC">
		<dataSource type="DBCP">
			<property name="driverClassName" value="${driver}" />
			<property name="url" value="${dburl}" />
			<property name="username" value="${username}" />
			<property name="password" value="${password}" />
			<!-- OPTIONAL PROPERTIES BELOW -->
			<property name="maxActive" value="10" />
			<property name="maxIdle" value="5" />
			<property name="maxWait" value="60000" />
			<!-- validation query -->
			<!--<property name="validationQuery" value="select * from DUAL" />-->
			<property name="logAbandoned" value="false" />
			<property name="removeAbandoned" value="false" />
			<property name="removeAbandonedTimeout" value="50000" />
			<property name="Driver.DriverSpecificProperty" value="SomeValue" />
		</dataSource>
	</transactionManager>
 
	<sqlMap resource="META-INF/sqlmap/mappings/testcase-basic.xml" />
	<sqlMap ../>
	..
</sqlMapConfig>
```

- properties : 표준 java properties (key=value 형태)파일에 대한 연결을 지원하며 설정 파일내에서 ${key} 와 같은 형태로 properties 형태로 외부화 해놓은 실제의 값(여기서는 DB 접속 관련 driver, url, id/pw)을 참조할 수 있다. resource 속성으로 classpath, url 속성으로 유효한 URL 상에 있는 자원을 지정 가능하다.
- settings : 이 설정 파일을 통해 생성된 SqlMapClient instance 에 대하여 다양한 옵션 설정을 통해 최적화할 수 있도록 지원한다. 모든 속성은 선택사항(optional) 이다.

| 속성 | 설명 | Example, Default |
| --- | --- | --- |
| maxRequests | 같은 시간대에 SQL 문을 실행한 수 있는 thread 의 최대 갯수 지정. | maxRequests=“256”, 512 |
| maxSessions | 주어진 시간에 활성화될 수 있는 session(또는 client) 수 지정. | maxSessions=“64”, 128 |
| maxTransactions | 같은 시간대에 SqlMapClient.startTransaction() 에 들어갈 수 있는 최대 갯수 지정. | maxTransactions=“16”, 32 |
| cacheModelsEnabled | SqlMapClient 에 대한 모든 cacheModel 에 대한 사용 여부를 global 하게 지정. | cacheModelsEnabled=“true”, true (enabled) |
| lazyLoadingEnabled | SqlMapClient 에 대한 모든 lazy loading 에 대한 사용 여부를 global 하게 지정. | lazyLoadingEnabled=“true”, true (enabled) |
| enhancementEnabled | runtime bytecode enhancement 기술 사용 여부 지정. | enhancementEnabled=“true”, false (disabled) |
| useStatementNamespaces | mapped statements 에 대한 참조 시 namespace 조합 사용 여부 지정. true 인 경우 queryForObject(“sqlMapName.statementName”); 과 같이 사용함. | useStatementNamespaces=“false”, false (disabled) |
| defaultStatementTimeout | 모든 JDBC 쿼리에 대한 timeout 시간(초) 지정, 각 statement 의 설정으로 override 가능함. 모든 driver가 이 설정을 지원하는 것은 아님에 유의할 것. | 지정하지 않는 경우 timeout 없음(cf. 각 statement 설정에 따라) |
| classInfoCacheEnabled | introspected(java 의 reflection API에 의해 내부 참조된) class의 캐쉬를 유지할지에 대한 설정 | classInfoCacheEnabled=“true”, true (enabled) |
| statementCachingEnabled | prepared statement 의 local cache 를 유지할지에 대한 설정 | statementCachingEnabled=“true”, true (enabled) |

- typeHandler : javaType ↔ jdbcType 간의 변환(prepared statement 의 파라메터 세팅/resultSet 의 값 얻기)을 처리하는 typeHandler 구현체를 등록할 수 있다.
- transactionManager : 트랜잭션 관리 서비스를 설정할 수 있다. type 속성으로 어떤 트랜잭션 관리자를 사용할지 지시할 수 있는데, JDBC, JTA, EXTERNAL 의 세가지 트랜잭션 관리자가 프레임워크에 포함되어 있다. 위에서는 일반적인 Connection commit()/rollback() 메서드를 통해 트랜잭션을 관리하는 JDBC 타입으로 설정하였다.
- dataSource : transactionManager 설정의 일부 영역으로 DataSource 에 대한 설정이다. type 속성으로 어떤 DataSourceFactory 를 사용할지 지시할 수 있는데, SIMPLE, DBCP, JNDI 의 세가지 설정이 가능하다. 위에서는 Apache Commons DBCP(Database Connection Pool) 를 사용하는 DBCP 타입으로 설정하였다. iBATIS 는 DBCP 속성에 대한 설정을 직접 명시할 수 있도록 지원하고 있다. iBATIS 2 버전 이후로는 단일 dataSource 만 지원한다.
- sqlMap : 명시적으로 각 SQL Map XML 파일을 포함하도록 설정한다. classpath (resource 속성으로 지정) 나 url(url 속성으로 지정) 상의 자원을 stream 형태로 로딩하게 된다. 위에서는 classpath 상에 존재하는 sql 매핑 파일을 지정하였다.

 이 외에도 typeAlias(global 한 type 별명-풀패키지명에 비해 간략히), resultObjectFactory (SQL 문의 실행에 의한 결과 객체의 생성을 iBATIS 의 ResultObjectFactory 인터페이스를 구현한 factory 클래스를 통해 처리할 수 있도록 지원) 에 대한 설정이 가능하다. DTD 상 sqlMap 설정은 하나 이상이 필요하고 다른 설정은 선택사항 이다.

## SQL Map XML 파일 (sql 매핑 파일)

 sql 매핑 파일은 iBATIS 의 mapped statement 형태로 처리될 수 있도록 SQL Map 문서 구조에 따라 다양한 옵션 설정 및 매핑 정의, sql 문을 외부화하여 저장하는 파일이다.

#### Sample SQL Map XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE sqlMapConfig PUBLIC "-//ibatis.apache.org//DTD SQL Map Config 2.0//EN" "http://ibatis.apache.org/dtd/sql-map-config-2.dtd">
 
<sqlMap namespace="Dept">
 
	<typeAlias alias="deptVO" type="egovframework.DeptVO" />
 
	<resultMap id="deptResult" class="deptVO">
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
	</resultMap>
 
	<insert id="insertDept" parameterClass="deptVO">
		insert into DEPT
		           (DEPT_NO,
		            DEPT_NAME,
		            LOC)
		values     (#deptNo#,
		            #deptName#,
		            #loc#)
	</insert>
 
	<select id="selectDept" parameterClass="deptVO" resultMap="deptResult">
		<![CDATA[
			select DEPT_NO,
			       DEPT_NAME,
			       LOC
			from   DEPT
			where  DEPT_NO = #deptNo#
		]]>
	</select>
 
</sqlMap>
```

- typeAlias : 현재 매핑 파일내에서 객체에 대한 간략한 alias 명을 지정함. (cf. 매우 자주 쓰이는 class 의 경우 sql-map-config.xml 에 global 하게 등록하는 것이 좋음)
- resultMap : DB 칼럼명(select 문의 칼럼 alias) 과 결과 객체의 attribute 에 대한 매핑 및 추가 옵션을 정의함.
- insert, select : 각 statement 타입에 따른 mapped statement 정의 요소 예시. 유형에 따라 insert/update/delete/select/procedure/statement 요소 사용 가능

 이 외에도 parameterMap, resultMap 에 대한 상세 정의, cacheModel 설정, sql 문 재사용을 위한 sql 요소 설정이 나타날 수 있다. 각각에 대한 상세 사항은 관련 가이드를 참고한다.

##### Mapped Statement

 Data Mapper 사상의 핵심으로 Mapped Statement 는 parameter 매핑(input) 과 result 매핑(output) 을 가질 수 있는 어떤 SQL 문이라도 될 수 있다. 단순하게는 파라메터나 결과에 대한 class 를 직접적으로 설정할 수 있으며(권고하지 않는 방법이지만 아예 설정하지 않고 프레임워크에서 제공하는 자동 맵핑 처리도 가능), in/out 매핑, 결과의 cache 유지 등에 대한 상세한 설정이 가능하다.

- statement 구문

```xml
<statement id="statementName"
	   [parameterClass="some.class.Name"]
	   [resultClass="some.class.Name"]
	   [parameterMap="nameOfParameterMap"]
	   [resultMap="nameOfResultMap"]
	   [cacheModel="nameOfCache"]
	   [timeout="5"]>
	select * from PRODUCT where PRD_ID = [?|#propertyName#]
	order by [$simpleDynamic$]
</statement>
```

- 위 statement 요소 위치에는 sql 문 유형에 따라 insert, update, delete, select, procedure 가 올 수 있다. 위에서 대괄호\[\] 내에 있는 속성은 선택 사항이다.
- parameterClass 나 resultClass 속성으로 In/Out 에 대한 객체를 직접 지정할 수 있다. 이는 일반적으로 표준 JavaBeans 객체 또는 Map (result 인 경우에는 Map 구현체 명시할 것) 이 될수 있으며, 단일 변수인 경우에는 primitive 래퍼 클래스로 지정할 수도 있다.
- prepared statement 에 대한 바인드 변수 맵핑을 위한 맵핑 정의를 별도의 parameterMap 태그로 따로 지정한 경우 위의 parameterMap 속성으로 해당 id 를 지정한다. parameterMap 을 지정한 경우 sql 문의 바인드 변수 영역은 ? 로 작성하며 parameterMap 매핑 설정의 순서와 갯수가 맞아야 함에 유의한다.
- parameterMap 을 쓰지 않고 Inline Parameter 로 쓰는 것을 더 선호하며 #속성명# 과 같은 형태로 간략히 기술할 수 있다.
- resultSet 에 대한 결과 객체 매핑을 위해 별도의 resultMap 태그로 따로 지정한 경우 위의 resultMap 속성으로 해당 id 를 지정한다. resultMap 의 사용은 성능상, 상세 옵션의 적용 기능성 측면에서 추천하는 바이다.
- 한번 조회 한 결과를 캐슁하기 위해 별도의 cacheModel 태그로 관련 설정을 한 경우, 대상 statement 에 해당 cacheModel id 를 위의 cacheModel 속성과 같이 지시한다. DB 데이터의 변경 시 cache 를 갱신할 수 있도록 cacheModel 설정의 flush 관련 설정에 유의해야 한다.
- 사용 DBMS 와 JDBC 드라이버가 지원하는 경우 timeout 을 명시할 수 있으며 이는 sql-map-config.xml 의 defaultStatementTimeout 에 우선한다.
- 위의 order by 절에 쓰인 $변수명$ 은 replaced Text 처리로 input 객체에 해당 변수에 대한 값으로 전달된 String 을 SQL 의 동적 변경 요소로 대치(replace)하여 처리한다. 바인드 변수로 처리할 수 없는 order by 절이나 from 절, 혹은 전체 sql 문의 동적 변경 등을 위해 사용될 수 있으나, SQL Injection 의 보안 위험이 있고, 테이블이나 칼럼이 변경되는 경우 내부적으로 자동 매핑된 결과 객체에 대한 resultSet metadata 의 캐슁내역과 맞지 않아 오류를 일으킬 수 있으므로 유의한다.