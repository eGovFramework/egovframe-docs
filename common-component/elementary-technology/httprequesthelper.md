---
  title: Http Request 정보 취득
  linkTitle: Http Request 정보 취득
  description: "Http Request(HttpServletRequest) 정보를 서비스 코드나 DAO 코드 상에서 취득할 수 있는 기능을 제공한다."
  url: /common-component/elementary-technology/httprequesthelper/
  menu:
    depth:
      name: httprequesthelper
      weight: 2
      parent: "new-components-v3.2"
      identifier: "httprequesthelper"
---



# 요소기술 - Http request 정보 취득

## 개요

 Http Request(HttpServletRequest) 정보를 서비스 코드나 DAO 코드 상에서 취득할 수 있는 기능을 제공한다.

## 설명

 Controller의 경우는 Http request에 대한 정보를 얻기 위해서 각 메소드에 파라미터에 HttpServerRequest를 추가하면 된다. 그러나 Service 부분이나 Repository 부분에서 Http request 정보를 얻으려면 파라미터화하여야 한다.  
HTTP Request 정보 취득을 사용하면 파미리터를 통하지 않고 Http request 정보를 얻을 수 있다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | egovframework.com.cmm.util.EgovHttpRequestHelper.java | Http Request 정보 취득 처리 관련 유틸리티 |  |

## 환경설정

 EgovHttpRequestHelper를 통해 Http Request 정보를 취득하려면 web.xml에 다음과 같은 설정이 추가되어야 한다.

```xml
  	<!-- 서비스 부분에서 HttpServletRequest 정보 얻기 -->
	<listener>
		<listener-class>org.springframework.web.context.request.RequestContextListener</listener-class>
	</listener>
```

## 사용방법

 EgovHttpRequestHelper는 다음과 같은 메소드를 제공한다.

| 메소드명 | 리턴유형 | 파라미터 | 설명 | 비고 |
| --- | --- | --- | --- | --- |
| isInHttpRequest | boolean | 없음 | 현재 Http 요청으로 처리되고 있는지를 제공 | 스케줄러 등의 같이 자체적인 Thread로 호출되는 경우는 HttpServletRequest 제공 불가 |
| getCurrentRequest | HttpServletRequest | 없음 | 현재 요청된 HttpServletRequest 제공 |  |
| getRequestIp | String | 없음 | 현재 요청된 IP 제공 |  |
| getRequestURI | String | 없음 | 현재 요청된 URI 제공 |  |
| getCurrentSession | HttpSession | 없음 | 현재 요청된 Request에 대한 Session 제공 |  |

## 참고자료

 **해당없음**