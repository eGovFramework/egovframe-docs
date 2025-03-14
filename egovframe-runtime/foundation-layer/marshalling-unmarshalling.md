---
title: Marshalling/Unmarshallig 서비스
linkTitle: "Marshalling/Unmarshallig"
description: Marshalling/Unmarshalling 서비스는 Java 객체를 XML로 변환(Marshalling)하거나, XML을 Java 객체로 변환(Unmarshalling)하는 기술이다. Spring은 이를 위해 다양한 OXM 툴(JAXB, Castor, XMLBeans 등)을 지원하며, 이 기능을 활용해 객체와 XML 간의 데이터 매핑을 쉽게 처리할 수 있다. Castor와 XMLBeans를 이용한 샘플 코드는 각각 XML 문서로 데이터를 저장하고 다시 객체로 변환하는 과정으로 구성되어 있다.
url: /egovframe-runtime/foundation-layer/marshalling-unmarshallig/
menu:
    depth:
        name: Marshalling/Unmarshallig
        weight: 9
        parent: "foundation-layer"
---
# Marshalling/Unmarshallig 서비스

## 개요

Object/XML Mapping, 줄여서 O/X mapping은 Object를 XML문서로 변환하는데 이를 **XML Mashalling** 또는 **Marshalling** 이다. 반대로 XML문서를 Object로 변환하는 것은 **Unmarshalling** 이다.

## 설명

### Spring Web Service OXM

```
Client <------ XML ------> Server
```

WS는 Server와 Client 두 대상 간의 데이터를 주고받는 기술 중 하나이다. 정보를 요청하는쪽이 Client이다.(Client는 Server가 될 수도 있고 일반 사용자가 될 수도 있다.) 요청한 정보를 받아서 알맞게 처리 후 결과값을 리턴하는 쪽이 Server이다.

```
Client(OXM) <------ XML(WSDL) ------> (OXM)Server
```

WS는 XML(WSDL)형식으로 데이터를 주고받는다. 따라서 이 XML를 객체화 하거나 객체를 XML화 해야 한다. 그것이 Marshalling,Unmarshalling이다. OXM Utill은 JAXB,Castor,XMLBeans,JiBX,XStream..등 여러 가지가 있다.

### Marshalling

Spring의 모든 marshalling 추상 클래스들은 [org.springframework.oxm.Marshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/Marshaller.html) interface를 implemention 한다.

```java
public interface Marshaller {
  /**
   * Marshals the object graph with the given root into the provided Result.
   */
  void marshal(Object graph, Result result)
      throws XmlMappingException, IOException;
}
```

| PARAMETER                    | 설 명                                      |
|------------------------------|------------------------------------------|
|  Object                      |  XML문서구조와 같은 Java 객체                     |
|  javax.xml.transform.Result  |   XML 출력과 관련된 객체들이 반드시 구현해야 할 Interface  |

- java.xml.transform.Result는 XML 출력과 관련된 객체들이 반드시 구현해야 할 Interface다.
- 구현 객체와 XML표현은 다음과 같이 매칭된다.

| javax.xml.transform.Result               |   XML표현                                              |
|------------------------------------------|------------------------------------------------------|
| javax.xml.transform.dom.DOMResult 	      | org.w3c.dom.Node 	                                   |
| javax.xml.transform.sax.SAXResult        | org.xml.sax.ContentHandler                           |
| javax.xml.transform.stream.StreamResult  | java.io.OutputStream java.io.File 또는 java.io.Writer  |

### Unmarshalling

Spring의 모든 Unmarshalling 추상 클래스들은 [org.springframework.oxm.Unmarshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/Unmarshaller.html) interface를 implemention 한다.

```java
public interface Unmarshaller {
  /**
   * Unmarshals the given provided Source into an object graph.
   */
  Object unmarshal(Source source)
      throws XmlMappingException, IOException;
}
```

| PARAMETER                     | 설 명                                                                     |
|-------------------------------|-------------------------------------------------------------------------|
|  javax.xml.transform.Source   |   XML source or transformation instructions 등을 매개변수로 받는 StreamSource 객체 |

- java.xml.transform.Source는 XML 입력과 관련된 객체들이 반드시 구현해야 할 Interface다.
- 구현 객체와 XML표현은 다음과 같이 매칭된다.

| javax.xml.transform.Source                |   XML표현                                             |
|-------------------------------------------|-----------------------------------------------------|
| javax.xml.transform.dom.DOMSource 	       | org.w3c.dom.Node 	                                  |
| javax.xml.transform.sax.SAXSource         | org.xml.sax.InputSource org.xml.sax.XMLReader       |
| javax.xml.transform.stream.StreamSource   | java.io.File java.io.InputStream 또는 java.io.Reader  |

### Marshaller 와 Unmarshaller 사용하기

[Spring's OXM](http://static.springframework.org/spring-ws/sites/1.5/apidocs/index.html)은 다양한 Java-XML Binding 오픈소스를 지원한다. 여기서는 오픈소스 [Castor](http://www.castor.org/)와 [XMLBeans](http://xmlbeans.apache.org/)를 사용하여 구현한 가이드프로그램을 제시한다.

#### Castor

Castor XML mapping은 XML Binding 오픈소스 프레임워크이다. Castor는 java object에서 XML문서, XML문서에서 java object로 변환을 지원한다. mapping file을 사용하여 좀더 수월하게 Castor를 사용할 수 있지만 그 외 추가적인 구성은 할 필요가 없다. 좀 더 많은 OpenSource Castor 정보를 원한다면 [Castor web site](http://www.castor.org/)와 [org.springframework.oxm.castor](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/castor/package-summary.html) **package**를 참조하면 된다.

##### Create binding classes

- XML Schemas를 작성한다.(text.xsd)
- 다음을 실행하면 스키마에 따라 -package에 지정된 패키지로 클래스들이 생성된다.
- java org.exolab.castor.builder.SourceGenerator -i text.xsd -package gen.xyz

|  ARGS     |  설 명                                         |
|-----------|----------------------------------------------|
| text.xsd  | 참조할 xml 스키마                                  |
| gen.xyz   | xml 스키마를 사용하여 Generation한 Java class package |

##### Configuration

```xml
<bean id="divertcastor" class="egovframework.rte.fdl.divert.DivertCastor">
        <property name="marshaller" ref="castorMarshaller" />
        <property name="unmarshaller" ref="castorMarshaller" />
</bean>
<bean id="castorMarshaller" class="org.springframework.oxm.castor.CastorMarshaller"/>
```

|  PROPERTIES  |  설 명                                            |
|--------------|-------------------------------------------------|
| marshaller   | [org.springframework.oxm.castor.CastorMarshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/castor/CastorMarshaller.html) |
| unmarshaller | [org.springframework.oxm.castor.CastorMarshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/castor/CastorMarshaller.html) |

##### Sample Source

**Java Object의 데이타를 XML문서로 DataBinding Sample Source**

```java
@Resource(name = "castorMarshaller")
private Marshaller marshaller;
 
public void testMarshalling() 
{
 try {
       FileOutputStream os = null;
       List<Writer> book2Writers = new ArrayList<Writer>();
       book2Writers.add(new Writer("J,J.R 툴킨"));
       book2Writers.add(new Writer("J.J.T 툴킨"));
       BookMg bookMg2 = new BookMg("9780446618502", "반지의 제왕", book2Writers);
 
       os = new FileOutputStream("CasterBook.xml");
       marshaller.marshal(bookMg2, new StreamResult(os));
 
     } catch (Exception e) 
     {
	logger.debug(e.getMessage());
	e.printStackTrace(System.err);
	fail("testMarshalling failed!");
     }
}
```

1. writer를 작가명을 매개변수로 하여 생성한다. (아래 Writer.java 코드 참조)
2. bookMg를 ISDN,책명,writer를 매개변수로 하여 생성한다. (아래 BookMg.java 코드 참조)
3. FileOutputSream을 Caster_Book.xml를 매개변수로 하여 Stream를 생성한다.
4. Result을 생성한 FileOutputStream을 매개변수로 하여 StreamResult를 생성한다.
5. marshaller.marshal를 사용하여 marshalling을 하는데 매개변수로는 bookMg와 StreamResult로 한다.
6. 실행후 JavaObject bookMg에 저장한 값이 CasterBook.xml로 Binding 된것을 확인한다. (아래 CasterBook.xml 코드 참조)

Writer.java
```java
public class Writer 
{
  private String Name;
  // 생성자
  public Writer() { }
  // 작가명
  public Writer(String Name) {
    this.Name = Name;
  }
  // 작가명 수정
  public void setName(String Name) {
    this.Name = Name;
  }
  // 작가명 리턴 
   public String getName() {
    return Name;
  }
}
```

BookMg.java
```java
public class BookMg 
{
  private String isbn;
  private String title;
  private List<Writer> writers;
 
  public BookMg() { }
  // 생성자
  @ isbn 책번호
  @ title 책제목
  @ writers 작가리스트
  public BookMg(String isbn, String title, List<Writer> writers) {
    this.isbn = isbn;
    this.title = title;
    this.writers = writers;
  }
   // 생성자
  @ isbn 책번호
  @ title 책제목
  @ writer 작가
  public BookMg(String isbn, String title, Writer writer) {
    this.isbn = isbn;
    this.title = title;
    this.writers = new LinkedList<Writer>();
    writers.add(writer);
  }
 // 책번호 설정
 @ isbn 책번호
  public void setIsbn(String isbn) {
    this.isbn = isbn;
  }
 // 책번호 리턴 
  public String getIsbn() {
    return isbn;
  }
 // 책제목 설정
 @ title 책제목
  public void setTitle(String title) {
    this.title = title;
  }
 // 책제목 리턴
  public String getTitle() {
    return title;
  }
 // 작가리스트 설정
 @ writers 작가리스트
  public void setWriters(List<Writer> writers) {
    this.writers = writers;
  }
 // 작가리스트 리턴 
  public List<Writer> getWriters() {
    return writers;
  }
 // 작가리스트에 작가 추가
 @ writer 작가
  public void addWriter(Writer writer) {
    writers.add(writer);
  }
}
```

CasterBook.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<book-mg>
  <isbn>9780446618502</isbn>
  <writers xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:type="java:egovframework.rte.fdl.divert.Writer">
    <name>J,J.R 툴킨</name>
  </writers>
  <writers xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:type="java:egovframework.rte.fdl.divert.Writer">
    <name>J.J.T 툴킨</name>
  </writers>
  <title>반지의 제왕2</title>
</book-mg>
```


**##### **XML문서를 JavaObject로 DataBinding Sample Source**

```java
@Resource(name = "castorMarshaller")
private Unmarshaller unmarshaller;
 
@Test
public void testUnmarshalling() 
{
   FileInputStream is = null;
  try 
  {
    is = new FileInputStream("CasterBook.xml");
    bookMg = (BookMg) unmarshaller.unmarshal(new StreamSource(is));
    writers = bookMg.getWriters();
    for (Iterator i = writers.iterator(); i.hasNext(); ) 
    {
      Writer writer = (Writer)i.next();
    }
  }catch(FileNotFoundException fnde)
  {
	fnde.getStackTrace();
  }
  catch(IOException ioe)
 {
	ioe.getStackTrace();
 }
 finally 
 {
    if (is != null) 
    {
     try
     {
	is.close();
     }catch(IOException ioe)
     {
	ioe.getStackTrace();
     }
   }
 }
}
```



1. FileInputSream을 CasterBook.xml를 매개변수로 하여 Stream를 생성한다.  (위 CasterBook.xml 코드 참조)
2. 생성한 FileInputSream을 매개변수로 하여 StreamSource를 생성한다.
3. marshaller.marshal를 사용하여 unmarshalling을 하는데 매개변수로는 StreamSource로 한다.
4. unmarshalling한 결과 bookMg를 얻어 작가 리스트를 얻는다.

#### XMLBeans

XMLBeans는 스키마 기반으로 XML 인포셋 전체에 커서 기반으로 접근할 수 있도록 하는 XML-Java binding tool이다. BEA Systems에 의해 개발되었으며 2003년에 아파치 프로젝트에 기증 되었다. 좀 더 많은 정보는 [XMLBeans web site](http://xmlbeans.apache.org/) 와 [org.springframework.oxm.xmlbeans](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/xmlbeans/package-summary.html) package를 참조 하면 된다.

##### Create binding jar

- XML Schemas를 작성한다.(text.xsd)
- 다음을 실행하면 스키마에 따라 jar 파일이 생성된다.
- scomp -out text.jar text.xsd

|  ARGS    |  설 명                |
|----------|---------------------|
| text.jar | binding classes jar |
| text.xsd | 참조할 xml 스키마         |

##### Configuration

```xml
<bean id="divertxmlbeans" class="egovframework.rte.fdl.divert.DivertXMLBeans">
          <property name="marshaller" ref="xmlBeansMarshaller" />
          <property name="unmarshaller" ref="xmlBeansMarshaller" />
</bean>
<bean id="xmlBeansMarshaller" class="org.springframework.oxm.xmlbeans.XmlBeansMarshaller" />
```

|  PROPERTIES  |  설 명                                                |
|--------------|-----------------------------------------------------|
| marshaller   | [org.springframework.oxm.xmlbeans.XmlBeansMarshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/xmlbeans/XmlBeansMarshaller.html) |
| unmarshaller | [org.springframework.oxm.xmlbeans.XmlBeansMarshaller](http://static.springframework.org/spring-ws/sites/1.5/apidocs/org/springframework/oxm/xmlbeans/XmlBeansMarshaller.html) |


##### Sample Source

**Java Object의 데이터를 XML문서로 DataBinding Sample Source**

```java
@Resource(name = "xmlBeansMarshaller")
private Marshaller marshaller;
 
@Test
public void testMarshalling() 
{
  FileOutputStream os = null; 
  userDoc = UserinfoDocument.Factory.newInstance();
  userElement = userDoc.addNewUserinfo();
 
  userElement.setName("홍길동");
  userElement.setAge(31);
  userElement.setPhone(022770918);
 
  xmlOptions = new XmlOptions();
  xmlOptions.setSavePrettyPrint();
  xmlOptions.setSavePrettyPrintIndent(4);
  xmlOptions.setCharacterEncoding("euc-kr");
 
 try 
 {
    os = new FileOutputStream("XMLBeanGen.xml");
    marshaller.marshal(userDoc, new StreamResult(os));
 }catch(Exception ee)
 {
   ee.getStackTrace();
   fail("testMarshalling failed!");
 }
 finally 
 {
    if (os != null) 
    {
      try
      {
	 os.close();
       }catch(IOException e3)
       {
  	 e3.getStackTrace();
	 fail("testMarshalling failed!");
       }
    }
  }
}
```

1. UserDoc 인스턴스를 생성한다.
2. 사용자정보를 저장할 userElement를 추가한다.
3. setName을 사용하여 사용자명을 저장한다.
4. setAge를 사용하여 나이를 저장한다.
5. setPhone를 사용하여 전화번호를 저장한다.
6. FileOutputSream을 XMLBeanGen.xml을 매개변수로 하여 생성한다. (아래 XMLBeanGen.xml 코드 참조)
7. marshaller.marshal를 Document객체와 StreamResult를 매개변수로 하여한다.

XMLBeanGen.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<userinfo>
  <name>홍길동</name>
  <age>31</age>
  <phone>022770918</phone>
</userinfo>
```

**XML문서를 JavaObject로 DataBinding Sample Source**

```java
@Resource(name = "xmlBeansMarshaller")
private Unmarshaller unmarshaller;
 
@Test
public void testUnmarshalling() 
{
    FileInputStream is = null;
    try 
    {
	is = new FileInputStream("XMLBeanGen.xml");
	userDoc = (UserinfoDocument) unmarshaller.unmarshal(new StreamSource(is));
	userElement =  userDoc.getUserinfo();
     }catch(FileNotFoundException fnde)
    {
	fnde.getStackTrace();
	fail("testUnmarshalling failed!");
    }
    catch(IOException ioe)
    {
	ioe.getStackTrace();
    }
    finally 
    {
      if (is != null)
      {
	try
	{
	   is.close();
	}catch(IOException ioe)
	{
	  ioe.getStackTrace();
	  fail("testUnmarshalling failed!");
	}
      }
    }
}
```

1. FileInputStream를 XMLBeanGen.xml을 매개변수로 하여 생성한다. (위 XMLBeanGen.xml 코드 참조)
2. 생성한 FileInputStream를 매개변수로 하여 StreamSource생성한다.
3. unmarshaller.unmarshal를 생성한 StreamSource를 매개변수로 unmashalling을 하여 document객체를 얻는다.
4. document객체에서 사용자정보를 얻는다.

## 참고자료
- [http://castor.codehaus.org/](http://castor.codehaus.org/)
- [http://xmlbeans.apache.org/documentation/tutorial_getstarted.html](http://xmlbeans.apache.org/documentation/tutorial_getstarted.html)

## 예제
- [marshalling/unmarshalling 예제](../../runtime-example/individual-example/foundation-layer/marshalling-unmarshalling-example.md)