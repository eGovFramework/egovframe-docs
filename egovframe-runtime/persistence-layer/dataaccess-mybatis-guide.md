---
title: MyBatis 적용 가이드
linkTitle: "MyBatis 적용 가이드"
description: 전자정부 표준프레임워크 기반 MyBatis 적용 가이드이다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis-guide/
menu:
    depth:
        name: MyBatis 적용 가이드
        weight: 4
        parent: "persistence-layer"
---
# MyBatis 적용 가이드

## 개요
전자정부 표준프레임워크 기반 MyBatis 적용 가이드이다.

📁 [ex-dataaccess-mybatis.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:rte2:psl:dataaccess:ex-dataaccess-mybatis.zip)

## Step 1. pom.xml 변경

표준프레임워크 dataaccess artifact version을 다음과 같이 2.7.0으로 변경한다.

```xml
<!-- 실행환경 라이브러리 -->
<dependency>
	<groupId>egovframework.rte</groupId>
	<artifactId>egovframework.rte.psl.dataaccess</artifactId>
	<version>2.7.0</version>
</dependency>
```

## Step 2. 환경 설정

### Step 2.1 XML 설정

Spring XML 설정 파일 상(ex: context-mapper.xml)에 다음과 같은 sqlSession bean을 추가한다.

Ex) context-mapper.xml

```xml
<!-- SqlSession setup for MyBatis Database Layer -->
<bean id="sqlSession" class="org.mybatis.spring.SqlSessionFactoryBean">
	<property name="dataSource" ref="dataSource" />
	<property name="mapperLocations" value="classpath:/sqlmap/mappers/**/*.xml" />
</bean>
```

### Step 2.2 mapper xml 작성

MyBatis 가이드에 따라 query xml을 작성한다. (2.1의 예제 상 지정된 mapperLocations 위치)

## Step 3. DAO 작성

DAO의 경우는 다음과 같이 3가지 방식이 가능하다.

| 방식 | 설명 | 비고 |
| --- | --- | --- |
| 기존 DAO 클래스 방식 | @Repository 지정 및 EgovAbstractMapper extends 활용 | 기존 iBatis와 같은 방식 |
| Mapper interface 방식 | Mapper 인터페이스 작성 및 @Mapper annotation 지정 | @Mapper는 marker annotation(표준프레임워크 제공) |
| Annotation 방식 | query xml 없이 mapper 인터페이스 상 @Select, @Insert 등을 활용 | Dynamic SQL 등의 사용에 제약이 있음 |

### 3.1 기존 DAO 형태로 사용하는 경우

@Repository 지정된 class에 EgovAbstractMapper를 extends 하여 insert, update, delete, selectByPk, list 메서드를 활용한다.

```java
@Repository("deptMapper")
public class DeptMapper extends EgovAbstractMapper {

    public void insertDept(String queryId, DeptVO vo) {
        insert(queryId, vo);
    }
 
    public int updateDept(String queryId, DeptVO vo) {
        return update(queryId, vo);
    }
 
    public int deleteDept(String queryId, DeptVO vo) {
        return delete(queryId, vo);
    }
 
    public DeptVO selectDept(String queryId, DeptVO vo) {
        return (DeptVO)selectByPk(queryId, vo);
    }
 
    @SuppressWarnings("unchecked")
    public List<DeptVO> selectDeptList(String queryId, DeptVO searchVO) {
        return list(queryId, searchVO);
    }
}
```

### 3.2 Mapper interface 사용 방식

Mapper 인터페이스 작성 시 다음과 같이 @Mapper annotation을 사용한다.

(패키지를 포함하는 클래스명 부분이 mapper xml 상의 namespace로 선택되고 인터페이스 메서드가 query id로 호출되는 방식)

```java
@Mapper("employerMapper")
public interface EmployerMapper  {

    public List<EmpVO> selectEmployerList(EmpVO vo);
 
    public EmpVO selectEmployer(BigDecimal empNo);
 
    public void insertEmployer(EmpVO vo);
 
    public int updateEmployer(EmpVO vo);
 
    public int deleteEmployer(BigDecimal empNo);

}
```

이 경우는 xml 설정상에 다음과 같은 MapperConfigurer 설정이 필요하다.

Ex: context-mapper.xml

```xml
<bean class="egovframework.rte.psl.dataaccess.mapper.MapperConfigurer">
	<property name="basePackage" value="egovframework.rte.**.mapper" />
</bean>
```

basePackage에 지정된 패키지 안에서 @Mapper annotation을 스캔하는 설정이다.

⇒ @Mapper로 지정된 인터페이스를 @Service에서 injection 하여 사용한다.

```java
public class EmployerMapperTest {

    @Resource(name = "employerMapper")
    EmployerMapper employerMapper;

    @Test
    public void testInsert() throws Exception {
        EmpVO vo = makeVO();

        // insert
        employerMapper.insertEmployer(vo);

        // select
        EmpVO resultVO = employerMapper.selectEmployer(vo.getEmpNo());

        // check
        checkResult(vo, resultVO);
    }
}
```

### 3.3 Annotation 사용 방식

mapper xml 작성 없이 Mapper 인터페이스 상에 @Select, @Insert, @Update, @Delete 등의 annotation을 통해 query가 지정되어 사용된다.

```java
@Mapper("departmentMapper")
public interface DepartmentMapper  {

    @Select("select DEPT_NO as deptNo, DEPT_NAME as deptName, LOC as loc from DEPT where DEPT_NO = #{deptNo}")
    public DeptVO selectDepartment(BigDecimal deptNo);
    
    @Insert("insert into DEPT(DEPT_NO, DEPT_NAME, LOC) values (#{deptNo}, #{deptName}, #{loc})")
    public void insertDepartment(DeptVO vo);
    
    @Update("update DEPT set DEPT_NAME = #{deptName}, LOC = #{loc} WHERE DEPT_NO = #{deptNo}")
    public int updateDepartment(DeptVO vo);
    
    @Delete("delete from DEPT WHERE DEPT_NO = #{deptNo}")
    public int deleteDepartment(BigDecimal deptNo);

}
```

⇒ 이 경우는 별도의 mapper xml을 만들 필요는 없지만, dynamic query를 사용하지 못하는 등의 제약사항이 따른다.