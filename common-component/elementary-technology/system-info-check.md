---
title: "시스템정보조회"
linkTitle: "시스템정보조회"
description: "시스템정보조회"
url: /common-component/elementary-technology/system/system-info-check/
menu:
  depth:
    name: "시스템정보조회"
    weight: 71
    parent: "system"
---

## 개요

운영 체제 수준의 시스템 정보 및 Java 가상 머신(JVM)의 시스템 프로퍼티 정보를 읽어와 시스템 환경 구성을 파악하는 기능을 제공한다.

## 주요 기능

* **OS 시스템 정보**: OS 이름, 버전, 아키텍처 및 시스템에 등록된 환경 변수 등을 확인한다.
* **Java 환경 정보**: 현재 구동 중인 JVM의 벤더, 버전 및 기본 파일 인코딩 등을 조회한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getSystemProperty(String sysProp)` | Java의 System.getProperty()에 해당하는 시스템 정보를 조회하여 반환한다. |

```java
import egovframework.com.utl.sys.srm.service.EgovSystemNetwork; // 혹은 관련 클래스

public class SystemInfoCheckExample {
    public void getSysInfo() {
        // OS 이름 및 Java 버전 확인
        String osName = System.getProperty("os.name");
        String javaVersion = System.getProperty("java.version");
        
        System.out.println("OS Name: " + osName);
        System.out.println("Java Version: " + javaVersion);
    }
}
```
