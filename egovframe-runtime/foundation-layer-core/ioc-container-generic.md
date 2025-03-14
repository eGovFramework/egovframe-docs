---
title: Generic
linkTitle: "Generic"
description: Spring 4 이상에서는 Autowired 및 Qualifier를 보완하여 제네릭(Generic) 타입의 의존성 주입을 지원한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-generic/"
menu:
  depth:
    name: Generic
    weight: 15
    parent: "ioc-container"
---
# Generic

## 개요

 Spring4 Generic은 Autowired 및 Qualifired를 보완하여 Generic을 지원합니다.

## 설명

 기존 Autowire 및 Qualifier의 기능에 대하여 확장하여 Spring4에서 추가로 지원하는 Generic 타입의 Autowire기능에 대하여 알아본다.

### Autowire 및 Qualifier

#### Autowiring 예제

 다음은 Customer 클래스에 Person property로 Autowire하는 예제이다.

 ```java
package com.egovframe.common;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
 
public class Customer {
	@Autowired
	private Person person;
	//...
}
```

#### Autowire의 문제점

 다음과 같은경우 Person에 Autowire로 주입될수 없다.

 ```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
		http://www.springframework.org/schema/beans/spring-beans-2.5.xsd">
 
	<bean class ="org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor"/>
 
	<bean id="customer" class="com.egovframe.common.Customer" />
 
	<bean id="personA" class="com.egovframe.common.Person" >
		<property name="name" value="GentlemanA" />
	</bean>
 
	<bean id="personB" class="com.egovframe.common.Person" >
		<property name="name" value="GentlemanB" />
	</bean>
 
</beans>
```

 같은 타입이 2개이므로 다음과 같은 오류를 발생시킨다.

 ```java
Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: 
	No unique bean of type [com.egovframe.common.Person] is defined: 
		expected single matching bean but found 2: [personA, personB]

```

#### Qualifier 사용

 Qualifier 어노테이션에 personA를 특정하여 처리 할수 있으나 개별적으로 하나하나 지정해야 하는 문제가 있다.

 ```java
package com.egovframe.common;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
 
public class Customer {
	@Autowired
	@Qualifier("personA")
	private Person person;
	//...
}
```

### Spring 4 Generics

#### Generic 설정

 추상화 클래스 Employee를 구현한 Manager,Admin을 Generic으로 설정한다. 이경우 Spring 4의 Generic에 대하여 Autowire 주입 대상이 된다.

 ```java
package generic;
 
import org.springframework.beans.factory.annotation.Autowired;
 
public class InjectBeans {
    @Autowired
    Employee<Manager> emp1;
 
    @Autowired
    Employee<Admin> emp2;
 
    public void invokeManager(){
        emp1.empSection();
    }
 
    public void invokeAdmin(){
    	emp2.empSection();
    }
}
```

#### 주입대상 구현 클래스

 Employee는 추상클래스이며 상속을 통하여 구현된다. Admin과 Manager는 구현클래스이며 Autowire 어노테이션에의해 자동 주입된다.

 ```java
package generic;
 
public abstract class Employee<T> {
    public void printCompanyName(){
        System.out.println("Display : Company Name");
    }
 
    public abstract void empSection();
}
```

 ```java
package generic;
 
public class Admin extends Employee<Admin>{
    public void empSection(){
        System.out.println("Display : Admin Section");
    }
}
```

 ```java
package generic;
 
public class Manager extends Employee<Manager>{
    public void empSection(){
        System.out.println("Display : Manager Section");
    }
}
```

#### 수행결과

 구현 클래스 각각의 empSection()이 수행되어 다음과 같은 결과가 출력된다.

```bash
6월 23, 2015 11:23:54 오전 org.springframework.context.annotation.AnnotationConfigApplicationContext prepareRefresh
INFO: Refreshing org.springframework.context.annotation.AnnotationConfigApplicationContext@1262a85: startup date [Tue Jun 23 11:23:54 KST 2015]; root of context hierarchy
Display : Admin Section
Display : Manager Section

```

#### Spring 3에서의 complie 및 실행

 Spring 3에서는 complie은 문제가 없으나 runtime시에 Generic 타입에 대한 주입기능이 없으므로 다음과 같은 오류가 발생한다.

 ```bash
6월 23, 2015 10:38:25 오전 org.springframework.context.annotation.AnnotationConfigApplicationContext prepareRefresh
INFO: Refreshing org.springframework.context.annotation.AnnotationConfigApplicationContext@1110f31: startup date [Tue Jun 23 10:38:25 KST 2015]; root of context hierarchy
6월 23, 2015 10:38:26 오전 org.springframework.beans.factory.support.DefaultListableBeanFactory preInstantiateSingletons
INFO: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@17f70bf: defining beans [org.springframework.context.annotation.internalConfigurationAnnotationProcessor,org.springframework.context.annotation.internalAutowiredAnnotationProcessor,org.springframework.context.annotation.internalRequiredAnnotationProcessor,org.springframework.context.annotation.internalCommonAnnotationProcessor,springMVCConfiguration,org.springframework.context.annotation.ConfigurationClassPostProcessor.importAwareProcessor,getManager,InjectBeans,getAdmin]; root of factory hierarchy
6월 23, 2015 10:38:26 오전 org.springframework.beans.factory.support.DefaultListableBeanFactory destroySingletons
INFO: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@17f70bf: defining beans [org.springframework.context.annotation.internalConfigurationAnnotationProcessor,org.springframework.context.annotation.internalAutowiredAnnotationProcessor,org.springframework.context.annotation.internalRequiredAnnotationProcessor,org.springframework.context.annotation.internalCommonAnnotationProcessor,springMVCConfiguration,org.springframework.context.annotation.ConfigurationClassPostProcessor.importAwareProcessor,getManager,InjectBeans,getAdmin]; root of factory hierarchy
Exception in thread "main" org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'InjectBeans': Injection of autowired dependencies failed; nested exception is org.springframework.beans.factory.BeanCreationException: Could not autowire field: generic.Employee generic.InjectBeans.emp1; nested exception is org.springframework.beans.factory.NoUniqueBeanDefinitionException: No qualifying bean of type [generic.Employee] is defined: expected single matching bean but found 2: getManager,getAdmin
	at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor.postProcessPropertyValues(AutowiredAnnotationBeanPostProcessor.java:289)
	at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.populateBean(AbstractAutowireCapableBeanFactory.java:1146)
	at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:519)
	at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:458)
	at org.springframework.beans.factory.support.AbstractBeanFactory$1.getObject(AbstractBeanFactory.java:296)
	at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:223)
	at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:293)
	at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:194)
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.preInstantiateSingletons(DefaultListableBeanFactory.java:633)
	at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:932)
	at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:479)
	at org.springframework.context.annotation.AnnotationConfigApplicationContext.<init>(AnnotationConfigApplicationContext.java:73)
	at generic.SpringMVCApplicationDemo.main(SpringMVCApplicationDemo.java:15)
Caused by: org.springframework.beans.factory.BeanCreationException: Could not autowire field: generic.Employee generic.InjectBeans.emp1; nested exception is org.springframework.beans.factory.NoUniqueBeanDefinitionException: No qualifying bean of type [generic.Employee] is defined: expected single matching bean but found 2: getManager,getAdmin
	at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor$AutowiredFieldElement.inject(AutowiredAnnotationBeanPostProcessor.java:517)
	at org.springframework.beans.factory.annotation.InjectionMetadata.inject(InjectionMetadata.java:87)
	at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor.postProcessPropertyValues(AutowiredAnnotationBeanPostProcessor.java:286)
	... 12 more
Caused by: org.springframework.beans.factory.NoUniqueBeanDefinitionException: No qualifying bean of type [generic.Employee] is defined: expected single matching bean but found 2: getManager,getAdmin
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.doResolveDependency(DefaultListableBeanFactory.java:870)
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.resolveDependency(DefaultListableBeanFactory.java:775)
	at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor$AutowiredFieldElement.inject(AutowiredAnnotationBeanPostProcessor.java:489)
	... 14 more

```