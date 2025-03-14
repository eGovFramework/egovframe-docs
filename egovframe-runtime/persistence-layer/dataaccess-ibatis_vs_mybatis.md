---
title: MyBatis 주요 변경점
linkTitle: "주요 변경사항"
description: MyBatis는 iBatis에서 패키지 구조와 용어가 변경되었으며, com.ibatis.*에서 org.apache.ibatis.*로 패키지 구조가 바뀌고, 여러 구문 및 속성들이 통합 또는 대체되었다. 예를 들어, sqlMap은 mapper로, parameterClass는 parameterType으로 변경되었다.
url: /egovframe-runtime/persistence-layer/dataaccess-mybatis/dataaccess-ibatis_vs_maybatis/
menu:
    depth:
        name: 주요 변경사항
        weight: 1
        parent: mybatis
---
# MyBatis 주요 변경점

 본 가이드는 MyBatis와 iBatis의 차이점을 설명한다.

## 변경된 용어(종합)

| iBatis | MyBatis | 비고 |
| --- | --- | --- |
| com.ibatis.\* | org.apache.ibatis.\* | 패키지 구조 변경 |
| SqlMapConfig | Configration | 용어변경 |
| sqlMap | mapper | 용어변경 |
| sqlMapClient | sqlSession | 구문대체 |
| rowHandler | resultHandler | 구문대체 |
| resultHandler | SqlSessionFactory | 구문대체 |
| parameterMap, parameterClass | parameterType | 속성 통합 |
| resultClass | resultType | 용어변경 |
| #var# | #{var} | 구문대체 |
| $var$ | ${var} | 구문대체 |
| <isEqual> , <isNull> | <if> | 구문대체 |

## 변경사항

### 패키지 구조 변경

| iBatis | MyBatis |
| --- | --- |
| com.ibatis.\* | org.apache.ibatis.\* |

 패키지 구조는 변경되었으나 기존에 iBatis 패키지명은 그대로 사용한다.

### MyBatis library 별도 제공

 Maven Dependency Information 예시

```xml
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.2.2</version>
</dependency>

<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.2.0</version>
</dependency>

```

### annotation 도입

- annotation 을 적극 도입하여 DAO 에 대해서 행하던 sqlMapClient DI 설정을 안 해도 된다.
- spring 2.5 대 부터 annotation 이 도입되어서 설정이 매우 간편해진 것처럼 무척 간편해 졌다.
- bean id sqlSessionFactory, sqlSessionTemplate 만 지정하면 된다.

### rowHandler 대체

- xml 및 대량 데이터 처리를 위해 사용하였던 rowHandler가 삭제되었다.
- sqlMapClient 가 없어지고 sqlSession 으로 대체 되었는데, sqlSession 의 API 를 살펴보니 large data 처리용 method 를 제공한다.
- rowHandler 가 resultHandler 로 바뀌었다.
- 큰 변화중 하나는 자바 어노테이션을 사용해서 xml을 사용하지 않고 모든 것을 자바로만 할 수 있게 되었다. 물론 Configration.xml 도 자바에서 직접 DataSource, Environment 등을 선언해서 클래스화 시킬 수 있다.
- 주의할 점은 xml로 Configure를 만들고 환경변수와 property를 클래스로도 만들었다면, 클래스 쪽이 나중에 읽어지게 돼서 xml로 되어있는 세팅이 자바 클래스에서 선언해 놓은 것으로 덮어써지게 된다. 혼란을 줄 수 있으니 한가지 방법만으로 프로젝트를 구성하는 것이 좋을 것이다.
- Configuration configuration = new Con…. 형식으로 선언을 하고 나서는 mapper도 xml이 아니고 configuration.addMapper(UserMapper.class) 형식으로 추가 해야 하기 때문에 어느 쪽으로 할 것인지 확실하게 결정을 하고 나서 진행해야 한다.

### 네임스페이스 방식 변경

- sqlMap 파일별로 줄여 놓은 이름을 사용했다면 이제 전체 경로(full path)로 사용하게 된다.(공식 설명서에서는 혼란을 줄이고 어떤 것이 호출되는지 정확하게 알 수 있으니 좋다고 기재)

| iBatis | MyBatis |
| --- | --- |
| &lt;sqlMap namespace=“User”&gt; | &lt;mapper namespace=“myBatis.mapper.UserMapper”&gt; |

 실제 자바쪽에서 호출할 때도 길게 호출하여야 한다.

```java
list = session.selectList("myBatis.mappers.UserMapper.getUserList");

```

 이런 경우에 위에서 이야기한 자바 어노테이션 (@Select)을 사용해서 mapper 파일을 xml이 아니고 자바로 만들어 놓으면 코드 힌트까지 사용해서 편하게 쓸 수 있다.

```java
UserMapper mapper = session.getMapper(UserMapper.class);

list = mapper.selectUserList();

```

## 변경되거나 추가된 속성들

 기존에 조건에 따라 변하는 쿼리를 만들기 위해서 사용되던 태그들이 변경되었다. 조금 더 직관적으로 바뀌었고 해당상황(Update, Select)등에 맞춰서 사용할 수 있는 태그들도 추가되었다.

- parameterMap은 더이상 사용하지 않게 되었다. parameterMap과 parameterClass 대신 parameterType 하나로 사용한다.
- resultMap은 여전히 남아있지만 resultClass 는 resultType 으로 변경되었다.
- parameterType과 resultType에는 기본형(int, byte, …. )부터 클래스 명까지 기존처럼 사용할 수 있다.
- 기존에 procedure를 호출하기 위해 사용하던 &lt;procedure&gt;가 사라지고 statementType 속성이 생겼다. PREPARED, STATEMENT, CALLABLE 중에 하나를 선택할 수 있고 기본값은 PREPARED이다.
- 파라미터를 매핑하기 위해서 사용하던 #var# 형태는 #{var} 로 바뀌었다. $var$ 역시 ${var} 형태로 사용하면 된다.

 참고) #{var}와 ${var}의 차이는 prepredStatement의 파라미터로 사용, String 값으로 사용.  
order by 같은 경우에 사용하기 위해서는 order by ${orderParam} 처럼 사용해야 한다.  
이 방법을 사용하는 경우 MyBatis가 자체적으로 쿼리의 적합성여부를 판단할 수 없기 때문에 사용자의 입력 값을 그대로 사용하는 것보다는 개발자가 미리 정해 놓은 값 등으로 변경하도록 해서 정확한 값이 들어올 수 있도록 해야 한다.

 sqlMap쪽에서 사용하던 typeAlias가 sqlMap이 바뀐 mapper 에서 사용되지 않고 Configration 파일에서 정의하도록 변경되었다.

```xml
<typeAliases>
    <typeAlias type="vo.UserVO" alias="User"/>
</typeAliases>

```

 Configuration 파일에 위의 형식처럼 Alias를 정의하면 전체 mapper 에서 사용할 수 있다.

### Dynamic Statement의 변화

- &lt;isEqual&gt; , &lt;isNull&gt; 등의 구문이 &lt;if&gt;로 통합되었다.

 &lt;if test=“userID != null”&gt; 형태로 간단하게 사용할 수 있다.  
&lt;dynamic&gt; 형태로 해서 where 조건절이나 and , or 를 동적으로 만들던 것이 &lt;where&gt;나 update에서 사용할 수 있는 &lt;set&gt; 등으로 변경되었다.

```xml
<select id="getUserList" resultType="User>
    SELECT * FROM TR_USER
        <where>
            <if test="isAdmin != null">
                authLevel = '1'
             </if>
          </where>
</select>

```

- trim, foreach 태그가 새로 추가

1) trim은 쿼리를 동적 생성 할 때에 쿼리를 연결하기 위해서 컴마(,)를 사용한 경우 마지막항목이 조건을 만족하지 못해서 생성된 쿼리 끝에 컴마가 붙어있다던가 하는 경우에 잘라낼 수 있다.
2) foreach는 반복적인 항목을 동적으로 넣을 때 사용할 수 있다. ( ex. where 조건절에서 in 을 사용하는 경우)

## 참고자료

- MyBatis 마이그레이션 가이드([http://code.google.com/p/mybatis/wiki/DocUpgrade3](http://code.google.com/p/mybatis/wiki/DocUpgrade3))
- [http://blog.naver.com/PostView.nhn?blogId=vikong&logNo=60180433051](http://blog.naver.com/PostView.nhn?blogId=vikong&logNo=60180433051)
