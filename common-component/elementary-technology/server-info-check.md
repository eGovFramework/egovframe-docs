---
title: "서버정보조회"
linkTitle: "서버정보조회"
description: "서버정보조회"
url: /common-component/elementary-technology/system/server-info-check/
menu:
  depth:
    name: "서버정보조회"
    weight: 64
    parent: "system"
---

## 개요

시스템이 구동 중인 서버의 운영 체제, 자바 가상 머신(JVM), 시스템 메모리(RAM) 등 서버의 기본 환경 및 상태 정보를 조회하는 기능을 제공한다.

## 주요 기능

* **OS 정보 확인**: 운영 체제의 이름, 버전 및 아키텍처 정보를 반환한다.
* **JVM 메모리 확인**: 현재 애플리케이션에 할당된 전체 메모리, 사용 중인 메모리, 여유 메모리 크기를 바이트 단위로 제공한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getOSInfo()` | 현재 시스템의 OS 환경(Windows, Unix, Linux 등)에 대한 정보를 문자열로 반환한다. |
| `long` | `getFreeMemory()` | 현재 JVM이 사용 가능한 여유 메모리 바이트를 반환한다. |

```java
import egovframework.com.utl.sys.srm.service.EgovServerState; // 관련 유틸리티 사용

public class ServerInfoCheckExample {
    public void checkServerInfo() throws Exception {
        // 메모리 정보 확인 예시
        long freeMemory = Runtime.getRuntime().freeMemory();
        long totalMemory = Runtime.getRuntime().totalMemory();
        
        System.out.println("Total Memory: " + totalMemory + " bytes");
        System.out.println("Free Memory: " + freeMemory + " bytes");
    }
}
```
