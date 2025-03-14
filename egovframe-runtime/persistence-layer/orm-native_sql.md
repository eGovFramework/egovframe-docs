---
title: Native SQL
linkTitle: "Native SQL"
description: JPA는 기본 API나 QL 외에도 특정 DBMS 기능을 활용하기 위해 createNativeQuery() 메소드를 통해 Native SQL 실행을 지원한다. 이를 통해 표준 SQL을 직접 사용하여 CRUD 작업을 수행할 수 있다.
url: /egovframe-runtime/persistence-layer/orm/orm-native_sql/
menu:
    depth:
        name: Native SQL
        weight: 5
        parent: "orm"
---
# Native SQL
기본적으로 CRUD 작업을 할 때 JPA 기본 API를 사용하거나 QL을 이용하여 수행한다. 그러나 특정 DBMS에서 제공하는 기능을 사용할 수 있도록 하기 위해 Native <Acronym title="Structured Query Language">SQL</Acronym> 사용을 지원한다.

## 기본적인 사용 방법
entityManager.createNativeQuery() 메소드를 이용하여 Native SQL을 실행할 수 있다.

### 기본 리스트 조회
SQL을 통해 하나의 테이블을 대상으로 조회 작업을 수행할 수 있다.

#### Sample Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT * ");
   qlBuf.append("FROM DEPARTMENT ");
   qlBuf.append("WHERE DEPT_NAME like :condition ");
   qlBuf.append("ORDER BY DEPT_NAME");
 
   Query query = em.createNativeQuery(qlBuf.toString(),Department.class);
   query.setParameter("condition", "%%");
 
   List deptList = query.getResultList();
```
위와 같이 정의된 SQL문을 통해 조회 조건에 맞는 Department 객체의 List가 리턴된다. WHERE절에서 ':'을 사용하여 Named Paramenter를 통해 조회 조건을 완성할 수 있다. 조회 조건의 값은 Query의 setParameter() 메소드를 통해 지정해 주고 있다. 또한, createNativeQuery의 두번재 인자로 리턴받고자하는 Entity 클래스(Department.class)를 지정한 것을 확인할 수 있다.

### JOIN을 통한 리스트 조회
Relation 관계에 놓여 있는 두개의 테이블을 대상으로 Native <Acronym title="Structured Query Language">SQL</Acronym>(Inner Join)을 이용한 조회 작업을 수행할 수 있다.

#### Basic Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT user.* ");
   qlBuf.append("FROM USER user ");
   qlBuf.append("join AUTHORITY auth on user.USER_ID = auth.USER_ID ");
   qlBuf.append("join ROLE role on auth.ROLE_ID = role.ROLE_ID ");
   qlBuf.append("WHERE role.ROLE_NAME = ?");
 
   Query query = em.createNativeQuery(qlBuf.toString(),User.class);
   query.setParameter(1, "Admin");
 
   List userList = query.getResultList();
```
위의 코드와 같이 join 키워드를 사용하여 Inner Join을 수행할 수 있다. 또한, Relation 관계에 놓여 있는 두개의 테이블을 대상으로 Native <Acronym title="Structured Query Language">SQL</Acronym>(Right Outer Join)을 이용한 조회 작업을 수행할 수 있다.

#### RIGHT JOIN Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT distinct role.* ");
   qlBuf.append("FROM USER user ");
   qlBuf.append("right join AUTHORITY auth on user.USER_ID=auth.USER_ID ");
   qlBuf.append("right join ROLE role on auth.ROLE_ID=role.ROLE_ID ");
   qlBuf.append("ORDER BY role.ROLE_NAME ASC ");
 
   Query query = em.createNativeQuery(qlBuf.toString(),Role.class);
 
   List roleList = query.getResultList();
```
또한 Join하여 조회한 결과를 각각의 Join된 객체의 값으로 select 하기 위해서는 createNativeQuery의 두번째 인자에 @SqlResultSetMapping에 정의된 명을 기재하여 수행한다.

#### Multi Entity Result Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT distinct user.*, department.* ");
   qlBuf.append("FROM USER user, DEPARTMENT department ");
   qlBuf.append("WHERE user.DEPT_ID = department.DEPT_ID ");
   qlBuf.append("AND department.DEPT_NAME = :condition1 ");
   qlBuf.append("AND user.USER_NAME like :condition2 ");
 
   Query query = em.createNativeQuery(qlBuf.toString(), "UserAndDept" ) ;		
   query.setParameter("condition1", "HRD");
   query.setParameter("condition2", "%%");
 
   List userList = query.getResultList();
```
위의 예를 보면 User Entity Class에 UserAndDept 라는 이름으로 리턴받고자 하는 Entity 클래스를 정의하고 있음을 알 수 있다.

#### SqlResultSetMapping Define Source
```java
@SqlResultSetMapping(name="UserAndDept",entities={@EntityResult(entityClass=User.class),
		                                  @EntityResult(entityClass=Department.class)
		                                 }
                    )
@Entity
public class User implements Serializable {
}
```
위의 예를 보면 User Entity 클래스에서 Annotation을 통해서 UserAndDept를 정의하고 있음을 알 수 있다. 또한, 각각의 추출은 아래와 같이 한다.

#### Multi Entity Result Use Source
```java
   Object[] results = (Object[]) userList.get(0);
 
   User user1 = (User)results[0];
   Department dept1 = (Department)results[1];
```

## Named Query
Entity 클래스 파일 내에 Annotation으로 정의한 SQL문의 name을 입력하여 실행시킬 수 있다.

#### Sample Source
```java
   Query query = em.createNamedQuery("nativeFindDeptList");
   query.setParameter("condition", "%%");
 
   List deptList = query.getResultList();
```
위와 같이 createNamedQuery() 메소드에 query name을 넘겨주면 이 이름에 맞는 QL문을 찾아서 실행하게 된다. 다음은 nativeFindDeptList가 담겨있는 Department Entity 클래스 소스 일부이다.

#### Entity Source
```java
@Entity
@NamedNativeQuery(name="nativeFindDeptList",
           resultClass=Department.class,
	         query="SELECT * FROM DEPARTMENT department " +
		       "WHERE department.DEPT_Name like :condition "+
		       "ORDER BY department.DEPT_Name" )
public class Department implements Serializable {
...
}
```
위에서 볼 수 있듯이 QL의 NamedQuery과는 resultClass 를 명시적으로 기재한다는 점에서 차이가 있다.

## Paging 처리
Paging 처리는 한 페이지에 보여줘야 할 조회 목록에 제한을 둠으로써 DB 또는 어플리케이션 메모리의 부하를 감소시키고자 하는데 목적이 있다. Native <Acronym title="Structured Query Language">SQL</Acronym> 수행시 페이징 처리된 조회 결과를 얻기 위한 방법에 대해 알아보도록 한다. 특정 테이블을 대상으로(예에서는 USER 테이블) Native SQL을 이용한 조회 작업을 수행한다. 이때, 조회를 시작해야 하는 Row의 Number(FirstResult)와 조회 목록의 개수(MaxResult)를 정의함으로써, 페이징 처리가 가능해진다.

#### Sample Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT * ");
   qlBuf.append("FROM User ");
   Query query = em.createNativeQuery(qlBuf.toString(),User.class);
 
   query.setFirstResult(1);
   query.setMaxResults(2);
 
   List userList = query.getResultList();
```
위와 같이 정의할 경우 QL에서는 persistence.xml 파일에 정의된 hibernate.dialect 속성에 따라 각각의 DB에 맞는 SQL을 생성한다. 이는 Pagination을 할 때 모든 데이터를 읽은 후 해당 페이지에 속한 데이터 갯수를 결과값으로 전달하는 것이 아니라 조회해야 할 데이터 즉, 해당 페이지에 속한 갯수만큼의 데이터만 읽어오게 된다.

## Function 호출
해당 DB에 생성한 Function을 이용하여 Native SQL을 실행하고 결과를 확인할 수 있다.

#### Sample Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT * FROM USER_TBL ");
   qlBuf.append("WHERE salary > FIND_USER(:condition)");
 
   Query query = em.createNativeQuery(qlBuf.toString(),User.class);
   query.setParameter("condition", "User1");
 
   List userList = query.getResultList();
```
위의 예에서 보면 FIND_USER라는 함수를 호출하여 WHERE문에서 비교를 수행하는 것을 알 수 있다. Procedure의 경우는 입력/출력 인자 처리를 어찌 해야하는지에 대한 확인이 불가능해서 예제로 설명하지 못했다.

