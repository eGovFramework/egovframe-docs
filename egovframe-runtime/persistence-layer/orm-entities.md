---
title: Entities
linkTitle: "Entities"
description: ORM 서비스를 구성하는 가장 기초적인 클래스로 어플리케이션에서 다루고자 하는 테이블에 대응하여 구성할 수 있으며 테이블이 포함하는 컬럼에 대응한 속성들을 가지고 있다.
url: /egovframe-runtime/persistence-layer/orm/orm-entities/
menu:
    depth:
        name: Entities
        weight: 1
        parent: "orm"
---
# Entities
ORM 서비스를 구성하는 가장 기초적인 클래스로 어플리케이션에서 다루고자 하는 테이블에 대응하여 구성할 수 있으며 테이블이 포함하는 컬럼에 대응한 속성들을 가지고 있다.

## 기본 필요 요건
Entity를 구성하기 위한 아래와 같은 요건이 있다.(JPA요건)

### [필수] Entity annotation 선언 필요 ( 혹은 XML 설정파일에 정의 )
```java
@Entity
public class User {
}
```

### [필수] Argument 없는 생성자 필요
```java
public User(){
}
```

### [필수] 최상위레벨 클래스로 생성되어야 하고 enum,interface로 정의될 수 없음

### [필수] final 클래스로 선언될 수 없음

### [필수] Primary Key 있어야 함 : @Id라는 Annotation 표기
```java
@Id
private String userId;
```

### [권장] Serializable 인터페이스 구현
```java
public class User implements Serializable {
   private static final long serialVersionUID = -8077677670915867738L;
}
```

### [권장] 속성 정보 접근을 위한 getter, setter 정의
```java
private String userName;
 
public String getUserName() {
    return userName;
}

public void setUserName(String userName) {
    this.userName = userName;
}
```

## 주요 Annotations
Entity를 구성하는 주요한 Annotation은 다음과 같다.

### @Entity
해당 클래스가 Entity 클래스임을 표시하는 것으로 클래스 선언문 위에 기재한다. 테이블명과 Entity명이 다를 때에는 name에 해당 테이블명을 기재한다
```java
@Entity(name="USER_TB")
public class User {
}
```
### @Id
해당 Attribute가 Key임을 표시하는 것으로 Attribute 위에 기재한다.
```java
@Id
private String userId;
```

### @Column
해당 Attribute와 매핑되는 컬럼정보를 입력하기 위한 것으로 Attribue위에 기재한다. 컬럼명과 Attribute명이 일치할 경우는 기재하지 않아도 됨
```java
@Column(name = "DEPT_NAME", length = 30)
private String deptName;
```
### @OneToOne, @OneToMany, @ManyToOne, @ManyToMany
테이블간 관계를 구성하기 위한 것으로 정의되는 Attribute위에 기재한다. 각각은 1:1,1:N,N:1,N;N의 관계를 표현함. 이에 대한 자세한 설명은 [association_mapping](./orm-association_mapping.md) 참고
```java
@ManyToMany
private Set<Role> roles = new HashSet(0);
```
### @Transient
테이블의 컬럼과 매핑되지 않고 쓰이는 Attribute를 정의하고자 할때 Attribute위에 기재한다.
```java
@Transient
private String roleName;
```

## Entity Status
- New(transient) : 단순히 Entity 객체가 초기화되어 있는 상태를 말한다.
- Managed(persistent) : Entity Manager에 의해 Entity가 관리되는 상태를 말한다.
- Detached : Entity 객체가 더 이상 Persistance Context와 연관이 없는 상태이다.
- Removed : Managed 되어 있는 Entity 객체가 삭제된 상태이다.