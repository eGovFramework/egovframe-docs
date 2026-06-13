---
title: "메시지 처리"
linkTitle: "메시지 처리"
description: "메시지 처리"
url: /common-component/elementary-technology/message-process/
menu:
  depth:
    weight: 3
    parent: "elementary-technology"
    identifier: "message-process"
---

## 개요

애플리케이션 내에서 사용하는 정보(Info), 경고(Warn), 에러(Error), 확인(Confirm) 메시지를 관리하고 취득하는
유틸리티 공통기능을 제공한다. Property 파일을 통해 각 유형별 메시지 정보를 처리한다.

## 설명

메시지는 성격에 따라 4가지(정보, 경고, 에러, 확인)로 구분되며, 별도의 Property 파일을 통해 메시지 내용을 관리한다.

### 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.cas.service.EgovMessageUtil.java` | 메시지 처리 관련 유틸리티 | |
| Controller | `egovframework.com.utl.fcc.web.EgovComUtlTestController.java` | 테스트용 Controller | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovMessage.jsp` | 테스트 페이지 | |

### 메소드

`EgovMessageUtil` 클래스에서 다음과 같은 메소드를 제공한다.

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| `String` | `getInfoMsg(String key)` | 정보 메시지 취득 | 메시지 키에 해당하는 정보 메시지를 얻는 기능 |
| `String` | `getInfoMsg(String key, String[] params)` | 정보 파라미터 취득 | 메시지 키에 해당하는 정보 메시지에 파라미터 값을 대치하여 얻는 기능 |
| `String` | `getWarnMsg(String key)` | 경고 메시지 취득 | 메시지 키에 해당하는 경고 메시지를 얻는 기능 |
| `String` | `getWarnMsg(String key, String[] params)` | 경고 파라미터 취득 | 메시지 키에 해당하는 경고 메시지에 파라미터 값을 대치하여 얻는 기능 |
| `String` | `getErrMsg(String key)` | 에러 메시지 취득 | 메시지 키에 해당하는 에러 메시지를 얻는 기능 |
| `String` | `getErrMsg(String key, String[] params)` | 에러 파라미터 취득 | 메시지 키에 해당하는 에러 메시지에 파라미터 값을 대치하여 얻는 기능 |
| `String` | `getConfirmMsg(String key)` | 확인 메시지 취득 | 메시지 키에 해당하는 확인 메시지를 얻는 기능 |
| `String` | `getConfirmMsg(String key, String[] params)` | 확인 파라미터 취득 | 메시지 키에 해당하는 확인 메시지에 파라미터 값을 대치하여 얻는 기능 |

#### Input

- `key`: 속성 파일에 기록된 key 정보
- `params`: 대치될 문자열 배열 정보
- Validation 체크: 요소기술 Validation 체크

#### Output

- `String`: 해당 key로 지정된 속성 정보. 해당 속성이 없으면 `null`을 리턴한다.

## 환경설정

메시지 처리를 위해서는 **User home** 디렉터리 하위의 `egovProps/conf/` 경로에
각 유형별 Property 파일이 정의되어 있어야 한다. 메시지 정의는 일반적인 Property 파일 정의 방식과 동일하다.

- `infomessage.properties` (정보 메시지)
- `warnmessage.properties` (경고 메시지)
- `errormessage.properties` (에러 메시지)
- `confirmmessage.properties` (확인 메시지)

> **참고**: User home 디렉터리는 `System.getProperty("user.home")`를 통해 얻는 정보이다.
> Windows 계열 운영체제는 보통 `C:\Users\사용자계정`이고, Unix/Linux 계열은 `/home/사용자계정`이 된다.

## 사용방법

각 `.properties` 파일에 다음과 같은 메시지가 정의되어 있다고 가정한다.

```properties
# infomessage.properties
test.message = info message
param.message = info message : {0} = {1}

# warnmessage.properties
test.message = warn message
param.message = warn message : {0} = {1}
```

Java 소스코드에서 `EgovMessageUtil` 클래스를 이용하여 메시지를 취득한다.

```java
import egovframework.com.utl.cas.service.EgovMessageUtil;

// ...

String message = null;

// 1. 일반 메시지 취득
message = EgovMessageUtil.getInfoMsg("test.message");
// message = EgovMessageUtil.getWarnMsg("test.message");
// message = EgovMessageUtil.getErrMsg("test.message");
// message = EgovMessageUtil.getConfirmMsg("test.message");

// 2. 파라미터 처리 메시지 취득 : String 배열의 값이 각각 {0}, {1}로 대치됨
message = EgovMessageUtil.getInfoMsg("param.message", new String[] {"정보", "해당되는 기대값이 없습니다."});
```
