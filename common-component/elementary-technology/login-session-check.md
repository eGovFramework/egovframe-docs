---
title: "로그인세션체크"
linkTitle: "로그인세션체크"
description: "로그인세션체크"
url: /common-component/elementary-technology/system/login-session-check/
menu:
  depth:
    name: "로그인세션체크"
    weight: 51
    parent: "system"
---

## 개요

현재 시스템에 접근하는 사용자의 세션 정보가 유효한지 검증하고 인증된 사용자의 로그인 상태를 확인하는 기능을 제공한다.

## 주요 기능

* **세션 유효성 검증**: 요청된 HttpServletRequest에서 세션 존재 여부를 확인한다.
* **사용자 인증 정보 확인**: 세션 내에 저장된 로그인 인증 객체(LoginVO 등)가 존재하는지 체크한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `checkLoginSession(HttpServletRequest request)` | 현재 요청의 세션이 유효하고 로그인된 상태인지 확인한다. |

```java
import egovframework.com.utl.fcc.service.EgovLoginSessionCheckUtil;
import javax.servlet.http.HttpServletRequest;

public class LoginSessionCheckExample {
    public void verifySession(HttpServletRequest request) {
        // 로그인 세션 유효성 검사
        boolean isValid = EgovLoginSessionCheckUtil.checkLoginSession(request);
        
        if (isValid) {
            System.out.println("로그인 세션이 유효합니다.");
        } else {
            System.out.println("세션이 만료되었거나 비정상적인 접근입니다.");
        }
    }
}
```
