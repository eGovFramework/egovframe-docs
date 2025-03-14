---
title: MongoDB support
linkTitle: "MongoDB support"
description: Spring Data MongoDB는 MongoDB를 위한 Data Access 기능을 제공하는 하위 프로젝트로, MongoTemplate을 통한 효율적인 데이터 처리와 Annotation 기반 매핑, Java 기반의 Query 및 Criteria DSL을 지원한다. 또한, Spring의 데이터 액세스 예외 계층 구조 변환 기능과 Spring Data Repository 인터페이스 통합을 제공한다. 이를 통해 MongoDB와의 데이터 접근을 보다 쉽게 구현할 수 있다.
url: /egovframe-runtime/persistence-layer/mongodb/mongodb-supprot3_5_1/
menu:
    depth:
        name: MongoDB support
        weight: 1
        parent: "mongodb"
---
# MongoDB support 3.5.1

## 설명
Spring Data MongoDB는 Spring Data의 하위 프로젝트로서 document-oriented storage를 지원하는 MongoDB에 대한 Data Access 기능을 제공한다.

### MongoDB support 주요 기능
- Spring configuration 지원 (@Configuration, XML namespace)
- 기본 처리를 효율적으로 지원하는 MongoTemplate helper 제공
- Spring이 제공하는 Data Access Exception hierarchy 변환 기능 제공
- Spring의 Conversion Service와 통합된 Feature Rich Object Mapping 기능
- Annotation 기반 매핑 metadata
- Java 기반 Query, Criteria, Update DSLs
- Spring Data의 Repository 인페이스 지원
- QueryDSL 등

##  1. 시작하기
Spring Data MongoDB를 사용하기 위해서는 다음과 같은 dependency 추가가 필요하다.

```xml
<dependency>
    <groupId>org.springframework.data</groupId>
    <artifactId>spring-data-mongodb</artifactId>
    <version>1.7.2.RELEASE</version>
</dependency>
```

## 2. Spring 관련 설정
### Mongo mongo-client, mongoTemplate 생성
Spring 기반에서는 다음과 같이 Mongo에 대한 인스턴스 생성이 필요하다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mongo="http://www.springframework.org/schema/data/mongo"
       xsi:schemaLocation=
               "http://www.springframework.org/schema/context
          http://www.springframework.org/schema/context/spring-context-4.0.xsd
          http://www.springframework.org/schema/data/mongo
          http://www.springframework.org/schema/data/mongo/spring-mongo.xsd
          http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans-4.0.xsd">
    <!-- Default bean name is 'mongo' -->
    <mongo:mongo-client
            host="localhost"
            port="27017"
            credentials="id:password@database"
            id="mongo">
    </mongo:mongo-client>

</beans>
```

추가적으로 MongoDB가 replica 방식으로 굿어된 경우는 다음과 같이 replica-set 설정을 지정하면 된다.

```xml
<mongo:mongo id="replicaSetMongo" replica-set="127.0.0.1:27017,localhost:27018"/>
```

### MongoDBFactory 생성
다음으로 Mongo 인스턴스와 연결을 위한 MongoDBFactory이 필요한데, XML 기반의 설정에서는 다음과 같이 지정할 수 있다.

```xml
<!-- Default bean name is 'mongoDbFactory' -->
<mongo:db-factory dbname="database" mongo-ref="mongo" id="mongoDbFactory" />
```

### MongoTemplate 생성
실제 mongoDB에 대한 처리(operations)를 위하여 MongoTemplate을 생성한다.

MontoTemplate의 다은과 같은 생성자를 통해 생성될 수 있다.
- MongoTemplate(Mongo mongo, String databaseName)
- MongoTemplate(Mongo mongo, String databaseName, UserCredentials userCredentials) : 사용자 접속 정보 추가
- MongoTemplate(MongoDbFactory mongoDbFactory) : MogoDbFactory(com.mongodb.Mongo object, database name 및 접속 계정 포함)를 통한 연결
- MongoTemplate(MongoDbFactory mongoDbFactory, MongoConverter mongoConverter) : 매핑을 위한 MongoConverter 사용

XML 설정일 경우는 다음과 같이 생성할 수 있다.

```xml
<mongo:mongo-client
        host="localhost"
        port="27017"
        credentials="id:password@database"
        id="mongo">
</mongo:mongo-client>

<bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
    <constructor-arg ref="mongo"/>
    <constructor-arg name="databaseName" value="geospatial"/>
</bean>
```

MongoDbFactory를 사용하는 경우 다음과 같이 지정할 수 있다.

```xml
<!-- Default bean name is 'mongo' -->
<mongo:mongo-client
        host="localhost"
        port="27017"
        credentials="id:password@xxx"
        id="mongo">
</mongo:mongo-client>

<!-- for Replica Sets -->
<!-- mongo:mongo id="replicaSetMongo" replica-set="127.0.0.1:27017,127.0.0.1:27018" /-->

<!-- Default bean name is 'mongoDbFactory' -->
<mongo:db-factory dbname="database" mongo-ref="mongo" id="mongoDbFactory" />

<bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
    <constructor-arg name="mongoDbFactory" ref="mongoDbFactory" />
</bean>
```

### 기본 처리
MongoTemplate는 저장, 수정, 삭제 및 object 매팽 등의 기본 기능을 제공한다.

다음은 Person 객체에 대한 간단한 기본 예제이다.

#### Person 클래스

```java
public class Person {

    private String id;
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Person [id=" + id + ", name=" + name + ", age=" + age + "]";
    }

}
```

#### Test 클래스

```java
@Resource(name="mongoTemplate")
private  MongoTemplate mongoTemplate;
 
@Test
public void testBasicOperations() {
 
	Person person = new Person("Joe", 34);
 
	// Insert
	mongoTemplate.insert(person);
	LOGGER.info("Insert : " + person);
 
	// Find
	person = mongoTemplate.findOne(new Query(where("name").is("Joe")), Person.class);
	LOGGER.info("Found: " + person);
 
	assertEquals("Joe", person.getName());
 
	// Update
	mongoTemplate.updateFirst(query(where("name").is("Joe")), update("age", 35), Person.class);    
	person = mongoTemplate.findOne(query(where("name").is("Joe")), Person.class);
	LOGGER.info("Updated: " + person);
 
	assertEquals(35, person.getAge());
 
	// Delete
	mongoTemplate.remove(person);
 
	// Check that deletion worked
	List<Person> people =  mongoTemplate.findAll(Person.class);
	LOGGER.info("Number of people = : " + people.size());
	assertEquals(0, people.size());
 
	mongoTemplate.dropCollection("person");
 
}
```

※ 내부적으로 MongoConverter에 의해 String과 ObjectId에 대해서는 자동 변환 처리됨

### _id 필드 처리
MongoDB는 모든 문서에 대하여 '_id' 필드를 가져야 한다. 그렇지 않은 경우 내부적으로 자동생성되는 ObjectId로 처리된다.
그러나 MongoMappingConverter가 사용되면 다음과 같은 규칙에 의해 '_id' 필드에 대한 매핑을 처리한다.

- @Id(org.springframework.data.annotation.Id)가 지정된 property가 '_id'에 매핑된다.
- id라는 이름의 property는 '_id'로 매핑된다. (위 Person 예제의 경우 이에 해당)

### 문서 저장 처리(save, insert)
MongoTemplate에는 객체를 저장하기 위한 몇 개의 메소드를 제공한다.
가장 간단한 경우가 POJO를 저장하는 것이다. 이 경우 collection 이름은 클래스명(not fully qualifed)이 사용되면, 저장 메소스 호출 시 지정될 수도 있다.

다음은 저장 처리 메소드에 대한 정리이다.

- void save(Object objectToSave) : 기본 collection에 저장
- void save(Object objectToSave, String collectionName) : 지정된 collection에 저장
- void insert(Object objectToSave) : 기본 collection에 등록
- void insert(Object objectToSave, String collectionName) : 지정된 collection에 등록

※ MongoTemplate은 저장을 위해 save와 insert를 제공하는데, save의 경우는 기존 등록된 문서가 없는 경우 insert로 처리되며 존재하는 경우 덮어쓰기를 한다.

insert의 경우 기존 id가 존재하면 오류를 발생한다.

### 문서 수정 처리(update)
문서 수정 처리를 위해서는 첫번째 문서만을 수정하는 updateFirst 메소드와 모든 문서를 수정하는 updateMulti로 구성된다.

다음은 계정이 저축계좌(SAVINGS)인 모든 계좌에 50원을 추가하는 예제이다.

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import static org.springframework.data.mongodb.core.query.Query;
import static org.springframework.data.mongodb.core.query.Update;
 
    ...

    WriteResult wr = mongoTemplate.updateMulti(
            new Query(where("accounts.accountType").is(Account.Type.SAVINGS)),
            new Update().inc("accounts.$.balance", 50.00),
            Account.class);
```

#### Update class 저장 메소드
- Update addToSet (String key, Object value) Update using the $addToSet update modifier
- Update inc (String key, Number inc) Update using the $inc update modifier
- Update pop (String key, Update.Position pos) Update using the $pop update modifier
- Update pull (String key, Object value) Update using the $pull update modifier
- Update pullAll (String key, Object[] values) Update using the $pullAll update modifier
- Update push (String key, Object value) Update using the $push update modifier
- Update pushAll (String key, Object[] values) Update using the $pushAll update modifier
- Update rename (String oldName, String newName) Update using the $rename update modifier
- Update set (String key, Object value) Update using the $set update modifier
- Update unset (String key) Update using the $unset update modifier

## 참고자료
MongoDB에 대한 기본 처리는 [MongoDB Manual](http://docs.mongodb.org/manual/)을 참조하고, Spring과의 연동 부분에 대한 세부적인 처리는 Spring Data MongoDB에 대한 [Reference](http://docs.spring.io/spring-data/data-mongo/docs/1.5.2.RELEASE/reference/html/mongo.core.html)를 참조한다.