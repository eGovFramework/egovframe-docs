---
title: Mapper XML Files
linkTitle: "Mapper XML Files"
description: MyBatis Mapper XML 파일은 SQL문을 정의하고, Parameter Object를 받아 SQL문을 실행하며, 그 결과를 Result Object에 자동으로 바인딩하는 기능을 제공한다. 이를 통해 SQL 실행과 데이터 매핑을 쉽게 처리할 수 있다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis/dataaccess-mapper_xml_files/
menu:
    depth:
        name: Mapper XML Files
        weight: 4
        parent: mybatis
---
# Mapper XML File

MyBatis Mapper XML (SQL Mapping XML) File은 실행할 SQL문을 정의해놓은 파일로서,  
SQL문 실행을 위해 Parameter Object를 받아오거나 SQL문 실행 결과를 Result Object에 자동 바인딩하는 기능 등을 제공한다.

## Mapper XML (SQL Mapping XML)

Mapper XML File에는 다음과 같은 요소들을 사용할 수 있다.

- **`<select>`**: 매핑된 SELECT 구문
- **`<insert>`**: 매핑된 INSERT 구문
- **`<update>`**: 매핑된 UPDATE 구문
- **`<delete>`**: 매핑된 DELETE 구문
- **`<sql>`**: 다른 구문에서 재사용하기 위한 SQL 조각
- **`<resultMap>`**: 데이터베이스 결과 데이터를 객체에 매핑하는 방법을 정의
- **`<cache>`**: 자신의 namespace를 위한 캐시설정
- **`<cache-ref>`**: 다른 namespace의 캐시설정을 참조

### Sample Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="egovframework.rte.psl.dataaccess.DeptMapper"> <!-- MyBatis에서는 namespace를 필수로 설정해야함 -->

    <resultMap id="deptResult" type="egovframework.rte.psl.dataaccess.vo.DeptVO"> <!-- [주의] iBatis의 class속성 -> type속성으로 변경 -->
        <result property="deptNo" column="DEPT_NO" />
        <result property="deptName" column="DEPT_NAME" />
        <result property="loc" column="LOC" />
    </resultMap>

    <select id="selectDept" parameterType="int" resultMap="deptResult"> <!-- [주의] iBatis의 parameterClass속성 -> parameterType속성으로 변경 -->
        <![CDATA[
            select DEPT_NO, DEPT_NAME, LOC
            from DEPT
            where DEPT_NO = #{deptNo}
        ]]>
    </select>

    <insert id="insertDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
        <![CDATA[
            insert into DEPT
                       (DEPT_NO, DEPT_NAME, LOC)
            values     (#{deptNo}, #{deptName}, #{loc})
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
### `<select>`

**`<select>`는 SELECT문을 작성할 때 사용되는 요소**로, 데이터베이스에서 조회한 결과를 오브젝트에 매핑하는 역할을 한다.

먼저 `<select>` 요소에서 사용 가능한 속성들에 대해 알아보고, 위 샘플코드에서 언급된 `<select>` 설정을 자세히 살펴보자.

- 속성

| 속성            | 설명                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------|
| `id`           | 해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)                        |
| `parameterType`| 해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭                             |
| `parameterMap` | `<select>` 외부에 정의된 Parameter Object(`<parameterMap>`)를 참조하는 방법, 권장하지 않음. `parameterType` 속성이나 Inline Parameter를 권장 |
| `resultType`   | 해당 구문이 리턴하는 타입의 패키지 경로를 포함한 전체 클래스명이나 별칭                               |
| `resultMap`    | `<select>` 외부에 정의된 Result Object(`<resultMap>`)를 참조하는 방법                                |
| `flushCache`   | 이 속성값이 true이면, 구문이 호출될 때마다 캐시가 지원됨 (default: false)                           |
| `useCache`     | 이 속성값이 true이면, 구문의 결과가 캐시됨 (default: true)                                          |
| `timeout`      | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대 시간 (드라이버에 따라 다소 지원되지 않을 수 있음) |

- 기본 예제

```xml
<select id="selectDept" parameterType="int" resultMap="deptResult">
    <![CDATA[
        select DEPT_NO,
               DEPT_NAME,
               LOC
        from DEPT
        where DEPT_NO = #{deptNo} <!-- 파라미터 바인딩 표기법 #{property} -->
    ]]>
</select>
```


위의 `<select>` 구문은 'selectDept'를 이용하여 호출하며, 'int' 타입의 파라미터를 받아와 WHERE절 조건식에 바인딩하고,  
SELECT 결과를 'deptResult'라는 이름을 가진 `<resultMap>` 설정에 따라 오브젝트에 매핑하여 리턴한다.

`<resultMap id="deptResult" ... />` 형태로 `<select>` 외부에 정의되어 있다.

## `<insert>, <update>, <delete>`

**`<insert>`, `<update>`, `<delete>`는 각각 INSERT, UPDATE, DELETE문을 작성할 때 사용되는 요소**로, 필요한 파라미터를 전달받아 데이터베이스의 데이터를 변경하는 역할을 한다.

먼저 `<insert>`, `<update>`, `<delete>` 요소에서 사용 가능한 속성들에 대해 알아보고, 위 샘플코드에서 언급된 설정을 각각 살펴보겠습니다.

### 1. `<insert>`

#### 속성

| 속성               | 설명                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------|
| `id`              | 해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)                         |
| `parameterType`   | 해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭                                |
| `flushCache`      | 이 속성값이 true이면, 구문이 호출될 때마다 캐시가 지원됨 (default: false)                               |
| `timeout`         | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대 시간 (드라이버에 따라 다소 지원되지 않을 수 있음) |
| `statementType`   | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis에게 Statement, PreparedStatement 또는 CallableStatement를 사용하게 함 (default: PREPARED) |
| `useGeneratedKeys`| DB 내부에서 생성한 키를 받는 JDBC `getGeneratedKeys` 메서드를 사용하도록 설정 (default: false)       |
| `keyProperty`     | `getGeneratedKeys` 메서드나 INSERT 구문의 `selectKey` 하위 요소에 의해 리턴된 키를 셋팅할 프로퍼티를 지정 |
| `keyColumn`       | 생성키를 가진 테이블의 칼럼명을 셋팅 (키 칼럼이 테이블의 첫번째 칼럼이 아닐 경우 필요)                   |

- 기본 예제

```xml
<insert id="insertDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
    <![CDATA[
        insert into DEPT (DEPT_NO, DEPT_NAME, LOC)
        values (#{deptNo}, #{deptName}, #{loc}) <!-- 파라미터 바인딩 표기법 #{property} -->
    ]]>
</insert>
```

위의 `<insert>` 구문은 'insertDept'를 이용하여 호출하며, 'egovframework.rte.psl.dataaccess.vo.DeptVO' 타입의 파라미터를 받아와 INSERT 절에 바인딩한다.

## 2. `<update>`

### 속성

| 속성               | 설명                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------|
| `id`              | 해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)                         |
| `parameterType`   | 해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭                                |
| `flushCache`      | 이 속성값이 true이면, 구문이 호출될 때마다 캐시가 지원됨 (default: false)                               |
| `timeout`         | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대 시간 (드라이버에 따라 다소 지원되지 않을 수 있음) |
| `statementType`   | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis에게 Statement, PreparedStatement 또는 CallableStatement를 사용하게 함 (default: PREPARED) |

### 기본 예제

```xml
<update id="updateDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
    <![CDATA[
        update DEPT
        set    DEPT_NAME = #{deptName}, <!-- 파라미터 바인딩 표기법 #{property} -->
               LOC = #{loc}
        where  DEPT_NO = #{deptNo}
    ]]>
</update>
```

위의 <update> 구문은 'updateDept'를 이용하여 호출하며, 'egovframework.rte.psl.dataaccess.vo.DeptVO' 타입의 파라미터를 받아와 UPDATE절에 바인딩한다.

## 3. `<delete>`

- 속성

| 속성               | 설명                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------|
| `id`              | 해당 구문을 호출할 때 사용되는 값으로, 각 SQL문을 구분하는 유일한 식별자 (필수)                         |
| `parameterType`   | 해당 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭                                |
| `flushCache`      | 이 속성값이 true이면, 구문이 호출될 때마다 캐시가 지원됨 (default: false)                               |
| `timeout`         | 예외가 던져지기 전에 데이터베이스의 요청 결과를 기다리는 최대 시간 (드라이버에 따라 다소 지원되지 않을 수 있음) |
| `statementType`   | STATEMENT / PREPARED / CALLABLE 중 선택, MyBatis에게 Statement, PreparedStatement 또는 CallableStatement를 사용하게 함 (default: PREPARED) |

- 기본 예제

```xml
<delete id="deleteDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO">
    <![CDATA[
        delete from DEPT
        where DEPT_NO = #{deptNo} -- 파라미터 바인딩 표기법 #{property}
    ]]>
</delete>
```

위의 `<delete>` 구문은 `deleteDept`를 이용하여 호출하며, `egovframework.rte.psl.dataaccess.vo.DeptVO` 타입의 파라미터를 받아와 WHERE절에 바인딩한다.

### 참고
parameterType에 지정한 전체 클래스명이 복잡하다면, 해당 클래스타입에 대한 Alias(별칭)로 대체할 수 있다.

```xml
<!-- In MyBatis Configuration XML File -->
<typeAlias type="egovframework.rte.psl.dataaccess.vo.DeptVO" alias="deptVO" />

<!-- Mapper XML File -->
<delete id="deleteDept" parameterType="deptVO">
    <![CDATA[
        delete from DEPT
        where DEPT_NO = #{deptNo} -- 파라미터 바인딩 표기법 #{property}
    ]]>
</delete>
```

### `<sql>`
**`<sql>` 요소는 다른 구문에서 재사용 가능한 SQL구문을 정의**할 때 사용한다.

<include refid="<sql의 ID값>" /> 설정을 통해 재사용할 수 있다.

- 기본예제
```xml
<sql id="userColumns"> id, username, password </sql>

<select id="selectUsers" resultType="map">
    <![CDATA[
        select <include refid="userColumns"/>
        from some_table
        where id = #{id}
    ]]>
</select>
```

## Parameters
예제 코드에서 파라미터를 전달하는 간단한 구문을 살펴보도록 하겠다.

```xml
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


위에서 egovframework.rte.psl.dataaccess.vo.DeptVO 클래스 타입의 객체가 mapper 오브젝트를 통해 전달될 경우 해당 객체의 deptNo, deptName, loc를 찾아서 PreparedStatement 파라미터로 전달된다.

추가적으로 파라미터 전달 시 파라미터에 다음과 같은 형태로 데이터 타입을 명시할 수 있다:

```sql
#{property, javaType=int, jdbcType=NUMERIC}
```
### `<resultMap>`
**`<resultMap>`는 SELECT 조회 결과값을 오브젝트에 매핑하기 위해 사용하는 요소**로, ResultSet에서 데이터를 가져올 때 필요한 JDBC 코드를 대신한다.

- 속성

| **속성** | **설명**                                                                      |
|----------|-------------------------------------------------------------------------------|
| **id**   | Statement에서 resultMap을 참조하기 위한 유일한 식별자                       |
| **type** | 구문이 리턴한 결과를 매핑할 오브젝트 타입의 패키지 경로를 포함한 전체 클래스명이나 별칭 |


- 기본예제

```
<!-- 기본 예제 코드 -->
<resultMap id="deptResult" type="egovframework.rte.psl.dataaccess.vo.DeptVO">
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

SELECT문 결과값은 **`<select>`에 지정한 `resultMap` 속성값에 따라 `<resultMap id="deptResult">`에 매핑**되어 리턴된다.

또는 다음과 같이 `<select>`에서 **`resultMap` 속성 대신 `resultType` 속성을 사용**하여 결과값을 매핑할 클래스 타입을 지정할 수도 있다. 

단, 아래와 같이 `resultType` 속성을 이용하는 경우에는 DB 컬럼명과 프로퍼티명이 동일해야 한다.

```xml
<select id="selectDept" parameterType="egovframework.rte.psl.dataaccess.vo.DeptVO" resultType="egovframework.rte.psl.dataaccess.vo.DeptVO">
    <![CDATA[
        select deptno, deptname, loc
        from   DEPT
        where  deptno = #{deptno}
    ]]>
</select>
```

위의 두 코드는 SELECT문의 칼럼명과 Result Object(DeptVO)의 프로퍼티명을 비교하여 일치하는 프로퍼티의 setter를 찾아 결과값을 매핑한다.

- DB 컬럼명과 프로퍼티명이 다를 경우

```xml
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
```

```xml
<!-- 2) <resultMap> 사용 시 -->
<resultMap id="deptResult" type="deptVO">
    <result property="deptNo" column="DEPT_NO" />
    <result property="deptName" column="DEPT_NAME" />
    <result property="loc" column="LOC" />
</resultMap>

<select id="selectDept" parameterType="deptVO" resultMap="deptResult">
    <![CDATA[
        select DEPT_NO, DEPT_NAME, LOC
        from   DEPT
        where  DEPT_NO = #{deptNo}
    ]]>
</select>
```

1)번의 경우, 컬럼 Alias를 이용하여 프로퍼티명과 일치시킨다.

2)번의 경우, <resultMap>의 하위 요소인 <result>을 이용하여 명시적으로 property명과 column명을 일치시킨다.

[참고] ResultSet 처리를 위해 hashmap 등으로 키 형태로 매핑하여 결과를 받아올 수 있지만, 좋지 않은 방법이므로 resultMap의 도메인 모델로는 자바빈이나 POJO를 사용한다.


## `<cache>`
MyBatis는 쉽게 설정 가능하고 변경 가능한 쿼리 캐싱 기능을 가지고 있다. MyBatis 3 캐시 구현체는 좀 더 쉽게 설정할 수 있도록 많은 부분이 수정되었다.

성능을 개선하고 순환하는 의존성을 해결하기 위해 필요한 로컬 세션 캐싱을 제외하고 기본적으로 캐시가 작동하지 않는다. 캐싱을 활성화하기 위해서, SQL 매핑 파일에 다음 한 줄을 추가하면 된다.


- `<cache/>`
- 디폴트 설정내용
1. 매핑 파일 내의 모든 `<select>` 구문의 결과는 캐시된다.
2. 매핑 파일 내의 모든 `<insert>`, `<update>`, `<delete>` 구문이 호출될 때 캐시가 플러시된다.  

이 외에 캐시 설정에 대해서는 MyBatis 매뉴얼을 참고하시길 바랍니다.

### `<cache-ref>`
MyBatis 에서는 이전 섹션 내용을 돌이켜보면서, 특정 명명공간을 위한 캐시는 오직 하나만 사용되거나 같은 명명공간내에서는 구문마다 캐시를 지울수 있다.

명명공간간의 캐시 설정과 인스턴스를 공유하고자 할때가 있을 것이다.

이 경우 cache-ref 요소를 사용해서 다른 캐시를 참조할 수 있다.

- `<cache-ref namespace=”com.someone.application.data.SomeMapper” />`