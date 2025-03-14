---
title: "Annotation-based Configuration"
linkTitle: "Annotation"
description: "Spring Framework는 의존성 주입을 위해 어노테이션을 사용할 수 있다. Spring 2.0에서는 @Required 어노테이션으로 필수 속성을 강제하는 기능이 도입되었고, Spring 2.5에서는 일반적인 어노테이션 기반 의존성 주입이 가능해졌다. Spring 3.0부터는 JSR-330(Java용 의존성 주입)의 @Inject 및 @Named와 같은 어노테이션도 지원된다."
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-annotation-based_configuration/"
menu:
    depth:
        name: Annotation
        weight: 9
        parent: "ioc-container"
---
# Annotation-based configuration

## 개요

 Spring Framework는 Spring의 종속성 삽입을 위해 annotation을 사용할 수 있다. Spring 2.0에서는 @Required 어노테이션으로 필수 속성을 강제할 수 있는 기능이 도입되었고 Spring 2.5에서는 이와 동일한 일반적인 접근 방식을 따라 Spring의 의존성 주입을 구동할 수 있게 되었으며, Spring 3.0부터 @Inject 및 @Named와 같이 javax.inject 패키지에 포함된 JSR-330(Java용 의존성 주입) 어노테이션에 대한 지원이 추가되었다.

## 설명

 Spring @Autowired annotation은 자동 엮음과 같은 기능을 제공하지만, 좀 더 세밀한 제어와 넓은 사용성을 제공한다. Spring Framework는 @Resource, @PostConstruct, @PreDestroy 등의 JSR-250 annotation도 지원한다. 이들 annotation을 사용하기 위해서는 Spring Container에 특정 BeanPostProcessors를 등록해야만 한다. 항상 그렇듯이, 이들 BeanPostProcessors가 개별적인 bean 정의로 등록될 수도 있지만, 'context' namespace를 사용하여 등록할 수도 있다.

 ```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd">
 
    <context:annotation-config/>
</beans>
```

 (위 &lt;context:annotation-config/&gt; tag를 사용하면, AutowiredAnnotationBeanPostProcessor, CommonAnnotationBeanPostProcessor, PersistenceAnnotationBeanPostProcessor, RequiredAnnotationBeanPostProcessor를 등록해 준다.)

### @Required

 @Required annotation은 bean property setter 메소드에 적용된다.

 ```java
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Required
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

 이 annotation은 단순히 bean property가 설정 시 반드시 설정되어야만 한다는 것을 나타낸다. 즉, bean 정의에 명시적으로 property 값을 선언하거나 자동 엮임을 통해서 설정되어야만 한다는 것을 의미한다. 만약 annotation이 적용된 bean property에 대한 설정이 이루어지지 않는 경우, Container는 exception을 던진다.

### @Autowired

 @Autowired annotation은 “전통적인” setter 메소드에 적용된다.

 ```java
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Autowired
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

 뿐만 아니라, 임의의 이름과 다수의 argument를 가진 메소드에도 적용될 수 있다.

 ```java
public class MovieRecommender {
    private MovieCatalog movieCatalog;
 
    private CustomerPreferenceDao customerPreferenceDao;
 
    @Autowired
    public void prepare(MovieCatalog movieCatalog, CustomerPreferenceDao customerPreferenceDao) {
        this.movieCatalog = movieCatalog;
        this.customerPreferenceDao = customerPreferenceDao;
    }
 
    // ...
}
```

 또한, @Autowired annotation은 생성자 및 field에도 적용될 수 있다.

 ```java
public class MovieRecommender {
    @Autowired
    private MovieCatalog movieCatalog;
 
    private CustomerPreferenceDao customerPreferenceDao;
 
    @Autowired
    public MovieRecommender(CustomerPreferenceDao customerPreferenceDao) {
        this.customerPreferenceDao = customerPreferenceDao;
    }
 
    // ...
}
```

 또한, array 타입의 field나 메소드에 적용함으로써, ApplicationContext에 존재하는 특정 Type의 모든 bean을 field나 메소드에 제공하는 것도 가능한다.

 ```java
public class MovieRecommender {
 
    @Autowired
    private MovieCatalog[] movieCatalogs;
 
    // ...
}
```

 Typed collections에도 같은 방식이 적용된다.

 ```java
public class MovieRecommender {
    private Set<MovieCatalog> movieCatalogs;
 
    @Autowired
    public void setMovieCatalogs(Set<MovieCatalog> movieCatalogs) {
        this.movieCatalogs = movieCatalogs;
    }
 
    // ...
}
```

 심지어 typed Map 역시 key 타입이 String인 한 자동 엮임이 가능하다. Map은 기대한 타입의 모든 bean을 value로 갖게 되고, key는 해당하는 bean의 이름이 된다.

 ```java
public class MovieRecommender {
    private Map<String, MovieCatalog> movieCatalogs;
 
    @Autowired
    public void setMovieCatalogs(Map<String, MovieCatalog> movieCatalogs) {
        this.movieCatalogs = movieCatalogs;
    }
 
    // ...
}
```

기본적으로, 자동 엮임은 대상이 되는 bean이 없을 경우 실패한다. 기본적으로 annotation이 적용된 메소드, 생성자, field는 필수로 간주한다. 아래와 같이 설정하여 기본 행동 방식을 변경할 수 있다.

 ```java
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Autowired(required=false)
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
 
    // ...
}
```

 @Autowired annotation은 잘 알려진 “분석가능한 종속성(resolvable dependencies)“에도 사용될 수 있다 : BeanFactory interface, ApplicationContext interface, ResourceLoader interface, ApplicationEventPublisher interface, MessageSource interface(그리고 이들을 상속한 ConfigurableApplicationContext 또는 ResourcePatternResolver interface)는 특별한 설정 없이 자동적으로 해결(resolve)된다.

### Qualifier를 사용한 annotation 기반의 자동 엮음(Fine-tuning annotation-based autowiring with qualifiers)

 Type을 이용한 자동 엮기는 대상이 다수가 발생할 수 있기 때문에, 선택 시 추가적인 제어가 필요하다. 한 방법으로 Spring의 @Qualifier annotation을 사용할 수 있다. 특정 argument를 qualifier와 관련시킴으로써, 타입을 찾을 대상을 좁히고, 각 argument에 해당하는 대상 bean을 선택할 수 있다.

 ```java
public class MovieRecommender {
 
    @Autowired
    @Qualifier("main")
    private MovieCatalog movieCatalog;
 
    // ...
}
```

 @Qualifier annotation은 생성자의 argument 및 메소드의 parameter 각각에 적용할 수 있다.

 ```java
public class MovieRecommender {
 
    private MovieCatalog movieCatalog;
 
    private CustomerPreferenceDao customerPreferenceDao;
 
    @Autowired
    public void prepare(@Qualifier("main") MovieCatalog movieCatalog, CustomerPreferenceDao customerPreferenceDao) {
        this.movieCatalog = movieCatalog;
        this.customerPreferenceDao = customerPreferenceDao;
    }
 
    // ...
}
```

 일치하는 bean 정의는 아래 예제에서 찾을 수 있다. Qualifier “main” 값을 가진 bean이 같은 값의 @Qualifier annotation이 있는 생성자 argument로 엮인다.

 ```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd">
 
    <context:annotation-config/>
 
    <bean class="example.SimpleMovieCatalog">
        <qualifier value="main"/>
        <!-- inject any dependencies required by this bean -->
    </bean>
 
    <bean class="example.SimpleMovieCatalog">
        <qualifier value="action"/>
        <!-- inject any dependencies required by this bean -->
    </bean>
 
    <bean id="movieRecommender" class="example.MovieRecommender"/>
 
</beans>
```

 대체 수단으로, bean 이름을 qualifier로 간주된다. 즉, qualifier element 대신 bean id가 “main”이라면 동일하게 동작한다. 어쨌든, 이름으로 bean을 찾는게 더 좋지만, @Autowired는 기본적으로 type을 기반으로 동작하고 qualifier는 선택적이다. 즉, 타입으로 bean 대상을 줄인 후에 qualifier 또는 bean name으로 대상을 좁힌다. Qualifier 값은 의미적으로 유일한 bean id를 나타내지는 않는다. 좋은 qualifier 값은 “main”, “EMEA”, “persistent” 등과 같이 bean id가 아닌 특정 컴포넌트의 특징을 표현하는 것이다. Qualifier는 typed collection에도 적용된다.

### @Resource

 Spring은 field나 bean property setter 메소드에 적용된 JSR-250 @Resource annotation을 사용하여 종속성 삽입을 지원한다. @Resource는 'name' attribute를 가지고, Spring은 그 값을 삽입할 bean 이름으로 인식한다.

 ```java
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Resource(name="myMovieFinder")
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
}
```

 만약 name이 명식적으로 설정되어 있지 않으면, field나 setter 메소드의 이름으로부터 name 값을 유추해낸다. Field의 경우, field 명과 같다. Setter 메소드의 경우, bean property 이름과 같다. 아래 예제에서는 “movieFinder” bean이 삽입된다.

 ```java
public class SimpleMovieLister {
    private MovieFinder movieFinder;
 
    @Resource
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
}
```

 @Autowired와 비슷하게, @Resource도 대안으로 bean type으로 대상을 찾는다. 뿐만 아니라 잘 알려진 “resolvable dependencies”로 해결한다. 둘 다 명시적으로 name을 설정하지 않은 경우 적용된다. 다음 예에서 customerPreferenceDao field를 위해서 “customerPreferenceDao” 이름을 가진 bean을 먼저 찾는다. 그 다음으로 CustomerPreferenceDao Type의 bean을 찾는다. “context” field는 알려진 해결가능한 종속성 type인 ApplicationContext에 기반하여 삽입된다.

 ```java
public class MovieRecommender {
    @Resource
    private CustomerPreferenceDao customerPreferenceDao;
 
    @Resource
    private ApplicationContext context;
 
    public MovieRecommender() {
    }
 
    // ...
}
```

### @PostConstrutor와 @PreDestroy

 CommonAnnotationBeanPostProcessor는 @Resource annotation 뿐 아니라 JSR-250 ***lifecycle*** annotation 역시 인식한다.

 ```java
public class CachingMovieLister {
    @PostConstruct
    public void populateMovieCache() {
        // populates the movie cache upon initialization...
    }
 
    @PreDestroy
    public void clearMovieCache() {
        // clears the movie cache upon destruction...
    }
}
```

## 참고자료

- [Spring Framework - Reference Document / 1.9. Annotation-based Container Configuration](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-annotation-config)