---
title: iBATIS에서의 Data Type 매핑
linkTitle: "Data Type"
description: Java 애플리케이션에서 데이터베이스와 상호작용할 때, Java 타입과 DBMS의 JDBC 타입 간의 정확한 매핑이 중요하다. iBATIS는 JavaBeans 객체의 속성과 DB 테이블의 컬럼 타입을 매핑하여 데이터 바인딩 및 매핑을 처리하며, 이를 통해 다양한 데이터 타입에 대한 적절한 사용 방법을 제공한다.
url: /egovframe-runtime/persistence-layer/dataaccess-ibatis/dataaccess-data_type/
menu:
    depth:
        name: Data Type
        weight: 3
        parent: dataaccess-ibatis
---
# Data Type

 어플리케이션을 작성할 때 Data Type 에 대한 올바른 사용과 관련 처리는 매우 중요하다. 특히 데이터베이스를 이용하여 데이터를 저장하고 조회할 때 Java 어플리케이션에서의 Type 과 DBMS 에서 지원하는 관련 매핑 jdbc Type 의 정확한 사용이 필요하며, 여기에서는 iBATIS 환경에서 javaType 과 특정 DBMS 의 jdbcType 의 적절한 매핑 사용예를 중심으로 일반적인 Data Type 의 사용 가이드를 참고할 수 있도록 한다.

## 기본 Data Type 사용 방법

 iBATIS SQL Mapper 프레임워크는 Java 어플리케이션 영역의 표준 JavaBeans 객체(또는 Map 등)의 각 Attribute 에 대한 Java Type 과 JDBC 드라이버에서 지원하는 각 DBMS의 테이블 칼럼에 대한 Data Type 의 매핑을 기반으로 parameter / result 객체에 대한 바인딩/매핑 을 처리한다. 각 javaType 에 대한 매칭되는 jdbcType 은 일반적인 Ansi SQL 을 사용한다고 하였을 때 아래에서 대략 확인할 수 있을 것이다. 특정 DBMS 벤더에 따라 추가적으로 지원/미지원 하는 jdbcType 이 다를 수 있고, 또한 같은 jdbcType 을 사용한다 하더라도 타입에 따른 사용 가능한 경계값(boundary max/min value)은 다를 수 있다.

 아래에서는 다양한 primitive 타입과 숫자 타입, 문자 타입, 날짜 타입에 대한 기본 insert/select 를 통해 iBATIS 사용 환경에서의 data type 에 대한 사용 예를 알아보겠다.

### Sample Type VO

```java
public class TypeTestVO implements Serializable {
 
    private static final long serialVersionUID = -3653247402772333834L;
 
    private int id;
 
    private BigDecimal bigdecimalType;
 
    private boolean booleanType;
 
    private byte byteType;
 
    private String charType;
 
    private double doubleType;
 
    private float floatType;
 
    private int intType;
 
    private long longType;
 
    private short shortType;
 
    private String stringType;
 
    private Date dateType;
 
    private java.sql.Date sqlDateType;
 
    private Time sqlTimeType;
 
    private Timestamp sqlTimestampType;
 
    private Calendar calendarType;
 
    public int getId() {
        return id;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    public BigDecimal getBigdecimalType() {
        return bigdecimalType;
    }
 
    public void setBigdecimalType(BigDecimal bigdecimalType) {
        this.bigdecimalType = bigdecimalType;
    }
 
    public boolean isBooleanType() {
        return booleanType;
    }
 
    public void setBooleanType(boolean booleanType) {
        this.booleanType = booleanType;
    }
 
    public byte getByteType() {
        return byteType;
    }
 
    public void setByteType(byte byteType) {
        this.byteType = byteType;
    }
 
    public String getCharType() {
        return charType;
    }
 
    public void setCharType(String charType) {
        this.charType = charType;
    }
 
    public double getDoubleType() {
        return doubleType;
    }
 
    public void setDoubleType(double doubleType) {
        this.doubleType = doubleType;
    }
 
    public float getFloatType() {
        return floatType;
    }
 
    public void setFloatType(float floatType) {
        this.floatType = floatType;
    }
 
    public int getIntType() {
        return intType;
    }
 
    public void setIntType(int intType) {
        this.intType = intType;
    }
 
    public long getLongType() {
        return longType;
    }
 
    public void setLongType(long longType) {
        this.longType = longType;
    }
 
    public short getShortType() {
        return shortType;
    }
 
    public void setShortType(short shortType) {
        this.shortType = shortType;
    }
 
    public String getStringType() {
        return stringType;
    }
 
    public void setStringType(String stringType) {
        this.stringType = stringType;
    }
 
    public Date getDateType() {
        return dateType;
    }
 
    public void setDateType(Date dateType) {
        this.dateType = dateType;
    }
 
    public java.sql.Date getSqlDateType() {
        return sqlDateType;
    }
 
    public void setSqlDateType(java.sql.Date sqlDateType) {
        this.sqlDateType = sqlDateType;
    }
 
    public Time getSqlTimeType() {
        return sqlTimeType;
    }
 
    public void setSqlTimeType(Time sqlTimeType) {
        this.sqlTimeType = sqlTimeType;
    }
 
    public Timestamp getSqlTimestampType() {
        return sqlTimestampType;
    }
 
    public void setSqlTimestampType(Timestamp sqlTimestampType) {
        this.sqlTimestampType = sqlTimestampType;
    }
 
    public Calendar getCalendarType() {
        return calendarType;
    }
 
    public void setCalendarType(Calendar calendarType) {
        this.calendarType = calendarType;
    }
 
}
```

 위 TypeTestVO 의 각 attribute 는 다양한 data Type 에 대한 사용예의 샘플이며 이에 대한 매핑 jdbc 타입은 아래의 각 DBMS 별 DDL 을 통해 일차적으로 살펴보자.

### Sample TYPETEST Table Hsqldb DDL script

```sql
create table TYPETEST (
    id numeric(10,0) not null,
    bigdecimal_type numeric(19,2),
    boolean_type boolean, 
    byte_type tinyint,
    char_type char(1),
    double_type double,
    float_type float,
    int_type integer,
    long_type bigint,
    short_type smallint,
    string_type varchar(255),
    date_type date,
    sql_date_type datetime,
    sql_time_type time,
    sql_timestamp_type timestamp,
    calendar_type timestamp,
    primary key (id)
);
```

 위 create sql 문의 hsqldb 의 예이며, 실제로 Ansi SQL 의 Data Type 에 대한 표준을 잘 따르는 예이다. boolean 타입을 직접 지원하고 있으며 tinyint, double, date, time 등 다양한 jdbcType 에 대하여 사용에 특별한 무리가 없음을 아래의 테스트 케이스로 알 수 있을 것이다.

### Sample SQL Mapping XML

```xml
<sqlMap namespace="TypeTest">
 
	<typeAlias alias="typeTestVO"
		type="egovframework.rte.psl.dataaccess.vo.TypeTestVO" />
 
	<!-- CalendarTypeHandler 는 sql-map-config.xml 에 등록하였음 -->
	<typeAlias alias="calendarTypeHandler" type="egovframework.rte.psl.dataaccess.typehandler.CalendarTypeHandler"/>
 
	<resultMap id="typeTestResult" class="typeTestVO">
		<result property="id" column="ID" />
		<result property="bigdecimalType" column="BIGDECIMAL_TYPE" />
		<result property="booleanType" column="BOOLEAN_TYPE" />
		<result property="byteType" column="BYTE_TYPE" />
		<result property="charType" column="CHAR_TYPE" />
		<result property="doubleType" column="DOUBLE_TYPE" />
		<result property="floatType" column="FLOAT_TYPE" />
		<result property="intType" column="INT_TYPE" />
		<result property="longType" column="LONG_TYPE" />
		<result property="shortType" column="SHORT_TYPE" />
		<result property="stringType" column="STRING_TYPE" />
		<result property="dateType" column="DATE_TYPE" />
		<result property="sqlDateType" column="SQL_DATE_TYPE" />
		<result property="sqlTimeType" column="SQL_TIME_TYPE" />
		<result property="sqlTimestampType" column="SQL_TIMESTAMP_TYPE" />
		<result property="calendarType" column="CALENDAR_TYPE" typeHandler="calendarTypeHandler" />
	</resultMap>
 
	<insert id="insertTypeTest" parameterClass="typeTestVO">
		<![CDATA[
			insert into TYPETEST
			           (ID,
			            BIGDECIMAL_TYPE,
			            BOOLEAN_TYPE,
			            BYTE_TYPE,
			            CHAR_TYPE,
			            DOUBLE_TYPE,
			            FLOAT_TYPE,
			            INT_TYPE,
			            LONG_TYPE,
			            SHORT_TYPE,
			            STRING_TYPE,
			            DATE_TYPE,
			            SQL_DATE_TYPE,
			            SQL_TIME_TYPE,
			            SQL_TIMESTAMP_TYPE,
			            CALENDAR_TYPE)
			values     (#id#,
			            #bigdecimalType#,
			            #booleanType#,
			            #byteType#,
			            #charType:CHAR#,
			            #doubleType#,
			            #floatType#,
			            #intType#,
			            #longType#,
			            #shortType#,
			            #stringType#,
			            #dateType#,
			            #sqlDateType#,
			            #sqlTimeType#,
			            #sqlTimestampType#,
			            #calendarType,handler=calendarTypeHandler#)
		]]>
	</insert>
 
	<select id="selectTypeTest" parameterClass="typeTestVO"
		resultMap="typeTestResult">
		<![CDATA[
			select ID,
			       BIGDECIMAL_TYPE,
			       BOOLEAN_TYPE,
			       BYTE_TYPE,
			       CHAR_TYPE,
			       DOUBLE_TYPE,
			       FLOAT_TYPE,
			       INT_TYPE,
			       LONG_TYPE,
			       SHORT_TYPE,
			       STRING_TYPE,
			       DATE_TYPE,
			       SQL_DATE_TYPE,
			       SQL_TIME_TYPE,
			       SQL_TIMESTAMP_TYPE,
			       CALENDAR_TYPE
			from   TYPETEST
			where  ID = #id#
		]]>
	</select>
 
</sqlMap>
```

 TypeTestVO JavaBeans 객체를 통해 insert/select 를 처리하는 sql 매핑 xml 이다. resultMap 을 정의하여 select 결과 객체 매핑을 처리하고 있으며, 입력 및 조회 조건 의 파라메터 바인딩을 Inline Parameter 방법을 통해 처리하고 있다. resultMap 이나 parameterMap(Inline Parameter 도 마찬가지) 에서는 javaType=“string”, jdbcType=“VARCHAR” 와 같이 명시적으로 java/jdbc type 에 대한 지시를 할 수도 있다. (성능상으로는 추천, 그러나 실제와 맞지 않는 type 지시는 런타임에 오류 발생) 또한, 위의 Inline parameter 처리 시 calendar 속성에 대해 handler=calendarTypeHandler 로 지시한 것과 resultMap 처리 시 typeHandler=“calendarTypeHandler” 로 지시한 것에서 확인할 수 있듯이 일반적인 java-jdbc 매핑으로 커버하지 못하는 부분에 대하여 사용자가 typeHandler 를 구현하여 타입 컨버전에 대한 로직 처리를 제공함으로써 위와 같이 calendar type ↔ TIMESTAMP 변환이 가능한 것처럼 확장할 수도 있다.

 위에서 TypeTestVO 와 SQL Mapping XML 은 아래의 추가적인 DBMS 테스트 시 변경없이 재사용하였고, 일부 Data Type 의 미지원/DBMS 별 매핑타입 사용/경계값 상이함 등에 대해서는 DDL / TestCase 에서 약간의 로직 분기나 회피를 통해 문제되는 부분을 피하고 전체적인 관점에서 재사용 할 수 있도록 테스트 하였으므로 참고하기 바란다.

### Sample TestCase

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {"classpath*:META-INF/spring/context-*.xml" })
@TransactionConfiguration(transactionManager = "txManager", defaultRollback = false)
@Transactional
public class DataTypeTest extends TestBase {
 
    @Resource(name = "typeTestDAO")
    TypeTestDAO typeTestDAO;
 
    @Before
    public void onSetUp() throws Exception {
 
        // 외부에 sql file 로부터 DB 초기화 (TypeTest 기존 테이블 삭제/생성)
        SimpleJdbcTestUtils.executeSqlScript(
            new SimpleJdbcTemplate(dataSource), new ClassPathResource(
                "META-INF/testdata/sample_schema_ddl_typetest_" + usingDBMS
                    + ".sql"), true);
    }
 
    public TypeTestVO makeVO() throws Exception {
        TypeTestVO vo = new TypeTestVO();
        vo.setId(1);
        vo.setBigdecimalType(new BigDecimal("99999999999999999.99"));
        vo.setBooleanType(true);
        vo.setByteType((byte) 127);
        // VO 에서 String 으로 선언했음. char 로 하고자 하는 경우 TypeHandler 작성 필요
        vo.setCharType("A");
        // Oracle 10g 에서 double precision 타입은 Double.MAX_VALUE 를 수용하지 못함.
        // oracle jdbc driver 에서 Double.MAX_VALUE 를 전달하면 Overflow Exception trying to bind 1.7976931348623157E308 에러 발생
        // mysql 5.0 에서 테스트 시 Double.MAX_VALUE 입력은 가능하나 조회 시 Infinity 로 되돌려짐
        // tibero - Double.MAX_VALUE 입력 시 Exception 발생
        vo.setDoubleType(isHsql ? Double.MAX_VALUE : 1.7976931348623157d);
        // mysql 5.0 에서 테스트 시 Float.MAX_VALUE 를 입력할 수 없음
        vo.setFloatType(isMysql ? (float) 3.40282 : Float.MAX_VALUE);
        vo.setIntType(Integer.MAX_VALUE);
        vo.setLongType(Long.MAX_VALUE);
        vo.setShortType(Short.MAX_VALUE);
        vo.setStringType("abcd가나다라あいうえおｶｷｸｹｺ");
        SimpleDateFormat sdf =
            new SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault());
        vo.setDateType(sdf.parse("2009-02-18"));
        long currentTime = new java.util.Date().getTime();
        vo.setSqlDateType(new java.sql.Date(currentTime));
        vo.setSqlTimeType(new java.sql.Time(currentTime));
        vo.setSqlTimestampType(new java.sql.Timestamp(currentTime));
        vo.setCalendarType(Calendar.getInstance());
 
        return vo;
    }
 
    public void checkResult(TypeTestVO vo, TypeTestVO resultVO) {
        assertNotNull(resultVO);
        assertEquals(vo.getId(), resultVO.getId());
        assertEquals(vo.getBigdecimalType(), resultVO.getBigdecimalType());
        assertEquals(vo.getByteType(), resultVO.getByteType());
        // mysql 인 경우 timestamp 칼럼에 null 을 입력하면 현재 시각으로 insert 됨에 유의
        if (vo.getCalendarType() == null && isMysql) {
            assertNotNull(resultVO.getCalendarType());
            // mysql 인 경우 java 의 timestamp 에 비해 3자리 정밀도 떨어짐
        } else if (vo.getCalendarType() != null && isMysql) {
            String orgSeconds =
                Long.toString(vo.getCalendarType().getTime().getTime());
            String mysqlSeconds =
                Long.toString(resultVO.getCalendarType().getTime().getTime());
            assertEquals(orgSeconds.substring(0, orgSeconds.length() - 3),
                mysqlSeconds.substring(0, mysqlSeconds.length() - 3));
        } else {
            assertEquals(vo.getCalendarType(), resultVO.getCalendarType());
        }
        assertEquals(vo.getCharType(), resultVO.getCharType());
        assertEquals(vo.getDateType(), resultVO.getDateType());
        // double 에 대한 delta 를 1e-15 로 주었음.
        assertEquals(vo.getDoubleType(), resultVO.getDoubleType(), isMysql
            ? 1e-14 : 1e-15);
        // float 에 대한 delta 를 1e-7 로 주었음.
        assertEquals(vo.getFloatType(), resultVO.getFloatType(), 1e-7);
        assertEquals(vo.getIntType(), resultVO.getIntType());
        assertEquals(vo.getLongType(), resultVO.getLongType());
        assertEquals(vo.getShortType(), resultVO.getShortType());
        // java.sql.Date 의 경우 Date 만 비교
        if (vo.getSqlDateType() != null) {
            assertEquals(vo.getSqlDateType().toString(), resultVO
                .getSqlDateType().toString());
        }
 
        // mysql 인 경우 timestamp 칼럼에 null 을 입력하면 현재 시각으로 insert 됨에 유의
        if (vo.getSqlTimestampType() == null && isMysql) {
            assertNotNull(resultVO.getSqlTimestampType());
        } else if (vo.getCalendarType() != null && isMysql) {
            String orgSeconds =
                Long.toString(vo.getSqlTimestampType().getTime());
            String mysqlSeconds =
                Long.toString(resultVO.getSqlTimestampType().getTime());
            assertEquals(orgSeconds.substring(0, orgSeconds.length() - 3),
                mysqlSeconds.substring(0, mysqlSeconds.length() - 3));
        } else {
            assertEquals(vo.getSqlTimestampType(), resultVO
                .getSqlTimestampType());
        }
        // java.sql.Time 의 경우 Time 만 비교
        if ((isHsql || isOracle || isTibero || isMysql)
            && vo.getSqlTimeType() != null) {
            assertEquals(vo.getSqlTimeType().toString(), resultVO
                .getSqlTimeType().toString());
        } else {
            assertEquals(vo.getSqlTimeType(), resultVO.getSqlTimeType());
        }
        assertEquals(vo.getStringType(), resultVO.getStringType());
        assertEquals(vo.isBooleanType(), resultVO.isBooleanType());
 
    }
 
    @Test
    public void testDataTypeTest() throws Exception {
        // 값을 세팅하지 않고 insert 해 봄 - id 는 int 의 초기값에 따라 0 임
        TypeTestVO vo = new TypeTestVO();
 
        // insert
        typeTestDAO.insertTypeTest("insertTypeTest", vo);
 
        // select
        TypeTestVO resultVO = typeTestDAO.selectTypeTest("selectTypeTest", vo);
 
        // check
        checkResult(vo, resultVO);
 
        try {
            // duplication 테스트
            typeTestDAO.insertTypeTest("insertTypeTest", vo);
 
            fail("키 값 duplicate 에러가 발생해야 합니다.");
        } catch (Exception e) {
            assertNotNull(e);
            assertTrue(e instanceof DataIntegrityViolationException);
            assertTrue(e.getCause() instanceof SQLException);
        }
 
        // DataType 테스트 데이터 입력 및 재조회
        vo = makeVO();
 
        // insert
        typeTestDAO.insertTypeTest("insertTypeTest", vo);
 
        // select
        resultVO = typeTestDAO.selectTypeTest("selectTypeTest", vo);
 
        // check
        checkResult(vo, resultVO);
 
    }
 
}
```

 위에서는 TypeTestVO 의 각 속성에 값을 세팅하지 않고 입력/조회, 키 값 중복 시 spring 의 DataIntegrityViolationException 이 발생하는지, 각 속성에 테스트 데이터(경계값 또는 의미있는 사용예 로써의 값)를 세팅하여 입력/조회 에 대한 처리를 확인해 봄으로써 java ↔ DBMS 의 타입 매핑의 예를 확인해 보았다. 특히 위의 makeVO 메서드 에서는 특정 javaType 에 대한 DBMS 의 db type 에 따라 경계값의 max value 가 달라질 수 있음을 확인할 수 있으며, checkResult 메서드에서는 특히 날짜 처리 타입과 관련하여 DBMS 에 따라 null 입력일 때 초기값 이나, 지원하는 정밀도(입력시 java 의 Date 류에서는 년월일시분초 를 넘어 상세하게 표현한 입력값 javaType 에 대해 jdbcType 의 결과 조회 시 날짜, 또는 시각 정보만으로 제한된다던지, 초 레벨의 정밀도가 java 에 비해 낮다던지)의 차이가 있음을 확인할 수 있다. java-jdbc type 에 대한 일반적인 매핑은 위 Hsqldb 의 예를 기본으로 이해하면 적합할 것으로 보며, 아래에서 특정 DBMS 의 DDL 예를 통해 각 데이터베이스 환경에서 Data Type 사용의 참고가 될 수 있기 바란다.

### Sample TYPETEST Table Oracle (10gR2 기준 테스트) DDL script

```sql
create table TYPETEST (
    id number(10,0) not null,
    bigdecimal_type number(19,2),
    boolean_type number(1,0), 
    byte_type number(3,0),
    char_type char(1),
    double_type double precision,
    float_type float,
    int_type number(10,0),
    long_type number(19,0),
    short_type number(5,0),
    string_type varchar2(255),
    date_type date,
    sql_date_type date,
    sql_time_type timestamp,
    sql_timestamp_type timestamp,
    calendar_type timestamp,
    primary key (id)
);
```

### Sample TYPETEST Table Mysql (5.X) DDL script

```sql
create table TYPETEST (
    id numeric(10,0) not null,
    bigdecimal_type numeric(19,2),
    boolean_type boolean, 
    byte_type tinyint,
    char_type char(1),
    double_type double,
    float_type float,
    int_type integer,
    long_type bigint,
    short_type smallint,
    string_type varchar(255),
    date_type date,
    sql_date_type datetime,
    sql_time_type time,
    sql_timestamp_type timestamp,
    calendar_type timestamp,
    primary key (id)
);
```

### Sample TYPETEST Table Tibero(3.x) DDL script

```sql
create table TYPETEST (
    id numeric(10,0) not null,
    bigdecimal_type number(19,2),
    boolean_type number(1), 
    byte_type number(3),
    char_type char(1),
    double_type double precision,
    float_type float,
    int_type integer,
    long_type integer, /* integer 가 bigint 의 범위까지 포함함 */
    short_type smallint,
    string_type varchar(255),
    date_type date,
    sql_date_type date,
    sql_time_type date,	/* time, timestamp 으로 설정 시 문제발생 */
    sql_timestamp_type timestamp,
    calendar_type timestamp,
    primary key (id)
);
```
