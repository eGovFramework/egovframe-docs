---
linkTitle: "Tomcat 한글"
title: Tomcat 한글 설정하기
description: Tomcat에서 문자셋 인코딩을 하여 한글이 깨지는 문제를 해결할 수 있다.
url: /egovframe-runtime/foundation-layer/file-upload-download-service/file-download/file-download-service-tomcat-encoding/
menu:
    depth:
        name: Tomcat 한글
        weight: 1
        parent: "fileDownload"
---
# Tomcat 한글 설정하기

## 개요

Tomcat에서 문자셋 인코딩을 하여 한글이 깨지는 문제를 해결할 수 있다.

## 설명

일반적으로 웹 어플리케이션이 GET과 POST 방식으로 파라미터를 넘겨 받을 때 request.setCharacterEncoding()을 통한 문자셋 인코딩이 필요하다.

#### Tomcat 4.x

```
단순히 JSP 혹은 서블릿의 최 상단에 request.setCharacterEncoding("euc-kr");을 하면 된다. 

GET과 POST 방식에 상관없이 인코딩을 해준다. 
```

#### Tomcat 5.x

```xml
POST 방식은 request.setCharacterEncoding("euc-kr");로 계속 하면된다. 
 
하지만 GET 방식은 server.xml의 <Connector> 설정 부분을 바꿔줘야만 한다. 
 
<Connector port="8080" 
maxThreads="150" minSpareThreads="25" maxSpareThreads="75" 
enableLookups="false" redirectPort="8443" acceptCount="100" 
debug="0" connectionTimeout="20000" 
disableUploadTimeout="true" URIEncoding="euc-kr"/> 
 
위에서 URIEncoding="euc-kr" 부분이다.
```

결론적으로 Tomcat 4.x와 Tomcat 5.x 는 모두 request.setCharacterEncoding()이 필요하다는 사실에는 변함이 없다.

#### 한글 파라미터를 가진 링크를 만들 때

JSP페이지에서 링크를 생성할 때, 한글이 됐든 공백이나 특수문자를 가진 영어가 됐든, 순수하게 영어와 숫자, 밑줄 등으로만 이뤄진게 아닌 모든 파라미터를 넘길 때는 무조건 URLEncoding을 해야한다고 봐도 된다.

Web Container에 따라 URLEncoding을 안하고 넘겨도 작동하는 경우가 있는데, 동일한 웹 컨테이너라도 버전에 따라 한글을 제대로 인식하지 못하는 경우도 있고, 또 다른 컨테이너에서는 URLEncoding이 안된 한글을 전혀 인식하지 못할 수도 있다.

그러므로 무조건 표준을 따라서 java.net.URLEncoder.encode()메 소드를 사용해 인코딩해서 넘기도록 한다. 디코드 작업은 request.setCharacterEncoding()에 의해서 자동으로 이뤄지므로 해줄것이 없다. (Tomcat 3.x대- JSP Spec 1.1 -에서는 request.setCharacterEncoding()이 없으므로 String.getBytes()를 이용해 직접 디코딩을 해줘야만 했다)

#### <%@ include file="test.jspf"%> 에서의 한글 

위와 같이 test.jspf를 static include 할 경우에 test.jspf에 있는 한글이 모두 깨질 수 있다. test.jspf에도 한글 설정이 필요한데, 이 경우에는 test.jspf의 최 상단에 다음을 추가하면 된다.

```jsp
<%@page pageEncoding="euc-kr"%>
```

- static include : JSP 페이지를 컴파일하는 시점에 해당 jspf 파일의 내용을 문자열 그대로 현재 jsp에 삽입하여 컴파일 하는 것. static include 방식에서 include 되는 대상 jsp의 확장자는 .jspf로 하는 것이 표준이다. .jspf 는 단독 실행을 위한 것이 아니라 항상 다른 JSP에 포함되어 쓰이는 목적으로 만들어졌기 때문에 완전한 JSP의 형태를 갖추고 있지 않다. 
- \<jsp:include page=””/> 이 방식은 동적 include 방식으로, JSP 페이지가 실행되는 중간에 page에 지정된 jsp를 실행한 결과를 삽입하는 방식이다. 이 방식에서는 include 되는 JSP 페이지가 원래부터 페이지 인코딩 정보 등을 포함한 완전한 JSP 형태를 갖추고 있어야만 한다.

## 참고자료

- [Tomcat/JSP와 한글](https://okky.kr/articles/57865)