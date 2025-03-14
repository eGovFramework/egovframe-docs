---
title: Property Service
linkTitle: "Property Service"
description: Property Service는 시스템 설정 정보를 외부 파일이나 Spring Bean 설정 파일에서 관리하여 유연성을 제공하는 서비스이다. **Bean 설정 파일**을 사용하여 간단하게 설정할 수 있지만, 변경 시 어플리케이션 재시작이 필요하다. **외부 설정 파일**을 사용하면 운영 중에도 설정 정보를 수정할 수 있으며, 실시간 갱신이 가능하다.
url: /egovframe-runtime/foundation-layer/property/property-service/
menu:
    depth:
        name: Property Service
        weight: 1
        parent: "Property"
---
# Property Service

## 개요

Property Service 는 시스템의 설치 환경에 관련된 정보나, 잦은 정보의 변경이 요구되는 경우 외부에서 그 정보를 관리하게 함으로써 시스템의 유연성을 높이기 위해서 제공하는 것으로 Spring Bean 설정 파일에 관리하고자 하는 정보를 입력(**Bean 설정 파일 사용**) 하거나 외부 파일에 정보 입력 후에 Bean 설정 파일에서 그 파일 위치를 입력하여 이용(**외부 설정 파일 사용**)할 수 있다.

## Bean 설정 파일 사용

간단하게 설정하고자 할 때 사용할 수 있는 방법으로 별도의 외부파일을 두지 않고 Spring Bean 설정 파일을 이용할 수 있다. 하지만 어플리케이션 운영 중에 Property 정보 변경은 불가능 하고 변경처리 시 어플리케이션을 재기동해야 한다. 사용하기 위해서는 bean property의 Name에 **properties**라고 입력하고 map entry의 **key**에 관리하고자 하는 키, **value**에 관리하고자 하는 값을 입력하여 설정한다.

### Configuration

```xml
<bean name="propertyService" class="egovframework.rte.fdl.property.impl.EgovPropertyServiceImpl" 
        destroy-method="destroy">
    <property name="properties">
        <map>
        <entry key="AAAA" value="1234"/>
        </map>
    </property>			
</bean>
```
- propertyService Bean을 추가할 경우 messageSource Bean도 함께 설정해 주어야 한다.
- 아래의 코드를 추가 설정한다.

### messageSource

```xml
<bean id="messageSource"
	class="org.springframework.context.support.ReloadableResourceBundleMessageSource">
	<property name="basenames">
		<list>
			<value>classpath:/message/message-common</value>
			<value>classpath:/egovframework/rte/fdl/idgnr/messages/idgnr</value>
			<value>classpath:/egovframework/rte/fdl/property/messages/properties</value>
		</list>
	</property>
	<property name="cacheSeconds">
		<value>60</value>
	</property>
</bean>
```

### Sample Source

```java
@Resource(name="propertyService")
protected EgovPropertyService propertyService ;
 
@Test
public void testPropertiesService() throws Exception {
   assertEquals("1234",propertyService.getString("AAAA"));
}
```

### 제공유형별 설정/사용 방법

|    제공유형          |          설정 방법            |               사용 방법                  |
|------------------|---------------------------|--------------------------------------|
|  String          |  key=“A” value=“ABC”      |  propertyService.getString(“A”)      |
|  boolean         |  key=“B” value=“true”     |  propertyService.getBoolean(“B”)     |
|  int             |  key=“C” value=“123”      |  propertyService.getInt(“C”)         |
|  long            |  key=“D” value=“123”      |  propertyService.getLong(“D”)        |
|  short           |  key=“E” value=“123”      |  propertyService.getShort(“E”)       |
|  float           |  key=“F” value=“123”      |  propertyService.getFloat(“F”)       |
|  Vector          |  key=“G” value=“123,456”  |  propertyService.getVector(“G”)      |


### 외부 설정 파일 사용

별도의 Property 파일을 만들어서 사용하는 방법으로 Spring Bean 설정 파일에는 파일의 위치를 입력하여 이용할 수 있다. 외부 설정 파일에 기재된 프로퍼티 내용은 어플리케이션 운영 중에 추가 및 변경 가능하다.

#### Configuration

```xml
<bean name="propertyService" class="egovframework.rte.fdl.property.impl.EgovPropertyServiceImpl" 
        destroy-method="destroy">
    <property name="extFileName">
        <set>
        <map>
            <entry key="encoding" value="UTF-8"/>
            <entry key="filename" value="file:./src/**/refresh-resource.properties"/>
        </map>
        <value>classpath*:properties/resource.properties</value>
        </set>
    </property>			
</bean>
```
- MAP을 이용해서 encoding 정보를 입력하는 방법과 파일 위치만을 기재하는 방법 두가지 설정방법 있음

#### properties 파일

```properties
AAAA=1234
```

#### Sample Source

```java
@Resource(name="propertyService")
protected EgovPropertyService propertyService ;
 
@Test
public void testPropertiesService() throws Exception {
   assertEquals("1234",propertyService.getString("AAAA"));
}
```

#### 실시간 갱신 방법

1. 외부파일에 기재된 property 내용을 수정한다.
2. propertyService.refreshPropertyFiles()를 호출한다.

