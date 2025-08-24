---
  title: 쿠키처리
  linkTitle: 쿠키처리
  description: "쿠키 처리와 관련된 다양한 공통기능을 제공한다."
  url: /common-component/elementary-technology/handling_cookie/
  menu:
    depth:
      name: 쿠키처리
      weight: 2
      parent: "cookie-session"
      identifier: "handling_cookie"
---



# 요소기술 - 쿠키처리

## 개요

 쿠키 처리와 관련된 다양한 공통기능을 제공한다.

## 설명

 쿠키에 객체 정보 저장, 취득, 제거의 기능으로 구성되어 있다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.cas.service.EgovSessionCookieUtil.java | 세션/쿠키 처리 관련 유틸리티 |  |
| Controller | egovframework.com.cmm.web.EgovComUtlController.java | 테스트용 controller |  |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovCookieProcess.jsp | 쿠키처리 테스트 페이지 |  |

##### 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| void | setCookie(HttpServletResponse response, String cookieNm, String cookieVal, int minute) | 쿠키 정보 생성 | 입력받은 분만큼 쿠키를 유지되도록 세팅 |
| String | getCookie(HttpServletRequest request, String cookieNm) | 쿠키정보 취득 | 쿠키값을 읽어들인다 |
| void | setCookie(HttpServletResponse response, String cookieNm) | 쿠키정보 삭제 | 쿠키의 유효시간을 0으로 설정 |

##### 관련테이블

 **N/A**

## 환경설정

 **해당없음**

## 사용방법

```java
import egovframework.com.utl.cas.service.EgovSessionCookieUtil;
...
 
// 쿠키정보 생성
String cookieNm = safeGetParameter(request,"NAME"); 
String cookieVal = safeGetParameter(request,"김기수"); 
 
EgovSessionCookieUtil.setCookie(response, cookieNm, cookieVal); 
 
// 쿠키정보 얻기
String cookieNm = safeGetParameter(request,"NAME"); 
String	resultStr = EgovSessionCookieUtil.getCookie(request, cookieNm); 
 
// 쿠키정보 삭제
String cookieNm = safeGetParameter(request,"NAME");  
EgovSessionCookieUtil.setCookie(response, cookieNm); 
 
 
 
// safeGetParameter : null 처리 및 보안 문제 처리 등을 포함 (example)
 
String safeGetParameter(HttpServletRequest request, String name) {
        String value = request.getParameter(name);
        if (value == null) {
            value = "";
        }
        return value.replaceAll("r", "").replaceAll("n", "");
}
```

## 참고자료
- 세션처리 참조: [세션처리](https://egovframework.github.io/egovframe-docs/common-component/elementary-technology/handling_session/)
