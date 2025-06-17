---
title: MVC Test
linkTitle: MVC Test
description: "Spring 3.2부터 제공하는 Test framework를 이용하여 쉽게 MVC server-side 테스트를 하는 방법에 대해 가이드한다."
url: /egovframe-development/test-tool/unit-test/mvc-test/
menu:
  depth:
    weight: 4
    parent: "unit-test"
    identifier: "mvc-test"
---
# MVC Test

## 개요

Spring mvc test framework에서는 API를 통한 Spring MVC 테스트를 지원한다. MVC Test Framework는 내부에서 TestContext를 통해 실제 스프링 구성을 로드하고, 실행 ServletContext를 사용없이 MVC 테스트가 가능하다.

### Spring mvc server-side test

기존 Spring 3.2버전까지 스프링 MVC Controller를 테스트하는 방법은 Controller를 객체화하거나 객체주입하고 Mock객체(MockHttpServletRequest, MockHttpServletResponse)를 사용하여 단위테스트를 작성하는 것이었다.
그러나 이러한 테스트 방식은 Controller내부에서 쓰이는 많은 annotation기능과 request처리과정의 로직들을 모두 검증/지원하지는 못한다는 단점이 있다. (@initBinder, @ModelAttribute, @ExceptionHandler 등…)

Spring 3.2부터는 Spring mvc test framework에서 Spring MVC Test를 보다 쉽고 간편하게 할 수 있는 방법을 제시한다.

Spring MVC Test는 "mock"구현을 기반으로하며 서블릿 컨테이너 실행 없이 동작하므로 JSP렌더링을 제외한 Request, Response처리가 동작한다. 물론 forward/redirect가 실제 동작하는 것이 아니며 "forward"또는 "redirect"로 호출된 URL이 저장되며 test코드 내부에서 예상값을 확인해볼 수 있다.

Spring MVC Test에서는 JSP를 포함한 Freemarker, Velocity, Thymeleaf와 같은 뷰 타입도 지원하며 HTML, JSON, XML타입의 렌더링 등 다양한 처리방식을 지원하고 있다.

Spring MVC Test에 대해 살펴보기에 앞서 테스트 코드 예를 살펴보자.
다음은 JSON요청 사용 예이다.

```java
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.springframework.test.web.servlet.MockMvcBuilder.*;

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration("test-servlet-context.xml")
public class ExampleTests {

    @Autowired
    private WebApplicationContext wac;

    private MockMvc mockMvc;

    @Before
    public void setup() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(this.wac).build();
    }

    @Test
    public void getAccount() throws Exception {
        this.mockMvc.perform(get("/accounts/1").accept(MediaType.parseMediaType("application/json;charset=UTF-8")))
          .andExpect(status().isOk())
          .andExpect(content().contentType("application/json"))
          .andExpect(jsonPath("$.name").value("Lee"));
    }

}
```

위의 코드에서 MockMvc의 perform함수를 통해 "/accounts/1" url로 request를 수행하고 응답받은 response를 통해 상태값(status:200), 컨텐트 타입("application/json"), JSON으로 받은 값들을 확인할 수 있다.

#### Setup Option

MVC Test의 TestContext는 WebApplicationcontext로 동작한다.
Test이전의 setup에서는 Spring mvc test에 필요한 MockMvc의 객체를 가져와야한다. setup option에는 다음 두가지 방법이 있다.

##### 1. @ContextConfiguration로 설정을 읽어들여 SetUp하는 방법

@ContextConfiguration의 xml에서 설정을 읽어들이고 WebApplicationContext를 주입하여 mockMvc를 생성한다.

```java
@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration("my-servlet-context.xml")
public class MyWebTests {

    @Autowired
    private WebApplicationContext wac;

    private MockMvc mockMvc;

    @Before
    public void setup() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(this.wac).build();
    }

    // ...

}
```

##### 2. Spring Configuration은 읽지 않고 controller객체만 생성하여 SetUp하는 방법

Controller가 생성되면서 기본 Spring mvc가 구성된다.

```java
public class MyWebTests {

    private MockMvc mockMvc;

    @Before
    public void setup() {
        this.mockMvc = MockMvcBuilders.standaloneSetup(new AccountController()).build();
    }

    // ...

}
```

Web MVC Layer의 구성에 따라 bean들이 호출되기 위해서는 설정 정보가 필요하기 때문에 첫번째 setUp방식을 권장한다.

#### Static Import

테스트코드 사용 시, 필요한 API는 Static Import를 선언하여 편리하게 바로 호출해주는 것이 좋다.
예를 들어 MockMvcRequestBuilders.\*, MockMvcResultMatchers.\*클래스 등과 같이 많이 쓰는 것들은 Static Import로 선언해주도록 한다.

```java
import static org.springframework.test.web.server.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.server.result.MockMvcResultMatchers.*;
```

#### MVC 테스트

다음은 Spring mvc 테스트코드에서 사용 가능한 MockMvc 함수이다.

| 함수명      | 설명                                                                | 예                                                                   |
| ----------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| perform     | 해당 경로로 요청하며 이때 호출할 URL과 HTTP METHOD를 설정할 수 있다 | .perform(get("/account/1")                                           |
| param       | 파라미터를 설정한다.                                                | .param("key", "value")                                               |
| cookie      | 쿠키를 설정한다.                                                    | .cookie(new Cookie("key", "value")                                   |
| sessionAttr | 세션을 설정한다.                                                    | sessionAttr("key", "value")                                          |
| accept      | response를 받을 Accept값을 설정한다.                                | .accept(MediaType.parseMediaType("application/json;charset=UTF-8"))) |
| andExpect   | 예상값의 Assert함수                                                 | andExpect(status().isOk()                                            |
| andDo       | 요청/응답에 대한 처리를 한다.                                       | andDo(print())                                                       |
| andReturn   | 리턴 처리한다.                                                      | .andReturn()                                                         |

##### Perform 함수 처리 예

request요청처리를 위해 MockMvc의 perform함수를 사용하며 내부에서 MockHttpServletRequest의 값을 설정하여 request요청을 할 수 있다.

```java
mockMvc.perform(post("/hotels/{id}", 42).accept(MediaType.APPLICATION_JSON));
```

HTTP메소드 외에 fileUpload메소드를 통해 내부에서 MockMultipartHttpServletRequest의 객체를 만들어 업로드요청을 수행할 수 있다.

```java
mockMvc.perform(fileUpload("/doc").file("a1", "ABC".getBytes("UTF-8")));
```

URI template에서 Query String 파라미터를 지정할 수도 있다.

```java
mockMvc.perform(get("/hotels?foo={foo}", "bar"));
```

또한 request파라미터를 추가할 수도 있다.

```java
mockMvc.perform(get("/hotels").param("foo", "bar"));
```

요청 URI에서 contextPath와 servletPath는 생략하는 것이 바람직하지만 요청시 Full URI와 함께 테스트해야하는 경우, request매핑이 제대로 작동하도록 contextPath와 servletPath를 설정해주도록 한다.

```java
mockMvc.perform(get("/app/main/hotels/{id}").contextPath("/app").servletPath("/main"))
```

매번 request요청 시 contextPath와 servletPath를 설정하는 것이 번거스러우므로, setup시에 미리 설정하는 것이 편리하다.

```java
public class MyWebTests {

    private MockMvc mockMvc;

    @Before
    public void setup() {
        mockMvc = standaloneSetup(new AccountController())
            .defaultRequest(get("/")
                .contextPath("/app").servletPath("/main")
                .accept(MediaType.APPLICATION_JSON).build();
    }

}
```

##### andExpect 함수 처리 예

예상 결과값을 위해 andExpect함수를 사용하며 하나 이상 사용 가능하다. MockMvcResultMatchers.\* 를 static import로 정의하여 andExpect함수 내에서 제공함수를 사용할 수 있다.MockMvcResultMatchers의 제공함수는 다음과 같이 두가지 종류가 있다.

* Response의 properties값. (response상태, header, content 등)
* 요청처리에서 발생하는 값 (Exception, Model, View, request값, session값 등)

response상태 확인 시,

```java
mockMvc.perform(get("/accounts/1")).andExpected(status().isOk());
```

andExpect함수를 여러개 사용 가능 시,

```java
mockMvc.perform(post("/persons"))
  .andExpect(status().isOk())
  .andExpect(model().attributeHasErrors("person"));
```

request요청 결과를 출력할 수도 있다. print메소드를 통해 요청 처리시 관련된 모든 결과 데이터를 출력해준다.

```java
mockMvc.perform(post("/persons"))
  .andDo(print())
  .andExpect(status().isOk())
  .andExpect(model().attributeHasErrors("person"));
```

andReturn메소드를 통해 return결과를 반환할 수도 있다.

```java
MvcResult mvcResult = mockMvc.perform(post("/persons")).andExpect(status().isOk()).andReturn();
```

같은 예상값을 테스트할 때는 setUp시에 다음과 같이 설정한다.

```java
standaloneSetup(new SimpleController())
    .alwaysExpect(status().isOk())
    .alwaysExpect(content().contentType("application/json;charset=UTF-8"))
    .build()
```

##### addFilters 함수 처리 예

Filter인스턴스를 두개 이상 등록하고자 할 때, mockMvc 세팅시에 다음과 같이 필터를 추가할 수 있다.

```java
mockMvc = standaloneSetup(new PersonController()).addFilters(new CharacterEncodingFilter()).build();
```

## 참고자료

[Spring reference 3.2.x : spring-mvc-test-framework](http://docs.spring.io/spring/docs/3.2.x/spring-framework-reference/html/testing.html#spring-mvc-test-framework)
