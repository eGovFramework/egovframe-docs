---
title: "유효메모리체크"
linkTitle: "유효메모리체크"
description: "유효메모리체크"
url: /common-component/elementary-technology/system/valid-memory-check/
menu:
  depth:
    name: "유효메모리체크"
    weight: 74
    parent: "system"
---

## 개요

현재 Java 애플리케이션(JVM)에 할당된 전체 메모리와 가용 메모리를 비교하여, 특정 작업(대용량 파일 처리 등)을 수행하기 위한 유효 메모리가 충분한지 사전에 검사하는 기능이다.

## 주요 기능

* **메모리 한계 검사**: 시스템 힙(Heap) 메모리 영역의 여유 공간을 바이트 단위로 확인한다.
* **OOM 방지**: 메모리 여유 공간이 부족한 상황에서 메모리를 많이 소비하는 로직의 실행을 차단하여 OutOfMemory 에러를 방지한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `checkValidMemory(long requiredMemory)` | 현재 가용 메모리가 요구되는 메모리보다 큰지 여부를 확인하여 반환한다. |

```java
import egovframework.com.utl.sys.srm.service.EgovServerState; // 관련 유틸리티

public class ValidMemoryCheckExample {
    public void processLargeData() {
        long required = 10485760; // 10MB 필요
        
        // 메모리 여유 여부 판단 로직 예시
        long freeMemory = Runtime.getRuntime().freeMemory();
        boolean isMemoryEnough = freeMemory > required;
        
        if (isMemoryEnough) {
            System.out.println("Memory is sufficient. Proceeding...");
        } else {
            System.out.println("Not enough memory. Free: " + freeMemory);
        }
    }
}
```
