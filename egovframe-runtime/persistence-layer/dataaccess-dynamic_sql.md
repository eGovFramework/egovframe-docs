---
title: iBATIS Dynamic SQL 사용
linkTitle: "Dynamic SQL"
description: iBATIS의 Dynamic 요소를 사용하면 다양한 조건에 따라 쿼리를 동적으로 변경할 수 있으며, 조건에 따라 SQL 문의 일부가 추가 또는 제거된다. 예를 들어, 특정 파라미터 값이 있을 때만 조건절이 추가되는 방식으로, SQL의 재사용성을 높이고 복잡한 조건 분기 문제를 해결한다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-dynamic-sql/
menu:
    depth:
        name: Dynamic SQL
        weight: 7
        parent: dataaccess-ibatis
---
# Dynamic SQL

 일반적으로 JDBC API 를 사용한 코딩에서 한번 정의한 쿼리문을 최대한 재사용하고자 하나 단순 파라메터 변수의 값만 변경하는 것으로 해결하기 어렵고 다양한 조건에 따라 조금씩 다른 쿼리의 실행이 필요한 경우 많은 if~else 조건 분기의 연결이 필요한 문제가 있다. 여기에서는 SQL 문의 동적인 변경에 대한 상대적으로 유연한 방법을 제공하는 iBATIS 의 Dynamic 요소에 대해 알아본다.

## 기본 Dynamic 요소 사용 방법

 아래의 샘플 Dynamic 요소 사용예를 참고하라.

### Sample Dynamic SQL mapping xml

```xml
	..
	<typeAlias alias="jobHistVO" type="egovframework.rte.psl.dataaccess.vo.JobHistVO" />
 
	<select id="selectJobHistListUsingDynamicElement" parameterClass="jobHistVO" resultClass="jobHistVO">
		<![CDATA[
			select EMP_NO     as empNo,
			       START_DATE as startDate,
			       END_DATE   as endDate,
			       JOB        as job,
			       SAL        as sal,
			       COMM       as comm,
			       DEPT_NO    as deptNo
			from   JOBHIST
		]]>
		<dynamic prepend="where">
			<isNotNull property="empNo" prepend="and">
				EMP_NO = #empNo#
			</isNotNull>		
		</dynamic>
			order by EMP_NO, START_DATE
	</select>
```

 위 sql 매핑 파일에서 파라메터 객체의 empNo 속성의 값 유무에 따라 where EMP\_NO = #empNo# 조건절이 동적으로 추가/제거 될 수 있는 예이다. 위에서 dynamic 의 prepend 속성으로 “where” 를 지정하고 있지만 하위 요소의 조건이 하나라도 만족하지 않으면 sql 문에 추가되지 않는다. 또한 위의 예에서는 하위 요소로 isNotNull 태그에 prepend=“and” 가 지정되어 있지만 처음 true 가 되는 조건의 prepend 는 parent 인 dynamic 의 prepend 인 “where” 로 덮어써져 최종적으로는 where EMP\_NO = #empNo# 가 됨에 유의한다.

### Sample TestCase

```java
..
    @Test
    public void testDynamicStatement() throws Exception {
        JobHistVO vo = new JobHistVO();
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트
        vo.setEmpNo(new BigDecimal(7788));
 
        // select
        List<JobHistVO> resultList =
            jobHistDAO.selectJobHistList(
                "selectJobHistListUsingDynamicElement", vo);
 
        // check
        assertNotNull(resultList);
        assertEquals(3, resultList.size());
 
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1987-04-19"), resultList.get(0).getStartDate());
        assertEquals(sdf.parse("1988-04-13"), resultList.get(1).getStartDate());
        assertEquals(sdf.parse("1990-05-05"), resultList.get(2).getStartDate());
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트
        vo.setEmpNo(null);
 
        // select
        resultList =
            jobHistDAO.selectJobHistList(
                "selectJobHistListUsingDynamicElement", vo);
 
        // check
        assertNotNull(resultList);
        // where 이 수행되지 않아 전체 데이터가 조회될 것임
        assertEquals(17, resultList.size());
 
    }
```

 위에서 파라메터 객체에 empNo 의 값을 세팅했을 때 결과로는 해당 조건절이 동적으로 추가된 조회 결과인 사원번호 7788 에 해당하는 Job 이력 3건만 조회되지만 empNo 의 값을 세팅하지 않았을 때(위에서 null 로 세팅하는 것도 동일) 조회 조건절 없이 전체 사원에 대한 이력이 모두 조회됨을 확인할 수 있다.

## Unary 조건 비교

 아래의 샘플 sql mapping xml 예를 참고하라.

 일반적인 경우 Dynamic SQL 작성을 위한 동적 요소는 Where 조건절의 변경을 위해 많이 쓰이지만, 아래에서는 테스트 편의의 목적으로 dual 에 대하여 임의의 상수를 입력 값으로 전달한 결과를 재조회 하는 과정에 Unary 비교 연산을 활용한 예이다.

### Sample Unary 비교 연산

```xml
	..
	<typeAlias alias="egovMap" type="egovframework.rte.psl.dataaccess.util.EgovMap" />
 
	<select id="selectDynamicUnary" parameterClass="map" remapResults="true" resultClass="egovMap">
		select
		<dynamic>
			<isEmpty property="testEmptyString">
				'empty String' as IS_EMPTY_STRING
			</isEmpty>
			<isNotEmpty property="testEmptyString">
				'not empty String' as IS_EMPTY_STRING
			</isNotEmpty>
			<isEmpty prepend=", " property="testEmptyCollection">
				'empty Collection' as IS_EMPTY_COLLECTION
			</isEmpty>
			<isNotEmpty prepend=", " property="testEmptyCollection">
				'not empty Collection' as IS_EMPTY_COLLECTION
			</isNotEmpty>
			<isNull prepend=", " property="testNull">
				'null' as IS_NULL
			</isNull>
			<isNotNull prepend=", " property="testNull">
				'not null' as IS_NULL
			</isNotNull>
			<isPropertyAvailable prepend=", " property="testProperty">
				'testProperty Available' as	TEST_PROPERTY_AVAILABLE
			</isPropertyAvailable>
			<isNotPropertyAvailable prepend=", " property="testProperty">
				'testProperty Not Available' as TEST_PROPERTY_AVAILABLE
			</isNotPropertyAvailable>
		</dynamic>
		from dual
	</select>
```

 위에서 테스트한 Unary 비교 연산 태그는 다음과 같다.

- isEmpty : Collection, String(또는 String.valueOf()) 대상 속성이 null 이거나 empty(”” 또는 size() &lt; 1) 인 경우 true
- isNotEmpty : Collection, String(또는 String.valueOf()) 대상 속성이 not null 이고 not empty(”” 또는 size() &lt; 1) 인 경우 true
- isNull : 대상 속성이 null 인 경우 true
- isNotNull : 대상 속성이 not null 인 경우 true
- isPropertyAvailable : 파라메터 객체에 대상 속성이 존재하는 경우 true
- isNotPropertyAvailable : 파라메터 객체에 대상 속성이 존재하지 않는 경우 true

 Unary 비교 연산 태그에 사용할 수 있는 속성은 다음과 같다.

- prepend : 동적 구문 앞에 추가되는 override 가능한 SQL 영역.
- property : 필수. 파라메터 객체의 어떤 property 에 대한 체크인지 지정.
- removeFirstPrepend : 첫번째로 내포될 내용을 생성하는 태그의 prepend 를 제거할지 여부(true/false)
- open : 전체 결과 구문에 대한 시작 문자열
- close : 전체 결과 구문에 대한 닫는 문자열

### Sample TestCase

```java
..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicUnary() throws Exception {
        Map map = new HashMap();
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트
        // isEmpty 테스트 - String
        map.put("testEmptyString", "");
        // isEmpty 테스트 - Collection
        List list = new ArrayList();
        map.put("testEmptyCollection", list);
        // isNull 테스트
        map.put("testNull", null);
        // isPropertyAvailable 테스트 - cf.) property 의 값을 null 로 설정하더라도 해당 property 는 Available 한것에 유의!
        map.put("testProperty", null);
 
        // select
        Map resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicUnary", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("empty String", resultMap.get("isEmptyString"));
        assertEquals("empty Collection", resultMap.get("isEmptyCollection"));
        assertEquals("null", resultMap.get("isNull"));
        assertEquals("testProperty Available", resultMap
            .get("testPropertyAvailable"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 2
        // isEmpty 테스트 - String - null 인 경우도 isEmpty 는 만족함
        map.put("testEmptyString", null);
        // isEmpty 테스트 - Collection - null 인 경우도 isEmpty 는 만족함
        List nullList = null;
        map.put("testEmptyCollection", nullList);
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicUnary", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("empty String", resultMap.get("isEmptyString"));
        assertEquals("empty Collection", resultMap.get("isEmptyCollection"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 3
        map.clear();
        // isEmpty 테스트 - String
        map.put("testEmptyString", "aa");
        // isEmpty 테스트 - Collection
        list.clear();
        list.add("aa");
        map.put("testEmptyCollection", list);
        // isNull 테스트
        map.put("testNull", new BigDecimal(0));
        // isPropertyAvailable 테스트 - key 자체를 담지 않았을 때 isNotPropertyAvailable 임
        // map.put("testProperty", null);
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicUnary", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("not empty String", resultMap.get("isEmptyString"));
        assertEquals("not empty Collection", resultMap.get("isEmptyCollection"));
        assertEquals("not null", resultMap.get("isNull"));
        assertEquals("testProperty Not Available", resultMap
            .get("testPropertyAvailable"));
 
    }
```

 위에서 Unary 조건 비교를 위한 입력 파라메터 객체(여기서는 Map 사용)를 다양하게 세팅하여 어떤 경우에 어떤 조건이 만족하는지 테스트한 예이다. 위에서 isEmpty 의 경우 String 이 null 이거나 ””, Collection 에 하위 element 가 add 되지 않은 경우나 Collection 객체 자체가 null 인 경우에 모두 만족하는 것을 확인할 수 있으며, isPropertyAvailable 태그는 입력 객체에 해당 key 만 추가되있고 값은 null 인 경우에도 true 임을 확인할 수 있다. Dynamic SQL 의 동적인 where 조건절 변경의 경우 전달된 인자의 특정 property 에 대한 isNotNull 또는 isNotEmpty 로 간단히 비교하는 경우가 가장 많이 쓰이게 된다.

## Binary 조건 비교

 아래의 샘플 sql mapping xml 예를 참고하라.

 마찬가지로 아래에서는 테스트 편의의 목적으로 dual 에 대하여 임의의 상수를 입력 값으로 전달한 결과를 재조회 하는 과정에 Binary 비교 연산을 활용한 예이다.

### Sample Binary 비교 연산

```xml
	..
	<typeAlias alias="egovMap" type="egovframework.rte.psl.dataaccess.util.EgovMap" />
 
	<select id="selectDynamicBinary" parameterClass="map" remapResults="true" resultClass="egovMap">
		select
		<dynamic>
			<isEqual property="testString" compareValue="test">
				'$testString$' as TEST_STRING, 'test : equals' as IS_EQUAL
			</isEqual>
			<isNotEqual property="testString" compareValue="test">
				'$testString$' as TEST_STRING, 'test : not equals' as IS_EQUAL
			</isNotEqual>
			<isPropertyAvailable property="testNumeric">
				<isEqual property="testNumeric" prepend=", " compareValue="10">
					cast($testNumeric$ as $castTypeScale$) as TEST_NUMERIC, '10 : equals' as IS_EQUAL_NUMERIC
				</isEqual>
				<isNotEqual property="testNumeric" prepend=", " compareValue="10">
					cast($testNumeric$ as $castTypeScale$) as TEST_NUMERIC, '10 : not equals' as IS_EQUAL_NUMERIC
				</isNotEqual>
			</isPropertyAvailable>
			<isGreaterEqual property="testNumeric" prepend=", " compareValue="10">
				'10 <![CDATA[<=]]> $testNumeric$' as IS_GREATER_EQUAL
			</isGreaterEqual>
			<isGreaterThan property="testNumeric" prepend=", " compareValue="10">
				'10 <![CDATA[<]]> $testNumeric$' as IS_GREATER_THAN
			</isGreaterThan>
			<isLessEqual property="testNumeric" prepend=", " compareValue="10">
				'10 <![CDATA[>=]]> $testNumeric$' as IS_LESS_EQUAL
			</isLessEqual>
			<isLessThan property="testNumeric" prepend=", " compareValue="10">
				'10 <![CDATA[>]]> $testNumeric$' as IS_LESS_THAN
			</isLessThan>
			<!-- checkMore -->
			<isPropertyAvailable property="testOtherString">
				<isEqual property="testOtherString" prepend=", " compareProperty="testString">
					'$testOtherString$' as TEST_OTHER_STRING, 'test : testOtherString equals testString' as COMPARE_PROPERTY_EQUAL
				</isEqual>
				<isNotEqual property="testOtherString" prepend=", " compareProperty="testString">
					'$testOtherString$' as TEST_OTHER_STRING, 'test : testOtherString not equals testString' as COMPARE_PROPERTY_EQUAL
				</isNotEqual>
				<isGreaterEqual property="testOtherString" prepend=", " compareProperty="testString">
					'''$testOtherString$'' <![CDATA[>=]]> ''$testString$''' as COMPARE_PROPERTY_GREATER_EQUAL
				</isGreaterEqual>
				<isGreaterThan property="testOtherString" prepend=", " compareProperty="testString">
					'''$testOtherString$'' <![CDATA[>]]> ''$testString$''' as COMPARE_PROPERTY_GREATER_THAN
				</isGreaterThan>
				<isLessEqual property="testOtherString" prepend=", " compareProperty="testString">
					'''$testOtherString$'' <![CDATA[<=]]> ''$testString$''' as COMPARE_PROPERTY_LESS_EQUAL
				</isLessEqual>
				<isLessThan property="testOtherString" prepend=", " compareProperty="testString">
					'''$testOtherString$'' <![CDATA[<]]> ''$testString$''' as COMPARE_PROPERTY_LESS_THAN
				</isLessThan>
			</isPropertyAvailable>
		</dynamic>
		from dual
	</select>
```

 위에서 테스트한 Binary 비교 연산 태그는 다음과 같다.

- isEqual : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값과 같은 경우 true
- isNotEqual : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값과 다른 경우 true
- isGreaterEqual : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값보다 크거나 같은 경우 true
- isGreaterThan : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값보다 큰 경우 true
- isLessEqual : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값보다 작거나 같은 경우 true
- isLessThan : 대상 속성이 compareValue 값 또는 compareProperty 로 명시한 대상 속성 값보다 작은 경우 true

 Binary 비교 연산 태그에 사용할 수 있는 속성은 다음과 같다.

- prepend : 동적 구문 앞에 추가되는 override 가능한 SQL 영역.
- property : 필수. 파라메터 객체의 어떤 property 에 대한 비교인지 지정.
- compareProperty : 파라메터 객체의 다른 property 와 대상 property 값을 비교하고자 할 경우 지정. (compareValue 가 없는 경우 필수)
- compareValue : 대상 property 와 비교될 값을 지정. (compareProperty 가 없는 경우 필수)
- removeFirstPrepend : 첫번째로 내포될 내용을 생성하는 태그의 prepend 를 제거할지 여부(true/false)
- open : 전체 결과 구문에 대한 시작 문자열
- close : 전체 결과 구문에 대한 닫는 문자열

 위에서 각 비교 연산 태그의 중첩이 가능함을 확인할 수 있다. 복잡한 조건 처리가 필요한 경우 다양한 비교 연산 태그의 중첩으로 적절히 구성할 수 있을 것이다. 또한 비교 연산자 (&gt;, &lt;) 등과 같이 XML 에서 escape 처리가 필요한 경우 &lt;!\[CDATA\[&gt;\]\]&gt; 와 같이 CDATA 섹션으로 묶어 사용할 수 있다. CDATA 섹션을 전체 쿼리 영역에 묶어 한번에 사용하면 편하겠지만 Dynamic 요소 자체는 실제 XML 태그로 해석이 되어야 하므로 위와 같이 Dynamic 영역 내에서 발생하는 특수문자에 대해 개별로 사용하는 번거로움이 존재함에 유의한다. cf.) < , > 대신 &amp;lt; , &amp;gt; 와 같이 직접 escape 처리 할수도 있다.

### Sample TestCase

```java

..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicBinary() throws Exception {
        Map map = new HashMap();
        String castTypeScale = "numeric(2)";
        // oracle 인 경우 - numeric 에 대응되는 type 은 number
        if (isOracle) {
            castTypeScale = "number(2)";
        } else if (isMysql) {
            castTypeScale = "decimal(2)";
        }
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트
        // isEqual 테스트 - String
        map.put("testString", "test");
        // isEqual 테스트 - BigDecimal
        map.put("testNumeric", new BigDecimal(10));
        // dual 임시 테이블 상에 상수 조회시 numeric(db) - decimal(java) 처리를 위해 cast 처리 추가
        map.put("castTypeScale", castTypeScale);
 
        // select
        Map resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("test", resultMap.get("testString"));
        assertEquals("test : equals", resultMap.get("isEqual"));
        assertEquals(new BigDecimal(10), resultMap.get("testNumeric"));
        assertEquals("10 : equals", resultMap.get("isEqualNumeric"));
        assertEquals("10 <= 10", resultMap.get("isGreaterEqual"));
        assertTrue(!resultMap.containsKey("isGreaterThan"));
        assertEquals("10 >= 10", resultMap.get("isLessEqual"));
        assertTrue(!resultMap.containsKey("isLessThan"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 2
        map.clear();
 
        // isEqual 테스트 - String
        map.put("testString", "not test");
        // isEqual 테스트 - BigDecimal
        map.put("testNumeric", new BigDecimal(11));
        // dual 임시 테이블 상에 상수 조회시 numeric(db) - decimal(java) 처리를 위해 cast 처리 추가
        map.put("castTypeScale", castTypeScale);
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("not test", resultMap.get("testString"));
        assertEquals("test : not equals", resultMap.get("isEqual"));
        assertEquals(new BigDecimal(11), resultMap.get("testNumeric"));
        assertEquals("10 : not equals", resultMap.get("isEqualNumeric"));
        assertEquals("10 <= 11", resultMap.get("isGreaterEqual"));
        assertEquals("10 < 11", resultMap.get("isGreaterThan"));
        assertTrue(!resultMap.containsKey("isLessEqual"));
        assertTrue(!resultMap.containsKey("isLessThan"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 2
        map.clear();
 
        // isEqual 테스트 - String
        // isEqual 비교 대상 property 에 null 값을 넘기면 에러는 발생하지 않고, isNotEqual 과 매칭됨
        map.put("testString", null);
        // isEqual 테스트 - BigDecimal
        map.put("testNumeric", new BigDecimal(9));
        // dual 임시 테이블 상에 상수 조회시 numeric(db) - decimal(java) 처리를 위해 cast 처리 추가
        map.put("castTypeScale", castTypeScale);
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
        // oracle 인 경우 '' 는 null 과 같고 결과 객체에는 null 로 맵핑됨
        assertEquals(!(isOracle || isTibero) ? "" : null, resultMap
            .get("testString"));
        assertEquals("test : not equals", resultMap.get("isEqual"));
        assertEquals(new BigDecimal(9), resultMap.get("testNumeric"));
        assertEquals("10 : not equals", resultMap.get("isEqualNumeric"));
        assertTrue(!resultMap.containsKey("isGreaterEqual"));
        assertTrue(!resultMap.containsKey("isGreaterThan"));
        assertEquals("10 >= 9", resultMap.get("isLessEqual"));
        assertEquals("10 > 9", resultMap.get("isLessThan"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 3
        map.clear();
 
        map.put("testString", "test");
        // isEqual 테스트 - BigDecimal
        map.put("testOtherString", "test");
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
 
        assertEquals("test : equals", resultMap.get("isEqual"));
        // testNumeric property 를 넘기지 않았을 때 기대 결과
        assertTrue(!resultMap.containsKey("isGreaterEqual"));
        assertTrue(!resultMap.containsKey("isGreaterThan"));
        assertTrue(!resultMap.containsKey("isLessEqual"));
        assertTrue(!resultMap.containsKey("isLessThan"));
        // testOtherString 비교
        assertEquals("test", resultMap.get("testOtherString"));
        assertEquals("test : testOtherString equals testString", resultMap
            .get("comparePropertyEqual"));
        assertEquals("'test' >= 'test'", resultMap
            .get("comparePropertyGreaterEqual"));
        assertTrue(!resultMap.containsKey("comparePropertyGreaterThan"));
        assertEquals("'test' <= 'test'", resultMap
            .get("comparePropertyLessEqual"));
        assertTrue(!resultMap.containsKey("comparePropertyLessThan"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 4
        map.clear();
 
        map.put("testString", "test");
        // 'test' >= 'sample' 테스트
        map.put("testOtherString", "sample");
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
 
        assertEquals("test : equals", resultMap.get("isEqual"));
        // testNumeric property 를 넘기지 않았을 때 기대 결과
        assertTrue(!resultMap.containsKey("isGreaterEqual"));
        assertTrue(!resultMap.containsKey("isGreaterThan"));
        assertTrue(!resultMap.containsKey("isLessEqual"));
        assertTrue(!resultMap.containsKey("isLessThan"));
        // testOtherString 비교
        assertEquals("sample", resultMap.get("testOtherString"));
        assertEquals("test : testOtherString not equals testString", resultMap
            .get("comparePropertyEqual"));
        assertTrue(!resultMap.containsKey("comparePropertyGreaterEqual"));
        assertTrue(!resultMap.containsKey("comparePropertyGreaterThan"));
        assertEquals("'sample' <= 'test'", resultMap
            .get("comparePropertyLessEqual"));
        assertEquals("'sample' < 'test'", resultMap
            .get("comparePropertyLessThan"));
 
        // 입력 파라메터 객체의 property 에 따른 Dynamic 테스트 5
        map.clear();
 
        map.put("testString", "test");
        // 'test' <= 'testa' 테스트
        map.put("testOtherString", "testa");
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicBinary", map);
 
        // check
        assertNotNull(resultMap);
 
        assertEquals("test : equals", resultMap.get("isEqual"));
        // testNumeric property 를 넘기지 않았을 때 기대 결과
        assertTrue(!resultMap.containsKey("isGreaterEqual"));
        assertTrue(!resultMap.containsKey("isGreaterThan"));
        assertTrue(!resultMap.containsKey("isLessEqual"));
        assertTrue(!resultMap.containsKey("isLessThan"));
        // testOtherString 비교
        assertEquals("testa", resultMap.get("testOtherString"));
        assertEquals("test : testOtherString not equals testString", resultMap
            .get("comparePropertyEqual"));
        assertEquals("'testa' >= 'test'", resultMap
            .get("comparePropertyGreaterEqual"));
        assertEquals("'testa' > 'test'", resultMap
            .get("comparePropertyGreaterThan"));
        assertTrue(!resultMap.containsKey("comparePropertyLessEqual"));
        assertTrue(!resultMap.containsKey("comparePropertyLessThan"));
 
    }


```

 위에서 Binary 조건 비교를 위한 입력 파라메터 객체(여기서는 Map 사용)를 다양하게 세팅하여 어떤 경우에 어떤 조건이 만족하는지 테스트한 예이다. 위에서 숫자형의 입력객체 속성에 대해 isGreaterEqual, isGreaterThan, isLessEqual, isLessThan 비교의 경우 쉽게 결과를 예상할 수 있으며 숫자 형식의 결과 조회를 위해 DB 단의 cast 를 처리하게 하였다. 테스트 시나리오 4, 5 에서 String 에 대한 isGreaterEqual, isGreaterThan, isLessEqual, isLessThan 가 가능함을 확인할 수 있으며 'sample' &lt; 'test' , 'testa' &gt; 'test' 임을 확인할 수 있다.

## ParameterPresent 비교

 아래의 샘플 sql mapping xml 예를 참고하라.

### Sample ParameterPresent 비교

```xml
	..
	<typeAlias alias="egovMap" type="egovframework.rte.psl.dataaccess.util.EgovMap" />
 
	<select id="selectDynamicParameterPresent" parameterClass="map" remapResults="true" resultClass="egovMap">
		select 
			<isParameterPresent>
				'parameter object exist' as IS_PARAMETER_PRESENT
			</isParameterPresent>
			<isNotParameterPresent>
				'parameter object not exist' as IS_PARAMETER_PRESENT
			</isNotParameterPresent>
		from dual
	</select>
```

- isParameterPresent : 파라메터 객체가 전달된(not null) 경우 true
- isNotParameterPresent : 파라메터 객체가 전달되지 않은(null) 경우 true

 ParameterPresent 비교 연산 태그에 사용할 수 있는 속성은 다음과 같다.

- prepend : 동적 구문 앞에 추가되는 override 가능한 SQL 영역.
- removeFirstPrepend : 첫번째로 내포될 내용을 생성하는 태그의 prepend 를 제거할지 여부(true/false)
- open : 전체 결과 구문에 대한 시작 문자열
- close : 전체 결과 구문에 대한 닫는 문자열

### Sample TestCase

```java
..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicParameterPresent() throws Exception {
 
        // 입력 파라메터 객체의 전달 여부에 따른 Dynamic 테스트
        // isParameterPresent 테스트
        Map map = new HashMap();
 
        // select
        Map resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicParameterPresent", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("parameter object exist", resultMap
            .get("isParameterPresent"));
 
        map = null;
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicParameterPresent", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("parameter object not exist", resultMap
            .get("isParameterPresent"));
    }
```

 iBATIS 의 쿼리문 실행을 위한 API 호출 시 파라메터 객체의 전달 여부에 따라 isParameterPresent, isNotParameterPresent 의 비교 연산을 사용할 수 있다.

## iterate 연산

 아래의 샘플 sql mapping xml 예를 참고하라.

 일반적으로 iterate 태그 처리에 가장 많이 사용되는 in 조건절 처리 예이다.

### Sample iterate 연산

```xml
	..
 	<typeAlias alias="jobHistVO" type="egovframework.rte.psl.dataaccess.vo.JobHistVO" />
	<typeAlias alias="empIncludesEmpListVO" type="egovframework.rte.psl.dataaccess.vo.EmpIncludesEmpListVO" />
 
	<select id="selectJobHistListUsingDynamicIterate" parameterClass="empIncludesEmpListVO" resultClass="jobHistVO">
		<![CDATA[
			select EMP_NO     as empNo,
			       START_DATE as startDate,
			       END_DATE   as endDate,
			       JOB        as job,
			       SAL        as sal,
			       COMM       as comm,
			       DEPT_NO    as deptNo
			from   JOBHIST
		]]>
		<dynamic prepend="where">
			<iterate property="empList" open="EMP_NO in (" conjunction=", " close=")">
				#empList[].empNo#
			</iterate>		
		</dynamic>
			order by EMP_NO, START_DATE
	</select>
```

- iterate : collection 형태의 대상 객체에 대하여 포함하고 있는 각 개별 요소만큼 반복 루프를 돌며 해당 내용을 수행한다.

 iterate 태그에 사용할 수 있는 속성은 다음과 같다.

- prepend : 동적 구문 앞에 추가되는 override 가능한 SQL 영역.
- property : java.util.Collection 이나 java.util.Iterator 또는 array(배열) 유형인 대상 객체를 지정. 명시되지 않으면 파라메터 객체가 collection 임을 가정하여 처리됨.
- removeFirstPrepend : 첫번째로 내포될 내용을 생성하는 태그의 prepend 를 제거할지 여부(true/false/iterate)
- open : 전체 결과 구문에 대한 시작 문자열. 괄호 용도로 유용함.
- close : 전체 결과 구문에 대한 닫는 문자열. 괄호 용도로 유용함.
- conjunction : 각 iteration 사이에 적용될 문자열. AND, OR 연산자나 ',' 등의 구분자 필요시 유용함.

 위에서는 empList 라는 attribute 로 List&lt;EmpVO&gt; 인 리스트 객체를 포함하는 EmpIncludesEmpListVO 가 파라메터 객체로 사용되고 있으며, iterate 태그에 의해서 empList 의 size 만큼 각 EmpVO 객체의 empNo 값이 in 리스트에 포함되는 아래의 조건절이 동적으로 만들어지게 된다.

```bashxml
where EMP_NO in ( ? , ? , ? ) 
```

 iterate 태그의 body 영역 표기법에 유의한다. #empList\[\].empNo# 에서 확인할 수 있듯이 looping 중의 현재 item 을 지시하기 위해 '리스트속성명\[\]' 이 사용되고 있으며 여기서는 해당 item 이 EmpVO 이고 empNo 라는 property 를 포함하고 있으며 이 값이 in 절의 현재 항목으로 바인딩되고 있다. 만약 파라메터 객체 자체가 iterate 가능한 형태인 경우 iterate property 의 명시 없이 body 영역에 '\[\]' 로 바로 현재 item 을 지시할 수 있다.

- iBATIS 에서는 파라메터 객체가 복합 객체인 경우 dot notation (. 을 사용하여) 을 사용하여 쉽게 원하는 sub 객체/속성에 접근할 수 있다.

### Sample TestCase

```java
..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicIterate() throws Exception {
        // CompositeKeyTest.testCompositeKeySelect() 참조
        EmpVO vo = new EmpVO();
        // 7521,'WARD','SALESMAN',7698,'1981-02-22',1250,500,30
        // --> mgr 이 7698 인 EMP
        // 7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600 --> O
        // 7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250 --> O
        // 7844,'TURNER','SALESMAN',7698,'1981-09-08',1500 --> O
        // 7900,'JAMES','CLERK',7698,'1981-12-03',950 --> X
        vo.setEmpNo(new BigDecimal(7521));
 
        // select
        EmpIncludesEmpListVO resultVO =
            empDAO.selectEmpIncludesEmpList(
                "selectEmpIncludesSameMgrMoreSalaryEmpList", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(new BigDecimal(7521), resultVO.getEmpNo());
        assertEquals("WARD", resultVO.getEmpName());
        assertTrue(resultVO.getEmpList() instanceof List);
        assertEquals(3, resultVO.getEmpList().size());
        assertEquals(new BigDecimal(7499), resultVO.getEmpList().get(0)
            .getEmpNo());
        assertEquals(new BigDecimal(1600), resultVO.getEmpList().get(0)
            .getSal());
        assertEquals(new BigDecimal(7844), resultVO.getEmpList().get(1)
            .getEmpNo());
        assertEquals(new BigDecimal(1500), resultVO.getEmpList().get(1)
            .getSal());
        assertEquals(new BigDecimal(7654), resultVO.getEmpList().get(2)
            .getEmpNo());
        assertEquals(new BigDecimal(1250), resultVO.getEmpList().get(2)
            .getSal());
 
        // select
        List<JobHistVO> resultList =
            jobHistDAO.getSqlMapClientTemplate().queryForList(
                "selectJobHistListUsingDynamicIterate", resultVO);
 
        assertNotNull(resultList);
        // 7499, 7654, 7844 의 jobhist 는 초기데이터에 따라 각 1건 임
        assertEquals(3, resultList.size());
 
        assertEquals(new BigDecimal(7499), resultList.get(0).getEmpNo());
        assertEquals(new BigDecimal(7654), resultList.get(1).getEmpNo());
        assertEquals(new BigDecimal(7844), resultList.get(2).getEmpNo());
 
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1981-02-20"), resultList.get(0).getStartDate());
        assertEquals(sdf.parse("1981-09-28"), resultList.get(1).getStartDate());
        assertEquals(sdf.parse("1981-09-08"), resultList.get(2).getStartDate());
 
    }
```

 위에서 이전에 작성한 CompositeKeyTest 의 쿼리를 실행하여 리스트 형태의 속성을 가지는 복합 객체를 만들었고, 이를 파라메터 객체로 iterate 테스트를 위한 쿼리를 수행하였다.

### iterate property 가 파라메터 객체의 속성 vs. 파라메터 객체 자신일 때 비교

```xml
	..
 
	<!-- parameterClass 는 명시하지 않았음. Map 에 collection 이란 key 로 List 를 넘긴 경우와 바로 List를 넘긴 경우로 구분하여 테스트 -->
	<!-- iterate 요소가 검색조건 등의 입력 파라메터 바인딩 변수로 사용될 경우는 #collection[]# 과 같이 사용하면 됨 -->
	<select id="selectDynamicIterateSimple" resultClass="egovMap">
		select 
			<isPropertyAvailable property="collection">
				<iterate property="collection" conjunction=", ">
					'$collection[]$' as $collection[]$
				</iterate>
			</isPropertyAvailable>
			<!-- List 를 바로 넘긴 경우 -->
			<isNotPropertyAvailable property="collection">
				<iterate conjunction=", ">
					'$[]$' as $[]$
				</iterate>
			</isNotPropertyAvailable>
		from dual
	</select>
```

 collection 이란 속성이 포함됬는지 여부에 따라 iterate 대상이 파라메터 객체의 속성(위에서는 파라메터 객체 내에 collection 이라는 property 로 전달된 리스트) 또는 파라메터 객체 자신(파라메터 객체 자신이 리스트 형태인 경우) 에 대한 iterate 처리 예이다. $property명$ 로 작성된 영역은 #property명# 와 같이 prepared statement 의 바인드 변수로 처리되는 것이 아니라 SQL 문 자체에 텍스트가 replace 되어 처리됨에 유의한다.

### Sample TestCase

```java
..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicIterateSimple() throws Exception {
        // Collection 형의 객체 size 만큼
        List iterateList = new ArrayList();
        iterateList.add("a");
        iterateList.add("b");
        iterateList.add("c");
 
        // select
        Map resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicIterateSimple", iterateList);
 
        // check
        assertNotNull(resultMap);
        assertEquals("a", resultMap.get("a"));
        assertEquals("b", resultMap.get("b"));
        assertEquals("c", resultMap.get("c"));
        assertTrue(!resultMap.containsKey("d"));
 
        // map 안에 collection 이란 property 로 List 를 넣은 경우
        Map map = new HashMap();
        map.put("collection", iterateList);
 
        // select
        resultMap =
            (Map) jobHistDAO.getSqlMapClientTemplate().queryForObject(
                "selectDynamicIterateSimple", map);
 
        // check
        assertNotNull(resultMap);
        assertEquals("a", resultMap.get("a"));
        assertEquals("b", resultMap.get("b"));
        assertEquals("c", resultMap.get("c"));
        assertTrue(!resultMap.containsKey("d"));
 
        // iterate 를 위한 테스트로 Map, Set, Iterator 를 시도해 보았으나 아래 에러를 냄. (List 나 Array 와 같이 index 로 접근 가능해야 하는듯)
        // The 'xxx'(ex. collection) property of the XXX (ex. java.util.HashMap$EntryIterator) class is not a List or
        // Array.
    }
```

 위에서 파라메터 객체 자체를 List 로 전달한 첫번째 경우와 파라메터 객체(Map) 안에 “collection” 이란 key 로 List 를 전달한 두번째 경우의 iterate 태그 처리 차이를 알 수 있을 것이다.

## Nested iterate 연산

 아래의 샘플 sql mapping xml 예를 참고하라.

### Sample iterate 연산

```xml
	..
 
	<select id="selectJobHistListUsingDynamicNestedIterate" parameterClass="map" resultClass="jobHistVO">
		<![CDATA[
			select EMP_NO     as empNo,
			       START_DATE as startDate,
			       END_DATE   as endDate,
			       JOB        as job,
			       SAL        as sal,
			       COMM       as comm,
			       DEPT_NO    as deptNo
			from   JOBHIST
		]]>
		<dynamic prepend="where">
			<iterate property="condition" open="(" conjunction="and" close=")">
				$condition[].columnName$ $condition[].columnOperation$ 
				<isEqual property="condition[].nested" compareValue="true">
					<iterate property="condition[].columnValue" open="(" conjunction="," close=")">
						#condition[].columnValue[]#
					</iterate>
				</isEqual>
				<isNotEqual property="condition[].nested" compareValue="true">
					#condition[].columnValue#
				</isNotEqual>
			</iterate>		
		</dynamic>
			order by EMP_NO, START_DATE
	</select>
```

 복잡한 조건 처리의 예로 일반 비교 연산과 Nested Iterate 처리가 함께 사용되고 있다. 쿼리 호출 시 columnName, columnOperation, columnValue 를 멀티로 넘기며 columnName 과 columnOperation 은 sql 문에 직접 replaced Text 로 처리하고 columnValue 에 대해서는 바인드 변수 처리하며, 이때 nested 로 추가 설정한 값이 true 이면 columnValue 가 in 조건절인 경우로 판단하여 nested iterate 처리하는 예이다. 아래 테스트 케이스에서 파라메터 객체 세팅에 따라 다음 조건절이 동적으로 추가된다.

```bash
where ( DEPT_NO = ? and SAL < ? and JOB in ( ? , ? ) )
```

### Sample TestCase

```java
..
    @SuppressWarnings("unchecked")
    @Test
    public void testDynamicNestedIterate() throws Exception {
        // nested iterate 태그 테스트 - columnName, columnOperation, columnValue 를 Map 형태로 모아 담은 List 를 condition 이란 key 로 파라메터 객체(Map) 에 추가
        // columnValue 가 nested iterate 로 풀려야 하는 경우(ex. in 조건절) nested 'true' 로 추가 설정을 하여 호출함.
        Map map = new HashMap();
        List condition = new ArrayList();
        Map columnMap1 = new HashMap();
        columnMap1.put("columnName", "DEPT_NO");
        columnMap1.put("columnOperation", "=");
        columnMap1.put("columnValue", new BigDecimal(30));
        condition.add(columnMap1);
 
        Map columnMap2 = new HashMap();
        columnMap2.put("columnName", "SAL");
        columnMap2.put("columnOperation", "<");
        columnMap2.put("columnValue", new BigDecimal(3000));
        condition.add(columnMap2);
 
        Map columnMap3 = new HashMap();
        columnMap3.put("columnName", "JOB");
        columnMap3.put("columnOperation", "in");
        List jobList = new ArrayList();
        jobList.add("CLERK");
        jobList.add("SALESMAN");
        columnMap3.put("columnValue", jobList);
        // List 를 nested 로 포함하고 있음을 flag 로 알림
        columnMap3.put("nested", "true");
        condition.add(columnMap3);
 
        map.put("condition", condition);
 
        // select
        List<JobHistVO> resultList =
            jobHistDAO.getSqlMapClientTemplate().queryForList(
                "selectJobHistListUsingDynamicNestedIterate", map);
 
        // check
        assertNotNull(resultList);
 
        // 결과 데이터
        // Empno Startdate Enddate Job Sal Comm Deptno
        // 1 7499 81/02/20 SALESMAN 1600 300 30
        // 2 7521 81/02/22 SALESMAN 1250 500 30
        // 3 7654 81/09/28 SALESMAN 1250 1400 30
        // cf.) 7698 81/05/01 MANAGER 2850 30 데이터는 in 조건절에 JOB 이 'MANAGER' 인 것이 없기 때문에 nested 안에서 필터링 됨.
        // 4 7844 81/09/08 SALESMAN 1500 0 30
        // 5 7900 83/01/15 CLERK 950 30
        assertEquals(5, resultList.size());
        assertEquals(new BigDecimal(7499), resultList.get(0).getEmpNo());
        assertEquals(new BigDecimal(7521), resultList.get(1).getEmpNo());
        assertEquals(new BigDecimal(7654), resultList.get(2).getEmpNo());
        assertEquals(new BigDecimal(7844), resultList.get(3).getEmpNo());
        assertEquals(new BigDecimal(7900), resultList.get(4).getEmpNo());
 
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1981-02-20"), resultList.get(0).getStartDate());
        assertEquals(sdf.parse("1981-02-22"), resultList.get(1).getStartDate());
        assertEquals(sdf.parse("1981-09-28"), resultList.get(2).getStartDate());
        assertEquals(sdf.parse("1981-09-08"), resultList.get(3).getStartDate());
        assertEquals(sdf.parse("1983-01-15"), resultList.get(4).getStartDate());
 
    }
```

 지금까지 살펴본 바에서 확인할 수 있듯이 iBATIS 의 Dynamic 요소를 사용하여 매우 복잡한 조건 처리도 가능하다. 그러나 조건 처리가 복잡한 경우 dynamic 태그 영역을 쉽게 알아보기 어렵고 단순 논리/산술 연산 수준의 태그로 감당하기 어려운 복잡한 요구사항에 완벽하게 대응하기는 미비한 점이 존재한다. iBATIS 차후 버전에서는 좀더 유연하고 강력한 Dynamic 처리가 가능해질 걸로 보인다.