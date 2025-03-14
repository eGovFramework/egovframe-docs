---
title: 프로그래밍 방식의 Transaction 관리
linkTitle: "Programmatic"
description: 프로그래밍 방식으로 트랜잭션을 관리할 때는 TransactionTemplate을 사용하거나 Transaction Manager를 사용하는 방법이 있다. TransactionTemplate은 콜백 메소드를 정의해 트랜잭션을 처리하는 방법을 제공한다.
url: /egovframe-runtime/persistence-layer/transaction/programmatic/
menu:
    depth:
        name: Programmatic
        weight: 2
        parent: "transaction"
---
# Programmatic Transaction Management

## 개요
프로그램에서 직접 트랜잭션을 관리하고자 할 때 사용할 수 있는 방법에 대해서 설명하고자 한다. TransactionTemplate를 사용하는 방법과 Trnasaction Manager를 사용하는 방법 두가지가 있다.

## 설명
### TransactionTemplate를 사용하는 방법
TransactionTemplate를 정의하고 callback 메소드 정의를 이용하여 Transaction 관리를 할 수 있도록 하는 방법이다.

<b>Configuration</b>

```xml
<bean id="transactionTemplate" class="org.springframework.transaction.support.TransactionTemplate">
    <property name="transactionManager" ref="transactionManager"/>
</bean>
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource"/>
</bean>
```

| PROPERTIES         | 설 명     |
| ------------------ | ------- |
| transactionManager | 트랜잭션매니저 |
| dataSource         | 데이타소스   |

위의 설정에서 transactionTemplate를 정의하고 property로 transactionManager을 정의한다. Templeate를 이용한 샘플은 아래와 같다.

#### Sample Source<

```java
@Test
public void testInsertCommit() throws Exception {
   transactionTemplate.execute(new TransactionCallbackWithoutResult() {
      public void doInTransactionWithoutResult(TransactionStatus status) {
         try {
            Role role = new Role();
            role.setRoleId("ROLE-001");
            role.setRoleName("ROLE-001");
            role.setRoleDesc(new Integer(1000));
            roleService.createRole(role);
         } catch (Exception e) {
            status.setRollbackOnly();
         }
      }
   });		
   Role retRole = roleService.findRole("ROLE-001");		
   assertEquals("roleName Compare OK",retRole.getRoleName(),"ROLE-001");
}
```

위의 예에서 transactionTemplate.execute에 TransactionCallbackWithoutResult를 정의하여 Transaction 관리를 하는 것을 확인할 수 있다.

#### 사용 방법

Transaction Context에 의해 호출될 callback 메소드를 정의하고 이 메소드 내에 비즈니스 로직을 구현해주면 된다. 아래는 사용하는 방법의 예이다

```java
    this.transactionTemplate.execute(new TransactionCallbackWithoutResult() {                
        public void doInTransactionWithoutResult(TransactionStatus status) {                    
            //... biz. logic ...       
        }
    });
 
    this.transactionTemplate.execute(new TransactionCallback() {                
        public Object doInTransaction(TransactionStatus status) {                    
            //... biz. logic ...       
        }
    });
```

callback 메소드 doInTransactionWithoutResult()는 Result 값이 없을 경우에 사용하고, Result 값이 존재하는 경우에는 doInTransaction()으로 사용하도록 한다. 또한, callback 메소드 내에서 입력 인자인 TransactionStatus 객체의 setRollbackOnly() 메소드를 호출함으로써 해당 Transaction을 rollback할 수 있다.

### Trnasaction Manager를 사용하는 방법
Transaction Manager를 직접 이용하는 방법이다.

#### Configuration

```xml
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
   <property name="dataSource" ref="dataSource"/>
</bean>
```

| PROPERTIES | 설 명      |
| ---------- | -------- |
| dataSource | 데이타소스 |

위의 설정에서 transactionManager을 정의한다.

#### Sample Source

```java
@Test
public void testInsertRollback() throws Exception {
 
    int prevCommitCount = roleService.getCommitCount();
    int prevRollbackCount = roleService.getRollbackCount();
 
    DefaultTransactionDefinition txDefinition = new DefaultTransactionDefinition();
    txDefinition.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRED);
    TransactionStatus txStatus = transactionManager.getTransaction(txDefinition);
 
    try {
        Role role = new Role();
        role.setRoleId(Thread.currentThread().getName() + "-roleId");
        role.setRoleName(Thread.currentThread().getName() + "-roleName");
        role.setRoleDesc(new Integer(1000));
        roleService.createRole(role);
        roleService.createRole(role);
        transactionManager.commit(txStatus);		
    } 
    catch (Exception e) {
        transactionManager.rollback(txStatus);
    } finally {
        assertEquals(prevCommitCount, roleService.getCommitCount());
        assertEquals(prevRollbackCount + 2, roleService.getRollbackCount());
    }
}
```

Transaction 서비스를 직접 얻어온 후에 위와 같이 try~catch 구문 내에서 Transaction 서비스를 이용하여, 적절히 begin, commit, rollback을 수행한다. 이 때, TransactionDefinition와 TransactionStatus 객체를 적절히 이용하면 된다.

## 참고자료