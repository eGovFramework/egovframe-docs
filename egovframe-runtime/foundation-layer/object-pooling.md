---
title: Object Pooling Service
linkTitle: "Object Pooling"
description: Object Pooling 서비스는 객체를 미리 생성해 Pool에서 재사용하여 성능을 향상시키는 방식이다. **ObjectPool** 인터페이스는 객체 할당과 반환을 처리하며, **PooledObjectFactory**는 객체의 생성, 유효성 검사, 재초기화 등의 생애주기 관리를 담당한다. **BaseObjectPool**과 **BasePooledObjectFactory**는 이들을 추상적으로 구현한 클래스들로, 다양한 객체 풀링을 지원한다.
url: /egovframe-runtime/foundation-layer/object-pooling/
menu:
    depth:
        name: Object Pooling
        weight: 11
        parent: "foundation-layer"
---
# Object Pooling Service

## 개요

객체에 대한 Pooling 기능을 제공하는 서비스이다. 객체의 생성 비용이 크고,생성 횟수가 많으면, 평균적으로 사용되는 객체의 수가 적은 경우,성능을 향상시키기 위해서 사용한다.
**Object Pool**은 소프트웨어 디자인 패턴으로서, 객체를 필요에 따라 생성하고 파괴하는 방식이 아닌,적절한 개수의 객체를 미리 사용 가능한 상태로 생성하여 이를 이용하는 방식이다.Client는 Pool에 객체를 요청하여 객체를 얻은 후, 업무를 수행한다. 얻어온 객체를 이용하여 업무 수행을 끝마친 후, 객체를 파괴하는 것이 아니라 Pool에게 돌려주어 다른 Client가 사용할 수 있도록 한다. **Object Pooling**은 객체 생성 비용이 크고,객체 생성 횟수가 많으며,평균적으로 사용되는 객체의 수가 적은 경우,높은 성능의 향상을 가져다 준다.

## 설명

### ObjectPool

**ObjectPool**은 아래와 같은 interface이다.

```java
public interface ObjectPool {
    Object borrowObject();
    void returnObject(Object borrowed);
}
```

[ObjectPool](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/ObjectPool.html) interface를 구현하여 코드를 작성하여 사용한다.


#### BaseObjectPool

**ObjectPool**을 구현한 추상 클래스이다.

```java
public abstract class BaseObjectPool<T> implements ObjectPool<T> {
 
    public abstract T borrowObject() throws Exception;
    public abstract void returnObject(T obj) throws Exception;
    public abstract void invalidateObject(T obj) throws Exception;
 
    public int getNumIdle() throws UnsupportedOperationException {
        return -1;
    }
 
    public int getNumActive() throws UnsupportedOperationException {
        return -1;
    }
 
    public void clear() throws Exception, UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }
 
    public void addObject() throws Exception, UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }
 
    public void close() {
        closed = true;
    }
 
    protected final boolean isClosed() {
        return closed;
    }
 
    protected final void assertOpen() throws IllegalStateException {
        if(isClosed()) {
            throw new IllegalStateException("Pool not open");
        }
    }
 
    private volatile boolean closed = false;
}
```

|  METHOD           |  설 명              |
|-------------------|-------------------|
| borrowObject      |  객체 할당            |
| returnObject      |  객체 반환            |
| invalidateObject  |  객체 할당 시 유효성검사     |
| getNumIdle        |  Idle 상태 객체 수 리턴   |
| getNumActive      |  Active 상태 객체 수 리턴 |
| clear             |  객체 삭제            |
| addObject         |  Pool에 객체 추가      |
| isClosed          |  객체 close여부 판단    |
| assertOpen        |  객체가 사용가능한 상태판단   |

#### KeyedObjectPool

[KeyedObjectPool](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/KeyedObjectPool.html)은 이기종(異機種) 객체들로 구성된 pool 구현을 위한 interface

```java
public interface KeyedObjectPool {
    Object borrowObject(Object key);
    void returnObject(Object key, Object borrowed);
}
```

|  METHOD       |  설 명   |
|---------------|--------|
| borrowObject  |  객체 할당 |
| returnObject  |  객체 반환 |

### PooledObjectFactory

**org.apache.commons.pool** package는 Object Pool객체 생성과 pool로부터 생성되는 object의 created와 destoryed 부분을 분리하여 구현 할 수 있도록 지원한다. **PooledObjectFactory**는 pooled object의 생존주기 관리를 위한 interface이다.

```java
public interface PooledObjectFactory<T> {
  PooledObject<T> makeObject() throws Exception;
  void destroyObject(PooledObject<T> p) throws Exception;
  boolean validateObject(PooledObject<T> p);
  void activateObject(PooledObject<T> p) throws Exception;
  void passivateObject(PooledObject<T> p) throws Exception;
```

|  METHOD          |  설 명                                    |
|------------------|-----------------------------------------|
| makeObject       |  객체 생성                                  |
| activateObject   |  Pool로 부터 객체를 할당 받을 때 호출된다(재초기화 할 때 이용).  |
| passivateObject  |  Pool로 객체를 반환할 때 호출된다(초기화 할 때 이용).       |
| validateObject   |  객체가 유효한지 측정하기 위해 호출된다.                 |
| destroyObject    |  객체를 삭제할 때 호출된다.                         |

ObjectPool 구현한 프로그램은 PoolableObjectFactory를 구현한 프로그램을 받아들이도록 구현한다면, 다양하고 독특한 ObjectPool을 구현 할 수 있다.

#### BasePooledObjectFactory

**PooledObjectFactory**를 구현한 추상 클래스이다.

```java
public abstract class BasePooledObjectFactory<T> implements PooledObjectFactory<T> {
 
    public abstract T create() throws Exception;
 
    public abstract PooledObject<T> wrap(T obj);
 
    @Override
    public PooledObject<T> makeObject() throws Exception {
        return wrap(create());
    }
 
    @Override
    public void destroyObject(PooledObject<T> p)
        throws Exception  {
    }
 
    @Override
    public boolean validateObject(PooledObject<T> p) {
        return true;
    }
 
    @Override
    public void activateObject(PooledObject<T> p) throws Exception {
    }
 
    @Override
    public void passivateObject(PooledObject<T> p)
        throws Exception {
    }
}
```

#### KeyedPooledObjectFactory

**KeyedObjectPools**를 위한 **PooledObjectFactory**이다.

```java
public interface KeyedPooledObjectFactory<K,V> {
    PooledObject<V> makeObject(K key) throws Exception;
    void destroyObject(K key, PooledObject<V> p) throws Exception;
    boolean validateObject(K key, PooledObject<V> p);
    void activateObject(K key, PooledObject<V> p) throws Exception;
    void passivateObject(K key, PooledObject<V> p) throws Exception;
}
```

|  METHOD          |  설 명                                    |
|------------------|-----------------------------------------|
| makeObject       |  객체 생성                                  |
| activateObject   |  Pool로 부터 객체를 할당 받을 때 호출된다(재초기화 할 때 이용).  |
| passivateObject  |  Pool로 객체를 반환할 때 호출된다(초기화 할 때 이용).       |
| validateObject   |  객체가 유효한지 측정하기 위해 호출된다.                 |
| destroyObject    |  객체를 삭제할 때 호출된다.                         |

#### BaseKeyedPoolableObjectFactory

**KeyedPoolableObjectFactory**를 구현한 추상 클래스이다.

```java
public abstract class BaseKeyedPooledObjectFactory<K,V>
        implements KeyedPooledObjectFactory<K,V> {
 
    public abstract V create(K key)
        throws Exception;
 
    public abstract PooledObject<V> wrap(V value);
 
    @Override
    public PooledObject<V> makeObject(K key) throws Exception {
        return wrap(create(key));
    }
 
    @Override
    public void destroyObject(K key, PooledObject<V> p)
        throws Exception {
    }
 
    @Override
    public boolean validateObject(K key, PooledObject<V> p) {
        return true;
    }
 
    @Override
    public void activateObject(K key, PooledObject<V> p)
        throws Exception {
    }
 
    @Override
    public void passivateObject(K key, PooledObject<V> p)
        throws Exception {
    }
}
```