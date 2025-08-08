---
  title: 이중등록(Double Submit) 방지
  linkTitle: 이중등록(Double Submit) 방지
  description: 새로고침 등의 중복 request 호출 시 등록 처리 등에 대한 이중 등록을 방지하는 기능을 제공한다.
  url: /common-component/elementary-technology/doublesubmit/
  menu:
    depth:
      name: doublesubmit
      weight: 1
      parent: "new-components-v3.2"
      identifier: "doublesubmit"
---



# 요소기술 - 이중등록(Double Submit) 방지

## 개요

 새로고침 등의 중복 request 호출 시 등록 처리 등에 대한 이중 등록을 방지하는 기능을 제공한다.

## 설명

 세션을 통해 고유한 token을 보관하고 해당 token을 파라미터와 비교함으로서 중복 처리를 방지한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | egovframework.com.cmm.util.EgovDoubleSubmitHelper.java | 중복 방지 처리 관련 유틸리티 |  |
| TagSupport | egovframework.com.cmm.taglibs.DoubleSubmitTag.java | Tag class |  |
| tld | /WEB-INF/META-INF/double-submit.tld | tld(tag library description) 파일 |  |

## 환경설정

 **해당없음**

## 사용방법

 우선 등록화면 및 수정화면의 JSP에 다음과 같은 taglib를 적용한다.

```xml
<%@ taglib prefix="double-submit" uri="http://www.egovframe.go.kr/tags/double-submit/jsp" %>
...
 
<form ...>
    <double-submit:preventer/>
</form>
```

 이렇게 되면 세션에 고유 UUID 정보를 생성한 후에 파라미터로 해당 UUID 값을 기록한다.

 다음으로 Controller의 각 메소드에 실제 Service를 호출하는 부분을 다음과 같이 변경한다.

* 변경 전

```javascript
if (isAuthenticated) {
    notification.setFrstRegisterId(user.getUniqId());
 
    notificationService.insertNotificationInf(notification);
 
}
```

* 변경 후

```javascript
if (isAuthenticated) {
    notification.setFrstRegisterId(user.getUniqId());
 
    if (EgovDoubleSubmitHelper.checkAndSaveToken()) {  
        notificationService.insertNotificationInf(notification);
    }
}
```

 EgovDoubleSubmitHelper.checkAndSaveToken() 메소드에서 내부적으로 현재 기록된 세션상의 UUID와 파라미터의 UUID 값이 같은지 비교 후, 동일한 경우 새로운 UUID를 세션 상에 기록한 후 return true로 처리된다. 새로운 UUID가 세션에 변경되었기 때문에 동일한 request가 재 호출시 세션의 UUID와 이전 파라미터의 UUID 값이 다르기 때문에 return false로 처리되어 실제 등록 처리 등을 생략할 수 있다.

## 사용방법 (여러 화면으로 접근되는 경우)

 위의 방식은 세션을 사용하기 때문에 하나의 웹 시스템을 여러 브라우저로 동시에 사용하는 경우 동일한 세션 ID로 인하여 서로 간섭될 수 있다.

 이 경우 다음과 같은 방식으로 token key를 지정함으로써 간섭을 회피할 수 있다. (동일한 업무를 접근하는 경우는 원칙적으로 회피 불가)

```xml
<%@ taglib prefix="double-submit" uri="http://www.egovframe.go.kr/tags/double-submit/jsp" %>
...
 
<form ...>
    <double-submit:preventer tokenKey="someKey"/>
</form>
```

```javascript
if (isAuthenticated) {
    notification.setFrstRegisterId(user.getUniqId());
 
    if (EgovDoubleSubmitHelper.checkAndSaveToken("someKey")) {  
        notificationService.insertNotificationInf(notification);
    }
}
```

## 참고자료

 **해당없음**