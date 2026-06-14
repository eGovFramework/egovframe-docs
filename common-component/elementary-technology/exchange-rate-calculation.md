---
title: "환율계산"
linkTitle: "환율계산"
description: "환율계산"
url: /common-component/elementary-technology/formatter-util/exchange-rate-calculation/
menu:
  depth:
    name: "환율계산"
    weight: 23
    parent: "formatter-util"
---

## 개요

환율계산 기능은 한국수출입은행에서 제공하는 환율 API를 활용하여 서로 다른 통화 간의 환율을 계산하는 유틸리티 기능이다.

### 주요 개념

- **한국수출입은행 환율 API**: 현재 환율 정보를 제공하는 외부 API.
- **지원 통화**: 대한민국(KRW), 미국(USD), 유럽연합(EUR), 일본(JPY), 중국(CNH) 간의 환율 계산을 지원한다.

### 설명

이 기능은 `egovframework.com.utl.fcc.service.EgovEhgtCalcUtil` 클래스 내에 구현되어 있으며, 금액과 대상 통화를 지정하여 환전된 금액을 문자열 형태로 반환받을 수 있다.

#### 환경 설정

환율계산 기능을 사용하기 위해서는 `globals.properties` 파일에 한국수출입은행 현재환율 API 인증키를 설정해야 한다.
API 인증키는 한국수출입은행 홈페이지의 '수출입은행 환율 API' 관련 페이지에서 발급받을 수 있다.

```properties
# globals.properties
ehgtCalc.authKey = 발급받은_API_인증키
```

#### 환율 계산

서로 다른 통화 간의 환율을 계산할 때 `EgovEhgtCalcUtil.getEhgtCalc()` 메서드를 사용한다.

- `getEhgtCalc(String srcType, long srcAmount, String cnvrType)`: 원본 통화 종류, 원본 금액,
  변환할 통화 종류를 입력받아 계산된 환율 금액을 반환한다.

#### 사용 예시

```java
import egovframework.com.utl.fcc.service.EgovEhgtCalcUtil;

public class ExchangeRateCalculationExample {
    public static void main(String[] args) {
        // 미국 달러(USD) 1달러를 한국 원화(KRW)로 계산
        // "U" = USD, "K" = KRW
        String result = EgovEhgtCalcUtil.getEhgtCalc("U", 1, "K");

        System.out.println("환율 계산 결과: " + result);
    }
}
```

*통화 코드의 경우, 한국 원화는 "K" 등 정해진 단일 문자 식별자 혹은 코드를 사용하므로 내부 API 구현 사양에 맞게 전달해야 한다.*

### 참고자료

- [한국수출입은행 환율 API](https://www.koreaexim.go.kr/ir/HPHKIR020M01)
