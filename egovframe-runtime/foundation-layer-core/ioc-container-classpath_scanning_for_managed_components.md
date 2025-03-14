---
title: "Classpath Scanning for Managed Components"
linkTitle: "Components Scan"
description: 이전의 대부분 예제들은 Spring Container에서 `BeanDefinition`을 생성하기 위한 설정 메타데이터로 XML을 사용했다. 이전 섹션에서는 소스 레벨의 어노테이션을 사용해 많은 설정 메타데이터를 제공할 수 있음을 보여주었다. 그러나 이 예제들에서도 기본적인 bean 정의는 여전히 XML 파일에 명시적으로 작성되었다. 이번 섹션에서는 classpath를 검색하고 filter를 사용해 대상 컴포넌트(candidate component) 를 검출하는 방법을 소개한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-classpath_scanning_for_managed_components/"
menu:
    depth:
        name: Components Scan
        weight: 10
        parent: "ioc-container"
---
# Classpath scanning for managed components

## 개요

본 장의 앞선 대부분의 예제들은 Spring Container 안에서 BeanDefinition을 생성하기 위한 설정 메타데이터를 명기하기 위해서 XML을 사용해왔다. 이전 section [Annotaion-based configuration](./ioc-container-annotation-based_configuration.md)은 source-level annotation을 사용하여 많은 양의 설정 메타데이터를 제공할 수 있음을 보였다. 이들 예제에서도 어쨌든, “base” bean 정의가 XML 파일 안에 명시적으로 정의되었다. 이번 section은 classpath를 검색하고, ***filter***를 통해 검사함으로써,
***대상 컴퍼넌트(candidate component)*** 를 검출하는 방법을 소개한다.

## 설명

### @Component and further stereotype annotations

 Spring 2.0부터 Data Access Object(DAO) 등과 같은 repository를 표시하기 위해서 @Repository annotation이 소개되었다. Spring 2.5는 추가적으로 @Component, @Service, @Controller annotation을 제공한다. @Component는 Spring이 관리하는 컴포넌트를 위한 포괄적인 stereotype을 나타낸다. 그리고 @Repository, @Service, @Controller는 좀 더 특별한 사용을 위한 @Component의 일종이다. (각각 persistence, service, presentation layer의 component를 의미한다.)

### Auto-detection Components

 Spring은 'stereotyped' class를 자동으로 탐지하고 ApplicationContext에 일치하는 BeanDefinition을 등록하는 기능을 제공한다. 아래 두 class는 자동 탐지의 대상이 된다.

 ```java
@Service
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Autowired
    public SimpleMovieLister(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
}
```

 ```java
@Repository
public class JpaMovieFinder implements MovieFinder {
    // implementation elided for clarity
}
```

 실제로 위 두 class를 자동 탐지하고 상응하는 bean을 등록하기 위해서는, 아래 예제 XML의 &lt;context:component-scan/&gt; element의 'basePackage'가 위 두 class의 공통 부모 package이어야 한다(또는 comma(',')로 구분된 list 역시 가능하다).

 ```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd">
 
    <context:component-scan base-package="org.example"/>
 
</beans>
```

### Naming autodetected components

 검색 과정에서 component가 자동 탐지되었을 때, bean 이름은 scan하고 있는 BeanNameGenerator 전략에 따라 생성된다. 기본적으로 name 값을 가지고 있는 Spring 'stereotype' annotation(@Component, @Repository, Service, Controller)는 상응하는 bean 정의에게 이름을 제공한다. 만약 이들 annotation이 name이 없거나 또 다른 탐지된 component인 경우, 기본 bean name generator는 class 이름의 첫 문자를 소문자로 변환한 값을 return할 것이다. 예를 들어, 아래 예제에서 두개의 component가 탐지되는데 각각의 이름은 'myMovieLister'와 'movieFinderImpl'이다.

 ```java
@Service("myMovieLister")
public class SimpleMovieLister {
    // ...
}
```

 ```java
@Repository
public class MovieFinderImpl implements MovieFinder {
    // ...
}
```

### Providing a scope for autodetected components

 일반적으로 Spring 관리 component는 'singleton'이다. 어쨌든 다른 scope이 필요한 경우가 있다. Spring Framework는 @Scope annotation을 제공한다.

 ```java
@Scope("prototype")
@Repository
public class MovieFinderImpl implements MovieFinder {
    // ...
}
```

### Providing qualifier metadata with annotations

 이번 section에서는 자동 엮임의 대상을 찾을 때 상세한 제어를 제공하기 위해 @Qualifier annotation을 사용하는 방법을 설명한다.

 ```java
@Component
@Qualifier("Action")
public class ActionMovieCatalog implements MovieCatalog {
    // ...
}
```

## 참고자료

- [Spring Framework - Reference Document / 1.10 Classpath scanning and managed components](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-classpath-scanning)