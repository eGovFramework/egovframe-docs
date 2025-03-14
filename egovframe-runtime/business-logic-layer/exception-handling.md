---
title: Exception Handling 서비스
linkTitle: Exception Handling
description: 전자정부 표준프레임워크 기반 시스템에서 Exception 처리는 AOP를 이용해 비즈니스 로직과 분리된 After throwing advice로 정의되며, Exception에 따른 적절한 대응을 목표로 한다. Exception 발생 시 클래스 정보와 종류는 후처리 로직 적용 여부를 결정하는 중요한 요소이다.
url: /egovframe-runtime/business-logic-layer/exception-handling/
menu:
  depth:
    name: Exception Handling
    weight: 1
    parent: business-logic-layer
---
# Exception Handling 서비스

## 개요

전자정부 표준프레임워크 기반의 시스템 개발 시 Exception 처리, 정확히는 Exception별 특정 로직(후처리 로직이라고 부르기도 함)이 흐를 수 있도록 하여 Exception에 따른 적절한 대응이 가능하도록 하고자 하는데 목적이 있다.<br/>
AOP의 도움을 받아 비즈니스 POJO와 분리되어 After throwing advice로 정의하였다.<br/>
AOP 관련 내용은 [AOP 모듈](../foundation-layer-core/aop.md)을 참조하길 바란다.

Exception에 대해 이야기 하겠다.<br/>
Exception 발생 시 Exception 발생 클래스 정보와 Exception 종류가 중요하다.<br/>
Exception 발생 클래스 정보와 Exception 종류는 모두 후처리 로직의 대상일지 아닐지를 결정하는 데 사용된다.

```java
	public CategoryVO selectCategory(CategoryVO vo) throws Exception {
		CategoryVO resultVO = categoryDAO.selectCategory(vo);
		try {
    ....
 
    // 넘어온 resultVO가 null 인 경우 EgovBizException 발생 (result.nodata.msg는 메세지 키에 해당됨)
		if (resultVO == null)
			throw processException("result.nodata.msg"); 
            // 또는 throw processException("result.nodata.msg", 발생한 Exception );
		return resultVO;
	}
```

## 설명

앞에서 언급했던 Exception 후처리 방식과 Exception은 아니지만 후처리 로직(leaveaTrace)을 실행할 하는 방식에 대해 설명하도록 하겠다.<br/>
간략하게 보면 Exception 후처리 방식은 **AOP(pointCut ⇒ after-throw) ⇒ ExceptionTransfer.transfer() ⇒ ExceptionHandlerService ⇒ Handler** 순으로 실행된다.

LeavaTrace는 AOP를 이용하는 구조가 아니고 Exception을 발생하지도 않는다. 단지 후처리 로직을 실행하도록 하고자 함에 목적이 있다.<br/>
실행 순서는 **LeavaTrace ⇒ TraceHandlerService ⇒ Handler** 순으로 실행한다.

먼저 Exception Handling에 대해 알아보도록 하자.

### Aop Config, ExceptionTransfer 설정 및 설명

#### Bean 설정

Exception 후처리와 leaveaTrace 설정을 위해서 샘플에서는 두 개의 xml 파일을 이용한다. (context-aspect.xml, context-common.xml)

먼저 Exception 후처리를 위한 부분을 보겠다.<br/>
Exception Handling을 위한 AOP 설정은 아래와 같다.<br/>
비즈니스 개발 시 패키지 구조는 바뀌기 때문에 Pointcut은 egov.sample.service.\*Impl.\*(..))을 수정하여 적용할 수 있다.<br/>
ExceptionTransfer의 property로 존재하는 exceptionHandlerService는 다수의 HandleManager를 등록 가능하도록 되어 있다.<br/>
여기서는 defaultExceptionHandleManager을 등록한 것을 볼 수 있다.

##### context-aspect.xml

```xml
...
	<aop:config>
		<aop:pointcut id="serviceMethod"
			expression="execution(* egov.sample.service.*Impl.*(..))" />
 
		<aop:aspect ref="exceptionTransfer">
			<aop:after-throwing throwing="exception"
				pointcut-ref="serviceMethod" method="transfer" />
		</aop:aspect>
	</aop:config>
 
	<bean id="exceptionTransfer" class="egovframework.rte.fdl.cmmn.aspect.ExceptionTransfer">
		<property name="exceptionHandlerService">
			<list>
				<ref bean="defaultExceptionHandleManager" />
			</list>
		</property>
	</bean>
 
	<bean id="defaultExceptionHandleManager"
		class="egovframework.rte.fdl.cmmn.exception.manager.DefaultExceptionHandleManager">
		<property name="patterns">
			<list>
				<value>**service.*Impl</value>
			</list>
		</property>
		<property name="handlers">
			<list>
				<ref bean="egovHandler" />
			</list>
		</property>
	</bean>
 
	<bean id="egovHandler"
		class="egovframework.rte.fdl.cmmn.exception.handler.EgovServiceExceptionHandler" />
...
```
defaultExceptionHandleManager는 setPatterns(), setHandlers() 메소드를 가지고 있다. 상단과 같이 등록된 pattern 정보를 이용하여 Exception 발생 클래스와의 비교하여 ture인 경우 handlers에 등록된 handler를 실행한다.<br/>
패턴 검사 시 사용되는 pathMatcher는 AntPathMatcher를 이용하고 있다.

특정 pattern 그룹군을 만든후 patterns에 등록하고 그에 해당하는 후처리 로직을 정의하여 등록할 수 있는 구조이다.

#### Handler 구현체

먼저 클래스에 대한 이해가 필요하다.<br/>
앞단에서 간단하게 설명했지만 다시 정리 하자면 Exception 발생 시 AOP pointcut “After-throwing”에 걸려 ExceptionTransfer 클래스의 transfer가 실행된다.<br/>
transfer 메소드는 ExceptionHandlerManager의 run 메소드를 실행한다. <br/>
아래는 구현 예로 DefaultExceptionHandleManager 코드이다.<br/>
**(구현 시 필수사항) 상위클래스는 AbsExceptionHandleManager 이고 인터페이스는 ExceptionHandlerService 이다.**<br/>
구현되는 메소드는 run(Exception exception)인 것을 확인할 수 있다.

##### DefaultExceptionHandleManager.java

```java
public class DefaultExceptionHandleManager extends AbsExceptionHandleManager implements ExceptionHandlerService {
 
	@Override
	public boolean run(Exception exception) throws Exception {
 
		log.debug(" DefaultExceptionHandleManager.run() ");
 
		// 매칭조건이 false 인 경우
		if (!enableMatcher())
			return false;
 
		for (String pattern : patterns) {
			log.debug("pattern = " + pattern + ", thisPackageName = " + thisPackageName);
			log.debug("pm.match(pattern, thisPackageName) =" + pm.match(pattern, thisPackageName));
			if (pm.match(pattern, thisPackageName)) {
				for (ExceptionHandler eh : handlers) {
					eh.occur(exception, getPackageName());
				}
				break;
			}
		}
 
		return true;
	}
 
}
```

#### Customizable Handler 등록

시나리오 : CustomizableHandler 클래스를 만들어 보고 sample 패키지에 있는 Helloworld 클래스 Exception 시에 CustomizableHandler를 실행한다.<br/>
먼저 CustomHandler 클래스를 아래와 같이 만든다.<br/>
ExceptionHandleManager 에서는 occur 메소드를 실행한다.<br/>
**Handler 구현체는 반드시 (필수사항) ExceptionHandler 인터페이스를 구현해야 한다.**

##### CustomizableHandler.java

```java
public class CustomizableHandler implements ExceptionHandler {
 
	protected Log log = LogFactory.getLog(this.getClass());
 
	public void occur(Exception ex, String packageName) {
 
		log.debug(" CustomHandler run...............");
		try {
			log.debug(" CustomHandler 실행 ...  ");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```

CustomizableHandler의 등록을 해보도록 하겠다.<br/>
여기서 주의해야 하는 부분은 patterns에 sample 패키지에 있는 Helloworld 클래스를 지정해주어야 한다는 것이다.

```xml
	<bean id="exceptionTransfer" class="egovframework.rte.fdl.cmmn.aspect.ExceptionTransfer">
		<property name="exceptionHandlerService">
			<list>
				<ref bean="customizableExceptionHandleManager" />
			</list>
		</property>
	</bean>
 
	<bean id="customizableExceptionHandleManager"
		class="egovframework.rte.fdl.cmmn.exception.manager.DefaultExceptionHandleManager">
		<property name="patterns">
			<list>
				<value>**sample.Helloworld</value>
			</list>
		</property>
		<property name="handlers">
			<list>
				<ref bean="customizableHandler1" />
				<ref bean="customizableHandler2" />
				<ref bean="customizableHandler3" />
			</list>
		</property>
	</bean>
 
	<bean id="customizableHandler1" class="sample.CustomizableHandler" />
	<bean id="customizableHandler2" class="sample.CustomizableHandler" />
	<bean id="customizableHandler3" class="sample.CustomizableHandler" />
```

이런식으로 여러개의 Handler를 등록해줄 수 있다.

### leaveaTrace 설정 및 설명

Exception이거나 Exception이 아닌 경우에 Trace 후처리 로직을 실행시키고자 할 때 사용한다.<br/>
설정하는 기본적인 구조는 Exception 후처리하는 방식과 같다. 설정 파일은 context-common.xml 이다.<br/>
DefaultTraceHandleManager에 TraceHandler를 등록하는 형태로 설정된다.

#### Bean 설정

```xml
...
	<bean id="leaveaTrace" class="egovframework.rte.fdl.cmmn.trace.LeaveaTrace">
		<property name="traceHandlerServices">
			<list>
				<ref bean="traceHandlerService" />
			</list>
		</property>
	</bean>
 
	<bean id="traceHandlerService" 	class="egovframework.rte.fdl.cmmn.trace.manager.DefaultTraceHandleManager">
		<property name="patterns">
			<list>
				<value>*</value>
			</list>
		</property>
		<property name="handlers">
			<list>
				<ref bean="defaultTraceHandler" />
			</list>
		</property>
	</bean>
 
	<bean id="antPathMatcher" class="org.springframework.util.AntPathMatcher" />
 
	<bean id="defaultTraceHandler"
		class="egovframework.rte.fdl.cmmn.trace.handler.DefaultTraceHandler" />
...
```

#### TraceHandler 확장 개발 Sample

##### Interface TraceHandler를 아래와 같이 implements 한다.

```java
package egovframework.rte.fdl.cmmn.trace.handler;
 
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
 
 
public class DefaultTraceHandler implements TraceHandler {
 
 
    public void todo(Class clazz, String message) {
	//수행하고자 하는 처리로직을 넣는 부분...
	System.out.println(" log ==> DefaultTraceHandler run...............");
    }
 
}
```

##### leaveaTrace 코드상 발생 Sample

사용 방법을 다시 상기해보면 아래와 같다.<br/>
메세지 키(message.trace.msg)를 이용하여 메세지 정보를 넘겨 Handler를 실행한다.

```java
	public CategoryVO selectCategory(CategoryVO vo) throws Exception {
		CategoryVO resultVO = categoryDAO.selectCategory(vo);
		try {
		  //강제로 발생한 ArithmeticException  
			int i = 1 / 0;
		} catch (ArithmeticException athex) {
		  //Exception을 발생하지 않고 후처리 로직 실행.
			leaveaTrace("message.trace.msg");
		}
 
		return resultVO;
	}
```

## 참고자료

- [exception-handling-framework-for-j2ee](https://www.oreilly.com/radar/?page=1)
- Effective Java (Joshua Bloch) : Chapter 8 예외처리