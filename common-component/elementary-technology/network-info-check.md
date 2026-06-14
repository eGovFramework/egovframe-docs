---
title: "네트워크정보조회"
linkTitle: "네트워크정보조회"
description: "네트워크정보조회"
url: /common-component/elementary-technology/system/network-info-check/
menu:
  depth:
    name: "네트워크정보조회"
    weight: 53
    parent: "system"
---

## 개요

현재 서버나 시스템이 연결되어 있는 네트워크 인터페이스의 다양한 속성 및 주소 정보를 조회하여 시스템 환경 구성이나 모니터링에 활용할 수 있도록 지원하는 기능이다.

## 주요 기능

* **IP 주소 확인**: 로컬 머신에 할당된 IP 주소(IPv4 등)를 조회한다.
* **MAC 주소 조회**: 물리적 네트워크 카드의 고유 식별자인 MAC 주소를 확인한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getMyIPaddress()` | 현재 시스템의 IP 주소를 문자열로 반환한다. |
| `String` | `getMyMACAddress()` | 현재 시스템의 MAC 주소를 문자열로 반환한다. |

```java
import egovframework.com.utl.sys.nwg.service.EgovNetworkState;

public class NetworkInfoCheckExample {
    public void getNetworkInfo() throws Exception {
        // IP 주소 확인
        String myIp = EgovNetworkState.getMyIPaddress();
        System.out.println("System IP: " + myIp);
        
        // MAC 주소 확인
        String myMac = EgovNetworkState.getMyMACAddress();
        System.out.println("System MAC: " + myMac);
    }
}
```
