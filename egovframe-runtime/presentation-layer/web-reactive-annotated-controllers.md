---
title: 스프링 WebFlux에서 어노테이션 기반 컨트롤러 활용 방법
linkTitle: "Annotated Controllers"
description: 스프링 WebFlux는 @Controller, @RestController 어노테이션을 통해 요청을 매핑하고 입력 처리 및 예외 처리를 지원한다. 컨트롤러는 메소드 기반으로 동작하며, 상속이나 인터페이스 구현 없이도 다양한 방식으로 활용할 수 있다.
url : /egovframe-runtime/presentation-layer/web-reactive/web-reactive-annotated-controllers/
menu:
    depth:
        name: Annotated Controllers
        weight: 3
        parent: "web_reactive"
---
# Annotated Controllers

## 설명
스프링 WebFlux는 어노테이션 기반 프로그램밍 모델을 지원하기 때문에 @Controller, @RestController 컴포넌트로 요청을 매핑하고, 입력을 받고, 예외처리를 할수 있다. 컨트롤러는 메소드를 여러가지로 활용할 수 있어서 클래스를 상속하거나 인터페이스를 구현하지 않아도 된다.
```java
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String handle() {
        return "Hello WebFlux";
    }
}
```
위 코드에서는 response body에 쓸 String을 리턴한다.

### @Controller
컨트롤러는 표준 스프링 빈으로 정의한다. @Controller 어노테이션을 달면 스프링이 클래스패스 내의 다른 @Component 클래스처럼 자동으로 스캔하고 빈으로 등록한다. 이 어노테이션을 선언하면 그 클래스가 Web 컴포넌트라는 뜻이기도 하다.
@Controller 빈을 자동으로 등록하려면 아래와 같이 컴포넌트 스캔을 위한 설정이 필요하다.
```java
@Configuration
@ComponentScan("org.example.web")
public class WebConfig {
// ...
}
```
@RestController는 자체에 @Controller, @ResponseBody를 선언하고 있어, 컨트롤러 내의 모든 메소드에 @ResponseBody를 상속한다. 따라서 리턴값으로 View를 만들지 않고 response body에 바로 쓸 수 있다.

### Request Mapping
컨트롤러 메소드 요청을 매핑할 때는 @RequestMapping을 사용한다. 이 어노테이션에 있는 속성으로 URL, HTTP 메소드, 요청 파라미터, 헤더, 미디어 타입을 매칭할 수 있다. 메소드에 선언하거나 모든 메소드에서 공유하고 싶을 때 클래스 레벨에 선언한다.
@GetMapping, @PostMapping, @PutMapping, @DeleteMapping, @PatchMapping은 HTTP 메소드를 바로 지정할 수 있다. 이 어노테이션은 컨트롤러 메소드에서 거의 대부분이 HTTP 메소드 하나만 담당하는 일종의 커스텀 어노테이션이다. 이 어노테이션을 선언하더라도 다른 매핑 조건을 공통으로 사용하려면 클래스 레벨의 @RequestMapping을 선언해야 한다.

### Handler Methods
@RequestMapping 핸들러는 다양한 컨트롤러 메소드 인자와 리턴값을 지원하므로 원하는 것을 선택하면 된다.
블로킹 I/O로 받는 인자(예를 들어 response body를 읽는 경우)는 리액티브 유형(Reactor, RxJava 또는 기타)을 사용할 수 있다. 이런 타입은 Description 컬럼에 명시되어 있다. 블로킹 없는 인자는 리액티브 타입을 사용하지 않는다.
일부 어노테이션은(예를 들어 @RequestParam, @RequestHeader 등) required attribute로 필수 여부를 지정할 수 있으며 JDK 8의 java.util.Optional을 사용해도 된다. 효과는 required=false와 동일하다.

### Model
@ModelAttribute 어노테이션은 다음과 같이 사용할 수 있다.

- @RequestMapping 메소드 인자에 선언해서 모델을 생성, 접근하고 WebDataBinder로 객체에 바인딩한다.
- @Controller나 @ControllerAdvice 클래스 메소드에 선언해서 다른 @RequestMapping 메소드를 실행하기 전 모델을 초기화한다.
- @RequestMapping 메소드에서 리턴하는 값을 molde attribute로 만든다.

여기서는 @ModelAttribute 메소드에 대해 설명한다. 컨트롤러는 @ModelAttribute 메소드를 얼마든지 가질 수 있다. 이러한 모든 메소드는 동일한 컨트롤러에서 @RequestMapping 메소드 앞에 호출된다. @ModelAttribute 메소드는 @ControllerAdvice를 통해 컨트롤러 간에 공유할 수도 있다.

@ModelAttribute 메소드는 여러가지 방법으로 활용할 수 있다. 지원하는 인자는 대부분 @RequestMapping 메소드와 동일하다.(@ModelAttribute 자체와 request body와 관련된 것은 제외)
다음은 @ModelAttribute 메소드 사용 예제이다.
```java
@ModelAttribute
public void populateModel(@RequestParam String number, Model model) {
model.addAttribute(accountRepository.findAccount(number));
// add more ...
}
```

### DataBinder
WebDataBinder는 @Controller나 @ControllerAdvice 클래스에서 @InitBinder 메소드로 초기화할 수 있다.
@InitBinder 메소드는 다음과 같이 사용할 수 있다.

@InitBinder 메소드롤 컨트롤러별 java.beans.PropertyEditor나 스프링 Converter, Formatter를 등록할 수 있다.
FormattingConversionService에서 전역으로 사용하는 Converter, Formatter는 웹플럭스 설정으로 등록한다.
@InitBinder 메소드가 지원하는 인자는 @ModelAttribute(커맨드 객체)만 제외하고 대부분 @RequestMapping 메소드와 동일하다.
보통은 WebDataBinder를 인자로 받아 컴포넌트를 등록하고 void를 리턴한다. 다음은 @InitBinder 어노테이션을 사용하는 예제이다.

```java
@Controller
public class FormController {

    @InitBinder
    public void initBinder(WebDataBinder binder) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        dateFormat.setLenient(false);
        binder.registerCustomEditor(Date.class, new CustomDateEditor(dateFormat, false));
    }
 
    // ...
}
```

### Managing Exceptions
@Controller와 @ControllerAdvice 클래스 메소드에 @ExceptionHandler를 선언하면 컨트롤러 메서드의 예외를 처리할 수 있다. 다음은 예외를 처리하는 예제이다.

```java
@Controller
public class SimpleController {

    // ...
 
    @ExceptionHandler
    public ResponseEntity<String> handle(IOException ex) {
        // ...
    }
}
```

### Controller Advice
@ExceptionHandler, @InitBinder, @ModelAttribute 메소드는 @Controller 클래스(혹은 상속한 클래스)에 적용된다.
모든 컨트롤러에 적용하고 싶다면 @ControllerAdvice나 @RestControllerAdvice를 선언한 클래스 안에 만들어야 한다.

@ControllerAdvice는 @Component 어노테이션이 선언되어 있기 때문에 컴포넌트 스캔으로 스프링 빈에 등록할 수 있다.
@RestControllerAdvice는 @ControllerAdvice와 @ResponseBody가 둘 다 선언되어 있어 @ExceptionHandler 메소드에서 리턴한 값은 메시지 변환을 통해 view를 만들거나 템플릿을 랜더링하는 대신 response body로 렌더링한다.

애플리케이션을 기동하면 프레임워크 내부에서 @ControllerAdvice를 선언한 스프링 빈을 찾아 @RequestMapping과 @ExceptionHandler 메소드를 적용한다.
전역에 설정한 @ExceptionHandler 메소드는 @Controller 메소드 다음에 적용한다. 반대로 전역 @ModelAttribute, @InitBinder 메소드는 @Controller 메소드 전에 적용한다.

기본적으로 @ControllerAdvice 메소드는 모든 요청에 적용되지만 다음 예제처럼 어노테이션 attribute로 컨트롤러를 지정할 수 있다.

```java
// Target all Controllers annotated with @RestController
@ControllerAdvice(annotations = RestController.class)
public class ExampleAdvice1 {}

// Target all Controllers within specific packages
@ControllerAdvice("org.example.controllers")
public class ExampleAdvice2 {}

// Target all Controllers assignable to specific classes
@ControllerAdvice(assignableTypes = {ControllerInterface.class, AbstractController.class})
public class ExampleAdvice3 {}
```

## 참고자료
- [The Spring Framework - Web Reactive - Annotated Controllers](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/web-reactive.html#webflux-controller)