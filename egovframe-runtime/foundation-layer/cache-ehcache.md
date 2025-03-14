---
title: EhCache
linkTitle: "EhCache"
description: 전자정부 프레임워크에서 EhCache를 사용한 캐시 서비스를 제공하며, Spring 3.1 이전에는 EhCache의 CacheManager를 직접 사용하고 이후 버전에서는 CacheManager Abstraction으로 캐시 사용을 유연하게 지원한다.
url: /egovframe-runtime/foundation-layer/cache/ehCache/
menu:
    depth:
        name: EhCache
        weight: 1
        parent: "cache"
---
# EhCache

## 개요

전자정부 프레임워크에서 Cache Service는 [EhCache](http://ehcache.sourceforge.net/)를 선정하여 가이드한다.

Spring 버전 3.1 이전에서는 EhCache에서 제공하는 CacheManager를 직접 사용한다. 3.1 이후 버전에서는 CacheManager Abstraction을 제공함으로써 Cache를 유연하게 사용할 수 있게 되었다. 아래에서는 EhCache의 설명과 Spring 3.1이전의 EhCache 사용법에 대하여 알아본다.

## 설명

EhCache를 이용하기 위한 기본 설정 및 기본 사용법에 대해서 설명한다.

### Bootstrap Source

Cache를 사용하기 위해서 Cache Manager를 생성하는 방법을 샘플을 통해서 설명한다.

```java
//클래스 패스를 이용하여 설정파일 읽어서 Cache Manager 생성하기.
URL url = getClass().getResource("/ehcache-default.xml");
manager = new CacheManager(url);
```

위에서 getResource를 통해서 읽어들이는 /ehcache-default.xml 의 파일 내용은 다음과 같다.

### Configuration

```xml
<ehcache>
<diskStore path="user.dir/second"/>
   <cache name="sampleMem"
           maxElementsInMemory="3"
           eternal="false"
           timeToIdleSeconds="360"
           timeToLiveSeconds="1000"
           overflowToDisk="false"
           diskPersistent="false"  
           memoryStoreEvictionPolicy="LRU">
   </cache>
</ehcache>
```

### Basic Usage Source

위에서 정의한 Cache Manager에서 Cache를 얻어서 기본적인 쓰고 읽고 지우는 것에 대한 샘플은 다음과 같다.

```java
// cache Name을 가지고 cache 얻기
Cache cache = manager.getCache("sampleMem");
 
// 1.Cache에 데이터 입력
cache.put(new Element("key1", "value1"));
 
// 2.Cache로부터 입력한 데이터 읽기
Element value = cache.get("key1");
 
// 3. Cache에서 데이터 삭제
cache.remove("key1");
```

- manager.getCache
  - Manager를 이용하여 해당하는 Cache 얻기
- cache.put
  - Cache에 자료 입력 ( 같은 키 값에 대해서 다른 value를 입력하면 수정처리됨 )
- cache.get
  - Cache에서 자료 읽기
- cache.remove
  - Cache에서 자료 삭제

## Cache Algorithm

Cache는 메모리를 이용하는 것을 기본으로 하기에 꼭 필요한 자료만을 관리하도록 보관 사이즈를 지정한다. 보관 사이즈를 넘어설 경우 불필요한 자료부터 삭제처리하는데, 필요한 자료에 대한 판단은 알고리즘을 통해서 한다. 지원되는 알고리즘은 LRU, FIFO, LFU 세 가지이고 각각에 대한 설정 및 사용법은 아래와 같다.

### LRU Algorithm

최근에 이용한 것을 남기는 알고리즘으로 설정은 아래와 같이 한다.

#### Configuration

```xml
<cache name="sampleMem"
        maxElementsInMemory="3"
        ...
        memoryStoreEvictionPolicy="LRU">
```

위의 설정에서 최대 보관 엔트리 갯수(maxElementsInMemory)는 3, 알고리즘은 LRU 로 설정된 것을 확인할 수 있다. 이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source 

```java
Cache cache = manager.getCache("sampleMem");
...
cache.get("key2");
cache.get("key2");
cache.get("key1");
cache.get("key1");
cache.get("key3");

// 4. Put New element in cache.
cache.put(new Element("key4", "value4"));    	

// 5. get key2 but can't key2 
assertNull("Can't get key2",cache.get("key2"));
```

### FIFO Algorithm

먼저 입력된것을 제거하는 알고리즘으로 설정은 아래와 같이 한다.

#### Configuration

```xml
<cache name="sampleMemFIFO"
        maxElementsInMemory="3"
        ...
        memoryStoreEvictionPolicy="FIFO">
```

위의 설정에서 최대 보관 엔트리 갯수(maxElementsInMemory)는 3, 알고리즘은 FIFO 로 설정된 것을 확인할 수 있다. 이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
   Cache cache = manager.getCache("sampleMemFIFO");
   cache.put(new Element("key1", "value1")); 
   cache.put(new Element("key2", "value2")); 
   cache.put(new Element("key3", "value3")); 
   ...
   cache.get("key2");
   cache.get("key2");
   cache.get("key1");
   cache.get("key1");
   cache.get("key3");
 
   // 4. Put New element in cache.
   cache.put(new Element("key4", "value4"));    	
 
   // 5. get key1 but can't key1 
   assertNull("Can't get key1",cache.get("key1"));
```

### LFU Algorithm

가장 적게 이용된 것을 제거하는 알고리즘으로 설정은 아래와 같이 한다.

#### Configuration

```xml
   <cache name="sampleMemLFU"
           maxElementsInMemory="3"
           ...
           memoryStoreEvictionPolicy="LFU">
```

위의 설정에서 최대 보관 엔트리 갯수(maxElementsInMemory)는 3, 알고리즘은 LFU 로 설정된 것을 확인할 수 있다. 이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
Cache cache = manager.getCache("sampleMemLFU");
cache.put(new Element("key1", "value1")); 
cache.put(new Element("key2", "value2")); 
cache.put(new Element("key3", "value3")); 
...
cache.get("key2");
cache.get("key2");
cache.get("key1");
cache.get("key1");
cache.get("key3");

// 4. Put New element in cache.
cache.put(new Element("key4", "value4"));    	

// 5. get key2 but can't key3 
assertNull("Can't get key3",cache.get("key3"));
```

## Cache Size & Device

Cache에서 관리해야 하는 정보의 사이즈 설정 및 저장 디바이스 관련 설정을 할 수 있다.

### Cache Device

디바이스 관련 설정은 메모리 관리 cache의 디스크 관리로의 이동관련 설정으로 메모리 관리 오브젝트 수가 넘었을때 Disk로 이동여부, flush 호출시 파일로 저장 여부에 대한 설정이 있다. 이에 대한 설정 예시는 다음과 같다.

#### Configuration

```xml
<cache name="sampleDisk"
       overflowToDisk="true"
       diskPersistent="true"  
       ...>
</cache>
```

- overflowToDisk
  - 메모리 관리 오브젝트 넘었을때 Disk로 이동 여부 (`true`, `false`)
- diskPersistent
  - flush시에 파일로 저장 여부 (`true`, `false`)

이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
Ehcache cache = manager.getCache("sampleDisk");

// 1. Put a content in Cache.
cache.put(new Element("key1", "value1"));

// 2. Get that item from Cache.
Element value = cache.get("key1");
assertEquals("value1", value.getValue().toString());

// 3. flush 를 한다.
cache.flush();		
File dataFile = new File(manager.getDiskStorePath()+ File.separator + "sampleDisk.data");
// 4. 파일로 저장 확인
assertTrue("File exists", dataFile.exists());
```

위의 샘플에서 flush 수행시 파일로 저장되는 것을 확인 할 수 있고, 메모리 관리 오브젝트 Disk이동 여부는 아래의 Cache Size의 예에서 확인한다.

### Cache Size

사이즈 관련 설정은 메모리에서 관리해야 할 최대 오브젝트 수, 디스크에서 관리하는 최대 오브젝트 수에 대한 설정이 있다. 이에 대한 설정 예시는 다음과 같다.

#### Configuration

```xml
<cache name="sampleDisk"
       maxElementsInMemory="3"
       maxElementsOnDisk="2"
       overflowToDisk="true"
       ...>
</cache>
```

- maxElementsInMemory
  - 메모리에서 관리하는 최대 오브젝트 수
- maxElementsOnDisk
  - 디스크에서 관리하는 최대 오브젝트 수

이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
Cache cache = manager.getCache("sampleDisk");

// 1. Put 3 contents in Cache.
cache.put(new Element("key1", "value1"));
cache.put(new Element("key2", "value2"));
cache.put(new Element("key3", "value3"));

// 2. Put Fourth content in Cache.
cache.put(new Element("key4", "value4"));
assertEquals(3, cache.getMemoryStoreSize()); //Memory에는 세개 유지함
assertEquals(1, cache.getDiskStoreSize());   //Disk로 하나 넘어감.

// 3. Put 5~7 contens in Cache.    
cache.put(new Element("key5", "value5"));
cache.put(new Element("key6", "value6"));
cache.put(new Element("key7", "value7"));

// Disk Max Size에 관계 없이 모두 넘어감
assertEquals(3, cache.getMemoryStoreSize()); //Memory에는 세개 유지함
assertEquals(4, cache.getDiskStoreSize());   //Disk에는 2개를 넘어서서 4개 유지함.

// 메모리것을 디스크로 이동시킴
cache.flush();
// Disk의 Max Size 대로 변경됨.
assertEquals(0, cache.getMemoryStoreSize()); //Memory에는 없어짐.
assertEquals(2, cache.getDiskStoreSize());   //Disk에는 DiskMaxSize 대로 2개만 남김.
```

위의 예를 보면 cache.put에 의해서는 Disk의 MaxSize에 관계없이 계속 Memory에서 Disk로 넘어가지만 flush를 수행하면 최대 디스크 보관수만을 남기는 것을 확인 할 수 있다.

## Distributed Cache

Ehcache는 Distributed Cache를 지원하는 방법으로 RMI, JGROUP, JMS등을 지원한다. 그 중에서 JGROUP와 ActiveMQ를 이용한 JMS 지원 설정 및 사용 방법을 설명한다. 자세한 설명은 [Ehcache Documentation](https://www.ehcache.org/documentation/) 참고.

### Using JGroups

JGroups는 multicast 기반의 커뮤니케이션 툴킷으로 그룹을 생성하고 그룹멤버간에 메세지를 주고 받을 수 있도록 지원한다. 관련한 자세한 정보는 [사이트](http://www.jgroups.org/) 참고

#### Configuration

```xml
    <cacheManagerPeerProviderFactory class="net.sf.ehcache.distribution.jgroups.JGroupsCacheManagerPeerProviderFactory"
                                     properties="connect=UDP(mcast_addr=224.10.10.10;mcast_port=5555;ip_ttl=32;
                                     mcast_send_buf_size=150000;mcast_recv_buf_size=80000):
                                     PING(timeout=2000;num_initial_members=6):
                                     MERGE2(min_interval=5000;max_interval=10000):
                                     FD_SOCK:VERIFY_SUSPECT(timeout=1500):
                                     pbcast.NAKACK(gc_lag=10;retransmit_timeout=3000):
                                     UNICAST(timeout=5000):
                                     pbcast.STABLE(desired_avg_gossip=20000):
                                     FRAG:
                                     pbcast.GMS(join_timeout=5000;join_retry_timeout=2000;shun=false;print_local_addr=false)"
                                     propertySeparator="::"/>
    <cache name="cacheSync"
           maxElementsInMemory="1000"
           eternal="false"
           timeToIdleSeconds="1000"
           timeToLiveSeconds="1000"
           overflowToDisk="false">
        <cacheEventListenerFactory class="net.sf.ehcache.distribution.jgroups.JGroupsCacheReplicatorFactory"
                                   properties="replicateAsynchronously=false, replicatePuts=true,
 												replicateUpdates=true, replicateUpdatesViaCopy=false,
 												replicateRemovals=true"/>
    </cache>
```

이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
// 위의 설정파일을 정보 읽어오기
URL url = this.getClass().getResource("/ehcache-distributed-jgroups.xml");
// 두개의 Cache Manager 생성
manager1 = new CacheManager(url);
manager2 = new CacheManager(url);

for (int i = 0; i < 10 ; i++) {
    manager1.getEhcache(CACHE_SYNC).put(new Element(new Integer(i), "value"));
}		
// 리플리케이션을 위한 시간 필요함.     
Thread.currentThread().sleep(100);
// 리플리케이션이 되어 manager2에도 동일한 Cache 정보 입력됨 확인.
assertTrue(manager1.getEhcache(CACHE_SYNC).getKeys().size() == manager2.getEhcache(CACHE_SYNC).getKeys().size() );
```

### Using ActiveMQ

ActiveMQ는 JMS 메세징 서비스를 제공하는 오픈 소스이다. 관련한 자세한 정보는 [사이트](http://activemq.apache.org/) 참조

#### Configuration

```xml
    <cacheManagerPeerProviderFactory
            class="net.sf.ehcache.distribution.jms.JMSCacheManagerPeerProviderFactory"
            properties="initialContextFactoryName=egovframework.rte.fdl.cache.distribute.TestActiveMQInitialContextFactory,
                providerURL=tcp://localhost:61616,
                replicationTopicConnectionFactoryBindingName=topicConnectionFactory,
                getQueueConnectionFactoryBindingName=queueConnectionFactory,
                replicationTopicBindingName=ehcache,
                getQueueBindingName=ehcacheGetQueue"
            propertySeparator=","
            />
 
    <cache name="CacheAsync"
           maxElementsInMemory="1000"
           eternal="false"
           timeToIdleSeconds="1000"
           timeToLiveSeconds="1000"
           overflowToDisk="false">
 
           <cacheEventListenerFactory class="net.sf.ehcache.distribution.jms.JMSCacheReplicatorFactory"
                                   properties="replicateAsynchronously=true, 
                                                replicatePuts=true,
                                                replicateUpdates=true,
                                                replicateUpdatesViaCopy=true,
                                                replicateRemovals=true,
                                                asynchronousReplicationIntervalMillis=1000"
                                    propertySeparator=","/>
    </cache>
```

이 설정을 이용하여 설정에 대한 결과를 확인하는 소스는 다음과 같다.

#### Sample Source

```java
URL url = this.getClass().getResource("/ehcache-distributed-activemq.xml");
manager1 = new CacheManager(url);
manager2 = new CacheManager(url);

cacheName = "CacheAsync";
for (int i = 0; i < 10 ; i++) {
    manager1.getEhcache("CacheAsync").put(new Element(new Integer(i), "value"));
}		

// replication 되는데 일정 시간이 필요함.
Thread.currentThread().sleep(1000);

assertTrue(manager1.getEhcache("CacheAsync").getKeys().size() == manager2.getEhcache("CacheAsync").getKeys().size() );
```

## Spring Integration

Spring 3.1 이전 버전에서 Ehcache를 이용하는 방법에 대해서 설정 및 설정을 이용한 기본 Cache 서비스에 대해서 설명한다.

### Configuration - Spring Application Context

```xml
<bean id="ehcache" class="org.springframework.cache.ehcache.EhCacheFactoryBean">
    <property name="cacheManager">
        <bean class="org.springframework.cache.ehcache.EhCacheManagerFactoryBean">
        <property name="configLocation" value="classpath:ehcache-default.xml"/>
        </bean>
    </property>    
</bean>
```

위와 같이 설정하면 Manager를 통하지 않고서 cache를 얻을 수 있다. ConfigLocation에 정의된 ehcache-default.xml은 Cache Basic의 Configuration에 설명한 설정파일과 동일한 것이다.

### Sample Source

```java
@Resource(name="ehcache")
Ehcache gCache ;

// cache Name을 가지고 cache 찾기
Ehcache cache = gCache.getCacheManager().getCache("sampleMem");    	

cache.put(new Element("key1", "value1"));
Element value = cache.get("key1");
```

위의 예를 보면 ehcache를 이용하여 Ehcache를 가지고 오고 getCacheManager()를 통해서 이름을 통한 cache 정보를 읽어오는 것을 확인할 수 있다. 그 이후에는 위에서 설명한 것과 동일한 방식으로 사용하는 것을 확인 할 수 있다.

## 참고자료

[EhCache](http://ehcache.sourceforge.net/)