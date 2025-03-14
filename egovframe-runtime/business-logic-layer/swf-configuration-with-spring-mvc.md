---
title: Spring Web Flow와 Spring MVC 연동
linkTitle: "MVC 연동"
description: Spring Web Flow는 Spring MVC와 연동해 웹 애플리케이션을 개발할 수 있으며, 이를 위해 web.xml에 DispatcherServlet 설정이 필요하다. DispatcherServlet은 웹 애플리케이션별로 등록되며, 요청 경로와 초기화 파라미터(contextConfigLocation)를 설정한다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-configuration-with-spring-mvc/
menu:
    depth:
        name: MVC 연동
        weight: 2
        parent: "swf-configuration"
---
## Spring Web Flow 와 MVC 연동

Spring Web Flow를 사용하여 웹을 개발할 때 Spring MVC와 연동하여 개발할 수 있다. 이를 위해 Spring MVC 연동 모듈 등을 설정해야 한다.
여기서는 booking-mvc sample( 실행데모(faces이지만 시나리오는 같음) )을 기준으로 설정하겠다.

## 설명

Spring MVC 와의 연동을 위해 우리는 web.xml 안에 있는 DispatcherServlet 설정을 보도록 하겠다.

### web.xml 환경 구성

Spring MVC를 구성하는 첫 단계는 web.xml에 DispatcherServlet을 구성하는 것이다.
DispatcherServlet은 웹 애플리케이션별 하나를 등록한다.

이 예제에서는 /spring/으로 시작하는 모든 요청을 받도록 설정하고 있다. init-param을 사용해 contextConfigLocation을 설정하고 있다.

**web.xml**

```xml
<servlet>
	<servlet-name>Spring MVC Dispatcher Servlet</servlet-name>
	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	<init-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/web-application-config.xml</param-value>
	</init-param>
</servlet>
<servlet-mapping>
	<servlet-name>Spring MVC Dispatcher Servlet</servlet-name>
	<url-pattern>/spring/*</url-pattern>
</servlet-mapping>
```

### Flow로 전달

DispatcherServlet은 애플리케이션 자원에 대한 요청과 핸들러를 매핑시켜 준다. Flow도 핸들러의 하나의 유형으로 처리된다.

#### FlowHandlerAdapter 등록 및 Flow 매핑 정의

먼저 FlowHandlerAdapter Bean을 정의하고 나서 property(flowExecutor)로 flowExecutor 빈을 설정함으로써
Spring MVC 내에서 Flow를 제어할 수 있도록 한다.

```xml
<!-- Enables FlowHandler URL mapping -->
<bean class="org.springframework.webflow.mvc.servlet.FlowHandlerAdapter">
	<property name="flowExecutor" ref="flowExecutor" />
</bean>
```

이 설정은 Dispatcher가 애플리케이션 자원 경로를 flow registry에 등록된 Flow로 매핑할 수 있도록 해준다.
예를 들어, /hotels/booking 요청은 hotels/booking 이란 Flow ID를 갖는 Flow에게 요청이 가게 된다.
flow registry에서 해당 ID 못 찾게 되면, Dispatcher의 순서에 따라 다음 핸들러 매핑에서 찾고, 없다면 “noHandlerFound”(?) 응답이 반환되게 된다.

#### 작업 흐름을 제어하는 Flow

조건에 맞는 flow가 매핑되면 FlowHandlerAdapter는 새로운 flow 실행을 시작할 것인지 아니면 HTTP 요청에 담겨있는 정보를 기반으로 기존 실행을 계속할 것인지를 판단하게 된다.

- HTTP 요청 파라미터는 모든 Flow 실행의 입력 맵에서 사용할 수 있다.
- Flow 실행이 마지막 응답 전송 없이 끝나는 경우, Default 핸들러가 동일한 요청을 새로이 Flow 실행을 시도(?)하게 된다
- 발생한 Excpetion이 NoSuchFlowExecutionException인 경우에는 새로이 Flow 실행을 시작해 복구 시도를 해보며, 다른 예외는 제어하지 않는다.

자세한 내용은 SWF JavaDoc 에서 FlowHandlerAdapter 클래스를 참고하길 바란다.

### 커스텀 FlowHandler 구현

FlowHandler는 HTTP 서블릿 환경에서 Flow가 실행을 커스터마이징할 수 있는 확장 영역이다.
FlowHandlerAdapter에 의해 실행/사용되며, 아래와 같은 수행을 한다.

- 실행되는 Flow의 id 반환
- Flow 실행시 입력될 값 생성
- Flow 실행이 종료되면서 반환하는 결과 처리
- Flow 실행에서 발생해서 던저진 예외 처리

이러한 수행을 위한 메소드는 org.springframework.mvc.servlet.FlowHandler 인터페이스 형태로 되어 있다.

```java
public interface FlowHandler {
 
	public String getFlowId();
 
	public MutableAttributeMap createExecutionInputMap(HttpServletRequest request);
 
	public String handleExecutionOutcome(FlowExecutionOutcome outcome, HttpServletRequest request, HttpServletResponse response);
 
	public String handleException(FlowException e,	HttpServletRequest request, HttpServletResponse response);
}
```

FlowHandler를 구현 시, AbstractFlowHandler를 상속하면 된다. 모든 연산은 선택적이 되어서, 필요할 때만 구현하면 되며,
구현하지 않으면 기본 구현 내용(AbstractFlowHandler 내에 구현된)이 적용된다.
특히 다음과 같은 경우에는 구현을 고려할 수 있다.

- getFlowId(HttpServletRequest) 재정의: HTTP 요청에서 직접적으로 Flow id를 받을 수 없을 때. 일반적으로는 요청의 URI에서 경로 정보를 얻게 됨. 예를 들어, http://localhost/app/hotels/booking?hotelId=1 는 hotels/booking이란 Flow id로 매핑 됨.
- createExecutionInputMap(HttpServletRequest) 재정의: HttpServletRequest에서 Flow 입력 파라미터를 세부적으로 직접 추출해야 하는 경우. 기본적으로는 모든 요청 파라미터가 Flow 입력 파라미터로 넘겨짐.
- handleExecutionOutcome 재정의: 직접 Flow 실행 결과를 제어할 필요가 있을 경우. 기본 행동은 Flow의 새로운 실행을 재시작하려고 마지막 Flow의 URL로 redirect 보냄.
- handleExeception 재정의: 제어되지 못한 Flow 실행을 세심하게 조정할 필요가 있는 경우. 기본적으로는 제어하지 않은 Exception은 Spring MVC ExceptionResolver로 다시 보내진다.

#### FlowHandler 예제

가장 일반적인 스프링 MVC와의 상호 작용은, Flow가 종료됐을 때 @Controller로 재전송하는 방법이다. FlowHandler는 이를 특정 controller URL을 Flow 정의와 관련 없이 가능하도록 해준다. 예를 보자.

```java
public class BookingFlowHandler extends AbstractFlowHandler {
	public String handleExecutionOutcome(FlowExecutionOutcome outcome, HttpServletRequest request,
	                                     HttpServletResponse response) {
		if (outcome.getId().equals("bookingConfirmed")) {
			return "/booking/show?bookingId=" + outcome.getOutput().get("bookingId");
		} else {
			return "/hotels/index";
		}
	}
}
```

재정의된 handleExecutionOutcome 메소드에서는 Flow 결과로 나온 flow id 가 bookingConfirmed인 경우 특정 URL(/booking/show?bookingId=…)로 보낸다.
flow id 가 bookingConfirmed 와 다른 경우 /hotels/index 에 대한되는 URL로 가게 된다.

#### 커스텀 FlowHandler 배포

커스텀 FlowHandler를 설치하려면,그냥 빈으로 등록하기만 하면 된다. 빈 이름은 반드시 적용하고자 하는 Flow의 id와 일치해야 한다

```xml
<bean name="hotels/booking" class="org.springframework.webflow.samples.booking.BookingFlowHandler"/>
```

이 설정을 통해서 /hotels/booking 자원에 대한 접근은 커스텀 핸들러인 BookingFlowHandler를 사용해서 hotels/booking이 실행되게 된다.
booking flow 가 끝나는 시점에서 BookingFlowHandler의 handleExecutionOutcome이 실행되며 String(URL) 결과에 따라 적당한 controller로 재전송된다.

#### FlowHandler 재전송

FlowExecutionOutcome이나 FlowException을 제어하는 FlowHandler는 제어를 한 후에 재전송하는 경로를 지정하는 String을 반환하게 된다. 이전 예에서 BookingFlowHandler는 bookingConfirmed 결과에 대해서는 booking/show로 재전송하고, 다른 결과에 대해서는 hotels/index 자원 URI로 반환하게 된다. 기본적으로 반환되는 자원의 위치는 현재 서블릿 매핑에 관계된다. 이는 flow handler가 상대 경로를 사용해서 애플리케이션 내에 있는 다른 컨트롤러로 redirect할 수 있게 해준다. **여기에 더해서 좀더 제어가 필요한 경우에 사용할 수 있는 명시적인 앞첨자를 제공한다.**

- servletRelative: 현재 서블릿에 대한 상대적인 자원으로 재전송
- contextRelative: 현재 웹 애플리케이션 컨텍스트 경로(web application context path)에 대한 상대적인 자원으로 재전송
- servletRelative: 서블릿 루트에 대한 상대적인 자원으로 재전송
- http: 또는 https: : 완전한 자원 URI로 재전송

이 앞첨자는 externalRedirect: 지시어와 함께 Flow 정의 내에서도 사용할 수 있다.
예를 들면, view=“externalRedirect:http://springframework.org”.

### 뷰 결정

Web Flow 2는 따로 지정하지 않는다면 Flow 파일이 있는 디렉터리에 있는 파일과 선택된 뷰 식별자를 매핑해주게 된다. 기존 스프링 MVC+Web Flow 애플리케이션에서는 이미 외부 ViewResolver가 매핑 처리를 해주고 있다. 그러므로 기존 resolver를 계속 사용하고, 기존 Flow 뷰가 패키징된 방법이 변경되는 것을 피하기 위해서 다음처럼 설정하자.

```xml
<webflow:flow-registry id="flowRegistry"	flow-builder-services="flowBuilderServices">
	<webflow:location path="/WEB-INF/hotels/booking/booking.xml" />
</webflow:flow-registry>
 
<webflow:flow-builder-services id="flowBuilderServices" 	view-factorycreator="mvcViewFactoryCreator" />
 
<bean id="mvcViewFactoryCreator" class="org.springframework.webflow.mvc.builder.MvcViewFactoryCreator">
	<property name="viewResolvers" ref="myExistingViewResolverToUseForFlows" />
</bean>
```

MvcViewFactoryCreator는 당신이 Spring MVC view 시스템(여기선 “myExistingViewResolverToUseForFlows”)을 Spring Web Flow 내에서 사용할 수 있도록 해준다.
Booking Hotels 샘플에서는 아래와 같이 설정되어 있다(tilesViewResolver 를 이용할 수 있도록 되어 있다).

```xml
<bean id="mvcViewFactoryCreator" class="org.springframework.webflow.mvc.builder.MvcViewFactoryCreator"> 
	<property name="viewResolvers" ref="tilesViewResolver"/> 
</bean>
```

또한 useSpringBinding의 값을 true로 설정하면 Spring MVC의 고유한 BeanWrapper를 이용하여 데이터 바인딩을 할 수 있다.

### 뷰에서 이벤트 보내기

flow가 view-state에 들어가서 잠시 멈추게 되면, 사용자를 해당 실행 URL로 재전송해서, 사용자 이벤트가 다시 시작되기를 기다리게 된다. 이번 절에서는 JSP, Velocity나 Freemarker처럼 템플릿 엔진에 의해서 생성된 HTML 기반 뷰에서 이벤트를 발생시키는 방법을 알아보자.

#### HTMl 버튼을 사용해서 이벤트 보내기

다음은 proceed와 cancle 이벤트를 발생시키는 같은 폼 내의 두 개 버튼을 보여준다.

```xml
<input type="submit" name="_eventId_proceed" value="Proceed" />
<input type="submit" name="_eventId_cancel" value="Cancel" />
```

버튼이 선택되면, SWF는 _eventId로 시작하는 요청 파라미터를 찾아서, 그 부분을 잘라내고 남은 문자열을 id로 사용하게 된다.
_eventId_proceed는 proceed가 된다. 그러기 때문에 동일한 폼에서 다양한 여러 이벤트를 발생시킬 수 있다.

#### hidden HTML 폼 파라미터 사용해 이벤트 신호 보내기

form이 submit될 때 proceed 이벤트가 발생하려면 다음처럼 하자.

```xml
<input type="submit" value="Proceed" />
<input type="hidden" name="_eventId" value="proceed" />
```

여기서는 _eventId 파라미터로 오는 값을 찾아서 event id로 해당 값을 사용하게 된다.
이런 방법은 form으로 전송할 수 있는 이벤트가 하나일 때만 생각해봐야 한다.

#### HTML link 사용해서 이벤트 보내기

```html
<a href="${flowExecutionUrl}&_eventId=cancel">Cancel</a>
```

**매개변수 식별 순서는 “eventId” ⇒ “_eventId” ⇒ 없음 이다.**

## 참고 자료

- [Spring Web Flow reference 2.0.x](http://static.springframework.org/spring-webflow/docs/2.0.x/reference/html/index.html)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
