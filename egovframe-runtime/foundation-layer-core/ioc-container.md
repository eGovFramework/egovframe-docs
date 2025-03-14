---
title: "IoC Container"
linkTitle: IoC Container
description: IoC 컨테이너는 객체 간의 종속성을 소스 코드 외부에서 설정하여 유연성과 확장성을 높이는 Spring 프레임워크의 핵심 기능이다.
url: /egovframe-runtime/foundation-layer-core/ioc-container/
menu:
  depth:
    name: IoC Container
    weight: 1
    parent: "foundation-layer-core"
    identifier: "ioc-container"
---
# IoC Container

## 개요
프레임워크의 기본적인 기능인 Inversion of Control(IoC) Container 기능을 제공하는 서비스이다.   
객체의 생성 시, 객체가 참조하고 있는 타 객체에 대한 종속성을 소스 코드 내부에서 하드 코딩하는 것이 아닌, 소스 코드 외부에서 설정하게 함으로써, 유연성 및 확장성을 향상시킨다.

### 주요 개념
#### Inversion of Control(IoC)
IoC는 Inversion of Control의 약자이다. 우리나라 말로 직역해 보면 "역제어"라고 할 수 있다. 제어의 역전 현상이 무엇인지 살펴본다.   
기존에 자바 기반으로 어플리케이션을 개발할 때 자바 객체를 생성하고 서로간의 의존 관계를 연결시키는 작업에 대한 제어권은 보통 개발되는 어플리케이션에 있었다.   
그러나, Servlet, EJB 등을 사용하는 경우 Servlet Container, EJB Container에게 제어권이 넘어가서 객체의 생명주기(Life Cycle)를 Container들이 전담하게 된다.   
이처럼 IoC에서 이야기하는 제어권의 역전이란 객체의 생성에서부터 생명주기의 관리까지 모든 객체에 대한 제어권이 바뀌었다는 것을 의미한다.

#### 관련문서
  * [Martin Fowler](http://martinfowler.com)가 저술한 [Inversion of Control](http://martinfowler.com/bliki/InversionOfControl.html)
  * [Inversion of Control 한글 번역](./ioc-container-inversion-of-control.md)

#### Dependency Injection
각 클래스 사이의 의존관계를 빈 설정(Bean Definition)정보를 바탕으로 컨테이너가 자동적으로 연결해주는 것을 말한다.   
컨테이너가 의존관계를 자동적으로 연결시켜주기 때문에 개발자들이 컨테이너 API를 이용하여 의존관계에 관여할 필요가 없게 되므로 컨테이너 API에 종속되는 것을 줄일 수 있다.   
개발자들은 단지 빈 설정파일(저장소 관리 파일)에서 의존관계가 필요하다는 정보를 추가하기만 하면 된다.

#### 관련문서
  * [Martin Fowler](http://martinfowler.com)가 저술한 [Inversion of Control Containers and the Dependency Injection pattern](http://martinfowler.com/articles/injection.html)
  * [Inversion of Control Containers and the Dependency Injection pattern 한글 번역](http://javacan.tistory.com/entry/120) by [최범균(Blog 자바캔(Java Can Do It))](http://javacan.tistory.com/)

### 사용된 오픈 소스
  * IoC Container는 <https://spring.io/projects/spring-framework>를 수정없이 사용한다.

## 설명
본 IoC Container는 Spring Framework의 기능을 수정없이 사용하는 것으로, 본 가이드 문서는 [Spring Framework Documentation](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html) 을 번역 및 요약한 것이다.   
Spring Framework IoC Container에 대한 상세한 설명이 필요한 경우, Spring Framework Documentation 원본 문서 및 Spring Framework API를 참조한다.

### IoC Container of Spring Framework
org.springframework.beans과 org.springframework.context 패키지는 Spring Framework의 IoC Container의 기반을 제공한다.   
BeanFactory 인터페이스는 객체를 관리하기 위한 보다 진보된 설정 메커니즘을 제공한다.   
BeanFactory 인터페이스를 기반으로 작성된 ApplicationContext 인터페이스(BeanFactory 인터페이스의 sub-interface이다)는 BeanFactory가 제공하는 기능 외에 Spring AOP, 메시지 리소스 처리(국제화에서 사용됨), 이벤트 전파, 웹 어플리케이션을 위한 WebSpplicationContext 등 어플리케이션 레이어에 특화된 context 등의 기능을 제공한다.

요약하면, BeanFactory는 프레임워크와 기본적인 기능에 대한 설정 기능을 제공하는 반면에, ApplicationContext는 좀더 Enterprise 환경에 맞는 기능들을 추가로 제공한다.   
ApplicationContext는 BeanFacatory의 완전한 superset이므로, BeanFactory의 기능 및 행동에 대한 설명은 ApplicationContext에도 모두 해당된다.

본 문서는 크게 두 부분으로 나뉘어지는데, 첫번째 부분은 BeanFactory와 ApplicationContext 모두에 적용되는 기본적인 원리를 설명하고, 두번째 부분은 ApplicationContext에만 적용되는 특징들을 설명한다.

  * [Basics](./ioc-container-basics.md/)
    IoC Container를 설명하기 위해 필요한 기본적인 개념 및 사용 방법을 설명한다.
  * [Dependencies](./ioc-container-dependencies.md/)
    IoC Container의 핵심 기능인 Dependency Injection의 사용 방식 및 설정 방법을 설명한다.
  * [Bean scope](./ioc-container-bean_scope.md/)
    IoC Container에 의해 관리되는 Bean의 생성 방식 및 적용 범위를 설명한다.
  * [Customizing the nature of a bean](./ioc-container-customizing_the_nature_of_a_bean.md/)
    Bean의 생명주기 관리, Bean이 속한 Container 참조 등 Bean의 성질을 변화시키는 방법을 설명한다.
  * [Bean definition inheritance](./ioc-container-bean_definition_inheritance.md/)
    Bean 정의 상속에 대해서 설명한다.
  * [IoC Container:Container extension points](./ioc-container-container_extension_points.md/)
     IoC Container의 기능을 확장하는 방법을 설명한다.
  * [IoC Container:The ApplicationContext](./ioc-container-the_applicationcontext.md/)
     ApplicationContext만이 제공하는 기능을 설명한다.
  * [IoC Container:Annotation-based configuration](./ioc-container-annotation-based_configuration.md/)
    Java Annotation을 기반으로 Bean을 정의하는 방법을 설명한다.
  * [IoC Container:Classpath scanning for managed components](./ioc-container-classpath_scanning_for_managed_components.md/)
    Dependency Injection에 의해 삽입되는 base Bean에 대한 Java Annotation 기반 설정 방법을 설명한다.
  * [IoC Container:JSR 330 Standard Annotations](./ioc-container-jsr_330_standard_annotations.md/)
    JSR-330 표준 Annotation에 대해서 설명한다.
  * [IoC Container:Java-based configuration](./ioc-container-java-based_configuration.md/)
    Java Annotation을 기반으로 Container를 구성하는 방법을 설명한다.
  * [Ioc Container:Environment Abstraction](./ioc-container-environment_abstraction.md/)
    환경 설정을 추상화하는 방법을 설명한다.

## 참고자료
  * [The Spring Framework - Reference Documentation / 1. The IoC Container](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans)
  * [Inversion of Control](http://martinfowler.com/bliki/InversionOfControl.html)
  * [Inversion of Control Containers and the Dependency Injection pattern](http://martinfowler.com/articles/injection.html)
  * [|Inversion of Control Containers and the Dependency Injection pattern 한글 번역](http://javacan.tistory.com/entry/120) by [최범균(Blog 자바캔(Java Can Do It))](http://javacan.tistory.com)
