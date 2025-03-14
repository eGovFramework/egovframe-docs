---
title: Fetch Strategy
linkTitle: "Fetch Strategy"
description: ORM에서 기본적으로 Lazy Loading을 사용하여 필요한 시점에 SQL을 실행하지만, 성능 이슈를 해결하기 위해 Batch 조회, Sub-Query 조회, Join Fetch와 같은 다양한 Fetch 전략이 있다. 이 전략들은 JPA 표준이 아닌 Hibernate 구현체에서 제공되는 기능이다.
url: /egovframe-runtime/persistence-layer/orm/orm-fetch_strategy/
menu:
    depth:
        name: Fetch Strategy
        weight: 8
        parent: "orm"
---
# Fetch Strategy
ORM 서비스는 기본적으로 Entity간의 연관관계를 정의하고 정의된 연관관계를 가지고 관련 Entity를 추출하여 사용한다. 관련 Entity를 추출하는데 기본적으로 Lazy Loading이란 기법을 통해서 객체가 실제로 필요하기 전까지 SQL을 실행하지 않고 Proxy 객체로 리턴하도록 하고 한다. 그러나 이러한 Lazy Loading으로 처리하게 되면 Lazy Loading을 하지 않는 것에 대비하여 필요시점에 쿼리를 여러번 수행해야 하는 문제가 발생한다. 이런 문제를 해결하기 위한 여러가지 Fetch 전략이 존재하는데 **Batch를 이용하여 데이터 조회, Sub-Query를 이용하여 데이터 조회, Join Fetch를 이용하여 데이터 한꺼번에 조회하는 방법**이 있다. 하지만 이 서비스는 JPA표준이 아닌 구현체인 Hibernate에 정의된 사항이다.

## Batch를 이용하여 데이터 조회
Entity 클래스에 BatchSize를 지정할 경우 지정한 개수만큼 해당 객체를 로딩하는 방식으로 쿼리 실행 회수가 n / batch size + 1로 감소한다. 다음은 batch-size 설정 예인 Department 클래스 파일의 일부이다.

### Config Source
```java
@Entity
public class Department implements Serializable {
   ...
   @org.hibernate.annotations.BatchSize(size=2)
   private Set<User> users ;
   ...
}
```
위에서 Department에 속한 Set<User> 을 추출할 때 적용되는 BatchSize를 2로 지정하였다.

### Sample Source
```java
   qlBuf.append("FROM Department");
   Query query = em.createQuery(qlBuf.toString());
 
   List deptList = query.getResultList();
 
   assertEquals("fail to match the size of department list.", 3, deptList.size());
 
   for (int i = 0; i < deptList.size(); i++) {
 
      Department department = (Department) deptList.get(i);
 
      if (i == 0) {
         assertEquals("fail to match a department name.", "HRD", department.getDeptName());
 
         Set users = department.getUsers();
         assertEquals("fail to match the size of user list.", 2, users.size());
 
      } else if (i == 1) {
         assertEquals("fail to match a department name.", "PD", department.getDeptName());
 
         Set users = department.getUsers();
         assertEquals("fail to match the size of user list.", 1, users.size());
   ...
```
위의 Config와 Sample에 의해서 query.getResultList()에 의한 것과 department.getUsers() 호출 시 자동 생성되는 SQL Query는 다음과 같다.

### Generated SQL
```SQL
SELECT ... FROM USER user0_
 
SELECT ... 
FROM USER users0_ 
WHERE users0_.DEPT_ID IN (?, ?)
```
위에 where 절의 [in (?,?)]에서의 ?의 숫자가 BatchSize이다. 위에서 2로 설정했기에 두개 지정되어 조회된다.

## Sub-Query를 이용하여 데이터 조회
Entity 클래스에 FetchMode를 SUBSELECT로 지정할 경우 Sub Query 형태의 SELECT 문이 수행되며 한번에 모두 로딩하게 된다. 다음은 SUBSELECT 설정 예인 User 클래스 파일의 일부이다.

### Config Source
```java
@Entity
public class User implements Serializable {
    ...
    @org.hibernate.annotations.Fetch(org.hibernate.annotations.FetchMode.SUBSELECT) 
    private Set<Role> roles = new HashSet(0);	
    ...
}
```
위에서 User에 속한 Set\<Role> 을 추출할 때 적용되는 FetchMode를 SUBSELECT 로 지정하였다.

### Sample Source
```java
   qlBuf.append("FROM User");
   Query query = em.createQuery(qlBuf.toString());
   List userList = query.getResultList();
 
   assertEquals("fail to match the size of user list.", 3, userList.size());
 
   for (int i = 0; i < userList.size(); i++) {
      User user = (User) userList.get(i);
 
      if (i == 0) {
         assertEquals("fail to match a user name.", "kim" , user.getUserName());
         assertEquals("fail to match a user password.", "kim123" , user.getPassword());
 
         Set roles = user.getRoles();
         assertEquals("fail to match the size of role list.", 2 , roles.size());
      } else if (i == 1) {
         assertEquals("fail to match a user name.", "lee" , user.getUserName());
         assertEquals("fail to match a user password.", "lee123" , user.getPassword());
         ...
```
위의 Config와 Sample에 의해서 query.getResultList() 호출 시와 user.getRoles() 호출 시 자동 생성되는 <Acronym title="Structured Query Language">SQL</Acronym> Query는 다음과 같다.

### Generated SQL
```SQL
SELECT ... FROM USER user0_
 
SELECT ... 
FROM AUTHORITY roles0_ LEFT OUTER JOIN ROLE role1_ ON roles0_.ROLE_ID=role1_.ROLE_ID 
WHERE roles0_.USER_ID IN (SELECT user0_.USER_ID FROM USER user0_)
```
위에 where절의 [in (select user0_.USER_ID from USER user0_)]를 보면 Sub Query 형태로 해당하는 모든 User에 대해서 모든 Roles 정보를 추출하는 것을 확인 할 수 있다.

## join fetch를 이용하여 데이터 한꺼번에 조회하는 방법
Entity 클래스에서의 별도 설정없이 QL 수행시 join fetch 를 기재함으로써 한번에 연관된 자식 엔티티를 모두 추출하여 사용한다.

### Sample Source
```java
   qlBuf.append("SELECT user ");
   // JOIN FETCH 를 이용함.
   qlBuf.append("FROM User user join fetch user.roles role ");
   qlBuf.append("WHERE role.roleName = ?");
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter(1, "Admin");
   List userList = query.getResultList();
 
   assertEquals("fail to match the size of user list.", 2, userList.size());
 
   for (int i = 0; i < userList.size(); i++) {
      User user = (User) userList.get(i);
 
      if (i == 0) {
         assertEquals("fail to match a user name.", "kim",user.getUserName());
         assertEquals("fail to match a user password.", "kim123",user.getPassword());
 
         Set roles = user.getRoles();
         assertEquals("fail to match the size of role list.", 1, roles.size());
      } else if (i == 1) {
         assertEquals("fail to match a user name.", "lee",user.getUserName());
         assertEquals("fail to match a user password.", "lee123",user.getPassword());
      ...
```
위의 예를 보면 [FROM User user join fetch user.roles role]에서 join fetch 라는 키워드를 쓴 것을 확인할 수 있다. 이것에 의한 생성된 SQL은 다음과 같다.

### Generated SQL
```SQL
SELECT ...
FROM USER user0_ INNER JOIN AUTHORITY roles1_ ON user0_.USER_ID=roles1_.USER_ID 
                 INNER JOIN ROLE role2_ ON roles1_.ROLE_ID=role2_.ROLE_ID 
WHERE role2_.ROLE_NAME=?
```
위에 SQL은 query.getResultList()에 의해서 실행되는 SQL로 JOIN에 관련된 ROLE정보를 모두 추출하는 것을 확인할 수 있다.