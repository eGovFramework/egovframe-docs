---
title: 선언적 Transaction 관리
linkTitle: "Declarative"
description: Spring에서는 트랜잭션을 코드에서 직접 처리하지 않고, 애노테이션이나 XML 정의를 통해 선언적으로 관리할 수 있다. 애노테이션 기반 트랜잭션 관리는 설정과 사용법을 통해 간편하게 트랜잭션을 처리할 수 있다.
url: /egovframe-runtime/persistence-layer/transaction/declarative/
menu:
    depth:
        name: Declarative
        weight: 1
        parent: "transaction"
---
# Declarative Transaction Management

## 개요
코드에서 직접적으로 Transaction 처리하지 않고, 선언적으로 Transaction을 관리할 수 있는데 Annotation을 이용한 Transaction 관리, XML 정의를 이용한 Transaction 관리를 지원한다.

## 설명
### Annotation Transaction Management
Annotation 설정을 이용해서 Transaction을 관리할 수 있는데 아래에서 예를 들어서 설정 방법과 사용법을 설명한다.

#### Configuration

```xml
<tx:annotation-driven transaction-manager="transactionManager" />
```

설정 XML에 위의 \<tx:annotation-driven..\>을 기재하면 설정된다. transactionManager는 [TransactionManager 설정](./transaction.md) 참조

#### Sample Source

```java
@Transactional
public void removeRole(Role role) throws Exception {
    this.roleDAO.removeRole(role);
}
```

위의 예를 보면 @Transactional을 트랜잭션 처리하고자 하는 메소드위에 기재하여 트랜잭션 관리를 할 수 있다. @Transactional에 속성을 정의하여 쓸 수 있는데 속성 목록은 아래와 같다.

| 속 성                    | 설 명                                                                           | 사 용 예                                                 |
| ---------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------- |
| isolation              | Transaction의 isolation Level 정의하는 요소. 별도로 정의하지 않으면 DB의 Isolation Level을 따름.   | @Transactional(isolation=Isolation.DEFAULT)           |
| noRollbackFor          | 정의된 Exception 목록에 대해서는 rollback을 수행하지 않음.                                     | @Transactional(noRollbackFor=NoRoleBackTx.class)      |
| noRollbackForClassName | Class 객체가 아닌 문자열을 이용하여 rollback을 수행하지 않아야 할 Exception 목록 정의                   | @Transactional(noRollbackForClassName=“NoRoleBackTx”) |
| propagation            | Transaction의 propagation 유형을 정의하기 위한 요소                                       | @Transactional(propagation=Propagation.REQUIRED)      |
| readOnly               | 해당 Transaction을 읽기 전용 모드로 처리 (Default = false)                                | @Transactional(readOnly = true)                       |
| rollbackFor            | 정의된 Exception 목록에 대해서는 rollback 수행                                            | @Transactional(rollbackFor=RoleBackTx.class)          |
| rollbackForClassName   | Class 객체가 아닌 문자열을 이용하여 rollback을 수행해야 할 Exception 목록 정의                       | @Transactional(rollbackForClassName=“RoleBackTx”)     |
| timeout                | 지정한 시간 내에 해당 메소드 수행이 완료되지 않은 경우 rollback 수행. -1일 경우 no timeout (Default = -1) | @Transactional(timeout=10)                            |

### Configurational Transaction Management
XML 정의 설정을 이용해서 Transaction을 관리할 수 있는데 아래에서 예를 들어서 설정 방법과 사용법을 설명한다.

#### Configuration

```xml
<aop:config>
    <aop:pointcut id="requiredTx" expression="execution(* egovframework.sample..impl.*Impl.*(..))"/>
    <aop:advisor advice-ref="txAdvice" pointcut-ref="requiredTx" />
</aop:config>

<tx:advice id="txAdvice" transaction-manager="transactionManager">
<tx:attributes>
    <tx:method name="find*" read-only="true"/>
    <tx:method name="createNoRBRole" no-rollback-for="NoRoleBackTx"/>
    <tx:method name="createRBRole" rollback-for="RoleBackTx"/>
    <tx:method name="create*"/>
</tx:attributes>
</tx:advice>
```

위의 설정을 보면 aop:pointcut를 이용하여 실행되어 Catch해야 하는 Method를 지정하고 tx:advice를 통해서 각각에 대한 룰을 정의하고 있다. 이렇게 정의하면 프로그램내에서는 별도의 트랜잭션 관련한 사항에 대해서 기술하지 않아도 트랜잭션관리가 된다. 위 샘플 XML에서와 같이 Transaction 관리를 위해 <tx:advice> 하위 태그인 <tx:method>에는 다음과 같은 상세 속성 정보를 부여할 수 있다. 관련 속성 정보는 아래와 같다.

| 속 성             | 설 명                                                                           | 사 용 예                          |
| --------------- | ----------------------------------------------------------------------------- | ------------------------------ |
| name            | 메소드명 기술. 와일드카드 사용 가능함                                                         | name=“find\*”                  |
| isolation       | Transaction의 isolation Level 정의하는 요소. 별도로 정의하지 않으면 DB의 Isolation Level을 따름.   | isolation=“DEFAULT”            |
| no-rollback-for | 정의된 Exception 목록에 대해서는 rollback을 수행하지 않음.                                     | no-rollback-for=“NoRoleBackTx” |
| propagation     | Transaction의 propagation 유형을 정의하기 위한 요소                                       | propagation=“REQUIRED”         |
| read-only       | 해당 Transaction을 읽기 전용 모드로 처리 (Default = false)                                | read-only=“true”               |
| rollback-for    | 정의된 Exception 목록에 대해서는 rollback 수행                                            | rollback-for=“RoleBackTx”      |
| timeout         | 지정한 시간 내에 해당 메소드 수행이 완료되지 않은 경우 rollback 수행. -1일 경우 no timeout (Default = -1) | timeout=“10”                   |

관련 속성별 가능 값 정보는 [스키마](http://www.springframework.org/schema/tx/spring-tx-2.5.xsd) 참조.

### Propagation Behavior, Isolation Level
위에서 설명한 두가지 Transaction Management에 공통적으로 사용되는 항목은 Propagation 과 Isolation Level에 대한 설명을 하고자 한다.

#### Propagation Behavior

트랜잭션의 전파 규칙을 설정하기 위해 사용한다.

| 속 성 명                     | 설 명                                                                                                                                                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PROPAGATION_MADATORY      | 반드시 Transaction 내에서 메소드가 실행되어야 한다. 없으면 예외발생                                                                                                                                                                                                                |
| PROPAGATION_NESTED        | Transaction에 있는 경우, 기존 Transaction 내의 nested transaction 형태로 메소드를 실행하고, nested transaction 자체적으로 commit, rollback이 가능하다. Transaction이 없는 경우, PROPAGATION_REQUIRED 속성으로 행동한다. nested transaction 형태로 실행될 때는 수행되는 변경사항이 커밋이 되기 전에는 기존 Transaction에서 보이지 않는다. |
| PROPAGATION_NEVER         | Manatory와 반대로 Transaction 없이 실행되어야 하며 Transaction이 있으면 예외를 발생시킨다.                                                                                                                                                                                          |
| PROPAGATION_NOT_SUPPORTED | Transaction 없이 메소드를 실행하며,기존의 Transaction이 있는 경우에는 이 Transaction을 호출된 메소드가 끝날 때까지 잠시 보류한다                                                                                                                                                                   |
| PROPAGATION_REQUIRED      | 기존 Transaction이 있는 경우에는 기존 Transaction 내에서 실행하고, 기존 Transaction이 없는 경우에는 새로운 Transaction을 생성한다.                                                                                                                                                            |
| PROPAGATION_REQUIRED_NEW  | 호출되는 메소드는 자신 만의 Transaction을 가지고 실행하고, 기존의 Transaction들은 보류된다                                                                                                                                                                                              |
| PROPAGATION_SUPPORTS      | 새로운 Transaction을 필요로 하지는 않지만, 기존의 Transaction이 있는 경우에는 Transaction 내에서 메소드를 실행한다.                                                                                                                                                                          |

#### Isolation Level

Transaction에서 일관성이 없는 데이터를 허용하도록 하는 수준이며, 여러 Transaction들이 다른 Transaction의 방해로부터 보호되는 정도를 나타낸다. 좀더 자세한 설명은 [여기](http://en.wikipedia.org/wiki/Isolation_level) 참고.

| 속 성 명                      | 설 명                                                                                                                                                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ISOLATION_DEFAULT          | 개별적인 PlatformTransactionManager를 위한 격리 레벨                                                                                                                                                                                    |
| ISOLATION_READ_COMMITTED   | 이 격리수준을 사용하는 메소드는 commit 되지 않은 데이터를 읽을 수 없다. 쓰기 락은 다른 Transaction에 의해 이미 변경된 데이터는 얻을수 없다. 따라서 조회 중인 commit 되지 않은 데이터는 불가능하다. 대개의 데이터베이스에서의 디폴트로 지원하는 격리 수준이다.                                                                |
| ISOLATION_READ_UNCOMMITTED | 가장 낮은 Transaction 수준이다. 이 격리수준을 사용하는 메소드는 commit 되지 않은 데이터를 읽을 수 있다. 그러나 이 격리수준은 새로운 레코드가 추가되었는지 알수 없다.                                                                                                                      |
| ISOLATION_REPEATABLE_READ  | ISOLATION_READ_COMMITED 보다는 다소 조금 더 엄격한 격리 수준이다. 이 격리 수준은 다른 Transaction이 새로운 데이터를 입력했다면, 새롭게 입력된 데이터를 조회할 수 있다는 것을 의미한다.                                                                                                    |
| ISOLATION_SERIALIZABLE     | 가장 높은 격리수준이다. 모든 Transaction(조회를 포함하여)은 각 라인이 실행될 때마다 기다려야 하기 때문에 매우 느리다. 이 격리수준을 사용하는 메소드는 데이터 상에 배타적 쓰기를 락을 얻음으로써 Transaction이 종료될 때까지 조회, 수정, 입력 데이터로부터 다른 Transaction의 처리를 막는다. 가장 많은 비용이 들지만 신뢰할만한 격리 수준을 제공하는 것이 가능하다. |

## 참고자료