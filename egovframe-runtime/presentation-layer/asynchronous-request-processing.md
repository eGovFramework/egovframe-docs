---
title: Asynchronous request processing
linkTitle: "비동기요청"
description: Servlet 3.0과 Spring MVC 3.2 이상에서는 비동기 요청 처리를 통해 요청 쓰레드가 반환된 후에도 내부 쓰레드에서 비동기 작업을 처리할 수 있다. 이를 위해 `Callable`, `DeferredResult`, `WebAsyncTask` 등을 사용해 시간이 오래 걸리는 작업을 비동기로 처리하고, 완료 후 응답을 보낼 수 있다.
url : /egovframe-runtime/presentation-layer/asynchronous-request-processing/
menu:
    depth:
        name: UI 비동기요청
        weight: 8
        parent: "presentation-layer"
---
# Asynchronous request processing

## 개요

기존의 요청 처리는 하나의 요청에 대해 한 개의 쓰레드를 사용하였다. 하나의 쓰레드에서 요청-응답 과정을 모두 처리하기 때문에 요청처리 이후 응답이 오기까지 쓰레드를 대기상태로 유지하였다. 그러나 서버와의 연결을 유지한채 대기상태로 있는 것이 아니라 서버와의 처리를 계속 이어가게 해주기 위해서는 이러한 기존의 처리에 한계가 있었다.

Servlet 3.0에서 제공하는 비동기 요청 처리는 쓰레드가 대기상태로 있는 것이 아니라 요청을 처리하는 Servlet 쓰레드가 요청후 바로 반환되고 내부의 다른 쓰레드가 이를 처리했다가 처리완료 후 응답처리 리소스가 가용할 때 Servlet쓰레드가 응답처리를 계속 이어가게 해 주는 것이다.

비동기 요청처리를 위해 다음과 같은 환경이 필요하다.

- Servlet 3.0이상
- Spring MVC 3.2이상 (eGov 3.0에 포함)
- Web.xml 설정 변경

### Servlet 3.0을 위한 pom dependency변경

```xml
<!-- Servlet -->
<dependency>
   <groupId>javax.servlet</groupId>
   <artifactId>javax.servlet-api</artifactId>
   <version>3.0.1</version>
   <scope>provided</scope>
</dependency>
```

### web.xml설정 변경

web.xml의 servlet버전을 변경해야한다.

```xml
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
    version="3.0">
 
    ...
 
</web-app>
```

web.xml내의 servlet설정에 async-supported 태그 값을 true로 설정한다.

```xml
<servlet>
   <servlet-name>appServlet</servlet-name>
   <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
   <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
   </init-param>
   <load-on-startup>1</load-on-startup>
   <async-supported>true</async-supported>
</servlet>
```

## 설명

Spring의 비동기 요청처리에서는 Servlet 쓰레드는 요청을 처리하고 Spring의 Async 제공 클래스를 통해 비동기모드로 전환되며 Servlet 쓰레드는 반환된다. 그 후 내부 Application의 쓰레드에서 서비스 처리가 일어나게 된다. 처리완료 후 Servlet 쓰레드가 다시 응답을 받아 이를 클라이언트로 전송한다.

Spring의 비동기 요청처리에서 제공하는 Class는 Servlet 쓰레드가 반환된 이후 내부 서비스를 처리하는 쓰레드의 종류에 따라 나뉜다.

### Callable

요청을 처리하는 Servlet 쓰레드가 반환되면 Spring MVC에서 제어하는 쓰레드에 의해 비동기처리된다.

Callable의 처리과정은 다음과 같다.

1. Controller의 RequestMapping method에서 일반적인 뷰 객체나 String값을 리턴하는 것이 아니라 Callable객체를 리턴한다.
2. Callable이 리턴될 때 Servlet 쓰레드가 반환되며 비동기처리를 Callable에게 위임한다.
3. Spring MVC내의 TaskExcutor에서 관리되는 쓰레드에서 Async처리가 된다.
4. Callable내부의 call()함수에서 리턴되는 값이 다시 Servlet 쓰레드로 전달된다.

Callable은 주로 요청처리가 오래걸리는 DB작업, REST API 요청처리를 하는 데 적합하다.

```java
@RequestMapping(“/view”)
public Callable<String> callableWithView(final Model model) {
  return new Callable<String>() {
    @Override
    public String call() throws Exception {
        Thread.sleep(2000);
        model.addAttribute(“foo”, “bar”);
        model.addAttribute(“fruit”, “apple”);
        return “view”;
    }
}
```

### DefferedResult

Servlet 스레드는 반환하고 Spring MVC가 제어하지 않는 쓰레드를 통해 비동기를 처리한다. DefferedResult는 JMS, AMQP, 스케쥴러, Redis, 다른 HTTP요청에서 사용된다.

DefferedResult의 처리과정은 다음과 같다.

1. Controller에서 DefferedResult를 반환하고 In-Memory Queue또는 List에 DefferedResult를 저장한다.
2. Servlet 쓰레드는 반환되고 이벤트 발생 시 Queue에서 DefferedResult객체를 꺼내 사용한다.

```java
@RequestMapping("/quotes")
@ResponseBody
public DeferredResult<String> quotes() {
  DeferredResult<String> deferredResult = new DeferredResult<String>();
  // Save the deferredResult in in-memory queue ...
  queue.add(defferedResult);
 
  return deferredResult;
}
 
// In some other thread...
@RequestMapping("/someEvent")
@ResponseBody
public String someEvent(String data) {
  for(DefferedResult<String> result : queue) {
    result.setResult(data);
  }
 
  return "view";
}
```

### AsyncTask

Callable과 동일한 방식으로 사용하며 Controller에서 Callable을 담아서 반환한다.

Timeout을 추가할 수 있으며 AsyncTaskExecutor를 지정하거나 작업의 종류에 따라 쓰레드 풀을 분리하여 사용할 수 있다.

```java
@RequestMapping("/facebooklink")
public WebAsyncTask<String> facebooklink() {
  return new WebAsyncTask<String>(
    30000L, // Timeout
    "facebookTaskExecutor", // TaskExecutor
    new Callable<String>() {
      @Override
      public String call() throws Exception {
      // 작업
        return result;
      }
    }
  );
}
```

### 참고자료

- [Spring Framework - Reference Document / 4.1 Support for Servlet 3 based asynchronous request processing](http://docs.spring.io/spring/docs/3.2.6.RELEASE/spring-framework-reference/htmlsingle/#new-in-3.2-webmvc-async)
- [Spring Framework - Reference Document / 17.3.4 Asynchronous Request Processing](http://docs.spring.io/spring/docs/3.2.6.RELEASE/spring-framework-reference/htmlsingle/#mvc-ann-async)

