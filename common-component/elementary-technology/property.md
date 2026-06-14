---
title: "프로퍼티"
linkTitle: "프로퍼티"
description: "프로퍼티"
url: /common-component/elementary-technology/system/property/
menu:
  depth:
    name: "프로퍼티"
    weight: 59
    parent: "system"
---

## 개요

시스템 운영에 필요한 환경 변수나 설정 정보가 담긴 프로퍼티(Properties) 파일의 내용을 읽어오거나 관리하는 기능을 제공한다.

## 주요 기능

* **설정값 읽기**: `globals.properties` 등의 설정 파일에 정의된 키(Key)에 해당하는 값(Value)을 가져온다.
* **환경 변수 통합 관리**: 자주 변경되는 설정값을 소스코드와 분리하여 파일 단위로 관리할 수 있도록 지원한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getProperty(String keyName)` | `globals.properties` 파일에서 지정된 키의 프로퍼티 값을 반환한다. |

```java
import egovframework.com.cmm.service.EgovProperties;

public class PropertyExample {
    public void getPropertyValue() {
        // Globals.OsType 등 정의된 프로퍼티 읽어오기
        String osType = EgovProperties.getProperty("Globals.OsType");
        String fileStorePath = EgovProperties.getProperty("Globals.fileStorePath");
        
        System.out.println("OS Type: " + osType);
        System.out.println("File Store Path: " + fileStorePath);
    }
}
```
