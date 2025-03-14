---
title: JPA Configuration
linkTitle: "JPA Configuration"
description: JPA는 persistence.xml 파일을 기반으로 동작하며, 이 파일은 실행 속성을 포함하고 여러 개의 persistence-unit을 정의할 수 있다. persistence.xml은 JPA 설정의 핵심 요소로, 상위에 <persistence> 태그를 포함하고 있다.
url: /egovframe-runtime/persistence-layer/orm/orm-jpa_configuration/
menu:
    depth:
        name: JPA Configuration
        weight: 10
        parent: "orm"
---
# JPA Configuration

 JPA는 실행 속성을 포함하고 있는 persistence.xml을 기반으로 하여 동작하도록 구성되어 있다. persistence.xml 파일의 주요 구성 요소와 속성 정의 방법에 대해 살펴보기로 한다. 먼저, persistence.xml 파일은 가장 상위에 &lt;persistence&gt; 태그를 포함하고 있으며 &lt;persistence&gt; 태그 내에 여러개의 &lt;persistence-unit&gt;를 포함할 수 있다.

## Persistence Unit

 Persistence Unit에 포함하고 있는 주요한 엔티티들은 다음과 같다.

| element 명 | 설 명 |
| --- | --- |
| provider | Entity Manager를 지원하는 Provider 클래스 |
| mapping-file | 매핑정보 파일 |
| class | Entity 클래스 리스트, @Entity, @Embeddable or @MappedSuperclass 를 포함하고 있는 클래스 |
| exclude-unlisted-classes | class 에서 정의하지 않은 것은 제외 |
| properties | JPA 구현체 프로퍼티 리스트 |

 상세한 정보는 [스키마](http://java.sun.com/xml/ns/persistence/persistence_1_0.xsd) 참조 아래는 위의 항목을 포함하고 있는 설정파일 예입니다.

```xml
   <persistence-unit name="HSQLMUnit" transaction-type="RESOURCE_LOCAL">
 
      <provider>org.hibernate.ejb.HibernatePersistence</provider>
      <class>egovframework.sample.model.bidirection.User</class>
      <exclude-unlisted-classes/>
      <properties>
         <property name="hibernate.connection.driver_class" value="net.sf.log4jdbc.DriverSpy"/>
      ...
```

## Hibernate Properties

 Properties 아래에 정의되는 Vendor별 설정 정보중에 Hibernate의 설정정보에 대해서 설명한다. 좀더 자세한 사항은 [Hibernate사이트](http://www.hibernate.org/hib_docs/reference/en/html/session-configuration.html)를 참조한다.

#### DataSource 속성

 아래의 속성들을 통해 Hibernate는 특정 DB에 접근하여 데이터 액세스 처리가 가능하다.

| 속 성 명 | 설 명 |
| --- | --- |
| hibernate.connection.driver\_class | 접근 대상이 되는 DB의 Driver 클래스명을 정의하기 위한 속성 |
| hibernate.connection.url | 접근 대상이 되는 DB의 URL을 정의하기 위한 속성 |
| hibernate.connection.username | DB에 접근할 때 사용할 사용자명을 정의하기 위한 속성 |
| hibernate.connection.password | DB에 접근할 때 사용할 패스워드를 정의하기 위한 속성 |

 다음은 위에서 언급한 속성들을 포함하고 있는 persistence.xml 파일의 일부이다

```xml
   <property name="hibernate.connection.driver_class" value="net.sf.log4jdbc.DriverSpy"/>
   <property name="hibernate.connection.url" value="jdbc:log4jdbc:hsqldb:mem:testdb"/>
   <property name="hibernate.connection.username" value="sa"/>
```

#### Generated SQL 속성

 아래의 속성들을 통해 Hibernate는 특정 DB에 접근하여 데이터 액세스 처리가 가능하다.

| 속 성 명 | 설 명 |
| --- | --- |
| hibernate.dialect | Hibernate 기반 개발시 DB에 특화된 SQL을 구성하지 않더라도 DB에 따라 알맞은 SQL을 생성할 수 있다. 이를 위해서 Dialect 클래스를 사용한다. hibernate.dialect는 Dialect 클래스명을 정의하기 위한 속성 |
| hibernate.default\_schema | Hibernate에서 SQL을 생성할 때 특정 테이블에 대해 별도 정의된 Schema가 없는 경우 적용할 DB Schema 명을 정의하기 위한 속성 |
| hibernate.default\_catalog | Hibernate에서 SQL을 생성할 때 특정 테이블에 대해 별도 정의된 Catalog가 없는 경우 적용할 DB Catalog 명을 정의하기 위한 속성 |

 다음은 위에서 언급한 속성들을 포함하고 있는 persistence.xml 파일의 일부이다

```xml
   <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
```

 다음은 Hibernate에서 제공하는 주요 Dialect 클래스 목록이다

| DB 종류 | Dialect 클래스 |
| --- | --- |
| Oracle 10g | org.hibernate.dialect.Oracle10gDialect |
| Oracle 9i/10i | org.hibernate.dialect.Oracle9iDialect |
| Oracle (모든 버전) | org.hibernate.dialect.OracleDialect |
| MySQL 5.x | org.hibernate.dialect.MySQL5Dialect |
| MySQL 4.x, 3.x | org.hibernate.dialect.MySQLDialect |
| DB2 | org.hibernate.dialect.DB2Dialect |
| Sybase 11.9.2 | org.hibernate.dialect.Sybase11Dialect |
| Sybase Anywhere | org.hibernate.dialect.SybaseAnywhereDialect |

#### Cache 속성

 아래의 속성들을 통해 Hibernate는 Cache 기능을 지원한다.

| 속 성 명 | 설 명 |
| --- | --- |
| hibernate.cache.provider\_class | Cache 기능을 구현하고 있는 구현체의 클래스명을 정의하기 위한 속성 |
| hibernate.cache.use\_second\_level\_cache | 2nd Level Cache를 적용할지 여부를 정의하기 위한 속성 (true/false) |
| hibernate.cache.use\_query\_cache | Hibernate Query를 Caching할지 여부를 정의하기 위한 속성 (true/false) |

 다음은 위에서 언급한 속성들을 포함하고 있는 persistence.xml 파일의 일부이다

```xml
   <property name="hibernate.cache.use_second_level_cache" value="true"/> 
   <property name="hibernate.cache.use_query_cache" value="true"/> 
   <property name="hibernate.cache.provider_class" value="org.hibernate.cache.EhCacheProvider"/>
```

#### Logging 속성

 아래의 속성들을 통해 Hibernate는 좀더 자세한 Logging 기능을 지원한다.

| 속 성 명 | 설 명 |
| --- | --- |
| hibernate.show\_sql | Hibernate을 통해 생성된 SQL을 콘솔에 남길 것인지 여부를 정의하는 속성 (true/false) |
| hibernate.format\_sql | hibernate.show\_sql=true인 경우 해당 SQL문의 포맷을 정돈하여 콘솔에 남길 것인지 여부를 정의하는 속성 (true/false) |
| hibernate.use\_sql\_comments | Hibernate을 통해 생성된 SQL을 콘솔에 남길 때 Comments도 같이 남길 것인지 여부를 정의하는 속성 (true/false) |

 다음은 위에서 언급한 속성들을 포함하고 있는 persistence.xml 파일의 일부이다

```xml
   <property name="hibernate.show_sql" value="true"/>
   <property name="hibernate.format_sql" value="true"/>
```

#### 기타 속성

| 속 성 명 | 설 명 |
| --- | --- |
| hibernate.hbm2ddl.auto | DDL을 자동으로 검증,생성 또는 수정할지 여부를 정의하기 위한 속성 (validate/ update/ create/ create-drop) |
| hibernate.jdbc.batch\_size | Hibernate는 일반적으로 실행해야 할 SQL들에 대해 일괄적으로 batch 처리를 수행하는데 이 때 batch로 처리할 SQL의 개수를 정의하기 위한 속성 |

 다음은 위에서 언급한 속성들을 포함하고 있는 persistence.xml 파일의 일부이다

```xml
   <property name="hibernate.hbm2ddl.auto" value="create-drop"/>
   <property name="hibernate.jdbc.batch_size" value="10" />
```