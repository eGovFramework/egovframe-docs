---
title: "네트워크상태조회"
linkTitle: "네트워크상태조회"
description: "네트워크상태조회"
url: /common-component/elementary-technology/system/network-status-check/
menu:
  depth:
    name: "네트워크상태조회"
    weight: 54
    parent: "system"
---

## 개요

지정된 원격 서버 또는 IP 주소와의 네트워크 통신 가능 여부를 확인하기 위해 Ping 테스트나 포트 상태 확인 등을 수행하는 기능이다.

## 주요 기능

* **Ping 테스트 수행**: 대상 호스트로 ICMP 에코 요청을 보내 응답이 오는지 확인하여 네트워크 접근성을 점검한다.
* **포트 스캔 기능**: 특정 IP의 특정 포트가 열려있는지 소켓 연결을 시도하여 서비스 가용성을 판별한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `getPingResult(String ip)` | 대상 IP로 Ping 명령을 실행하여 정상 응답 여부를 반환한다. |
| `boolean` | `checkPortState(String ip, int port)` | 대상 IP의 특정 포트가 연결 가능한지 확인한다. |

```java
import egovframework.com.utl.sys.nwg.service.EgovNetworkState;

public class NetworkStatusCheckExample {
    public void checkNetwork() throws Exception {
        String targetIp = "192.168.0.1";
        
        // Ping 결과 확인
        boolean isPingOk = EgovNetworkState.getPingResult(targetIp);
        System.out.println("Ping to " + targetIp + " : " + (isPingOk ? "Success" : "Fail"));
        
        // 특정 포트(예: 80) 상태 확인
        boolean isPortOpen = EgovNetworkState.checkPortState(targetIp, 80);
        System.out.println("Port 80 Open : " + isPortOpen);
    }
}
```
