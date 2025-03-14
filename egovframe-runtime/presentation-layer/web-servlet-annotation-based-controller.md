---
title: Annotation 기반 Controller
linkTitle: "Annotation"
description: 스프링 프레임워크는 2.5 버전부터 Java 5+ 이상에서 @Controller를 이용한 Annotation 기반 컨트롤러 개발을 지원한다. 이는 기존의 계층형 Controller(SimpleFormController, MultiActionController)와 달리 인터페이스 구현 없이 더 유연하고 간결한 방식으로 요청을 처리할 수 있는 점이 주요 개선점이다.
url : /egovframe-runtime/presentation-layer/web-servlet/web-servlet-annotation-based-controller/
menu:
    depth:
        name: Annotation
        weight: 6
        parent: "web-servlet"
---
# Annotation-based Controller

## 개요

스프링 프레임워크는 2.5 버젼 부터 Java 5+ 이상이면 @Controller(Annotation-based Controller)를 개발할 수 있는 환경을 제공한다.
인터페이스 Controller를 구현한 SimpleFormController, MultiActionController 같은 기존의 계층형(Hierarchy) Controller와의 주요 차이점 및 개선점은 아래와 같다.

- [어노테이션을 이용한 설정](#어노테이션을-이용한-설정)
  - XML 기반으로 설정하던 정보들을 어노테이션을 사용해서 정의한다.
- [유연해진 메소드 시그니쳐](#유연해진-메소드-시그니쳐)
  - Controller 메소드의 파라미터와 리턴 타입을 좀 더 다양하게 필요에 따라 선택할 수 있다.
- [POJO-Style의 Controller](#pojo-style의-controller)
  - Controller 개발시에 특정 인터페이스를 구현 하거나 특정 클래스를 상속해야할 필요가 없다.
  - 하지만 폼 처리, 다중 액션등 기존의 계층형 Controller가 제공하던 기능들을 여전히 쉽게 구현할 수 있다.

계층형 Controller로 작성된 폼 처리를 @Controller로 구현하는 예도 설명한다.
예제 코드 easycompany의 Controller는 동일한 기능(또한 공통의 Service, DAO, JSP를 사용)을 계층형 Controller와 @Controller로 각각 작성했다.

- 계층형 Controller - 패키지 com.easycompany.controller.hierarchy
- @Controller - 패키지 com.easycompany.controller.annotation


## 설명

### 어노테이션을 이용한 설정

계층형 Controller들을 사용하면 여러 정보들(요청과 Controller의 매핑 설정 등)을 XML 설정 파일에 명시 해줘야 하는데, 복잡할 뿐 아니라 설정 파일과 코드 사이를 빈번히 이동 해야하는 부담과 번거로움이 될 수 있다.
@MVC는 Controller 코드안에 어노테이션으로 설정함으로써 좀 더 편리하게 MVC 프로그래밍을 할 수 있도록 했다.
@MVC에서 사용하는 주요 어노테이션은 아래와 같다.

| 이름                 | 설명                                                                                                    |
|--------------------|-------------------------------------------------------------------------------------------------------|
| @Controller        | 해당 클래스가 Controller임을 나타내기 위한 어노테이션                                                                    |
| @RequestMapping    | 요청에 대해 어떤 Controller, 어떤 메소드가 처리할지를 맵핑하기 위한 어노테이션                                                     |
| @RequestParam      | Controller 메소드의 파라미터와 웹요청 파라미터와 맵핑하기 위한 어노테이션                                                         |
| @ModelAttribute    | Controller 메소드의 파라미터나 리턴값을 Model 객체와 바인딩하기 위한 어노테이션                                                   |
| @SessionAttributes | Model 객체를 세션에 저장하고 사용하기 위한 어노테이션                                                                      |
| @RequestPart       | Multipart 요청의 경우, 웹요청 파라미터와 맵핑가능한 어노테이션(egov 3.0, Spring 3.1.x부터 추가)                                  |
| @CommandMap        | Controller메소드의 파라미터를 Map형태로 받을 때 웹요청 파라미터와 맵핑하기 위한 어노테이션(egov 3.0부터 추가)                               |
| @ControllerAdvice  | Controller를 보조하는 어노테이션으로 Controller에서 쓰이는 공통기능들을  모듈화하여 전역으로 쓰기 위한 어노테이션(egov 3.0, Spring 3.2.X부터 추가) |

#### @Controller

@MVC에서 Controller를 만들기 위해서는 작성한 클래스에 @Controller를 붙여주면 된다. 특정 클래스를 구현하거나 상속할 필요가 없다.

```java
package com.easycompany.controller.annotation;
 
@Controller
public class LoginController {
   ...
}
```

앞서 DefaultAnnotationHandlerMapping에서 언급한 대로 `<context:component-scan>` 태그를 이용해 @Controller들이 있는 패키지를 선언해 주면 된다.
@Controller만 스캔 한다면 include, exclude 등의 필터를 사용하라.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
				http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-2.5.xsd">
 
        <context:component-scan base-package="com.easycompany.controller.annotation" />
 
</beans>
```

#### @RequestMapping

@RequestMapping은 요청에 대해 어떤 Controller, 어떤 메소드가 처리할지를 맵핑하기 위한 어노테이션이다. @RequestMapping이 사용하는 속성은 아래와 같다.

| 이름       | 타입              | 설명                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value    | String[]        | URL 값으로 맵핑 조건을 부여한다.<br> @RequestMapping(value=”/hello.do”) 또는 @RequestMapping(value={”/hello.do”, ”/world.do” })와 같이 표기하며,<br> 기본값이기 때문에 @RequestMapping(”/hello.do”)으로 표기할 수도 있다.<br> ”/myPath/*.do”와 같이 Ant-Style의 패턴매칭을 이용할 수도 있다.<br> Spring 3.1부터 URL뒤에 중괄호를 이용하여 변수값을 직접 받을 수 있도록 하였다. 아래 설명(URI Template Variable Enhancements)을 참고하라                                                                              |
| method   | RequestMethod[] | HTTP Request 메소드값을 맵핑 조건으로 부여한다.<br> HTTP 요청 메소드값이 일치해야 맵핑이 이루어 지게 한다.<br> @RequestMapping(method = RequestMethod.POST)같은 형식으로 표기한다.<br> 사용 가능한 메소드는 GET, POST, HEAD, OPTIONS, PUT, DELETE, TRACE이다                                                                                                                                                                                                                        |
| params   | String[]        | HTTP Request 파라미터를 맵핑 조건으로 부여한다.<br> params=“myParam=myValue”이면 HTTP Request URL중에 myParam이라는 파라미터가 있어야 하고 값은 myValue이어야 맵핑한다.<br> params=“myParam”와 같이 파라미터 이름만으로 조건을 부여할 수도 있고, ”!myParam”하면 myParam이라는 파라미터가 없는 요청 만을 맵핑한다.<br> @RequestMapping(params={“myParam1=myValue”, “myParam2”, ”!myParam3”})와 같이 조건을 주었다면,<br> HTTP Request에는 파라미터 myParam1이 myValue값을 가지고 있고, myParam2 파라미터가 있어야 하고, myParam3라는 파라미터는 없어야 한다. |
| consumes | String[]        | 설정과 Content-Type request헤더가 일치 할 경우에만 URL이 호출된다.                                                                                                                                                                                                                                                                                                                                                                           |
| produces | String[]        | 설정과 Accept request헤더가 일치 할 경우에만 URL이 호출된다.                                                                                                                                                                                                                                                                                                                                                                                 |

@RequestMapping은 클래스 단위(type level)나 메소드 단위(method level)로 설정할 수 있다.


**type level**

/hello.do 요청이 오면 HelloController의 hello 메소드가 수행된다.

```java
@Controller
@RequestMapping("/hello.do")
public class HelloController {
 
    @RequestMapping   //type level에서 URL을 정의하고 Controller에 메소드가 하나만 있어도 요청 처리를 담당할 메소드 위에 @RequestMapping 표기를 해야 제대로 맵핑이 된다.
    public String hello(){
	...		
    }
}
```

**method level**

/hello.do 요청이 오면 hello 메소드,
/helloForm.do 요청은 GET 방식이면 helloGet 메소드, POST 방식이면 helloPost 메소드가 수행된다.


```java
@Controller
public class HelloController {	
 
	@RequestMapping(value="/hello.do")
	public String hello(){
		...
	}
 
	@RequestMapping(value="/helloForm.do", method = RequestMethod.GET)
	public String helloGet(){
		...
	}
 
	@RequestMapping(value="/helloForm.do", method = RequestMethod.POST)
	public String helloPost(){
		...
	}	
}
```

**type + method level**
둘 다 설정할 수도 있는데, 이 경우엔 type level에 설정한 @RequestMapping의 value(URL)를 method level에서 재정의 할수 없다.

/hello.do 요청시에 GET 방식이면 helloGet 메소드, POST 방식이면 helloPost 메소드가 수행된다.

```java
@Controller
@RequestMapping("/hello.do")
public class HelloController {
 
	@RequestMapping(method = RequestMethod.GET)
	public String helloGet(){
		...
	}
 
	@RequestMapping(method = RequestMethod.POST)
	public String helloPost(){
		...
	}
}
```

AbstractController 상속받아 구현한 예제 코드 LoginController를 어노테이션 기반의 Controller로 구현해 보겠다.

기존의 LoginController는 URL /loginProcess.do로 오는 요청의 HTTP 메소드가 POST일때 handleRequestInternal 메소드가 실행되는 Controller였는데,

다음과 같이 구현할 수 있겠다.

```java
package com.easycompany.controller.annotation;
...
@Controller
public class LoginController {
 
	@Autowired
	private LoginService loginService;
 
	@RequestMapping(value = "/loginProcess.do", method = RequestMethod.POST)
	public String login(HttpServletRequest request) {
 
		String id = request.getParameter("id");
		String password = request.getParameter("password");
 
		Account account = (Account) loginService.authenticate(id,password);
 
		if (account != null) {
			request.getSession().setAttribute("UserAccount", account);
			return "redirect:/employeeList.do";
		} else {
			return "login";
		}
	}	
}
```

위 예제 코드에서 서비스 클래스를 호출하기 위해서 @Autowired가 사용되었는데 자세한 내용은 [여기](https://docs.spring.io/spring-framework/reference/core/beans/annotation-config/autowired.html)를 참고하라.

**type + method level + request**

앞의 내용에서 추가되어 request의 header설정 일치 여부에 따라 URL호출이 가능하다.

다음 예제에서 URL이 /pets로 요청된 경우, POST타입의 request의 content-type이 application/json인 경우에만 다음 메소드가 호출된다.

```java
@Controller
...
@RequestMapping(value = "/pets", method = RequestMethod.POST, consumes="application/json")
public void addPet(@RequestBody Pet pet, Model model) {
    // implementation omitted
}
```

다음 예제에서 GET타입으로 URL이 /pets/*로 요청된 경우, request의 accept header가 application/json인 경우에만 다음 메소드가 호출된다.

```java
@Controller
...
@RequestMapping(value = "/pets/{petId}", method = RequestMethod.GET, produces="application/json")
@ResponseBody
public Pet getPet(@PathVariable String petId, Model model) 
    // implementation omitted
}
```

**URI Template Variale Enhancements**

@RequestMapping의 value에 URL뒤에 중괄호로 Controller메소드의 파라미터로 받을 값의 변수명을 입력해주면 변수를 받을 수 있다.

다음 예제에서 Controller메소드의 URL을 ”/user/view/{id}“로 설정하였을 때, 만약 /user/view/12345 로 URL요청이 들어오면 view함수의 파라미터인 id가 12345로 설정된다.

```java
@RequestMapping("/user/view/{id}")
public String view(@PathVariable("id") int id) {
    // implementation omitted
}
```

**@RequestParam**

@RequestParam은 Controller 메소드의 파라미터와 웹요청 파라미터와 맵핑하기 위한 어노테이션이다.
관련 속성은 아래와 같다.

| 이름       | 타입      | 설명                                  |
|----------|---------|-------------------------------------|
| value    | String  | 파라미터 이름                             |
| required | boolean | 해당 파라미터가 반드시 필수 인지 여부. 기본값은 true이다. |

아래 코드와 같은 방법으로 사용되는데,
해당 파라미터가 Request 객체 안에 없을때 그냥 null값을 바인드 하고 싶다면, pageNo 파라미터 처럼 required=false로 명시해야 한다.

name 파라미터는 required가 true이므로, 만일 name 파라미터가 null이면 org.springframework.web.bind.MissingServletRequestParameterException이 발생한다.

```java
@Controller
public class HelloController {
 
    @RequestMapping("/hello.do")
    public String hello(@RequestParam("name") String name, //required 조건이 없으면 기본값은 true, 즉 필수 파라미터 이다. 파라미터 name이 존재하지 않으면 Exception 발생.
			@RequestParam(value="pageNo", required=false) String pageNo){ //파라미터 pageNo가 존재하지 않으면 String pageNo는 null.
	...		
    }
}
```

위에서 작성한 LoginController의 login 메소드를 보면 파라미터 아이디와 패스워드를 Http Request 객체에서 getParameter 메소드를 이용해 구하는데,

@RequestParam을 사용하면 아래와 같이 변경할수 있다.

```java
package com.easycompany.controller.annotation;
...
@Controller
public class LoginController {
 
	@Autowired
	private LoginService loginService;
 
	@RequestMapping(value = "/loginProcess.do", method = RequestMethod.POST)
	public String login(
			HttpServletRequest request,
			@RequestParam("id") String id,
			@RequestParam("password") String password) {		
 
		Account account = (Account) loginService.authenticate(id,password);
 
		if (account != null) {
			request.getSession().setAttribute("UserAccount", account);
			return "redirect:/employeeList.do";
		} else {
			return "login";
		}
	}
}
```

#### @ModelAttribute

@ModelAttribute의 속성은 아래와 같다.

| 이름    | 타입     | 설명                  |
|-------|--------|---------------------|
| value | String | 바인드하려는 Model 속성 이름. |

@ModelAttribute는 실제적으로 ModelMap.addAttribute와 같은 기능을 발휘하는데, Controller에서 2가지 방법으로 사용된다.

**1.메소드 리턴 데이터와 Model 속성(attribute)의 바인딩**

메소드에서 비지니스 로직(DB 처리같은)을 처리한 후 결과 데이터를 ModelMap 객체에 저장하는 로직은 일반적으로 자주 발생한다.

```java
...
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public String formBackingObject(@RequestParam("deptid") String deptid, ModelMap model) {
		Department department = departmentService.getDepartmentInfoById(deptid); //DB에서 부서정보 데이터를 가져온다.
		model.addAttribute("department", department); //데이터를 모델 객체에 저장한다.
		return "modifydepartment";
	}
...
```

@ModelAttribute를 메소드에 선언하면 해당 메소드의 리턴 데이터가 ModelMap 객체에 저장된다.
위 코드를 아래와 같이 변경할수 있는데, 사용자로 부터 GET방식의 /updateDepartment.do 호출이 들어오면,
formBackingObject 메소드가 실행 되기 전에 DefaultAnnotationHandlerMapping이 org.springframework.web.bind.annotation.support.HandlerMethodInvoker을 이용해서
(@ModelAttribute가 선언된)getEmployeeInfo를 실행하고, 결과를 ModelMap객체에 저장한다.
결과적으로 getEmployeeInfo 메소드는 ModelMap.addAttribute(“department”, departmentService.getDepartmentInfoById(…)) 작업을 하게 되는것이다.

```java
...
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public String formBackingObject() {
		return "modifydepartment";
	}
 
	@ModelAttribute("department")
	public Department getEmployeeInfo(@RequestParam("deptid") String deptid){
		return departmentService.getDepartmentInfoById(deptid); //DB에서 부서정보 데이터를 가져온다.
	}
	또는
	public @ModelAttribute("department") Department getDepartmentInfoById(@RequestParam("deptid") String deptid){
		return departmentService.getDepartmentInfoById(deptid);
	}
...
```

**2.메소드 파라미터와 Model 속성(attribute)의 바인딩**

@ModelAttribute는 ModelMap 객체의 특정 속성(attribute) 메소드의 파라미터와 바인딩 할때도 사용될수 있다.
아래와 같이 메소드의 파라미터에 ”**@ModelAttribute(“department”) Department department**” 선언하면 department에는 **(Department)ModelMap.get(“department”)** 값이 바인딩된다.
따라서, 아래와 같은 코드라면 formBackingObject 메소드 파라미터 department에는 getDepartmentInfo 메소드가 ModelMap 객체에 저장한 Department 데이터가 들어 있다.

```java
...
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public String formBackingObject(@ModelAttribute("department") Department department) { //department에는 getDepartmentInfo에서 구해온 데이터들이 들어가 있다.
		System.out.println(employee.getEmployeeid());
		System.out.println(employee.getName());
		return "modifydepartment";
	}
 
	@ModelAttribute("department")
	public Department getDepartmentInfo(@RequestParam("deptid") String deptid){
		return departmentService.getDepartmentInfoById(deptid); //DB에서 부서정보 데이터를 가져온다.
	}
...
```

#### @SessionAttributes

@SessionAttributes는 model attribute를 session에 저장, 유지할 때 사용하는 어노테이션이다. @SessionAttributes는 클래스 레벨(type level)에서 선언할 수 있다. 관련 속성은 아래와 같다.

| 이름    | 타입       | 설명                                 |
|-------|----------|------------------------------------|
| types | Class[]  | session에 저장하려는 model attribute의 타입 |
| value | String[] | session에 저장하려는 model attribute의 이름 |

#### @RequestParam

Multipart request의 경우, 넘겨받은 Contents의 Content-Type에 따라 HttpMessageConverter를 통해 해당 타입대로 multipart컨텐츠를 얻을 때 사용하는 어노테이션이다.

예를 들어 다음과 같이 요청이 multipart로 들어올 때

```
POST /someUrl
Content-Type: multipart/mixed
 
--edt7Tfrdusa7r3lNQc79vXuhIIMlatb7PQg7Vp
Content-Disposition: form-data; name="meta-data"
Content-Type: application/json; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
{
  "name": "value"
}
--edt7Tfrdusa7r3lNQc79vXuhIIMlatb7PQg7Vp
Content-Disposition: form-data; name="file-data"; filename="file.properties"
Content-Type: text/xml
Content-Transfer-Encoding: 8bit
... File Data ...
```
Controller에서 요청값은 아래와 같이 받을 수 있다.

```java
@RequestMapping(value="/someUrl", method = RequestMethod.POST)
public String onSubmit(@RequestPart("meta-data") MetaData metadata,
                       @RequestPart("file-data") MultipartFile file) {
    // ...
}
```

#### @CommandMap
@CommandMap은 실행환경 3.0환경부터 추가된 Controller에서 Map형태로 웹요청 값을 받았을 때 다른 Map형태의 argument와 구분해주기 위한 어노테이션이다. @CommandMap은 파라미터 레벨(type level)에서만 선언할 수 있다.

사용 방법은 다음과 같다.

```java
   @RequestMapping("/test.do")
   public void test(HttpServletRequest request, @CommandMap Map<String, String> commandMap) {
	//생략
   }
```

자세한 사용방법은 [AnnotationCommandMapArgumentResolver](web-servlet-AnnotationCommandMapArgumentResolver.md)을 참고한다.

#### @ControllerAdvice

@ControllerAdvice 어노테이션을 통해 Controller에서 쓰이는 몇가지 어노테이션 기능들을 모듈화하여 전역으로 쓸 수 있다.
@ControllerAdvice은 @RequestMapping이 붙은 메소드를 지원하며 다음과 같은 Controller 어노테이션을 지원한다.

| 이름                | 설명                                                                              |
|-------------------|---------------------------------------------------------------------------------|
| @ExceptionHandler | @ExceptionHandler 뒤에 붙은 Exception이 발생했을 때, 전역적으로 예외처리가 가능하다.                    |
| @InitBinder       |  모델 검증과 바인딩을 하기 위한 Annotation으로써 JSR-303 빈 검증기능을 사용하는 스프링 validator를 사용할 수 있다.  |
| @ModelAttribute   |  도메인 오브젝트나 DTO프로퍼티에 요청파라미터를 한 번에 받을 수 있는 @ModelAttribute를 전역으로 사용 가능하다.         |


**@ExceptionHandler with @ControllerAdvice**

기존에는 예외발생시, AnnotationMethodHandlerExceptionResolver가 Controller내부에서 @ExceptionHandler가 붙은 메소드를 찾아 예외처리를 해준다.

Controller 내부에서만 @ExceptionHandler가 동작하기 때문에 각 Controller별로 @ExceptionHandler 메소드를 만들어야했다.

```java
@Controller
public class HelloController {
 
  @RequestMapping("/hello")
  public void hello() {    
    //DataAccessException이 일어날 가능성
  }
     
  // Controller 내부에서 DataAccessException발생시 호출
  @ExceptionHandler(DataAccessException.class)
  public ModelAndView dataAccessExceptionHandler(DataAccessException e) {
    return new ModelAndView("dataexception").addObject("msg", ex.getMessage();
  }
}
```
Spring 3.2부터는 @ControllerAdvice를 이용하여 @ExceptionHandler를 전역으로 쓸 수 있다.

@ControllerAdvice + @ExceptionHandler를 통해 각각의 Exception에 대하여 전역적인 후처리 관리가 가능해진다.

즉, Controller마다 @ExceptionHandler를 만들지 않더라도 @ControllerAdvice가 붙은 Class안에서 여러 Exception에 대한 처리가 가능한 @ExceptionHandler 메소드를 만들면 로지컬한 Exception별 후처리가 가능해지는 것이다.

@ControllerAdvice와 함께 @ExceptionHandler를 쓰는 방법은 다음과 같다.
다음과 같이 쓰는 경우, Controller에서 발생하는 해당 Exception들이 예외처리가 된다.


```java
@ControllerAdvice
public class CentralControllerHandler {
 
    @ExceptionHandler({EgovBizException.class})
    public ModelAndView handleEgovBizException(EgovBizException ee) {
    //생략
    }
    
    @ExceptionHandler({BaseException.class})
    public ModelAndView handleBaseException(BaseException be) {
    //생략
    }
}
```

**@InitBinder with @ControllerAdvice**

@ControllerAdvice가 붙은 Class내부에서 @InitBinder 메소드를 씀으로써 이를 전역으로 쓸 수도 있다.

- @InitBinder
  - WebDataBinder를 초기화하는 메소드를 지정할 수 있는 설정을 제공한다. WebDataBinder는 Web request parameter를 javaBean객체에 바인딩하는 특정한 DataBinder이다.
  - 일반적으로 annotation handler메소드의 command와 form객체 인자를 조사하는데 사용된다.(CustomEditor를 등록하거나 Validator를 등록할 때 쓰인다)

@ControllerAdvice 와 함께 @InitBinder를 쓰는 방법은 다음과 같다.
@InitBinder는 Controller에서 @Valid를 쓰는 경우에만 해당 파라미터의 데이터 검증이 적용된다.

Person객체를 모델바인딩 및 검증해주는 PersonValidator를 이용하는 경우이다.

```java
@ControllerAdvice
public class CentralControllerHandler {
 
    @InitBinder
    public void initBinder(WebDataBinder binder) {
    binder.setValidator(new PersonValidator());
    }
 
    //생략
}
```

이 때 Controller의 구현 예이다.

```java
@RequestMapping(value="/persons")
public void updatePerson(@Valid Person person, HttpServletRequest request, HttpServletResponse response) {
    personService.updatePerson(person);
    //생략
}
```

#### @ModelAttribute와 @ControllerAdvice

@ControllerAdvice를 통해 @ModelAttribute의 메소드 또한 전역으로 쓰일 수 있다.

```java
@ControllerAdvice
public class GlobalControllerAdvice {
 
  ... 
 
  @ModelAttribute("model")
  public Model getModel() {
    return this.model();
  }
}
```

### 유연해진 메소드 시그니쳐

@RequestMapping을 적용한 Controller의 메소드는 아래와 같은 메소드 파라미터와 리턴 타입을 사용할수 있다.

특정 클래스를 확장하거나 인터페이스를 구현해야 하는 제약이 없기 때문에 계층형 Controller 비해 유연한 메소드 시그니쳐를 갖는다.

#### @Controller의 메소드 파라미터

사용가능한 메소드 파라미터는 아래와 같다.

- Servlet API
  - ServletRequest, HttpServletRequest, HttpServletResponse, HttpSession 같은 요청,응답,세션관련 Servlet API들
- WebRequest, NativeWebRequest
  - org.springframework.web.context.request.WebRequest, org.springframework.web.context.request.NativeWebRequest
- java.util.Locale
- java.io.InputStream / java.io.Reader
- java.io.OutputStream / java.io.Writer
- @RequestParam
  - HTTP Request의 파라미터와 메소드의 argument를 바인딩하기 위해 사용하는 어노테이션
- java.util.Map / org.springframework.ui.Model / org.springframework.ui.ModelMap
  - 뷰에 전달할 모델데이터들
 - Command/form 객체
   - HTTP Request로 전달된 parameter를 바인딩한 커맨드 객체, @ModelAttribute을 사용하면 alias를 줄수 있다.
 - Errors, BindingResult
   - org.springframework.validation.Errors / org.springframework.validation.BindingResult 유효성 검사후 결과 데이터를 저장한 객체
 - SessionStatus
   - org.springframework.web.bind.support.SessionStatus 세션폼 처리시에 해당 세션을 제거하기 위해 사용된다.

메소드는 임의의 순서대로 파라미터를 사용할수 있다. 단, BindingResult가 메소드의 argument로 사용될 때는 바인딩 할 커맨드 객체가 바로 앞에 와야 한다.

```java
public String updateEmployee(...,@ModelAttribute("employee") Employee employee,			
			BindingResult bindingResult,...) /* (O) */
 
public String updateEmployee(...,BindingResult bindingResult,
                        @ModelAttribute("employee") Employee employee,...) /* (X) */
```

**이 외의 타입을 메소드 파라미터로 사용하려면?**

스프링 프레임워크는 위에서 언급한 타입이 아닌 custom arguments도 메소드 파라미터로 사용할 수 있도록 org.springframework.web.bind.support.WebArgumentResolver라는 인터페이스를 제공한다.

WebArgumentResolver를 사용한 예제는 [이곳](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte:ptl:controller:commandmapargumentresolver)을 참고


#### @Controller의 메소드 리턴 타입

사용가능한 메소드 리턴 타입은 아래와 같다.

- ModelAndView
  - 커맨드 객체와 @ModelAttribute이 적용된 메소드의 리턴 데이터가 담긴 Model 객체와 View 정보가 담겨 있다.

```java
        @RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public ModelAndView formBackingObject(@RequestParam("deptid") String deptid) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		ModelAndView mav = new ModelAndView("modifydepartment");
		mav.addObject("department", department);
		return mav;
	}
```
또는
```java
	public ModelAndView formBackingObject(@RequestParam("deptid") String deptid, ModelMap model) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		model.addAttribute("department", department);
		ModelAndView mav = new ModelAndView("modifydepartment");
		mav.addAllObjects(model);
		return mav;
	}
```

- Model (또는 ModelMap)
  - 커맨드 객체와 @ModelAttribute이 적용된 메소드의 리턴 데이터가 Model 객체에 담겨 있다.
  - View 이름은 RequestToViewNameTranslator가 URL을 이용하여 결정한다.
  - 인터페이스 RequestToViewNameTranslator의 구현클래스인 DefaultRequestToViewNameTranslator가 View 이름을 결정하는 방식은 아래와 같다.

```
http://localhost:8080/gamecast/display.html -> display
http://localhost:8080/gamecast/displayShoppingCart.html -> displayShoppingCart
http://localhost:8080/gamecast/admin/index.html -> admin/index
```

```java
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public Model formBackingObject(@RequestParam("deptid") String deptid, Model model) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		model.addAttribute("department", department);
		return model;
	}
```
또는
```java
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public Model formBackingObject(@RequestParam("deptid") String deptid) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		Model model = new ExtendedModelMap();
		model.addAttribute("department", department);
		return model;
	}
```

- Map
  - 커맨드 객체와 @ModelAttribute이 적용된 메소드의 리턴 데이터가 Map 객체에 담겨 있으며, View 이름은 역시 RequestToViewNameTranslator가 결정한다.

```java
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public Map formBackingObject(@RequestParam("deptid") String deptid) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		Map model = new HashMap();
		model.put("department", department);
		return model;
	}
```
또는
```java
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public Map formBackingObject(@RequestParam("deptid") String deptid, Map model) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		model.put("department", department);
		return model;
	}
```

- String
  - 리턴하는 String 값이 곧 View 이름이된다.
  - 커맨드 객체와 @ModelAttribute이 적용된 메소드의 리턴 데이터가 Model(또는 ModelMap)에 담겨있다.
  - 리턴할 Model(또는 ModelMap)객체가 해당 메소드의 argument에 선언되어 있어야한다.

```java
/* (O) */
@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
public String formBackingObject(@RequestParam("deptid") String deptid, ModelMap model) {
    Department department = departmentService.getDepartmentInfoById(deptid);
    model.addAttribute("department", department);
    return "modifydepartment";
}

/* (X) */
@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
public String formBackingObject(@RequestParam("deptid") String deptid) {
    Department department = departmentService.getDepartmentInfoById(deptid);
    ModelMap model = new ModelMap();
    model.addAttribute("department", department);
    return "modifydepartment";
}
```

- View
  - View를 리턴한다. 커맨드 객체와 @ModelAttribute이 적용된 메소드의 리턴 데이터가 Model(또는 ModelMap)에 담겨 있다.
- void
  - 메소드가 ServletResponse / HttpServletResponse등을 사용해서 직접 응답을 처리하는 경우. View 이름은 RequestToViewNameTranslator가 결정한다.

### POJO-Style의 Controller

@MVC는 Controller 개발시에 특정 인터페이스를 구현 하거나 특정 클래스를 상속해야할 필요가 없다.

Controller의 메소드에서 Servlet API를 반드시 참조하지 않아도 되며, 훨씬 유연해진 메소드 시그니쳐로 개발이 가능하다.

여기서는 SimpleFormController의 폼 처리 액션을 @Controller로 구현함으로써, POJO-Style에 가까워졌지만 기존의 계층형 Controller에서 제공하던 기능들을 여전히 구현할 수 있음을 보이고자 한다.

#### FormController by SimpleFormController -> @Controller

앞서 SimpleFormController을 설명하면서 예제로 작성된 com.easycompany.controller.hierarchy.UpdateDepartmentController를 @ModelAttribute와 @RequestMapping을 이용해서 같은 기능을 @Controller로 작성해 보겠다.

JSP 소스는 동일한 것을 사용한다. [이곳](web-servlet-controller.md#simpleformcontroller)의 예제 화면 이미지 및 JSP 코드를 참고.
기존의 UpdateDepartmentController를 보면 3가지 메소드로 이루어졌다.

- referenceData
  - 입력폼에 필요한 참조데이터인 상위부서정보를 가져와서 Map 객체에 저장한다. 이후에 이 Map 객체는 스프링 내부 로직에 의해 ModelMap 객체에 저장된다.
- formBackingObject
  - GET 방식 호출일때 초기 입력폼에 들어갈 부서 데이터를 리턴한다. 이 데이터 역시 ModelMap 객체에 저장된다.
- onSubmit
  - POST 전송시에 호출되며 폼 전송을 처리한다.

```java
package com.easycompany.controller.hierarchy;
...
 
public class UpdateDepartmentController extends SimpleFormController{
 
	private DepartmentService departmentService;
 
	public void setDepartmentService(DepartmentService departmentService){
		this.departmentService = departmentService;
	}
 
	//상위부서리스트(selectbox)는 부서정보클래스에 없으므로 , 상위부서리스트 데이터를 DB에서 구해서 별도의 참조데이터로 구성한다.
	@Override
	protected Map referenceData(HttpServletRequest request, Object command, Errors errors) throws Exception{
 
		Map referenceMap = new HashMap();
		referenceMap.put("deptInfoOneDepthCategory",departmentService.getDepartmentIdNameList("1"));	//상위부서정보를 가져와서 Map에 담는다.
		return referenceMap;
	}
 
	@Override
	protected Object formBackingObject(HttpServletRequest request) throws Exception {
		if(!isFormSubmission(request)){	// GET 요청이면
			String deptid = request.getParameter("deptid");
			Department department = departmentService.getDepartmentInfoById(deptid);//부서 아이디로 DB를 조회한 결과가 커맨드 객체 반영.
			return department;
		}else{	// POST 요청이면
			//AbstractFormController의 formBackingObject을 호출하면 요청객체의 파라미터와 설정된 커맨드 객체간에 기본적인 데이터 바인딩이 이루어 진다.
			return super.formBackingObject(request);
		}
	}
 
	@Override
	protected ModelAndView onSubmit(HttpServletRequest request,
			HttpServletResponse response, Object command, BindException errors) throws Exception{
 
		Department department = (Department) command;
 
		try {
			departmentService.updateDepartment(department);
		} catch (Exception ex) {
			return showForm(request, response, errors);
		}
 
		return new ModelAndView(getSuccessView(), "department", department);
	}
}
```

@Controller로 작성된 com.easycompany.controller.annotation.UpdateDepartmentController은 3개의 메소드로 이루어져 있다.

계층형 Controller인 기존의 UpdateDepartmentController와는 달리 각 메소드는 Override 할 필요없기 때문에 메소드 이름은 자유롭게 지을 수 있다.

쉬운 비교를 위해 SimpleFormController과 동일한 메소드 이름을 선택했다.

- referenceData
  - 입력폼에 필요한 참조데이터인 상위부서정보를 가져와서 ModelMap에 저장한다.(by @ModelAttribute)
- formBackingObject
  - GET 방식 호출일때 처리를 담당한다. 초기 입력폼 구성을 위한 부서데이터를 가져와서 ModelMap에 저장한다.
- onSubmit
  - POST 전송시에 호출되며 폼 전송을 처리한다.

(POJO에 가까운) 프레임워크 코드들은 감춰졌고, 보다 직관적으로 비지니스 내용을 표현할 수 있게 되었다고 생각한다.

```java
package com.easycompany.controller.annotation;
 
...
@Controller
public class UpdateDepartmentController {
 
	@Autowired
	private DepartmentService departmentService;
 
	//상위부서리스트(selectbox)는 부서정보클래스에 없으므로 , 상위부서리스트 데이터를 DB에서 구해서 별도의 참조데이터로 구성한다.
	@ModelAttribute("deptInfoOneDepthCategory")
	public Map<String, String> referenceData() {
		return departmentService.getDepartmentIdNameList("1");
	}
 
	// 해당 부서번호의 부서정보 데이터를 불러와 입력폼을 채운다
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.GET)
	public String formBackingObject(@RequestParam("deptid") String deptid, ModelMap model) {
		Department department = departmentService.getDepartmentInfoById(deptid);
		model.addAttribute("department", department); //form tag의 commandName은 이 attribute name과 일치해야 한다. <form:form commandName="department">.
		return "modifydepartment";
	}
 
	//사용자가 데이터 수정을 끝내고 저장 버튼을 누르면 수정 데이터로 저장을 담당하는 서비스(DB)를 호출한다.
	//저장이 성공하면 부서리스트 페이지로 이동하고 에러가 있으면 다시 입력폼페이지로 이동한다.
	@RequestMapping(value = "/updateDepartment.do", method = RequestMethod.POST)
	public String onSubmit(@ModelAttribute("department") Department department, BindingResult bindingResult) {
 
		//validation code
		new DepartmentValidator().validate(department, bindingResult);		
		if(bindingResult.hasErrors()){
			return "modifydepartment";
		}
 
		try {
			departmentService.updateDepartment(department);
			return "redirect:/departmentList.do?depth=1";
		} catch (Exception e) {
			e.printStackTrace();
			return "modifydepartment";
		}
	}
}
```

## 참고자료

- [The Spring Framework - Reference Documentation 2.5.6](https://docs.spring.io/spring-framework/docs/2.5.x/reference/index.html)
- [Spring Framework API Documentation 2.5.6](https://docs.spring.io/spring-framework/docs/2.5.6/javadoc-api/)
- [SpringSource Team Blog,Annotated Web MVC Controllers in Spring 2.5, Juergen Hoeller](https://spring.io/blog/2007/11/14/annotated-web-mvc-controllers-in-spring-2-5)