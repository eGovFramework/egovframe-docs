# Mapper XML File

 MyBatis Mapper XML (SQL Mapping XML) File은 실행할 SQL문을 정의해놓은 파일로서,

 SQL문 실행을 위해 Parameter Object를 받아오거나 SQL문 실행 결과를 Result Obejct에 자동 바인딩하는 기능 등을 제공한다.

 다음은 MyBatis Mapper XML File에서 사용할 수 있는 요소와 속성에 관한 설명이다.

## Mapper XML (SQL Mapping XML)

 Mapper XML File에는 다음과 같은 요소들을 사용할 수 있다.

- <select> : 매핑된 SELECT 구문
- <insert> : 매핑된 INSERT 구문
- <update> : 매핑된 UPDATE 구문
- <delete> : 매핑된 DELETE 구문
- <sql> : 다른 구문에서 재사용하기 위한 SQL 조각
- <resultMap> : 데이터베이스 결과 데이터를 객체에 매핑하는 방법을 정의
- <cache> : 자신의 namespace를 위한 캐시설정
- <cache-ref> : 다른 namespace의 캐시설정을 참조

### Sample Configuration

```bash
 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
 
<mapper namespace="egovframework.rte.psl.dataaccess.DeptMapper"> -- MyBatis에서는 namespace를 필수로 설정해야함
 
	<resultMap id="deptResult" type="egovframework.rte.psl.dataaccess.vo.DeptVO"> -- [주의] iBatis의 class속성 -> type속성으로 변경
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
	</resultMap>
 
	<select id="selectDept" parameterType="int" resultMap="deptResult"> -- [주의] iBatis의 parameterClass속성 -> parameterType속성으로 변경
		<![CDATA[
			select DEPT_NO,DEPT_NAME,LOC
			from   DEPT
			where  DEPT_NO = #{deptNo}
		]]>
	</select>
 
	<insert id="insertDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			insert into DEPT
			           (DEPT_NO,DEPT_NAME,LOC)
			values     (#{deptNo},#{deptName},#{loc})
		]]>
	</insert>
 
	<update id="updateDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			update DEPT
			set    DEPT_NAME = #{deptName},
			       LOC = #{loc}
			where  DEPT_NO = #{deptNo}
		]]>
	</update>
 
	<delete id="deleteDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			delete from DEPT
			where       DEPT_NO = #{deptNo}
		]]>
	</delete>
 
</mapper>
```

### <select>

 **&lt;select&gt;는 SELECT문을 작성할 때 사용되는 요소**로, 데이터베이스에서 조회한 결과를 오브젝트에 매핑하는 역할을 한다.

 먼저 &lt;select&gt; 요소에서 사용 가능한 속성들에 대해 알아보고, 위 샘플코드에서 언급된 &lt;select&gt; 설정을 자세히 살펴본다.

- **속성**

| 속성 | 설명 |
| --- | --- |
| **id** | **해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)** |
| **parameterType** | **해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭** |
| parameterMap | <select> 외부에 정의된 Parameter Object(<parameterMap>)를 참조하는 방법, 권장하지 않는다. parameterType 속성이나 Inline Parameter를 권장 |
| **resultType** | **해당 구문이 리턴하는 타입의 패키지 경로를 포함한 전체 클래스명이나 별칭** |
| **resultMap** | **<select> 외부에 정의된 Result Object(<resultMap>)를 참조하는 방법** |
| flushCache | 이 속성값이 true이면, 구문이 호출될때마다 캐시가 지원진다. (default: false) |
| useCache | 이 속성값이 true이면, 구문의 결과가 캐시된다. (default: true) |
| timeout | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대시간 (드라이버에 따라 다소 지원되지 않을 수 있다) |

- **기본예제**

```bash
	<select id="selectDept" parameterType="int" resultMap="deptResult">
		<![CDATA[
			select DEPT_NO,
			       DEPT_NAME,
			       LOC
			from   DEPT
			where  DEPT_NO = #{deptNo} -- 파라미터 바인딩 표기법 #{property}
		]]>
	</select>
```

 위의 &lt;select&gt; 구문은 'selectDept'를 이용하여 호출하며, 'int' 타입의 파라미터를 받아와 WHERE절 조건식에 바인딩하고,

 SELECT 결과를 'deptResult'라는 이름을 가진 &lt;resultMap&gt; 설정에 따라 오브젝트에 매핑하여 리턴한다.

 &lt;resultMap id=“deptResult” … /&gt;형태로 &lt;select&gt; 외부에 정의되어 있다.

### <insert>, <update>, <delete>

 **&lt;insert&gt;, &lt;update&gt;, &lt;delete&gt;는 INSERT, UPDATE, DELETE문을 작성할 때 사용되는 요소**로, 필요한 파라미터를 전달받아 데이터베이스의 데이터를 변경하는 역할을 한다.

 먼저 &lt;insert&gt;, &lt;update&gt;, &lt;delete&gt; 요소에서 사용 가능한 속성들에 대해 알아보고, 위 샘플코드에서 언급된 &lt;insert&gt;, &lt;update&gt;, &lt;delete&gt; 설정을 각각 살펴본다.

 **1\. &lt;insert&gt;**

- **속성**

| 속성 | 설명 |
| --- | --- |
| **id** | **해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)** |
| **parameterType** | **해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭** |
| flushCache | 이 속성값이 true이면, 구문이 호출될때마다 캐시가 지원진다. (default: false) |
| timeout | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대시간 (드라이버에 따라 다소 지원되지 않을 수 있다) |
| statementType | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis 에게 Statement, PreparedStatement 또는 CallableStatement 를 사용하게 한다. (default: PREPARED) |
| useGeneratedKeys | DB 내부에서 생성한 키를 받는 JDBC getGeneratedKeys 메서드를 사용하도록 설정 (default: false) |
| keyProperty | getGeneratedKeys 메서드나 insert 구문의 selectKey 하위 요소에 의해 리턴된 키를 셋팅할 프로퍼티를 지정 |
| keyColumn | 생성키를 가진 테이블의 칼럼명을 셋팅, 키 칼럼이 테이블이 첫번째 칼럼이 아닌 데이터베이스(PostgreSQL 처럼)에서만 필요 |

- **기본예제**

```bash
	<insert id="insertDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			insert into DEPT (DEPT_NO,DEPT_NAME,LOC)
			values (#{deptNo},#{deptName},#{loc}) -- 파라미터 바인딩 표기법 #{property}
		]]>
	</insert>
```

 위의 &lt;insert&gt; 구문은 'insertDept'를 이용하여 호출하며, 'egovframework.rte.psl.dataaccess.vo.DeptVO' 타입의 파라미터를 받아와 INSERT절에 바인딩한다.

 **2\. &lt;update&gt;**

- **속성**

| 속성 | 설명 |
| --- | --- |
| **id** | **해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)** |
| **parameterType** | **해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭** |
| flushCache | 이 속성값이 true이면, 구문이 호출될때마다 캐시가 지원진다. (default: false) |
| timeout | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대시간 (드라이버에 따라 다소 지원되지 않을 수 있다) |
| statementType | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis 에게 Statement, PreparedStatement 또는 CallableStatement 를 사용하게 한다. (default: PREPARED) |

- **기본예제**

```bash
	<update id="updateDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			update DEPT
			set    DEPT_NAME = #{deptName}, -- 파라미터 바인딩 표기법 #{property}
			       LOC = #{loc}
			where  DEPT_NO = #{deptNo}
		]]>
	</update>
```

 위의 &lt;update&gt; 구문은 'updateDept'를 이용하여 호출하며, 'egovframework.rte.psl.dataaccess.vo.DeptVO' 타입의 파라미터를 받아와 UPDATE절에 바인딩한다.

 **3\. &lt;delete&gt;**

- **속성**

| 속성 | 설명 |
| --- | --- |
| **id** | **해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)** |
| **parameterType** | **해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭** |
| flushCache | 이 속성값이 true이면, 구문이 호출될때마다 캐시가 지원진다. (default: false) |
| timeout | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대시간 (드라이버에 따라 다소 지원되지 않을 수 있다) |
| statementType | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis 에게 Statement, PreparedStatement 또는 CallableStatement 를 사용하게 한다. (default: PREPARED) |

- **기본예제**

```bash
	<delete id="deleteDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			delete from DEPT
			where DEPT_NO = #{deptNo} -- 파라미터 바인딩 표기법 #{property}
		]]>
	</delete>
```

 위의 &lt;delete&gt; 구문은 'deleteDept'를 이용하여 호출하며, 'egovframework.rte.psl.dataaccess.vo.DeptVO' 타입의 파라미터를 받아와 WHERE절에 바인딩한다.

 **\[참고\]**

 parameterType에 지정한 전체 클래스명이 복잡하다면, 해당 클래스타입에 대한 Alias(별칭)로 대체할 수 있다.

```bash
	<!--In MyBatis Configuration XML File -->
	<typeAlias type="egovframework.rte.psl.dataaccess.vo.DeptVO" alias="deptVO" />
 
	<!-- Mapper XML File -->
	<delete id="deleteDept" parameterType="deptVO">
		<![CDATA[
			delete from DEPT
			where DEPT_NO = #{deptNo} -- 파라미터 바인딩 표기법 #{property}
		]]>
	</delete>
```

### <sql>

 **&lt;sql&gt; 요소는 다른 구문에서 재사용 가능한 SQL구문을 정의**할 때 사용한다.

 &lt;include refid=”&lt;sql&gt;의 ID값” /&gt; 설정을 통해 재사용할 수 있다.

- **기본예제**

```bash
	<sql id="userColumns"> id,username,password </sql>
 
	<select id="selectUsers" resultType="map">
		<![CDATA[
			select <include refid="userColumns"/>
			from some_table
			where id = #{id}
		]]>
	</select>
```

### Parameters

 예제 코드에서 파라미터를 전달하는 간단한 구문을 살펴보도록 하겠다.

```bash
 
	<insert id="insertDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
		<![CDATA[
			insert into DEPT
			           (DEPT_NO,
			            DEPT_NAME,
			            LOC)
			values     (#{deptNo},
			            #{deptName},
			            #{loc})
		]]>
	</insert>
```

 위에서 egovframework.rte.psl.dataaccess.vo.DeptVO 클래스 타입의 객체가 mapper 오브젝트를 통해 전달될 경우 해당 객체의 deptNo, deptName, loc 를 찾아서 PreparedStatement 파라미터로 전달된다.

 추가적으로 파라미터 전달 시 파라미터에 다음과 같은 형태로 데이터 타입을 명시할 수 있다. #{property,javaType=int,jdbcType=NUMERIC}

### <resultMap>

 **&lt;resultMap&gt;는 SELECT 조회 결과값을 오브젝트에 매핑하기 위해 사용하는 요소**로, ResultSet 에서 데이터를 가져올 때 필요한 JDBC 코드를 대신한다.

- **속성**

| 속성 | 설명 |
| --- | --- |
| **id** | Statement에서 resultMap을 참조하기 위한 유일한 식별자 |
| **type** | 구문이 리턴한 결과를 매핑할 오브젝트 타입의 패키지 경로를 포함한 전체 클래스명이나 별칭 |

- **기본예제**

```bash
	<!-- In MyBatis Configuration XML File -->
	<!-- <typeAlias type="egovframework.rte.psl.dataaccess.vo.DeptVO" alias="deptVO" /> -->
 
	<resultMap id="deptResult" type="egovframework.rte.psl.dataaccess.vo.DeptVO">
	<!-- DeptVO 클래스를 typeAlias로 정의한 경우, <resultMap id="deptResult" type="deptVO"> 도 가능 -->
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
	</resultMap>
 
	<select id="selectDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO" resultMap="deptResult">
		<![CDATA[
			select DEPT_NO,DEPT_NAME,LOC
			from   DEPT
			where  DEPT_NO = #{deptNo}
		]]>
	</select>
```

 SELECT문 결과값은 &lt;select&gt;에 지정한 **resultMap 속성값에 따라 &lt;resultMap id=“deptResult”&gt;에 매핑**되어 리턴된다.

 또는 다음과 같이 &lt;select&gt;에서 **resultMap 속성 대신 resultType 속성을 사용**하여 결과값을 매핑할 클래스 타입을 지정할 수도 있다.

 단, 아래와 같이 resultType 속성을 이용하는 경우에는 DB 컬럼명과 프로퍼티명이 동일해야한다.

```bash
	<select id="selectDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO" resultType="egovframework.rte.psl.dataaccess.vo.DeptVO ">
	<!-- DeptVO 클래스를 typeAlias로 정의한 경우, <select id="selectDept" parameterType="deptVO" resultType="deptVO">도 가능 -->	
		<![CDATA[
			select deptno,deptname,loc
			from   DEPT
			where  deptno= #{deptno}
		]]>
	</select>
```

 위의 두 코드는 SELECT문의 칼럼명과 Result Object(DeptVO)의 프로퍼티명을 비교하여 일치하는 프로퍼티의 setter를 찾아 결과값을 매핑한다.

- **DB컬럼명과 프로퍼티명이 다를 경우**

```bash
	<!-- 1) resultType 속성 사용 시 -->
	<select id="selectDept" resultType="deptVO">
		<![CDATA[
			select
				DEPT_NO     as "deptNo",
				DEPT_NAME   as "deptName",
				LOC         as "loc"
			from DEPT
			where DEPT_NO = #{deptNo}
		]]>
	</select>
 
	<!-- 2) <resultMap> 사용 시 -->
	<resultMap id="deptResult" type="deptVO">
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
	</resultMap>
 
	<select id="selectDept" parameterType="deptVO" resultMap="deptResult">
		<![CDATA[
			select DEPT_NO,DEPT_NAME,LOC
			from   DEPT
			where  DEPT_NO = #{deptNo}
		]]>
	</select>
```

 1)번의 경우, 컬럼 Alias를 이용하여 프로퍼티명과 일치시킨다.

 2)번의 경우, &lt;resultMap&gt;의 하위요소인 &lt;result&gt;을 이용하여 명시적으로 property명과 column명을 일치시킨다.

 \[참고\] ResultSet 처리를 위해 hashmap등을 사용하여 키 형태로 매핑하여 결과를 받아올 수있으나, 좋지 않은 방법이므로 resultMap의 도메인 모델로는 자바빈이나 POJO를 사용한다.

### <cache>

 MyBatis 는 쉽게 설정가능하고 변경가능한 쿼리 캐싱 기능을 가지고 있다. MyBatis 3 캐시 구현체는 좀더 쉽게 설정할 수 있도록 많은 부분이 수정되었다.

 성능을 개선하고 순환하는 의존성을 해결하기 위해 필요한 로컬 세션 캐싱을 제외하고 기본적으로 캐시가 작동하지 않는다. 캐싱을 활성화하기 위해서, SQL 매핑 파일에 다음 한줄을 추가하면 된다.

- **<cache/>**
- 디폴트 설정내용

- 매핑 파일 내의 모든 <select> 구문의 결과는 cache된다.
- 매핑 파일 내의 모든 <insert>, <update>, <delete> 구문이 호출될 때 cache를 flush한다.

 이 외에 cache 설정에 대해서는 MyBatis 매뉴얼을 참고하시길 바랍니다.

### <cache-ref>

 MyBatis 에서는 이전 섹션 내용을 돌이켜보면서, 특정 명명공간을 위한 캐시는 오직 하나만 사용되거나 같은 명명공간내에서는 구문마다 캐시를 지울수 있다.

 명명공간간의 캐시 설정과 인스턴스를 공유하고자 할때가 있을 것이다.

 이 경우 cache-ref 요소를 사용해서 다른 캐시를 참조할 수 있다.

- <cache-ref namespace=”com.someone.application.data.SomeMapper” />