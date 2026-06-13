---
title: "쿠키/세션"
linkTitle: "쿠키/세션"
description: "쿠키/세션"
url: /common-component/elementary-technology/cookie-session/
menu:
  depth:
    weight: 5
    parent: "elementary-technology"
    identifier: "cookie-session"
---

## 개요

쿠키(Cookie) 및 세션(Session) 처리와 관련된 다양한 공통기능을 제공한다.

## 설명

### 쿠키 처리

쿠키에 객체 정보를 저장, 취득, 제거하는 기능으로 구성되어 있다.

#### 쿠키 관련 소스

| 유형 | 대상소스 | 설명 |
| --- | --- | --- |
| Service | `EgovSessionCookieUtil.java` | 세션/쿠키 처리 관련 유틸리티 |
| Controller | `EgovComUtlController.java` | 테스트용 controller |
| JSP | `EgovCookieProcess.jsp` | 쿠키처리 테스트 페이지 |

#### 쿠키 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| `void` | `setCookie(response, cookieNm, cookieVal, minute)` | 쿠키 정보 생성 | 입력받은 분만큼 쿠키를 유지되도록 세팅 |
| `String` | `getCookie(request, cookieNm)` | 쿠키정보 취득 | 쿠키값을 읽어들인다 |
| `void` | `setCookie(response, cookieNm)` | 쿠키정보 삭제 | 쿠키의 유효시간을 0으로 설정 |

#### 쿠키 사용방법

```java
import egovframework.com.utl.cas.service.EgovSessionCookieUtil;
...

// 쿠키정보 생성
String cookieNm = safeGetParameter(request, "NAME"); 
String cookieVal = safeGetParameter(request, "김기수"); 

EgovSessionCookieUtil.setCookie(response, cookieNm, cookieVal); 

// 쿠키정보 얻기
String cookieNm = safeGetParameter(request, "NAME"); 
String resultStr = EgovSessionCookieUtil.getCookie(request, cookieNm); 

// 쿠키정보 삭제
String cookieNm = safeGetParameter(request, "NAME");  
EgovSessionCookieUtil.setCookie(response, cookieNm); 

// safeGetParameter : null 처리 및 보안 문제 처리 등을 포함 (example)
String safeGetParameter(HttpServletRequest request, String name) {
    String value = request.getParameter(name);
    if (value == null) {
        value = "";
    }
    return value.replaceAll("\r", "").replaceAll("\n", "");
}
```

### 세션 처리

세션에 객체 정보를 저장, 취득, 제거하는 기능을 갖으며 `HttpServletRequest` 객체의 `HttpSession` 정보를 사용하여 처리된다.

#### 세션 관련 소스

| 유형 | 대상소스 | 설명 |
| --- | --- | --- |
| Service | `EgovSessionCookieUtil.java` | 세션 처리 관련 유틸리티 |
| Controller | `EgovComUtlTestController.java` | 테스트용 controller |
| JSP | `EgovSession.jsp` | 테스트 페이지 |

#### 세션 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| `void` | `setSessionAttribute(request, key, value)` | 세션 정보 생성 | `HttpSession`에 주어진 키 값으로 세션 정보를 생성하는 기능 |
| `void` | `setSessionAttribute(request, key, obj)` | 세션 객체 생성 | `HttpSession`에 주어진 키 값으로 세션 객체를 생성하는 기능 |
| `Object` | `getSessionAttribute(request, key)` | 세션 객체 취득 | `HttpSession`에 존재하는 주어진 키 값에 해당하는 세션 객체를 얻어오는 기능 |
| `String` | `getSessionValues(request)` | 세션 객체 리스트 취득 | `HttpSession` 객체내의 모든 값을 호출하는 기능 |
| `void` | `removeSessionAttribute(request, key)` | 세션 객체 삭제 | `HttpSession`에 존재하는 세션을 주어진 키 값으로 삭제하는 기능 |

##### Input

- `request` : JSP 또는 Servlet의 request 객체
- `key` : 세션에 사용 키값으로 null이 아닌 문자열 사용 (예, "UserId")
- `value`, `obj` : 세션에 해당 key 값으로 저장될 객체로 null 가능 (예, "KILDONG")
- Validation 체크: 요소기술 Validation 체크

##### Output

- `Object`, `String` : 해당 key로 저장된 객체

#### 세션 사용방법

```java
import javax.servlet.http.HttpServletRequest;

import egovframework.com.utl.cas.service.EgovSessionCookieUtil;

...
// 세션 정보 저장
EgovSessionCookieUtil.setSessionAttribute(request, "USER_ID", "KildongHong");
EgovSessionCookieUtil.setSessionAttribute(request, "USER_NAME", "홍길동");

// 세션 정보 출력 (모든 세션 정보 표시)
logger.info("Session Infos : " + EgovSessionCookieUtil.getSessionValuesString(request));

// 특정 세션 정보 취득
String userId = (String)EgovSessionCookieUtil.getSessionAttribute("USER_ID");

// 세션 정보 삭제
EgovSessionCookieUtil.removeSessionAttribute(request, "USER_ID");
EgovSessionCookieUtil.removeSessionAttribute(request, "USER_NAME");
```

## 참고자료

- 해당없음
