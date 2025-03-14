---
title: Spring MVC Tag Configuration
linkTitle: "Tag Configuration"
description: Spring 3부터 mvc태그를 통하여 Controller처리를 위한 설정을 쉽게 하도록 Spring mvc 네임스페이스를 제공한다.
url : /egovframe-runtime/presentation-layer/web-servlet/web-servlet-spring-mvc-tag-configuration/
menu:
    depth:
        name: Tag Configuration
        weight: 4
        parent: "web-servlet"
---
# Spring MVC Tag Configuration

## 개요

Spring 3부터 mvc태그를 통하여 Controller처리를 위한 설정을 쉽게 하도록 Spring mvc 네임스페이스를 제공한다.

- [<mvc:annotation-driven>](#mvcannotation-driven)
- [<mvc:interceptors>](#mvcinterceptors)
- [<mvc:view-controller>](#mvcview-controller)

## 설명

### mvc:annotation-driven

Spring 3.0부터 제공하는 mvc 태그 설정이다. Annotation기반의 Controller호출 설정과 필요한 bean설정을 편리하게 하도록 만들어졌다. 그러나 내부 수정이 어렵기 때문에 mvc:annotation-driven에서 제공하는 기능에 대하여 잘 숙지하고 변경이 불가능 한 경우에는 mvc:annotation-driven을 쓰지 않고 필요한 bean을 수동으로 넣어줘야하는 경우도 있다.
mvc:annotation-driven에서 쓰는 bean설정을 중복으로 쓰지 않도록 주의한다.

#### mvc:annotation-driven에서 제공하는 기능

- RequestMappingHandlerMapping bean등록(기존 DefaultAnnotationHandlerMapping)
- RequestMappingHandlerAdapter bean등록(기존 AnnotationMethodHandlerAdapter)
  - customArgumentResolvers, customReturnValueHandlers 추가 가능
- JSR-303의 검증용 어노테이션(@Valid)를 사용할 수 있도록 LocalValidatorFactoryBean bean설정 (JSR-303지원 라이브러리 존재 시)
- RequestMappingHandlerAdapter의 messageConverters프로퍼티로 메시지 컨버터들 등록

(다음 설정과 동일한 동작을 한다.)

```xml
<bean class="org.springframework.http.converter.ByteArrayHttpMessageConverter" />
<bean class="org.springframework.http.converter.StringHttpMessageConverter">
  <property name="writeAcceptCharset" value="false" />
</bean>
<bean class="org.springframework.http.converter.ResourceHttpMessageConverter" />
<bean class="org.springframework.http.converter.xml.SourceHttpMessageConverter" />
<bean class="org.springframework.http.converter.xml.XmlAwareFormHttpMessageConverter" />
 
<!-- jaxb2라이브러리 존재시 -->
<bean class="org.springframework.http.converter.xml.Jaxb2RootElementHttpMessageConverter" />
 
<!-- jackson 라이브러리 존재시 -->
<bean class="org.springframework.http.converter.json.MappingJacksonHttpMessageConverter"/>
 
<!-- rome 라이브러리 존재시 -->
<bean class="org.springframework.http.converter.feed.AtomFeedHttpMessageConverter" />
<bean class="org.springframework.http.converter.feed.RssChannelHttpMessageConverter" />
```

- 디폴트 validator로 어노테이션 방식의 포맷터를 지원하는 FormattingConversionServiceFactoryBean를 제공하며 validator를 추가 설정하도록 지원
- 디폴트 컨버전 서비스로 FormattingConversionServiceFactoryBean을 제공하며 conversion-service를 추가 설정하도록 지원
- ConversionServiceExposingInterceptor를 등록하여 JSP의 `<spring:eval>`에서 ConversionService를 적용되도록 지원

#### mvc:annotation-driven 설정 시 주의해야할 점

1. `<mvc:annotation-driven>`을 사용할 때는 직접 RequestMappingHandlerAdapter를 등록해주어서는 안되며 직접 등록이 필요한 경우에는 `<mvc:annotation-driven>`을 설정하지 않고 각각의 필요한 설정을 수동으로 해주어야 한다. 전자정부 프레임워크 3.0에서는 Controller의 파라미터로 CommandMap을 쓰기 위하여 RequestMappingHandlerAdapter를 상속받은 EgovRequestMappingHandlerAdapter를 만들었으며, CommandMap을 써야하는 경우 `<mvc:annotation-driven>`을 설정하지 않고 EgovRequestMappingHandlerAdapter를 직접 선언하도록 가이드하고 있다.
2. RequestMappingHandlerAdapter의 customArgumentResolvers 속성에 pring 3.1이전 버전은 WebArgumentResolver인터페이스를 구현해야 했으나 HandlerMethodArgumentResolver인터페이스를 구현한 ArgumentResolver가 설정해야 한다. `<mvc:annotation-driven>` 내부 설정으로 WebArgumentResolver인터페이스 구현체를 쓸 수 있으나 이는 RequestMappingHandlerAdapter가 처리하는 것이 아니라 ServletWebArgumentResolverAdapter에서 호환하도록 변경해주는 것이다.
3. customReturnValueHandlers의 속성은 (Spring3.1이전버전의 customModelAndViewResolvers속성에서 이름변경) 기존에는 ModelAndViewResolver인터페이스의 구현체를 설정하였으나 Spring 3.1부터 HandlerMethodReturnValueHandler인터페이스의 구현체를 설정해야 한다.

### mvc:interceptors

기존 HandlerMapping에는 Interceptor를 모든 url에 일괄적으로만 적용할 수 있었기 때문에 전자정부 프레임워크에서는 SimpleUrlAnnotationHandlerMapping을 제공하여 url별로 Interceptor를 걸 수 있도록 하였다. 그러나 Spring 3부터 제공하는 <mvc:interceptors>태그를 통해 url마다 Interceptor를 적용할 수 있도록 Spring mvc태그 스키마에서 제공하고 있다. 따라서 SimpleUrlAnnotationHandlerMapping은 deprecated되었으며 url별로 Interceptor를 적용하기 위해서는 <mvc:interceptors>태그를 사용하도록 한다.

Interceptor를 일괄 적용하기 위해서는 다음의 예와 같이 사용한다.

```xml
<mvc:interceptors>
    <bean class="egov.interceptors.EgovInterceptor"/>
</mvc:interceptors>
```

특정 패턴의 url에만 인터셉터를 적용하기 위해서는 `<mvc:interceptors>`태그 내부에 `<mvc:interceptor>`를 사용한다.
만약 `/egov/sample`로 시작되는 URL요청에만 인터셉터를 정의하기 위해서는 다음과 같이 사용할 수 있다.

```xml
<mvc:interceptors>
    <mvc:interceptor>
      <mvc:mapping path="/egov/sample/*"/>
      <bean class="egov.interceptors.EgovInterceptor"/>
    </mvc:interceptor>
</mvc:interceptors>
```

또한 interceptor에 특정 URL Pattern을 제외하여 맵핑하는 기능도 지원하고 있다. 이 때는 `<mvc:interceptor>`내부에서 `<exclude-mapping>`태그를 사용한다.
만약 /egov/로 시작하는 URL중 /egov/admin/으로 시작하는 URL에 interceptor맵핑을 제외하고 싶으면 다음과 같이 사용한다.

`<exclude-mapping>` 태그는 spring 3.2 버전 부터 사용 가능 합니다.

```xml
<mvc:interceptors>
    <mvc:interceptor>
      <mvc:mapping path="/egov/**"/>
      <mvc:exclude-mapping path="/egov/admin/**"/>
      <bean class="egov.interceptors.EgovInterceptor"/>
    </mvc:interceptor>
</mvc:interceptors>
```

### mvc:view-controller

Controller에서 별다른 로직 없이 View를 지정하여 DispatcherServlet에 넘겨주는 작업만 하는 경우가 많다. 이럴 때 사용할 수 있는 것이 바로 `<mvc:view-controller>`태그이다.
`<mvc:view-controller>`태그를 설정하여 매핑할 URL패턴과 View이름만 넣어주면 해당 URL을 매핑하고 설정한 view를 리턴하는 ParameterizableViewController가 자동으로 등록된다.

만약 ”/“URL을 요청받았을 경우 “index”를 View이름으로 리턴하기 위해서는 다음과 같이 사용한다.

```xml
<mvc:view-controller path="/" view-name="index"/>
```

InternalResourceViewResolver의 prefix를 /WEB-INF/views/로 정하고 suffix를 .jsp로 정하였다면 / URL이 요청되었을 때 /WEB-INF/views/index.jsp view를 호출하게 된다.

## 참고자료

- [Spring 3.2.x reference : Enabling the MVC Java Config or the MVC XML Namespace](http://docs.spring.io/spring/docs/3.2.x/spring-framework-reference/html/mvc.html#mvc-config-enable/)
