---
title: Inline Parameters
linkTitle: "Inline Parameters"
description: "Inline Parameters는 #property# 노테이션을 사용해 간편하게 바인드 변수 매핑을 처리하며, 별도의 parameterMap 선언 없이 입력 객체의 속성을 SQL에 직접 매핑할 수 있다. Dynamic 요소와 함께 사용 가능하며, 필요한 경우 JDBC 타입과 null 값을 추가 노테이션으로 지정할 수 있다."
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-inline_paramters/
menu:
    depth:
        name: Inline Parameters
        weight: 5
        parent: dataaccess-ibatis
---
# Inline Parameters

 이전에 살펴본 prepared statement 에 대한 바인드 변수 매핑 처리를 위한 parameterMap 요소(SQL 문 외부에 정의한 입력 객체 property name 및 javaType, jdbcType 을 비롯한 옵션을 설정 매핑 요소) 와 동일한 기능을 처리하는 간편한 방법을 Inline Parameters 방법으로 제공한다. 보통 parameterClass 로 명시된 입력 객체에 대해 바인드 변수 영역을 간단한 #property# 노테이션으로 나타내는 Inline Parameter 방법은 기존 parameterMap 에서의 ? 와 이의 순서를 맞춘 외부 parameterMap 선언으로 처리하는 방법에 비해 많이 사용되고 일반적으로 추천하는 방법이다. 이는 Dynamic 요소와 함께 사용될 수 있고 별도의 외부 매핑 정의 없이 바인드 변수 처리가 필요한 위치에 해당 property 를 직접 사용 가능하며, 필요한 경우 jdbcType 이나 nullValue 를 간단한 추가 노테이션(ex. #empName:VARCHAR:blank# ) 와 같이 지정할 수 있고, 상세한 옵션이 필요한 경우에는 (ex. #comm,javaType=decimal,jdbcType=NUMERIC,nullValue=-99999# ) 와 같이 ,(comma) 로 구분된 필요한 속성=값 을 상세하게 기술할 수도 있다.

## 기본 Inline Parameters 사용 방법

 아래의 샘플 Inline Parameters 사용 쿼리문을 참고하라.

### Sample Inline Parameters

```xml
	..
	<typeAlias alias="empVO" type="egovframework.rte.psl.dataaccess.vo.EmpVO" />
 
	<insert id="insertEmptUsingInLineParam">
		<![CDATA[
			insert into EMP
			           (EMP_NO,
			            EMP_NAME,
			            JOB,
			            MGR,
			            HIRE_DATE,
			            SAL,
			            COMM,
			            DEPT_NO)
			values     (#empNo:NUMERIC#,
			            #empName:VARCHAR:blank#,
			            #job:VARCHAR:""#,	/* inline parameter 에서는 empty String 을 nullValue로 대체할 수 없음 - cf.) oracle인 경우는 "" 가 null 임 */
			            #mgr:NUMERIC#,
			            #hireDate:DATE#,
			            #sal:NUMERIC#,	
			            #comm,javaType=decimal,jdbcType=NUMERIC,nullValue=-99999#,
			            #deptNo:NUMERIC#)
		]]>
	</insert>
```

 위 sql 매핑 파일에서 별도의 parameterMap 외부 정의없이 #property:jdbcType# 형태로 직접 바인드 변수 영역에 나타내고 있다. #property# 만 나타내도 iBATIS 에서 자동으로 타입처리는 잘된다. 위에서는 해당 쿼리에 parameterClass=“empVO” 에 대한 입력 객체 설정이 나타나 있지 않음에도 iBATIS 에서 런타임에 인자로 주어지는 입력 객체를 자동으로 파악하여 파라메터 처리를 하고 있음을 확인할 수 있다. 그러나 parameterClass 의 명시는 성능 상 반드시 추천하는 바이다.

- #property#
- #property:jdbcType#
- #property:jdbcType:nullValue# 형태까지 : 를 구분자로 함께 나타낼 수 있으며 nullValue 대체 값은 jdbcType 명시가 반드시 필요하다.

 이 외에도 속성=값 형태의 옵션 설정을 , 를 구분자로 아래와 같이 나타낼 수 있다.

- #propertyName,javaType=?,jdbcType=?,mode=?,nullValue=?,handler=?,numericScale=?#

 위에서 ? 부분을 해당 속성에 따라 적절한 값으로 설정하면 된다. mode 는 stored procedure 의 IN/OUT/INOUT 모드를 지시할 수 있는 속성이고 numericScale 은 stored procedure 의 OUT/INOUT 변수가 decimal 이나 numeric인 경우 DBMS 의 Scale 정보를 유지하기 위해 명시해야 하는 속성이다. handler 속성에는 typeHandler 를 지시할 수 있다.

### Sample TestCase

```java
..
   public EmpVO makeVO() throws ParseException {
        EmpVO vo = new EmpVO();
        vo.setEmpNo(new BigDecimal(9000));
        vo.setEmpName("test Emp");
        vo.setJob("test Job");
        // 7839,'KING','PRESIDENT'
        vo.setMgr(new BigDecimal(7839));
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        vo.setHireDate(sdf.parse("2009-02-09"));
 
        // mysql 은 소숫점 이하 자리가 .00 으로 기본 들어가게 되어 테스트 편의상 numeric(5) 로 선언하였음.
        if (isMysql) {
            vo.setSal(new BigDecimal("12345"));
            vo.setComm(new BigDecimal(100));
        } else {
            vo.setSal(new BigDecimal("12345.67"));
            vo.setComm(new BigDecimal(100.00));
        }
        // 10,'ACCOUNTING','NEW YORK'
        vo.setDeptNo(new BigDecimal(10));
        return vo;
    }
 
    public void checkResult(EmpVO vo, EmpVO resultVO) {
        assertNotNull(resultVO);
        assertEquals(vo.getEmpNo(), resultVO.getEmpNo());
        assertEquals(vo.getEmpName(), resultVO.getEmpName());
        assertEquals(vo.getJob(), resultVO.getJob());
        assertEquals(vo.getMgr(), resultVO.getMgr());
        assertEquals(vo.getHireDate(), resultVO.getHireDate());
        assertEquals(vo.getSal(), resultVO.getSal());
        assertEquals(vo.getComm(), resultVO.getComm());
        assertEquals(vo.getDeptNo(), resultVO.getDeptNo());
    }
 
    @Test
    public void testInLineParameterInsert() throws Exception {
        EmpVO vo = makeVO();
 
        // insert
        empDAO.insertEmp("insertEmptUsingInLineParam", vo);
 
        // select
        EmpVO resultVO = empDAO.selectEmp("selectEmp", vo);
 
        // check
        checkResult(vo, resultVO);
    }
 
    @Test
    public void testInLineParameterInsertWithNullValue() throws Exception {
        EmpVO vo = new EmpVO();
        // key 설정
        vo.setEmpNo(new BigDecimal(9000));
 
        // inline parameter nullValue test
        vo.setEmpName("blank");
        // inline parameter 에서는 empty String 을
        // nullValue로 대체할 수 없음
        // ref.)
        // http://www.nabble.com/inline-map-format%3A-empty-String-in-nullValue-td18905940.html
        vo.setJob(""); // cf.) oracle 인 경우 "" 는 null 과
        // 같음!
        vo.setComm(new BigDecimal("-99999"));
 
        // insert
        empDAO.insertEmp("insertEmptUsingInLineParam", vo);
 
        // select
        EmpVO resultVO = empDAO.selectEmp("selectEmp", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(vo.getEmpNo(), resultVO.getEmpNo());
        // inline parameter 설정에서
        // #empName:VARCHAR:blank# ..
        // 에 따라 해당값이 null 로
        // 입력되었을 것임
        assertNull(resultVO.getEmpName());
        // inline parameter 에서는 empty String 을
        // nullValue로 대체할 수 없음 확인!
        // cf.) parameterMap 케이스에서는
        // assertNull(resultVO.getJob()) // cf.) oracle
        // 인 경우 "" 는 null 과 같음!
        // assertNotNull(resultVO.getJob());
        assertNull(resultVO.getComm());
    }
..
```

 위에서 Inline Parameters 을 이용한 파라메터 객체 바인딩을 처리하는 insertEmptUsingInLineParam 쿼리문에 대해 입력객체를 세팅 후 입력/조회 처리하고 있는 테스트 케이스이다. 실제로 위 어플리케이션 영역은 parameterMap 사용 시와 차이가 없음을 알 수 있다. 위의 testInLineParameterInsertWithNullValue 테스트 메서드에서는 Inline Parameters 에 nullValue 속성으로 지정한 특정한 값을 세팅 함으로써 DB 에 null 로 입력이 된 결과를 조회하여 assertNull 로 확인하고 있다. 위에서 empty String 의 nullValue 설정은 inline parameter 노테이션의 한계로 제대로 처리되지 않음을 확인하였으므로 참고하기 바란다.