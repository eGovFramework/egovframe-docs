---
title: Entity Operation
linkTitle: "Entity Operation"
description: ORM서비스를 이용하여 특정 DB에 데이터를 입력, 수정, 조회, 삭제, 배치입력하는 방법에 대해 알아보도록 한다.
url: /egovframe-runtime/persistence-layer/orm/orm-entity_operation/
menu:
    depth:
        name: Entity Operation
        weight: 2
        parent: "orm"
---
# Entity Operation
ORM서비스를 이용하여 특정 DB에 데이터를 입력, 수정, 조회, 삭제, 배치입력하는 방법에 대해 알아보도록 한다.

## 입력
EntityManager의 persist()메소드를 호출하여 DB에 단건의 데이터를 추가할 수 있다. persist() 메소드 호출시 대상이 되는 Entity를 입력 인자로 전달해야 한다.

### Sample Source
```java
private Department addDepartment() throws Exception {
   // 1. insert a new Department information
   Department department = new Department();
   String DepartmentId = "DEPT-0001";
   department.setDeptId(DepartmentId);
   department.setDeptName("SaleDept");
   department.setDesc("판매부서");
 
   em.persist(department);
   ...
   return department;
}
```
위의 예를 보면 EntityManager의 persist() 메소드에 department라는 Entity를 입력인자로 전달하여 처리하였다.

## 수정
수정을 하고자 할때는 두가지 방법으로 가능한데 우선 EntityManager의 merge()메소드를 호출하여 DB에 단건의 데이터를 수정할 수 있고, 특정 객체가 Persistent 상태이고, 동일한 트랜잭션 내에서 해당 객체의 속성 값에 변경이 발생한 경우 merge() 메소드를 직접적으로 호출하지 않아도 트랜잭션 종료 시점에 변경 여부가 체크되어 변경 사항이 DB에 반영된다.

### merge 호출 Sample Source
```java
public void testUpdateDepartment() throws Exception {
   // 1. insert a new Department information
   Department department = addDepartment();
 
   // 2. update a Department information
   department.setDeptName("Purchase Dept");
 
   // 3. 명시적인 메소드 호출
   em.merge(department);
}
```
위의 예를 보면 EntityManager의 merge() 메소드에 department라는 Entity를 입력인자로 전달하여 처리하였다.

### merge 호출없는 Sample Source
```java
public void testUpdateDepartment() throws Exception {
   // 1. insert a new Department information
   Department department = addDepartment();
 
   // 2. update a Department information
   department.setDeptName("Purchase Dept");
 
   // commit. successful update!!!
}
```
위의 예를 보면 setDeptName()을 통해서 변경하고 Commit 처리시 변경된다.

## 조회
EntityManager의 find()메소드를 호출하여 DB에서 원하는 한건의 데이터를 조회할 수 있다. find() 메소드 호출시 대상이 되는 Entity의 Id를 입력 인자로 전달해야 한다.

### Sample Source
```java
private void assertDepartmentInfo(String departmentId, Department department)
              throws Exception {
 
   Department result = (Department) em.find(Department.class, departmentId);
 
   //...
}
```
위의 예를 보면 EntityManager의 find() 메소드에 departmentId라는 Entity Id를 입력인자로 전달하여 처리하였다.

## 삭제
EntityManager의 remove()메소드를 호출하여 DB에서 원하는 한건의 데이터를 조회할 수 있다. remove() 메소드 호출시 대상이 되는 Entity를 입력 인자로 전달해야 한다.

### Sample Source
```java
public void testDeleteDepartment() throws Exception {
 
   // 1. insert a new Department information
   Department department = addDepartment();
 
   // 2. delete a Department information
   em.remove(department);
 
}
```
위의 예를 보면 EntityManager의 remove() 메소드에 department라는 Entity를 입력인자로 전달하여 처리하였다. 그러나 주의할 점은 위의 예에서는 department 객체는 DB에 등록처리한 객체와 동일 객체이기에 그대로 remove를 쓸 수 있지만 키만 동일하게 신규로 객체를 만든경우에는 remove를 바로 쓸수 없다. 그럴 경우에는 아래와 같은 방법으로 처리해야 한다.

### Sample Source
```java
public void testDeleteDepartment() throws Exception {
 
   Department department = new Department();
   department.setDeptId = "DEPT_1";
 
   // 2. delete a Department information
   em.remove(em.getReference(Department.class, department.getDeptId()));
 
}
```
위의 예에서는 getReference 메소드를 호출하여 Entity의 Id에 해당하는 객체 정보를 추출하여 그정보를 입력인자로 해서 remove를 호출하였다.

## 배치입력
EntityManager의 persist()메소드를 호출하여 DB에 입력하고 loop를 통해 반복적으로 수행한다. OutOfMemoryException 방지를 위해서 일정한 term을 두고 flush(),clear()을 호출하여 메모리에 있는 사항을 삭제한다.

### Sample Source
```java
public void testMultiSave() throws Exception {
 
   for (int i = 0; i < 900 ; i++) {
 
      Department department = new Department();
      String DeptId = "DEPT-000" + i;
      department.setDeptId(DeptId);
      department.setDeptName("Sale" + i);
      department.setDesc("판매부" + i);
 
      em.persist(department);
      logger.debug("=== DEPT-000"+i+" ===");
 
      // OutOfMemoryException 피하기 위해서
      if (i != 0 && i % 9 == 0) {
         em.flush();
         em.clear();
     }
  }
}
```

## Callback Methods
엔티티 클래스에 정의하거나 EntityListener를 지정하여 콜백함수를 정의하여 실제 엔티티 Operation 직전 직후에 비지니스 로직 체크등의 로직을 별도 분리하여 처리하도록 지원한다.

### Callback Methods
| 메소드명        | 설 명              | 관련 Operation                                                                                                                                                          |
| ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PrePersist  | Persist이전 시점에 수행 | [persist](#입력) |
| PostPersist | Persist이후 시점에 수행 | [persist](#입력) |
| PreRemove   | Remove이전 시점에 수행  | [remove](#삭제)  |
| PostRemove  | Remove이후 시점에 수행  | [remove](#삭제)  |
| PreUpdate   | Update이전 시점에 수행  | [merge](#수정)   |
| PostUpdate  | Update이후 시점에 수행  | [merge](#수정)   |
| PostLoad    | Find 이후 시점에 수행   | [find](#조회)    |

### Entity에 직접 정의
콜백 함수를 Entity 클래스에 직접 Annotation을 기재하여 Method를 정의할 수 있다.

#### Define Source - Entity 클래스에 정의
```java
@Entity
public class User {
   @PrePersist
   @PreUpdate
   protected void validateCreate() throws Exception {
      if (getSalary() < 2000000 )
         throw new Exception("Insufficient Salary !");
   }
}
```
위의 예를 보면 Persist, Update 이전 시점에 Salary가 2,000,000 이하가 되는지 여부를 체크를 하도록 한다. Update의 경우는 EntityManager의 merge()를 이용하여 하는 것과 ql을 이용하여 Update 수행하는 것 모두에 해당한다.

#### Sample Source - merge() 이용 케이스
```java
@Test
public void testUpdateFailUser() throws Exception {
 
   newTransaction(); 
 
   User getUser = (User) em.find(User.class, "User1");
   assertEquals(getUser.getSalary(), sal );
   user.setSalary(1000000);
 
   em.merge(user);
 
   // 2. Update User , 위의 merge() 호출이 아닌 Transaction 종료시 Update수행됨. 
   try{
      closeTransaction();
   }
      catch( Exception e ){
      e.printStackTrace();
      assertTrue("fail to PreUpdate.",e instanceof Exception);
   }
}
```
위의 예를 보면 salary가 2000000 이하로 설정되어 Update될 경우 Exception 이 발생하는 것을 알 수 있다.

#### Sample Source - ql을 통한 Update 케이스
```java
@Test
public void testUpdateFail2User() throws Exception {
 
   newTransaction(); 
 
   User getUser = (User) em.find(User.class, "User1");
 
   StringBuffer ql = new StringBuffer();
   ql.append("UPDATE User user ");
   ql.append("SET user.salary = :salary ");
   ql.append("WHERE user.userId = :userId ");
 
   Query query = em.createQuery(ql.toString());
   query.setParameter("salary", 1000000);
   query.setParameter("userId",getUser.getUserId());
 
   // 2. Update User , 위의 merge() 호출이 아닌 Transaction 종료시 Update수행됨. 
   try{
      closeTransaction();
   }
      catch( Exception e ){
      e.printStackTrace();
      assertTrue("fail to PreUpdate.",e instanceof Exception);
   }
}
```
위의 예를 보면 salary가 2000000 이하로 설정되어 Update될 경우 Exception 이 발생하는 것을 알 수 있다. ql를 이용한 Update를 처리할 때도 동일하게 Exception이 발생함을 확인할 수 있다.

### EntityListener 정의
엔티티 클래스에 EntityListener를 지정하고 EntityListener에서 Annotation을 기재하여 Method를 정의할 수 있다.

#### Define Source - EntityListener 클래스에 정의
```java
@Entity
@EntityListeners(egovframework.sample.model.callback.AlertMonitor.class)
public class User {
}
 
//위에서 정의한 AlertMonitor 클래스
public class AlertMonitor {	
   @PostPersist
   public void newUserAlert(User user) {
      System.out.println(user.getUserName()+" Created!");
   }
 
   @PostLoad
   public void usrGetAlert(User user) {
      System.out.println(user.getUserName()+" Get!");
   }
}
```
정의하는 위치가 다르고 원래 엔티티를 매개변수로 넘겨야 하는 부분이 차이가 있지만 엔티티 클래스에 지정하는 것과 동일하게 작동한다.