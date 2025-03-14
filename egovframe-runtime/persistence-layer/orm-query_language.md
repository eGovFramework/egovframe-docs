---
title: JPA Query Language
linkTitle: "Query Language"
description: JPA는 객체 지향적인 관점에서 DB 유형에 독립적인 쿼리를 정의할 수 있도록 별도의 Query Language(QL)를 제공하며, 주요 유형으로 SELECT 문과 UPDATE/DELETE 문이 있다. SELECT 문은 다양한 절(WHERE, ORDER BY, GROUP BY)과 함께 사용되며, UPDATE/DELETE 문은 WHERE 절과 함께 사용된다.
url: /egovframe-runtime/persistence-layer/orm/orm-query-language/
menu:
    depth:
        name: Query Language
        weight: 4
        parent: "orm"
---
# Query Language
JPA에는 별도의 Query Language를 제공함으로써 객체 지향 관점에서 특정 객체에 대한 조회와 DB 유형에 독립적인 Query 정의를 가능하도록 한다. 구성요소 및 작성 방법은 아래와 같다.

## 구성요소
QL Statement 유형으로는 SELECT 문과 Update and Delete 문 두가지가 있다.

- SELECT문 : SELECT 절 + FROM 절 + WHERE 절(Option) + ORDER BY 절(Option) + GROUP BY 절(Option)
- UPDATE&DELETE문 : UPDATE/DELETE 절 + WHERE 절
각각의 절에 대해서 아래에서 알아보고자 한다.

### SELECT 절
조회 결과값을 구체적으로 명시하고자 할 경우 정의한다.

```SQL
SELECT [object 또는  property], Aggregate Funtions , ...
```

여러 건의 데이터를 조회할 경우 조회 결과값을 List, Map 또는 사용자 정의 Type으로 정의 가능하다. (Default = Object[])

```SQL
SELECT new List(prop1, prop2, …)
```

가능한 Aggregate Funtions

```
COUNT   : Long 으로 리턴
MAX, MIN: 정의된 필드로 리턴
AVG     : Double로 리턴
SUM     : integral type의 경우는 Long, float type의 경우는 Double, BigInteger는 BigInteger, BigDecimal 은 BigDecimal 
```

**QL에서 사용 가능한 주요 Function**

#### String Functions
| 함수명                       | 설명                                      |
| --------------------------- | ------------------------------------------ |
| CONCAT(str1, str2)          | 두개의 문자열을 연결한다.                   |
| SUBSTRING(str, idx, length) | 문자열의 지정한 idx 위치에서 length만큼의 문자열을 얻어낸다. |
| TRIM([type] str)            | 문자열의 앞뒤 공백을 삭제한다. (Type이 BOTH일 경우 앞뒤공백 삭제, Type이 LEADING일 경우 앞 공백 삭제, Type이 TRAILING일 경우 뒤 공백 삭제) |
| LOWER(str)                  | 소문자로 변환한다.                          |
| UPPER(str)                  | 대문자로 변환한다.                          |
| LENGTH(str)                 | 문자열의 전체 길이를 구한다.                 |
| LOCATE(str, s, idx)         | 해당 문자열 str에서 정의된 문자열 s가 포함되어 있는 위치를 구한다. 검색 시작 위치는 idx이다. |

#### Arithmetic Functions
| 함수명                  | 설 명                        |
| ---------------------- | -------------------------- |
| ABS(num)               | 숫자의 절대값을 구한다.              |
| SQRT(num)              | 숫자의 제곱근을 구한다.              |
| MOD(num1,num2)         | num2을 num2로 나눈 나머지값을 구한다.   |
| SIZE(collection value) | Collection의 포함 엔트리 숫자를 구한다. |

#### DateTime Functions
| 함수명             | 설 명              |
| ----------------- | ---------------- |
| CURRENT_DATE      | 현재 날짜를 구한다.      |
| CURRENT_TIME      | 현재 시간을 구한다.      |
| CURRENT_TIMESTAMP | 현재 날짜 및 시간을 구한다. |

### FROM 절
조회 대상 객체를 정의하며, SELECT 절이 생략되었을 경우 FROM 절에 정의된 객체가 전달 대상이 된다.

```SQL
FROM [object] ((AS) alias), …
```

#### JOINS
FROM 절에 JOIN 을 쓸 수 있는데 JOIN의 종류는 다음과 같다.
| JOIN 종류          | 예 제                                                                           | 설 명                                                                                                                    |
| ---------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Inner Joins      | SELECT c FROM Customer c **JOIN** c.orders o WHERE c.status = 1               | 비교 대상 양쪽 모두 존재하는 것 추출(Order를 낸 고객만 추출)                                                                                 |
| Left Outer Joins | SELECT c FROM Customer c **LEFT JOIN** c.orders o WHERE c.status = 1          | 한쪽에만 존재하더라도 추출(Order를 내지않은 고객도 추출)                                                                                     |
| Fetch Joins      | SELECT d FROM Department d LEFT JOIN **FETCH** d.employees WHERE d.deptno = 1 | FETCH문 뒤에 오는 자식리스트도 같이 추출 (Department의 attribute로 가지고 있는 employee 목록 추출, lazy로딩의 경우 Fetch를 하지 않으면 employee정보는 추출되지 않음) |

### WHERE 절(Option)
조회 결과 영역을 보다 상세히 구분하고자 할 경우 정의한다.
```SQL
WHERE [condition], …
```
조건을 나타내는 여러 표현이 있는데 그중에 대표적인 것은 다음과 같다.
 Outer pipes  Cell padding 
No sorting
| 조건                            | 설명                                                          | 예                                         |
| ----------------------------- | ------------------------------------------------------------ | ----------------------------------------- |
| Path Expressions              | entity 클래스의 attribute를 지칭함.                                    | user.roles                                |
| Named Parameters              | 이름을 지정한 파라미터를 지정할 수 있고 setParameter를 통해서 값을 지정함.              | WHERE department.deptName like :condition |
| Positional Parameters         | 위치를 지정한 파라미터를 지정할 수 있고 setParameter를 통해서 값을 지정함.              | WHERE role.roleName = ?1                  |
| Collection Member Expressions | Collection 타입의 Attribute를 ”[NOT] MEMBER [OF]” 라는 표현으로 조건처리함. | user MEMBER OF role.users                 |

그외에도 IN, LIKE, IS NULL, EXISTS, [Function](#string-functions) 등의 표현이 지원된다.

### ORDER BY 절(Option)
조회 결과의 정렬 방법을 정의한다.
```SQL
ORDER BY [condition] (ASC 또는 DESC), …
```

### GROUP BY 절(Option)
조회 결과를 특정 기준으로 그룹핑하고자 할 경우 정의한다
```SQL
GROUP BY [condition], …
[HAVING] [condition]
```
## 기본적인 사용 방법
대표적인 사용 방법을 예제소스 기반으로 설명하고자 한다. 기본적인 CRUD 방법과 Join 방법은 다음과 같다

### 기본 리스트 조회
QL을 통해 하나의 테이블을 대상으로 조회 작업을 수행할 수 있다.

#### Sample Source
```java
   StringBuffer qlBuf = new StringBuffer();
   qlBuf.append("FROM Department department ");
   qlBuf.append("WHERE department.deptName like :condition ");
   qlBuf.append("ORDER BY department.deptName");
 
   Query qlQuery = em.createQuery(qlBuf.toString());
   qlQuery.setParameter("condition", "%%");
 
   List departmentList = qlQuery.getResultList();
```
위와 같이 정의된 QL문을 통해 조회 조건에 맞는 Department 객체의 List가 리턴된다. WHERE절의 조회 조건은 객체명.Attribute명(department.deptName)으로 정의할 수 있으며 ':'을 사용하여 Named Paramenter를 통해 조회 조건을 완성할 수 있다. 조회 조건의 값은 Query의 setParameter() 메소드를 통해 지정해 주고 있다.

### JOIN을 통한 리스트 조회
INNER JOIN 과 LEFT OUTER JOIN 을 수행할 수 있고 그 예는 다음과 같다.

#### INNER JOIN (1)
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT user ");
   qlBuf.append("FROM User user join user.roles role ");
   qlBuf.append("WHERE role.roleName = ?1");
 
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter(1, "Admin");
 
   List userList = query.getResultList();
```
위와 같이 정의된 QL문을 통해 조회 조건에 맞는 Department 객체의 List가 리턴된다. FROM절에서 JOIN을 이용하여 INNER JOIN 처리를 했고 WHERE절의 조회 조건은 객체명.Attribute명(department.deptName)으로 정의할 수 있으며 '?!'를 사용하여 Positional Paramenter를 통해 조회 조건을 완성할 수 있다. 조회 조건의 값은 Query의 setParameter() 메소드를 통해 지정해 주고 있다.

#### INNER JOIN (2)
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT distinct user ");
   qlBuf.append("FROM User user, Department department ");
   qlBuf.append("WHERE user.department.deptId = department.deptId ");
   qlBuf.append("AND department.deptId = :condition1 ");
   qlBuf.append("AND user.userName like :condition2 ");
 
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter("condition1", "Dept1");
   query.setParameter("condition2", "%%");
 
   List userList = query.getResultList();
```
위와 같이 정의된 QL문을 통해 조회 조건에 맞는 Department 객체의 List가 리턴된다. WHERE절에서 '='를 통해 INNER JOIN 처리를 했고 조회 조건은 객체명.Attribute명(department.deptName)으로 정의할 수 있으며 '?!'를 사용하여 Positional Paramenter를 통해 조회 조건을 완성할 수 있다. 조회 조건의 값은 Query의 setParameter() 메소드를 통해 지정해 주고 있다.

#### LEFT OUTER JOIN
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT distinct role ");
   qlBuf.append("FROM Role role left outer join role.users user ");
   qlBuf.append("ORDER BY role.roleName ASC ");
 
   Query query = em.createQuery(qlBuf.toString());
 
   List roleList = query.getResultList();
```
위와 같이 정의된 QL문을 통해 조회 조건에 맞는 role객체의 List가 리턴된다. FROM절에서 LEFT OUTER JOIN 처리를 했다. LEFT OUTER JOIN이므로 RIGHT에 있는 정보가 누락되더라도 추출되므로 위의 예에서는 USER 정보가 없는 ROLE 정보도 모두 리스트 됨을 알 수 있다.

## Defined Return Type
조회 작업을 수행한 후, 조회 작업의 결과를 원하는 객체 형태로 전달받을 수 있다. 이는 여러 테이블을 Join할 경우 한 테이블에 매핑되는 Persistence 클래스가 아닌 composite 클래스로 리턴받고자 할 때 사용할 수 있다.

### 특정 객체 형태로 전달
Relation 관계에 놓여 있는 두개의 테이블을 대상으로 QL(Inner Join)을 이용한 조회 결과를 특정 객체(예에선 User객체)형태로 전달받는다
```java
   StringBuffer qlBuf = new StringBuffer();
   qlBuf.append("SELECT new User(user.userId as userId, ");
   qlBuf.append("	user.userName as userName, user.password as password, ");
   qlBuf.append("	role.roleName as roleName, ");
   qlBuf.append("	user.department.deptName as deptName) ");
   qlBuf.append("FROM User user join user.roles role ");
   qlBuf.append("WHERE role.roleName = :condition");
 
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter("condition", "Admin");
 
   List userList = query.getResultList();
```
한가지 주의할 점은 new User(…)를 통해서 생성자를 호출하고 있는데 이 생성자가 User 클래스에 정의되어 있어야 한다. 또한 리턴된 결과값에서 각각의 attribute에 해당하는 값을 꺼낼 때에는 List에서 각 User 객체를 꺼낸 다음 getter 메소드를 사용한다.
```SQL
   User user1 = (User) userList.get(0);
   user1.getUserName());
   User user2 = (User) userList.get(1);
   user2.getUserName());
```

### Map 형태로 전달
Relation 관계에 놓여 있는 두개의 테이블을 대상으로 QL(Inner Join)을 이용한 조회 결과를 Map 형태로 전달받는다
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT new Map(user.userId as userId, ");
   qlBuf.append("	user.userName as userName, user.password as password, ");
   qlBuf.append("	role.roleName as roleName, ");
   qlBuf.append("	user.department.deptName as deptName) ");
   qlBuf.append("FROM User user join user.roles role ");
   qlBuf.append("WHERE role.roleName = :condition");
 
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter("condition", "Admin");
 
   List userList = query.getResultList();
```
위와 같이 정의할 경우 조회 결과는 Map의 List 형태가 된다. 이때 alias로 정의한 userId, userName, password, roleName, deptName이 Map의 Key 값이 된다. 따라서 다음과 같이 Map으로 정의된 Key 값을 통해 결과값을 조회할 수 있다.
```java
   List userList = query.getResultList();
 
   Map user1 = (Map) userList.get(0);
   user1.get("userId");
   user1.get("userName");
   ...
```
### List 형태로 전달
Relation 관계에 놓여 있는 두개의 테이블을 대상으로 QL(Inner Join)을 이용한 조회 결과를 List 형태로 전달받는다
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("SELECT new List(user.userId as userId, ");
   qlBuf.append("	user.userName as userName, user.password as password, ");
   qlBuf.append("	role.roleName as roleName, ");
   qlBuf.append("	user.department.deptName as deptName) ");
   qlBuf.append("FROM User user join user.roles role ");
   qlBuf.append("WHERE role.roleName = :condition");
 
   Query query = em.createQuery(qlBuf.toString());
   query.setParameter("condition", "Admin");
 
   List userList = query.getResultList();
```
위와 같이 정의할 경우 조회 결과는 List의 List 형태가 된다. List에서 결과값을 꺼낼 때에는 정의된 순서에 따르면 된다.
```java
   List userList = query.getResultList();
 
   List user1 = (List) userList.get(0);
   user1.get(1); //userId
   user1.get(2); //userName
   ...
```

## Named Query
Entity 클래스 파일 내에 Annotation으로 정의한 QL문의 name을 입력하여 실행시킬 수 있다.

### Sample Source
```java
   Query qlQuery = em.createNamedQuery("findDeptList");
   qlQuery.setParameter("condition", "%%");
 
   List deptList = qlQuery.getResultList();
```
위와 같이 createNamedQuery() 메소드에 query name을 넘겨주면 이 이름에 맞는 QL문을 찾아서 실행하게 된다. 다음은 findDeptList가 담겨있는 Department Entity 클래스 소스 일부이다.

### Entity Source
```java
@Entity
@NamedQuery(name = "findDeptList", 
           query = "FROM Department department WHERE department.deptName like :condition ORDER BY department.deptName")
public class Department implements Serializable {
...
}
```

## Paging 처리
Paging 처리는 한 페이지에 보여줘야 할 조회 목록에 제한을 둠으로써 DB 또는 어플리케이션 메모리의 부하를 감소시키고자 하는데 목적이 있다. QL 수행시 페이징 처리된 조회 결과를 얻기 위한 방법에 대해 알아보도록 한다. 특정 테이블을 대상으로(예에서는 USER 테이블) QL을 이용한 조회 작업을 수행한다. 이때, 조회를 시작해야 하는 Row의 Number(FirstResult)와 조회 목록의 개수(MaxResult)를 정의함으로써, 페이징 처리가 가능해진다.

### Sample Source
```java
   StringBuffer qlBuf = new StringBuffer();
 
   qlBuf.append("FROM User user ");
   Query query = em.createQuery(qlBuf.toString());
   //첫번째로 조회해야 할 항목의 번호
   query.setFirstResult(1);
   //조회 항목의 전체 개수
   query.setMaxResults(2);
 
   List userList = query.getResultList();
```
위와 같이 정의할 경우 QL에서는 persistence.xml 파일에 정의된 hibernate.dialect 속성에 따라 각각의 DB에 맞는 SQL을 생성한다. 이는 Pagination을 할 때 모든 데이터를 읽은 후 해당 페이지에 속한 데이터 갯수를 결과값으로 전달하는 것이 아니라 조회해야 할 데이터 즉, 해당 페이지에 속한 갯수만큼의 데이터만 읽어오게 된다.

## QL을 이용한 CUD
기본적으로 JPA를 이용한 CUD(Create, Update, Delete)를 할 때에는 기본 API를 사용하게 된다. (본메뉴얼 [Basic CRUD](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:psl:orm:basic_crud) 참고) 그러나 특이한 경우 QL을 통해 기본 CUD를 수행해야 하는 경우가 발생할 수 있다.

### INSERT
다음은 QL을 사용한 Insert문의 예이다.
```java
   StringBuffer ql = new StringBuffer();
 
   ql.append("INSERT INTO Department (deptId,deptName) ");
   ql.append("SELECT CONCAT(deptId,'UPD'), CONCAT(deptName,'UPD') ");
   ql.append("FROM Department department ");
   ql.append("WHERE deptId = :deptId");
 
   Query query = em.createQuery(ql.toString());
   query.setParameter("deptId", "Dept1");
 
   query.executeUpdate();
```
위와 같이 작성할 경우 QL을 이용하여 신규 Department 정보를 등록할 수 있다.

### UPDATE
다음은 QL을 사용한 Update문의 예이다.
```java
   StringBuffer ql = new StringBuffer();
 
   ql.append("UPDATE Department department ");
   ql.append("SET department.desc = :desc ");
   ql.append("WHERE department.deptId = :deptId and department.deptName = :deptName ");
 
   Query query = em.createQuery(ql.toString());
   query.setParameter("desc", "Human Resource");
   query.setParameter("deptId", "Dept1");
   query.setParameter("deptName", "HRD");
 
   query.executeUpdate();
```
위의 예는 QL을 사용하여 Department 정보를 수정한 것이며 Query의 setParameter() 메소드를 통해 인자값을 세팅하고 있다.

### DELETE
다음은 QL을 사용한 Delete문의 예이다.
```java
   StringBuffer ql = new StringBuffer();
   ql.append("DELETE Department department ");
   ql.append("WHERE department.deptId = :deptId ");
 
   Query query = em.createQuery(ql.toString());
   query.setParameter("deptId", "Dept1");
 
   query.executeUpdate();
```
위의 예는 QL을 사용하여 Department 정보를 삭제한 것이며 Query의 setParameter() 메소드를 통해 인자값을 세팅하고 있다.

