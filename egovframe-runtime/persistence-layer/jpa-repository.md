---
title: Spring Data Repository
linkTitle: "JPA Repository"
description: Spring Data는 Repository를 추상화하여 Data Access Layer 구현을 최소화하고, 메소드명만으로 쿼리를 자동 생성하는 Query Method를 지원해 개발 생산성을 높인다. CrudRepository는 기본적인 CRUD 메소드를, PagingAndSortingRepository는 페이징 및 정렬 기능을 제공한다.
url: /egovframe-runtime/persistence-layer/jpa-spring-data/jpa-repository/
menu:
    depth:
        name: JPA Repository
        weight: 1
        parent: "jpa-spring-data"
---
# Repository

## 설명
일반적으로 Data Access Layer를 구현하기 위해서는 상당량의 코드를 작성해야 한다. Spring Data에서는 Repository를 추상화하여 다양한 저장소에 접근하기 위한 Data Access Layer 구현 코드를 최소화함으로써 개발생산성을 높일 수 있도록 한다. 이는 Query Method를 통해 가능한데 Query Method란 메소드명만 가지고 쿼리를 만들 수 있다는 것이다. 특정 규칙에 맞게 메소드를 작성하면 개발자가 따로 Data Access 클래스를 만들지 않아도 Spring Data가 대신하여 해당 Database와 자동으로 매핑하여 결과를 가져다준다.

Repository 인터페이스를 상속받아 CRUD 관련 메소드들을 제공하는 CrudRepository 인터페이스와 Paging 처리 기능이 제공되는 PagingAndSortingRepository 인터페이스를 살펴보도록 하겠다.

## User Guide
### CRUD 기능 제공 인터페이스
Spring Data 리파지토리 추상화의 핵심 인터페이스는 바로 Repository이다. Repository는 일종의 마커 인터페이스로 클래스 타입과 ID 타입을 이용해서 작성할 수 있으며 Repository 인터페이스의 하위 인터페이스로 CRUD 기능을 제공하는 CrudRepository가 있다.
다음은 CrudRepository 코드이다.

```java
public interface CrudRepository<T, ID extends Serializable> extends Repository<T, ID> {

    <S extends T> S save(S entity);........................❶

    T findOne(ID primaryKey);..............................❷

    Iterable<T> findAll();.................................❸

    Long count();..........................................❹

    void delete(T entity);.................................❺

    boolean exists(ID primaryKey);.........................❻

}
```

❶ 전달받은 엔터티를 저장한다.

❷ 전달된 ID로 식별한 엔터티를 리턴한다.

❸ 모든 엔터티를 리턴한다.

❹ 엔터티의 갯수를 리턴한다.

❺ 전달받은 엔터티를 삭제한다.

❻ 전달된 ID에 해당하는 엔터티의 존재여부를 리턴한다.

### CRUD 기능 제공 인터페이스
Spring Data에서는 CrudRepository 이외에도 페이징 처리 기능을 제공하는 PagingAndSortingRespository라는 인터페이스를 제공하며 이 인터페이스는 CrudRepository를 상속받고 있다.

```java
public interface PagingAndSortingRepository<T, ID extends Serializable> extends CrudRepository<T, ID> {
    Iterable<T> findAll(Sort sort);
    Page<T> findAll(Pageable pageable);
}
```

<b>PagingAndSortingRepository</b> 인터페이스를 사용하여 2번째 페이지에서 20건의 데이터를 가져오는 예제이다.

```java
PagingAndSortingRepository<User, Long> repository = 
Page<User> users = repository.findAll(new PageRequest(1, 20));
```

## 참고자료
- [http://static.springsource.org/spring-data/data-jpa/docs/current/reference/html/](http://static.springsource.org/spring-data/data-jpa/docs/current/reference/html/)
