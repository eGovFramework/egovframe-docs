---
title: Concurrency
linkTitle: "Concurrency"
description: 동시에 동일한 데이터에 접근할 때 Optimistic Locking을 지원하며, Pessimistic Locking은 JPA 2.0부터 Hibernate의 Native API를 통해 지원된다.
url: /egovframe-runtime/persistence-layer/orm/orm-concurrency/
menu:
    depth:
        name: Concurrency
        weight: 6
        parent: "orm"
---
# Concurrency
동시에 동일한 데이터에 접근할 때에 데이터에 대한 접근을 제어하기 위해 Optimistic Locking을 지원한다. 한편 Hibernate의 Native API를 통해서는 지원 가능한 Pessimistic Locking 은 JPA2.0 버전에 정의될 예정이다.

## Optimistic Locking
### Without Locking Source
```java
@Test
public void testUpdateUserWithoutOptimisticLocking() throws Exception {
 
   // 1. 테스트를 위한 신규 데이터를 입력
   newTransaction();
   addDepartmentUserAtOnce();
   closeTransaction();
 
   // 2. 동일한 식별자를 이용하여 User 정보를 두번 조회
   newTransaction();
   User fstUser = (User) em.find(User.class,"User1");
   User scdUser = (User) em.find(User.class,"User1");
   closeTransaction();
 
   // 3. Detached 상태에서의 변경처리
   fstUser.setUserName("First : Kim");
 
   // 4. 별도의 트랜잭션으로 변경처리
   newTransaction();
   scdUser.setUserName("Second : Kim");
   closeTransaction();
 
   // 5. 3에서 작업한 내용이 반영되어 변경.
   newTransaction();
   em.merge(fstUser);
   closeTransaction();
}
```
위에서 제시한 로직에 대해 자세히 살펴보자.

1. #1, #2번 코드에 의해 각각 동일한 식별자를 이용하여 같은 데이터 조회
1. 두번째 트랜잭션이 종료된 후, #3번 코드에서는 Detached 상태의 fstUser 객체의 userName 변경
1. 세번째 트랜잭션 내의 #4번 코드에서는 scdUser 객체의 userName 변경, 세번째 트랜잭션 종료시 변경 사항이 DB에 반영
1. 네번째 트랜잭션 내에서 #3번 코드를 통해 변경된 fstUser 객체에 대해 update 수행
1. fstUser에 대한 수정 작업 또한 성공적으로 처리
2. 
결론적으로 보면, userId가 “User1”인 User의 userName은 “First : Kim”이 되어 앞서 scdUser에서 요청했던 수정 작업은 무시된 것이다. 이러한 현상을 Lost Update라고 하며, 이를 해결하기 위한 방법은 3가지가 있다.

1. Last Commit Wins : Optimistic Locking 을 수행하지 않게 되면 기본적으로 수행되는 유형으로 2개의 트랜잭션 모두 성공적으로 commit된다. 그러므로 두번째 commit은 첫번째 commit 내용을 덮어쓸 수 있다. (위의 예의 경우)
1. First Commit Wins : Optimistic Locking을 적용한 유형으로 첫번째 commit만이 성공적으로 이루어지며, 두번째 commit 시에는 Error를 얻게 된다.
1. Merge : 첫번째 commit만이 성공적으로 이루어지며, 두번째 commit 시에는 Error를 얻게 된다. 그러나 First Commit Wins와는 달리 두번째 commit을 위한 작업을 처음부터 다시 하지 않고 개발자의 선택에 의해 선택적으로 변경될 수 있도록 한다. 가장 좋은 전략이나 변경 사항을 merge 할 수 있는 화면이나 방법을 직접 제공해 줄 수 있어야 한다.(추가 구현 필요함)

JPA에서는 Versioning 기반의 Automatic Optimistic Locking을 통해 First Commit Wins 전략을 취할 수 있도록 지원한다. JPA에서 Optimistic Locking을 수행하기 위해서는 해당 테이블에 Version을 추가해야 한다. 그러한 경우 해당 테이블과 매핑된 객체를 로드할 때 Version 정보도 함께 로드되고 객체 수정시 테이블의 현재 값과 비교하여 처리 여부를 결정하게 된다.

### With Optimistic Locking Source
```java
@Test
public void testUpdateDepartmentWithOptimisticLocking() throws Exception {
 
   // 1. 테스트를 위한 신규 데이터를 입력
   newTransaction();
   addDepartmentUserAtOnce();
   closeTransaction();
 
   // 2. Department 정보를 두번 조회
   newTransaction();
   Department fstDepartment = (Department) em.find(Department.class,"Dept1");
   assertEquals("fail to check a version of department.", 0, fstDepartment.getVersion());
   Department scdDepartment = (Department) em.find(Department.class,"Dept1");
   closeTransaction();
 
   // 3. 두번째 조회한 Department 정보에 다른 deptName을 셋팅하여 DB에 반영
   fstDepartment.setDeptName("First : Dept.");
 
   // 4. 첫번째 조회한 Department 정보에 대해 merge() 메소드를 호출
   newTransaction();
   scdDepartment.setDeptName("Second : Dept.");
   closeTransaction();
 
   // 5. 세번째 트랜잭션에서의 수정으로 인해 DEPARTMENT_VERSION이 이미 변경되었기 때문에
   //    StaleObjectStateException 발생이 예상
   newTransaction();
   try {
      em.merge(fstDepartment);
      closeTransaction();
   } catch (Exception e) {
      e.printStackTrace();
      assertTrue("fail to throw StaleObjectStateException.",e instanceof StaleObjectStateException);
   }
}
```
위와같이 다음의 testUpdateDepartmentWithOptimisticLocking() 메소드를 수행하였을 때 첫번째 수정 작업은 성공적으로 이루어지나 두번째 수정 작업에 대해서는 #6번 코드에서처럼 StaleObjectStateException이 throw될 것이다. 이를 위한 entity 클래스의 설정의 일부분은 다음과 같다.

### Entity Class Source
```java
@Entity
@Table(name="DEPARTMENT")
public class Department {
 
   private static final long serialVersionUID = 1L;
 
   @Id
   @Column(name = "DEPT_ID", length = 10)
   private String deptId;
 
   @Version
   @Column(name = "DEPT_VERSION")
   private int version;
...
}
```
위에서 보는 것 같이 DEPT_VERSION이라는 컬럼을 추가하여 버전관리를 하게 함으로써 Optimistic Locking처리를 할 수 있다.

