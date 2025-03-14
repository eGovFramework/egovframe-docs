---
title: Mapper Dynamic SQL
linkTitle: "Dynamic SQL"
description: MyBatis는 다양한 조건에 따라 동적으로 SQL을 생성할 수 있는 강력한 동적 SQL 기능을 제공하며, OGNL 기반의 표현식을 통해 유연하고 편리하게 사용할 수 있다. 이는 iBatis보다 간단하고 직관적인 방식으로 동적 SQL 처리를 가능하게 한다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis/dataaccess-mybatis-dynamic-sql/
menu:
    depth:
        name: Dynamic SQL
        weight: 5
        parent: mybatis
---
# Dynamic SQL

일반적으로 JDBC API를 사용한 코딩에서 다양한 조건에 따라 다양한 형태의 쿼리의 실행이 필요한 경우가 존재하며 이에 MyBatis는 강력한 동적 SQL 언어를 제공한다.

MyBatis는 SQL 문의 동적인 변경에 대해 iBatis보다 상대적으로 유연하다.<br>
iBatis도 다양한 Dynamic 요소를 제공하였으나 이해해야 하는 요소들이 많았다.

MyBatis에서 제공하는 동적 SQL 요소들은 JSTL이나 XML 기반의 텍스트 프로세서와 유사한 형태로 제공되며 OGNL 기반의 표현식을 제공함으로써 보다 유연하고 편리하게 Dynamic 요소를 사용할 수 있다.

## 기본 Dynamic 요소 사용 방법

### Sample Dynamic SQL mapper xml

MyBatis에서 제공하는 Dynamic 요소의 기본적인 형태에 대해 알아보도록 한다.<br>
아래 Sql 매퍼 파일은 파라미터 객체의 empNo 속성의 값 유무에 따라 `where EMP_NO = #{empNo}` 조건절을 동적으로 추가/제거할 수 있는 예이다.

```xml
	<select id="selectJobHistListUsingDynamicElement" parameterType="egovframework.rte.psl.dataaccess.vo.JobHistVO" resultMap="egovframework.rte.psl.dataaccess.vo.JobHistVO">
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
		<where>
			<if test="empNo != null">
				EMP_NO = #{empNo}				
			</if>		
		</where>
	</select>
```

where 요소는 태그에 의해 콘텐츠가 리턴되면 단순히 “WHERE” 만을 추가한다. 하지만 하위 요소의 조건이 하나라도 만족하지 않으면 추가되지 않는다.<br>
또한 콘텐츠가 “AND” 나 “OR”로 시작한다면, 그 “AND” 나 “OR”를 지워버리는 점에 유념하여 사용하도록 한다.

### if

if는 가장 많이 사용되는 Dynamic 요소로 문자열을 선택적으로 검색하는 기능을 제공한다.<br>
where 절 안에 사용되며 if 안에 해당 값이 존재하지 않으면 모든 결과값이 리턴된다.

```xml
        ..
	<select id="selectEmployerList" parameterType="egovframework.rte.psl.dataaccess.vo.EmpVO" resultType="egovframework.rte.psl.dataaccess.vo.EmpVO">
		<![CDATA[
			select
				EMP_NO as empNo,
				EMP_NAME as empName,
				JOB as job,
				MGR as mgr,
				HIRE_DATE as hireDate,
				SAL as sal,
				COMM as comm,
				DEPT_NO as deptNo
			from EMP
		]]>
		<where>
			<if test="empNo != null">
				EMP_NO = #{empNo}
			</if>
			<if test="empName != null">
				EMP_NAME LIKE '%' || #{empName} || '%'
			</if>
		</where>
	</select>
```
전달된 인자의 특정 property에 대해 if로 비교하는 경우가 가장 많이 사용된다.

### choose (when, otherwise)

모든 조건을 적용하는 대신 한 가지 조건 만을 적용해야 할 필요가 있는 경우 MyBatis에서 제공하는 choose 요소를 사용하며 이는 자바의 switch 구문과 유사한 개념이다.

아래 예제를 보면 지금은 MGR 정보만으로 검색하고, EMP 정보가 있다면 그 값으로 검색된다.<br>
두 가지 값을 모두 제공하지 않는다면 HIRE 상태인 Employee 정보가 리턴될 것이다.

```xml
	<select id="selectEmployeeList" parameterType="egovframework.rte.psl.dataaccess.vo.EmpVO" resultType="egovframework.rte.psl.dataaccess.vo.EmpVO">
		SELECT * FROM EMP WHERE JOB = 'Engineer'
		<choose>
			<when test="mgr ! null">
				AND MGR like #{mgr}
			</when>
			<when test="empNo ! null and empName ! =null">
				AND EMP_NAME like #{empName}
			</when>
			<otherwise>
				AND HIRE_STATUS = 'Y'
			</otherwise>
		</choose>
	</select>
```

### trim (where, set)

아래 예제의 `<trim prefix=“WHERE” prefixOverrides=“AND|OR”>`은 `<where>`와 동일하게 동작한다. 즉, where 요소에 대한 trim 기능을 제공한다.

```xml
	..
	<select id="selectEmployerList" parameterType="egovframework.rte.psl.dataaccess.vo.EmpVO"
		resultType="egovframework.rte.psl.dataaccess.vo.EmpVO">
		<![CDATA[
			select
				EMP_NO as empNo,
				EMP_NAME as empName,
				JOB as job,
				MGR as mgr,
				HIRE_DATE as hireDate,
				SAL as sal,
				COMM as comm,
				DEPT_NO as deptNo
			from EMP
		]]>
		<trim prefix="WHERE" prefixOverrides="AND|OR ">
			<if test="empNo != null">
				EMP_NO = #{empNo}
			</if>
			<if test="empName != null">
				EMP_NAME LIKE '%' || #{empName} || '%'
			</if>
		</trim>
	</select>
```

### foreach
아래의 샘플 sql mapper xml 예를 참고하라. 일반적으로 iterate 태그 처리에 가장 많이 사용되는 in 조건절 처리 예이다.

foreach 요소는 매우 강력한 기능을 제공하는데 그중 하나가 collection을 명시하는 것을 허용하는 것이다.<br>
foreach 요소에서는 item, index 두 가지 변수를 선언하며, 이 요소는 열고 닫는 문자열로 명시할 수 있고 반복 간에 둘 수 있는 구분자도 추가 가능하다.

```xml
	<select id="selectJobHistListUsingDynamicNestedIterate" parameterType="egovframework.rte.psl.dataaccess.util.EgovMap" resultMap="jobHistVO">
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
			where
			<foreach collection="condition" item="item" open="(" separator="and" close=")">
				${item.columnName} ${item.columnOperation} 
				<if test="item.nested == 'true'">
					<foreach item="item" index="index" collection="item.columnValue" open="(" separator="," close=")">
					      '${item}'
					</foreach>
				</if>
				<if test="item.nested != 'true'">
					#{item.columnValue}
				</if>
			</foreach>		
			order by EMP_NO, START_DATE
	</select>
```
