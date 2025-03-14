---
title: Query Method
linkTitle: "Query Method"
description: JPA 모듈은 문자열로 쿼리를 정의하거나 메서드에서 파생되어진 쿼리를 사용하는 방법을 지원한다.
url: /egovframe-runtime/persistence-layer/jpa-spring-data/jpa-querymethod/
menu:
    depth:
        name: Query Method
        weight: 2
        parent: "jpa-spring-data"
---
# Query Method

## 설명

## User Guide
### Query Method
JPA 모듈은 문자열로 쿼리를 정의하거나 메서드에서 파생되어진 쿼리를 사용하는 방법을 지원한다.

#### 쿼리생성
스트링으로 쿼리를 정의하는 예시 :

```java
public interface UserRepository extends Repository<User, Long> {
    List<User> findByEmailAddressAndLastname(String emailAddress, String lastname);
```

JPA표준 API는 위의 스트링으로 정의된 쿼리를 다음 쿼리로 변경한다.

```sql
select u from User u where u.emailAddress = ?1 and u.lastname = ?2
```

#### 지원하는 메서드 명
| Keyword             | Sample                              | JPQL snippet                                                   |
| ------------------- | ----------------------------------- | -------------------------------------------------------------- |
| `And`               | findByLastnameAndFirstname          | … where x.lastname = ?1 and x.firstname = ?2                   |
| `Or`                | findByLastnameOrFirstname           | … where x.lastname = ?1 or x.firstname = ?2                    |
| `Between`           | findByStartDateBetween              | … where x.startDate between 1? and ?2                          |
| `LessThan`          | findByAgeLessThan                   | … where x.age < ?1                                             |
| `GreaterThan`       | findByAgeGreaterThan                | … where x.age > ?1                                             |
| `After`             | findByStartDateAfter                | … where x.startDate > ?1                                       |
| `Before`            | findByStartDateBefore               | … where x.startDate < ?1                                       |
| `IsNull`            | findByAgeIsNull                     | … where x.age is null                                          |
| `IsNotNull,NotNull` | findByAge(Is)NotNull                | … where x.age not null                                         |
| `Like`              | findByFirstnameLike                 | … where x.firstname like ?1                                    |
| `NotLike`           | findByFirstnameNotLike              | … where x.firstname not like ?1                                |
| `StartingWith`      | findByFirstnameStartingWith         | … where x.firstname like ?1 (parameter bound with appended %)  |
| `EndingWith`        | findByFirstnameEndingWith           | … where x.firstname like ?1 (parameter bound with prepended %) |
| `Containing`        | findByFirstnameContaining           | … where x.firstname like ?1 (parameter bound wrapped in %)     |
| `OrderBy`           | findByAgeOrderByLastnameDesc        | … where x.age = ?1 order by x.lastname desc                    |
| `Not`               | findByLastnameNot                   | … where x.lastname <> ?1                                       |
| `In`                | findByAgeIn(Collection<Age> ages)   | … where x.age in ?1                                            |
| `NotIn`             | findByAgeNotIn(Collection<Age> age) | … where x.age not in ?1                                        |
| `True`              | findByActiveTrue()                  | … where x.active = true                                        |
| `False`             | findByActiveFalse()                 | … where x.active = false                                       |

### Using @Query
Using named queries to declare queries for entities is a valid approach and works fine for a small number of queries. As the queries themselves are tied to the Java method that executes them you actually can bind them directly using the Spring Data JPA @Query annotation rather than annotating them to the domain class. This will free the domain class from persistence specific information and co-locate the query to the repository interface.

쿼리메서드에 정의된 쿼리들은 xml에 선언된 @NamedQuery나 named queries보다 우선하여 처리됩니다.

@Query를 이용한 쿼리 선언 예제 :

```java
public interface UserRepository extends JpaRepository<User, Long> {
    @Query("select u from User u where u.emailAddress = ?1")
    User findByEmailAddress(String emailAddress);
}
```

#### 파라미터를 활용한 @Query
By default Spring Data JPA will use position based parameter binding as described in all the samples above. This makes query methods a little error prone to refactoring regarding the parameter position. To solve this issue you can use @Param annotation to give a method parameter a concrete name and bind the name in the query: 기본적으로 스프링 데이터 JPA는 위의 모든 샘플에 설명 된대로 파라미터가 바인딩 된 바인딩 위치 기반 매개 변수를 사용합니다.

파라미터를 이용한 쿼리 선언 예제 :

```java
public interface UserRepository extends JpaRepository<User, Long> {
    @Query("select u from User u where u.firstname = :firstname or u.lastname = :lastname")
    User findByLastnameOrFirstname(@Param("lastname") String lastname, @Param("firstname") String firstname);
}
```

## 참고자료
- [http://static.springsource.org/spring-data/data-jpa/docs/current/reference/html/jpa.repositories.html](http://static.springsource.org/spring-data/data-jpa/docs/current/reference/html/jpa.repositories.html)