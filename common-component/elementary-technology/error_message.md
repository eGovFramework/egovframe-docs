---
  title: 에러메시지
  linkTitle: 에러메시지
  description: "에러에 해당되는 메시지 정보를 확인할 수 있는 공통기능을 제공한다."
  url: /common-component/elementary-technology/error_message/
  menu:
    depth:
      name: 에러메시지
      weight: 2
      parent: "message-process"
      identifier: "error_message"
---



# 요소기술 - 에러메시지

## 개요

 에러에 해당되는 메시지 정보를 확인할 수 있는 공통기능을 제공한다.

## 설명

 에러(error)로 구분된 메시지 정보를 property 처리를 통해 처리된다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.cas.service.EgovMessageUtil.java | 메시지 처리 관련 유틸리티 |  |
| Controller | egovframework.com.utl.fcc.web.EgovComUtlTestController.java | 테스트용 controller |  |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovMessage.jsp | 테스트 페이지 |  |

##### 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | getErrorMsg(String key) | 에러 메시지 취득 | 메시지키에 해당 에러메시지를 얻는 기능 |
| String | getErrorMsg(String key, String[] params) | 에러 메시지 파라미터 취득 | 메시지키에 해당 에러메시지를 해당되는 파라미터 값을 대치하여 얻는 기능 |

##### Input

- key : 속성 파일에 기록된 key 정보
- params : 대치될 문자열 배열 정보
- Validation 체크: [요소기술 Validation 체크](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EC%9A%94%EC%86%8C%EA%B8%B0%EC%88%A0_validation_%EC%B2%B4%ED%81%AC)

##### Output

- String : 해당 key 지정된 속성 정보로 해당 속성이 없으면 null 리턴

## 환경설정

 메시지 처리를 위해서는 ***User home***  디렉토리밑에 egovProps/conf/errormessage.properties 파일에 메시지가 정의되어 있어야 한다. 해당 메시지 정의는 일반 property 정의 방식과 같다.

- User home 디렉토리 : System.getProperty(“user.home”)를 통해 얻는 정보로 Windows 계열의 OS는 보통 “C:\Documents and Settings\사용자계정“이고, Unix계정의 경우는 ”/home/사용자계정“이 된다.

## 사용방법

 우선 errormessage.properties 파일에 다음과 같은 메시지가 정의되어 있다고 가정한다.

```properties
test.message = error message
param.message = error message : {0} = {1}

```

```java
import egovframework.com.utl.cas.service.EgovMessageUtil;
 
...
String message = null;
 
// 일반 경고 메시지 취득
message = EgovMessageUtil.getErrorMsg("test.message");
 
// 파라미터 처리 경고 메시지 취득 : String 배열의 값이 각각 {0}, {1}로 대치됨
message = EgovMessageUtil.getErrorMsg("param.message", new String[2] {"오류", "해당되는 기대값이 없습니다."});
```

## 참고자료

- 경고메시지 참조: [경고메시지](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EA%B2%BD%EA%B3%A0%EB%A9%94%EC%8B%9C%EC%A7%80)
- 정보메시지 참조: [정보메시지](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EC%A0%95%EB%B3%B4%EB%A9%94%EC%8B%9C%EC%A7%80)
- 확인메시지 참조: [확인메시지](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%ED%99%95%EC%9D%B8%EB%A9%94%EC%8B%9C%EC%A7%80)