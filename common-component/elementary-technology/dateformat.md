---
  title: 날짜 지역화 처리
  linkTitle: 날짜 지역화 처리
  description: "다국어 지원을 위한 국가간 날짜 표시 변환 기능을 제공한다."
  url: /common-component/elementary-technology/dateformat/
  menu:
    depth:
      name: dateformat
      weight: 4
      parent: "new-components-v3.2"
      identifier: "dateformat"
---



# 요소기술 - 날짜 지역화 처리

## 개요

 다국어 지원을 위한 국가간 날짜 표시 변환 기능을 제공한다.

## 설명

 Locale에 맞게 날짜 및 시간의 출력 형식을 변환한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.fcc.service.EgovDateFormat | 날짜 및 시간에 대한 출력 형식 변환 |  |

##### 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | formatDate(Date date) | 날짜 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 날짜를 변환한다. |
| String | formatDate(Locale locale, Date date) | 날짜 표시 형식 변환 | Locale에 해당하는 형식으로 날짜를 변환한다. |
| String | formatDate(int style, Date date) | 날짜 표시 형식 변환 | 주어진 스타일에 따라 기본 Locale(JVM의 Locale)에 해당하는 형식으로 날짜를 변환한다. |
| String | formatDate(int style, Locale locale, Date date) | 날짜 표시 형식 변환 | 주어진 스타일에 따라 Locale에 해당하는 형식으로 날짜를 변환한다. |
| String | formatDateTime(Date date) | 날짜, 시간 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 날짜 및 시간을 변환한다. |
| String | formatDateTime(Locale locale, Date date) | 날짜, 시간 표시 형식 변환 | Locale에 해당하는 형식으로 날짜 및 시간을 변환한다. |
| String | formatDateTime(int dateStyle, int timeStyle, Date date) | 날짜, 시간 표시 형식 변환 | 주어진 스타일에 따라 기본 Locale(JVM의 Locale)에 해당하는 형식으로 날짜 및 시간을 변환한다. |
| String | formatDateTime(int dateStyle, int timeStyle, Locale locale, Date date) | 날짜, 시간 표시 형식 변환 | 주어진 스타일에 따라 Locale에 해당하는 형식으로 날짜 및 시간을 변환한다. |
| String | formatTime(Date date) | 시간 표시 형식 변환 | 기본 Locale(JVM의 Locale)에 해당하는 형식으로 시간을 변환한다. |
| String | formatTime(Locale locale, Date date) | 시간 표시 형식 변환 | Locale에 해당하는 형식으로 시간을 변환한다. |
| String | formatTime(int style, Date date) | 시간 표시 형식 변환 | 주어진 스타일에 따라 기본 Locale(JVM의 Locale)에 해당하는 형식으로 시간을 변환한다. |
| String | formatTime(int style, Locale locale, Date date) | 시간 표시 형식 변환 | 주어진 스타일에 따라 Locale에 해당하는 형식으로 시간을 변환한다. |

##### Input

- 날짜 및 시간 : Date 타입
- Locale : 지역화 처리를 위한 Locale
- style, dateStyle, timeStyle : 날짜 또는 시간의 스타일.  
사용 가능한 값은 java.text.DateFormat.FULL, java.text.DateFormat.LONG, java.text.DateFormat.MEDIUM, java.text.DateFormat.SHORT, java.text.DateFormat.DEFAULT 이다.

##### Output

- String : Locale에 맞게 변환된 날짜 및 시간 문자열

## 사용방법

```java
import java.text.DateFormat;
import egovframework.com.utl.fcc.service.EgovDateFormat;
 
...
Date today = new Date();
Locale[] locales = NumberFormat.getAvailableLocales();
 
for (Locale locale : locales ) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(locale).append(",").append(locale.getDisplayLanguage()).append(",")
        .append(locale.getDisplayCountry()).append(" : ")
        .append("\n Date          : ").append(EgovDateFormat.formatDate(DateFormat.FULL, locale, today))
        .append("\n Time          : ").append(EgovDateFormat.formatTime(DateFormat.FULL, locale, today))
        .append("\n Date and Time : ").append(EgovDateFormat.formatDateTime(locale, today));
    System.out.println(buffer.toString());
}
```

 출력 예

```bash
ko_KR,한국어,대한민국 : 
 Date          : 2014년 9월 17일 수요일
 Time          : 오후 3시 17분 48초 KST
 Date and Time : 2014. 9. 17 오후 3:17:48
en_US,영어,미국 : 
 Date          : Wednesday, September 17, 2014
 Time          : 3:17:48 PM KST
 Date and Time : Sep 17, 2014 3:17:48 PM
zh,중국어, : 
 Date          : 2014年9月17日 星期三
 Time          : 下午03时17分48秒 KST
 Date and Time : 2014-9-17 15:17:

```