---
  title: HTTPS UrlRewrite filter
  linkTitle: HTTPS UrlRewrite filter
  description: "서버내의 특정 URL의 경우 HTTP로 호출 되더라도 HTTPS로 전환 하여 Redirect 하고, 그 외의 URL의 경우는 HTTP로 연결한다."
  url: /common-component/elementary-technology/urlrewrite/
  menu:
    depth:
      name: HTTPS UrlRewrite filter
      weight: 6
      parent: "new-components-v3.2"
      identifier: "urlrewrite"
---



# 요소기술 – HTTPS UrlRewrite filter

## 개요

 서버내의 특정 URL의 경우 HTTP로 호출 되더라도 HTTPS로 전환 하여 Redirect 하고, 그 외의 URL의 경우는 HTTP로 연결한다.

## 설명

 Servlet Filter 기능을 이용하여 특정 서버에 요청 된 URL 들을 필터링 하여,

 특정 URL의 경우에는 HTTP로 요청이 들어 오더라도 HTTPS로 연결하며, 그 이외의 URL은 HTTP로 연결한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| filter | egovframework.com.cmm.util.EgovUrlRewriteFilter.java | HTTPS Redirect filter |  |

## 환경설정

 **해당없음**

## 사용방법

 web.xml 파일에 다음과 같은 filter를 설정한다.

```xml
<filter>
	<filter-name>UrlRewriteFilter</filter-name>
	<filter-class>egovframework.com.cmm.util.EgovUrlRewriteFilter</filter-class>
	<init-param>
		<param-name>targetURI</param-name>
		<param-value>/sample1/, /sample/</param-value>
	</init-param>	
	<init-param>		
		<param-name>httpPort</param-name>
		<param-value>8080</param-value>
	</init-param>
	<init-param>		
		<param-name>httpsPort</param-name>
		<param-value>8181</param-value>
	</init-param>
</filter>
<filter-mapping>
	<filter-name>UrlRewriteFilter</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```

 UrlRewrite filter 의 경우 Servlet Filter 방식으로 구현 된 특정 URL에 대하여 HTTPS로 재 설정 해 주는 기능이다.

 위와 같이 설정하면, 서버에 요청 된 URL의 형태와 param-name이 targetURI로 정의 된 AntPattern을 AntPathMatcher 방식으로 비교하여,

 요청된 URL이 해당 패턴에 해당될 경우 HTTPS 방식으로 전환하며, 그 이외의 요청에 대해서는 HTTPS로 요청이 들어 오더라도 HTTP로 전환하여 서버로 전송한다.

 추가로 HTTP 및 HTTPS 포트 지정을 위하여 &lt;param-name&gt;의 값 중 httpPort 및 httpsPort 를 정의할 수 있다.

 targetURI를 지정하는 방법은 param-name이 targetURI로 지정 된 param-value에 전환 할 URI 패턴을 입력하면 되고, ”,” 구분자를 통해 중복 등록이 가능하다.  
(예시) &lt;param-value&gt;/sample1/, /sample/, /index.do&lt;/param-value&gt; )

## 참고자료

 **해당없음**