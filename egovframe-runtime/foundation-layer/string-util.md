---
title: String Util Service
linkTitle: "String Util"
description: EgovStringUtil, EgovNumericUtil, EgovDateUtil, EgovObjectUtil 등의 서비스는 문자열, 숫자, 날짜, 객체 생성 등을 쉽게 다룰 수 있도록 다양한 기능을 제공한다. 이를 통해 패턴 매칭, 데이터 형식 변환, 숫자 계산, 날짜 계산, 객체 인스턴스화 등의 작업을 효율적으로 수행할 수 있다.
url: /egovframe-runtime/foundation-layer/string-util/
menu:
    depth:
        name: String Util
        weight: 19
        parent: "foundation-layer"
---
# String Util Service

## 개요

시스템을 개발할 때 필요한 문자열 데이터를 다루기 위해 다양한 기능을 사용하도록 서비스한다. 문자열을 다루는 **EgovStringUtil Service**와 숫자를 다루는 **EgovNumericUtil Service**, 날짜형식을 다루는 **EgovDateUtil Service** 그리고 객체 생성 등의 **EgovObjectUtil Service** 4가지가 있다.

## 설명

### 1. EgovStringUtil Service

#### Pattern matching

String이 특정 Pattern(정규표현식)에 부합하는지 검사한다.

##### Sample Source

```java
@Test
public void testPatternMatch() throws Exception {
  // pattern match 성공
  String str = "abc-def";
  pattern = "*-*";
  assertTrue(EgovStringUtil.isPatternMatching(str, pattern));
 
  // pattern match 실패
  str = "abc";
  assertTrue(!EgovStringUtil.isPatternMatching(str, pattern));
}
```

#### Formatting

다양한 타입의 데이터를 특정 String형식(Format)으로 변환한다.

##### Sample Source

```java
@Test
public void testTypeConversion() throws Exception {
  // int => string
  assertEquals("1", EgovStringUtil.integer2string(1));
 
  // long => string
  assertEquals("1000000000", EgovStringUtil.long2string(1000000000));
 
  // float => string
  assertEquals("34.5", EgovStringUtil.float2string(34.5f));
 
  // double => string
  assertEquals("34.5", EgovStringUtil.double2string(34.5));
 
  // string => int
  assertEquals(1, EgovStringUtil.string2integer("1"));
  assertEquals(0, EgovStringUtil.string2integer(null, 0));
 
  // string => float
  assertEquals(Float.valueOf(34.5f), Float.valueOf(EgovStringUtil.string2float("34.5")));
  assertEquals(Float.valueOf(10.5f), Float.valueOf(EgovStringUtil.string2float(null, 10.5f)));
 
  // string => double
  assertEquals(Double.valueOf(34.5), Double.valueOf(EgovStringUtil.string2double("34.5")));
  assertEquals(Double.valueOf(34.5), Double.valueOf(EgovStringUtil.string2double(null, 34.5)));
 
  // string => long
  assertEquals(100000000, EgovStringUtil.string2long("100000000"));
  assertEquals(100000000, EgovStringUtil.string2long(null, 100000000));
}
```

#### Substring

전체 String 중 일부를 가져온다.

##### Sample Source

```java
@Test
public void testToSubString() throws Exception {
  String source = "substring test";
 
  assertEquals("test", EgovStringUtil.toSubString(source, 10));
  assertEquals("string", EgovStringUtil.toSubString(source, 3, 9));
}
```

#### Trim

전체 String 중 앞뒤에 존재하는 공백 문자(white character)를 제거한다.

##### Sample Source

```java
@Test
public void testStringTrim() throws Exception {
  String str = "  substring  ";
 
  assertEquals("substring"  , EgovStringUtil.trim(str));
  assertEquals("substring  ", EgovStringUtil.ltrim(str));
  assertEquals("  substring", EgovStringUtil.rtrim(str));
}
```

#### Concatenate

두 String을 붙여서 하나의 String을 생성한다.

##### Sample Source

```java
@Test
public void testConcat() throws Exception {
  String str1 = "substring";
  String str2 = "test";
 
  assertEquals("substringtest", EgovStringUtil.concat(str1, str2));
}
```

#### Find

전체 String 중 특정 String Pattern이 있는지 찾는다.

##### Sample Source

```java
@Test
public void testFindPattern() throws Exception {
  String pattern = "\\d{4}-\\d{1,2}-\\d{1,2}";
 
  // 일치하는 pattern 을 찾는다.
  Matcher matcher = Pattern.compile(pattern).matcher("2009-02-03");    	
  assertTrue(matcher.find());
 
  // 일치하는 pattern 을 찾는다.
  matcher = Pattern.compile(pattern).matcher("abcdef2009-02-03abcdef");
  assertTrue(matcher.find());
 
  // 일치하는 pattern 을 찾지 못한다.
  matcher = Pattern.compile(pattern).matcher("abcdef2009-02-A3abcdef");
  assertFalse(matcher.find());
}
```

### 2. EgovNumericUtil Service

숫자체크, 더하기, 빼기, 곱하기, 나누기, 올림, 내림 기능

#### 숫자체크 기능

주어진 문자열이 숫자형식인지 검사한다.

##### Sample Source

```java
@Test
public void testIsNumber() throws Exception {
  assertFalse(EgovNumericUtil.isNumber("abc"));
  assertFalse(EgovNumericUtil.isNumber("!@"));
  assertFalse(EgovNumericUtil.isNumber("ab-123"));
  assertTrue(EgovNumericUtil.isNumber("-123"));
  assertTrue(EgovNumericUtil.isNumber("1234"));
}
```

#### 더하기 기능

두 문자열 값의 덧셈을 실행한다.

##### Sample Source

```java
@Test
public void testPlus() throws Exception {
  assertEquals("400",      EgovNumericUtil.plus("151", "249"));
  assertEquals("400.0000", EgovNumericUtil.plus("151.7531", "248.2469"));
  assertEquals("400.000",  EgovNumericUtil.plus("151.7531", "248.2469", 3));
  assertEquals("399.9654", EgovNumericUtil.plus("151.7531", "248.2123"));
  assertEquals("399.966",  EgovNumericUtil.plus("151.7531", "248.2123", 3, EgovNumericUtil.ROUND_UP));
  assertEquals("399.965",  EgovNumericUtil.plus("151.7531", "248.2123", 3, EgovNumericUtil.ROUND_DOWN));
  assertEquals("399.97",   EgovNumericUtil.plus("151.7531", "248.2123", 2, EgovNumericUtil.ROUND_HALF_UP));
}
```

#### 빼기 기능

두 문자열 값의 뺄셈을 실행한다.

##### Sample Source

```java
@Test
public void testMinus() throws Exception {
  assertEquals("89",       EgovNumericUtil.minus("240", "151"));
  assertEquals("96.4938",  EgovNumericUtil.minus("248.2469", "151.7531"));
  assertEquals("96.49380", EgovNumericUtil.minus("248.2469", "151.7531", 5));
  assertEquals("96.4592",  EgovNumericUtil.minus("248.2123", "151.7531"));
  assertEquals("96.460",   EgovNumericUtil.minus("248.2123", "151.7531", 3, EgovNumericUtil.ROUND_UP));
  assertEquals("96.459",   EgovNumericUtil.minus("248.2123", "151.7531", 3, EgovNumericUtil.ROUND_DOWN));
  assertEquals("96.46",    EgovNumericUtil.minus("248.2123", "151.7531", 2, EgovNumericUtil.ROUND_HALF_UP));
}
```

#### 곱하기 기능

두 문자열 값의 곱셈을 실행한다.

##### Sample Source

```java
@Test
public void testMultiply() throws Exception {
  assertEquals("180",       EgovNumericUtil.multiply("15", "12"));
  assertEquals("189.6135",  EgovNumericUtil.multiply("15.23", "12.45"));
  assertEquals("189.61350", EgovNumericUtil.multiply("15.23", "12.45", 5));
  assertEquals("189.614",   EgovNumericUtil.multiply("15.23", "12.45", 3, EgovNumericUtil.ROUND_UP));
  assertEquals("189.613",   EgovNumericUtil.multiply("15.23", "12.45", 3, EgovNumericUtil.ROUND_DOWN));
  assertEquals("189.61",    EgovNumericUtil.multiply("15.23", "12.45", 2, EgovNumericUtil.ROUND_HALF_UP));
}
```

#### 나누기 기능

두 문자열 값의 나눗셈을 실행한다.

##### Sample Source

```java
@Test
public void testDivide() throws Exception {
  assertEquals("1.25",  EgovNumericUtil.divide("15", "12"));
 
  Class<Exception> exceptionClass = null;
  try {
  	assertEquals("1.2232931726907630522088353413655", EgovNumericUtil.divide("15.23", "12.45"));
  } catch (Exception e) {
  	log.error("### Exception : " + e.toString());
  	exceptionClass = (Class<Exception>) e.getClass();
  } finally {
  	assertEquals(ArithmeticException.class, exceptionClass);
  }
 
  assertEquals("1.22",  EgovNumericUtil.divide("15.23", "12.45", 5));
  assertEquals("1.224", EgovNumericUtil.divide("15.23", "12.45", 3, EgovNumericUtil.ROUND_UP));
  assertEquals("1.223", EgovNumericUtil.divide("15.23", "12.45", 3, EgovNumericUtil.ROUND_DOWN));
  assertEquals("1.22",  EgovNumericUtil.divide("15.23", "12.45", 2, EgovNumericUtil.ROUND_HALF_UP));
}
```

#### 올림, 내림 기능

주어진 값의 반올림, 올림, 내림을 실행한다.

##### Sample Source

```java
@Test
public void testScale() throws Exception {
  assertEquals("151.754", EgovNumericUtil.setScale("151.7531", 3, EgovNumericUtil.ROUND_UP));
  assertEquals("151.753", EgovNumericUtil.setScale("151.7531", 3, EgovNumericUtil.ROUND_DOWN));
  assertEquals("151.753", EgovNumericUtil.setScale("151.7531", 3, EgovNumericUtil.ROUND_HALF_UP));
}
```

### 3. EgovDateUtil Service

날짜계산, 현재일자 조회, 요일, 날짜형식체크 기능

#### 날짜계산 기능

주어진 날짜에 해당 년,월 또는 일자를 더하여 계산된 일자를 조회한다.

##### Sample Source

```java
@Test
public void testCalcDate() throws Exception {
  assertEquals("20100114",  EgovDateUtil.getCalcDateAsString ("2009", "3", "20", 300, "day"));
  assertEquals("2010",      EgovDateUtil.getCalcYearAsString ("2009", "3", "20", 300, "day"));
  assertEquals("01",        EgovDateUtil.getCalcMonthAsString("2009", "3", "20", 300, "day"));
  assertEquals("14",        EgovDateUtil.getCalcDayAsString  ("2009", "3", "20", 300, "day"));
 
  assertEquals(2010,        EgovDateUtil.getCalcYearAsInt ("2009", "3", "20", 300, "day"));
  assertEquals(1,           EgovDateUtil.getCalcMonthAsInt("2009", "3", "20", 300, "day"));
  assertEquals(14,          EgovDateUtil.getCalcDayAsInt  ("2009", "3", "20", 300, "day"));
}
```
시작일자와 종료일자 및 두 시간 사이의 일자/밀리초 수를 계산한다.

##### Sample Source

```java
@Test
public void testDayCount() throws Exception {
  assertEquals(90,  EgovDateUtil.getDayCount("20090101", "20090401"));
  assertEquals(90,  EgovDateUtil.getDayCountWithFormatter("20090101", "20090401", "yyyyMMdd"));
  assertEquals(182, EgovDateUtil.getDayCountWithFormatter("2008/12/01", "2009/06/01", "yyyy/MM/dd"));
}
 
@Test
public void testTimeCount() throws Exception {
  assertEquals(86400000, EgovDateUtil.getTimeCount("20090401",       "20090402"));
  assertEquals(60000,    EgovDateUtil.getTimeCount("20090301000000", "20090301000100"));
  assertEquals(3600000,  EgovDateUtil.getTimeCount("20090301000000", "20090301010000"));
}
```

#### 현재일자 조회 기능

현재 일자를 조회한다.

##### Sample Source

```java
@Test
public void testCurrentDate() throws Exception {
  assertEquals(Calendar.getInstance().get(Calendar.YEAR),         EgovDateUtil.getCurrentYearAsInt());
  assertEquals(Calendar.getInstance().get(Calendar.MONTH) + 1,    EgovDateUtil.getCurrentMonthAsInt());
  assertEquals(Calendar.getInstance().get(Calendar.DAY_OF_MONTH), EgovDateUtil.getCurrentDayAsInt());
  assertEquals(Calendar.getInstance().get(Calendar.HOUR_OF_DAY),  EgovDateUtil.getCurrentHourAsInt());
  assertEquals(Calendar.getInstance().get(Calendar.MINUTE),       EgovDateUtil.getCurrentMinuteAsInt());
}
```

#### 요일 기능

입력 일자의 해당 요일을 조회한다.

##### Sample Source

```java
@Test
public void testGetDayOfWeek() throws Exception {
  assertEquals("일", EgovDateUtil.getDayOfWeekAsString("2009", "03", "22"));
  assertEquals("월", EgovDateUtil.getDayOfWeekAsString("2009", "03", "23"));
  assertEquals("화", EgovDateUtil.getDayOfWeekAsString("2009", "03", "24"));
  assertEquals("수", EgovDateUtil.getDayOfWeekAsString("2009", "03", "25"));
  assertEquals("목", EgovDateUtil.getDayOfWeekAsString("2009", "03", "26"));
  assertEquals("금", EgovDateUtil.getDayOfWeekAsString("2009", "03", "27"));
  assertEquals("토", EgovDateUtil.getDayOfWeekAsString("2009", "03", "28"));
}
```
두 일자 사이에 해당 요일의 수를 조회한다.

##### Sample Source

```java
@Test
public void testGetDayOfWeek() throws Exception {
  assertEquals(5,  EgovDateUtil.getDayOfWeekCount("20090301", "20090331", "일요일"));
  assertEquals(4,  EgovDateUtil.getDayOfWeekCount("20090301", "20090331", "토요일"));
  assertEquals(22, EgovDateUtil.getDayOfWeekCount("20090101", "20090531", "일"));
  assertEquals(52, EgovDateUtil.getDayOfWeekCount("20090101", "20091231", "일"));
  assertEquals(52, EgovDateUtil.getDayOfWeekCount("20090101", "20091231", "금"));
  assertEquals(52, EgovDateUtil.getDayOfWeekCount("20090101", "20091231", "토"));
}
```

#### 날짜 형식 체크 기능

해당 날짜의 형식이 적합성을 조회한다.

##### Sample Source

```java
@Test
public void testDateFormatCheck() throws Exception {
  // 형식이 틀린경우 ParseException 발생
  Class<Exception> exceptionClass = null;
 
  try {
  	dateFormatCheck = EgovDateUtil.dateFormatCheck("20090300");
  } catch (Exception e) {
  	exceptionClass = (Class<Exception>) e.getClass();
  } finally {
  	assertEquals(ParseException.class, exceptionClass);
  }
}
```

### 4. EgovObjectUtil Service

클래스명으로 객체를 생성하며 객체는 파라미터가 없는 기본 생성자 또는 파라미터가 존재하는 생성자 등 다양한 형태로 객체를 인스턴스화 할 수 있다.

#### Instantiate 기능

파라미터가 없는 기본 생성자로 객체를 인스턴스화 한다.

##### Sample Source

```java
@Test
public void testInstantiate() throws Exception {
  String className = "java.lang.String";
  Object object = EgovObjectUtil.instantiate(className);
 
  String string = (String) object;
  string = "eGovFramework";
  assertEquals("Framework", string.substring(4));
}
```

#### Instantiate 기능 - 생성자의 파라미터 포함

파라미터가 존재하는 형태의 생성자로 객체를 인스턴스화 한다.

##### Sample Source

```java
@Test
public void testInstantiateParamConstructor() throws Exception {
  String className = "java.lang.StringBuffer";
  String[] types = new String[]{"java.lang.String"};
  Object[] values = new Object[]{"전자정부 공통서비스"};
 
  StringBuffer sb = (StringBuffer)EgovObjectUtil.instantiate(className, types, values);
  sb.append(" 및 개발프레임워크 구축 사업");		
  assertEquals("전자정부 공통서비스 및 개발프레임워크 구축 사업", sb.toString());
}
```

## 참고자료

- [Jakarta Regexp](http://jakarta.apache.org/regexp/)