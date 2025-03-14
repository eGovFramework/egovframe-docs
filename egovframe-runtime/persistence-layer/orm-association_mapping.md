---
title: Association Mapping
linkTitle: "Association Mapping"
description: "두 클래스 간의 연관 관계를 매핑하는 방법으로, 1:1 관계는 @OneToOne 애노테이션을 사용해 처리하고, 1:N 관계는 @OneToMany와 @ManyToOne 애노테이션을 사용해 매핑한다. 다양한 컬렉션 매핑과 inverse, cascade 같은 주요 속성도 함께 설정할 수 있다."
url: /egovframe-runtime/persistence-layer/orm/orm-associaion_mapping/
menu:
    depth:
        name: Association Mapping
        weight: 3
        parent: "orm"
---
# Association Mapping
두 클래스 사이의 Association 유형별 매핑 방법에 대해서 살펴보고자 한다. 그리고 다양한 Collection의 매핑 방법 및 Collection의 주요속성인 inverse,cascade에 대해서 샘플코드를 중심으로 살펴본다.

## One To One Mapping
테이블간 1:1 매핑이 있을 경우에 각각의 Entity 클래스를 정의하고 클래스간 관계를 OneToOne 매핑으로 처리한다.

##### Sample Source
```java
@Entity
public class Employee {
    @OneToOne
    private TravelProfile profile;
}

@Entity
public class TravelProfile {
    @OneToOne
    private Employee employee;
}
```
위의 예를 보면 Employee 와 TravelProfile가 각각 OneToOne이라는 Annotation을 기재하여 매핑처리한 것을 알수 있다.

## One To Many Mapping
테이블간 1:N 매핑이 있을 경우에 각각의 Entity 클래스를 정의하고 한쪽에는 OneToMany, 다른쪽에는 ManyToOne 이라는 Annotation을 기재하여 관계를 나타낸다.

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @ManyToOne
    private Department department;
}
```
위의 예를 보면 Department:User = 1:N 의 관계가 있으며 그 관계에 대해서 Department 클래스에서 OneToMany로 표시하고 User 클래스에서 ManyToOne으로 표시하여 관계를 나타냈다.

### Collection Type
Collection은 위의 예에서 사용된 Set 이외에도 List,Map를 사용할 수 있는데 각각의 사용법은 다음과 같다

#### Set
java.util.Set 타입으로 \<set>을 이용하여 정의한다. 객체의 저장 순서를 알 수 없으며, 동일 객체의 중복 저장을 허용하지 않는다. (HashSet 이용) 다음은 set 태그를 이용하여 Collection 객체를 정의한 소스 코드의 예이다

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}
```

#### List
java.util.List 타입으로 \<list>를 이용하여 정의한다. List 타입의 경우 저장된 객체의 순서를 알 수 있으며, 저장 순서를 테이블에 보관하기 위해서 별도 인덱스 컬럼 정의가 필요하다. (ArrayList 이용) 다음은 list 태그를 이용하여 Collection 객체를 정의한 소스 코드의 예이다

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class )
    private List<User> users = new ArrayList(0);
}
```

#### Map
java.util.map 타입으로 \<map>을 이용하여 (키,값)을 쌍으로 정의한다. (HashMap 이용) 다음은 map 태그를 이용하여 Collection 객체를 정의한 소스 코드의 예이다. Key 설정을 위해 MapKey라는 Annotation을 추가적으로 정의해야 한다.

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    @MapKey(name="userId")
    private Map<String,User> users ;
}
```

### 단방향/양방향 관계 속성
1:N(부모:자식)관계 지정에 있어서 자식쪽에서 부모에 대한 참조 관계를 가지고 있느냐 없느냐에 따라서 참조관계가 있으면 양방향 관계, 없으면 단방향 관계로 정의된다.

#### 단방향
자식 Entity에 부모 Entity에 대한 참조정보 없이 정의한다.

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @Column(name="DEPT_ID")
    private String deptId;
}
```
위의 예에서 보면 User 클래스에서 Department 클래스에 대한 참조관계를 지정하지 않고 단순하게 테이블의 컬럼 DEPT_ID와의 매핑으로 deptId를 지정한 것을 알 수 있다.

#### 양방향
자식 Entity에 부모 Entity에 대한 참조정보를 지정하여 정의한다.

##### Sample Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @ManyToOne
    private Department department;
}
```
위의 예에서 보면 User 클래스에서 Department 클래스에 대한 ManyToOne Annotation을 통해 매핑관계를 지정한 것을 알 수 있다.

### mappedBy,Cascade 속성
mappedBy와 cascade는 Collection 정의시 중요한 의미를 가지는 속성 중의 하나로, 다음과 같은 의미를 지닌다.

- mappedBy: 객체간 관계 연결을 어느 Entity에서 할 것인지에 대한 옵션을 정의하기 위한 속성이다.
- cascade : 부모 객체에 대한 CUD를 자식 객체에도 전이할지에 대한 옵션을 정의하기 위한 속성이다.
#### mappedBy: ○, cascade: ○
mappedBy와 cascade를 모두 정의하여 사용할 경우에는 자식 Entity에서 관계연결 처리를하고 부모 Entity에서 CUD처리시 자식 Entity도 자동으로 처리된다.

##### Define Source
```java
@Entity
public class Department{
@OneToMany(targetEntity=User.class,mappedBy="deptId",cascade={CascadeType.PERSIST, CascadeType.MERGE})
private Set<User> users = new HashSet(0);
}

@Entity
public class User{
@ManyToOne(targetEntity=Department.class)
private Department department;
}
```

##### Sample Source
```java
// User(자식) Entity의 setDepartment 메소드를 통해서 관계설정
user.setDepartment(department);

// 부모 entity의 저장으로 자식까지 동시처리
em.persist(department);
```

#### mappedBy: ○, cascade: Ⅹ
mappedBy만 정의하여 사용할 경우에는 자식 Entity에서 관계연결 처리를하고 부모,자식 각자 CUD처리한다.

##### Define Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class,mappedBy="deptId")
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @ManyToOne(targetEntity=Department.class)
    private Department department;
}
```

##### Sample Source
```java
// User(자식) Entity의 setDepartment 메소드를 통해서 관계설정
user.setDepartment(department);

// 부모/자식 entity의 각각 처리
em.persist(department);
em.persist(user);
```

#### mappedBy: Ⅹ, cascade: ○
cascade만 정의하여 사용할 경우에는 부모 Entity에서 관계연결 처리를 하고 부모 Entity에서 CUD처리시 자식 Entity도 자동으로 처리된다.

##### Define Source
```java
@Entity
public class Department{
@OneToMany(targetEntity=User.class,cascade={CascadeType.PERSIST, CascadeType.MERGE})
private Set<User> users = new HashSet(0);
}

@Entity
public class User{
@ManyToOne(targetEntity=Department.class)
private Department department;
}
```

##### Sample Source
```java
// Department(부모) Entity의 getUsers().add 메소드를 통해서 관계설정
department.getUsers().add(user);

// 부모 entity의 저장으로 자식까지 동시처리
em.persist(department);
```

#### mappedBy: Ⅹ, cascade: Ⅹ
모두 정의하지 않을때는 부모 Entity에서 관계 연결 처리를 하고 부모,자식 각자 CUD처리한다.

##### Define Source
```java
@Entity
public class Department{
    @OneToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @ManyToOne(targetEntity=Department.class)
    private Department department;
}
```

##### Sample Source
```java
// Department(부모) Entity의 getUsers().add 메소드를 통해서 관계설정
department.getUsers().add(user);

// 부모/자식 entity의 각각 처리
em.persist(department);
em.persist(user);
```

### Many To Many Mapping
테이블간 M:N 매핑이 있을 경우에 각각의 Entity 클래스를 정의하고 양쪽에 ManyToMany이라는 Annotation을 기재하여 관계를 나타낸다.

##### Sample Source
```java
@Entity
public class Role{
    @ManyToMany(targetEntity=User.class)
    private Set<User> users = new HashSet(0);
}

@Entity
public class User{
    @ManyToMany
    @JoinTable(name="AUTHORITY",
        joinColumns=@JoinColumn(name="USER_ID"),
        inverseJoinColumns=@JoinColumn(name="ROLE_ID"))
    private Set<Role> roles = new HashSet(0);
}
```

위의 예를 보면 Role:User = M:N 의 관계가 있으며 그 관계에 대해서 Role클래스에서 ManyToMany로 표시하고 User 클래스에서 ManyToMany로 표시하여 관계를 나타내면서 User 클래스에서 관계를 위한 별도의 테이블에 대한 정의를 하고 있다. 이 경우에 ROLE과 USER를 연결하는 관계 테이블로 AUTHORITY가 사용된 것을 알 수 있다.
