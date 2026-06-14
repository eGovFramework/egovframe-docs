---
title: "프로세스ID조회"
linkTitle: "프로세스ID조회"
description: "프로세스ID조회"
url: /common-component/elementary-technology/system/process-id-check/
menu:
  depth:
    name: "프로세스ID조회"
    weight: 57
    parent: "system"
---

## 개요

현재 운영 체제에서 구동 중인 Java 애플리케이션의 프로세스 아이디(PID)를 조회하는 기능을 제공한다. 프로세스 모니터링이나 특정 프로세스를 제어할 때 활용된다.

## 주요 기능

* **현재 PID 확인**: 시스템 상에서 실행 중인 현재 JVM 인스턴스의 프로세스 ID를 반환한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getProcessId()` | 현재 실행 중인 프로세스의 ID(PID)를 문자열로 반환한다. |

```java
import egovframework.com.utl.sys.prm.service.EgovProcessMonitring;

public class ProcessIdCheckExample {
    public void checkProcessId() throws Exception {
        // 현재 프로세스 ID 조회
        String pid = EgovProcessMonitring.getProcessId();
        System.out.println("Current Process ID: " + pid);
    }
}
```
