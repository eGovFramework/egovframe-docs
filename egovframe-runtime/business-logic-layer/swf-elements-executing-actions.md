---
title: Action 실행
linkTitle: "Executing Actions"
description: Action-state는 flow 내에서 특정 액션 실행 후 그 결과에 따라 다른 상태로 전이하는 기능을 제공하며, decision-state는 if-else와 같은 흐름 제어를 수행한다. 예를 들어, 특정 조건에 따라 transition이 결정되는 구조를 정의할 수 있다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-elements/swf-elements-executing-actions/
menu:
  depth:
    name: Executing Actions
    weight: 4
    parent: "swf-elements"
---
# Action 실행

## 개요

action-state는 flow 내에서 action 실행을 제어하기 위한 요소이다.  
decision-state를 이용하여 if-else와 같은 흐름 제어를 할 수 있다. 좀 더 자세히 알아보도록 하자.

## 설명

### 액션 상태 정의하기

특정 액션을 호출한 다음에, 그 결과에 따라서 다른 상태로 전이하고 싶은 경우에는 action-state 구성 요소를 사용하자.  
직관적으로 봤을 때 아래 코드는 interview.moreAnswersNeeded()의 결과값에 의해 transition이 실행될 것을 예상할 수 있다.

```xml
<action-state id="moreAnswersNeeded">
	<evaluate expression="interview.moreAnswersNeeded()" />
	<transition on="yes" to="answerQuestions" />
	<transition on="no" to="finish" />
</action-state>
```

좀더 완전한 예를 살펴보자.

```xml
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
                      http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
	<on-start>
		<evaluate expression="interviewFactory.createInterview()"
			result="flowScope.interview" />
	</on-start>
 
	<view-state id="answerQuestions" model="questionSet">
		<on-entry>
			<evaluate expression="interview.getNextQuestionSet()"
				result="viewScope.questionSet" />
		</on-entry>
		<transition on="submitAnswers" to="moreAnswersNeeded">
			<evaluate expression="interview.recordAnswers(questionSet)" />
		</transition>
	</view-state>
 
	<action-state id="moreAnswersNeeded">
		<evaluate expression="interview.moreAnswersNeeded()" />
		<transition on="yes" to="answerQuestions" />
		<transition on="no" to="finish" />
	</action-state>
 
	<end-state id="finish" />
 
</flow>
```

### 의사결정 상태(decision states) 정의

action-state를 대신해서 편리하게 if/else 문법을 사용해서 이동하고자 하는 의사결정을 해주는 decision-state를 사용한다.  
이전 예제를 의사결정 상태로 구현한 예를 보자.

```xml
<decision-state id="moreAnswersNeeded">
	<if test="interview.moreAnswersNeeded()" then="answerQuestions" else="finish" />
</decision-state>  
```

### 액션 출력 이벤트 매핑

액션은 대부분 POJO의 메소드를 호출한다. action-state와 decision-state을 호출했을 때,
이들 메소드가 반환하는 값은 상태를 전이하게 해주는데 사용할 수 있다. 전이가 이벤트에 의해서 발생되기 때문에, 우선 메소드가 반환하는 값은 반드시 Event 객체에 매핑되어야 한다.  
다음 테이블은 공통적으로 반환하는 값 타입에 따라 Event 객체가 어떻게 매핑되는지를 설명해준다.

메소드 반환 타입 매핑된 Event 식별자 표현

| 결과로 리턴되는 타입 | 메핑되는 이벤트 값 |
|----------------|----------|
| java.lang.String | String 값 | 
| java.lang.Boolean | yes(true에 해당), no(false에 해당) | 
| java.lang.Enum Enum | Enum 이름 | 
| 나머지 다른 타입 | success | 

예제.moreAnswersNeeded() 메소드의 리턴 타입은 boolean인 것을 예상할 수 있으면 그에 따라 yes, no에 매핑됨을 알 수 있다.

```xml
<action-state id="moreAnswersNeeded">
	<evaluate expression="interview.moreAnswersNeeded()" />
	<transition on="yes" to="answerQuestions" />
	<transition on="no" to="finish" />
</action-state>
```

### 액션 구현

POJO 로직처럼 action 코드를 작성하는 것이 가장 일반적이다.  
때로는 flow context에 접근할 필요가 있는 액션 코드를 작성할 필요가 있다.  
이럴 때는 POJO를 호출하면서, EL 변수로 flowRequestContext를 건낼 수 있다.  
그 대신 Action 인터페이스를 구현하거나, MultiAction 기본 클래스를 상속할 수도 있다.  

#### POJO 메소드 호출

```xml
<evaluate expression="pojoAction.method(flowRequestContext)" />
```

```java
public class PojoAction {
 public String method(RequestContext context) {
  ...
 }
}
```

#### custom Action 구현 호출

```xml
<evaluate expression="customAction" />
```

```java
public class CustomAction implements Action {
  public Event execute(RequestContext context) {
  ...
  }
}
```

#### MultiAction 구현 호출

```xml
<evaluate expression="multiAction.actionMethod1" />
```

```java
public class CustomMultiAction extends MultiAction {
	public Event actionMethod1(RequestContext context) {
  ...
	}
  ...
	public Event actionMethod2(RequestContext context) {
  ...
	}
 
}
```

### 액션 예외

action은 복잡한 비즈니스 로직을 캡슐화하고 있는 서비스를 호출할 수도 있다.  
이 서비스들은 비즈니스 예외를 던질 수도 있으니 이를 처리해야 할 수도 있다.

#### POJO 액션 사용 시 비즈니스 예외 제어하기

```xml
<evaluate expression="bookingAction.makeBooking(booking, flowRequestContext)" />
```

```java
public class BookingAction {
	public String makeBooking(Booking booking, RequestContext context) {
		try {
			BookingConfirmation confirmation = bookingService.make(booking);
			context.getFlowScope().put("confirmation", confirmation);
			return "success";
		} catch (RoomNotAvailableException e) {
 
			context.addMessage(new MessageBuilder().error().efaultText("No room is available at this hotel").build());
 
			return "error";
		}
	}
}
```

### MultiAction 사용 시 비즈니스 예외 제어하기

아래 예제는 이전 예제와 기능적으로는 동일하지만, POJO 액션 대신 MultiAction으로 구현했다.  
Event ${methodName}(RequestContext) 규약에 따라 메소드를 구성하면 되고, POJO의 자유스러움에 비해, 보다 더 강력한 타입 안정성을 제공한다.

```xml
<evaluate expression="bookingAction.makeBooking" />
```

```java
public class BookingAction extends MultiAction {
	public Event makeBooking(RequestContext context) {
		try {
			Booking booking = (Booking) context.getFlowScope().get("booking");
			BookingConfirmation confirmation = bookingService.make(booking);
			context.getFlowScope().put("confirmation", confirmation);
			return success();
		} catch (RoomNotAvailableException e) {
			context.getMessageContext()
			       .addMessage(new MessageBuilder().error().defaultText("No room is available at this hotel").build());
			return error();
		}
	}
}
```

### 다른 Action 실행 예제

#### on-start

```xml
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
	<input name="hotelId" />
	<on-start>
		<evaluate expression="bookingService.createBooking(hotelId, currentUser.name)"
			result="flowScope.booking" />
	</on-start>
</flow>
```

#### on-entry

```xml
<view-state id="changeSearchCriteria" view="enterSearchCriteria.xhtml"
	popup="true">
	<on-entry>
		<render fragments="hotelSearchForm" />
	</on-entry>
</view-state>
```
#### on-exit

```xml
<view-state id="editOrder">
	<on-entry>
		<evaluate expression="orderService.selectForUpdate(orderId, currentUser)"
			result="viewScope.order" />
	</on-entry>
	<transition on="save" to="finish">
		<evaluate expression="orderService.update(order, currentUser)" />
	</transition>
	<on-exit>
		<evaluate expression="orderService.releaseLock(order, currentUser)" />
	</on-exit>
</view-state>
```
#### on-end

```xml
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
                      http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
	<input name="orderId" />
	<on-start>
		<evaluate expression="orderService.selectForUpdate(orderId, currentUser)"
			result="flowScope.order" />
	</on-start>
	<view-state id="editOrder">
		<transition on="save" to="finish">
			<evaluate expression="orderService.update(order, currentUser)" />
		</transition>
	</view-state>
	<on-end>
		<evaluate expression="orderService.releaseLock(order, currentUser)" />
	</on-end>
</flow>
```
#### on-render

```xml
<view-state id="reviewHotels">
	<on-render>
		<evaluate expression="bookingService.findHotels(searchCriteria)"
			result="viewScope.hotels" result-type="dataModel" />
	</on-render>
	<transition on="select" to="reviewHotel">
		<set name="flowScope.hotel" value="hotels.selectedRow" />
	</transition>
</view-state>
```
#### on-transition

```xml
<subflow-state id="addGuest" subflow="createGuest">
	<transition on="guestCreated" to="reviewBooking">
		<evaluate expression="booking.guestList.add(currentEvent.attributes.newGuest)" />
	</transition>
</subfow-state>
```
#### Named actions

```xml
<action-state id="doTwoThings">
	<evaluate expression="service.thingOne()">
		<attribute name="name" value="thingOne" />
	</evaluate>
	<evaluate expression="service.thingTwo()">
		<attribute name="name" value="thingTwo" />
	</evaluate>
	<transition on="thingTwo.success" to="showResults" />
</action-state>
```

#### Streaming actions

아래 예는 flow에서 printBoardingPassAction를 호출하는 것으로 PDF로 프린트하고자 할 때 구현하는 예를 보여주고 있다.  
AbstractAction을 상속한 PrintBoardingPassAction의 doExecute() 메소드 안에 실제 pdf 관련 소스를 구현하고 success()를 리턴한다.

```xml
<view-state id="reviewItinerary">
	<transition on="print">
		<evaluate expression="printBoardingPassAction" />
	</transition>
</view-state>
```

```java
public class PrintBoardingPassAction extends AbstractAction {
  public Event doExecute(RequestContext context) {
    // stream PDF content here...
    // - Access HttpServletResponse by calling context.getExternalContext().getNativeResponse();
    // - Mark response complete by calling context.getExternalContext().recordResponseComplete();
    return success();
  }
}
```

## 참고자료
- [Spring Web Flow reference 2.0.x](http://static.springframework.org/spring-webflow/docs/2.0.x/reference/html/index.html) (링크 만료)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)