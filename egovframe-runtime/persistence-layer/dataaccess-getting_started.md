---
title: MyBatis 시작하기
linkTitle: "시작하기"
description: MyBatis 애플리케이션은 SqlSessionFactory 인스턴스를 사용하며, 이를 SqlSessionFactoryBuilder를 통해 XML 설정 파일에서 빌드할 수 있다. Resources 유틸 클래스를 사용하여 클래스패스 또는 다른 위치에서 자원을 쉽게 로드할 수 있다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis/dataaccess-getting_started/
menu:
    depth:
        name: 시작하기
        weight: 2
        parent: mybatis
---
## 시작하기

 모든 MyBatis 애플리케이션은 SqlSessionFactory 인스턴스를 사용한다. SqlSessionFactory 인스턴스는 SqlSessionFactoryBuilder 를 사용하여 만들 수 있다. SqlSessionFactoryBuilder 는 XML 설정파일에서 SqlSessionFactory 인스턴스를 빌드할 수 있다;

### XML에서 SqlSessionFactory 빌드하기

 XML 파일에서 SqlSessionFactory 인스턴스를 빌드하는 것은 매우 간단하다. 설정을 위해 클래스패스 자원을 사용하는 것을 추천하나, 파일 경로나 file URL 로부터 만들어진 InputStream 인스턴스를 사용할 수도 있다. MyBatis 는 클래스패스와 다른 위치에서 자원을 로드하는 것으로 좀더 쉽게 해주는 Resources 라는 유틸성 클래스를 가지고 있다.

```java
String resource = "org/mybatis/example/mybatis-config.xml";
InputStream inputStream = Resources.getResourceAsStream(resource);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

```

 XML 설정파일에서 지정하는 MyBatis 의 핵심이 되는 설정은 트랜잭션을 제어하기 위한 TransactionManager 과 함께 데이터베이스 Connection 인스턴스를 가져오기 위한 DataSource 를 포함한다. 예제 :

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <environments default="development">
    <environment id="development">
      <transactionManager type="JDBC"/>
      <dataSource type="POOLED">
        <property name="driver" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
      </dataSource>
    </environment>
  </environments>
  <mappers>
    <mapper resource="org/mybatis/example/BlogMapper.xml"/>
  </mappers>
</configuration>

```

 좀 더 많은 XML 설정방법이 있지만, 위 예제에서는 가장 핵심적인 부분만을 보여주고 있다. XML 가장 위부분에서는 XML 문서의 유효성체크를 위해 필요하다. environment 요소는 트랜잭션 관리와 커넥션 풀링을 위한 환경적인 설정을 나타낸다. mappers 요소는 SQL 코드와 매핑 정의를 가지는 XML 파일인 mapper 의 목록을 지정한다.

### XML 을 사용하지 않고 SqlSessionFactory 빌드하기

 XML 보다 자바를 사용해서 직접 설정하길 원한다면, XML 파일과 같은 모든 설정을 제공하는 Configuration 클래스를 사용하면 된다.

```java
DataSource dataSource = DeptDataSourceFactory.getDeptDataSource();
TransactionFactory transactionFactory = new JdbcTransactionFactory();
Environment environment = new Environment("development", transactionFactory, dataSource);
Configuration configuration = new Configuration(environment);
configuration.addMapper(DeptMapper.class);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(configuration);

```

 이 설정에서 추가로 해야 할 일은 Mapper 클래스를 추가하는 것이다. Mapper 클래스는 SQL 매핑 어노테이션을 가진 자바 클래스이다. 어쨌든 자바 어노테이션의 몇 가지 제약과 몇 가지 설정방법의 복잡함에도 불구하고, XML 매핑은 세부적인 매핑을 위해 언제든 필요하다.

### SqlSessionFactory 에서 SqlSession 만들기

 SqlSessionFactory 이름에서 보듯이, SqlSession 인스턴스를 만들 수 있다. SqlSession 은 데이터베이스에 대해 SQL 명령어를 실행하기 위해 필요한 모든 메서드를 가지고 있다. 그래서 SqlSession 인스턴스를 통해 직접 SQL 구문을 실행할 수 있다. 예를 들면 :

```java
 SqlSession session = sqlSessionFactory.openSession();
 try {
   Dept dept = session.selectOne("egovframework.rte.psl.dataaccess.DeptMapper.selectDept", 101);
 } finally {
   session.close();
 }

```

 이 방법이 MyBatis 의 이전버전을 사용한 사람이라면 굉장히 친숙할 것이다. 하지만 좀더 좋은 방법이 생겼다. 주어진 SQL 구문의 파라미터와 리턴값을 설명하는 인터페이스(예를 들면, DeptMapper.class )를 사용하여, 문자열 처리 오류나 타입 캐스팅 오류 없이 좀더 타입에 안전하고 깔끔하게 실행할 수 있다.

 예를 들면:

```java
SqlSession session = sqlSessionFactory.openSession();
try {
  DeptMapper mapper = session.getMapper(DeptMapper.class);
  Dept dept = mapper.selectDept(101);
} finally {
  session.close();
}

```

 그럼 좀더 자세히 살펴보자.

### 매핑된 SQL 구문 살펴보기

 이 시점에 SqlSession 이나 Mapper 클래스가 정확히 어떻게 실행되는지 궁금할 것이다. 매핑된 SQL 구문에 대한 내용이 가장 중요하다. 그래서 이 문서 전반에서 가장 자주 다루어진다. 하지만 다음의 두가지 예제를 통해 정확히 어떻게 작동하는지에 대해서는 충분히 이해하게 될 것이다.

 위 예제처럼, 구문은 XML 이나 어노테이션을 사용해서 정의할 수 있다. 그럼 먼저 XML 을 보자. MyBatis 가 제공하는 대부분의 기능은 XML 을 통해 매핑 기법을 사용한다. 이전에 MyBatis 를 사용했었다면 쉽게 이해되겠지만, XML 매핑 문서에 이전보다 많은 기능이 추가되었다. SqlSession 을 호출하는 XML 기반의 매핑 구문이다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper   PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" 
     "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="egovframework.rte.psl.dataaccess.DeptMapper">
	<select id="selectDept" 
                parameterType="int" 
                     resultType="Dept">
		<![CDATA[
			select *
			from   DEPT
			where  DEPT_NO = #{deptNo}
		]]>
	</select>
</mapper>

```

 한 개의 매퍼 XML 파일에는 많은 수의 매핑 구문을 정의할 수 있다. XML 도입부의 헤더와 doctype 을 제외하면, 나머지는 쉽게 이해되는 구문의 형태이다. 여기선 egovframework.rte.psl.dataaccess.DeptMapper 명명공간에서 selectDept 라는 매핑 구문을 정의했고, 이는 결과적으로 egovframework.rte.psl.dataaccess.DeptMapper.selectDept 형태로 실제 명시되게 된다. 그래서 다음처럼 사용하게 되는 셈이다.

 Dept dept = (Dept) session.selectOne(“egovframework.rte.psl.dataaccess.DeptMapper.selectDept”, 101); 이건 마치 패키지를 포함한 전체 경로의 클래스내 메서드를 호출하는 것과 비슷한 형태이다. 이 이름은 매핑된 select 구문의 이름과 파라미터 그리고 리턴 타입을 가진 명명공간과 같은 이름의 Mapper 클래스와 직접 매핑될 수 있다. 이건 위에서 본 것과 같은 Mapper 인터페이스의 메서드를 간단히 호출하도록 허용한다. 위 예제에 대응되는 형태는 아래와 같다.

 DeptMapper mapper = session.getMapper(DeptMapper.class); Dept dept = mapper.selectDept(101); 두번째 방법은 많은 장점을 가진다. 먼저 문자열에 의존하지 않는다는 것이다. 이는 애플리케이션을 좀더 안전하게 만든다. 두번째는 개발자가 IDE 를 사용할 때, 매핑된 SQL 구문을 사용할 때의 수고를 덜어준다. 세번째는 리턴 타입에 대해 타입 캐스팅을 하지 않아도 된다. 그래서 DeptMapper 인터페이스는 깔끔하고 리턴 타입에 대해 타입에 안전하며 이는 파라미터에도 그대로 적용된다.

#### 참고 : 명명공간(Namespaces)에 대한 설명

 명명공간(Namespaces) 이 이전 버전에서는 사실 선택 사항이었다. 하지만 이제는 패키지 경로를 포함한 전체 이름을 가진 구문을 구분하기 위해 필수로 사용해야 한다.

 명명공간은 인터페이스 바인딩을 가능하게 한다. 명명공간을 사용하고 자바 패키지의 명명공간을 두면 코드가 깔끔해 지고 MyBatis 의 사용성이 크게 향상될 것이다.

 이름 분석(Name Resolution): 타이핑을 줄이기 위해, MyBatis 는 구문과 결과맵, 캐시등의 모든 설정요소를 위한 이름 분석 규칙을 사용한다.

- “com.mypackage.MyMapper.selectAllThings” 과 같은 패키지를 포함한 전체 경로명(Fully qualified names)은 같은 형태의 경로가 있다면 그 경로내에서 직접 찾는다.
- “selectAllThings” 과 같은 짧은 형태의 이름은 모호하지 않은 엔트리를 참고하기 위해 사용될 수 있다. 그래서 짧은 이름은 모호해서 에러를 자주 보게 되니 되도록이면 전체 경로를 사용해야 할 것이다.

## 참고 자료

- [http://mybatis.github.io/mybatis-3/ko](http://mybatis.github.io/mybatis-3/ko)
- [http://mybatis.github.io/mybatis-3/getting-started.html](http://mybatis.github.io/mybatis-3/getting-started.html)
