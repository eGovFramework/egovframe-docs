---
title: Cache Abstraction
linkTitle: "Abstraction"
description: Cache를 설정하여 CacheManager를 통해 Cache에 접근하는 방법에 대하여 알아보고, 자바메소드를 Caching하는 @Cacheable에 대하여 알아본다.
url: /egovframe-runtime/foundation-layer/cache/abstraction/
menu:
    depth:
        name: Abstraction
        weight: 2
        parent: "cache"
---
# Cache Abstraction

## 개요

Spring 3.1부터 Cache Service는 Cache 추상화(CacheManager Interface)와 Cache 추상화를 Java메소드에 제공할 수 있는 @Cacheable을 제공한다. Cache 추상화는 Spring의 트랜잭션기능과 유사하게 코드의 변화를 최소화하면서 Proxy를 통해 동작하게끔 한다. Cache 구현체가 아닌 Cache추상화만을 제공하며 실제 Cache Data저장소는 EhCache와 ConcurrentMap을 지원한다.

- Cache Configuration
  - Cache설정을 통하여 어떠한 Cache Data저장소를 쓸 것인지 결정할 수 있다. (EhCache/ConcurrentMap)
- Cache Manager
  - CacheManager를 통해 설정과 상관없이 동일한 코드로 Cache에 접근할 수 있다.
- Cache Annotation
  - 메소드의 Cache Annotation을 통해 쉽게 Cache데이터를 저장/삭제할 수 있다.

## 설명

Cache를 설정하여 CacheManager를 통해 Cache에 접근하는 방법에 대하여 알아보고, 자바메소드를 Caching하는 @Cacheable에 대하여 알아본다.

### Cache Configuration

#### EhCache

- [EhCache](./cache-ehcache.md) 참조

Spring에서는 EhCache를 지원하는 CacheManager로써 EhCacheCacheManager를 제공한다. <EhCache 설정>

```xml
<cache:annotation-driven cache-manager="cacheManager" />
<!-- EhCache를 저장소로 사용하는 Cache Manager -->
 <bean id="cacheManager" class="org.springframework.cache.ehcache.EhCacheCacheManager">
<property name="cacheManager" ref="ehcache"></property>
</bean>
<!-- Ehcache library setup -->
<bean id="ehcache"
class="org.springframework.cache.ehcache.EhCacheManagerFactoryBean"
p:config-location="classpath:springframework/cache/ehcache/ehcache.xml" />
```

Ehcache.xml에서 defaultCache저장소와 추가 Cache저장소의 설정을 한다. EhCache는 비록 ConcurrentMap보다 속도는 느리지만 Cache관리기능 측면에서 유용하여 EhCache를 추천한다.
- 프로젝트에서는 Cache의 사용에 대하여 개발자의 가이드가 필요하다. 업무별/서비스별 Cache저장소를 분리하여 Cache데이터를 관리하도록 하며, 적용케이스에 대하여 가이드 하여야 한다.

`<ehcache.xml>`

```xml
<ehcache…> 
<defaultCache 
            maxElementsInMemory="10000"
            eternal="false"
            timeToIdleSeconds="120"
            timeToLiveSeconds="120"
            overflowToDisk="true"
            diskSpoolBufferSizeMB="30"
            maxElementsOnDisk="10000000"
            diskPersistent="false"
            diskExpiryThreadIntervalSeconds="120"
            memoryStoreEvictionPolicy="LRU"
            statistics="false"
            />
<cache name="ehcache"
           …>
```

#### ConcurrentMap

Spring에서는 ConcurrentMap을 지원하는 SimpleCacheManager를 제공한다.

`<CacheManager설정>`

```xml
<cache:annotation-driven cache-manager="cacheManager"/>
 <!-- ConcurrentMap을 저장소로 사용하는 Cache Manager -->
<bean id="cacheManager" class="org.springframework.cache.support.SimpleCacheManager"> 
   <property name="caches"> 
      <set> 
         <bean class="org.springframework.cache.concurrent.ConcurrentMapCacheFactoryBean" p:name="default"/>    
         <bean class="org.springframework.cache.concurrent.ConcurrentMapCacheFactoryBean" p:name="books"/>   
      </set> 
   </property> 
</bean>
```

#### Cache Annotation을 위한 annotation-driven 설정

Cache Annotation으로 Cache를 적용하기 위해서는 반드시 `<cache:annotatioin-driven>`을 붙여주어야한다. 이 네임스페이스는 AOP를 사용해서 캐시 기능을 다양한 방법으로 설정할 수 있는 옵션을 제공한다. 이 설정은 Transaction에 사용되는 `<tx:annotation-driven>`과 비슷하다.

|  속성                  |  기본값                        |  설명                                                                         |
|----------------------|-----------------------------|-----------------------------------------------------------------------------|
|  cache-manager       |  cacheManager               |  사용할 CacheManager의 이름. CacheManager의 Bean id가 cacheManager가 아닐 경우, 설정해야한다.  |
|  mode                |  proxy                      |  스프링 AOP를 사용하는 설정이며, “aspect”를 사용할 수도 있다.                                   |
|  proxy-target-class  |  false                      |  false인 경우, JDK의 인터페이스 기반 프록시를 사용한다. true를 사용하면 클래스 기반 프록시를 사용한다.           |
|  order               |  Ordered.LOWEST_PRECEDENCE  |  @Cacheable/@CacheEvict메소드의 Cache advice가 적용되는 순서                           |

- `<cache:annotation-driven/>`은 오로지 이것이 정의된 동일 ApplicationContext안의 bean에서 @Cacheable과 @CacheEvict을 찾는다. 즉, `<cache:annotation-driven>`을 DispatcherServlet을 위한 WebApplicationContext에 선언했을 때 @Cacheable/@CacheEvict는 controller내부에서만 식별된다.

### CacheManager를 통한 Cache접근

ehCache, concurrentMap의 설정과 상관없이 코드상으로 동일한 CacheManager인터페이스로 bean을 주입받아 사용할 수 있다.

`<CacheManager 의 사용>`

```java
import org.springframework.cache.CacheManager;
@Autowired 
private CacheManager cacheManager;
Cache cache = cacheManager.getCache("cache명");
```

### @Cacheable

자바 메소드에 `@Cacheable`을 설정함으로써 Caching할 수 있다. 타겟 메소드가 호출되었을 때, 캐시에 해당 메서드가 이미 동일한 인자로 있는지 확인하고, 만약 있다면 메소드를 호출하지 않고 캐시해둔 결과를 Proxy에서 반환하게 된다.

Java Method에 적용가능한 Cache Annotation은 다음과 같다.

- `@Cacheable`
  - Cache에 메소드 데이터를 생성한다.
- `@CacheEvict`
  - Cache에 메소드 데이터를 삭제한다.

#### @Cacheable 사용방법

별다른 조건 없이 호출되는 모든 인자를 caching하고자 할 때는 아래와 같이 cache명만 쓰면 된다. 이 코드는 Cache이름이 “books”인 cache저장소를 사용하였다. 메소드가 호출될 때 매번 “books”에 Cache데이터를 확인하고 이미 실행된 적이 있는지를 확인한다. 만약 “books”에 데이터가 있으면 그 값을 반환하게 된다.

##### 기본

```java
@Cacheable("books")
public Book findBook(ISBN isbn, boolean checkWarehouse, boolean includeUsed)
```

Cache되는 저장소를 여러 개 정의할 수도 있다. 아래의 코드에서는 findBook메소드 호출 시 “books”와 “isbns” 두 군데에 캐시데이터가 저장된다.

`<여러 cache 저장소에 caching>`

```java
@Cacheable({ "books", "isbns" })
public Book findBook(ISBN isbn) {...}
```

##### Cache Abstraction Key생성

Cache는 키-값으로 저장되며, 캐시된 메소드를 호출시마다 키를 통해 값을 가져오므로 캐시를 찾을 수 있는 키가 생성되어야 한다. 별도의 커스텀 키가 정의되지 않으면 default로 다음과 같은 알고리즘 기반의 KeyGenerator를 사용하여 Key를 생성한다.

- 매개변수가 아무것도 없으면 0을 반환한다.
- 매개변수가 하나면, 그 인스턴스를 반환한다.
- 매개변수가 둘 이상이면, 모든 매개변수의 Hash로 계산된 키를 반환한다.

이 외에 다른 기본키를 생성하려면 org.springframework.cache.KeyGenerator 인터페이스를 구현하면 된다.

##### Custom key 추가

`@Cacheable`을 적용한 메소드의 인자가 여러개일 때 Key로 사용할 것을 SpEL로 명시할 수 있다.

```java
@Cacheable(value="books", key="#isbn"
public Book findBook(ISBN isbn, boolean checkWarehouse, boolean includeUsed)
 
 
@Cacheable(value="books", key="#isbn.rawNumber")
public Book findBook(ISBN isbn, boolean checkWarehouse, boolean includeUsed)
 
 
@Cacheable(value="books", key="T(someType).hash(#isbn)")
public Book findBook(ISBN isbn, boolean checkWarehouse, boolean includeUsed)
```

##### Conditional 추가

Conditional을 주어서 그 값이 true이면 caching을 하고, false이면 caching을 하지 않기 때문에 호출 시 매번 메소드 내부가 실행된다. Conditional에서는 SpEL사용이 가능하며 Condition과 Unless를 쓸 수 있다. condition과는 달리 unless는 메소드의 결과값 반환 시점에 결과값을 확인하여 caching여부를 결정하게 된다.

```java
@Cacheable(value="book", condition="#name.length < 32")
public Book findBook(String name)
```
```java
@Cacheable(value="book", condition="#name.length < 32", unless="#result.hardback")
public Book findBook(String name)
```

Conditional에 쓰는 SpEL의 설명은 다음과 같다.

|  명칭             |  위치          | 설명                                                                                 |  예제                                  |
|-----------------|--------------|------------------------------------------------------------------------------------|--------------------------------------|
|  methodName     |  root객체      | 호출되는 메소드명                                                                          |  #root.methodName                    |
|  method         |  root객체      | 호출되는 메소드                                                                           |  #root.method.name                   |
|  target         |  root객체      | 호출되는 타겟 오브젝트                                                                       |  #root.target                        |
|  targetClass    |  root객체      | 호출되는 타겟 클래스                                                                        |  #root.targetClass                   |
|  args           |  root객체      | 타겟을 호출 시 사용되는 인자들(배열)                                                              |  #root.args[0]                       |
|  caches         |  root객체      | 현재 메소드가 실행되는 캐시들의 집합                                                               |  #root.caches[0].name                |
|  argument name  |  평가 context  | 메소드 인자명을 사용할 수 없을 때 대신 a&lt;#arg&gt;로 대체하여 사용할 수 있다. #arg는 0부터 시작하는 인자의 인덱스를 나타난다. |  iban 또는 a0  (p&lt;#arg&gt;로도 사용가능)  |
|  result         |  평가 context  | 메소드 호출 결과. unless와 cache evict표현에서만 사용가능하다.                                        |  #result                             |

### @CacheEvict

`@CacheEvict`는 `@Cacheable`과 반대로 cache저장소의 데이터를 제거함으로써 사용하지 않는 데이터를 정리하는데 유용하다. `@CacheEvict`는 캐시 삭제를 수행할 메서드에 선언한다. `@CacheEvict`도 여러 개의 캐시를 명시할 수 있으며, key와 condition을 사용할 수 있다. 또한 allEntries 속성은 키 값으로 Cache Entry 하나만 비우는 것이 아니라 캐시영역의 모든 Entries를 비우도록 한다. 이 경우에는 키를 명시하더라도 이를 무시하고 모든 Entries를 비우게 된다.

```java
@CacheEvict(value = "books", allEntries=true)
public void loadBooks(InputStream batch)
```

### @CachePut

메소드의 흐름을 방해하지 않고 Cache에 저장하거나 업데이트를 해야 하는 경우, `@CachePut`을 사용한다. 즉, 메소드는 항상 실행되고 그 결과가 캐시에 저장된다. `@CachePut`은 `@Cacheable`과 동일한 옵션을 제공하며, Cache에 저장하는 것보다는 메소드의 흐름을 최적화하는데 사용되어야 한다.

`@Cacheable`과 함께 사용하는 것은 일반적으로 권장하지 않는다.

### @Caching

다수의 Cache annotation을 쓰고자 할 때 `@Caching`을 쓴다. `@Cacheable`, `@CacheEvic`, `@CachePut`을 지원한다.

```java
@Caching(evict = { @CacheEvict("primary"), @CacheEvict(value = "secondary", key = "#p0") })
public Book importBooks(String deposit, Date date)
```

### XML기반 Caching설정

Java메소드에 Annotation을 붙이는 대신 XML로 caching할 메소드를 정의할 수 있다. 아래에서는 CacheManager bean설정을 생략하였다. BookService 패키지의 하위 메소드 중 findBook 메소드에 cacheable이 적용되며 loadBooks 메소드에 cacheEvict가 적용되었다.

```xml
<!-- the service we want to make cacheable -->
<bean id="bookService" class="x.y.service.DefaultBookService"/>
 
<!-- cache definitions -->
<cache:advice id="cacheAdvice" cache-manager="cacheManager">
    <cache:caching cache="books">
        <cache:cacheable method="findBook" key="#isbn"/>
        <cache:cache-evict method="loadBooks" all-entries="true"/>
    </cache:caching>
</cache:advice>
 
<!-- apply the cacheable behavior to all BookService interfaces -->
<aop:config>
    <aop:advisor advice-ref="cacheAdvice" pointcut="execution(* x.y.BookService.*(..))"/>
</aop:config>
...
// CacheManager설정 생략
```

## 참고자료

- [Spring Framework - Reference Document / cache](http://docs.spring.io/spring/docs/3.2.6.RELEASE/spring-framework-reference/htmlsingle/)
- [Spring Team Blog - Caching](https://spring.io/blog/2011/02/23/spring-3-1-m1-cache-abstraction)









































