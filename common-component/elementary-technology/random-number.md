---
title: "랜덤숫자생성"
linkTitle: "랜덤숫자생성"
description: "랜덤숫자생성"
url: /common-component/elementary-technology/system/random-number/
menu:
  depth:
    name: "랜덤숫자생성"
    weight: 61
    parent: "system"
---

## 개요

특정 범위 내에서 난수(Random Number)를 생성하거나, 지정된 길이만큼의 무작위 숫자 문자열을 생성하는 기능을 제공한다.

## 주요 기능

* **난수 생성**: 최소값과 최대값 사이의 임의의 정수를 추출한다.
* **보안 난수 적용**: 보안 수준이 높은 난수 생성기(SecureRandom 등)를 활용하여 예측할 수 없는 숫자를 발생시킨다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `int` | `getRandomNumber(int min, int max)` | 지정된 범위(최소값~최대값) 사이의 난수를 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil; // 또는 연관 유틸리티

public class RandomNumberExample {
    public void generateRandomNumber() {
        // 1부터 100 사이의 무작위 정수 생성
        // (설명을 위한 예시이며 실제 메서드명과 파라미터는 유틸리티 클래스 구현에 따라 다를 수 있습니다.)
        int randomNum = (int)(Math.random() * 100) + 1;
        System.out.println("Generated Random Number: " + randomNum);
    }
}
```
