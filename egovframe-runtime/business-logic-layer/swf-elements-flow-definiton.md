---
title: Flow 정의
linkTitle: "Flow 정의"
description: Flow는 여러 단계의 흐름을 캡슐화한 재사용 가능한 구조로, 상태(state)로 구성되며 각 상태는 이벤트에 따라 다른 뷰로 전환된다. 웹 애플리케이션 개발자는 XML 기반의 Flow 정의 언어로 Flow를 작성하며, 첫 번째 상태가 Flow의 시작점이 된다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-elements/swf-elements-flow-definition/
menu:
  depth:
    name: Flow 정의
    weight: 1
    parent: swf-elements
---
# Flow 정의

## 개요 

### Flow

Flow란 상이한 상황(context)에서 실행될 수 있는 재사용이 가능한 여러 단계들의 흐름을 캡슐화한 것을 의미한다.
모든 Flow는 아래와 같은 Root로 시작한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
    http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
 
</flow>
```

### Flow의 구성

SWF에서 Flow는 “Sate(state)“로 부르는 일련의 단계들로 구성된다. Flow로 진입하게 되는 Sate는 일반적으로 사용자에게 보여지는 뷰가 된다.
이 뷰에서는 Sate를 제어하게 되는 이벤트가 발생한다. 이들 이벤트는 결과적으로 다른 뷰로 이동하게 되는 Transition(transition)을 일으키게 된다.
모든 state는 \<flow/> 안에 정의하게 된다. 맨 처음 정의되는 state가 Flow의 시작점이 된다.

#### Flow의 작성법

Flow는 웹 애플리케이션 개발자가 XML 기반 Flow 정의 언어를 사용해서 작성된다.

## 설명

### Flow의 필수적인 언어 구성요소

```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
                     http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
 
	<view-state id="enterBookingDetails" />
 
	<view-state id="enterBookingDetails">
		<transition on="submit" to="reviewBooking" />
	</view-state>
 
	<end-state id="bookingCancelled" />
 
</flow>
```

- view-state: Flow 중 화면을 보여주는 Sate를 정의하는 구성 요소
- 편의상 Flow 정의 파일이 있는 디렉터리 내에서 view-state id와 일치하는 화면 템플릿을 맞춰 보게 됨
- transition: Sate 내에서 발생한 이벤트를 제어하는 구성 요소. 화면 이동을 일으킴.
- end-state: Flow의 결과를 정의

### Actions

대부분의 Flow는 화면 이동 로직 뿐만 아니라, 애플리케이션의 비즈니스 서비스나 다른 행동을 호출할 필요가 있을 수 있다.
Flow 내에서 Action을 취할 수 있는 여러 지점이 존재한다.

- Flow가 시작할 때
- Sate에 들어갈 때
- 화면을 보여줄 때
- Transition이 일어날 때
- Sate가 종료될 때
- Flow가 종료될 때
  
SWF에서 Action은 기본적으로 Unified EL이라는 간결한 표현 언어를 사용해서 정의하게 된다.

##### evaluate

대부분 evaluate 구성 요소를 사용하게 된다. 이를 통해 Spring Bean에 있는 메소드나 다른 Flow 변수를 호출할 수 있다.
예를 들면 아래와 같다.

```xml
<!-- [1] entityManager Bean 의 persist 메소드에 booking 객체를 넣어 호출한다.  -->
<evaluate expression="entityManager.persist(booking)" />
 
<!-- [2] findHotels 메소드 호출하고 실행결과 Hotels 객체를 flowScope 데이타 모델에  저장한다. -->
<evaluate expression="bookingService.findHotels(searchCriteria)" result="flowScope.hotels" />
 
<!-- [3] findHotels 메소드 호출하고 실행결과 Hotels 객체를 flowScope 데이타 모델에  저장시 dataModel 타입으로 변환하여 저장한다.  -->
<evaluate expression="bookingService.findHotels(searchCriteria)" result="flowScope.hotels" result-type="dataModel"/>
```

아래 예에서는 Flow가 시작할 때 Flow 범위에 Booking 객체를 생성해 저장한다. hotelId는 Flow의 입력 속성으로 받게 된다.

```xml
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
    http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
 
	<input name="hotelId" />
 
	<on-start>
		<evaluate expression="bookingService.createBooking(hotelId, currentUser.name)"	result="flowScope.booking" />
	</on-start>
 
	<view-state id="enterBookingDetails">
		<transition on="submit" to="reviewBooking" />
	</view-state>
 
	<view-state id="reviewBooking">
		<transition on="confirm" to="bookingConfirmed" />
		<transition on="revise" to="enterBookingDetails" />
		<transition on="cancel" to="bookingCancelled" />
	</view-state>
 
	<end-state id="bookingConfirmed" />
	<end-state id="bookingCancelled" />
</flow>
```

#### 입력/출력 매핑

각각의 Flow는 잘 정의된 입력/출력 계약(input/output contract)를 갖고 있다.
Flow는 시작할 때 입력 속성을 건네받게 되고, 종료될 때 출력 속성을 반환하게 된다. 이처럼 Flow 호출은 개념적으로 다음과 같은 메소드 호출과 비슷하다.

```java
FlowOutcome flowId(Map<String, Object> inputAttributes);
```

반환되는 FlowOutcome은 다음과 같은 메소드 선언부를 갖게 된다.

```java
public interface FlowOutcome {
	public String getName();
	public Map<String, Object> getOutputAttributes();
}
```

##### 입력

```xml
<!-- [1] 해당 변수의 값은 flow scope 내에 hotelId 이란 이름으로 저장된다.  -->
<input name="hotelId" />
 
<!-- [2] type 속성으로 속성 지정 가능. 타입이 일치하지 않다면 타입 변환 시도 -->
<input name="hotelId" type="long" />
 
<!-- [3] value 속성으로 입력 값을 할당 -->
<input name="hotelId" value="flowScope.myParameterObject.hotelId" />
 
<!-- [4] required 속성으로 null이나 비어있지 못하도록 강제 -->
<input name="hotelId" type="long" value="flowScope.hotelId" required="true" />
```

##### 출력

Flow 출력 속성은 output 구성 요소를 사용한다. output 속성은 end-state 내에 선언한다. 출력 값은 속성의 이름으로 Flow 범위 내에서 얻어오게 된다.

```xml
<end-state id="bookingConfirmed">
  <output name="bookingId" />
</end-state>
 
<!-- 직접 대상 값 지정 -->
<end-state id="bookingConfirmed">
  <output name="confirmationNumber" value="booking.confirmationNumber" />
</end-state>
```

##### 입력/출력 매핑:샘플

```xml
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow
                      http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
	<input name="hotelId" />
 
	<on-start>
		<evaluate expression="bookingService.createBooking(hotelId, currentUser.name)" 	result="flowScope.booking" />
	</on-start>
 
	<view-state id="enterBookingDetails">
		<transition on="submit" to="reviewBooking" />
	</view-state>
 
	<view-state id="reviewBooking">
		<transition on="confirm" to="bookingConfirmed" />
		<transition on="revise" to="enterBookingDetails" />
		<transition on="cancel" to="bookingCancelled" />
	</view-state>
 
	<end-state id="bookingConfirmed">
		<output name="bookingId" value="booking.id" />
	</end-state>
	<end-state id="bookingCancelled" />
</flow>
```

위 Flow는 이제 hotelId를 입력 값으로 받아서, 새로운 예약이 끝나게 되면 bookingId 출력 속성을 결과로 반환하게 된다.

#### 변수들

Flow에는 하나 이상의 인스턴스 변수 선언이 가능하다. 이 변수들은 flow가 시작할 때 할당되며,
변수를 유지하게 되는 모든 @Autowired transient 참조는 Flow가 재시작될 때 다시 값이 할당(rewired) 되게 된다.
var 구성 요소를 사용해서 Flow 변수를 선언하자.

```xml
<var name="searchCriteria" class="com.mycompany.myapp.hotels.search.SearchCriteria"/>
```

변수로 사용하는 클래스가 Flow 요청 간 인스턴스의 Sate를 유지하기 위해서 java.io.Serializable을 interface로 가지고 있어야 함을 기억하자.

#### Sub Flow 호출

Flow 내에서 하위 Flow로써 또 다른 Flow 호출이 가능하다. 이때 하위 Flow가 결과를 반환할 때까지 기존 Flow는 대기하게 된다.

##### subflow-state

subflow-state 구성요소를 사용해서 하위 Flow 호출을 하게 된다.

```xml
<subflow-state id="addGuest" subflow="createGuest">
	<transition on="guestCreated" to="reviewBooking">
		<evaluate expression="booking.guests.add(currentEvent.attributes.guest)" />
	</transition>
	<transition on="creationCancelled" to="reviewBooking" />
</subfow-state>
```

이 예제에서는 createGuest Flow를 호출한다. guestCreated 출력이 반환되면, 새로운 손님이 예약 손님 리스트에 추가된다.

##### subflow input 전달

input 구성요소를 사용하면 하위 Flow에 입력값을 건낼 수 있다.

```xml
<subflow-state id="addGuest" subflow="createGuest">
	<input name="booking" />
	<transition to="reviewBooking" />
</subfow-state>
```

##### subflow output 매핑

출력 값의 이름으로 하위 Flow에서 출력하는 속성을 참조해서 Transition을 하게 된다.

```xml
<subflow-state  ..>
  <transition on="guestCreated" to="reviewBooking">
    <evaluate expression="booking.guests.add(currentEvent.attributes.guest)" />
  </transition>
  ..
```

이 예에서는 guestCreated을 반환하게 될 때 gest 이름으로 넘어온 값을 booking 내의 guests (currentEvent.attributes.guest)의 일부로 추가해주고 있다.

#### 샘플:Sub Flow 호출하기

아래는 샘플 코드이다.

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
 
	<view-state id="enterBookingDetails">
		<transition on="submit" to="reviewBooking" />
	</view-state>
 
	<view-state id="reviewBooking">
 
		<transition on="addGuest" to="addGuest" />
		<transition on="confirm" to="bookingConfirmed" />
		<transition on="revise" to="enterBookingDetails" />
		<transition on="cancel" to="bookingCancelled" />
	</view-state>
 
	<subflow-state id="addGuest" subflow="createGuest">
		<transition on="guestCreated" to="reviewBooking">
			<evaluate expression="booking.guests.add(currentEvent.attributes.guest)" />
		</transition>
		<transition on="creationCancelled" to="reviewBooking" />
	</subfow-state>
 
	<end-state id="bookingConfirmed">
		<output name="bookingId" value="booking.id" />
	</end-state>
	<end-state id="bookingCancelled" />
</flow>
```

## 참고자료

- [Spring Web Flow reference 2.0.x](http://static.springframework.org/spring-webflow/docs/2.0.x/reference/html/index.html) (링크 만료됨)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
