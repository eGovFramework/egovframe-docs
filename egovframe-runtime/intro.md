# eGovframe-docs

## 표준프레임워크 실행환경
* [표준프레임워크 실행환경 소개](./intro/overview.md)

### 공통기반 핵심
* [IoC Container]()
  * [Basics]()  
    IoC Container를 설명하기 위해 필요한 기본적인 개념 및 사용 방법을 설명한다.
  * [Dependencies]()  
    IoC Container의 핵심 기능인 Dependency Injection의 사용 방식 및 설정 방법을 설명한다.
  * [Bean scope]()  
    IoC Container에 의해 관리되는 Bean의 생성 방식 및 적용 범위를 설명한다.
  * [Customizing the nature of a bean]()  
    Bean의 생명주기 관리, Bean이 속한 Container 참조 등 Bean의 성질을 변화시키는 방법을 설명한다.
  * [Bean definition inheritance]()  
    Bean 정의 상속에 대해서 설명한다.
  * [Container extension points]()  
    IoC Container의 기능을 확장하는 방법을 설명한다.
  * [The ApplicationContext]()  
    ApplicationContext만이 제공하는 기능을 설명한다.
  * [Annotation-based configuration]()  
    Annotation을 기반으로 Container를 구성하는 방법을 설명한다.
  * [Classpath scanning for managed components]()  
    Dependency Injection에 의해 삽입되는 base Bean에 대한 Java Annotation 기반 설정 방법을 설명한다.
  * [JSR 330 Standard Annotations]()  
    JSR-330 표준 Annotation에 대해서 설명한다.
  * [Java-based configuration]()  
    Java Annotation을 기반으로 Container를 구성하는 방법을 설명한다.
  * [Environment Abstraction]()  
    환경 설정을 추상화하는 방법을 설명한다.
  * [주요 개념 - Inversion of Control]()  
    Spring 4.0부터 추가된 Generic에 대하여 설명한다.
  * [Generic]()
* [AOP]()
  * [@AspectJ 어노테이션을 이용한 AOP 구현]()
  * [XML Schema를 이용한 AOP 구현]()
  * [실행환경 AOP 가이드라인]()
* [Resource]()
* [Spring Expression Language(SpEL)]()

### 공통기반
* [Server Security]()
  * [Architecture]()
  * [Authentication]()
  * [Authorization]()
  * [설정 간소화]()
* [Session 방식 접근제어]()
* [Scheduling]()
* [Logging]()
  * [SLF4J]()
  * [Log4J 2]()
    * [프로그래밍내에서 직접 설정하는 방법]()
    * [설정 파일을 사용하는 방법]()
* [ID Generation]()
* [Property]()
  * [Property Service]()
  * [Property Source]()
* [Environment]()
* [Cache]()
  * [EhCache]()
  * [Cache Abstraction]()
* [Marshalling/Unmarshalling]()
* [XML Manipulation]()
* [Object Pooling]()
* Crypto
  * [Encryption/Decryption]()
  * [crypto 간소화]()
* [FTP]()
* [Mail]()
* [Compress/Decompress]()
* [File Upload/Download]()
  * [file_upload]()
  * [file_download]()
* [File Handling]()
* [Excel]()
* [String Util]()

### 화면처리
* [Web Servlet]()
  * [Spring MVC Architecture]()  
    스프링 MVC의 기본 구조 및 핵심 컴포넌트에 대해 설명한다.
  * [DispatcherServlet]()  
    스프링 MVC의 핵심 컴포넌트인 DispatcherServlet의 기능과 등록방법에 대해 설명한다.
  * [HandlerMapping]()  
    요청과 Controller간의 연결고리 역활을 하는 컴포넌트인 HandlerMapping에 대해서 설명한다.
  * [Spring Mvc tag configuration]()  
    Spring에서 제공하는 mvc태그를 통해 간단하게 설정하는 방법에 대하여 설명한다.
  * [Controller]()  
    인터페이스 Controller를 구현한 AbstractController, SimpleFormContrller 같은 계층형(hierarchy) Controller에 대해서 설명한다.
  * [Annotation-based Controller]()  
    @MVC구현을 위한 관련 어노테이션과 활용 방법에 대해서 설명한다.
  * [Validation]()  
    객체의 유효성 검증 기능에 대해서 설명한다.
  * [Declarative Validation]()  
    스프링의 선언적 Validation 기능에 대해서 설명한다.
  * [View]()  
    스프링 MVC의 View와 스프링 폼 태그에 대해서 설명한다.
  * [AnnotationCommandMapArgumentResolver]()  
    Request Parameter값을 @RequestParam을 통해 손쉽게 가져오는 방법을 설명한다.
* [Web Reactive]()
  * [Reactive Core]()
  * [DispatcherHandler]()
  * [Annotated Controllers]()
  * [Functional Endpoints]()
  * [WebClient]()
* [Ajax 지원]()
* [Internationalization]()
* [Security]()
* [UI Adaptor]()
* [Asynchronous request processing]()  
  비동기요청처리에 대하여 설명한다.
* [jQuery ajax]()
* [WebSocket]()
  * [STOMP]()
  * [SockJS]()
* [bootstrap]()

### UX처리
* [UX/UI Controller Component]()
* [HTML5+CSS3.0+JavaScript Module App Framework 기본 활용]()
* [UI - bootstrap]()

### 업무처리
* [Exception Handling]()
* [Spring Web Flow]()
  * SWF Getting Started
    * [Hello world]()  
    Hello 예제 2가지를 샘플로 설명한다.
  * SWF Configuration
    * [SWF 시스템 설정]()  
    Spring Web Flow 를 사용하기 위한 Web 개발환경에 대한 세팅을 설명한다.
    * [Spring Web Flow 와 MVC 연동]()  
    Spring Web Flow 를 사용하기 위한 Spring MVC 설정을 설명한다.
    * [Securing Flows]()  
    Web Flow 에 적용되는 Spring Security 에 대해 설명한다.
    * [Flow Managed Persistence]()  
    Web Flow에서 하이버네이트와 JPA 객체 영속화 기술과 연동에 관해 설명한다.
  * SWF
    * [Flow Definition]()  
    Flow 의 필수적인 언어 구성요소와 sub flow 에 대해 설명한다.
    * [Expression Language]()  
    Web Flow 설계시 데이타 모델 및 action 실행을 위한 EL을 설명한다.
    * [Rendering Views]()  
    flow 내에서 화면을 생성하는 요소에 대해 설명한다.
    * [Executing actions]()  
    flow 내에서 실행 요소에 대해 설명한다.
    * [Flow Inheritance]()  
    flow 간의 상속에 대해 설명한다.

### 데이터처리
* [Data Source]()
* [iBatis]()
  * [iBATIS Configuration]()
  * [Spring iBatis Integration]()
  * [Data Type]()
  * [parameterMap]()
  * [Inline Parameters]()
  * [resultMap]()
  * [Dynamic SQL]()
* [MyBatis]()
  * [주요 변경 사항]()
  * [Getting Started]()
  * [Configuration XML]()
  * [Mapper XML Files]()
  * [Dynamic SQL]()
  * [표준프레임워크 기반 적용 가이드]()
* [Spring Data - JPA]()
  * [Repository]()
  * [Query Method]()
* Spring Data - MongoDB
  * [MongoDB support]()
  * [MongoDB Repositories]()
  * [MongoDB support 3.5.1]()
  * [MongoDB Repositories 3.5.1]()
* [ORM]()
  * [Entities]()
  * [Entity Operation]()
  * [Association Mapping]()
  * [Query Language]()
  * [Native SQL]()
  * [Concurrency]()
  * [Cache Handling]()
  * [Fetch Strategy]()
  * [Spring Integration]()
  * [JPA Configuration]()
* [Transaction]()
* [Spring Data - Reactive]()
  * [R2DBC]()
  * [MongoDB]()
  * [Cassandra]()
  * [Redis]()

### 연계통합
* [Naming Service]()
* [Integration Service]()
  * [Metadata]()
  * [연계 서비스 API]()
* [WebService]()
* [Restful]()   
스프링의 Restful Web Service의 사용법에 대해서 설명한다.
* [Cloud Data Stream]()
* [Swagger]()

### 배치처리
* [배치실행환경소개]()
* Batch Core
  * [Job Configuration]()  
    배치처리 기능 중 Job 설정에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Job Execution]()  
    배치처리 기능 중 Job 실행에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Step Configuration]()  
    배치처리 기능 중 Step 설정에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Step Execution]()  
    배치처리 기능 중 Step 실행에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [ItemReader]() / [ItemWriter]() / [Resource Variable]()  
    리소스 설정 및 Read/Write하는 방법에 대해 설명한다.
  * [Tasklet]()  
    아이템 기반이 아닌 배치처리에 대한 기본개념 및 사용법에 대해 설명한다.
* Batch Execution  
  * [JobRepository]()   
  배치수행정보를 저장하는 JobRepository의 기본 개념 및 사용법에 대해 설명한다.
  * [JobLauncher]()   
  배치작업을 실행하는 JobLauncher의 기본 개념 및 사용법에 대해 설명한다.
    * [Remote JobLauncher]()  
    Online에서 배치계의 Batch Job을 기동시키기 위하여 Batch Remote Client의 기본 개념 및 사용법에 대해 설명한다. 
  * [JobRunner]()   
  다양한 유형의 배치실행을 지원하는 JobRunner설정에 관한 기본 개념 및 사용법에 대해 설명한다.
* Batch Support  
  * [Skip/Retry/Repeat]()   
  배치수행 중 오류처리와 관련한 Skip/Retry/Repeat의 기본 개념 및 사용법에 대해 설명한다.
  * [MultiData Processing]()   
  다수 건의 리소스를 처리하는 MultiData Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [History Management]()   
  배치수행 이력정보를 관리하는 History Management의 기본 개념 및 사용법에 대해 설명한다.
  * [Sync / Async Processing]()   
  동기,비동기 실행을 지원하는 Sync / Async Processing의 기본 개념 및 사용법에 대해 설명한다. 
  * [Pre / Post Processing]()   
  전처리,후처리 실행을 지원하는 Pre / Post Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [Parallel Processing]()   
  배치수행 시 성능향상을 위한 Parallel Processing의 기본 개념 및 사용법에 대해 설명한다.  
  * [Code Base Exception]()   
  배치수행 시 코드기반 에러 처리에 대한 기본 사용법에 대해 설명한다.
* [Center Cut]()   
큐를 사용한 센터 컷의 관한 기본 개념 및 사용법에 대해 설명한다.


### 배치운영환경
* [배치운영환경]()   
일괄(배치) 개발/실행환경에서 작성된 배치Job을 등록/실행하고 수행현황을 모니터링하며 처리결과를 확인하기 위한 표준화된 운영환경을 제공합니다. 
