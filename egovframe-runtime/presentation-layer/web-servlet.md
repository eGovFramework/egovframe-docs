# Web Servlet

## 개요

![Web Servlet](./images/web-servlet.jpg)

MVC(Model-View-Controller) 패턴은 코드를 기능(역활)에 따라 Model, View, Controller 3가지 요소로 분리한다.
- Model : 어플리케이션의 데이터와 비지니스 로직을 담는 객체이다.
- View : Model의 정보를 사용자에게 표시한다. 하나의 Model을 다양한 View에서 사용할 수 있다.
- Controller : Model과 View의 중계역활을 한다. 사용자의 요청을 받아 Model에 변경된 상태를 반영하고, 응답을 위한 View를 선택한다.
MVC 패턴은 UI 코드와 비지니스 코드를 분리함으로써 종속성을 줄이고, 재사용성을 높이고, 보다 쉬운 변경이 가능하도록 한다.
MVC 패턴이 Web Framework에만 사용되는 단어는 아니지만, 전자정부프레임워크에서 “MVC 서비스”란 MVC 패턴을 활용한 Web MVC Framework를 의미한다.

## 설명

오픈소스 Web MVC Framework에는 Spring MVC, Struts, Webwork, JSF등이 있으며, 각각의 장점을 가지고 사용되고 있다.
기능상에서 큰차이는 없으나, 아래와 같은 장점을 고려 전자정부프레임워크에서는 Spring Web MVC를 MVC 서비스의 기반 오픈 소스로 채택하였다.

- Framework내의 특정 클래스를 상속하거나, 참조, 구현해야 하는 등의 제약사항이 비교적 적다. Controller(Spring 2.5 @MVC)나 Form 클래스등이 좀 더 POJO-style에 가까워 비지니스 로직에 집중된 코드를 작성할 수 있다.
- IOC Contatiner가 Spring 이라면 (간단한 설정으로 Struts나 Webwork같은 Web Framework을 사용할 수 있겠지만) 연계를 위한 추가 설정없이 Spring MVC를 사용할 수 있다. 전자정부프레임워크의 IOC Container는 Spring이다.
- 오픈소스 프로젝트가 활성화(꾸준한 기능 추가, 빠른 bug fix와 Q&A) 되어 있으며 로드맵이 신뢰할만 하다.
- 국내 커뮤니티 활성화 정도, 관련 참고문서나 도서를 쉽게 구할 수 있다.

### Spring MVC

Spring MVC 에 대한 설명은 아래 상세 페이지를 참고

- [Spring MVC Architecture](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:spring_mvc_architecture)
- [DispatcherServlet](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:dispatcherservlet)
- [HandlerMapping](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:handlermapping)
- [Controller](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:controller)
- [Annotation-based Controller](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:annotation-based_controller)
- [Validation](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.10:ptl:validation)
- [Declarative Validation](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.10:ptl:jsr303)
- [View](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:ptl:view)

### 예제 실행

- [easycompany 설치 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.10:ptl:easycompany) : MVC와 Ajax Support, Security의 예제코드인 easycompany 설치와 실행 방법을 가이드한다.

## 참고자료

- [SUN Java BluePrints, Model-View-Controller](http://java.sun.com/blueprints/patterns/MVC-detailed.html)