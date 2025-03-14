---
title: "Customizing the nature of a Bean"
linkTitle: "Customizing"
description: Spring에서 Bean의 라이프사이클 관리를 위해 `InitializingBean`과 `DisposableBean` 인터페이스를 구현할 수 있다. 컨테이너는 빈이 초기화될 때 `afterPropertiesSet()` 메서드를, 소멸될 때 `destroy()` 메서드를 호출하여 특정 작업을 수행하도록 한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-customizing_the_nature_of_a_bean/"
menu:
    depth:
        name: Customizing
        weight: 4
        parent: "ioc-container"
---
# Customizing the nature of a bean

## 개요

 컨테이너의 빈 라이프사이클 관리와 상호 작용하기 위해 Spring InitializingBean 및 DisposableBean 인터페이스를 구현할 수 있는데, 컨테이너는 전자의 경우 afterPropertiesSet()을 호출하고 후자의 경우 destroy()를 호출하여 빈이 초기화 및 소멸될 때 특정 작업을 수행하도록 한다.

## 설명

### Lifecycle callbacks

 Spring Framework는 Container 내부의 bean의 행동을 변화시길 수 있는 다양한 callback interface를 제공한다.

#### 객체화 callbacks(Initialization callbacks)

 org.springframework.beans.factory.InitializingBean interface를 구현하면 bean에 필요한 모든 property를 설정한 후, 초기화 작업을 수행한다. InitializingBean interface는 다음 메소드를 명시하고 있다.

 ```java
void afterPropertiesSet() throws Exception;
```

 일반적으로, InitializingBean interface의 사용을 권장하지 않는다. 왜냐하면 code가 불필요하게 Spring과 결합되기(couple) 때문이다. 대안으로, bean 정의는 초기화 메소드를 지정할 수 있다. XML 기반 설정의 경우, 'init-method' attribute를 사용한다.

 ```xml
<bean id="exampleInitBean" class="examples.ExampleBean" init-method="init"/>
```

 ```java
public class ExampleBean {
    public void init() {
        // do some initialization work
    }
}
```

 위 예제는 아래 예제와 같다.

 ```xml
<bean id="exampleInitBean" class="examples.AnotherExampleBean"/>
```

 ```java
public class AnotherExampleBean implements InitializingBean {
    @Override
    public void afterPropertiesSet() {
        // do some initialization work
    }
}
```

#### 파괴 callbacks(Destruction callbacks)

 org.springframework.beans.factory.DisposableBean interface를 구현하면, Container가 파괴될 때 bean이 callback를 받을 수 있다. DisposableBean interface는 다음 메소드를 명시하고 있다.

 ```java
void destroy() throws Exception;
```

 일반적으로, DisposableBean interface의 사용을 권장하지 않는다. 왜냐하면 code가 불필요하게 Spring과 결합되기(couple) 때문이다. 대안으로, bean 정의는 초기화 메소드를 지정할 수 있다. XML 기반 설정의 경우, 'destroy-method' attribute를 사용한다.

 ```xml
<bean id="exampleInitBean" class="examples.ExampleBean" destroy-method="cleanup"/>
```

 ```java
public class ExampleBean {
    public void cleanup() {
        // do some destruction work (like releasing pooled connections)
    }
}
```

 위 예제는 아래 예제와 같다.

 ```xml
<bean id="exampleInitBean" class="examples.AnotherExampleBean"/>
```

 ```java
public class AnotherExampleBean implements DisposableBean {
    @Override
    public void destroy() {
        // do some destruction work (like releasing pooled connections)
    }
}
```

#### 기본 객체화 및 파괴 메소드(Default initialization & destroy methods)

 Spring Container는 모든 bean에 대해서 같은 이름의 초기화 및 파괴 메소드를 지정할 수 있다.

 ```java
public class DefaultBlogService implements BlogService {
    private BlogDao blogDao;
 
    public void setBlogDao(BlogDao blogDao) {
        this.blogDao = blogDao;
    }
 
    // this is (unsurprisingly) the initialization callback method
    public void init() {
        if (this.blogDao == null) {
            throw new IllegalStateException("The [blogDao] property must be set.");
        }
    }
}
```

 ```xml
<beans default-init-method="init">
    <bean id="blogService" class="com.foo.DefaultBlogService">
        <property name="blogDao" ref="blogDao" />
    </bean>
</beans>
```

 &lt;beans/&gt; element의 'default-init-method' attribute를 이용하여 기본 객체화 callback 메소드를 지정할 수 있다. 파괴 callback 메소드의 경우 'default-destroy-method' attribute를 이용하여 지정할 수 있다.

 &lt;bean/&gt; element에 'init-method', 'destroy-method' attribute가 정의되어 있는 경우, 기본값은 무시된다.

#### 생명주기 메커니즘 병합

 Spring Framework에서는 3가지 방식의 생명주기 메커니즘이 존재한다: InitialzingBean과 DisposableBean interface; 맞춤 init()과 destroy() 메소드; 그리고 [@PostConstruct and @PreDestroy annotations](./ioc-container-annotation-based_configuration.md#postconstrutor와-predestroy)

 만약 서로 다른 생명주기 메커니즘을 같이 사용할 경우, 개발자는 적용되는 순서를 알고 있어야 한다. 객체화 메소드의 순서는 다음과 같다.

1.  @PostConstruct annotation이 있는 메소드
    
2.  InitializingBean callback interface에 정의된 afterPropertiesSet()
    
3.  맞춤 init() 메소드
    

 파괴 메소드의 호출 순서는 다음과 같다.

1.  @PreDestroy annotation이 있는 메소드
    
2.  DisposableBean callback interface에 정의된 destroy()
    
3.  맞춤 destroy() 메소드
    

#### 시작 및 종료 callbacks(Startup and Shutdown Callbacks)

 Lifecycle 인터페이스는 자체 수명 주기 요구 사항(예: 일부 백그라운드 프로세스 시작 및 중지)이 있는 모든 객체에 대해 필수 메서드를 정의할 수 있다.

 ```java
public interface Lifecycle {
    void start();
 
    void stop();
 
    boolean isRunning();
}
```

 모든 Spring 관리 객체는 Lifecycle 인터페이스를 구현할 수 있다. 그런 다음 애플리케이션 컨텍스트 자체가 시작 및 중지 신호를 수신하면(예: 런타임에 중지/재시작 시나리오의 경우) 해당 컨텍스트 내에 정의된 모든 Lifecycle 구현으로 해당 호출을 캐스케이드한다.

 ```java
public interface LifecycleProcessor extends Lifecycle {
    void onRefresh();
 
    void onClose();
}
```

## 참고자료

*   [Spring Framework - Reference Document / 1.6 Customizing the nature of a bean](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-factory-nature)