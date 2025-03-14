---
linkTitle: "AOP 가이드라인"
title: 실행환경 AOP 가이드라인
url: "/egovframe-runtime/foundation-layer-core/aop/aop-guide/"
menu:
  depth:
    weight: 3
    parent: "AOP"
    name: "AOP 가이드라인"
description: "표준프레임워크 실행환경은 XML Schema 기반의 AOP 방법을 사용하여 예외처리와 트랜잭션을 처리하며, 이는 @AspectJ Annotation 기반보다 횡단 관심사의 설정관계를 파악하는 데 유리하다."
---
# 실행환경 AOP 가이드라인

## 개요

 전자정부 실행환경은 XML Schema에 기반한 AOP 방법을 사용하며, 예외처리와 트랜잭션 처리에 적용하였다. XML Schema에 기반한 AOP 방법은 @AspectJ Annotation 기반 방법에 비해 횡단 관심사에 대한 설정관계를 파악하기 유리하다.

## 설명

### 예외 처리

 실행환경은 DAO에서 발생한 Exception을 받아 Service단에서 처리할 수 있다. 실행환경에서 추가로 제공하는 Exception은 다음과 같다.

- EgovBizException: 업무에서 Checked Exception인 경우에 공통으로 사용하는 Exception이다. 개발자가 특정한 오류에 대해서 throw하여 특정 메시지를 전달하고자 하는 경우에는 processException() 메소드를 이용하도록 한다.
- ExceptionTransfer: AOP 기능을 이용하여 ServiceImpl 클래스에서 Exception이 발생한 경우(after-throwing인 경우)에 trace()메소드에서 처리한다. 내부적으로 EgovBizException인지 RuntimeException(ex.DataAccessException)인지 구분하여 throw한다. ExceptionTransfer는 내부적으로 DefaultExceptionHandleManager 클래스에 의해서 정의된 패턴에 대해서 Handler에 의해서 동작한다.

#### 관점(Aspect) 정의

 예외 처리를 위한 Spring 설정 파일(resources/egovframework.spring/context-aspect.xml) 내에 관점(Aspect) 클래스를 빈으로 정의한 뒤, 해당 관점(Aspect)에 대한 포인트컷과 충고(Advice)를 정의한다.

```xml
<bean id="exceptionTransfer" class="org.egovframe.rte.fdl.cmmn.aspect.ExceptionTransfer">
...
</bean>
 
<aop:config>
	<aop:pointcut id="serviceMethod" expression="execution(* org.egovframe.rte.sample.service..*Impl.*(..))" />
		<aop:aspect ref="exceptionTransfer">
		<aop:after-throwing throwing="exception" pointcut-ref="serviceMethod" method="transfer" />
	</aop:aspect>
</aop:config>
...
</beans>
```

 ExceptionTransfer는 org.egovframe.rte.sample.service 패키지 내에 속한 모든 클래스 중 클래스명이 Impl로 끝나는 클래스의 메소드 실행시 발생한 예외를 처리하는 역할을 수행한다.

#### 충고(Advice) 정의

 충고(Advice)로 정의된 ExceptionTransfer 클래스는 실행환경 소스코드에 포함되어 있다. ExceptionTransfer 클래스는 예외가 발생된 경우 내부적으로 예외처리 설정 파일에 명시된 ExceptionHandler를 호출하는 기능을 한다. ExceptionTransfer 클래스의 코드 일부는 다음과 같다.

```java
public class ExceptionTransfer {
	...
	public void transfer(JoinPoint thisJoinPoint, Exception exception) throws Exception {
		log.debug("execute ExceptionTransfer.transfer ");
 
		Class clazz = thisJoinPoint.getTarget().getClass();
		Locale locale = LocaleContextHolder.getLocale();
 
		// BizException 인 경우는 이미 메시지 처리 되었음. 로그만 기록
		if (exception instanceof EgovBizException) {
			log.debug("Exception case :: EgovBizException ");
 
			EgovBizException be = (EgovBizException) exception;
			getLog(clazz).error(be.getMessage(), be.getCause());
			// Exception Handler 에 발생된 Package 와 Exception 설정.
			processHandling(clazz, exception, pm, exceptionHandlerServices, false);
			throw be;
		} else if (exception instanceof RuntimeException) {
			log.debug("RuntimeException case :: RuntimeException ");
 
			RuntimeException be = (RuntimeException) exception;
			getLog(clazz).error(be.getMessage(), be.getCause());
			// Exception Handler 에 발생된 Package 와 Exception 설정.
			processHandling(clazz, exception, pm, exceptionHandlerServices, true);
 
			if (be instanceof DataAccessException) {
				log.debug("RuntimeException case :: DataAccessException ");
				DataAccessException sqlEx = (DataAccessException) be;
				// throw processException(clazz, "fail.data.sql",
				// new String[] {
				// Integer.toString(((SQLException) sqlEx
				// .getCause()).getErrorCode()),
				// ((SQLException) sqlEx.getCause())
				// .getLocalizedMessage() }, sqlEx, locale);
				throw sqlEx;
			}
			throw be;
		} else if (exception instanceof FdlException) {
			log.debug("FdlException case :: FdlException ");
			FdlException fe = (FdlException) exception;
			getLog(clazz).error(fe.getMessage(), fe.getCause());
			throw fe;
		} else {
			og.debug("case :: Exception ");
			getLog(clazz).error(exception.getMessage(), exception.getCause());
			throw processException(clazz, "fail.common.msg", new String[] {}, exception, locale);
		}
	}
}
```

### 트랜잭션 처리

 실행환경에서 트랜잭션 설정은 “resources/egovframework.spring/context-transaction.xml” 파일을 참조한다. 다음은 context-transaction.xml 설정 파일을 일부이다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	...
	http://www.springframework.org/schema/tx
	http://www.springframework.org/schema/tx/spring-tx.xsd
	http://www.springframework.org/schema/aop
	http://www.springframework.org/schema/aop/spring-aop.xsd">
 
	<!-- 트랜잭션 관리자를 설정한다.  -->
	<bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
		<property name="dataSource" ref="dataSource"/>
	</bean>
 
	<!-- 트랜잭션 Advice를 설정한다. -->
	<tx:advice id="txAdvice" transaction-manager="txManager">
		<tx:attributes>
			<tx:method name="*" rollback-for="Exception"/>
		</tx:attributes>
	</tx:advice>
 
	<!-- 트랜잭션 Pointcut를 설정한다.--->
	<aop:config>
		<aop:pointcut id="requiredTx" expression="execution(* org.egovframe.rte.sample..impl.*Impl.*(..))"/>
		<aop:advisor advice-ref="txAdvice" pointcut-ref="requiredTx" />
	</aop:config>
</beans>
```

- txAdvice는 메소드에서 예외 발생시 트랜잭션 롤백을 수행한다.
- requiredTx는 egovframework.rte.sample 패키지 하위 impl 패키지에서 Impl로 끝나는 모든 클래스의 메소드를 포인트컷으로 지정한다.

## 참고자료

- [실행환경 Exception Handling 서비스](../business-logic-layer/exception-handling.md)
- [실행환경 Transaction 서비스](../persistence-layer/transaction.md)