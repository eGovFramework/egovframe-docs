---
linkTitle: "AOP XML"
title: XML 스키마 기반 AOP 지원
url: "/egovframe-runtime/foundation-layer-core/aop/aop-xmlschema/"
menu:
    depth:
        weight: 2
        parent: "AOP"
        name: "AOP XML"
description: "Java 5 버전을 사용할 수 없거나 XML 기반 설정을 선호하는 경우, Spring 2.0 이상에서는 XML 스키마 기반 AOP를 사용할 수 있으며, `aop` 네임스페이스를 제공한다. 이 방식에서도 @AspectJ AOP에서 사용된 포인트컷 표현식과 충고(Advice) 유형을 동일하게 사용할 수 있다."
---
# XML 스키마 기반 AOP 지원

## 개요

 Java 5 버전을 사용할 수 없거나, XML 기반 설정을 선호한다면, Spring 2.0 이상에서 제공하는 XML 스키마 기반의 AOP를 사용할 수 있다. Spring은 관점(Aspect) 정의를 지원하기 위해 “aop” 네임스페이스를 제공한다. @AspectJ를 이용한 AOP 지원에서 사용된 포인트컷 표현식과 충고(Advice) 유형은 XML 스키마 기반 AOP 지원에도 동일하게 제공된다.

## 설명

### 관점(Aspect) 정의하기

 Spring 어플리케이션 컨텍스트에서 빈으로 정의된 일반 Java 개체는 관점(Aspect)으로 정의될 수 있다. 관점(Aspect)은 &lt;aop:aspect&gt; 요소를 사용하여 정의한다.

 ```xml
<bean id="adviceUsingXML" class="org.egovframe.rte.fdl.aop.sample.AdviceUsingXML" />
<aop:config>
    <aop:aspect ref="adviceUsingXML">
    ...
    </aop:aspect>
</aop:config>
```

 관점(Aspect)로 정의된 aBean은 Spring 빈처럼 설정되고 의존성 주입이 될 수 있다.

### 포인트컷(Pointcut) 정의하기

 포인트컷은 결합점(Join points)을 지정하여 충고(Advice)가 언제 실행될지를 지정하는데 사용된다. Spring AOP는 Spring 빈에 대한 메소드 실행 결합점만을 지원하므로, Spring에서 포인트컷은 빈의 메소드 실행점을 지정하는 것으로 생각할 수 있다. 다음 예제는 egovframework.rte.fdl.aop.sample 패키지 하위의 Sample 명으로 끝나는 클래스의 모든 메소드 수행과 일치할 'targetMethod' 라는 이름의 pointcut을 정의한다. 포인트컷은 &lt;aop:config&gt; 요소 내에 정의한다. 포인트컷 표현식은 AspectJ 포인트컷 표현 언어와 동일하게 사용할 수 있다.

 ```xml
<aop:config>
    <aop:pointcut id="targetMethod" expression="execution(* org.egovframe.rte.fdl.aop.sample.*Sample.*(..))" />
</aop:config>
```

### 충고(Advice) 정의하기

 충고(Advice)는 관점(Aspect)의 실제 구현체로 포인트컷 표현식과 일치하는 결합점에 삽입되어 동작할 수 있는 코드이다. 충고는 결합점과 결합하여 동작하는 시점에 따라 before advice, after advice, around advice 타입으로 구분된다. @AspectJ를 이용한 AOP와 동일하게 5종류의 충고(Advice)를 지원한다.

#### Before advice

 Before advice는 &lt;aop:aspect&gt; 요소 내에서 &lt;aop:before&gt; 요소를 사용하여 정의한다. 다음은 before 충고를 정의하는 XML의 예제이다. before 충고인 beforeTargetMethod() 메소드는 targetMethod()로 정의된 포인트컷 전에 수행된다.

 ```xml
<aop:aspect ref="adviceUsingXML">
    <aop:before pointcut-ref="targetMethod" method="beforeTargetMethod" />
</aop:aspect>
```

 다음은 before 충고를 구현하고 있는 클래스이다. before 충고를 수행하는 beforeTargetXML()메소드는 해당 포인트컷을 가진 클래스명과 메소드 명을 출력한다.

 ```java
 public class AdviceUsingXML {
    ...
    public void beforeTargetMethod(JoinPoint thisJoinPoint) {
        System.out.println("AdviceUsingXML.beforeTargetMethod executed.");
 
        Class clazz = thisJoinPoint.getTarget().getClass();
        String className = thisJoinPoint.getTarget().getClass().getSimpleName();
        String methodName = thisJoinPoint.getSignature().getName();
 
        System.out.println(className + "." + methodName + " executed.");
    }
    ...
}
```

#### After returning advice

 After returning 충고는 정상적으로 메소드가 실행될 때 수행된다. After 충고는 &lt;aop:aspect&gt; 요소 내에서 &lt;aop:after-returning&gt; 요소를 사용하여 정의한다. 다음은 After returning 충고를 사용하는 예제이다. afterReturningTargetMethod() 충고는 targetMethod()로 정의된 포인트컷 후에 수행된다. targetMethod() 포인트컷의 실행 결과는 retVal 변수에 저장되어 전달된다.

 ```xml
<aop:aspect ref="adviceUsingXML">
    <aop:after-returning pointcut-ref="targetMethod" method="afterReturningTargetMethod" returning="retVal" />
</aop:aspect>
```

 다음은 After returning 충고를 구현하고 있는 클래스이다. After returning 충고를 수행하는 afterReturningTargetMethod()메소드는 해당 포인트컷의 반환값을 출력한다.

 ```java
 public class AdviceUsingXML {
    ...
    public void afterReturningTargetMethod(JoinPoint thisJoinPoint, Object retVal) {
        System.out.println("AdviceUsingXML.afterReturningTargetMethod executed." + return value is [" + retVal + "]");
    }
    ...
}
```

#### After throwing advice

 After throwing 충고는 메소드가 수행 중 예외사항을 반환하고 종료하는 경우 수행된다. After 충고는 &lt;aop:aspect&gt; 요소 내에서 &lt;aop:after-returning&gt; 요소를 사용하여 정의한다. 다음은 After throwing 충고를 사용하는 예제이다. afterThrowingTargetMethod() 충고는 targetMethod()로 정의된 포인트컷에서 예외가 발생한 후에 수행된다. targetMethod() 포인트컷에서 발생된 예외는 exception 변수에 저장되어 전달된다.

 ```xml
<aop:aspect ref="adviceUsingXML">
    <aop:after-throwing pointcut-ref="targetMethod" method="afterThrowingTargetMethod" throwing="exception" />
</aop:aspect>
```

 다음은 After throwing 충고를 구현하고 있는 클래스이다. After throwing 충고를 수행하는 afterReturningTargetMethod()메소드는 전달 받은 예외를 한번 더 감싸서 사용자가 쉽게 알아 볼 수 있도록 메시지를 설정하여 반환한다.

 ```java
 public class AdviceUsingXML {
    ...
    public void afterThrowingTargetMethod(JoinPoint thisJoinPoint, Exception exception) throws Exception {
        System.out.println("AdviceUsingXML.afterThrowingTargetMethod executed.");
        System.err.println("에러가 발생했습니다.", exception);
        throw new BizException("에러가 발생했습니다.", exception);
    }
    ...
}
```

#### After (finally) advice

 After (finally) 충고는 메소드 수행 후 무조건 수행된다. After 충고는 &lt;aop:aspect&gt; 요소 내에서 &lt;aop:after&gt; 요소를 사용하여 정의한다. After 충고는 다음은 After (finally) 충고를 사용하는 예제이다. afterTargetMethod() 충고는 targetMethod()로 정의된 포인트컷의 정상 종료 및 예외 발생의 경우 모두에 대해 수행된다. 보통은 리소스 해제와 같은 작업을 수행한다.

 ```xml
<aop:aspect ref="adviceUsingXML">
    <aop:after pointcut-ref="targetMethod" method="afterTargetMethod" />
</aop:aspect>
```

 다음은 After (finally) 충고를 구현하고 있는 클래스이다. After (finally) 충고를 수행하는 afterTargetMethod()메소드는 after 충고가 수행됨을 표시하는 메시지를 출력한다.

 ```java
 public class AdviceUsingXML {
    ...
    public void afterTargetMethod(JoinPoint thisJoinPoint) {
        System.out.println("AdviceUsingXML.afterTargetMethod executed.");
    }
    ...
}
```

#### Around advice

 Around 충고는 메소드 수행 전후에 수행된다. After 충고는 &lt;aop:aspect&gt; 요소 내에서 &lt;aop:around&gt; 요소를 사용하여 정의한다. Around 충고는 정상 종료와 예외 발생 경우를 모두 처리해야 하는 경우에 사용된다. 리소스 해제와 같은 작업이 해당된다.

 ```xml
<aop:aspect ref="adviceUsingXML">
    <aop:around pointcut-ref="targetMethod" method="aroundTargetMethod" />
</aop:aspect>
```

 다음은 Around 충고를 구현하고 있는 클래스이다. aroundTargetMethod() 충고는 파라미터로 ProceedingJoinPoint을 전달하며 proceed() 메소드 호출을 통해 대상 포인트컷을 실행한다. 포인트컷 수행 결과값인 retVal을 Around 충고 내에서 변환하여 반환할 수 있음을 보여준다.

 ```java
 public class AdviceUsingXML {
    ...
    public Object aroundTargetMethod(ProceedingJoinPoint thisJoinPoint) throws Throwable {
        System.out.println("AdviceUsingXML.aroundTargetMethod start.");
        long time1 = System.currentTimeMillis();
        Object retVal = thisJoinPoint.proceed();
 
        System.out.println("ProceedingJoinPoint executed. return value is [" + retVal + "]");
 
        retVal = retVal + "(modified)";
        System.out.println("return value modified to [" + retVal + "]");
 
        long time2 = System.currentTimeMillis();
        System.out.println("AdviceUsingXML.aroundTargetMethod end. Time(" + (time2 - time1) + ")");
        return retVal;
    }
    ...
}
```

### 관점(Aspect) 실행하기

 앞서 정의한 관점(Aspect)가 정상적으로 동작하는지 확인하기 위해 테스트 코드를 이용해 확인해 본다. AdviceTest 클래스는 대상 메소드 수행 시 예외 없이 정상 실행하는 경우와 예외 발생의 경우를 구분해서 테스트한다.

#### 정상 실행의 경우

 testAdvice() 함수는 대상 메소드가 정상 수행되는 사례를 보여준다. egovframework.rte.fdl.aop.sample 패키지에 속하는 AdviceSample 클래스의 someMethod() 메소드는 before, after returning, after finally, around 충고(Advice)가 적용된다.

 ```java
 public class AdviceTest{
    @Resource(name = "adviceSample")
    AdviceSample adviceSample;
 
    @Test
    public void testAdvice() throws Exception {
        SampleVO vo = new SampleVO();
        ..
        String resultStr = adviceSample.someMethod(vo);
 
        assertEquals("someMethod executed.(modified)", resultStr);
    }
}
```

 테스트 코드를 수행한 결과 로그는 다음과 같다.

 ```bash
AdviceUsingXML.beforeTargetMethod executed.
AdviceSample.someMethod executed.
AdviceUsingXML.aroundTargetMethod start.
AdviceUsingXML.afterReturningTargetMethod executed. return value is [someMethod executed.]
AdviceUsingXML.afterTargetMethod executed.
ProceedingJoinPoint executed. return value is [someMethod executed.]
return value modified to [someMethod executed.(modified)]
AdviceUsingXML.aroundTargetMethod end. Time(12)

```

 콘솔 로그 출력을 보면 충고(Advice)가 적용되는 순서는 다음과 같다.

- @Before
- @Around (대상 메소드 수행 전)
- 대상 메소드
- @AfterReturning
- @After(finally)
- @Around (대상 메소드 수행 후)

 주의할 점은 @Around 충고는 대상 메소드의 반환 값(return value)를 변경 가능하지만, After returning 충고는 반환 값을 참조 가능하지만 변경할 수 없다.

#### 예외 발생의 경우

 testAnnotationAspectWithException() 함수는 대상 메소드에 오류가 발생한 사례를 보여준다. egovframework.rte.fdl.aop.sample 패키지에 속하는 AnnotationAdviceSample 클래스의 someMethod() 메소드는 before, after throwing, after finally, around 충고(Advice)가 적용된다.

 ```java
 public class AdviceTest{
    @Resource(name = "adviceSample")
    AdviceSample adviceSample;
 
    @Test
    public void testAdviceWithException() throws Exception {
        SampleVO vo = new SampleVO();
        // exception 을 발생시키도록 플래그 설정
        vo.setForceException(true);
        ...
        try {
            // vo 의 forceException 플래그가 true 이면 - / by zero 상황을 강제로 처리함
            resultStr = adviceSample.someMethod(vo);
            fail("exception 을 강제로 발생시켜 이 라인이 수행될 수 없습니다.");
        } catch (Exception e) {
            ...
        }
    }
}
```

 테스트 코드를 수행한 결과 로그는 다음과 같다.

 ```bash
AdviceUsingXML.beforeTargetMethod executed.
AdviceSample.someMethod executed.
AdviceUsingXML.aroundTargetMethod start.
AdviceUsingXML.afterThrowingTargetMethod executed.
에러가 발생했습니다.
java.lang.ArithmeticException: / by zero
...

```

 콘솔 로그 출력을 보면 충고(Advice)가 적용되는 순서는 다음과 같다.

- @Before
- @Around (대상 메소드 수행 전)
- 대상 메소드 (ArithmeticException 예외가 발생한다)
- @AfterThrowing
- @After(finally)

 예외가 발생하더라도 after 로 정의한 충고(Advice)는 수행되는 것을 확인할 수 있다. After Throwing 충고(Advice)는 에러 메시지를 재설정하고 새로운 예외를 생성하여 전달할 수 있다.

## 참고자료

- [Spring Framework - Reference Document / 5.5 Schema-based AOP support](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html/core.html#aop-schema)