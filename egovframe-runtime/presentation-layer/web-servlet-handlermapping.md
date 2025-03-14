---
title: HandlerMapping
linkTitle: "HandlerMapping"
description: DispatcherServlet은 요청을 처리할 Controller를 HandlerMapping을 통해 매핑하며, Spring MVC는 여러 종류의 HandlerMapping 구현 클래스를 제공한다. Spring 3.1 이후 버전부터 기본 HandlerMapping은 RequestMappingHandlerMapping이며, 그 이전 버전에서는 DefaultAnnotationHandlerMapping이 기본으로 사용되었다.
url : /egovframe-runtime/presentation-layer/web-servlet/web-servlet-handlermapping/
menu:
    depth:
        name: HandlerMapping
        weight: 3
        parent: "web-servlet"
---
# HandlerMapping

## 개요

DispatcherServlet에 Client로부터 Http Request가 들어 오면 HandlerMapping은 요청처리를 담당할 Controller를 mapping한다.
Spring MVC는 interface인 HandlerMapping의 구현 클래스도 가지고 있는데, 용도에 따라 여러 개의 HandlerMapping을 사용하는 것도 가능하다.
빈 정의 파일에 HandlerMapping에 대한 정의가 없다면 Spring MVC는 기본(default) HandlerMapping을 사용한다.

기본 HandlerMapping은 BeanNameUrlHandlerMapping이며, jdk1.5 이상의 실행환경일 때, Spring 3.1이후 버전이면(egov 3.0부터) RequestMappingHandlerMapping가 기본 HandlerMapping이며,
Spring 3.1이전 버전이면(egov 3.0이전 버전) DefaultAnnotationHandlerMapping가 기본 HandlerMapping이다.
(DefaultAnnotationHAndlerMapping은 3.1부터 deprecated되고 RequestMappingHandlerMapping으로 대체됨)

## 설명

BeanNameUrlHandlerMapping, SimpleUrlHandlerMapping 등 주요 HandlerMapping 구현 클래스는 상위 추상 클래스인 AbstractHandlerMapping과 AbstractUrlHandlerMapping을 확장하기 때문에 이 추상클래스들의 프로퍼티를 사용한다.
주요 프로퍼티는 아래와 같다.

- defaultHandler
  - 요청에 해당하는 Controller가 없을 경우, defaultHandler에 등록된 Controller를 반환한다.
- alwaysUseFullPath
  - URL과 Controller 매핑시에 URL full path를 사용할지 여부를 나타낸다.
  - 예를 들어, servlet-mapping이 /easycompany/* 이고, alwaysUseFullPath가 true이면 /easycompany/employeeList.do, alwaysUseFullPath가 false이면 /employeeList.do 이다.
- interceptors
  - Controller가 요청을 처리하기 전,후로 특정한 로직을 수행되기 원할때 interpceptor를 등록한다. 복수개의 interpceptor를 등록할 수 있다. interceptor에 대한 자세한 설명은 이곳을 참고하라.
- order
  - 여러개의 HandlerMapping 사용시에 우선순위.

```xml
...
<bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping" p:order="2"/>
<bean class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping" p:order="3">
...
```

- pathMatcher : 사용자 요청 URL path와 설정정보의 URL path를 매칭할때, 특정 스타일의 매칭을 지원하는 PathMatcher를 등록할수 있다. 기본값은 Ant-style의 패턴매칭을 제공하는 AntPathMatcher이다.

Spring MVC(3.1이후버전) 제공하는 주요 HandlerMapping 구현 클래스는 아래와 같다.

- BeanNameUrlHandlerMapping
- RequestMappingHandlerMapping(DefaultAnnotationHandlerMapping이 deprecated되면서 대체됨)
- ControllerClassNameHandlerMapping
- SimpleUrlHandlerMapping

Spring 3 버전 이전에는 @MVC에서 DefaultAnnotationHandlerMapping은 URL 단위로 interceptor를 적용할 수 없기에 전자정부프레임워크에서 아래와 같은 HandlerMapping 구현 클래스를 추가했다.

- SimpleUrlAnnotationHandlerMapping

그러나 Spring 3버전부터 <mvc:interceptors> element에서 url별로 interceptor를 적용할 수 있도록 추가하여 SimpleUrlAnnotationHandlerMapping은 deprecated되었다.

### BeanNameUrlHandlerMapping

BeanNameUrlHandlerMapping은 빈정의 태그에서 **name** attribute에 선언된 URL과 **class** attribute에 정의된 Controller를 매핑하는 방식으로 동작한다.
예를 들어, 아래와 같이 정의되어 있다면,

```xml
<beans ...>
...
   <!--HandlerMapping이 BeanNameUrlHandlerMapping 밖에 없다면 BeanNameUrlHandlerMapping에 대한 별도의 빈정의는 필요 없다.-->
   <!--<bean class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>--> 
   <bean name="/insertEmployee.do" class="com.easycompany.controller.InsertEmployeeController">
       ...
   </bean>
...
</beans>
```

Client에서 URL ~~/insertEmployee.do 요청이 들어오면 InsertEmployeeController 클래스가 요청 처리를 담당한다.

앞 개요에서 언급했듯이 WAC(WebgApplicationContext)에 HandlerMapping 빈정의가 없다면 BeanNameUrlHandlerMapping이 (별도의 빈 정의 없이) 사용된다.
하지만, SimpleUrlHandlerMapping 같은 다른 HandlerMapping과 같이 써야 한다면, BeanNameUrlHandlerMapping도 빈정의가 되어야 한다.

```xml
<beans ...>
...
   <bean class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping">
      <property name="mappings">
       ....
      </property>
   </bean>
 
   <bean class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>
   <bean name="/insertEmployee.do" class="com.easycompany.controller.InsertEmployeeController">
       ....
   </bean>
...
</beans>
```

### RequestMappingHandlerMapping ( @deprecated DefaultAnnotationHandlerMapping과 거의 동일 )

@MVC 개발을 하려면 RequestMappingHandlerMapping을(Spring 3.1이전버전은 DefaultAnnotationHandlerMapping) 사용해야 한다. 단, jdk 1.5 이상의 개발환경이어야 한다.
RequestMappingHandlerMapping 사용 방법은 세가지가 있다.

- 선언하지 않는 방법
- `<mvc:annotation-driven/>`을 선언하는 방법
- RequestMappingHandlerMapping을 직접 선언하는 방법

#### 선언하지 않는 방법

RequestMappingHandlerMapping은 기본 HandlerMapping이므로 지정하지 않아도 사용가능하다. 아래와 같이 컴포넌트 스캔할 패키지를 지정해 주면,

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
				http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-2.5.xsd">
 
       <context:component-scan base-package="org.mycode.controller" />
 
</beans>
```

패키지 org.mycode.controller 아래의 @Controller중에 @RequestMapping에 선언된 URL과 해당 @Controller 클래스의 메소드와 매핑한다.

#### <mvc:annotation-driven/>을 선언하는 방법

@MVC사용 시 필요한 빈들을 등록해주는 `<mvc:annotation-driven/>`을 설정하면 내부에서
org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping ,org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter 이 구성된다.

- 기존 Spring 3.0버전에서 `<mvc:annotation-driven/>`는 DefaultAnnotationHandlerMapping, AnnotationMethodHandlerAdapter를 구성해주었다.

`<mvc:annotation-driven>`은 다음과 같이 사용한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans ... 생략>
  <mvc:annotation-driven/>
<!-- 생략 -->
</beans>
```

- 여기서 주의할 점은, CommandMap을 사용할 경우 mvc:annotation-driven을 선언하면 안된다. CommandMap을 사용할 경우 EogvRequestMappingHandlerAdapter와 RequestMappingHandlerMapping을 직접 선언해주어야한다.

#### RequestMappingHandlerMapping을 직접 선언하는 방법

다른 HandlerMapping과 함께 사용할 때 선언한다.

```xml
<bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping"/>
<!--생략-->
```

#### Controller코드 예제

위와 같이 RequestMappingHandlerMapping을 설정하였을 때

Controller에서의 간단한 예제를 보면,

```java
package org.mycode.controller;
....
@Controller
public class HelloController {
 
      @RequestMapping(value="/hello.do")
      public String hellomethod(){
           ......   
      }
}
```

/hello.do로 URL 요청이 들어 오면 HelloController의 메소드 hellomethod가 실행된다.

### ControllerClassNameHandlerMapping

ControllerClassNameHandlerMapping은 빈정의된 Controller의 클래스 이름중 suffix인 Controller를 제거한 나머지 이름의 소문자로 url mapping한다.

```xml
<beans ..>
   ...
   <bean class="org.springframework.web.servlet.mvc.support.ControllerClassNameHandlerMapping"/>
 
   <bean class="com.easycompany.controller.hierarchy.EmployeeListController"/>
 
   <bean class="com.easycompany.controller.hierarchy.InsertEmployeeController"/>
   ...
</beans>
```

빈 정의가 위와 같다면, EmployeeListController ↔ /employeelist*, InsertEmployeeController ↔ /insertemployee* 과 같이 url mapping이 이루어 진다.
ControllerClassNameHandlerMapping에 프로퍼티 값으로 caseSensitive나 pathPrefix, basePackage등을 설정할 수 있는데,

- caseSensitive
  - Controller 이름으로 URL 경로 mapping시에 대문자 사용여부. (ex. /insertemployee* 가 아니라 /easycompany/insertEmployee*로 사용하기 원할때).
- pathPrefix
  - URL 경로에 기본적인 prefix 값. 기본값은 false이다.
- basePackage
  - URL mapping에 사용되는 Controller의 기본 패키지 이름이다. 사용되는 Controller의 패키지명에 기본 패키지에 추가되는 subpackage가 있다면 해당 subpackage 이름이 URL 경로에 추가된다.

```xml
<beans ..>
   ...
   <bean class="org.springframework.web.servlet.mvc.support.ControllerClassNameHandlerMapping">
      <property name="pathPrefix" value="/easycompany"/>
      <property name="caseSensitive" value="true"/> 
      <property name="basePackage" value="com.easycompany.controller"/>
   </bean>
 
   <bean class="com.easycompany.controller.hierarchy.EmployeeListController"/>
 
   <bean class="com.easycompany.controller.hierarchy.InsertEmployeeController"/>
   ...
</beans>
```

하면, EmployeeListController ↔ /easycompany/hierarchy/employeeList*, InsertEmployeeController ↔ /easycompany/hierarchy/insertEmployee* 과 같이 url mapping이 이루어 진다.

### SimpleUrlHandlerMapping

SimpleUrlHandlerMapping은 Ant-Style 패턴 매칭을 지원하며, 하나의 Controller에 여러 URL을 mapping 할 수 있다.
proerty의 key 값에 URL 패턴을 지정하고 value에는 Controller의 id 혹은 이름을 지정한다.

```xml
<beans ...>
...
         <bean class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping">
                <property name="mappings">
                        <props>
                                <prop key="/employeeList.do">employeeListController</prop>
                                <prop key="/insertEmployee.do">insertEmployeeController</prop>
                                <prop key="/updateEmployee.do">updateEmployeeController</prop>
                                <prop key="/loginProcess.do">loginController</prop>
                                <prop key="/**/login.do">staticPageController</prop>
                                <prop key="/static/*.html">staticPageController</prop>
                        </props>
                </property>
         </bean>
 
         <bean id="loginController" class="com.easycompany.controller.hierarchy.LoginController"/>
         <bean id="employeeListController" class="com.easycompany.controller.hierarchy.EmployeeListController" />
         <bean id="insertEmployeeController" class="com.easycompany.controller.hierarchy.InsertEmployeeController" />
         <bean id="updateEmployeeController" class="com.easycompany.controller.hierarchy.UpdateEmployeeController" />
         <bean id="staticPageController" class="org.springframework.web.servlet.mvc.UrlFilenameViewController" />
...
</beans>
```

SimpleUrlHandlerMapping을 사용하면 Interceptor를 특정 URL 단위로 적용하는게 가능하다.
프로퍼티 interceptors에 적용하려는 Interceptor들을 리스트로 선언해주면 된다.
URL /employeeList.do, /insertEmployee.do, /updateEmployee.do 요청에 대해서 사용자 인증여부를 interceptor로 검증한다고 하면,아래와 같이 정의한다.

```xml
<beans ...>
...
         <bean class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping">
                <property name="interceptors">
                     <list>
                        <ref local="authenticInterceptor"/>
                     </list>
                </property>
                <property name="mappings">
                        <props>
                                <prop key="/employeeList.do">employeeListController</prop>
                                <prop key="/insertEmployee.do">insertEmployeeController</prop>
                                <prop key="/updateEmployee.do">updateEmployeeController</prop>
                        </props>
                </property>
         </bean>
         <bean class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping">
                <property name="mappings">
                        <props>                                
                                <prop key="/**/login.do">staticPageController</prop>
                                <prop key="/static/*.html">staticPageController</prop>
                        </props>
                </property>
         </bean>
 
         <bean id="loginController" class="com.easycompany.controller.hierarchy.LoginController"/>
         <bean id="employeeListController" class="com.easycompany.controller.hierarchy.EmployeeListController" />
         <bean id="insertEmployeeController" class="com.easycompany.controller.hierarchy.InsertEmployeeController" />
         <bean id="updateEmployeeController" class="com.easycompany.controller.hierarchy.UpdateEmployeeController" />
         <bean id="staticPageController" class="org.springframework.web.servlet.mvc.UrlFilenameViewController" />
 
         <bean id="authenticInterceptor" class="com.easycompany.interceptor.AuthenticInterceptor" />
...
</beans>
```

### SimpleUrlAnnotationHandlerMapping (@deprecated)

- Spring 3부터 `<mvc:interceptors>` element를 통해 SimpleUrlAnnotationHandlerMapping과 동일한 기능을 제공하므로 deprecated되었다.

DefaultAnnotationHandlerMapping에 interceptor를 등록하면, 모든 @Controller에 interceptor가 적용되는 문제점이 있다.
SimpleUrlAnnotationHandlerMapping은 @Controller 사용시에 url 단위로 Interceptor를 적용하기 위해 개발되었다.
Spring 3부터 `<mvc:interceptors>`를 이용하여 동일한 기능을 제공하므로 현재 SimpleUrlAnnotationHandlerMapping은 deprecated되었다.
그러나 이전 버전은 해당기능을 제공하지 않는다.

SimpleUrlAnnotationHandlerMapping은 아래와 같은 3가지 사항이 고려됬다.

- HandlerMapping:Interceptors 관계의 스프링 구조를 깨뜨리지 말자. (ex. Controller:Interceptor (X))
- 쉬운 사용을 위해 기존의 HandlerMapping과 비슷한 방식의 사용법을 선택하자. (ex.SimpleUrlHandlerMapping)
- 최소한의 커스터마이징을 하자. → 짧은 시간… 또한 추후 deprecated시에 시스템에 영향을 최소화 하기 위해.

웹 어플리케이션이 초기 구동될때, DefaultAnnotationHandlerMapping은 2가지 주요한 작업을 한다. (다른 HandlerMapping도 유사한 작업을 한다.)

1. @RequestMapping의 url 정보를 읽어 들여 해당 Controller와 url간의 매핑 작업.
2. 설정된 Interceptor들에 대한 정보를 읽어 들임.

1번 작업은 DefaultAnnotationHandlerMapping의 상위 클래스인 AbstractDetectingUrlHandlerMapping에서 이루어 지는데,
맵핑을 위한 url리스트를 가져오는 determineUrlsForHandler 메소드는 하위 클래스에서 구현하도록 abstract 선언 되어 있다.

```java
public abstract class AbstractDetectingUrlHandlerMapping extends AbstractUrlHandlerMapping {
...
	protected void detectHandlers() throws BeansException {
		if (logger.isDebugEnabled()) {
			logger.debug("Looking for URL mappings in application context: " + getApplicationContext());
		}
		String[] beanNames = (this.detectHandlersInAncestorContexts ?
				BeanFactoryUtils.beanNamesForTypeIncludingAncestors(getApplicationContext(), Object.class) :
				getApplicationContext().getBeanNamesForType(Object.class));
 
		// Take any bean name that we can determine URLs for.
		for (int i = 0; i < beanNames.length; i++) {
			String beanName = beanNames[i];
			String[] urls = determineUrlsForHandler(beanName);
			if (!ObjectUtils.isEmpty(urls)) {
				// URL paths found: Let's consider it a handler.
				registerHandler(urls, beanName);
			}
			else {
				if (logger.isDebugEnabled()) {
					logger.debug("Rejected bean name '" + beanNames[i] + "': no URL paths identified");
				}
			}
		}
	}
	protected abstract String[] determineUrlsForHandler(String beanName);
}
```

DefaultAnnotationHandlerMapping의 determineUrlsForHandler 메소드는 @RequestMapping의 url 리스트를 전부 가져오기 때문에,
빈 설정 파일에 정의한 url 리스트만 가져오도록 SimpleUrlAnnotationHandlerMapping에서 determineUrlsForHandler 메소드를 구현 한다.

```java
package egovframework.rte.ptl.mvc.handler;
...
public class SimpleUrlAnnotationHandlerMapping extends DefaultAnnotationHandlerMapping {
 
	//url리스트, 중복값을 허용하지 않음으로 Set 객체에 담는다.
	private Set<String> urls;
 
	public void setUrls(Set<String> urls) {
		this.urls = urls;
	}
 
	/**
	 * @RequestMapping로 선언된 url중에 프로퍼티 urls에 정의된 url만 remapping해 return
	 * url mapping시에는 PathMatcher를 사용하는데, 별도로 등록한 PathMatcher가 없다면 AntPathMatcher를 사용한다.
	 * @param urlsArray - @RequestMapping로 선언된 url list
	 * @return urlsArray중에 설정된 url을 필터링해서 return.
	 */
	private String[] remappingUrls(String[] urlsArray) {
 
		if (urlsArray==null) {
			return null;
		}
 
		ArrayList<String> remappedUrls = new ArrayList<String>();
 
		for(Iterator<String> it = this.urls.iterator(); it.hasNext();) {
			String urlPattern = (String) it.next();
			for(int i=0;i<urlsArray.length;i++){
				if(getPathMatcher().matchStart(urlPattern, urlsArray[i])){					
					remappedUrls.add(urlsArray[i]);
				}
			}
		}
 
		return (String[]) remappedUrls.toArray(new String[remappedUrls.size()]);		
	}
 
	/**
	 * @RequestMapping로 선언된 url을 필터링하기 위해
	 * org.springframework.web.servlet.mvc.annotation.DefaultAnnotationHandlerMapping의 
	 * 메소드 protected String[] determineUrlsForHandler(String beanName)를 override.
	 * 
	 * @param beanName - the name of the candidate bean
	 * @return 빈에 해당하는 URL list
	 */
	protected String[] determineUrlsForHandler(String beanName) {
		return remappingUrls(super.determineUrlsForHandler(beanName));
	}	
}
```

인터셉터를 적용할 url들을 프로퍼티 urls에 선언하면 되며, Ant-style의 패턴 매칭이 지원된다.
SimpleUrlAnnotationHandlerMapping은 선언된 url만을 Controller와 매핑처리한다.
따라서, 아래와 같이 선언된 DefaultAnnotationHandlerMapping와 같이 선언되어야 하며, 우선순위는 SimpleUrlAnnotationHandlerMapping이 높아야 한다.

```xml
<bean id="selectAnnotaionMapper"
    class="egovframework.rte.ptl.mvc.handler.SimpleUrlAnnotationHandlerMapping"
    p:order="1">
    <property name="interceptors">
        <list>
            <ref local="authenticInterceptor"/>
        </list>
    </property>
    <property name="urls">
        <set>
            <value>/*Employee.do</value>
            <value>/employeeList.do</value>
        </set>
    </property>
</bean>

<bean id="annotationMapper" 
    class="org.springframework.web.servlet.mvc.annotation.DefaultAnnotationHandlerMapping" 
    p:order="2"/>

<bean id="authenticInterceptor" class="com.easycompany.interceptor.AuthenticInterceptor" />
```

## 참고자료

- The Spring Framework - Reference Documentation 2.5.6
- Spring Framework API Documentation 2.5.6