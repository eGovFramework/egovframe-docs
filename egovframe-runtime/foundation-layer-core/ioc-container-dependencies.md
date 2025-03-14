---
title: Dependencies
linkTitle: "Dependencies"
description: 일반적인 엔터프라이즈 애플리케이션은 여러 객체가 협력하여 작동하며, Spring에서는 이러한 객체들을 각각 독립적인 빈으로 정의한다. Spring 프레임워크를 통해 독립적으로 정의된 빈들이 협업하여 애플리케이션의 목표를 달성하는 방법을 설명한다.
url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-dependencies/"
menu:
    depth:
        name: Dependencies
        weight: 2
        parent: "ioc-container"
---
# Dependencies

## 개요

 일반적인 엔터프라이즈 애플리케이션은 단일 객체(또는 Spring 용어로 빈)로만 이루어지지 않고 간단한 애플리케이션도 최종 사용자에게 일관된 사용자 경험을 제공하기 위해 여러 객체가 함께 작동한다. 이러한 객체들은 독립적으로 존재하며, Spring 프레임워크를 사용하여 각각의 빈으로 정의된다. 여기서는 독립적으로 정의된 여러 빈들이 협업하여 목표를 달성하는 방법에 대해 설명한다.

## 설명

### 종속성 삽입(Injecting dependencies)

 종속성 삽입(Dependency Injection(DI))의 기본적인 원칙은 객체는 단지 생성자나 set 메소드를 통해서만 종속성(필요로 하는 객체)를 정의한다는 것이다.  
그러면 Container는 Bean 객체를 생성할 때, Bean이 정의한 종속성을 추가하게 되는데 이는 Bean이 스스로 필요한 객체를 생성하거나 찾는 등의 제어를 가지는 것과는 반대의 개념으로 Inversion of Control(IoC)라고 부른다.  
종속성 삽입에는 두 가지 방법이 있다. [Constructor Injection](#constructor-injection)과 [Setter Injection](#setter-injection)이다.

#### Constructor Injection

 생성자(Constructor) 기반의 DI는 다수의 arguments를 갖는 생성자를 호출하여 종속성을 주입한다. &lt;constructor-arg&gt; element를 사용한다.

 ```java
package x.y;
 
public class Foo {
    public Foo(Bar bar, Baz baz) {
        // ...
    }
}
```

 ```xml
<beans>
    <bean name="foo" class="x.y.Foo">
        <constructor-arg>
            <bean class="x.y.Bar"/>
        </constructor-arg>
        <constructor-arg>
            <bean class="x.y.Baz"/>
        </constructor-arg>
    </bean>
</beans>
```

 만약, &lt;value&gt;true&lt;/value&gt;와 같이 type이 명확하지 않은 값을 사용하는 경우, Spring은 생성자의 어떤 argument에 해당하는지 결정할 수 없다.

 ```java
package examples;
 
public class ExampleBean {
    // No. of years to the calculate the Ultimate Answer
    private int years;
 
    // The Answer to Life, the Universe, and Everything
    private String ultimateAnswer;
 
    public ExampleBean(int years, String ultimateAnswer) {
        this.years = years;
        this.ultimateAnswer = ultimateAnswer;
    }
}
```

##### Constructor Argument Type Matching

 위와 같은 경우, 'type' attribute를 통해서 각 argument의 타입을 지정할 수 있다.

 ```xml
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg type="int" value="7500000"/>
    <constructor-arg type="java.lang.String" value="42"/>
</bean>
```

##### Constructor Argument Index

 위와 같은 경우 'index' attribute를 통해서 각 argument의 위치를 지정할 수 있다.

 ```xml
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg index="0" value="7500000"/>
    <constructor-arg index="1" value="42"/>
</bean>
```

 (\* ***index***는 0부터 시작한다.)

#### Setter Injection

 Setter 기반의 DI는 argument가 없는 생성자를 통해 bean 객체가 생성된 후, setter 메소드를 호출하여 종속성을 주입한다. &lt;property&gt; element를 사용한다.

 ```xml
<bean id="exampleBean" class="examples.ExampleBean">
    <!-- setter injection using the nested <ref/> element -->
    <property name="beanOne"><ref bean="anotherExampleBean"/></property>
 
    <!-- setter injection using the neater 'ref' attribute -->
    <property name="beanTwo" ref="yetAnotherBean"/>
    <property name="integerProperty" value="1"/>
</bean>
 
<bean id="anotherExampleBean" class="examples.AnotherBean"/>
<bean id="yetAnotherBean" class="examples.YetAnotherBean"/>
```

 ```java
public class ExampleBean {
    private AnotherBean beanOne;
    private YetAnotherBean beanTwo;
    private int i;
 
    public void setBeanOne(AnotherBean beanOne) {
        this.beanOne = beanOne;
    }
 
    public void setBeanTwo(YetAnotherBean beanTwo) {
        this.beanTwo = beanTwo;
    }
 
    public void setIntegerProperty(int i) {
        this.i = i;
    }    
}
```

### 종속성 상세 설정(Dependencies and configuration in detail)

 본 장은 종속성 삽입에 사용되는 &lt;constructor-arg&gt;와 &lt;property&gt; element의 sub-element type을 설명한다.

#### 명확한 값(Straight values(primitives, Strings, etc.))

 사람이 인식 가능한 문자열 형태를 &lt;value&gt; tag를 사용하여 표현한다. String을 argument나 property의 type에 맞춰 변환해준다.

 ```xml
<bean id="myDataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
    <!-- results in a setDriverClassName(String) call -->
    <property name="driverClassName">
        <value>com.mysql.jdbc.Driver</value>
    </property>
    <property name="url">
        <value>jdbc:mysql://localhost:3306/mydb</value>
    </property>
    <property name="username">
        <value>root</value>
    </property>
    <property name="password">
        <value>masterkaoli</value>
    </property>
</bean>
```

 &lt;value&gt; element 대신 'value' attribute를 사용할 수도 있다.

 ```xml
<bean id="myDataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
    <!-- results in a setDriverClassName(String) call -->
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql://localhost:3306/mydb"/>
    <property name="username" value="root"/>
    <property name="password" value="masterkaoli"/>
</bean>
```

#### 다른 bean 참조(References to other beans(collaborators))

 ref element는 Container 안에 있는 다른 bean을 참조한다. 참조할 객체를 지정하는 방식에는 3가지가 있다.

1.  bean attribute  
    가장 일반적인 형태로 같은 Container 또는 부모 Container에 포함된 bean 객체를 참조한다. 'bean' attribute는 대상 bean의 'id' 또는 여러 'name'들 중. 하나와 같아야 한다.
    
     ```xml
    <ref bean="someBean"/>
    ```
    
2.  local attribute  
    같은 XML 설정 파일 내의 bean 객체를 참조한다. 'local' attribute는 반드시 대상 bean의 'id'와 같아야 한다. 만약 대상 bean이 같은 XML 파일에 존재한다면. local을 사용하는 것이 좋다.
    
     ```xml
    <ref local="someBean"/>
    ```
    
3.  parent attribute  
    현재 Container의 부모 Container의 bean 객체를 참조한다. 'parent' attribute는 대상 bean의 'id' 또는 여러 'name'들 중 하나와 같아야 한다.
    
     ```xml
    <!-- in the parent context -->
    <bean id="accountService" class="com.foo.SimpleAccountService">
        <!-- insert dependencies as required as here -->
    </bean>
    ```
    
     ```xml
    <!-- in the child (descendant) context -->
    <bean id="accountService"  <-- notice that the name of this bean is the same as the name of the 'parent' bean
        class="org.springframework.aop.framework.ProxyFactoryBean">
        <property name="target">
            <ref parent="accountService"/>  <-- notice how we refer to the parent bean
        </property>
        <!-- insert other configuration and dependencies as required as here -->
    </bean>
    ```
    

#### Inner beans

 &lt;property/&gt; 또는 &lt;constructor-arg/&gt; element 안에 있는 &lt;bean/&gt; element를 ***inner bean***이라고 한다. Inner bean은 id나 name을 정의할 필요가 없다. 정의한다 해도 Container에서 무시하기 때문에 정의하지 않는 것이 좋다.

 ```xml
<bean id="outer" class="...">
    <!-- instead of using a reference to a target bean, simply define the target bean inline -->
    <property name="target">
        <bean class="com.example.Person"> <!-- this is the inner bean -->
            <property name="name" value="Fiona Apple"/>
            <property name="age" value="25"/>
        </bean>
    </property>
</bean>
```

 Inner bean의 'scope' flag와 'id', 'name'은 무시된다. Inner bean의 scope은 항상 prototype이다. 따라서 inner bean을 다른 bean에 주입하는 것은 불가능한다.

#### Collections

 Java Collection 타입인 List, Set, Map, Properties를 표현하기 위해 &lt;list/&gt;, &lt;set/&gt;, &lt;map/&gt;, &lt;props/&gt; element가 사용된다.

 ```xml
<bean id="moreComplexObject" class="example.ComplexObject">
    <!-- results in a setAdminEmails(java.util.Properties) call -->
    <property name="adminEmails">
        <props>
            <prop key="administrator">administrator@example.org</prop>
            <prop key="support">support@example.org</prop>
            <prop key="development">development@example.org</prop>
        </props>
    </property>
    <!-- results in a setSomeList(java.util.List) call -->
    <property name="someList">
    <list>
        <value>a list element followed by a reference</value>
        <ref bean="myDataSource" />
    </list>
    </property>
    <!-- results in a setSomeMap(java.util.Map) call -->
    <property name="someMap">
        <map>
            <entry>
                <key>
                    <value>an entry</value>
                </key>
                <value>just some string</value>
            </entry>
            <entry>
                <key>
                    <value>a ref</value>
                </key>
                <ref bean="myDataSource" />
            </entry>
        </map>
    </property>
    <!-- results in a setSomeSet(java.util.Set) call -->
    <property name="someSet">
        <set>
            <value>just some string</value>
            <ref bean="myDataSource" />
        </set>
    </property>
</bean>
```

 map의 key와 value, set의 value의 값은 아래 element 중 하나가 될 수 있다.

 ```java
bean | ref | idref | list | set | map | props | value | null

```

##### Collection 병합(Collection merging)

 Container는 collection 병합 기능을 제공한다. Bean 정의 상속을 사용하여 부모 bean 정의의 &lt;list/&gt;, &lt;map/&gt;, &lt;set/&gt;, &lt;props/&gt; element와 자식 bean 정의의 &lt;list/&gt;, &lt;map/&gt;, &lt;set/&gt;, &lt;props/&gt; element를 병합할 수 있다.

 ```xml
<beans>
<bean id="parent" abstract="true" class="example.ComplexObject">
    <property name="adminEmails">
        <props>
            <prop key="administrator">administrator@example.com</prop>
            <prop key="support">support@example.com</prop>
        </props>
    </property>
</bean>
<bean id="child" parent="parent">
    <property name="adminEmails">
        <!-- the merge is specified on the *child* collection definition -->
        <props merge="true">
            <prop key="sales">sales@example.com</prop>
            <prop key="support">support@example.co.uk</prop>
        </props>
    </property>
</bean>
<beans>
```

 위 설정에 따라 생성된 child bean 객체의 adminEmails는 아래와 같은 값을 가진다.

 ```java
administrator=administrator@example.com
sales=sales@example.com
support=support@example.co.uk

```

#### Nulls

 null 값을 사용하기 위해서 &lt;null/&gt; element를 사용한다. Spring는 argument가 없을 경우 빈 문자열(””)로 인식한다.

 ```xml
<bean class="ExampleBean">
    <property name="email"><value/></property>
</bean>
```

 위 설정에 따르면, email의 값은 ”“이다. 다음은 null값을 갖는 예제이다.

 ```xml
<bean class="ExampleBean">
    <property name="email"><null/></property>
</bean>
```

#### 간편한 설정 방법(Shortcuts and other convenience options for XML-based configuration metadata)

##### XML-based configuration metadata shortcuts

 &lt;property/&gt;, &lt;constructor-arg/&gt;, &lt;entry/&gt; element는 모두 &lt;value/&gt; element 대신에 'value' attribute를 사용할 수 있다.

 ```xml
<property name="myProperty">
    <value>hello</value>
</property>
```

 ```xml
<constructor-arg>
    <value>hello</value>
</constructor-arg>
```

 ```xml
<entry key="myKey">
    <value>hello</value>
</entry>
```

 위 설정은 아래와 동일한 설정이다.

 ```xml
<property name="myProperty" value="hello"/>
```

 ```xml
<constructor-arg value="hello"/>
```

 ```xml
<entry key="myKey" value="hello"/>
```

 &lt;property/&gt;, &lt;constructor-arg/&gt; element는 &lt;ref/&gt; element 대신에 'ref' attribute를 사용할 수 있다.

 ```xml
<property name="myProperty">
    <ref bean="myBean">
</property>
```

 ```xml
<constructor-arg>
    <ref bean="myBean">
</constructor-arg>
```

 위 설정은 아래와 동일한 설정이다.

 ```xml
<property name="myProperty" ref="myBean"/>
```

 ```xml
<constructor-arg ref="myBean"/>
```

 단, shortcut은 &lt;ref bean="xxx"&gt;와 동일하다. &lt;ref local="xxx"&gt;에 해당하는 shortcut은 없다.

 &lt;entry/&gt; element는 'key' / 'key-ref'와 'value' / 'value-ref' attribute를 사용할 수 있다.

 ```xml
<entry>
    <key>
        <ref bean="myKeyBean" />
    </key>
    <ref bean="myValueBean" />
</entry>
```

 위 설정은 아래와 같은 설정이다.

 ```xml
<entry key-ref="myKeyBean" value-ref="myValueBean"/>
```

##### The p-namespace and how to use it to configure properties

 ''&lt;property/&gt;'' element 대신 “p-namespace”를 사용하여 XML 설정을 작성할 수 있다. 아래 classic bean과 p-namespace bean은 동일한 Bean 설정이다.

 ```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:p="http://www.springframework.org/schema/p"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
 
    <bean name="classic" class="com.example.ExampleBean">
        <property name="email" value="foo@bar.com/>
    </bean>
 
    <bean name="p-namespace"
        class="com.example.ExampleBean"
        p:email="foo@bar.com"/>
</beans>
```

 아래 예제는 다른 bean 객체의 참조를 삽입하는 예제이다. Attribute 이름 끝에 '-ref'를 붙이면 참조로 인식한다.

 ```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:p="http://www.springframework.org/schema/p"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
 
    <bean name="john-classic" class="com.example.Person">
        <property name="name" value="John Doe"/>
        <property name="spouse" ref="jane"/>
    </bean>
 
    <bean name="john-modern" 
        class="com.example.Person"
        p:name="John Doe"
        p:spouse-ref="jane"/>
 
    <bean name="jane" class="com.example.Person">
        <property name="name" value="Jane Doe"/>
    </bean>
</beans>
```

#### Compound property names

 복합 형식의 property 이름도 사용 가능하다.

 ```xml
<bean id="foo" class="foo.Bar">
    <property name="fred.bob.sammy" value="123" />
</bean>
```

 foo bean은 fred property를 가지고, fred property는 bob property를 가진다. 그리고 bob property는 sammy property를 가지고, 마지막 sammy property가 123을 값으로 가진다. 이 작업이 정상적으로 동작하려면 bean이 생성되었을 때, foo의 fred property, fred의 bob property는 반드시 null이 아니어야 한다. 그렇지 않을 경우 NullPointerException이 발생한다.

### depends-on 사용(Using depends-on)

 대부분의 경우, bean들간의 종속성은 ''&lt;ref/&gt;'' element에 의해 표현된다. 하지만 드물게 이런 종속성이 직접 나타나지 않는 경우도 있다(예를 들면, database driver 등록처럼 static 메소드에 의해 초기화되어야 하는 경우 등). 이런 경우 'depends-on' attribute를 사용하여 명시적으로 종속성을 표현할 수 있다.

 ```xml
<bean id="beanOne" class="ExampleBean" depends-on="manager"/>
 
<bean id="manager" class="ManagerBean" />
```

 만약 다수의 bean에 대한 종속성을 표현하고 하는 경우에는, 'depends-on' attribute의 값으로 bean 이름을 나열하면 된다. bean 이름의 구분자로는 콤마(','), 공백문자(' '), 세미콜론(';') 등을 사용할 수 있다.

 ```xml
<bean id="beanOne" class="ExampleBean" depends-on="manager,accountDao">
    <property name="manager" ref="manager" />
</bean>
 
<bean id="manager" class="ManagerBean" />
<bean id="accountDao" class="x.y.jdbc.JdbcAccountDao" />
```

### 늦은 객체화(Lazily-instantiated beans)

 ApplicationContext는 시작시에 모든 singleton bean을 선객체화(pre-instantiate)한다. 선객체화(pre-instantiate)는 초기화 과정에서 모든 singleton baen을 생성하고 설정한다는 것을 의미한다. 일반적으로 선객체화가 좋은 방식인데, 왜냐하면 잘못된 설정이 있는 경우, 즉시 발견할 수 있기 때문이다.

 어쨌거나, 이런 방식을 원하지 않을 경우도 있다. 만약 ApplicationContext에 의해 선 객체화 되는 singleton bean을 원하지 않을 경우, 선택적으로 bean 정의에 늦은 객체화(lazy-initailized)를 설정할 수 있다. 늦은 객체화(lazy-initailized)로 설정된 bean은 시작 시에 생성되는 것이 아니라, 처음으로 필요로 했을 때 생성된다.

 XML 설정에서는 ''&lt;bean/&gt;'' element의 'lazy-init' attribute를 사용한다.

 ```xml
<bean id="lazy" class="com.foo.ExpensiveToCreateBean" lazy-init="true"/>
 
<bean name="not.lazy" class="com.foo.AnotherBean"/>
```

 늦은 객체화에 대해서 이해하고 있어야 하는 것은, 만약 늦은 객체화로 설정된 bean에 대해서 그렇지 않은 singleton bean이 종속성을 가지고 있다면, ApplicationContext는 시작 시에 singleton bean이 종속하고 있는 모든 bean을 생성한다는 것이다. 즉, 명시적으로 늦은 객체화로 선언한 bean이라도 시작 시에 생성될 수 있다.

 그리고, &lt;beans/&gt; element의 'default-lazy-init' attribute를 사용하여 Container 레벨에서의 늦은 객체화를 설정할 수 있다.

 ```xml
<beans default-lazy-init="true">
    <!-- no beans will be pre-instantiated... -->
</beans>
```

### 자동엮기(Autowiring collaborators)

 Spring Container는 서로 관계된 bean들을 자동으로 엮어(***autowire***)줄 수 있다. 자동엮기(autowiring)는 각각의 bean 단위로 설정된다. 자동엮기(autowiring) 기능을 사용하면 property나 생성자 argument를 지정할 필요가 없어지므로, 타이핑일 줄일 수 있다. 자동엮기(autowiring)에는 5가지 모드가 있으며, XML 기반 설정에서는 &lt;bean/&gt; element의 'autowire' attribute를 사용하여 설정할 수 있다.

| Mode | 설명 |
| --- | --- |
| no | 자동엮기를 사용하지 않는다. Bean에 대한 참조는 ref element를 사용하여 지정해야만 한다. 이 모드가 기본(default)이다. |
| byName | Property 이름으로 자동엮기를 수행한다. Property의 이름과 같은 이름을 가진 bean을 찾아서 엮어준다. |
| byType | Property 타입으로 자동엮기를 수행한다. Property의 타입과 같은 타입을 가진 bean을 찾아서 엮어준다. 만약 같은 타입을 가진 bean이 Container에 둘 이상 존재할 경우 exception이 발생한다. 만약 같은 타입을 가진 bean이 존재하지 않는 경우, 아무 일도 발생하지 않는다; 즉, property에는 설정되지 않는다. |
| constructor | ***byType***과 유사하지만, 생성자 argument에만 적용된다. 만약 같은 타입의 bean이 존재하지 않거나 둘 이상 존재할 경우, exception이 발생한다. |
| autodetect | Bean class의 성질에 따라 ***constructor***와 ***byType*** 모드 중 하나를 선택한다. 만약 default 생성자가 존재하면, ***byType*** 모드가 적용된다. |

 만약 종속성을 property나 constructor-arg를 사용하여 명시적으로 설정한 경우, 자동엮기(autowiring) 설정은 무시된다.

#### Bean을 자동엮기 대상에서 제외하는 방법(Excluding a bean from being available from autowiring

 &lt;bean/&gt; element의 'autowire-candidate' attribute 값을 'false'로 설정함으로써, 대상 bean이 다른 bean에 의해 자동엮임을 당하는 것을 방지할 수 있다.

### 종속성 검사(Checking for dependencies)

 Spring IoC Container는 bean의 미해결 종속성의 존재를 검사할 수 있다. 이 기능은 bean의 모든 property가 지정되었는지는 확인하고 싶을 때 유용하다. 종속성 검자(Dependency checking) 기능은 자동엮기(autowiring) 기능과 마찬가지로 각각의 bean마다 설정할 수 있다. 종속성 검사에는 4가지 모드가 있으며, XML 기반 설정에서는 &lt;bean/&gt; element의 'dependency-check' attribute를 사용하여 설정할 수 있다.

| Mode | 설명 |
| --- | --- |
| none | 종속성 검사를 하지 않는다. 기본(default) 모드이다. |
| simple | Primitive 타입과 collection에 대해서 종속성 검사를 수행한다. |
| object | 관련된 객체에 대해서만 종속성 검사를 수행한다. |
| all | Primitive 타입과 collection, 관련된 객체에 대해서 종속성 검사를 수행한다. |

### 메소드 삽입(Method Injection)

 대부분의 어플리케이션에서, Container에 존재하는 대부분의 bean은 singleton이다. Singleton bean이 다른 singleton bean과 협력(collaborate)하거나, non-singleton bean이 다른 non-singleton bean과 협력하는 경우, 가장 일반적인 방법은 bean의 property를 정의함으로써 종속성을 조절하는 것이다. 하지만 만약 관련된 bean들의 생명주기가 다른 경우 문제가 발생한다. Singleton bean A가 non-singleton bean B를 사용한다고 할 때, Container는 singleton bean A를 단지 한번만 생성할 것이고, 따라서 property도 역시 한번만 설정될 것이다. Container는 bean B가 필요한 매 순간 새로운 객체를 생성하여 bean A에게 제공해야 하지만, 그럴 수 있는 방법이 없다.

 위 문제에 대한 한가지 해법은 몇몇 제어의 역전(inversion of control)를 버리는 것이다. Bean A는 BeanFactoryAware interface를 구현함으로써 자신이 속한 Container를 알 수 있다. 그리고 bean B의 객체가 필요한 순간에 Container의 getBean(“B”)을 호출함으로써 bean B의 객체를 가져올 수 있다.

 ```java
 // a class that uses a stateful Command-style class to perform some processing
package fiona.apple;
 
// lots of Spring-API imports
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanFactoryAware;
 
public class CommandManager implements BeanFactoryAware {
    private BeanFactory beanFactory;
 
    public Object process(Map commandState) {
        // grab a new instance of the appropriate Command
        Command command = createCommand();
        // set the state on the (hopefully brand new) Command instance
        command.setState(commandState);
        return command.execute();
    }
 
    // the Command returned here could be an implementation that executes asynchronously, or whatever
    protected Command createCommand() {
        return (Command) this.beanFactory.getBean("command"); // notice the Spring API dependency
    }
 
    public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
        this.beanFactory = beanFactory;
    }
}
```

 위 예제는 일반적으로는 바람직하지 않은 솔루션이다. 왜냐하면 업무 코드(business code)는 Spring Framework과 관련될 필요가 없기 때문이다. 메소드 삽입(Method Injection)은 이런 경우를 말끔히 해결할 수 있는 방법이다.

#### Lookup 메소드 삽입(Lookup method injection)

 Lookup 메소드 삽입은 Container가 관리하고 있는 bean의 메소드를 덮어써서(override) Container 안에 있는 다른 bean을 찾을 수 있게 하는 기능이다. Spring Framework는 메소드 삽입을 구현하기 위해서 CGLIB 라이브러리를 사용하여 동적으로 상속클래스를 생성한다.

 ```java
 package fiona.apple;
 
// no more Spring imports! 
public abstract class CommandManager {
    public Object process(Object commandState) {
        // grab a new instance of the appropriate Command interface
        Command command = createCommand();
        // set the state on the (hopefully brand new) Command instance
        command.setState(commandState);
        return command.execute();
    }
 
    // okay... but where is the implementation of this method?
    protected abstract Command createCommand();
}
```

 삽입될 메소드는 반드시 다음과 같은 형태를 가져야 한다.

 ```xml
<public|protected> [abstract] <return-type> theMethodName(no-arguments);
```

 만약 메소드가 abstract이면, 동적으로 생성된 서브클래스는 메소드를 구현할 것이다. 만약 그렇지 않으면 동적으로 생성된 서브클래스를 원본 클래스의 메소드를 덮어쓸(override) 것이다.

 ```xml
<!-- a stateful bean deployed as a prototype (non-singleton) -->
<bean id="command" class="fiona.apple.AsyncCommand" scope="prototype">
    <!-- inject dependencies here as required -->
</bean>
 
<!-- commandProcessor uses statefulCommandHelper -->
<bean id="commandManager" class="fiona.apple.CommandManager">
    <lookup-method name="createCommand" bean="command"/>
</bean>
```

 ***commandManager***는 ***command*** bean의 새로운 객체가 필요할 때마다 자신의 createCommand() 메소드를 호출할 것이다. 만약 command bean이 prototype이 아닌 singleton인 경우, createCommand 메소드는 같은 객체를 리턴할 것이다.

 동적 서브클래스 생성이 동작하려면 classpath에 CGLIB가 추가되어 있어야 한다. 그리고 원본 class는 final이면 안되며, 덮어쓸(override) 메소드 역시 final이면 안된다.

## 참고자료

*   [Spring Framework - Reference Document / 1.4 Dependencies](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#beans-dependencies)
