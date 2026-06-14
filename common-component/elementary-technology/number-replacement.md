---
title: "숫자치환"
linkTitle: "숫자치환"
description: "숫자치환"
url: /common-component/elementary-technology/formatter-util/number-replacement/
menu:
  depth:
    name: "숫자치환"
    weight: 17
    parent: "formatter-util"
---

<!-- markdownlint-disable MD025 -->
# 숫자치환
<!-- markdownlint-restore -->

## 개요

특정 숫자나 입력받은 숫자 집합 내에서 지정된 대상 숫자를 다른 숫자로 치환해 주는 기능을 제공하는 요소기술이다.

## 주요 개념

### 숫자치환 동작 방식

입력받은 숫자(`srcNumber`) 중 변환의 대상이 되는 특정 숫자(`cnvrSrcNumber`)를 찾아, 목적하는
변환 숫자(`cnvrTrgtNumber`)로 모두 치환하여 결과값을 반환한다. 내부적으로는 입력받은 숫자를
문자열로 변환한 후 치환 처리를 수행하고 다시 정수형으로 반환하는 방식으로 동작한다.

## 설명

`egovframework.com.utl.fcc.service.EgovNumberUtil` 클래스의 `getNumberCnvr` 메서드를 활용하여 숫자 변환을 수행할 수 있다.

### 1. 숫자치환 처리 구현

실제 비즈니스 로직이나 컨트롤러에서 다음과 같이 `getNumberCnvr` 메서드를 호출하여 숫자를 치환할 수 있다.

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;

// ... (생략) ...

// 원본 숫자
int srcNumber = 123453;
// 치환할 대상 숫자
int cnvrSrcNumber = 3;
// 치환될 목적 숫자
int cnvrTrgtNumber = 9;

// 결과: 129459 (123453에서 3을 찾아 9로 모두 치환)
int resultNumber = EgovNumberUtil.getNumberCnvr(srcNumber, cnvrSrcNumber, cnvrTrgtNumber);
```

### 2. 테스트 환경 제공

표준프레임워크 공통컴포넌트에서는 `EgovComUtlController.java`와
`/WEB-INF/jsp/egovframework/cmm/utl/EgovNumberReplc.jsp`를 통해 해당 기능의 동작을 웹 화면에서 직접
테스트해 볼 수 있는 예제를 제공한다. 화면에서 원본 숫자, 변환 대상 숫자, 변환할 숫자를 직접 입력하여
치환 결과를 확인할 수 있다.

> **참고**: 해당 테스트 페이지 및 컨트롤러는 기능의 정상 동작 여부를 확인하기 위해 제공되는 참조용 예제이다.
> 운영 환경에 적용할 때에는 보안상 취약점이 될 수 있으므로 삭제하거나 별도의 접근 제어 등 보안 정책을
> 적용하는 것을 권장한다.

## 참고자료

- 관련 클래스: `egovframework.com.utl.fcc.service.EgovNumberUtil`
