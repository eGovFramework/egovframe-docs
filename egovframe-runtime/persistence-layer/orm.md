---
title: ORM 서비스
linkTitle: ORM
description: ORM 서비스는 객체 모델링과 관계형 데이터 모델링의 불일치를 해결하기 위해 JPA와 Hibernate를 사용하며, DBMS 변경 시에도 설정 정보만 수정하면 코드 변경 없이 동작이 가능하다. Lazy Loading과 Cache 활용으로 성능을 향상시키며, Entity Class에 최소한의 Annotation을 사용해 매핑을 정의한다. SQL 처리 방식에 익숙한 개발자는 추가 학습이 필요할 수 있다.
url: /egovframe-runtime/persistence-layer/orm/
menu:
    depth:
        name: "ORM"
        weight: 7
        parent: "persistence-layer"
        identifier: "orm"
---
# ORM 서비스

## 개요
객체 모델링(Object Oriented Modeling)과 관계형 데이터 모델링(Relational Data Modeling) 사이의 불일치를 해결해 주는 OR Mapping 서비스로 자바 표준인 JPA를 표준 서비스로 제시하고 구현체로는 JPA 구현체중에 가장 성능이 우수한 것으로 알려진 Hibernate를 이용하였다. 서비스의 특징을 살펴보면 다음과 같다.
- 특정 DBMS에 영향을 받지 않으므로 DBMS가 변경되더라도 데이터 액세스 처리 코드에 대한 변경없이 설정 정보의 변경만으로도 동작 가능하다.
- SQL을 작성하고 <acronym title="Structured Query Language">SQL</acronym> 실행 결과로부터 전달하고자 하는 객체로 변경하는 코드를 작성하는 시간이 줄어든다. 하지만 필요시 [SQL 작업](orm-native_sql.md)도 가능하다.
- 기본적으로 필요 시점에만 DBMS에 접근하는 Lazy Loading 전략 채택하고 [Cache활용](orm-cache_handling.md)을 통해 DBMS에 대한 접근 횟수를 줄여나가 어플리케이션의 성능 향상을 도모한다.
- 별도의 <acronym title="Extensible Markup Language">XML</acronym> 파일로 매핑을 관리하지 않고 [Entity Class](./orm-entities.md)에 최소한의 Annotation으로 정의하므로써 작업이 용이하다.
- Entity Class가 일반 클래스로 정의됨으로써 상속이나 다양성, 캡슐화 같은 것들을 그대로 적용하면서 퍼시스턴스 오브젝트로 사용할 수 있다.
- 자바 표준이므로 많은 벤더들에서 구현체를 지원하고 개발을 편리하게 할 수 있는 [JPA툴(Dali)](https://projects.eclipse.org/projects/webtools.dali)을 지원한다.
- SQL을 이용하여 처리하는 방식에 익숙한 개발자가 사용하려면 학습이 필요하고 이에 따른 장벽이 존재한다.

## 설명
### 주요 개념

<img src="../images/conceptua_architecture.jpg" align="left"/>

옆의 그림에서 보는것과 같이 DBMS 기반의 어플리케이션 수행을 하기 위해 필요한 주요 구성 요소는 Entity, Persistence.xml 이며, 각각은 다음과 같은 역할을 수행한다.
- [Entity](orm-entities.md): 어플리케이션 실행 여부와 상관없이 물리적으로 존재하는 데이터들을 다룬다. 일반적으로 DBMS 데이터를 이용하는 어플리케이션을 개발할 경우 어플리케이션의 비즈니스 레이어에서 특정 DBMS에 맞는 SQL을 통해 어플리케이션의 데이터를 처리하게 된다. 그러나 JPA 기반의 어플리케이션에서는 Entity를 중심으로 하여 어플리케이션의 데이터와 DBMS 연동이 가능해진다. annotation 기반으로 매핑관련 사항도 Entity 클래스에서 정의할 수 있어서 별도의 파일없이 테이블과의 관계를 표현할 수 있다.
- [Persistence.xml](orm-jpa_configuration.md): 구현체에 대한 선언 및 대상 엔티티 클래스 지정 구현체별 프로퍼티 지정등을 할 수 있는 설정 파일로 JPA를 이용해서 어플리케이션을 구동할 경우 필수적으로 작성을 해야하는 파일이다.
- [JPA(Hibernate)](https://hibernate.org/) : JPA 구현체로의 Hibernate의 요소는 Hibernate Core , Hibernate Annotations , Hibernate EntityManager 로 되어 있으며 JPA 구성에 필요한 Entity Manager등 구현 클래스를 포함하고 있다.
- JPA Tool : JPA 지원툴이 Eclipse Web Tools Platform내에 서브프로젝트로 Dali JPA Tools 가 있다. 이 툴을 활용함으로써 DB에 생성된 테이블로부터 Entity 클래스 생성등 손이 많이 가는 작업을 자동으로 처리할 수 있다. 자세한 정보는 [Dali Homepage](https://projects.eclipse.org/projects/webtools.dali)를 참조한다.

### 시작하기
ORM 서비스에 대한 자세한 설명에 앞서 간단하게 ORM 서비스를 시작하는데 필요한 것에 대한 설명을 하고자 한다.

#### Step1. 사전 준비
##### 필요 **Library**
본 서비스를 활용하기 위해서 필요한 Library 목록과 설명은 아래와 같다.

라이브러리|설명|연관 라이브러리
---|---|---
antlr-2.7.7.jar|파서 라이브러리||
commons-collections-3.2.jar|collection 처리를 위한 라이브러리|
commons-dbcp-1.2.2.jar|DataSource 커넥션 풀 라이브러리|
commons-logging-1.1.1.jar|Logging 처리를 위한 라이브러리|	hibernate-annotations-3.4.0.GA.jar에서 참조
log4j-1.3alpha-8.jar|Logging 처리를 위한 라이브러리|
slf4j-api-1.5.3.jar|Logging 처리를 위한 라이브러리|
slf4j-log4j12-1.5.3.jar|Logging 처리를 위한 라이브러리|	
commons-pool-1.3.jar|pooling 처리를 위한 라이브러리|commons-dbcp-1.2.2.jar에서 참조
dom4j-1.6.1.jar|XML 파싱 라이브러리|hibernate-3.2.4.ga.jar 에서 참조
ejb3-persistence-1.0.2.GA.jar|JPA Interface 클래스 라이브러리|
hibernate-annotations-3.4.0.GA.jar|Hibernate Annotation|
hibernate-entitymanager-3.4.0.GA.jar|Hibernate Entity Manager 구현체 라이브러리|
hibernate-commons-annotations-3.1.0.GA.jar|Hibernate 공통 annotation 라이브러리|hibernate-entitymanager-3.4.0.GA.jar에서 참조|
hibernate-core-3.3.0.SP1.jar|Hiberante Core 라이브러리|hibernate-entitymanager-3.4.0.GA.jar에서 참조
javassist-3.4.GA.jar|자바 bytecode 조작 라이브러리|hibernate-entitymanager-3.4.0.GA.jar에서 참조
jta-1.1.jar|JTA 인터페이스 라이브러리|hibernate-entitymanager-3.4.0.GA.jar에서 참조
hsqldb-1.8.0.10.jar|HSQL JDBC 드라이버|
mysql-connector-java-5.1.6.jar|	MYSQL JDBC 드라이버|
ojdbc-14.jar|ORACLE JDBC 드라이버|
junit-4.4.jar|테스트 지원 라이브러리|	

#### Step2. Entity 클래스 생성
간단한 형태의 Entity 클래스를 생성한다. 네개의 Attribute로 구성되어 있고 각각의 getter,setter 메소드로 구성되어 있다.
##### Entity 클래스
```java
@Entity
public class Department implements Serializable {
 
   private static final long serialVersionUID = 1L;
 
   @Id
   private String deptId;
 
   private String deptName;
 
   private Date createDate;
 
   private BigDecimal empCount;
 
   public String getDeptId() {
      return deptId;
   }
 
   public void setDeptId(String deptId) {
      this.deptId = deptId;
   }	   
   ...
}
```
- @Entity : Department 가 Entity 클래스임을 정의
- @Id : Primary Key 정보 지정

#### Step3. persistence.xml 생성
위에서 정의한 Entity 클래스를 가지고 JPA 수행하기 위한 프로퍼티 파일로 구현체제공 클래스정보,엔티티클래스정보,DB접속 정보,로깅정보,테이블자동생성정보를 포함하고 있다.
```java
<persistence-unit name="PersistUnit" transaction-type="RESOURCE_LOCAL">
 
   <provider>org.hibernate.ejb.HibernatePersistence</provider>
 
   <class>egovframework.Department</class>
   <exclude-unlisted-classes/>
 
   <properties>
      <property name="hibernate.connection.driver_class" value="org.hsqldb.jdbcDriver"/>
      <property name="hibernate.connection.url" value="jdbc:hsqldb:mem:testdb"/>
      <property name="hibernate.connection.username" value="sa"/>
      <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
 
      <property name="hibernate.connection.autocommit" value="false"/>
      <property name="hibernate.show_sql" value="true"/>
      <property name="hibernate.format_sql" value="true"/>
      <property name="hibernate.hbm2ddl.auto" value="create"/>
   </properties>
 
</persistence-unit>
```
- provider : 구현체 클래스 지정
- class : 엔티티 클래스명 정의
- exclude-unlisted-classes : 위에서 지정하지 않은 클래스는 엔티티라고 정의되어 있어도 제외
- hibernate.connection.* : DB 연결정보로 각자 환경에 맞추어 변경 가능
- hibernate.dialect : DBMS별 Hibernate 사용을 위한 클래스 ( 각 DBMS별로 별도로 정의됨 )
- hibernate.connection.autocommit : 자동 커밋여부 설정 false로 했으므로 명시적인 commit 가 필요함
- hibernate.show_sql : 로그에 SQL 포함
- hibernate.format_sql : <acronym title="Structured Query Language">SQL</acronym>을 포맷에 맞추어 출력
- hibernate.hbm2ddl.auto : DDL 자동 생성 , Entity로 정의된 클래스에 대해서 자동으로 테이블 생성함

#### Step4. 테스트 클래스 생성
위에서 정의한 Department를 이용하여 입력,수정,조회,삭제 처리를 하는 것을 JUNIT형태로 구성하였다.
```java
@Test
public void testDepartment() throws Exception {
 
   String modifyName = "Marketing Department";
   String deptId = "DEPT-0001";
   Department department = makeDepartment(deptId);
 
   // Entity Manager 생성
   emf = Persistence.createEntityManagerFactory("PersistUnit");
   em = emf.createEntityManager();	
 
   // 입력
   em.getTransaction().begin();
   em.persist(department);
   em.getTransaction().commit();	
 
   em.getTransaction().begin();
   Department departmentAfterInsert = em.find(Department.class, deptId );
   // 입력 확인
   assertEquals("Department Name Compare!",department.getDeptName(),departmentAfterInsert.getDeptName());
 
   // 수정
   departmentAfterInsert.setDeptName(modifyName);
   em.merge(departmentAfterInsert);
   em.getTransaction().commit();	
 
   em.getTransaction().begin();
   Department departmentAfterUpdate = em.find(Department.class, deptId );
   // 수정 확인
   assertEquals("Department Modify Name Compare!",modifyName,departmentAfterUpdate.getDeptName());
 
   // 삭제
   em.remove(departmentAfterUpdate);
   em.getTransaction().commit();	
 
   // 삭제 확인
   Department departmentAfterDelete = em.find(Department.class, deptId );
   assertNull("Department is Deleted!",departmentAfterDelete);
 
   em.close();
 
}
```
- Persistence.createEntityManagerFactory : Entity Manager Factory 생성하기
- emf.createEntityManager : Entity Manager 생성
- em.getTransaction().begin() : Transaction 시작
- em.getTransaction().commit(): Commit 처리
- em.persist : Insert 처리
- em.find : SELECT 처리
- em.merge : UPDATE 처리
- em.remove : DELETE 처리
- assertEquals : 값이 같은지 비교하는 것 (JUnit 메소드)
- assertNull : NULL 인지 확인하는 것 (JUnit 메소드)

#### Step5. 실행
1. [ormsimpleguide.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:rte:ormsimpleguide.zip) 파일을 다운로드 받아서 압축을 푼다.
2. 이클립스에서 압축 푼 폴더를 선택하여 프로젝트를 Import 한다.
3. 프로젝트내 src 폴더에 Department.java, DepartmentTest.java, resources 폴더에 META-INF/persistence.xml, log4j.xml 가 정상적으로 있는지 확인한다.
4. lib에 라이브러리 파일이 있는지 확인한다.
5. DepartmentTest.java를 선택하여 마우스 오른쪽 클릭하여 Run As > JUnit Test 실행한다.
6. JUnit 결과창에서 정상적으로 수행된 것을 확인한다.
※ ORACLE 이나 MySQL의 경우는 첨부되는 persistence.xml 의 주석을 참고하여 설정하고 수행하면 정상적으로 수행되는 것을 확인할 수 있다.

### 상세 설명
1. [Entities](./orm-entities.md)
1. [Entity Operation](./orm-entity_operation.md)
1. [Association Mapping](./orm-association_mapping.md)
1. [Query Language](./orm-query_language.md)
1. [Native SQL](./orm-native_sql.md)
1. [Concurrency](./orm-concurrency.md)
1. [Cache Handling](./orm-cache_handling.md)
1. [Fetch Strategy](./orm-fetch_strategy./md)
1. [Spring Integration](./orm-spring_integration.md)
1. [JPA Configuration](./orm-jpa_configuration.md)

## 예제
[ORM 예제](../../runtime-example/individual-example/persistence-layer/orm-example.md)