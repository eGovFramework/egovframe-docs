---
title: "HTTP서비스모니터링"
linkTitle: "HTTP서비스모니터링"
description: "HTTP서비스모니터링"
url: /common-component/elementary-technology/system/http-service-monitoring/
menu:
  depth:
    name: "HTTP서비스모니터링"
    weight: 49
    parent: "system"
---

## 개요

특정 HTTP(웹) 서비스의 정상 동작 여부를 확인하기 위해 주기적으로 서비스 호출을 수행하고 응답 상태 코드를 확인하는 기능을 제공한다.

## 주요 기능

* **서비스 가용성 점검**: 대상 URL로 HTTP 요청을 전송하여 정상적인 HTTP 응답(200 OK 등)이 오는지 확인한다.
* **에러 식별**: 서비스 불가(503), 페이지 없음(404) 등의 에러 상태 코드를 반환하여 장애 상황을 감지한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `getHttpMonitorStatus(String url)` | 입력된 URL의 HTTP 서비스 상태를 점검하여 정상 동작 여부를 반환한다. |

```java
import egovframework.com.utl.sys.htm.service.EgovHttpMonitorUtil;

public class HttpServiceMonitoringExample {
    public void monitorHttpService() throws Exception {
        String targetUrl = "http://www.egovframe.go.kr";
        
        // HTTP 서비스 모니터링 수행
        boolean isUp = EgovHttpMonitorUtil.getHttpMonitorStatus(targetUrl);
        
        if (isUp) {
            System.out.println("HTTP Service is UP and running.");
        } else {
            System.out.println("HTTP Service is DOWN.");
        }
    }
}
```
