---
  title: 숫자 지역화 처리
  linkTitle: 숫자 지역화 처리
  description: "다국어 지원을 위한 국가간 숫자 표시 변환 기능을 제공한다."
  url: /common-component/elementary-technology/numberformat/
  menu:
    depth:
      name: 숫자 지역화 처리
      weight: 3
      parent: "new-components-v3.2"
      identifier: "numberformat"
---



# 요소기술 - 숫자 지역화 처리

## 개요

 다국어 지원을 위한 국가간 숫자 표시 변환 기능을 제공한다.

## 설명

 Locale에 맞게 숫자, 통화, 퍼센트의 출력 형식을 변환한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.fcc.service.EgovNumberFormat | 숫자, 통화, 퍼센트에 대한 출력 형식 변환 |  |

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | formatNumber(Number number) | 숫자 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Locale locale, Number number) | 숫자 표시 형식 변환 | Locale에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Number number, boolean groupingUsed) | 숫자 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Locale locale, Number number, boolean groupingUsed) | 숫자 표시 형식 변환 | Locale에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Number number, int maxFactionDigits) | 숫자 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Locale locale, Number number, int maxFactionDigits) | 숫자 표시 형식 변환 | Locale에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Number number, boolean groupingUsed, int maxFactionDigits) | 숫자 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 숫자를 변환한다. |
| String | formatNumber(Locale locale, Number number, boolean groupingUsed, int maxFactionDigits) | 숫자 표시 형식 변환 | Locale에 해당하는 형식으로 숫자를 변환한다. |
| String | formatCurrency(Number number) | 통화 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 통화를 변환한다. |
| String | formatCurrency(Locale locale, Number number) | 통화 표시 형식 변환 | Locale에 해당하는 형식으로 통화를 변환한다. |
| String | formatCurrency(Number number, boolean groupingUsed) | 통화 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 통화를 변환한다. |
| String | formatCurrency(Locale locale, Number number, boolean groupingUsed) | 통화 표시 형식 변환 | Locale에 해당하는 형식으로 통화를 변환한다. |
| String | formatPercent(Number number) | 퍼센트 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Locale locale, Number number) | 퍼센트 표시 형식 변환 | Locale에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Number number, boolean groupingUsed) | 퍼센트 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Locale locale, Number number, boolean groupingUsed) | 퍼센트 표시 형식 변환 | Locale에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Number number, int maxFactionDigits) | 퍼센트 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Locale locale, Number number, int maxFactionDigits) | 퍼센트 표시 형식 변환 | Locale에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Number number, boolean groupingUsed, int maxFactionDigits) | 퍼센트 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 퍼센트를 변환한다. |
| String | formatPercent(Locale locale, Number number, boolean groupingUsed, int maxFactionDigits) | 퍼센트 표시 형식 변환 | Locale에 해당하는 형식으로 퍼센트를 변환한다. |

##### Input

- 숫자 : Number 타입
- Locale : 지역화 처리를 위한 Locale
- groupingUsed : 그룹 분리기호 포함 여부
- maxFactionDigits : 변환된 문자열에서 출력할 소수점 이하 최대 자리수

##### Output

- String : Locale에 맞게 변환된 숫자, 통화, 퍼센트 문자열

## 사용방법

```java
사용방법
import egovframework.com.utl.fcc.service.EgovNumberFormat;
 
...
Double amount = new Double(10000000.567);
Double percent = new Double(11.23456);
Locale[] locales = NumberFormat.getAvailableLocales();
 
for (Locale locale : locales ) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(locale).append(",").append(locale.getDisplayLanguage()).append(",")
        .append(locale.getDisplayCountry()).append(" : ")
        .append("\n Number        : ").append(EgovNumberFormat.formatNumber(locale, amount))
        .append("\n Currency      : ").append(EgovNumberFormat.formatCurrency(locale, amount))
        .append("\n Percent       : ").append(EgovNumberFormat.formatPercent(locale, percent));
    System.out.println(buffer.toString());
}
```

 출력 예

```bash
ko_KR,한국어,대한민국 : 
 Number        : 10,000,000.567
 Currency      : ￦10,000,001
 Percent       : 1,123%
en_US,영어,미국 : 
 Number        : 10,000,000.567
 Currency      : $10,000,000.57
 Percent       : 1,123%
ru_RU,러시아어,러시아 : 
 Number        : 10 000 000,567
 Currency      : 10 000 000,57 руб.
 Percent       : 1 123%
tr_TR,터키어,터키 : 
 Number        : 10.000.000,567
 Currency      : 10.000.000,57 TL
 Percent       : % 1.123

```