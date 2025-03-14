---
title: iBATIS parameterMap
linkTitle: "parameterMap"
description: parameterMap은 Java 객체의 속성에 대한 매핑을 설정하여 SQL 바인드 변수를 처리하는 요소로, 기술적인 매핑이 필요한 경우에 사용되지만, Dynamic 요소와 함께 사용할 수 없고 바인드 변수의 순서를 맞춰야 하는 제한이 있어 일반적으로 추천되지 않는다. 대신 parameterClass나 Inline Parameter 방식이 더 자주 사용된다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-parameterMap/
menu:
    depth:
        name: parameterMap
        weight: 4
        parent: dataaccess-ibatis
---
# parameterMap

 parameterMap 은 해당 요소로 SQL 문 외부에 정의한 입력 객체의 속성에 대한 name 및 javaType, jdbcType 을 비롯한 옵션을 설정할 수 있는 매핑 요소이다. 이를 통해 JavaBeans 객체(또는 Map 등)에 대한 prepared statement 에 대한 바인드 변수 매핑을 처리할 수 있다. 유사한 기능을 처리하는 parameterClass 나 Inline Parameter 에 비해 많이 사용되지 않지만 더 기술적인(descriptive) parameterMap(예를 들어 stored procedure 를 위한) 이 필요하거나, XML 의 일관된 사용과 순수성을 지키고자 할때 좋은 접근법이 될 수도 있다. 그러나 Dynamic 요소와 함께 사용될 수 없고 바인드 변수의 갯수와 순서를 정확히 맞춰야 하는 불편이 있는 등 일반적으로 사용을 추천하지 않는다.

## 기본 parameterMap 사용 방법

 아래의 샘플 parameterMap 정의를 참고하라.

### Sample parameterMap

```xml
	..
	<typeAlias alias="empVO" type="egovframework.rte.psl.dataaccess.vo.EmpVO" />
 
	<parameterMap id="empParam" class="empVO">
		<parameter property="empNo" javaType="decimal" jdbcType="NUMERIC" />
		<parameter property="empName" javaType="string" jdbcType="VARCHAR" nullValue="blank" />
		<parameter property="job" javaType="string" jdbcType="VARCHAR" nullValue="" />
		<parameter property="mgr" javaType="decimal" jdbcType="NUMERIC" />
		<parameter property="hireDate" javaType="date" jdbcType="DATE" />
		<parameter property="sal" javaType="decimal" jdbcType="NUMERIC" />
		<parameter property="comm" javaType="decimal" jdbcType="NUMERIC" nullValue="-99999" />
		<parameter property="deptNo" javaType="decimal" jdbcType="NUMERIC" />
	</parameterMap>
 
	<insert id="insertEmpUsingParameterMap" parameterMap="empParam">
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
			values     (?,
			            ?,
			            ?,
			            ?,
			            ?,
			            ?,
			            ?,
			            ?)
		]]>
	</insert>
```

 위 sql 매핑 파일에서 parameterMap 요소로 empParam 이라는 id 를 부여하고 대상 입력 객체는 EmpVO 를 지정하고 있다. EmpVO 에 대한 상세 attribute (속성) 들에 대해 parameter 하위 요소로 매핑 정의를 하고 있는데 이때 추가적으로 javaType, jdbcType 에 대해 위에서는 명시하였다. (java 의 reflection 기술을 사용하여 대상 클래스의 개별 속성에 대한 type 을 구하는 것보다 직접 type 에 대한 지시를 설정으로 명시하므로 약간의 성능상 이점이 있을 수 있다.) 위에서는 동일한 property 가 중복으로 사용되는 경우가 없으나 parameterMap 은 아래의 insertEmpUsingParameterMap mapped statement 예에서 보듯이 ? 에 대한 순서대로 매핑되므로 만약 중복으로 사용되는 경우가 필요하다면 parameterMap 정의부터 순서를 맞추어 동일한 property 의 중복 정의가 필요할 수 있다. 또한 nullValue 속성을 지정한 property 에 대해서는 해당 값이 nullValue 에 지정된 값으로 전달되는 경우 데이터베이스에는 null 로 처리가 이 외에도 typeName, resultMap, mode, typeHandler, numericScale 에 대한 속성 정의가 가능하다.

### Sample TestCase

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {"classpath*:META-INF/spring/context-*.xml" })
@TransactionConfiguration(transactionManager = "txManager", defaultRollback = false)
@Transactional
public class ParameterMapTest extends TestBase {
 
    @Resource(name = "empDAO")
    EmpDAO empDAO;
 
    @Before
    public void onSetUp() throws Exception {
        // DB 초기화
    }
 
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
        // mysql 5.0.X에서는 소숫점 자릿수 만큼 .00 이 달려 나와 테스트 편의상 소숫점 자리수가 없도록 칼럼 선언 하였음.
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
    public void testParameterMapInsert() throws Exception {
        EmpVO vo = makeVO();
 
        // insert
        empDAO.insertEmp("insertEmpUsingParameterMap", vo);
 
        // select
        EmpVO resultVO = empDAO.selectEmp("selectEmp", vo);
 
        // check
        checkResult(vo, resultVO);
    }
 
    @Test
    public void testParameterMapInsertWithNullValue() throws Exception {
        EmpVO vo = new EmpVO();
        // key 설정
        vo.setEmpNo(new BigDecimal(9000));
 
        // parameterMap nullValue test
        vo.setEmpName("blank");
        vo.setJob("");
        // cf.) -99999.99 는 NumberFormatException 임을
        // 확인하였음!
        vo.setComm(new BigDecimal("-99999"));
 
        // insert
        empDAO.insertEmp("insertEmpUsingParameterMap", vo);
 
        // select
        EmpVO resultVO = empDAO.selectEmp("selectEmp", vo);
 
        // check
        assertNotNull(resultVO);
        assertEquals(vo.getEmpNo(), resultVO.getEmpNo());
        // parameterMap 설정에서 nullValue="blank" .. 에 따라
        // 해당값이 null 로 입력되었을 것임
        assertNull(resultVO.getEmpName());
        assertNull(resultVO.getJob());
        assertNull(resultVO.getComm());
    }
 
}
```

 위에서 parameterMap 을 이용한 파라메터 객체 바인딩을 처리하는 insertEmpUsingParameterMap 쿼리문에 대해 입력객체를 세팅 후 입력/조회 처리하고 있는 테스트 케이스이다. 실제로 매핑 파일 내에서 parameterMap 을 사용하는 경우와 Inline parameter 또는 parameterClass 를 그대로 쓰는 경우에서도 어플리케이션 영역은 동일한 형태의 입력 객체를 인자로 iBATIS API 를 호출하게 된다. 위의 testParameterMapInsertWithNullValue 테스트 메서드에서는 parameterMap 에 nullValue 속성으로 지정한 특정한 값을 세팅 하므로써 DB 에 null 로 입력이 된 결과를 조회하여 assertNull 로 확인하고 있다.