---
title: "Bean Definition Inheritance"
linkTitle: "Inheritance"
description: Bean 정의는 설정 정보를 포함하며, 자식 bean 정의는 부모 bean 정의로부터 설정 정보를 상속받는다. 자식 bean 정의는 부모로부터 상속받은 설정 정보를 필요에 따라 덮어쓰거나 추가할 수 있다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-bean_definition_inheritance/"
menu:
    depth:
        weight: 6
        parent: "ioc-container"
---
# Bean definition inheritance

## 개요

 Bean 정의는 많은 양의 설정 정보를 포함하고 있다. 자식 bean 정의는 부모 bean 정의로부터 설정 정보를 상속받은 bean 정의를 의미한다. 자식 bean 정의는 필요에 따라 부모 bean 정의로부터 상속받은 설정 정보를 덮어쓰거나 추가할 수 있다.

## 설명

 XML 기반 설정에서는 자식 bean 정의에 'parent' attribute를 사용하여 상속관계를 정의할 수 있다.

 ```xml
<bean id="inheritedTestBean" abstract="true"
        class="org.springframework.beans.TestBean">
    <property name="name" value="parent"/>
    <property name="age" value="1"/>
</bean>
 
<bean id="inheritsWithDifferentClass"
        class="org.springframework.beans.DerivedTestBean"
        parent="inheritedTestBean" init-method="initialize">
    <property name="name" value="override"/>
    <!-- the age property value of 1 will be inherited from  parent -->
</bean>
```

 자식 bean 정의는 bean class가 명기되어 있지 않을 경우, 부모 bean 정의의 값을 사용한다. 만약 자식 bean 정의에 bean class가 명기되어 있는 경우, 자식 bean 정의의 bean class는 부모 bean 정의의 모든 property 값을 받아들일 수 있어야 한다.

 자식 bean 정의는 부모 bean 정의의 생성자 argument 값, property 값, 그리고 메소드 덮어씀을 상속받는다. 만약 init-method, destroy-method, static factory 메소드 설정이 명기되어 있을 경우, 부모의 설정을 덮어쓴다.

 다음 설정은 항상 자식 bean 정의의 값을 따른다: ***depends on, autowire mode, dependency check, singleton, scope, lazy init***.

 부모 bean 정의는 abstract attribute를 사용하여 abstract로 설정할 수 있다. 이 경우, 부모 bean 정의는 class를 지정하지 않는다.

 ```xml
<bean id="inheritedTestBeanWithoutClass" abstract="true">
    <property name="name" value="parent"/>
    <property name="age" value="1"/>
</bean>
 
<bean id="inheritsWithClass" class="org.springframework.beans.DerivedTestBean"
        parent="inheritedTestBeanWithoutClass" init-method="initialize">
    <property name="name" value="override"/>
    <!-- age will inherit the value of 1 from the parent bean definition-->
</bean>
```

 부모 bean 정의는 완전하지 않기 때문에 객체화 될 수 없다.

## 참고자료

*   [Spring Framework - Reference Document / 1.7 Bean definition inheritance](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-child-bean-definitions)