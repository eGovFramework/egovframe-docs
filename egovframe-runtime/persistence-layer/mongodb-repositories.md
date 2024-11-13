---
linkTitle: "- Repositories"
weight: 22
draft: true
title: MongoDB Repositories
description: Spring Data MongoDB는 Spring Data의 repository 추상화 인터페이스를 지원하며, 자세한 내용은 Spring Data JPA 가이드의 Repository 섹션을 참조 한다.
---
# MongoDB Repositories

## 설명
Spring Data MongoDB도 Spring Data repository 추상화 인터페이스를 지원한다. 이에 대한 내용은 Spring Data JPA 가이드 중 [Repository](./jpa-repository.md) 부분을 참조한다.

## 1. 시작하기
MongoDB에 대한 repository를 사용하기 위해서는 다음과 같은 mongo schem의 repositories 설정이 필요하다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:mongo="http://www.springframework.org/schema/data/mongo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
		http://www.springframework.org/schema/data/mongo http://www.springframework.org/schema/data/mongo/spring-mongo.xsd">

    <mongo:mongo host="localhost" />

    <mongo:db-factory dbname="database" mongo-ref="mongo" />

    <bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
        <constructor-arg name="mongoDbFactory" ref="mongoDbFactory" />
    </bean>

    <!-- for Repository -->
    <mongo:repositories base-package="egovframework.rte.psl.data.mongodb.repository" />

</beans>
```

### Domain Object 생성
일반적인 POJO를 통해 MongoDB에 문서를 저장한다.

```java
public class Person {
    @Id
    private String id;

    private String firstname;

    private String lastname;

    private Address address;

    private double[] location;
 
    ...

    // getters/setters
```

### 기본 repository interface

```java
public interface PersonRepository extends MongoRepository<Person, Long> {

    // additional custom finder methods go here
}
```

### Paging 처리
MongoRepository interface는 기본적으로 PagingAndSortingRepository를 extends하기 때문에 다음과 같은 기본 페이징 처리를 지원한다.

```java
@Autowired
private PersonRepository repository;
 
...

@Test
public void readsFirstPageCorrectly() {

    Page<Person> persons = repository.findAll(new PageRequest(0, 10));

    LOGGER.info("Persons Total elements : " + persons.getTotalElements());

    assertTrue(persons.isFirst());
}
```

## 2. Query methods
Repository는 Spring Data에서 제공되는 keyword 기반의 query method를 사용할 수 있다.

ex:
```java
public interface PersonRepository extends MongoRepository<Person, String> {

    List<Person> findByLastname(String lastname);

    Page<Person> findByFirstname(String firstname, Pageable pageable);

    Person findByShippingAddresses(Address address);

}
```

지원되는 keyword는 다음과 같다.

| Keyword            | Sample                                 | Logic result                                                   |
| ------------------ | -------------------------------------- | -------------------------------------------------------------- |
| GreaterThan        | findByAgeGreaterThan(int age)          | {“age” : {“$gt” : age}}                                        |
| GreaterThanEqual   | findByAgeGreaterThanEqual(int age)     | {“age” : {“$gte” : age}}                                       |
| LessThan           | findByAgeLessThan(int age)             | {“age” : {“$lt” : age}}                                        |
| LessThanEqual      | findByAgeLessThanEqual(int age)        | {“age” : {“$lte” : age}}                                       |
| Between            | findByAgeBetween(int from, int to)     | {“age” : {“$gt” : from, “$lt” : to}}                           |
| In                 | findByAgeIn(Collection ages)           | {“age” : {“$in” : [ages…]}}                                    |
| NotIn              | findByAgeNotIn(Collection ages)        | “age” : {“$nin” : [ages…]}}                                    |
| IsNotNull, NotNull | findByFirstnameNotNull()               | {“age” : {“$ne” : null}}                                       |
| IsNull, Null       | findByFirstnameNull()                  | {“age” : null}                                                 |
| Like               | findByFirstnameLike(String name)       | {“age” : age} ( age as regex)                                  |
| Regex              | findByFirstnameRegex(String firstname) | {“firstname” : {“$regex” : firstname }}                        |
| (No keyword)       | findByFirstname(String name)           | {“age” : name}                                                 |
| Not                | findByFirstnameNot(String name)        | {“age” : {“$ne” : name}}                                       |
| Near               | findByLocationNear(Point point)        | {“location” : {“$near” : [x,y]}}                               |
| Within             | findByLocationWithin(Circle circle)    | {“location” : {“$within” : {“$center” : [ [x, y], distance]}}} |
| Within             | findByLocationWithin(Box box)          | {“location” : {“$within” : {“$box” : [ [x1, y1], x2, y2]}}}    |
| IsTrue, True       | findByActiveIsTrue()                   | {“active” : true}                                              |
| IsFalse, False     | findByActiveIsFalse()                  | {“active” : false}                                             |
| Exists             | findByLocationExists(boolean exists)   | {“location” : {“$exists” : exists }}                           |

## 3. Repository delete queries
위의 keyword를 delete..By 또는 remove..By 형태로 사용하는 경우 삭제 처리가 가능하다.

```java
public interface PersonRepository extends MongoRepository<Person, String> {
    List <Person> deleteByLastname(String lastname);

    Long deletePersonByLastname(String lastname);
}
```

## 4. Geo-spatial repository queries
Near keyword를 사용하는 경우 geo-spatial 처리와 관련된 query도 처리 가능하다.

```java
public interface PersonRepository extends MongoRepository<Person, String> {
    // { 'location' : { '$near' : [point.x, point.y], '$maxDistance' : distance}}
    List<Person> findByLocationNear(Point location, Distance distance);
}
```

## 5. MongoDB JSON based query methods
org.springframework.data.mongodb.repository.Query anntation을 사용할 경우 JSON query 방식을 통해 직접 query를 지정할 수 있다.

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    @Query("{ 'firstname' : ?0 }")
    List<Person> findByThePersonsFirstname(String firstname);
 
}
```