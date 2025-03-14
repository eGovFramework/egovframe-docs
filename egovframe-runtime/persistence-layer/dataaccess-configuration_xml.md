---
title: MyBatis Configuration XML File
linkTitle: "Configuration XML"
description: MyBatis XML 설정 파일은 `properties`, `settings`, `typeAliases`, `mappers` 등 다양한 설정 항목으로 구성되며, 데이터베이스와의 상호작용을 정의하는 중요한 설정들을 포함한다. 이 파일은 MyBatis의 동작 방식과 데이터베이스 연결 환경을 관리하는 역할을 한다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis/dataaccess-configuration_xml/
menu:
    depth:
        name: Configuration XML
        weight: 3
        parent: mybatis
---
# MyBatis Configuration XML File

 MyBatis XML 설정파일은 다양한 셋팅과 프로퍼티를 가진다 해당 파일의 작성과 상세한 옵션 설정에 대해 알아본다.

## Configuration XML

 MyBatis XML 설정파일의 일반적인 구조 및 구성은 properties, settings, typeAliases, typeHandlers, objectFactory, plugins, environments, databaseIdProvider, mappers 등의 내용으로 구성이 되어 있으며 주요 내용은 아래와 같다.

#### Sample Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
 
<configuration>
 
	<properties resource="org/mybatis/example/config.properties">
		<property name="username" value="dev_user"/>
		<property name="password" value="F2Fa3!33TYyg"/>
	</properties>
 
	<settings>
		<setting name="cacheEnabled" value="true"/>
		<setting name="lazyLoadingEnabled" value="true"/>
		<setting name="multipleResultSetsEnabled" value="true"/>
	</settings>
 
	<typeHandlers>
		<typeHandler handler="egovframework.rte.psl.dataaccess.typehandler.CalendarMapperTypeHandler" />
	</typeHandlers>
 
	<typeAliases>
		<typeAlias alias="deptVO" type="egovframework.rte.psl.dataaccess.vo.DeptVO" />
		<typeAlias alias="empVO" type="egovframework.rte.psl.dataaccess.vo.EmpVO" />
	.
	.
	. 
 
</typeAliases>
 
.
.
.
.
 
</configuration>
```

- properties : 표준 java properties (key=value 형태)파일에 대한 연결을 지원하며 설정 파일내에서 ${key} 와 같은 형태로 properties 형태로 외부화해놓은 실제 값(여기서는 DB 접속 관련 driver, url, id/pw)을 참조할 수 있다. resource 속성으로 classpath, url 속성으로 유효한 URL 상에 있는 자원을 지정 가능하다.

- settings : 런타임시 MyBatis의 행위를 조정하기 위한 옵션 설정을 통해 최적화할 수 있도록 지원한다. 다음표는 셋팅과 그 의미 그리고 디폴트 값을 설명한다.

| 셋팅 | 설명 | 사용가능한 값들 | 디폴트 |
| --- | --- | --- | --- |
| cacheEnabled | 설정에서 각 mapper 에 설정된 캐시를 전역적으로 사용할지 말지에 대한 여부 | true / false | TRUE |
| lazyLoadingEnabled | 늦은 로딩을 사용할지에 대한 여부. 사용하지 않는다면 모두 즉시 로딩할 것이다. | true / false | TRUE |
| aggressiveLazyLoading | 활성화 상태로 두게 되면 늦은(lazy) 로딩 프로퍼티를 가진 객체는 호출에 따라 로드될 것이다. 반면에 개별 프로퍼티는 요청할때 로드된다. | true / false | TRUE |
| multipleResultSetsEnabled | 한개의 구문에서 여러개의 ResultSet 을 허용할지의 여부(드라이버가 해당 기능을 지원해야 함) | true / false | TRUE |
| useColumnLabel | 칼럼명 대신에 칼럼라벨을 사용. 드라이버마다 조금 다르게 작동한다. 문서와 간단한 테스트를 통해 실제 기대하는 것처럼 작동하는지 확인해야 한다. | true / false | TRUE |
| useGeneratedKeys | 생성키에 대한 JDBC 지원을 허용. 지원하는 드라이버가 필요하다. true 로 설정하면 생성키를 강제로 생성한다. 일부 드라이버(예를들면, Derby)에서는 이 설정을 무시한다. | true / false | FALSE |
| autoMappingBehavior | MyBatis 가 칼럼을 필드/프로퍼티에 자동으로 매핑할지와 방법에 대해 명시. PARTIAL 은 간단한 자동매핑만 할뿐, 내포된 결과에 대해서는 처리하지 않는다. FULL 은 처리가능한 모든 자동매핑을 처리한다. | NONE, PARTIAL, FULL | PARTIAL |
| defaultExecutorType | 디폴트 실행자(executor) 설정. SIMPLE 실행자는 특별히 하는 것이 없다. REUSE 실행자는 PreparedStatement 를 재사용한다. BATCH 실행자는 구문을 재사용하고 수정을 배치처리한다. | SIMPLE REUSE BATCH | SIMPLE |
| defaultStatementTimeout | 데이터베이스로의 응답을 얼마나 오래 기다릴지를 판단하는 타임아웃을 셋팅 | 양수 | 셋팅되지 않음(null) |
| safeRowBoundsEnabled | 중첩구문내 RowBound 사용을 허용 | true / false | FALSE |
| mapUnderscoreToCamelCase | 전통적인 데이터베이스 칼럼명 형태인 A\_COLUMN을 CamelCase형태의 자바 프로퍼티명 형태인 aColumn으로 자동으로 매핑하도록 함 | true / false | FALSE |
| localCacheScope | MyBatis uses local cache to prevent circular references and speed up repeated nested queries. By default (SESSION) all queries executed during a session are cached. If localCacheScope=STATEMENT local session will be used just for statement execution, no data will be shared between two different calls to the same SqlSession. | SESSION / STATEMENT | SESSION |
| jdbcTypeForNull | Specifies the JDBC type for null values when no specific JDBC type was provided for the parameter. Some drivers require specifying the column JDBC type but others work with generic values like NULL, VARCHAR or OTHER. | JdbcType enumeration. Most common are: NULL, VARCHAR and OTHER | OTHER |
| lazyLoadTriggerMethods | Specifies which Object's methods trigger a lazy load | A method name list separated by commas | equals,clone,hashCode,toString |
| defaultScriptingLanguage | Specifies the language used by default for dynamic SQL generation. | A type alias or fully qualified class name. | org.apache.ibatis.scripting.xmltags.XMLDynamicLanguageDriver |
| callSettersOnNulls | Specifies if setters or map's put method will be called when a retrieved value is null. It is useful when you rely on Map.keySet() or null value initialization. Note primitives such as (int,boolean,etc.) will not be set to null. | true / false | FALSE |
| logPrefix | Specifies the prefix string that MyBatis will add to the logger names. | Any String | Not set |
| logImpl | Specifies which logging implementation MyBatis should use. If this setting is not present logging implementation will be autodiscovered. | SLF4J / LOG4J / LOG4J2 / JDK\_LOGGING / COMMONS\_LOGGING / STDOUT\_LOGGING / NO\_LOGGING | Not set |
| proxyFactory | Specifies the proxy tool that MyBatis will use for creating lazy loading capable objects. | CGLIB / JAVASSIST | CGLIB |

- typeAliases : 타입 별칭을 통해 자바 타입에 대한 좀더 짧은 이름을 사용할 수 있다. 오직 XML 설정에서만 사용되며, 타이핑을 줄이기 위해 사용된다.

- typeHandler : MyBatis 가 PreparedStatement 에 파라미터를 셋팅하고 ResultSet 에서 값을 가져올때마다, TypeHandler 는 적절한 자바 타입의 값을 가져오기 위해 사용된다. typeHandler 구현체를 등록하여 사용할 수 있다.

- objectFactory : MyBatis 는 결과 객체의 인스턴스를 만들기 위해 ObjectFactory를 사용한다.

- mappers: 매핑된 SQL 구문을 정의한다. 해당 매퍼 파일의 지정은 클래스패스에 상대적으로 리소스를 지정할 수도 있고, url 을 통해서 지정할 수 도 있다

 이외에도 plugins (매핑 구문을 실행하는 어떤 시점에 호출을 가로챈다. 기본적으로 MyBatis 는 메서드 호출을 가로채기 위한 플러그인을 허용한다), environments (여러개의 환경으로 설정), databaseIdProvider(데이터베이스 제품마다 다른 구문을 실행) 등의 설정을 통해 다양한 환경 및 시점에서 추가적인 설정이 가능하다.
