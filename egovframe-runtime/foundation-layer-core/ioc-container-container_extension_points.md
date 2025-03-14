---
title: "Container Extension Points"
linkTitle: "Extension"
description: Spring Framework의 IoC 컴포넌트는 확장을 염두에 두고 설계되었다. 일반적으로 개발자가 BeanFactory나 ApplicationContext 구현 클래스를 상속받을 필요는 없으며, Spring IoC Container는 통합 인터페이스의 구현체를 통해 확장할 수 있다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container_extension_points/"
menu:
    depth:
        name: Extension
        weight: 7
        parent: "ioc-container"
---
# Container extension points

## 개요

Spring Framework의 IoC 컴포넌트는 확장을 고려하여 설계되었다. 일반적으로 어플리케이션 개발자가 다양한 BeanFactory 또는 ApplicationContext 구현 클래스를 상속받을 필요는 없다.  
Spring IoC Container는 특별한 통합 interface의 구현체를 삽입하여 확장할 수 있다.

## 설명

### BeanPostProcessors를 사용한 확장(Customizing beans using BeanPostProcessors)

BeanPostProcessors interface는 다수의 callback 메소드를 정의하고 있는데, 어플리케이션 개발자는 이들 메소드를 구현함으로써 자신만의 객체화 로직(instantiation logic), 종속성 해결 로직(dependency-resolution logic) 등을 제공할 수 있다.  
org.springframework.beans.factory.config.BeanPostProcessor interface는 두개의 callback 메소드로 구성되어 있다. 특정 class가 Container에 post-processor로 등록되면, post-processor는 Container에서 생성되는 각각의 bean 객체에 대해서, Container 객체화 메소드 전에 callback을 받는다.  
중요한 것은 BeanFactory는 post-processor를 다루는 방식에 있어서 ApplicationContext와는 조금 다르다. ApplicationContext는 BeanPostProcessor interface를 구현한 bean을 ***자동적으로 인식하고*** post-processor로 등록한다. 하지만 BeanFactory 구현을 사용하면 post-processor는 다음과 같이 명시적으로 등록되어야 한다.

 ```java
ConfigurableBeanFactory factory = new XmlBeanFactory(...);
 
// now register any needed BeanPostProcessor instances
MyBeanPostProcessor postProcessor = new MyBeanPostProcessor();
factory.addBeanPostProcessor(postProcessor);
 
// now start using the factory
```

 명시적인 등록은 불편하기 때문에 대부분의 Spring 기반 어플리케이션에서는 순수 BeanFactory 구현보다는 ApplicationContext 구현을 사용한다.

#### Example: Hello World, BeanPostProcessor-style

 본 예제는 올바른 예는 아니지만, 기본적인 사용 방법을 보여주기 위함이다.

 ```java
package scripting;
 
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.beans.BeansException;
 
public class InstantiationTracingBeanPostProcessor implements BeanPostProcessor {
    // simply return the instantiated bean as-is
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        return bean; // we could potentially return any object reference here...
    }
 
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("Bean '" + beanName + "' created : " + bean.toString());
        return bean;
    }
}
```

 ```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:lang="http://www.springframework.org/schema/lang"
    xsi:schemaLocation=" http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/lang
        http://www.springframework.org/schema/lang/spring-lang.xsd">
 
    <lang:groovy id="messenger" script-source="classpath:org/springframework/scripting/groovy/Messenger.groovy">
        <lang:property name="message" value="Fiona Apple Is Just So Dreamy."/> 
    </lang:groovy>
 
    <!-- 
    when the above bean ('messenger') is instantiated, this custom
    BeanPostProcessor implementation will output the fact to the system console
    -->
    <bean class="scripting.InstantiationTracingBeanPostProcessor"/>
</beans>
```

 InstantiationTracingBeanPostProcessor는 단순히 정의된다. 비록 이름을 가지고 있지는 않지만 bean이기 때문에 다른 bean과 같이 종속성은 삽입될 수 있다.

### BeanFactoryPostProcesors를 사용한 확장(Customizing configuration metadata with BeanFactoryPostProcessors)

 org.springframework.beans.factory.config.BeanFactoryPostProcessor는 BeanPostProcessor와 의미적으로 비슷하지만, 큰 차이점 중 하나는 BeanFactoryPostProcessors는 bean 설정 메타정보를 처리한다는 것이다. Spring IoC Container는 BeanFactoryPostProcessors가 설정 메타정보를 읽고, Container가 실제로 bean을 객체화 하기 전에 그 정보를 변경할 수 있도록 허용한다.

 Bean factory post-processor는 BeanFactory의 경우 수동으로 실행되고, ApplicationContext의 경우 자동으로 실행된다.

 BeanFactory에서는 다음과 같이 수동으로 실행한다.

 ```java
XmlBeanFactory factory = new XmlBeanFactory(new FileSystemResource("beans.xml"));
 
// bring in some property values from a Properties file
PropertyPlaceholderConfigurer cfg = new PropertyPlaceholderConfigurer();
cfg.setLocation(new FileSystemResource("jdbc.properties"));
 
// now actually do the replacement
cfg.postProcessBeanFactory(factory);
```

#### Example: the PropertyPlaceholderConfigurer

 PropertyPlaceholderConfigurer는 BeanFactory 정의로부터 property 값을 분리하기 위해 사용한다. 분리된 값은 Java Properties 형식으로 작성된 다른 파일로 분리된다. 이 방식은 주 XML 설정 파일을 변경하지 않고, 환경 변수 등을 변경할 때 유용하다.(예를 들어 database URLs, 사용자명, 패스워드 등)

 ```xml
<bean class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
    <property name="locations">
        <value>classpath:com/foo/jdbc.properties</value>
    </property>
</bean>
 
<bean id="dataSource" destroy-method="close" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="${jdbc.driverClassName}"/>
    <property name="url" value="${jdbc.url}"/>
    <property name="username" value="${jdbc.username}"/>
    <property name="password" value="${jdbc.password}"/>
</bean>
```

 위 설정의 실제 값은 아래와 같다.

 ```java
jdbc.driverClassName=org.hsqldb.jdbcDriver
jdbc.url=jdbc:hsqldb:hsql://production:9002
jdbc.username=sa
jdbc.password=root

```

 만약 Spring 2.5부터 지원되는 context namespace를 사용하면 다음과 같이 설정할 수 있다.

 ```xml
<context:property-placeholder location="classpath:com/foo/jdbc.properties"/>
```

 PropertyPlaceholderConfigurer는 사용자가 지정한 Properties 파일 뿐 아니라 만약 지정한 property가 없을 경우, Java System properties도 검사할 수 있다. 이 기능은 systemPropertiesMode 설정을 통해 조절할 수 있다.

#### Example: the PropertyOverrideConfigurer

 PropertyOverrideConfigurer는 또다른 bean factory post-processor로 PropertyPlaceholderConfigurer와 비슷하다. 하지만 PropertyPlaceholderConfigurer와는 반대로 원본 설정은 bean properties로 기본(default) 값을 가지거나 전혀 값을 가지지 않을 수 있다. 만약 Properties 파일이 특정 bean property를 위한 값을 가지고 있지 않을 경우, 기본 context definition이 사용된다. Properties 파일 설정의 각 줄은 다음과 같은 형식이다.

 ```java
beanName.property=value

```

 Spring 2.5부터 지원되는 context namespace를 사용하면 다음과 같이 설정할 수 있다.

 ```xml
<context:property-override location="classpath:override.properties"/>
```

### FactoryBeans를 사용한 확장(Customizing instantiation logic using FactoryBeans)

 org.springframework.beans.factory.FactoryBean interface를 구현한 객체는 스스로 fatory가 된다. FactoryBean interface는 Spring IoC Container에 객체화 로직을 삽입할 수 있는 방법이다. 만약 복잡한 객체화 코드를 가지고 있어 장황한 XML 설정보다는 Java로 직접 표현하는 것이 더 좋은 경우, 객체화 코드를 가지고 있는 FactoryBean를 생성하여 Container에서 삽입할 수 있다.

 FactoryBean interface는 다음 3가지 메소드를 제공한다.

- Object getObject(): 생성한 객체를 return한다. 생성된 객체는 공유될 수도 있다.
    
- boolean isSingleton(): 만약 FactoryBean이 singleton을 리턴하면 true, 아니면 false 이다.
    
- Class getObjectType(): getObject() 메소드에 의해 객체의 타입을 리턴하는데 미리 알 수 없는 경우에는 null을 리턴한다.
    

 Container에게 FactoryBean이 생성한 객체가 아닌 FactoryBean 그 자체를 요구하는 경우도 있다. 이런 경우, BeanFactory의 getBean 메소드를 호출할 때 bean id 앞에 '&'를 붙이면 된다.

## 참고자료

- [Spring Framework - Reference Document / 1.8 Container Extension Points](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-factory-extension)