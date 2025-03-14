---
title: JSR 330 표준 어노테이션 사용하기
linkTitle: "JSR 330"
description: Spring 3.0부터 JSR-330 표준 의존성 주입 어노테이션을 지원하며, 이를 사용하려면 클래스패스에 javax.inject 라이브러리를 추가해야 한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-jsr_330_standard_annotations/"
menu:
    depth:
        name: JSR 330
        weight: 11
        parent: "ioc-container"
---
# JSR 330 표준 어노테이션 사용하기

## 개요

 스프링 3.0부터 JSR-330 표준 어노테이션(의존성 주입)을 지원한다. 이 어노테이션들은 스프링 어노테이션들과 같은 방법으로 스캔된다. 이 어노테이션들을 사용하기 위해서는 클래스패스에 관련 jar 파일들을 가지고 있어야 한다.  
Maven을 사용한다면 Maven Repository([https://mvnrepository.com/artifact/javax.inject/javax.inject/1](https://mvnrepository.com/artifact/javax.inject/javax.inject/1))에서 javax.inject라는 아티펙트가 제공된다. pom.xml 파일에 아래의 의존성을 추가하여 사용할 수 있다.

 ```xml
<dependency>
    <groupId>javax.inject</groupId>
    <artifactId>javax.inject</artifactId>
    <version>1</version>
</dependency>
```

## 설명

### 1\. @Inject 와 @Named 를 이용한 의존성 주입

 @Autowired를 대신하여 @javax.inject.Inject를 아래와 같이 사용할 수 있다.

 ```java
import javax.inject.Inject;
 
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Inject
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    public void listMovies() {
        this.movieFinder.findMovies(...);
        // ...
    }
}
```

 @Autowired와 같이 @Inject를 필드 수준, 함수 수준, 생성자 인자 수준으로 사용할 수 있고, 주입 지점을 Provider로 선언할 수 있으며 Provider.get() 호출을 통해 근접 범위의 Bean들에 대한 요청 시 접근 또는 다른 Bean에 대한 지연된 접근을 허용할 수 있다.

 ```java
import javax.inject.Inject;
import javax.inject.Provider;
 
public class SimpleMovieLister {
    private Provider<MovieFinder> movieFinder;
 
    @Inject
    public void setMovieFinder(Provider<MovieFinder> movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    public void listMovies() {
        this.movieFinder.get().findMovies(...);
        // ...
    }
}
```

 주입될 의존성에 대해 지정된 이름을 사용하고자 할 경우에는 아래와 같이 @Named 어노테이션을 사용할 수 있다.

 ```java
import javax.inject.Inject;
import javax.inject.Named;
 
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Inject
    public void setMovieFinder(@Named("main") MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

### 2\. @Component 어노테이션과 동일한 표준인 @Named, @ManagedBean 어노테이션

 @Component를 대신하여, @javax.inject.Named나 javax.annotation.ManagedBean를 아래와 같이 사용할 수 있다.

 ```java
import javax.inject.Inject;
import javax.inject.Named;
 
@Named("movieListener")  // @ManagedBean("movieListener") could be used as well
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Inject
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

 일반적으로 컴포넌트에 대한 이름을 명시하지 않고 @Component를 사용할 수 있는데, 아래 예제처럼 @Named도 비슷하게 사용할 수 있다.

 ```java
import javax.inject.Inject;
import javax.inject.Named;
 
@Named
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Inject
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

 @Named나 @ManagedBean을 사용할 때 아래 예제에서 보여주는 것처럼 스프링 어노테이션과 같이 동일한 방법으로 컴포넌트 탐색이 가능하다.

 ```java
@Configuration
@ComponentScan(basePackages = "org.example")
public class AppConfig  {
    // ...
}
```

### 3\. JSR-330 표준 어노테이션의 제한점

 표준 어노테이션으로 작업할 때 아래 표와 같이 일부 중요한 기능이 사용 불가능하다.

| Spring | javax.inject.\* | javax.inject 제한 및 비고 |
| --- | --- | --- |
| @Autowired | @Inject | @Inject는 required 속성이 없다. 자바 8의 Optional을 대신 사용할 수 있다. |
| @Component | @Named / @ManagedBean | JSR-330은 조합구성을 제공하지 않기 때문에 명명된 컴포넌트만 식별해야 한다. |
| @Scope(“singleton”) | @Singleton | JSR-330의 기본범위는 스프링의 prototype 같으나 스프링의 일반 기본값과 일관성을 유지하기 위해 스프링 컨테이너에 선언된 JSR-330 빈은 기본적으로 singleton이다. Singleton이 아닌 다른 범위를 사용하려면 스프링의 @Scope 어노테이션을 사용해야 한다. javax.inject도 @Scope 어노테이션을 제공하지만 자체적 어노테이션을 생성할 때 사용한다. |
| @Qualifier | @Qualifier / @Named | javax.inject.Qualifier는 사용자 정의 한정자를 만들기 위한 메타 어노테이션으로 스프링의 값이 있는 @Qualifier 같은 구체적인 String으로 된 한정자는 javax.inject.Named로 연결할 수 있습니다. |
| @Value | \- | 동등한 것이 없음 |
| @Required | \- | 동등한 것이 없음 |
| @Lazy | \- | 동등한 것이 없음 |
| ObjectFactory | Provider | javax.inject.Provider는 짧은 get() 함수명만 있는 스프링의 ObjectFactory의 직접적 대안으로 사용할 수 있으며 스프링의 @Autowired, 어노테이션이 없는 생성자나 Setter 함수와 조합하여 사용될 수 있다. |

## 참고자료

- [Spring Framework - Reference Document / 1.11. Using JSR 330 Standard Annotations](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-standard-annotations)