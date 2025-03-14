---
title: Cache Handling
linkTitle: "Cache Handling"
description: JPA에서는 성능 이슈를 개선하기 위해 1레벨 캐시를 활용하며, 객체를 테이블로 매핑해 데이터 액세스 처리를 수행한다. JPA 2.0부터는 2레벨 캐시가 추가되어 더 효율적인 캐시 관리가 가능해졌다.
url: /egovframe-runtime/persistence-layer/orm/orm-cache_handling/
menu:
    depth:
        name: Cache Handling
        weight: 7
        parent: "orm"
---
# Cache Handling
입력 인자로 전달된 객체를 정의된 테이블로 매핑시켜 데이터 액세스 처리를 수행해야 하는데 JPA에서는 이로 인해 발생 가능한 성능 이슈를 개선하기 위해 Cache를 활용한다. 현재 표준버전에서는 1 level Cache 만을 정의하고 있다. JPA 2.0에서는 2level Cache 정의 추가됨.

## 1 Level Cache
Entity Manager 내부에 정의된 Cache로, 트랜잭션의 시작과 종료 사이에서 사용되며 한 트랜잭션 내에서 읽혀진 객체들을 보관하는 역할을 수행한다. JPA 구현체는 하나의 트랜잭션 내에서 동일한 객체를 한 번 이상 Loading할 경우 2번째부터는 Cache로부터 해당 객체를 추출하고 또한, 한 트랜잭션 범위 내에서 객체의 속성 변경시 변경 사항은 트랜잭션 종료시에 자동적으로 DB에 반영하도록 한다. 즉, 하나의 트랜잭션 내에서 동일한 객체에 대한 재조회가 이루어지는 경우 Cache를 이용함으로써 DB 접근 횟수를 줄여주기 때문에 어플리케이션 성능 향상에 도움이 되는 것이다.

### Sample Source
```java
@Test
public void testFindUser() throws Exception {
   newTransaction();
 
   SetUpInitCacheData.initializeData(em);
 
   User user = (User) em.find(User.class, "User1");
 
   Set roles = (Set)user.getRoles();
   roles.iterator();
 
   // 1. Read from Cache
   user = (User) em.find(User.class, "User1");
 
   roles = (Set)user.getRoles();
   roles.iterator();
 
   closeTransaction();		
}
```

위와 같이 작성할 경우 동일한 트랜잭션 내에서 SetUpInitCacheData.initializeData(em)을 통해 persist된 Persistence 객체는 1LC에 저장되므로 다음에 #1번 코드에서처럼 동일한 Persistence 객체 조회시 DB에 재접근하지 않고도, Cache를 통해 조회된다.

## 2 Level Cache
2 Level Cache에 대한 것은 JPA 2.0에서 정의하고 있어서 여기서는 JPA 구현체로 쓰이는 Hibernate에서 지원하는 방법으로 가이드를 하고자 한다. 2 Level Cache는 어플리케이션 단위의 Cache로, 어플리케이션 관점에서의 Cache 기능을 지원한다. 이는 여러 트랜잭션들을 통해 Load된 Persistence 객체를 Session Factory 레벨에서 저장하는 방법으로 처리된다. persistence.xml 파일 내에 hibernate.cache.use_second_level_cache, hibernate.cache.provider_class 등을 정의 하고, 2 Level Cache에 저장되어야 할 Persistence Class 매핑 파일의 <cache> 속성을 정의하면 해당 어플리케이션을 구성하는 특정 Persistence 객체들에 대해 2LC를 적용할 수 있다. 다음은 2 Level Cache에 대한 속성이 정의되어 있는 persistence.xml 파일의 일부이다.

### Config 파일
```xml
<persistence-unit name="HSQLMCUnit" transaction-type="RESOURCE_LOCAL">
   ...
   <properties>
      <property name="hibernate.cache.use_second_level_cache" value="true"/> 
      <property name="hibernate.cache.provider_class" value="org.hibernate.cache.EhCacheProvider"/> 
   ...
   </properties>
</persistence-unit>
```

다음은 cache 속성이 READ_WRITE로 설정되어 있는 Entity 클래스의 일부이다.

```java
// Department에 지정
@Cache(usage=CacheConcurrencyStrategy.READ_WRITE)
public class Department {
 
  // Department와 User의 Join에 지정
  @Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
  @OneToMany(targetEntity=User.class, mappedBy="department" 
 	       ,cascade={CascadeType.PERSIST, CascadeType.MERGE})
  private Set<User> users ;
}
 
// User에 지정
@Entity
@Cache(usage=CacheConcurrencyStrategy.READ_WRITE)
public class User {
}
```
위에서 Department, User , Set<User> 세군데에 Cache를 지정한 것을 알 수 있다. 각각은 Department 와 User 그리고 Department와 User의 Join에 대해서 Cache를 지정하는 것이다. Cache 속성은 위에서 정의한 READ_WRITE외에도 다음과 값으로 정의할 수 있다.

- READ_OLNY : Persistence 객체가 변경되지 않는 경우에 사용 가능하다. 수정이 없으므로 분산 환경에서도 안전하게 사용 가능하며 가장 빠른 성능을 제공한다.
- NONSTRICT_READ_WRITE : 트랜잭션 격리를 엄격히 적용할 필요가 없는 경우 사용 가능하다.
- TRANSACTIONAL : 완전한 트랜잭션을 보장하나 가장 느린 성능을 제공한다.
  
### Sample Source
```java
@Test
public void testFindDepartment() throws Exception {
 
   // 데이터 입력.
   newTransaction();
   SetUpInitCacheData.initializeData(em);
   closeTransaction();
 
   //Hibernate 메소드를 이용하기 위해  Hibernate Session Factory 생성(Entity Manager 로부터 얻어냄)
   newHibernateSessionFactory();
 
   // 2Level Cache를 이용한 자료 추출(Hibernate의 메소드를 이용함)
   newSession();
   Department department = (Department) session.get(Department.class, "Dept1");
 
   Set users = department.getUsers();
   users.iterator();
   closeSession();
 
   // 2Level Cache를 이용한 자료 추출(Hibernate의 메소드를 이용함)
   newSession();
   department = (Department) session.get(Department.class, "Dept1");
 
   users = department.getUsers();
   users.iterator();
 
   // Hibernate Session close
   closeSession();		
}
```
위의 예에서 두번째 Session.get()을 통해서는 DB 접근없이 2 Level Cache의 값을 가지고 오는 것을 알 수 있다.