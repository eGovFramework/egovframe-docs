---
  title: 세션처리
  linkTitle: 세션처리
  description: "세션 처리와 관련된 다양한 공통기능을 제공한다."
  url: /common-component/elementary-technology/handling_session/
  menu:
    depth:
      name: 세션처리
      weight: 1
      parent: "cookie-session"
      identifier: "handling_session"
---



# 요소기술 - 세션처리

## 개요

 세션 처리와 관련된 다양한 공통기능을 제공한다.

## 설명

 세션에 객체 정보 저장, 취득, 제거의 기능을 갖으며 HttpServletRequest 객체의 HttpSession 정보를 사용하여 처리된다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.cas.service.EgovSessionCookieUtil.java | 세션 처리 관련 유틸리티 |  |
| Controller | egovframework.com.utl.fcc.web.EgovComUtlTestController.java | 테스트용 controller |  |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovSession.jsp | 테스트 페이지 |  |

##### 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| void | setSessionAttribute(HttpServletRequest request, String key, String value) | 세션 정보 생성 | HttpSession에 주어진 키 값으로 세션 정보를 생성하는 기능 |
| void | setSessionAttribute(HttpServletRequest request, String key, Object obj) | 세션 객체 생성 | HttpSession에 주어진 키 값으로 세션 객체를 생성하는 기능 |
| Object | getSessionAttribute(HttpServletRequest request, String key) | 세션 객체 취득 | HttpSession에 존재하는 주어진 키 값에 해당하는 세션 객체를 얻어오는 기능 |
| String | getSessionValues(HttpServletRequest request) | 세션 객체 리스트 취득 | HttpSession 객체내의 모든 값을 호출하는 기능 |
| void | removeSessionAttribute(HttpServletRequest request, String key) | 세션 객체 삭제 | HttpSession에 존재하는 세션을 주어진 키 값으로 삭제하는 기능 |

##### Input

- request : JSP 또는 Servlet의 request 객체
- key : 세션에 사용 키값으로 null이 아닌 문자열 사용 (예, “UserId”)
- value, obj : 세션에 해당 key 값으로 저장될 객체로 null 가능 (예, “KILDONG”)
- Validation 체크: [요소기술 Validation 체크](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EC%9A%94%EC%86%8C%EA%B8%B0%EC%88%A0_validation_%EC%B2%B4%ED%81%AC)

##### Output

- Object, String : 해당 key로 저정된 객체

## 환경설정

 **해당없음**

## 사용방법

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

- 쿠키처리 참조: [쿠키처리](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EC%BF%A0%ED%82%A4%EC%B2%98%EB%A6%AC)