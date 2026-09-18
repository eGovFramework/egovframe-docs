---
title: "숫자유효성체크"
linkTitle: "숫자유효성체크"
description: "숫자유효성체크"
url: /common-component/elementary-technology/formatter-util/number-validation/
menu:
  depth:
    name: "숫자유효성체크"
    weight: 16
    parent: "formatter-util"
---

# 숫자 유효성체크

## 개요

숫자 유효성체크는 문자열의 각 문자가 ASCII 숫자 `0`부터 `9`까지로 구성되어 있는지 검사하는 요소기술이다.
`EgovNumberUtil`의 정적 메서드를 호출하여 사용하며, 별도의 환경설정은 필요하지 않다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getNumberValidCheck(String checkStr)` | `Boolean` | 문자열이 ASCII 숫자로만 구성되어 있는지 검사한다. |

### 입력값과 반환값

- `checkStr`: 검사할 `String` 타입의 문자열이다. 정수 타입의 값을 전달하는 메서드가 아니다.
- 반환값: 숫자 문자만 포함하면 `true`, 다른 문자가 포함되면 `false`를 반환한다.
- `null`과 빈 문자열의 처리 결과는 적용한 소스 버전에 따라 다르므로 아래의 버전별 동작을 확인한다.

## 입력값별 동작

| 입력값 | 반환값 | 설명 |
| --- | --- | --- |
| `"12345"` | `true` | 모든 문자가 ASCII 숫자이다. |
| `"0"`, `"00123"` | `true` | 0과 앞자리의 0을 허용한다. |
| `"-123"`, `"+123"` | `false` | 부호는 숫자 문자에 포함되지 않는다. |
| `"12.3"`, `"1e3"` | `false` | 소수점과 지수 표기의 문자를 허용하지 않는다. |
| `"1,000"` | `false` | 자릿수 구분 쉼표를 허용하지 않는다. |
| `" 123"`, `"123 "`, `"1 23"` | `false` | 공백을 자동으로 제거하지 않는다. |
| `"１２３"` | `false` | 전각 숫자는 ASCII 숫자가 아니다. |
| `"2147483648"` | `true` | 숫자의 크기나 `int` 범위는 검사하지 않는다. |

### 버전별 null과 빈 문자열 처리

공통컴포넌트 `v5.0.0` 소스와 `a0f3963` 커밋의 소스는 다음과 같이 동작한다.
수정 커밋의 적용 여부는 프로젝트에서 사용하는 `EgovNumberUtil` 소스로 확인한다.

| 입력값 | `v5.0.0` | `a0f3963` 수정이 반영된 소스 |
| --- | --- | --- |
| `null` | `NullPointerException` 발생 | `false` 반환 |
| `""` | `true` 반환 | `false` 반환 |

`v5.0.0`은 문자열 길이를 바로 조회하므로 `null`에서 예외가 발생한다.
빈 문자열은 문자 검사 반복문을 실행하지 않고 `true`를 반환한다.
`a0f3963` 커밋에서는 문자 검사 전에 `null`과 빈 문자열을 거부하는 조건이 추가되었다.

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;

boolean digits = EgovNumberUtil.getNumberValidCheck("12345"); // true
boolean decimal = EgovNumberUtil.getNumberValidCheck("12.3"); // false
boolean negative = EgovNumberUtil.getNumberValidCheck("-123"); // false
```

### 필수 입력값 검사

숫자로만 구성된 필수 입력값을 검사하려면 `null`과 빈 문자열을 먼저 확인한다.
다음 예제는 `v5.0.0`과 수정된 소스 모두에서 사용할 수 있다.

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;

public class NumberValidationExample {
    public static boolean isRequiredDigits(String value) {
        return value != null
                && !value.isEmpty()
                && EgovNumberUtil.getNumberValidCheck(value);
    }

    public static void main(String[] args) {
        System.out.println(isRequiredDigits("00123")); // true
        System.out.println(isRequiredDigits("12.3"));  // false
        System.out.println(isRequiredDigits(" 123"));  // false
        System.out.println(isRequiredDigits(""));      // false
        System.out.println(isRequiredDigits(null));    // false
    }
}
```

`&&`는 왼쪽 조건이 `false`이면 오른쪽 조건을 평가하지 않으므로 `null`을 메서드에 전달하지 않는다.

## 사용 시 주의사항

- 이 메서드는 문자열의 문자 구성을 검사한다. 음수, 소수 등 모든 수치 표현을 판별하는 용도로 사용하지 않는다.
- 앞뒤 공백을 허용하려면 업무 규칙에 따라 호출 전에 공백을 제거한다. 원본 입력을 엄격하게 검사해야 하는 경우에는 제거하지 않는다.
- 반환값이 `true`여도 숫자 타입으로 변환할 수 있다는 의미는 아니다.
  예를 들어 `"2147483648"`은 검사를 통과하지만 `Integer.parseInt`로 변환하면 `NumberFormatException`이 발생한다.
  숫자 변환 단계에서 대상 타입의 범위와 예외를 별도로 처리한다.

## 참고자료

- [공식 포털 숫자유효성체크 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:숫자유효성체크)
- [공통컴포넌트 v5.0.0 EgovNumberUtil 소스](https://github.com/eGovFramework/egovframe-common-components/blob/v5.0.0/src/main/java/egovframework/com/utl/fcc/service/EgovNumberUtil.java)
- [null과 빈 문자열 검사 수정 커밋](https://github.com/eGovFramework/egovframe-common-components/commit/a0f39632ea410c4951efd41846d31d9d8c39d88b)
