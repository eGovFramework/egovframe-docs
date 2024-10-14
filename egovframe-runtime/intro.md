# 표준프레임워크 실행환경 가이드

## 표준프레임워크 실행환경
* [표준프레임워크 실행환경 소개](./intro/overview.md)

### 공통기반 핵심
* [IoC Container](./foundation-layer-core/ioc-container.md)
  * [Basics](./foundation-layer-core/ioc-container-basics.md)  
    IoC Container를 설명하기 위해 필요한 기본적인 개념 및 사용 방법을 설명한다.
  * [Dependencies](./foundation-layer-core/ioc-container-dependencies.md)  
    IoC Container의 핵심 기능인 Dependency Injection의 사용 방식 및 설정 방법을 설명한다.
  * [Bean scope](./foundation-layer-core/ioc-container-bean_scope.md)  
    IoC Container에 의해 관리되는 Bean의 생성 방식 및 적용 범위를 설명한다.
  * [Customizing the nature of a bean](./foundation-layer-core/ioc-container-customizing_the_nature_of_a_bean.md)  
    Bean의 생명주기 관리, Bean이 속한 Container 참조 등 Bean의 성질을 변화시키는 방법을 설명한다.
  * [Bean definition inheritance](./foundation-layer-core/ioc-container-bean_definition_inheritance.md)  
    Bean 정의 상속에 대해서 설명한다.
  * [Container extension points](./foundation-layer-core/ioc-container-container_extension_points.md)  
    IoC Container의 기능을 확장하는 방법을 설명한다.
  * [The ApplicationContext](./foundation-layer-core/ioc-container-the_applicationcontext.md)  
    ApplicationContext만이 제공하는 기능을 설명한다.
  * [Annotation-based configuration](./foundation-layer-core/ioc-container-annotation-based_configuration.md)  
    Annotation을 기반으로 Container를 구성하는 방법을 설명한다.
  * [Classpath scanning for managed components](./foundation-layer-core/ioc-container-classpath_scanning_for_managed_components.md)  
    Dependency Injection에 의해 삽입되는 base Bean에 대한 Java Annotation 기반 설정 방법을 설명한다.
  * [JSR 330 Standard Annotations](./foundation-layer-core/ioc-container-jsr_330_standard_annotations.md)  
    JSR-330 표준 Annotation에 대해서 설명한다.
  * [Java-based configuration](./foundation-layer-core/ioc-container-java-based_configuration.md)  
    Java Annotation을 기반으로 Container를 구성하는 방법을 설명한다.
  * [Environment Abstraction](./foundation-layer-core/ioc-container-environment_abstraction.md)  
    환경 설정을 추상화하는 방법을 설명한다.
  * [주요 개념 - Inversion of Control](./foundation-layer-core/ioc-container-inversion_of_control.md)  
    Spring 4.0부터 추가된 Generic에 대하여 설명한다.
  * [Generic](./foundation-layer-core/ioc-container-generic.md)
* [AOP](./foundation-layer-core/aop.md)
  * [@AspectJ 어노테이션을 이용한 AOP 구현](./foundation-layer-core/aop-aspectj.md)
  * [XML Schema를 이용한 AOP 구현](./foundation-layer-core/aop-xmlschema.md)
  * [실행환경 AOP 가이드라인](./foundation-layer-core/aop-egovrteaopguide.md)
* [Resource](./foundation-layer-core/resource.md)
* [Spring Expression Language(SpEL)](./foundation-layer-core/spel.md)

### 공통기반
* [Server Security](./foundation-layer/server-security.md)
  * [Architecture](./foundation-layer/server-security-architecture.md)
  * [Authentication](./foundation-layer/server-security-authentication.md)
  * [Authorization](./foundation-layer/server-security-authorization.md)
  * [설정 간소화](./foundation-layer/server-security-simplifying-settings.md)
* [Session 방식 접근제어](./foundation-layer/session-based-access-control-permission-settings.md)
* [Scheduling](./foundation-layer/scheduling-service.md)
* [Logging](./foundation-layer/logging-service.md)
  * [SLF4J](./foundation-layer/logging-slf4j.md)
  * [Log4J 2](./foundation-layer/logging-log4j2.md)
    * [프로그래밍내에서 직접 설정하는 방법](./foundation-layer/logging-log4j2_configuration_code.md)
    * [설정 파일을 사용하는 방법](./foundation-layer/logging-log4j2_configuration_file.md)
* [ID Generation](./foundation-layer/id-generation.md)
* [Property](./foundation-layer/property.md)
  * [Property Service](./foundation-layer/property-service.md)
  * [Property Source](./foundation-layer/property-source.md)
* [Environment](./foundation-layer/environment.md)
* [Cache](./foundation-layer/cache.md)
  * [EhCache](./foundation-layer/cache-ehcache.md)
  * [Cache Abstraction](./foundation-layer/cache-abstraction.md)
* [Marshalling/Unmarshalling](./foundation-layer/marshalling-unmarshalling-service.md)
* [XML Manipulation](./foundation-layer/xml-manipulation-service.md)
* [Object Pooling](./foundation-layer/object-pooling-service.md)
* Crypto
  * [Encryption/Decryption](./foundation-layer/crypto-encryption-decryption.md)
  * [crypto 간소화](./foundation-layer/crypto-simplification-service.md)
* [FTP](./foundation-layer/ftp-service.md)
* [Mail](./foundation-layer/mail-service.md)
* [Compress/Decompress](./foundation-layer/compress-decompress-service.md)
* [File Upload/Download](./foundation-layer/file-updown-service.md)
  * [file_upload](./foundation-layer/file-upload-service.md)
  * [file_download](./foundation-layer/file-down-service.md)
* [File Handling](./foundation-layer/file-handling.md)
* [Excel](./foundation-layer/excel-service.md)
* [String Util](./foundation-layer/string-util-service.md)

### 화면처리
* [Web Servlet](./presentation-layer/web-servlet.md)
  * [Spring MVC Architecture](./presentation-layer/web-servlet-spring-mvc-architecture.md)  
    스프링 MVC의 기본 구조 및 핵심 컴포넌트에 대해 설명한다.
  * [DispatcherServlet](./presentation-layer/web-servlet-dispatcherservlet.md)  
    스프링 MVC의 핵심 컴포넌트인 DispatcherServlet의 기능과 등록방법에 대해 설명한다.
  * [HandlerMapping](./presentation-layer/web-servlet-handlermapping.md)  
    요청과 Controller간의 연결고리 역활을 하는 컴포넌트인 HandlerMapping에 대해서 설명한다.
  * [Spring MVC tag configuration](./presentation-layer/web-servlet-spring-mvc-tag-configuration.md)  
    Spring에서 제공하는 MVC태그를 통해 간단하게 설정하는 방법에 대하여 설명한다.
  * [Controller](./presentation-layer/web-servlet-controller.md)  
    인터페이스 Controller를 구현한 AbstractController, SimpleFormContrller 같은 계층형(hierarchy) Controller에 대해서 설명한다.
  * [Annotation-based Controller](./presentation-layer/web-servlet-annotation-based-controller.md)  
    @MVC구현을 위한 관련 어노테이션과 활용 방법에 대해서 설명한다.
  * [Validation](./presentation-layer/web-servlet-validation.md)  
    객체의 유효성 검증 기능에 대해서 설명한다.
  * [Declarative Validation](./presentation-layer/web-servlet-declarative-validation.md)  
    스프링의 선언적 Validation 기능에 대해서 설명한다.
  * [View](./presentation-layer/web-servlet-view.md)  
    스프링 MVC의 View와 스프링 폼 태그에 대해서 설명한다.
  * [AnnotationCommandMapArgumentResolver](./presentation-layer/web-servlet-AnnotationCommandMapArgumentResolver.md)  
    Request Parameter값을 @RequestParam을 통해 손쉽게 가져오는 방법을 설명한다.
* [Web Reactive](./presentation-layer/web-reactive.md)
  * [Reactive Core](./presentation-layer/web-reactive-reactive-core.md)
  * [DispatcherHandler](./presentation-layer/web-reactive-dispatcherhandler.md)
  * [Annotated Controllers](./presentation-layer/web-reactive-annotated-controllers.md)
  * [Functional Endpoints](./presentation-layer/web-reactive-functional-endpoints.md)
  * [WebClient](./presentation-layer/web-reactive-webclient.md)
* [Ajax 지원](./presentation-layer/ajax.md)
* [Internationalization](./presentation-layer/internationalization.md)
* [Security](./presentation-layer/security-service.md)
* [UI Adaptor](./presentation-layer/ui-adaptor-service.md)
* [Asynchronous request processing](./presentation-layer/asynchronous-request-processing.md)  
  비동기요청처리에 대하여 설명한다.
* [jQuery ajax](./presentation-layer/jquery-ajax.md)
* [WebSocket](./presentation-layer/websocket.md)
  * [STOMP](./presentation-layer/websocket-stomp.md)
  * [SockJS](./presentation-layer/websocket-sockjs.md)
* [bootstrap](./presentation-layer/bootstrap.md)

### UX처리
* [UX/UI Controller Component](./presentation-layer/uxui-controller-component.md)
* [HTML5+CSS3.0+JavaScript Module App Framework 기본 활용](./presentation-layer/html5-css3.0-javascript-module-app-framework-basic.md)
* [UI - bootstrap](./presentation-layer/bootstrap.md)

### 업무처리
* [Exception Handling](./business-logic-layer/exception-handling.md)
* [Spring Web Flow](./business-logic-layer/spring-web-flow.md)
  * SWF Getting Started
    * [Hello world](./business-logic-layer/getting-started.md)  
      Hello 예제 2가지를 샘플로 설명한다.
  * SWF Configuration
    * [SWF 시스템 설정](./business-logic-layer/setting-system.md)  
      Spring Web Flow 를 사용하기 위한 Web 개발환경에 대한 세팅을 설명한다.
    * [Spring Web Flow 와 MVC 연동](./business-logic-layer/with-spring-mvc.md)  
      Spring Web Flow 를 사용하기 위한 Spring MVC 설정을 설명한다.
    * [Securing Flows](./business-logic-layer/securing-flows.md)  
      Web Flow 에 적용되는 Spring Security 에 대해 설명한다.
    * [Flow Managed Persistence](./business-logic-layer/flow-managed-persistence.md)  
      Web Flow에서 하이버네이트와 JPA 객체 영속화 기술과 연동에 관해 설명한다.
  * SWF
    * [Flow Definition](./business-logic-layer/flow-definiton.md)  
      Flow 의 필수적인 언어 구성요소와 sub flow 에 대해 설명한다.
    * [Expression Language](./business-logic-layer/expression-language.md)  
      Web Flow 설계시 데이타 모델 및 action 실행을 위한 EL을 설명한다.
    * [Rendering Views](./business-logic-layer/rendering-views.md)  
      flow 내에서 화면을 생성하는 요소에 대해 설명한다.
    * [Executing actions](./business-logic-layer/executing_actions.md)  
      flow 내에서 실행 요소에 대해 설명한다.
    * [Flow Inheritance](./business-logic-layer/flow-inheritance.md)  
      flow 간의 상속에 대해 설명한다.

### 데이터처리
* [Data Source](./persistence-layer/data-source.md)
* [iBatis](./persistence-layer/data-access.md)
  * [iBATIS Configuration](./persistence-layer/dataaccess-ibatis_configuration.md)
  * [Spring iBatis Integration](./persistence-layer/dataaccess-spring_ibatis_integration.md)
  * [Data Type](./persistence-layer/dataaccess-data_type.md)
  * [parameterMap](./persistence-layer/dataaccess-parametermap.md)
  * [Inline Parameters](./persistence-layer/dataaccess-inline_parameters.md)
  * [resultMap](./persistence-layer/dataaccess-resultmap.md)
  * [Dynamic SQL](./persistence-layer/dataaccess-dynamic_sql.md)
* [MyBatis](./persistence-layer/jpa-mybatis.md)
  * [주요 변경 사항](./persistence-layer/dataaccess-ibatis_vs_mybatis.md)
  * [Getting Started](./persistence-layer/dataaccess-getting_started.md)
  * [Configuration XML](./persistence-layer/dataaccess-configuration_xml.md)
  * [Mapper XML Files](./persistence-layer/dataaccess-mapper_xml_files.md)
  * [Dynamic SQL](./persistence-layer/dataaccess-mybatis-dynamic-sql.md)
  * [표준프레임워크 기반 적용 가이드](./persistence-layer/dataaccess-mybatis-guide.md)
* [Spring Data - JPA](./persistence-layer/jpa-spring-data.md)
  * [Repository](./persistence-layer/jpa-repository.md)
  * [Query Method](./persistence-layer/jpa-querymethod.md)
* Spring Data - MongoDB
  * [MongoDB support](./persistence-layer/mongodb-support.md)
  * [MongoDB Repositories](./persistence-layer/mongodb-repositories.md)
  * [MongoDB support 3.5.1](./persistence-layer/mongodb-support3_5_1.md)
  * [MongoDB Repositories 3.5.1](./persistence-layer/mongodb-repositories3_5_1.md)
* [ORM](./persistence-layer/orm.md)
  * [Entities](./persistence-layer/orm-entities.md)
  * [Entity Operation](./persistence-layer/orm-entity_operation.md)
  * [Association Mapping](./persistence-layer/dataaccess-association_mapping.md)
  * [Query Language](./persistence-layer/orm-query_language.md)
  * [Native SQL](./persistence-layer/orm-native_sql.md)
  * [Concurrency](./persistence-layer/orm-concurrency.md)
  * [Cache Handling](./persistence-layer/orm-cache_handling.md)
  * [Fetch Strategy](./persistence-layer/orm-fetch_strategy.md)
  * [Spring Integration](./persistence-layer/orm-spring_integration.md)
  * [JPA Configuration](./persistence-layer/orm-jpa_configuration.md)
* [Transaction](./persistence-layer/transaction.md)
* [Spring Data - Reactive](./persistence-layer/reactive-preface.md)
  * [R2DBC](./persistence-layer/reactive-r2dbc.md)
  * [MongoDB](./persistence-layer/reactive-mongodb.md)
  * [Cassandra](./persistence-layer/reactive-cassandra.md)
  * [Redis](./persistence-layer/reactive-redis.md)

### 연계통합
* [Naming Service](./integration-layer/naming-service.md)
* [Integration Service](./integration-layer/integration-service.md)
  * [Metadata](./integration-layer/integration-service-metadata.md)
  * [연계 서비스 API](./integration-layer/integration-service-api.md)
* [WebService](./integration-layer/webservice.md)
* [Restful](./integration-layer/restful.md)   
  스프링의 Restful Web Service의 사용법에 대해서 설명한다.
* [Cloud Data Stream](./integration-layer/cloud-data-stream.md)
* [Swagger](./integration-layer/swagger.md)

### 배치처리
* [배치실행환경소개](./batch-layer/intro.md)
* Batch Core
  * [Job Configuration](./batch-layer/batch-core-job.md)  
    배치처리 기능 중 Job 설정에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Job Execution](./batch-layer/batch-core-job.md#jobexecution)  
    배치처리 기능 중 Job 실행에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Step Configuration](./batch-layer/batch-core-step.md)  
    배치처리 기능 중 Step 설정에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [Step Execution](./batch-layer/batch-core-step.md#stepexecution)  
    배치처리 기능 중 Step 실행에 관한 기본 개념 및 사용법에 대해 설명한다.
  * [ItemReader](./batch-layer/batch-core-itemreader.md) / [ItemWriter](./batch-layer/batch-core-item-writer.md) / [Resource Variable](./batch-layer/batch-core-resource-variable.md)  
    리소스 설정 및 Read/Write하는 방법에 대해 설명한다.
  * [Tasklet](./batch-layer/batch-core-step.md#taskletstep)  
    아이템 기반이 아닌 배치처리에 대한 기본개념 및 사용법에 대해 설명한다.
* Batch Execution
  * [JobRepository](./batch-layer/batch-execution-job_repository.md)   
    배치수행정보를 저장하는 JobRepository의 기본 개념 및 사용법에 대해 설명한다.
  * [JobLauncher](./batch-layer/batch-execution-job-launcher.md)   
    배치작업을 실행하는 JobLauncher의 기본 개념 및 사용법에 대해 설명한다.
    * [Remote JobLauncher](./batch-layer/batch-execution-remote-job-launcher.md)  
      Online에서 배치계의 Batch Job을 기동시키기 위하여 Batch Remote Client의 기본 개념 및 사용법에 대해 설명한다.
  * [JobRunner](./batch-layer/batch-execution-job-runner.md)   
    다양한 유형의 배치실행을 지원하는 JobRunner설정에 관한 기본 개념 및 사용법에 대해 설명한다.
* Batch Support
  * [Skip/Retry/Repeat](./batch-layer/batch-core-skip_repeat_retry.md)   
    배치수행 중 오류처리와 관련한 Skip/Retry/Repeat의 기본 개념 및 사용법에 대해 설명한다.
  * [MultiData Processing](./batch-layer/batch-core-multidata_process.md)   
    다수 건의 리소스를 처리하는 MultiData Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [History Management](./batch-layer/batch-core-history_management.md)   
    배치수행 이력정보를 관리하는 History Management의 기본 개념 및 사용법에 대해 설명한다.
  * [Sync / Async Processing](./batch-layer/batch-example-sync_async_v3.7.md)   
    동기,비동기 실행을 지원하는 Sync / Async Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [Pre / Post Processing](./batch-layer/batch-core-listener.md)   
    전처리,후처리 실행을 지원하는 Pre / Post Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [Parallel Processing](./batch-layer/batch-core-parallel_process.md)   
    배치수행 시 성능향상을 위한 Parallel Processing의 기본 개념 및 사용법에 대해 설명한다.
  * [Code Base Exception](./batch-layer/batch-core-code_base_exception.md)   
    배치수행 시 코드기반 에러 처리에 대한 기본 사용법에 대해 설명한다.
* [Center Cut](./batch-layer/batch-centercut-intro.md)   
  큐를 사용한 센터 컷의 관한 기본 개념 및 사용법에 대해 설명한다.


### 배치운영환경
* [배치운영환경]()   
  일괄(배치) 개발/실행환경에서 작성된 배치Job을 등록/실행하고 수행현황을 모니터링하며 처리결과를 확인하기 위한 표준화된 운영환경을 제공합니다.