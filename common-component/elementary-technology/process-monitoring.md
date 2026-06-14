---
title: "프로세스모니터링"
linkTitle: "프로세스모니터링"
description: "프로세스모니터링"
url: /common-component/elementary-technology/system/process-monitoring/
menu:
  depth:
    name: "프로세스모니터링"
    weight: 58
    parent: "system"
---

## 개요

서버 운영 체제에서 실행 중인 특정 프로세스의 상태를 주기적으로 모니터링하여 프로세스의 정상 동작 여부를 확인하는 기능을 제공한다.

## 주요 기능

* **프로세스 구동 확인**: 프로세스명(또는 프로세스 아이디)을 기반으로 해당 프로세스가 현재 시스템에서 실행 중인지 여부를 점검한다.
* **장애 감지**: 등록된 프로세스가 예상치 않게 중단되었는지 파악하여 시스템 안정성 관리에 활용한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `getProcessStatus(String processNm)` | 지정된 프로세스 이름이 현재 실행 중이면 true, 아니면 false를 반환한다. |

```java
import egovframework.com.utl.sys.prm.service.EgovProcessMonitring;

public class ProcessMonitoringExample {
    public void monitorProcess() throws Exception {
        String processName = "tomcat";
        
        // 프로세스 실행 여부 확인
        boolean isRunning = EgovProcessMonitring.getProcessStatus(processName);
        
        if (isRunning) {
            System.out.println(processName + " is running normally.");
        } else {
            System.out.println(processName + " is stopped.");
        }
    }
}
```
