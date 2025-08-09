---
  title: 중복 로그인 방지 기능
  linkTitle: 중복 로그인 방지 기능
  description: "spring security 없이 중복 로그인을 방지하기 위한 기능이다."
  url: /common-component/elementary-technology/multilogin/
  menu:
    depth:
      name: 중복 로그인 방지 기능
      weight: 7
      parent: "new-components-v3.2"
      identifier: "multilogin"
---



# 요소기술 - 중복 로그인 방지 기능

## 개요

 spring security 없이 중복 로그인을 방지하기 위한 기능이다.

## 설명

 로그인할 때 로그인 ID와 세션 ID를 Map에 저장하고, 로그아웃할 때 혹은 세션타임아웃 설정에 따라 두 정보를 Map에서 제거한다.  
이미 로그인한 상태에서 다른 브라우저를 통해 또 다른 로그인을 시도하면, Map에 등록된 이전 세션을 무효화하고 새로운 세션 ID를 Map에 등록한다.  
이전 세션 ID로는 더이상 서비스를 이용할 수 없게 되며, 가장 마지막에 로그인한 세션만 유효하다.  

 본 기능은 **HttpSessionBindingListener 인터페이스의 valueBound()와 valueUnBound() 메소드를 구현한 EgovHttpSessionBindingListener**를 통해 동작한다.  
***valueBound()*** 는 HttpSessionBindingListener 구현체가 HttpSession 객체에 setAttribute() 될 때 자동 호출되고,  
***valueUnBound()*** 는 HttpSession 객체에서 invalidate() 될 때 자동 호출된다.

 HttpSessionListener과 달리 HttpSessionBindingListener을 이용하면, 세션이 생성된 이후와 세션이 제거된 이후에 처리할 로직을 추가할 수 있다.  
EgovHttpSessionBindingListener 객체는 로그인과 로그아웃 시점에 세션에 바인딩되고 제거되면서 HttpSessionBindingEvent를 발생시키고,  
HttpSessionBindingEvent에 저장된 로그인 ID와 세션 정보를 이용하여 중복 로그인 방지 기능을 제공한다.

##### 관련소스

| 패키지 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| /egovframework/com/utl/slm/ | **EgovHttpSessionBindingListener.java** | 세션 생성 시점이 아닌 로그인 혹은 로그아웃 시점에 발생하는 SessionBindingEvent를 체크하기 위한 클래스 | HttpSessionBindingListener 구현체 |
| /egovframework/com/utl/slm/ | **EgovMultiLoginPreventor.java** | 로그인 ID와 세션 ID를 관리하고 로그인 상태를 제어하기 위한 클래스 | ConcurrentHashMap을 이용 |

## 사용방법 - 로그인/로그아웃 컨트롤러 메소드에 코드 추가

### 1. 로그인 요청을 처리하는 컨트롤러 메소드 안에 다음을 정의한다.

```java
EgovHttpSessionBindingListener listener = new EgovHttpSessionBindingListener();
request.getSession().setAttribute("사용자 로그인ID", listener);

```

 **사용자 로그인 ID를 키 값으로 현재 세션에 EgovHttpSessionBindingListener 객체를 바인딩한다.**  
이 때 EgovHttpSessionBidingListener의 valueBound() 메소드가 자동 호출되면서, 사용자 로그인 ID와 현재 세션 ID를 Map에 저장한다.  
이미 존재하는 세션 ID가 있다면 valueBound() 메소드를 통해 모두 무효화시키기 때문에, 현재 세션 ID으로만 서비스 접근이 가능하다.

```java
// 예제소스
    @RequestMapping(value="/uat/uia/actionLogin.do")
    public String actionLogin(@ModelAttribute("loginVO") LoginVO loginVO, HttpServletRequest request, ModelMap model) throws Exception {
        LoginVO resultVO = loginService.actionLogin(loginVO);
        if (resultVO != null && resultVO.getId() != null && !resultVO.getId().equals("") && loginPolicyYn) {
        	request.getSession().setAttribute("LoginVO", resultVO);
 
-->                EgovHttpSessionBindingListener listener = new EgovHttpSessionBindingListener();
-->                request.getSession().setAttribute(resultVO.getId(), listener);
 
        	return "forward:/cmm/main/mainPage.do";        	
        } else {
        	model.addAttribute("message", egovMessageSource.getMessage("fail.common.login"));
        	return "cmm/uat/uia/EgovLoginUsr";
        }
```

### 2. 로그아웃 요청을 처리하는 컨트롤러 메소드 안에 다음을 정의한다.

```java
request.getSession().invalidate();
```

 **사용자가 로그아웃 버튼을 눌렀을 때 명시적으로 세션을 무효화하도록 HttpSession의 invalidate() 메소드를 호출한다.**  
이 때 EgovHttpSessionBidingListener의 valueUnBound() 메소드가 자동 호출되면서, Map에 등록된 사용자 로그인 ID와 현재 세션 ID를 제거할 것이다.

 만약 사용자가 로그아웃 버튼을 누르지 않았더라도 세션타임아웃 설정에 의해 valueUnBound() 메소드가 자동으로 호출된다.  
또한 로그아웃 하지 않고 다른 브라우저를 통해 새로운 로그인을 시도하면,  
1번에서 설명한대로 현재 세션 ID 외에 다른 세션이 존재하는지를 확인하고, 이전에 저장된 세션 ID가 남아있다면 자동으로 그 세션을 무효화시킨다.

```java
// 예제소스
        @RequestMapping(value="/uat/uia/actionLogout.do")
	public String actionLogout(HttpServletRequest request, ModelMap model) throws Exception {
    	try {
    		RequestContextHolder.getRequestAttributes().removeAttribute("LoginVO", RequestAttributes.SCOPE_SESSION);
 
-->    		request.getSession().invalidate();
 
    	} catch (Exception e) { 
                leaveaTrace.trace("fail.common.msg", this.getClass());
	}
    	return "forward:/cmm/main/mainPage.do"; 
    }
```

## 참고자료

 **해당없음**