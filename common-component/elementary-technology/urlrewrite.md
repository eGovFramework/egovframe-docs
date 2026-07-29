---
  title: HTTPS UrlRewrite filter
  linkTitle: HTTPS UrlRewrite filter
  description: "서버내의 특정 URL의 경우 HTTP로 호출 되더라도 HTTPS로 전환 하여 Redirect 하고, 그 외의 URL의 경우는 HTTP로 연결한다."
  url: /common-component/elementary-technology/new-components-v3.2/urlrewrite/
  menu:
    depth:
      name: HTTPS UrlRewrite filter
      weight: 6
      parent: "new-components-v3.2"
      identifier: "urlrewrite"
---



# 요소기술 – HTTPS UrlRewrite filter

## 개요

 서버 내 특정 URL에 대해 HTTP 요청이 들어오더라도 HTTPS로 리다이렉트하고, 그 외의 URL은 HTTP로 연결하는 기능을 제공한다.

## 설명

Servlet Filter를 이용하여 서버로 요청되는 URL을 필터링한다.

지정한 URL 패턴에 대해서는 HTTP 요청을 HTTPS로 전환하고, 그 외의 URL은 HTTP로 연결한다.

### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Filter | egovframework.com.cmm.util.EgovUrlRewriteFilter.java | HTTPS Redirect filter |  |

## 환경설정

 **해당없음**

## 사용방법

 web.xml 파일에 다음과 같은 Filter를 설정한다.

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

 UrlRewrite Filter는 Servlet Filter 방식으로 구현되어 있으며, 지정한 URL 패턴에 대해 HTTPS로 리다이렉트하는 기능을 제공한다.

 위와 같이 설정하면 요청된 URL을 `targetURI`에 정의한 Ant 패턴과 `AntPathMatcher` 방식으로 비교한다.

 요청된 URL이 해당 패턴과 일치하면 HTTPS로 전환하며, 그 외의 요청은 HTTP로 처리한다.

 HTTP 및 HTTPS 포트는 `httpPort`와 `httpsPort` 파라미터로 지정할 수 있다.

`targetURI`의 `param-value`에 HTTPS로 전환할 URI 패턴을 입력하며, 쉼표(`,`)를 사용하여 여러 패턴을 등록할 수 있다. 
(예시) &lt;param-value&gt;/sample1/, /sample/, /index.do&lt;/param-value&gt; )

## 참고자료

별도의 환경설정은 필요하지 않다.
