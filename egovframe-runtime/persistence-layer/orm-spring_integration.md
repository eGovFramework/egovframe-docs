---
title: Spring과 JPA 통합
linkTitle: "Spring Integration"
description: Spring은 JPA 기반 DAO 클래스를 쉽게 구현하기 위해 JpaTemplate을 제공하지만, 직접 EntityManager 메서드를 사용하는 방식(plain JPA)도 지원한다. JPA를 사용하기 위해서는 persistence.xml과 Spring ApplicationContext 설정이 필요하다.
url: /egovframe-runtime/persistence-layer/orm/orm-spring_integration/
menu:
    depth:
        name: Spring Integration
        weight: 9
        parent: "orm"
---
# Spring Integration

 Spring에서는 JPA 기반에서 DAO 클래스를 쉽게 구현할 수 있도록 하기 위해 JdbcTemplate,HibernateTemplate등처럼 **JpaTemplate**을 제공한다. 하지만 JPA에 있어서는 Entity Manager의 Method를 직접 이용하는 것(**plain JPA**)에 대한 것도 가이드한다. 이에 두가지 방법에 대한 설정 및 사용방법에 대해서 설명하고자 한다. [Spring JPA](http://static.springframework.org/spring/docs/2.5.x/reference/orm.html#orm-jpa)

## 기본 설정

 Spring 기반하에서 JPA를 쓰고자 할 때 필요한 설정은 persistence.xml과 ApplicationContext 파일 설정이 필요하다.

#### persistence.xml 설정

```xml
<persistence-unit name="HSQLMUnit" transaction-type="RESOURCE_LOCAL"> 
   // 구현체는 Hibernate	
   <provider>org.hibernate.ejb.HibernatePersistence</provider>
 
   // Entity Class List
   <class>egovframework.sample.model.bidirection.User</class>
   <class>egovframework.sample.model.bidirection.Role</class>
   <class>egovframework.sample.model.bidirection.Department</class>
   <exclude-unlisted-classes/>
 
   <properties>
      // DBMS별 다른 설정 여기는 HSQL 설정.
      <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
      <property name="hibernate.show_sql" value="true"/>
      <property name="hibernate.format_sql" value="true"/>
      <property name="hibernate.hbm2ddl.auto" value="create-drop"/>
   </properties>
</persistence-unit>
```

 위에서 Entity Class List와 그에 따르는 &lt;exclude-unlisted-classes/&gt;는 프로젝트내에 있는 엔티티 클래스중에 리스트하는 것만을 엔티티로 인식하도록 설정하는 것이고 dialect설정은 DBMS별 별도 설정이다. 위의 예에서는 HSQL 설정.

#### Application Context 설정

```xml
   // 1.Transation Manager 설정
   <bean id="transactionManager" class="org.springframework.orm.jpa.JpaTransactionManager">
      <property name="entityManagerFactory" ref="entityManagerFactory"/>
   </bean>	
 
   // 2.Entity Manager Factory 설정
   <bean id="entityManagerFactory" class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean">
      <property name="persistenceUnitName" value="HSQLMUnit"/>
      <property name="persistenceXmlLocation" value="classpath:META-INF/persistHSQLMemDB.xml"/>
      <property name="dataSource" ref="dataSource"/>
   </bean>
 
    // 3.DataSource 설정
   <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
      <property name="driverClassName" value="net.sf.log4jdbc.DriverSpy"/>
      <property name="url" value="jdbc:log4jdbc:hsqldb:mem:testdb"/>
      <property name="username" value="sa"/>
      <property name="password" value=""/>
      <property name="defaultAutoCommit" value="false"/>
   </bean>	
 
   // 4.JPA Annotation 사용 설정
   <bean class="org.springframework.orm.jpa.support.PersistenceAnnotationBeanPostProcessor"/>	
 
   // 5.Annotation 사용 설정
   <context:component-scan base-package="egovframework"/>
 
   // 6.Annotation 기반의 Transaction 활성화 설정 
   <tx:annotation-driven />
```

 위의 예를 살펴보면 1.Transation Manager 설정, 2.Entity Manager Factory 설정, 3.DataSource 설정, 4.JPA Annotation 사용 설정, 5.Annotation 사용 설정, 6.Annotation 기반의 Transaction 활성화 설정 으로 구분되어 설정되어 있고 1~4까지가 JPA를 위한 설정이다. 각자 쓰고자 할때 변경이 필요한 부분은 2,3,5 내역으로 2번 항목은 persistence.xml 파일 위치와 persistenceUnitName 설정, 3번 항목은 DBMS연결을 위한 DataSource 설정, 5번 항목은 package 설정이다.

## JpaTemplate 이용

 Spring에서 정의한 JpaDaoSupport를 상속받아 getJpaTemplate()를 통해서 Entity Method 등을 호출 작업할 수 있다.

#### DAO 클래스 Source

```java
public class UserDAO extends JpaDaoSupport {
   // Application Context 에서 설정한 Entity Manager Factory 명을 지정하여 부모의 EntityManagerFactory를 설정한다.
   @Resource(name="entityManagerFactory")
   public void setEMF(EntityManagerFactory entityManagerFactory) {
      super.setEntityManagerFactory(entityManagerFactory);
   }
 
   // getTemplate()에 의한 입력	
   public void createUser(User user) throws Exception {
      this.getJpaTemplate().persist(user);
   }
 
   // getTemplate()에 의한 조회	
   public User findUser(String userId) throws Exception {
      return (User) this.getJpaTemplate().find(User.class, userId);
   }
 
   // getTemplate()에 의한 query .. find method 지원됨	
   public List findUserListAll() throws Exception {
      return this.getJpaTemplate().find("FROM User user ORDER BY user.userName");
   }
 
   // getTemplate()에 의한 삭제	
   public void removeUser(User user) throws Exception {
      this.getJpaTemplate().remove(this.getJpaTemplate().getReference(User.class, user.getUserId()));
   }
 
   // getTemplate()에 의한 수정
   public void updateUser(User user) throws Exception {
      this.getJpaTemplate().merge(user);
   }
}

```

 위의 예를 보면 JpaDaoSupport 를 상속받아서 this.getJpaTemplate().method()를 통해서 기능을 구현하였다.

#### Entity 클래스 Source

```java
@Entity
public class User implements Serializable {
 
   private static final long serialVersionUID = -8077677670915867738L;
 
   @Id
   @Column(name = "USER_ID", length=10)
   private String userId;
 
   @Column(name = "USER_NAME", length=20)
   private String userName;
 
   @Column(length=20)
   private String password;
 
   ...
}
```

 위의 예제는 DAO 클래스에서 쓰인 User Entity Class 소스의 일부이다.

## Plain JPA 이용

 JPA에서 정의한 Entity Manager의 Entity Method를 호출 작업할 수 있다. Entity Manager를 통해 작업함으로써 Spring 환경하에서 Spring에 대한 의존성을 최소화 할 수 있다.

#### DAO 클래스 Source

```java
public class RoleDAO {
   // Application Context 설정의 4.JPA Annotation 사용 설정에 의해서 정의가능한 것으로 Annotation기반으로 Entity Manager를 지정한다.	
   @PersistenceContext
   private EntityManager em;
 
   // EntityManager를 통한 입력	
   public void createRole(Role role) throws Exception {
      em.persist(role);
   }
 
   // EntityManager를 통한 조회
   public Role findRole(String roleId) throws Exception {
      return (Role) em.find(Role.class, roleId);
   }
 
   // EntityManager를 통한 Query
   public List findRoleListAll() throws Exception {
      Query query = em.createQuery("FROM Role role ORDER BY role.roleName");
      return  query.getResultList();		
   }
 
   // EntityManager를 통한 삭제
   public void removeRole(Role role) throws Exception {
      em.remove(em.getReference(Role.class, role.getRoleId()));
   }
 
   // EntityManager를 통한 수정
   public void updateRole(Role role) throws Exception {
      em.merge(role);
   }
}
```

 위의 예를 보면 Entity Manager의 메소드를 통해서 기능을 구현하였다

#### Entity 클래스 Source

```java
@Entity
public class Role implements Serializable {
 
   private static final long serialVersionUID = 1042037005623082102L;
 
   @Id
   @Column(name = "ROLE_ID", length=10)
   private String roleId;
 
   @Column(name = "ROLE_NAME", length=20)
   private String roleName;
 
   @Column(name = "DESC" , length=50)	
   private String desc;	
   ...
}
```

 위의 예제는 DAO 클래스에서 쓰인 Role Entity Class 소스의 일부이다.