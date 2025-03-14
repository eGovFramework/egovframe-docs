---
title: View
linkTitle: "View"
description: Controller는 요청을 처리한 후 View 이름과 데이터를 ModelAndView에 저장해 DispatcherServlet에 반환하고, DispatcherServlet은 ViewResolver를 통해 실제 View 객체를 얻는다. 이 View는 Model 객체의 정보를 출력하며, 스프링은 JSP에서 편리한 데이터 출력을 위해 Spring form tag library를 제공한다.
url : /egovframe-runtime/presentation-layer/web-servlet-declarative-validation/web-servlet-view/
menu:
    depth:
        name: View
        weight: 1
        parent: "bean_vaildation"
---
# View

## 개요

Controller가 요청에 대한 처리를 하고, View 이름과 데이터(Model)를 ModelAndView에 저장해 DispatcherServlet에 반환(return)하면,
DispatcherServlet은 View 이름을 가지고 ViewResolver에게서 실제 View 객체를 얻고, 이 View는 Controller가 저장한 Model 객체의 정보를 출력한다.
여기서는 View와 ViewResolver, 그리고 JSP에서 편리한 데이터 출력을 위해 스프링이 제공하는 Spring form tag library에 대해서 설명한다.

- [View](#view)
	- [개요](#개요)
	- [설명](#설명)
		- [ViewResolver](#viewresolver)
			- [InternalResourceViewResolver/UrlBasedViewResolver](#internalresourceviewresolverurlbasedviewresolver)
		- [View](#view-1)
		- [Spring Tag Library](#spring-tag-library)
			- [meassage tag(`<spring:message>`)](#meassage-tagspringmessage)
			- [form tag(`<form:form>,<form:input>,...`)](#form-tagformformforminput)
		- [전자정부프레임워크 Tag Library](#전자정부프레임워크-tag-library)
	- [참고자료](#참고자료)

## 설명

### ViewResolver

Controller는 코드내에서 실제 View 객체를 생성하지 않고 View 이름만을 결정할 수 있는데, 이로써 Controller와 View의 분리(decoupling)를 가능하게 한다.

```java
package com.easycompany.controller.hierarchy;
...
public class EmployeeListController extends AbstractCommandController{
        ...
	@Override
	protected ModelAndView handle(HttpServletRequest request,
			HttpServletResponse response, Object command, BindException errors)
			throws Exception {
		...
		List<Employee> employeelist = employeeService.getAllEmployees(commandMap);
 
		ModelAndView modelview = new ModelAndView();
		modelview.addObject("employeelist", employeelist);
		...
		//직접 View 객체를 생성하지 않고,
		//View view = new InternalResourceView("/jsp/employeelist.jsp"); 
		//modelview.setView(view);
		//View 이름만을 저장.
		modelview.setViewName("employeelist");
 
		return modelview;
	}
}
```

이때, DispatcherServlet에 실제 View 객체를 구해주는건 Controller가 아니라 ViewResolver가 담당한다.
ViewResolver는 Controller가 반환한 ModelAndView 객체에 담긴 View 이름을 가지고 실제 View 객체를 반환하는 인터페이스이다.
Spring에서 제공하는 ViewResolver 구현 클래스는 아래와 같다.

| ViewResolver                                      | 설명                                                                                                                |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| XmlViewResolver                                   | View이름과 View 클래스간의 매핑정보가 담긴 XML로 부터 View이름에 해당하는 View를 구한다.<br> 기본설정 파일은 /WEB-INF/views.xml이다.                    |
| ResourceBundleViewResolver                        | View이름과 View 클래스간의 매핑정보가 담긴 리소스 번들(프로퍼티파일)로 부터 View 이름에 해당하는 View를 구한다.<br> 기본설정 파일은 views.properties이다.          |
| InternalResourceViewResolver/UrlBasedViewResolver | 특정 디렉토리 경로의 JSP파일들을 호출할 때 편리하게 사용할수 있다.<br> 기본적으로 사용하는 View 클래스는 InternalResourceView이며, View 이름이 곧 JSP 파일이름이 된다. |
| VelocityViewResolver /FreeMarkerViewResolver      | Velocity/FreeMarker 연동시에 사용한다.                                                                                    |

#### InternalResourceViewResolver/UrlBasedViewResolver

비지니스 로직 처리가 끝난 후 ”/jsp/main/abc.jsp” 경로의 JSP 파일로 forwarding하는 Controller가 있다고 하면, InternalResourceViewResolver/UrlBasedViewResolver를 사용해서 아래와 같이 Controller를 작성하고, 빈 정의 파일에 설정할 수 있다.

```xml
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver"/>
```
또는
```xml
<bean class="org.springframework.web.servlet.view.UrlBasedViewResolver "/>
```

```java
@Controller
public class HelloController {
	@RequestMapping("...")
	public String hello(){
		... //비지니스 로직 처리.
		return "/jsp/main/abc.jsp"; //뷰이름이 곧 JSP 파일의 경로.
	}	
}
```
InternalResourceViewResolver/UrlBasedViewResolver의 프로퍼티 prefix, suffix를 사용하면 좀더 간단하게 처리할수 있는데,
JSP가 특정 디렉토리 경로 아래에 있고, 예를 들어 /jsp/main 디렉토리 아래, 확장자는 .jsp 이라면,

```xml
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver"
	p:prefix="/jsp/main/" p:suffix=".jsp" />
```
또는
```xml
<bean class="org.springframework.web.servlet.view.UrlBasedViewResolver"
	p:prefix="/jsp/main/" p:suffix=".jsp" />
```

```java
@Controller
public class HelloController {
	@RequestMapping("...")
	public String hello(){
		...
		return "abc"; //prefix와 suffix를 제외한 부분만 표기.
	}	
}
```
간단히 뷰이름을 설정할 수 있다.

### View

Spring이 제공하는 View 클래스를 사용할 수도 있지만, UI Tool 등과의 연동등으로 인해 View 클래스를 직접 작성해야 하는 경우도 발생한다.
인터페이스 View를 직접 구현해서 View 클래스를 만들수도 있지만, AbstractView를 확장하여 구현해보자.
renderMergedOutputModel 메소드를 구현하면 되는데, 아래와 같은 메소드 시그니쳐를 가지고 있다.

```java
protected abstract void renderMergedOutputModel(Map model,
                                                HttpServletRequest request,
                                                HttpServletResponse response) throws Exception
```

AjaxTags란 Ajax 관련 오픈소스 사용을 위해 Model 객체의 데이터를 'text/xml' 형식으로 렌더링하는 View 클래스를 만들어 봤다.

```java
package com.easycompany.view;
 
import java.io.PrintWriter;
import java.util.Map;
 
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
 
import org.springframework.web.servlet.view.AbstractView;
 
public class AjaxXmlView extends AbstractView {
 
	@Override
	protected void renderMergedOutputModel(Map model,
			HttpServletRequest request, HttpServletResponse response)
			throws Exception {
 
		response.setContentType("text/xml");
		response.setHeader("Cache-Control", "no-cache");
		response.setCharacterEncoding("UTF-8");
 
		PrintWriter writer = response.getWriter();
		writer.write((String) model.get("ajaxXml"));
		writer.close();
	}
}
```

### Spring Tag Library

#### meassage tag(`<spring:message>`)

스프링은 메시지 리소스 파일로 부터 메시지를 가져와 간편하게 출력할수 있도록, `<spring:message>` 태그를 제공한다.
JSP 페이지의 타이틀을 `<spring:message>`를 이용해서 출력하는 예제를 만들어 보자.
빈 정의 파일에 리소스 번들 관련된 설정이 되어 있어야 한다.

```xml
<!-- Message Source-->
<bean id="messageSource" class="org.springframework.context.support.ResourceBundleMessageSource"
	p:basename="messages"/>
```

먼저 메시지 관련 리소스 파일에 코드값을 설정해준다. PropertiedEditor 같은 유틸의 도움을 받으면 편리하게 한글 입력-편집이 가능하다.

/easycompany/webapp/WEB-INF/classes/messages_ko.properties

```properties
...
# -- spring:message --
easaycompany.loginform.title=로그인페이지
easaycompany.employeelist.title=사원 정보 리스트 페이지
easaycompany.updateemployee.title=사원 정보 수정 페이지
easaycompany.insertemployee.title=사원 정보 입력 페이지
easaycompany.departmentlist.title=부서 정보 리스트 페이지
easaycompany.updatedepartment.title=부서 정보 수정 페이지
easaycompany.insertdepartment.title=부서 정보 입력 페이지
```

JSP 페이지에 커스텀 태그를 사용하기 위해 라이브러리 선언을 해줘야 한다. 그리고 `<spring:message>` 태그의 code 값에는 메시지 키값을 주면 된다.

```jsp
...
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title><spring:message code="easaycompany.departmentlist.title"/></title>
...
```

해당 화면의 타이틀이 “부서 정보 리스트 페이지”로 표기 될 것이다.

#### form tag(`<form:form>,<form:input>,...`)

폼 관련 어플리케이션을 개발할 때는 스프링이 제공하는 폼 태그와 같이 사용하면 편리하다.
스프링 폼 태그는 Model 데이터의 커맨드 객체(command object)나 참조 데이터(reference data)들을 화면상에서 쉽게 출력하도록 도와 준다.
일단, 스프링 폼 태그를 사용하려면 페이지에 커스텀 태그 라이브러리를 선언해야 한다.

```jsp
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
```

스프링 폼 태그에는 아래와 같은 태그들이 있다.

***<form:form>***

`<form:form>`는 속성 commandName에 정의된 model attribute를 PageContext에 저장해서, `<form:input>`이나 `<form:hidden>`같은 tag들이 접근할 수 있도록 한다.
관련 속성은 아래와 같다.

- commandName
  - 참조하려는 model attribute 이름
- action
  - 폼 전송할 URL
- method
  - 폼 전송시에 HTTP 메소드(GET, POST)
- enctype
  - 폼 전송시에 데이터 인코딩 타입

`<form:form>` 태그를 사용하고 출력된 페이지에서 소스 보기로 HTML 코드를 열어보면 아래와 같이 HTML FORM 태그가 출력된걸 확인할 수 있을것이다.

```jsp
<form:form commandName="department" action="http://myUrl..." method="post"> -> <form id="department" action="http://myUrl..." method="post">
 
<form:form commandName="department"> -> <form id="department" action="현재페이지 URL" method="post">
```


***<form:input>***

HTML text타입의 input 태그에 commandName에 지정된 객체 프로퍼티를 바인딩하기 위해 사용한다.
path에 프로퍼티 이름을 적으면, text타입의 input 태그의 id, name 값이 프로퍼티 이름이 되고, value는 해당 프로퍼티의 값이 된다.

```jsp
<form:form commandName="department">
	<tr>
		<th>부서이름</th>
		<td><form:input path="deptname" size="20"/></td>
	</tr>
</form:form>
```

아래와 같이 HTML로 출력된다.

```html
<form id="department" action="/easycompany/updateDepartment.do?deptid=1100" method="post">
	<tr>
		<th>부서이름</th>
		<td><input id="deptname" name="deptname" type="text" value="회식메뉴혁신팀" size="20"/></td>
	</tr>
</form>
```

***<form:password>***

HTML password타입의 input 태그에 commandName에 지정된 객체 프로퍼티를 바인딩하기 위해 사용한다.
바인딩값을 표기하기 위해서는 showPassword 속성을 showPassword=“true”로 지정해 주어야 한다.

***<form:hidden>***

HTML hidden타입의 input 태그에 commandName에 지정된 객체 프로퍼티를 바인딩하기 위해 사용한다.

***<form:select>, <form:options>, <form:option>***

HTML select, option 태그에 commandName에 지정된 객체 프로퍼티를 바인딩하기 위해 사용한다.
아래와 같이 `<form:select>`의 path 속성에 commandName 객체의 프로퍼티를 지정하고,
`<form:options>`의 items 속성에 List, Map등의 Collection 객체를 값으로 주면,

```jsp
<form:form commandName="department">
	<tr>
		<th>상위부서</th>
		<td>
			<form:select path="superdeptid">
				<option value="">상위부서를 선택하세요.</option>
				<form:options items="${deptInfoOneDepthCategory}" />
			</form:select>
		</td>
	</tr>
</form:form>
```

아래와 같이 HTML로 출력된다. `<form:select>`의 path 속성값과 일치하는 option 값이 있으면 `selected=“selected”` 된다.

```jsp
<form id="department" action="/easycompany/updateDepartment.do?deptid=1100" method="post">
	<tr>
		<th>상위부서</th>
		<td>
			<select id="superdeptid" name="superdeptid">
				<option value="">상위부서를 선택하세요.</option>
				<option value="5000">금융사업부</option>
                                <option value="3000">IT연구소</option>
                                <option value="4000">공공사업부</option>
                                <option value="1000" selected="selected">경영기획실</option>
                                <option value="2000">경영지원실</option>
			</select>
		</td>
	</tr>
</form>
```

***<form:checkboxes>***

***<form:checkbox>***

***<form:errors>***

### 전자정부프레임워크 Tag Library

**`<ui:pagination/>`**

페이징 처리의 편의를 위해 `<ui:pagination/>` 태그를 제공한다.
`<ui:pagination/>`의 주요 속성은 아래와 같다.

| 이름             | 설명                                                                                             | 필수여부 |
|----------------|------------------------------------------------------------------------------------------------|------|
| paginationInfo | 페이징리스트를 만들기 위해 필요한 데이터. 데이터 타입은 egovframework.rte.ptl.mvc.tags.ui.pagination.PaginationInfo이다. | yes  |
| type           | 페이징리스트 렌더링을 담당할 클래스의 아이디. 이 아이디는 빈설정 파일에 선언된 프로퍼티 rendererType의 key값이다.                        | yes  |
| jsFunction     | 페이지 번호에 걸리게 될 자바스크립트 함수 이름. 페이지 번호가 기본적인 argument로 전달된다.                                       | yes  |

ui 태그에 대한 라이브러리 선언을 해주고 페이징 리스트가 위치할 곳에 아래와 같이 사용하면 된다.
paginationInfo 속성에는 Controller에서 Model 객체에 저장한 PaginationInfo의 attribute name을 적어 주면 되고,
jsFunction 속성은 페이징 리스트의 각 페이지 번호에 걸릴 링크인 자바스크립트 함수명을 적어 주면 된다.
type 속성은 빈 설정시에 rendererType 프로퍼티의 entry key값을 적어준다. 렌더링 타입을 태그에서 결정하는 것이다.

**1. 관련 클래스 빈 설정한다.**

```xml
<!-- For Pagination Tag -->	 
<bean id="imageRenderer" class="com.easycompany.tag.ImagePaginationRenderer"/>

<bean id="textRenderer" class="egovframework.rte.ptl.mvc.tags.ui.pagination.DefaultPaginationRenderer"/>

<bean id="paginationManager" class="egovframework.rte.ptl.mvc.tags.ui.pagination.DefaultPaginationManager">
    <property name="rendererType">
        <map>
            <entry key="image" value-ref="imageRenderer"/>
            <entry key="text" value-ref="textRenderer"/>
        </map>
    </property>
</bean>
```

**2. JSP에서 라이브러리를 선언한 후 사용한다.**

```jsp
<%@ taglib prefix="ui" uri="http://egovframework.gov/ctl/ui"%>
...
<script type="text/javascript">
	function linkPage(pageNo){
		location.href = "/easycompany/employeeList.do?pageNo="+pageNo;
	}	
</script>
<body>
...
		<ui:pagination paginationInfo = "${paginationInfo}"
			type="image"
			jsFunction="linkPage"/>
...
</body>
```

`<ui:pagination/>`에 대한 좀더 상세한 설명과 사용법, 확장 방법등은 [이곳](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte:ptl:view:paginationtag)을 참고

## 참고자료

- The Spring Framework - Reference Documentation 2.5.6
- Spring Framework API Documentation 2.5.6










