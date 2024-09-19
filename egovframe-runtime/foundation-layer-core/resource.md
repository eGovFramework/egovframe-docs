# Resource 서비스

## 개요

 리소스를 활용하여 가장 많이 사용하는 메시지 제공 서비스를 살펴본다. 메시지 제공 서비스는 미리 정의된 파일에서 메시지를 읽어 들인 후, 오류 발생시 또는 안내 메시지를 제공하기 위해 키값에 해당하는 메시지를 가져오는 기능을 제공한다.

## 설명

### Message Basic

 메시지를 활용하기 위한 기본 설정 및 활용에 대해서 예제를 중심으로 설명한다.

#### Configuration

```xml
<bean name="messageSource"  class="org.springframework.context.support.ResourceBundleMessageSource">
   <property name="useCodeAsDefaultMessage">
      <value>true</value>
   </property>
   <property name="basenames">
      <list>
         <value>egovframework-message</value>
      </list>
   </property>
</bean>
```

 위의 설정에서”egovframework-message” 로 지정한 파일은 실제로는 egovframework-message.properties 로 정의되어 있다. 파일의 위치를 지정하는 방법이 여러가지가 가능한데 그 설정에 대한 것은 [4.참고자료](https://www.egovframe.go.kr//wiki/doku.php?id=egovframework:rte:fdl:resource#참고자료) 참조.

#### Sample Source

```bash
//egovframework-message.properties에 정의된 메시지 내용.
resource.basic.msg1=message1
 
@Resource(name="messageSource")
MessageSource messageSource ;
 
[String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky) getMsg = messageSource.getMessage("resource.basic.msg1" , null , [Locale](http://www.google.com/search?hl=en&q=allinurl%3Alocale+java.sun.com&btnI=I%27m%20Feeling%20Lucky).getDefault() );
assertEquals("Get Message Success!", getMsg , "message1");
```

 위의 소스를 보면 messageSource.getMessage를 이용하여 Massage를 얻는 것을 확인 할 수 있다.

### Message Locale

 동일한 메시지 키를 가지고 언어별로 별도로 설정 관리하여 사용자에 따라서 사용자에 맞는 언어로 메시지를 제공할 수 있다.

#### Configuration

```xml
<bean name="messageSource" 
   class="org.springframework.context.support.ResourceBundleMessageSource">
   <property name="useCodeAsDefaultMessage">
      <value>true</value>
   </property>
   <property name="basenames">
      <list>
         <value>egovframework-message-locale</value>		
      </list>
   </property>
</bean>
```

 위의 설정에서”egovframework-message-locale” 로 지정한 파일을 egovframework-message-locale\_ko.properties,egovframework-message-locale\_en.properties로 정의하고 동일한 메시지키에 해당하는 메시지를 달리 지정한다.

#### Propreties File

```bash
//egovframework-message-locale_ko.properties 파일 내용
resource.locale.msg1=메시지1
 
//egovframework-message-locale_en.properties 파일 내용
resource.locale.msg1=en_message1
```

 위에서 resource.locale.msg1 라는 키에 다른 메시지를 설정한 것을 확인할 수 있다. 위와 같이 설정하면 locale 정보에 따라서 메시지를 제공받을 수 있다.

#### Sample Source

```bash
//egovframework-message.properties에 정의된 메시지 내용.
resource.basic.msg1=message1
 
[String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky) getMsg = messageSource.getMessage("resource.locale.msg1" , null , [Locale](http://www.google.com/search?hl=en&q=allinurl%3Alocale+java.sun.com&btnI=I%27m%20Feeling%20Lucky).KOREAN );
assertEquals("Get Message Success!", getMsg , "메시지1");
 
[String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky) getMsg = messageSource.getMessage("resource.locale.msg1" , null , [Locale](http://www.google.com/search?hl=en&q=allinurl%3Alocale+java.sun.com&btnI=I%27m%20Feeling%20Lucky).ENGLISH );
assertEquals("Get Message Success!", getMsg , "en_message1");
```

 위에서 Locale정보에 따라서 추출되는 메시지의 내용이 다른 것을 확인할 수 있다.

### Message Parameter

 프로그램 수행중에 발생되는 메시지를 추가하여 제공 할 수 있는데 그것에 대한 사용 방법은 설정은 위와 동일하고 Properties 파일에 아래와 같이 설정한다.

#### Properties File

```bash
resource.basic.msg3=message {0} {1}
```

 위에서 {0},{1}로 정의된 부분에 추가 메시지를 입력하여 제공 받을 수 있다. 위의 설정을 활용하는 샘플은 아래와 같다.

#### Sample Source

```bash
[Object](http://www.google.com/search?hl=en&q=allinurl%3Aobject+java.sun.com&btnI=I%27m%20Feeling%20Lucky)[] parameter = { new [String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky)("1") , new [Integer](http://www.google.com/search?hl=en&q=allinurl%3Ainteger+java.sun.com&btnI=I%27m%20Feeling%20Lucky)(2) };
 
[String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky) getMsg = messageSource.getMessage("resource.basic.msg3" , parameter , [Locale](http://www.google.com/search?hl=en&q=allinurl%3Alocale+java.sun.com&btnI=I%27m%20Feeling%20Lucky).getDefault() );
assertEquals("Get Message Success!", getMsg , "message 1 2");
```

 위에서 parameter에 1과 2를 지정하여 getMessage의 두번째 인자에 넣고 호출하면 리턴 메시지로 “message 1 2”를 얻는 것을 확인 할 수 있다.

## 참고자료

- [Spring Framework - Reference Document / 2. Spring Resource](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#resources)