---
title: Restful
linkTitle: "Restful"
description: Spring MVC를 통해 구현한 RESTful은 리소스에 대한 접근을 URI를 이용하며, HTTP의 PUT, GET, POST, DELETE 등과 같은 메소드의 의미를 그대로 사용하므로, 단순하게 접근 할 수 있다.
url: /egovframe-runtime/integration-layer/restful/
menu:
    depth:
        name: Restful
        weight: 4
        parent: "integration-layer"
---
# Restful

## 개요

Spring MVC를 통해 구현한 RESTful은 리소스에 대한 접근을 URI를 이용하며, HTTP의 PUT, GET, POST, DELETE 등과 같은 메소드의 의미를 그대로 사용하므로, 단순하게 접근 할 수 있다.

## 설명

### web.xml 설정

```xml
    <servlet-mapping>
        <servlet-name>action</servlet-name>
        <url-pattern>*.html</url-pattern>
    </servlet-mapping>
        <servlet-mapping>
    <servlet-name>action</servlet-name>
        <url-pattern>*.xml</url-pattern>
        </servlet-mapping>
    <servlet-mapping>
        <servlet-name>action</servlet-name>
        <url-pattern>*.json</url-pattern>
    </servlet-mapping>
    
    <filter>
        <filter-name>httpMethodFilter</filter-name>
        <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>httpMethodFilter</filter-name>
        <url-pattern>/springrest/*</url-pattern>
    </filter-mapping>
```

자세한 설명은 아래에 있다.

### Request Mapping

- 설정

    REST 스타일의 URL은 '/cgr’, '/cgr/CATEGORY-00000000001' 처럼 계층 구조로 사용가능하도록 설계되었다. 따라서 web.xml에 DispatcherServlet을 정의하고 매핑할 URL 패턴을 '/'로 지정해야한다. **DispatcherServlet URL 매핑** 샘플은 다음과 같다.

    ```xml
        <servlet-mapping>    
            <servlet-name>action</servlet-name>    
            <url-pattern>/springrest/*</url-pattern>
        </servlet-mapping>
    ```

    아래와 같은 방법으로도 DispatcherServlet URL 매핑을 사용 할 수 있다.

    ```xml
        <servlet-mapping>
            <servlet-name>action</servlet-name>
            <url-pattern>*.do</url-pattern>
        </servlet-mapping>
        <servlet-mapping>
            <servlet-name>action</servlet-name>
            <url-pattern>*.html</url-pattern>
        </servlet-mapping>
        <servlet-mapping>
            <servlet-name>action</servlet-name>
            <url-pattern>*.xml</url-pattern>
        </servlet-mapping>
        <servlet-mapping>
            <servlet-name>action</servlet-name>
            <url-pattern>*.json</url-pattern>
        </servlet-mapping>
    ```

- 사용

    Spring에서 제공하는 REST 지원 기능들은 모두 Spring MVC 기반으로 되어 있다. REST 방식으로 노출되는 서비스는 곧 Controller의 메소드이기 때문에 기존에 웹 어플리케이션을 개발하던 방식과 크게 다르지 않다.

    Resource의 ID인 URI를 Controller 클래스나 메소드에 매핑하기 위해서는 **@RequestMapping**을 사용한다. @RequestMapping이 URI Template을 지원하기 때문에 아래 샘플코드와 같이 사용할 수 있다.

    ```java
    @Controller
    @SessionAttributes(types=CategoryVO.class)
    public class EgovCategoryController {
            //…
        @RequestMapping(value="/springrest/cgr/{ctgryId}", method=RequestMethod.GET)
        public String updtCategoryView(@PathVariable String ctgryId, Model model) throws Exception{
            // …
        }
    }
    ```

    모든 HTTP method 사용을 위해서 @RequestMapping에서 'method' 속성을 제공한다. 따라서, '/springrest/cgr/CATEGORY-00000000001'이라는 URI가 GET으로 요청이 들어올 경우 위의 updtCategoryView ( ) 메소드가 매핑될 것이다.

- @PathVariable annotation추가

    ‘/springrest/cgr/CATEGORY-00000000001’로 URI요청이 들어왔을 경우 @PathVariable을 사용하여 ‘ctgryID’ 입력 인자로 바인딩 된다.

    ```java
    @RequestMapping(value="/springrest/cgr/{ctgryId}", method=RequestMethod.GET)
    public String updtCategoryView(@PathVariable String ctgryId, Model model) throws Exception{
        // …
    }
    ```

### HTTP Method Conversion

- 설정

    브라우저 기반의 HTML에서는 GET, POST만 지원한다. 일반적으로 HTTP에서는 POST를 사용하고, hidden 타입의 입력값으로 HTTP METHOD를 지정하는 경우가 많다. 다음은 web.xml에 **HiddenHttpMethodFilter를** 정의한 모습이다.

    ```xml
        <filter>
            <filter-name>httpMethodFilter</filter-name>
        <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
        </filter>
        <filter-mapping>
            <filter-name>httpMethodFilter</filter-name>
            <url-pattern>/springrest/*</url-pattern>
        </filter-mapping>
    ```

- 사용

    web.xml에 HiddenHttpMethodFilter 설정을 추가하면, **HTTP Method가 POST이고 _method라는 파라미터가 존재하는 경우 HTTP의 Method를 _method 값으로 바꾼다.**

    또한 Spring에서는 &lt;form:form&gt;에서 실제 HTTP Method를 지정하는 hidden 타입의 입력 필드를 자동으로 추가해주기 때문에 훨씬 더 편리하게 사용할 수 있다.

    ```html
        <form:form method="delete">
	        <input type=submit value=Delete/>
        </form:form>
    ```

    JSP에 위와 같이 작성하면, 내부적으로는 POST 방식으로 “_method=delete”가 전달되는 것이다.

    샘플코드이다.

    ```html
    function fncSubmit(method) {
        document.detailForm._method.value=method;
        document.detailForm.submit();
    }
    
    //..
    
    <form:form name="detailForm" method="${method}">
        <a href="javascript:fncSubmit('delete');">삭제</a>
    </form:form>
    ```

### HTTP Method Conversion

Xml과 json 등 다른 view로 보여지는 것으로 spring에서는 **ContentNegotiatingViewResolver를** 제공한다. ContentNegotiatingViewResolver는 다른 View Resolver들과 반드시 함께 사용되어야 하므로 View Resolver 설정 시 반드시 order를 정의해야 한다. 당연히 ContentNegotiatingViewResolver가 가장 높은 우선순위(가장 작은숫자)를 가져야 한다. defaultView는 View를 찾지 못한 경우 디폴트 View로 사용된다.

```xml
<bean class="org.springframework.web.servlet.view.ContentNegotiatingViewResolver">
    <property name="defaultViews">
        <list>
            <bean class="org.springframework.web.servlet.view.json.MappingJacksonJsonView">
                <property name="prefixJson" value="false"/>
            </bean>
        </list>
    </property>
</bean>
```

### Views

- MarshallingView

    클라이언트에게 xml 응답을 돌려주기 위해 Spring OXM Marshaller를 사용한다. Spring oxm는 JAXB2, XMLBeans, JiBX, Castor등을 사용하여 Marshaller를 손쉽게 정희할 수 있게 해준다. Restful 예제에서는 JAXB2를 사용하였다. (OXM예제는 Castor사용)

    ```xml
    <bean class="org.springframework.web.servlet.view.ContentNegotiatingViewResolver">
        <property name="mediaTypes">
            <map>
                <entry key="html" value="text/html" />
                <entry key="xml" value="application/xml" />
                <entry key="json" value="application/json" />
            </map>
        </property>
        <property name="order" value="0" />
    //..
    </beans>
    
    <bean name="cgr/egovCategoryRegister" class="org.springframework.web.servlet.view.xml.MarshallingView">
        <property name="marshaller" ref="marshaller" />
    </bean>
    
    <oxm:jaxb2-marshaller id="marshaller">
        <oxm:class-to-be-bound name="egovframework.rte.tex.cgr.service.CategoryVO" />
    </oxm:jaxb2-marshaller>
    ```

- MappingJacksonJsonView

    JSON으로 응답을 전달할 수 있는 View.

    ```xml
    <bean class="org.springframework.web.servlet.view.ContentNegotiatingViewResolver">
        <property name="mediaTypes">
            <map>
                <entry key="html" value="text/html" />
                <entry key="xml" value="application/xml" />
                <entry key="json" value="application/json" />
            </map>
        </property>
        <property name="order" value="0" />
        //..
    </beans>
    
    <bean name="cgr/egovCategoryList" 
    class="org.springframework.web.servlet.view.json.MappingJacksonJsonView" />
    ```

### 실제 사용 예

- jsp

    ```html
    function fncSubmit(method) {
        document.detailForm._method.value=method;		
        document.detailForm.submit();
    }
    
    //..
    
    <form:form name="detailForm" method="${method}">
    //..
    </form:form>
    
    //..
    <a href="javascript:fncSubmit('post');">등록</a> //----------- controller 2.
    <a href="javascript:fncSubmit('put');">수정</a> //------------- controller 3.
    <a href="javascript:fncSubmit('delete');">삭제</a> //----------- controller 4.
    <a href=" /springrest/cgr/{id}.xml">xml 보기</a> // ContentNegotiatingViewResolver설정
    <a href=" /springrest/cgr/{id}.json">json(defaultView) 보기</a> // ContentNegotiatingViewResolver설정
    <a href=" /springrest/cgr.html">목록</a> //------------------ controller 1.
    <a href=" /springrest/cgr.json">목록(json)</a> // ContentNegotiatingViewResolver 설정
    ```

- controller

    ```java
    // 1. 목록
    @RequestMapping(value="/springrest/cgr", method=RequestMethod.GET)
    public String selectCategoryList(..) throws Exception {
        //..
    }
    
    // 2. 등록
    @RequestMapping(value="/springrest/cgr", method = RequestMethod.POST, ..)
    public String create( ..) throws Exception {
        //..
    }
    
    // 3. 수정
    @RequestMapping(value = "/springrest/cgr/{ctgryId}", method = RequestMethod.PUT, ..)
    public String update(..) throws Exception {
        //..
    }
    
    // 4. 삭제
    @RequestMapping(value = "/springrest/cgr/{ctgryId}", method=RequestMethod.DELETE)
    public String deleteCategory(@PathVariable String ctgryId, SessionStatus status) throws Exception{
        //..
    }
    ```

## 참고자료

- [RESTful 예제](./rex-restful-example.md)
