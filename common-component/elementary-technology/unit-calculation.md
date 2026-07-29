---
title: "단위계산"
linkTitle: "단위계산"
description: "단위계산"
url: /common-component/elementary-technology/formatter-util/unit-calculation/
menu:
  depth:
    name: "단위계산"
    weight: 13
    parent: "formatter-util"
---

## 개요

단위계산은 제곱미터와 평 간의 환산을 비롯하여 넓이, 길이, 무게, 부피 등의 단위를 서로 환산하는 기능을 제공한다.

## 설명

해당 컴포넌트는 다음과 같이 다양한 단위의 환산 기능을 제공한다.

* **길이**: 길이를 다른 길이 단위로 환산하는 기능을 제공한다.
* **부피**: 부피를 다른 부피 단위로 환산하는 기능을 제공한다.
* **넓이**: 넓이를 다른 넓이 단위로 환산하는 기능을 제공한다.
* **무게**: 무게를 다른 무게 단위로 환산하는 기능을 제공한다.

### 관련 소스

| 유형 | 대상 소스명 | 비고 |
| --- | --- | --- |
| Class | `egovframework.com.utl.fda.ucc.service.EgovUnitCalcUtil.java` | 단위계산 기능을 제공하는 Java 클래스 |

### 클래스 다이어그램

![단위계산 클래스 다이어그램](./images/unit-calculation-class-diagram.jpg)

## 관련 화면 및 수행 매뉴얼

### 단위계산 환산

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 단위계산 | `/EgovPageLink.do?link=cmm/utl/EgovUnitCalc` | `moveToPage` | |

넓이, 길이, 무게, 부피 탭에서 입력 단위를 입력한 후 환산할 단위를 선택하여 변환을 수행한다.

![단위계산 화면](./images/unit-calculation-screen.jpg)

* **변환**: 입력한 단위를 선택한 환산 단위로 변환한다.
