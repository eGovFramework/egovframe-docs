---
title: resultMap
linkTitle: "resultMap"
description: resultMap은 SQL 결과를 Java 객체의 속성에 어떻게 매핑할지 상세하게 제어할 수 있는 매핑 요소로, 칼럼 타입 지정, null 값 대체, 타입 핸들러 처리, 복합 객체 매핑 등을 지원한다. 이는 자동 매핑 방식보다 더 복잡한 매핑을 처리할 수 있어 많이 사용된다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-resultMap/
menu:
    depth:
        name: resultMap
        weight: 6
        parent: dataaccess-ibatis
---
# resultMap

 resultMap 은 SQL 문 외부에 정의한 매핑 요소로, result set 으로부터 어떻게 데이터를 뽑아낼지, 어떤 칼럼을 어떤 property로 매핑할지에 대한 상세한 제어를 가능케 해준다. resultMap 은 일반적으로 가장 많이 사용되는 중요한 매핑 요소로 resultClass 속성을 이용한 자동 매핑 접근법에 비교하여 칼럼 타입의 지시, null value 대체값, typeHandler 처리, complex property 매핑(다른 JavaBean, Collections 등을 포함하는 복합 객체) 등을 허용한다.

## 기본 resultMap 사용 방법

 아래의 샘플 resultMap 정의를 참고하라.

### Sample resultMap

```xml
	..
	<typeAlias alias="empVO" type="egovframework.rte.psl.dataaccess.vo.EmpVO" />
 
	<resultMap id="empResult" class="empVO" >
		<result property="empNo" column="EMP_NO" columnIndex="1"
			javaType="decimal" jdbcType="NUMERIC" />
		<result property="empName" column="EMP_NAME" columnIndex="2"
			javaType="string" jdbcType="VARCHAR" />
		<result property="job" column="JOB" columnIndex="3" javaType="string"
			jdbcType="VARCHAR" />
		<result property="mgr" column="MGR" columnIndex="4" javaType="decimal"
			jdbcType="NUMERIC" />
		<result property="hireDate" column="HIRE_DATE" columnIndex="5"
			javaType="date" jdbcType="DATE" />
		<result property="sal" column="SAL" columnIndex="6" javaType="decimal"
			jdbcType="NUMERIC" />
		<result property="comm" column="COMM" columnIndex="7" javaType="decimal"
			jdbcType="NUMERIC" nullValue="0" />
		<result property="deptNo" column="DEPT_NO" columnIndex="8"
			javaType="decimal" jdbcType="NUMERIC" />
	</resultMap>
 
	<select id="selectEmpUsingResultMap" parameterClass="empVO" resultMap="empResult">
		<![CDATA[
			select EMP_NO,
			       EMP_NAME,
			       JOB,
			       MGR,
			       HIRE_DATE,
			       SAL,
			       COMM,
			       DEPT_NO
			from   EMP
			where  EMP_NO = #empNo#
		]]>
	</select>
```

 위 sql 매핑 파일에서 resultMap 요소로 empResult 라는 id 를 부여하고 대상 결과 객체는 EmpVO 를 지정하고 있다. EmpVO 에 대한 상세 attribute (속성) 들에 대해 result 하위 요소로 매핑 정의를 하고 있는데 column 속성으로 result set 에서 얻을 수 있는 select 대상 칼럼(column alias 를 쓴 경우이면 해당 alias 명) 을 매핑하게 된다. 위에서는 추가적으로 columnIndex, javaType, jdbcType 에 대해 명시하였다. 위와 같이 타입을 명확하게 지시해주면 java 의 reflection 기술을 사용하여 대상 클래스의 개별 속성에 대한 type 을 구하는 것보다 성능상 이점이 있을 수 있다. columnIndex 를 지정하는 경우에는 rs.getString(“EMP\_NAME”) → rs.getString(2)로 처리되는 사소한 성능상의 이점이 있지만, 순서의 지정이나 설정 자체의 번거로움으로 추천하지 않는 바이다. 또한 nullValue 속성을 지정한 property 에 대해서는 해당 값이 데이터베이스에서 null 로 읽혔을 때 nullValue 에 지정된 값으로 대체되어 JavaBeans property 에 설정된다. 이 외에도 result 하위 요소의 속성으로 select, resultMap 을 통해 다른 쿼리문의 결과나 complex property 의 처리를 위한 내포 객체에 대한 외부 resultMap 매핑요소를 참조할 수 있다. 또한 typeHandler 속성을 통해 iBATIS 의 기본 처리가 아닌 custom typeHandler 구현체를 지시할 수도 있다.

- resultMap structure

```xml
	<resultMap id="resultMapName" class="some.domain.Class" 
		[extends="parent-resultMap"] [groupBy="some property list"]>
		<result property="propertyName" column="COLUMN_NAME" 
			[columnIndex="1"] [javaType="int"] [jdbcType="NUMERIC"] [nullValue="-999999"]
			[select="someOtherStatement"] [resultMap="someOtherResultMap"]
			[typeHandler="com.mydomain.MyTypehandler"] />
		<result … />
		<result … />
		<result … />
	</resultMap>
```

 위에서 resultMap 태그의 extends 속성을 명시하면 외부에 정의한 다른 resultMap 을 상속(관련 property - column 매핑을 현재 resultMap 에 정의하지 않고도)할 수 있으며, groupBy 속성을 사용하여 nested resultMap 에서의 N+1 쿼리 문제를 풀수 있도록 해당 속성을 통해 명시한 property 리스트의 값이 같은 row 들에 대해 하나의 결과 객체로 생성해 주게 된다.

### Sample TestCase

```java
..
    @Test
    public void testResultMapSelect() throws Exception {
        EmpVO vo = new EmpVO();
        // 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
        vo.setEmpNo(new BigDecimal(7369));
 
        // select
        EmpVO resultVO = empDAO.selectEmp("selectEmpUsingResultMap", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(new BigDecimal(7369), resultVO.getEmpNo());
        assertEquals("SMITH", resultVO.getEmpName());
        assertEquals("CLERK", resultVO.getJob());
        assertEquals(new BigDecimal(7902), resultVO.getMgr());
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1980-12-17"), resultVO.getHireDate());
        assertEquals(new BigDecimal(800), resultVO.getSal());
 
        // nullValue test - <result property="comm" column="COMM" .. nullValue="0" />
        assertEquals(new BigDecimal(0), resultVO.getComm());
        assertEquals(new BigDecimal(20), resultVO.getDeptNo());
    }
```

 위에서 resultMap 을 이용한 결과 객체 매핑을 처리하는 selectEmpUsingResultMap 쿼리문에 대해 조회조건(pk) 를 세팅한 입력 객체를 인자로 조회 처리하고 있는 테스트 케이스이다. 실제로 매핑 파일 내에서 resultMap 을 사용하는 경우와 resultClass 를 그대로 쓰는 경우에서도 어플리케이션 영역은 동일한 형태의 결과 객체를 얻을 수 있지만 sql 매핑 파일내에서 resultMap 의 정의와 사용은 많은 장점이 있으므로 추천된다. 위의 테스트 검증을 통해 EmpVO 의 결과 객체로 조회 결과가 잘 반영되었음을 확인할 수 있고 nullValue 속성으로 지정한 comm attribute 에 대해서는 데이터베이스는 null 이지만 0 에 해당하는 numeric 값으로 대체되어 조회되었음을 확인할 수 있다.

## resultMap 상속

 아래의 샘플 resultMap 정의를 참고하라.

### Sample VO

```java
..
public class EmpExtendsDeptVO extends DeptVO {
 
    private static final long serialVersionUID = -4653117983538108612L;
 
    private BigDecimal empNo;
 
    private String empName;
 
    private String job;
 
    private BigDecimal mgr;
 
    private Date hireDate;
 
    private BigDecimal sal;
 
    private BigDecimal comm;
 
    public BigDecimal getEmpNo() {
        return empNo;
    }
 
    public void setEmpNo(BigDecimal empNo) {
        this.empNo = empNo;
    }
..
```

### Sample resultMap (extends)

```xml
	..
	<typeAlias alias="empExtendsDeptVO" type="egovframework.rte.psl.dataaccess.vo.EmpExtendsDeptVO" />
 
	<!--
		cf.) VO 의 상속관계와 resultMap의 상속관계가 같을 필요는 없음. 아래의 empExtendsDeptResult 가
		empResult (Emp 속성을 가지고 있는 위의 resultMap)를 extends 하고 있지만 실제
		EmpExtendsDeptVO 는 DeptVO 를 extends 하면서 child가 Emp 속성을 가지게끔 define 했음을 볼
		수 있음
	--> 
	<resultMap id="empExtendsDeptResult" class="empExtendsDeptVO" extends="empResult">
		<!--<result property="deptNo" column="DEPT_NO"/>-->
		<result property="deptName" column="DEPT_NAME"/>
		<result property="loc" column="LOC"/>
	</resultMap>
 
	<select id="selectEmpExtendsDeptUsingResultMap" parameterClass="empVO" resultMap="empExtendsDeptResult">
		<![CDATA[
			select EMP_NO,
			       EMP_NAME,
			       JOB,
			       MGR,
			       HIRE_DATE,
			       SAL,
			       COMM,
			       A.DEPT_NO,
			       B.DEPT_NAME,
			       B.LOC
			from   EMP A, DEPT B
			where  A.DEPT_NO = B.DEPT_NO
			and    EMP_NO = #empNo#
		]]>
	</select>
```

 empExtendsDeptResult resultMap 은 위의 기본적인 resultMap 사용 방법에서 정의한 empResult resultMap 을 extends 하고 있으며, 추가적인 deptName, loc 에 대한 property 매핑만을 추가하여 실제로 emp 관련 property 들에 대해서는 extends 하고 있는 매핑 정의를 따라 자동으로 처리가 됨을 확인할 수 있다. resultMap 에 대한 매핑 정의의 상속은 결과 객체 JavaBeans 의 상속 관계와는 상관없이 별개로 이루어진다. (위에서는 VO extends 코드와 resultMap extends 가 반대임)

### Sample TestCase

```java
..
    @Test
    public void testExtendsResultMapSelect() throws Exception {
        EmpVO vo = new EmpVO();
        // 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
        vo.setEmpNo(new BigDecimal(7369));
 
        // select
        EmpExtendsDeptVO resultVO =
            empDAO.selectEmpExtendsDept("selectEmpExtendsDeptUsingResultMap",
                vo);
 
        // check
        assertNotNull(resultVO);
        // resultMap extends test (extends empResult)
        assertEquals(new BigDecimal(7369), resultVO.getEmpNo());
        assertEquals("SMITH", resultVO.getEmpName());
        assertEquals("CLERK", resultVO.getJob());
        assertEquals(new BigDecimal(7902), resultVO.getMgr());
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1980-12-17"), resultVO.getHireDate());
        assertEquals(new BigDecimal(800), resultVO.getSal());
        // nullValue test - <result property="comm" column="COMM" .. nullValue="0" />
        assertEquals(new BigDecimal(0), resultVO.getComm());
        assertEquals(new BigDecimal(20), resultVO.getDeptNo());
 
        assertEquals("RESEARCH", resultVO.getDeptName());
        assertEquals("DALLAS", resultVO.getLoc());
 
    }
```

 위에서 extends 속성을 통해 상위 resultMap 을 상속하는 empExtendsDeptResult resultMap 을 이용한 결과 객체 매핑을 처리하는 selectEmpExtendsDeptUsingResultMap 에 대해 조회 처리하고 있는 테스트 케이스이다. 위의 테스트 검증을 통해 EmpExtendsDeptVO 의 결과 객체로 조회 결과가 잘 반영되었음을 확인할 수 있고 parent resultMap 에 존재하는 nullValue 대체 처리도 잘 반영됨을 확인할 수 있다.

## Simple Composite resultMap

 아래의 샘플 resultMap 정의를 참고하라.

### Sample VO

```java
..
public class EmpDeptSimpleCompositeVO implements Serializable {
 
    private static final long serialVersionUID = -8049578957221741495L;
 
    private BigDecimal empNo;
 
    private String empName;
 
    private String job;
 
    private BigDecimal mgr;
 
    private Date hireDate;
 
    private BigDecimal sal;
 
    private BigDecimal comm;
 
    private BigDecimal deptNo;
 
    private String deptName;
 
    private String loc;
 
    public BigDecimal getEmpNo() {
        return empNo;
    }
 
    public void setEmpNo(BigDecimal empNo) {
        this.empNo = empNo;
    }
..
```

 별도의 parent - child extends 구조를 사용하지 않고 단순히 attributes 를 통합한 VO 이다.

### Sample resultMap

```xml
	..
	<typeAlias alias="empDeptSimpleCompositeVO" type="egovframework.rte.psl.dataaccess.vo.EmpDeptSimpleCompositeVO" />
 
	<resultMap id="empDeptSimpleComposite" class="empDeptSimpleCompositeVO" >
		<result property="empNo" column="EMP_NO"/>
		<result property="empName" column="EMP_NAME"/>
		<result property="job" column="JOB"/>
		<result property="mgr" column="MGR"/>
		<result property="hireDate" column="HIRE_DATE"/>
		<result property="sal" column="SAL"/>
		<result property="comm" column="COMM" nullValue="0"/>
		<result property="deptNo" column="DEPT_NO"/>
		<result property="deptName" column="DEPT_NAME"/>
		<result property="loc" column="LOC"/>
	</resultMap>
 
	<select id="selectEmpDeptSimpleCompositeUsingResultMap" parameterClass="empVO" resultMap="empDeptSimpleComposite">
		<![CDATA[
			select EMP_NO,
			       EMP_NAME,
			       JOB,
			       MGR,
			       HIRE_DATE,
			       SAL,
			       COMM,
			       A.DEPT_NO,
			       B.DEPT_NAME,
			       B.LOC
			from   EMP A, DEPT B
			where  A.DEPT_NO = B.DEPT_NO
			and    EMP_NO = #empNo#
		]]>
	</select>
```

 EMP 와 DEPT 에 대한 조인 쿼리를 통하여 DEPT 정보를 포함하는 결과 row 를 조회하는 쿼리문은 위에서와 완전히 동일하며, extends 를 사용하는 empExtendsDeptResult resultMap 과 비교하여 resultMap 정의가 모든 요소를 포함하고 있다. 위에서는 조회 필드가 결과 객체의 property 가 동일하므로 extends 를 사용하는 resultMap 으로 단순히 resultClass 만 맞춰주어 변경 가능할 것이다.

### Sample TestCase

```java
..
    @Test
    public void testSimpleCompositeResultMapSelect() throws Exception {
        EmpVO vo = new EmpVO();
        // 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
        vo.setEmpNo(new BigDecimal(7369));
 
        // select
        EmpDeptSimpleCompositeVO resultVO =
            empDAO.selectEmpDeptSimpleComposite(
                "selectEmpDeptSimpleCompositeUsingResultMap", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(new BigDecimal(7369), resultVO.getEmpNo());
        assertEquals("SMITH", resultVO.getEmpName());
        assertEquals("CLERK", resultVO.getJob());
        assertEquals(new BigDecimal(7902), resultVO.getMgr());
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1980-12-17"), resultVO.getHireDate());
        assertEquals(new BigDecimal(800), resultVO.getSal());
        // nullValue test - <result property="comm" column="COMM" .. nullValue="0" />
        assertEquals(new BigDecimal(0), resultVO.getComm());
        assertEquals(new BigDecimal(20), resultVO.getDeptNo());
        assertEquals("RESEARCH", resultVO.getDeptName());
        assertEquals("DALLAS", resultVO.getLoc());
 
    }
```

 extends 없이 모든 매핑 요소를 simple 하게 모두 정의한 resultMap 을 이용한 결과 객체 매핑을 처리하는 selectEmpDeptSimpleCompositeUsingResultMap 에 대해 조회 처리하고 있는 테스트 케이스이다. 위의 테스트 검증을 통해 EmpDeptSimpleCompositeV 의 결과 객체로 조회 결과가 잘 반영되었음을 확인할 수 있다.

 위의 비교 구현을 통해 join 조회를 통해 얻어지는 결과 객체가 단순 composite VO 형태인 경우 resultMap extends 을 사용하면 좀더 쉽게 매핑 처리할 수 있을 것으로 보여진다.

## Complex Properties resultMap 사용 방법

 아래의 1:1, 1:N, 1:N(N+1 select), Hierarchical relation 에 대한 샘플 resultMap 정의를 참고하라.

### Complext Properties - (1:1 관계) resultMap

```java

..
public class EmpIncludesDeptVO implements Serializable {
 
    private static final long serialVersionUID = -4113989804152701350L;
 
    private BigDecimal empNo;
 
    private String empName;
 
    private String job;
 
    private BigDecimal mgr;
 
    private Date hireDate;
 
    private BigDecimal sal;
 
    private BigDecimal comm;
 
    private BigDecimal deptNo;
 
    // EMP - DEPT 1:1 relation
    private DeptVO deptVO;
 
    public BigDecimal getEmpNo() {
        return empNo;
    }
 
    public void setEmpNo(BigDecimal empNo) {
        this.empNo = empNo;
    }
..
    public DeptVO getDeptVO() {
        return deptVO;
    }
 
    public void setDeptVO(DeptVO deptVO) {
        this.deptVO = deptVO;
    }
}

```

 위의 EmpIncludesDeptVO 는 DeptVO 를 1:1 관계의 멤버 attribute 로 포함하고 있다.

```xml
<sqlMap namespace="EmpComplexResult">
	..
	<typeAlias alias="empIncludesDeptVO" type="egovframework.rte.psl.dataaccess.vo.EmpIncludesDeptVO" />
 
	<resultMap id="empIncludesDeptResult" class="empIncludesDeptVO">
		<result property="empNo" column="EMP_NO" />
		<result property="empName" column="EMP_NAME" />
		<result property="job" column="JOB" />
		<result property="mgr" column="MGR" />
		<result property="hireDate" column="HIRE_DATE" />
		<result property="sal" column="SAL" />
		<result property="comm" column="COMM" nullValue="0" />
		<result property="deptNo" column="DEPT_NO" />
 
		<!--
			Emp-Dept 1:1 relation
			테스트 결과 resultMap 의 참조 시 sql-map-config.xml 의
			useStatementNamespaces="false" 와 상관없이 namespace prefix 를 써야 하는듯
		-->
		<result property="deptVO" resultMap="EmpComplexResult.getDeptResult" />
	</resultMap>
 
	<resultMap id="getDeptResult" class="deptVO">
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
	</resultMap>
 
	<select id="selectEmpIncludesDeptResultUsingResultMap" parameterClass="empVO" resultMap="empIncludesDeptResult">
		<![CDATA[
			select EMP_NO,
			       EMP_NAME,
			       JOB,
			       MGR,
			       HIRE_DATE,
			       SAL,
			       COMM,
			       A.DEPT_NO as DEPT_NO,
			       B.DEPT_NAME,
			       B.LOC
			from   EMP A, DEPT B
			where  A.DEPT_NO = B.DEPT_NO
			and    EMP_NO = #empNo#
		]]>
	</select>
```

 위 sql 매핑 파일에서 1:1 관계를 표현하는 Complex Properties 를 포함하는 EmpIncludesDeptVO 에 대한 resultMap 매핑 처리 시 해당 객체의 deptVO 멤버 attribute 에 대한 매핑 정의를 위해 resultMap=“EmpComplexResult.getDeptResult” 과 같이 DeptVO 에 대한 외부 resultMap 을 재사용하며 참조하고 있다. iBATIS 는 nested resultMap 에 대한 매핑 정의를 참고하여 join 쿼리에 의한 결과 칼럼을 자동으로 복합 객체(특히 DeptVO 관련 멤버 객체에)에 매핑해 주게 된다.

### Sample TestCase

```java
..
    @Test
    public void testComplexPropertiesOneToOneResultMapSelect() throws Exception {
        EmpVO vo = new EmpVO();
        // 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
        vo.setEmpNo(new BigDecimal(7369));
 
        // select
        EmpIncludesDeptVO resultVO =
            empDAO.selectEmpDeptComplexProperties(
                "selectEmpIncludesDeptResultUsingResultMap", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(new BigDecimal(7369), resultVO.getEmpNo());
        assertEquals("SMITH", resultVO.getEmpName());
        assertEquals("CLERK", resultVO.getJob());
        assertEquals(new BigDecimal(7902), resultVO.getMgr());
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1980-12-17"), resultVO.getHireDate());
        assertEquals(new BigDecimal(800), resultVO.getSal());
        assertEquals(new BigDecimal(0), resultVO.getComm());
        assertEquals(new BigDecimal(20), resultVO.getDeptNo());
        // 1:1 relation included DeptVO
        assertEquals(new BigDecimal(20), resultVO.getDeptVO().getDeptNo());
        assertEquals("RESEARCH", resultVO.getDeptVO().getDeptName());
        assertEquals("DALLAS", resultVO.getDeptVO().getLoc());
    }
```

 위의 테스트 케이스 검증 코드에서 resultVO.getDeptVO().getXXX 와 같이 내포 객체의 각 attribute 가 잘 설정되었음을 확인할 수 있다.

### Complext Properties - (1:N 관계) resultMap

```java
..
public class DeptIncludesEmpListVO implements Serializable {
 
    private static final long serialVersionUID = -3369530755443065377L;
 
    private BigDecimal deptNo;
 
    private String deptName;
 
    private String loc;
 
    private List<EmpVO> empVOList;
 
    public BigDecimal getDeptNo() {
        return deptNo;
    }
 
    public void setDeptNo(BigDecimal deptNo) {
        this.deptNo = deptNo;
    }
..
    public List<EmpVO> getEmpVOList() {
        return empVOList;
    }
 
    public void setEmpVOList(List<EmpVO> empVOList) {
        this.empVOList = empVOList;
    }
}
```

 위의 DeptIncludesEmpListVO 는 EmpVO 의 List 를 1:N 관계의 멤버 attribute 로 포함하고 있다.

```xml
<sqlMap namespace="EmpComplexResult">
	..
	<typeAlias alias="deptIncludesEmpListVO" type="egovframework.rte.psl.dataaccess.vo.DeptIncludesEmpListVO" />
 
	<!-- 1:N 인 경우 groupBy 속성을 명시 -->
	<resultMap id="deptIncludesEmpListResult" class="deptIncludesEmpListVO" groupBy="deptNo">
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
 
		<!-- Dept-EmpList 1:N relation -->
		<result property="empVOList" resultMap="EmpComplexResult.getEmpResult" />
	</resultMap>
 
	<resultMap id="getEmpResult" class="empVO">
		<result property="empNo" column="EMP_NO" />
		<result property="empName" column="EMP_NAME" />
		<result property="job" column="JOB" />
		<result property="mgr" column="MGR" />
		<result property="hireDate" column="HIRE_DATE" />
		<result property="sal" column="SAL" />
		<result property="comm" column="COMM" nullValue="0" />
		<result property="deptNo" column="DEPT_NO" />
	</resultMap>
 
	<select id="selectDeptIncludesEmpListResultUsingResultMap" parameterClass="deptVO" resultMap="deptIncludesEmpListResult">
		<![CDATA[
			select   A.DEPT_NO as DEPT_NO,
			         DEPT_NAME,
			         LOC,
			         EMP_NO,
			         EMP_NAME,
			         JOB,
			         MGR,
			         HIRE_DATE,
			         SAL,
			         COMM
			from     DEPT A,
			         EMP B
			where    A.DEPT_NO = B.DEPT_NO
			         and A.DEPT_NO = #deptNo#
			order by B.EMP_NO
		]]>
	</select>
```

 위 sql 매핑 파일에서 1:N 관계를 표현하는 Complex Properties 를 포함하는 DeptIncludesEmpListVO 에 대한 resultMap 매핑 처리 시 해당 객체의 empVOList 멤버 attribute 에 대한 매핑 정의를 위해 resultMap=“EmpComplexResult.getEmpResult” 과 같이 EmpVO 에 대한 외부 resultMap 을 재사용하며 참조하고 있다. 이때 위의 쿼리에서는 join 에 따라 조회되는 row 수가 1:1 관계와 같이 단건이 아니라 같은 DEPT\_NO 에 대해 복수 개의 결과가 얻어지는데 이에 대한 resultMap 정의 시 groupBy=“deptNo” 을 지정하였으므로 같은 deptNo 인 다건의 EmpVO 에 대한 List 가 복합 객체의 List 멤버 attribute 에 설정되어 얻어진다. iBATIS 는 nested resultMap 에 대한 매핑 정의를 참고하여 join 쿼리에 의한 결과 칼럼을 자동으로 복합 객체에 매핑해 주게 되며 여기에서와 같이 groupBy 로 지정한 property 로 그룹핑하여 하위 요소를 List 형태로 자동 세팅할 수 있다.

### Sample TestCase

```java
..
    @Test
    public void testComplexPropertiesOneToManyResultMapSelect()
            throws Exception {
        DeptVO vo = new DeptVO();
        // 20,'RESEARCH','DALLAS'
        vo.setDeptNo(new BigDecimal(20));
 
        // select
        DeptIncludesEmpListVO resultVO =
            empDAO.selectDeptEmpListComplexProperties(
                "selectDeptIncludesEmpListResultUsingResultMap", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(new BigDecimal(20), resultVO.getDeptNo());
        assertEquals("RESEARCH", resultVO.getDeptName());
        assertEquals("DALLAS", resultVO.getLoc());
 
        assertTrue(0 < resultVO.getEmpVOList().size());
 
        /*
         * deptNo 20 인 EmpList 는 초기데이터에 따라 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
         * 7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20 7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20
         * 7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20 7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20
         */
        assertEquals(5, resultVO.getEmpVOList().size());
 
        assertEquals(new BigDecimal(7369), resultVO.getEmpVOList().get(0)
            .getEmpNo());
        assertEquals("SMITH", resultVO.getEmpVOList().get(0).getEmpName());
        assertEquals("CLERK", resultVO.getEmpVOList().get(0).getJob());
        assertEquals(new BigDecimal(7902), resultVO.getEmpVOList().get(0)
            .getMgr());
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        assertEquals(sdf.parse("1980-12-17"), resultVO.getEmpVOList().get(0)
            .getHireDate());
        assertEquals(new BigDecimal(800), resultVO.getEmpVOList().get(0)
            .getSal());
        assertEquals(new BigDecimal(0), resultVO.getEmpVOList().get(0)
            .getComm());
        assertEquals(new BigDecimal(20), resultVO.getEmpVOList().get(0)
            .getDeptNo());
 
        assertEquals(new BigDecimal(7566), resultVO.getEmpVOList().get(1)
            .getEmpNo());
        assertEquals(new BigDecimal(7788), resultVO.getEmpVOList().get(2)
            .getEmpNo());
        assertEquals(new BigDecimal(7876), resultVO.getEmpVOList().get(3)
            .getEmpNo());
        assertEquals(new BigDecimal(7902), resultVO.getEmpVOList().get(4)
            .getEmpNo());
    }
```

 위의 테스트 케이스 검증 코드에서 resultVO.getEmpVOList().get(X).getXXX 와 같이 내포 객체(List&lt;EmpVO&gt;)의 각 EmpVO 와 해당 attributes 가 잘 설정되었음을 확인할 수 있다.

### Complext Properties - (1:N 관계 - outer join 의 경우) resultMap

 1:N 관계를 포함하는 복합 객체의 리스트를 조회할 때 outer join 을 사용한 예이다.

```xml
<sqlMap namespace="EmpComplexResult">
	..
	<select id="selectDeptIncludesEmpListResultListUsingResultMap" parameterClass="deptVO" resultMap="deptIncludesEmpListResult">
		<![CDATA[
			select   A.DEPT_NO as DEPT_NO,
			         DEPT_NAME,
			         LOC,
			         EMP_NO,
			         EMP_NAME,
			         JOB,
			         MGR,
			         HIRE_DATE,
			         SAL,
			         COMM
			from     DEPT A
			         left outer join EMP B
			           on (A.DEPT_NO = B.DEPT_NO)
			where    A.DEPT_NAME like '%'||#deptName#||'%'
			order by A.DEPT_NO,
			         B.EMP_NO
		]]>
	</select>
```

### Sample TestCase

```java
..
    @Test
    public void testComplexPropertiesOneToManyVOListResultMapSelect()
            throws Exception {
        DeptVO vo = new DeptVO();
        // deptName 에 의한 like 검색 테스트 '%'|| 'E' ||'%' --> R'E'S'E'ARCH, SAL'E'S, OP'E'RATIONS
        // 20,'RESEARCH','DALLAS'
        // 30,'SALES','CHICAGO'
        // 40,'OPERATIONS','BOSTON'
        vo.setDeptName("E");
 
        // select
        List<DeptIncludesEmpListVO> resultList =
            empDAO.selectDeptEmpListComplexPropertiesList(isMysql
                ? "selectDeptIncludesEmpListResultListUsingResultMapMysql"
                : "selectDeptIncludesEmpListResultListUsingResultMap", vo);
 
        // check
        assertNotNull(resultList);
        assertEquals(3, resultList.size());
 
        assertEquals(new BigDecimal(20), resultList.get(0).getDeptNo());
        assertEquals(new BigDecimal(30), resultList.get(1).getDeptNo());
        assertEquals(new BigDecimal(40), resultList.get(2).getDeptNo());
 
        /*
         * deptNo 20 인 EmpList 는 초기데이터에 따라 5 명, deptNo 30 인 EmpList 는 초기데이터에 따라 6 명, deptNo 40 인 EmpList 는 초기데이터에 따라 0 명
         * --> cf.)outer join 에 따라 deptNo 만 가진 EmpVO 1건 생김
         */
        assertEquals(5, resultList.get(0).getEmpVOList().size());
        assertEquals(6, resultList.get(1).getEmpVOList().size());
        // cf.)outer join 에 따라 deptNo 만 가진 EmpVO 1건 생김을 확인함. 주의할 것!
        assertEquals(1, resultList.get(2).getEmpVOList().size());
        assertNull(resultList.get(2).getEmpVOList().get(0).getEmpNo());
 
        /*
         * deptNo 20 인 EmpList 는 초기데이터에 따라 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
         * 7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20 7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20
         * 7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20 7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20
         */
        assertEquals(new BigDecimal(7566), resultList.get(0).getEmpVOList()
            .get(1).getEmpNo());
        assertEquals(new BigDecimal(7788), resultList.get(0).getEmpVOList()
            .get(2).getEmpNo());
        assertEquals(new BigDecimal(7876), resultList.get(0).getEmpVOList()
            .get(3).getEmpNo());
        assertEquals(new BigDecimal(7902), resultList.get(0).getEmpVOList()
            .get(4).getEmpNo());
    }
```

 위의 테스트 케이스 검증 코드에서 iBATIS 의 resultMap 을 사용하여 outer join 의 결과를 복합 객체로 매핑하는 경우 (groupBy 속성 사용 형태) join key 에 해당하는 값만을 가진 하위 객체가 의도하지 않게 생기는 문제가 있어 보이므로 사용에 유의하기 바란다!

### Complext Properties - (1:N 관계 - N+1 select 형태) resultMap

 EmpVO 의 List 를 1:N 관계의 멤버 attribute 로 포함하고 있는 DeptIncludesEmpListVO 를 결과 객체로 사용하고 있는 것은 같다.

```xml
<sqlMap namespace="EmpComplexResult">
	..
	<!-- 1:N 인 경우 N+1 select 형태 - 비추천 -->
	<resultMap id="deptIncludesEmpListUsingSelectAttrResult" class="deptIncludesEmpListVO">
		<result property="deptNo" column="DEPT_NO" />
		<result property="deptName" column="DEPT_NAME" />
		<result property="loc" column="LOC" />
 
		<!-- Dept-EmpList 1:N relation using select attribute -->
		<result property="empVOList" column="DEPT_NO" select="selectEmpList" />
	</resultMap>
 
	<select id="selectDeptIncludesEmpListResultListUsingRepetitionSelect" parameterClass="deptVO"
			resultMap="deptIncludesEmpListUsingSelectAttrResult">
		<![CDATA[
			select   DEPT_NO,
			         DEPT_NAME,
			         LOC
			from     DEPT
			where    DEPT_NAME like '%'||#deptName#||'%'
			order by DEPT_NO
		]]>
	</select>
 
	<select id="selectEmpList" parameterClass="decimal" resultMap="getEmpResult">
		<![CDATA[
			select   EMP_NO,
			         EMP_NAME,
			         JOB,
			         MGR,
			         HIRE_DATE,
			         SAL,
			         COMM,
			         DEPT_NO
			from     EMP
			where    DEPT_NO = #deptNo#
			order by EMP_NO
		]]>
	</select>
```

 위 sql 매핑 파일에서 1:N 관계를 표현하는 Complex Properties 를 포함하는 DeptIncludesEmpListVO 에 대한 resultMap 매핑 처리 시 해당 객체의 empVOList 멤버 attribute 에 대한 매핑 정의를 위해 select=“selectEmpList” 과 같이 별도의 쿼리문을 호출하여(EmpVO 에 대한 resultMap 으로 처리되는) 처리하는 예이다. 쿼리문 상에서 join 을 사용하지 않고 있으며 메인 쿼리문 한번(1번)의 호출에도 결과 rows 수만큼의 select 속성으로 지정한 별도 쿼리 (N번) 가 수행되므로 성능 측면에서 매우 바람직하지 않은 형태이다.

### Sample TestCase

```java
..
    @Test
    public void testComplexPropertiesOneToManyVOListRepetitionSelect()
            throws Exception {
        DeptVO vo = new DeptVO();
        // deptName 에 의한 like 검색 테스트 '%'|| 'E' ||'%' --> R'E'S'E'ARCH, SAL'E'S, OP'E'RATIONS
        // 20,'RESEARCH','DALLAS'
        // 30,'SALES','CHICAGO'
        // 40,'OPERATIONS','BOSTON'
        vo.setDeptName("E");
 
        // select
        List<DeptIncludesEmpListVO> resultList =
            empDAO
                .selectDeptEmpListComplexPropertiesList(
                    isMysql
                        ? "selectDeptIncludesEmpListResultListUsingRepetitionSelectMysql"
                        : "selectDeptIncludesEmpListResultListUsingRepetitionSelect",
                    vo);
 
        // check
        assertNotNull(resultList);
        assertEquals(3, resultList.size());
 
        assertEquals(new BigDecimal(20), resultList.get(0).getDeptNo());
        assertEquals(new BigDecimal(30), resultList.get(1).getDeptNo());
        assertEquals(new BigDecimal(40), resultList.get(2).getDeptNo());
 
        /*
         * deptNo 20 인 EmpList 는 초기데이터에 따라 5 명, deptNo 30 인 EmpList 는 초기데이터에 따라 6 명 deptNo 40 인 EmpList 는 초기데이터에 따라 0 명
         * --> 위 outer join 케이스와 달리 EmpList 도 건수 없음 확인
         */
        assertEquals(5, resultList.get(0).getEmpVOList().size());
        assertEquals(6, resultList.get(1).getEmpVOList().size());
        assertEquals(0, resultList.get(2).getEmpVOList().size());
 
        /*
         * deptNo 20 인 EmpList 는 초기데이터에 따라 7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20
         * 7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20 7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20
         * 7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20 7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20
         */
        assertEquals(new BigDecimal(7566), resultList.get(0).getEmpVOList()
            .get(1).getEmpNo());
        assertEquals(new BigDecimal(7788), resultList.get(0).getEmpVOList()
            .get(2).getEmpNo());
        assertEquals(new BigDecimal(7876), resultList.get(0).getEmpVOList()
            .get(3).getEmpNo());
        assertEquals(new BigDecimal(7902), resultList.get(0).getEmpVOList()
            .get(4).getEmpNo());
    }
```

 위의 테스트 케이스 검증 코드에서 resultList.get(X).getEmpVOList().get(X).getXXX 와 같이 조회 결과(List) 의 내포 객체(List&lt;EmpVO&gt;)의 각 EmpVO 와 해당 attributes 가 잘 설정되었음을 확인할 수 있다. 그러나 N+1 조회의 성능 문제를 야기하므로 sql 매핑 정의 시 join 쿼리와 groupBy 속성을 통한 1:N 관계 처리 매핑으로 처리하는 것이 바람직하다.

### Complext Properties - (Hierarchy 관계) resultMap

```java
..
public class EmpIncludesMgrVO implements Serializable {
 
    private static final long serialVersionUID = 5695339933191681519L;
 
    private BigDecimal empNo;
 
    private String empName;
 
    private String job;
 
    private BigDecimal mgr;
 
    private Date hireDate;
 
    private BigDecimal sal;
 
    private BigDecimal comm;
 
    private BigDecimal deptNo;
 
    // Hierarchy 관계
    private EmpIncludesMgrVO mgrVO;
 
    public BigDecimal getEmpNo() {
        return empNo;
    }
 
    public void setEmpNo(BigDecimal empNo) {
        this.empNo = empNo;
    }
..
    public EmpIncludesMgrVO getMgrVO() {
        return mgrVO;
    }
 
    public void setMgrVO(EmpIncludesMgrVO mgrVO) {
        this.mgrVO = mgrVO;
    }
}
```

 위의 EmpIncludesMgrVO 는 자신과 동일한 EmpIncludesMgrVO 를 Hierarchy 관계의 멤버 attribute 로 포함하고 있다. 위에서는 Emp 의 Manager 에 대해서 포함하고 있는데 MgrVO 를 거슬러 올라가면 결국 자기 관리자 path 에 있는 모든 사원에 대한 정보를 포함하고 있는 객체라 볼 수 있다.

```xml
<sqlMap namespace="EmpComplexResult">
	..
	<typeAlias alias="empIncludesMgrVO" type="egovframework.rte.psl.dataaccess.vo.EmpIncludesMgrVO" />
 
	<!-- Hierarchical relation 인 경우 ibatis resultMap select 에 의한 처리 예 -->
	<resultMap id="empIncludesMgrResult" class="empIncludesMgrVO" extends="getEmpResult">
		<result property="mgrVO" column="MGR" select="selectMgrHierarchy" />
	</resultMap>
 
	<!-- 하나의 쿼리를 사용하여 empNo, mgr 속성의 유무에 따라 Hierarchy 반복조회로도 사용토록 변경
		 parameterClass 는 최초 조회와 resultMap 의 select 조회의 경우 empVO 와 decimal 로 다르기 때문에
		 따로 명시하지 않고 자동 reflection 에 의해 처리토록 함
	 -->
	<select id="selectMgrHierarchy" resultMap="empIncludesMgrResult">
		<![CDATA[
			select   EMP_NO,
			         EMP_NAME,
			         JOB,
			         MGR,
			         HIRE_DATE,
			         SAL,
			         COMM,
			         DEPT_NO
			from     EMP
			where    1=1
		]]>
		<!-- 최초 - empNo 는 parameter bean 의 property 임-->
		<isPropertyAvailable property="empNo" prepend="and">
			EMP_NO = #empNo#
		</isPropertyAvailable>
		<!-- 반복 - column="MGR" 에 의한 연결로 empNo 는 property가 아님 -->
		<isNotPropertyAvailable property="empNo" prepend="and">
			EMP_NO = #mgr#
		</isNotPropertyAvailable>
	</select>
```

 위 sql 매핑 파일에서 Hierarchy 관계를 표현하는 Complex Properties 를 포함하는 EmpIncludesMgrVO 에 대한 resultMap 매핑 처리 시 해당 객체의 mgrVO 멤버 attribute 에 대한 매핑 정의를 위해 select=“selectMgrHierarchy” 과 같이 자기 자신의 sql 문을 재호출 하는 형태이다.

### Sample TestCase

```java
..
    @Test
    public void testComplexPropertiesHierarcyRepetitionSelect()
            throws Exception {
        EmpVO vo = new EmpVO();
        // 7369,'SMITH','CLERK',7902
        // --> 7902,'FORD','ANALYST',7566
        // --> 7566,'JONES','MANAGER',7839
        // --> 7839,'KING','PRESIDENT',NULL
        vo.setEmpNo(new BigDecimal(7369));
 
        try {
 
            // select
            // EmpIncludesMgrVO resultVO =
            // empDAO.selectEmpMgrHierarchy("selectEmpWithMgr", vo);
            EmpIncludesMgrVO resultVO =
                empDAO.selectEmpMgrHierarchy("selectMgrHierarchy", vo);
 
            // check
            assertNotNull(resultVO);
            assertEquals(new BigDecimal(7369), resultVO.getEmpNo());
            assertEquals("SMITH", resultVO.getEmpName());
            assertEquals("CLERK", resultVO.getJob());
            assertEquals(new BigDecimal(7902), resultVO.getMgr());
            SimpleDateFormat sdf =
                new SimpleDateFormat("yyyy-MM-dd", java.util.Locale
                    .getDefault());
            assertEquals(sdf.parse("1980-12-17"), resultVO.getHireDate());
            assertEquals(new BigDecimal(800), resultVO.getSal());
            assertEquals(new BigDecimal(0), resultVO.getComm());
            assertEquals(new BigDecimal(20), resultVO.getDeptNo());
 
            assertTrue(resultVO.getMgrVO() instanceof EmpIncludesMgrVO);
            assertEquals(new BigDecimal(7902), resultVO.getMgrVO().getEmpNo());
            assertEquals(new BigDecimal(7566), resultVO.getMgrVO().getMgrVO()
                .getEmpNo());
            assertEquals(new BigDecimal(7839), resultVO.getMgrVO().getMgrVO()
                .getMgrVO().getEmpNo());
            assertNull(resultVO.getMgrVO().getMgrVO().getMgrVO().getMgrVO());
 
        } catch (UncategorizedSQLException ue) {
            // tibero 인 경우 ibatis 의 재귀 queyr 형태의 sub 객체 맵핑 시 com.tmax.tibero.jdbc.TbSQLException: TJDBC-90646:Resultset
            // is already closed 에러 발생 확인함!
            assertTrue(isTibero);
            assertTrue(ue.getCause() instanceof NestedSQLException);
            assertTrue(ue.getCause().getCause().getCause().getCause() instanceof TbSQLException);
            assertTrue(((TbSQLException) ue.getCause().getCause().getCause()
                .getCause()).getMessage().contains(
                "TJDBC-90646:Resultset is already closed"));
        }
    }
```

 위의 테스트 케이스 검증 코드에서 SMITH → FORD → JONES → KING 으로 연결되는 관리자 정보를 모두 포함하는 복합 객체의 각 attribute 가 잘 설정되었음을 확인할 수 있다. 일부 DBMS 에서는 문제가 발생할 수 있으므로 사용에 유의한다.