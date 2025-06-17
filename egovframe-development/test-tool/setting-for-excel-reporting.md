---
title: "엑셀 리포팅 사용을 위한 setting.xml 설정"
linkTitle: "엑셀 리포팅 사용을 위한 setting.xml 설정"
description: "엑셀 리포팅 사용을 위한 setting.xml 설정 방법에 대해 설명한다."
url: /egovframe-development/test-tool/ref/setting-for-excel-reporting
menu:
  depth:
    weight: 9
    parent: "ref"
---
## 엑셀 리포팅 사용을 위한 setting.xml 설정

오픈소스가 아닌 전자정부 개발프레임워크에서 개발한 테스트 엑셀 리포팅을 사용하기 위해서는 setting.xml에 다음과 같이 설정해야 한다.

```xml
<settings>
 . . . 중략 . . .
  <pluginGroups>
    <pluginGroup>egovframework.dev</pluginGroup>
  </pluginGroups>
</settings>
```

### Maven에서 기능 호출하는 방법

Maven에서 해당 기능을 사용하기 위해 호출하는 방법은 두 가지가 있다.

1. Full Name 방식 : goal에 **groupID:artifactID:version:goal** 식으로 지정하는 것이다.

```
 Maven clean 기능을 사용하고자 할 때, 다음과 같이 사용한다.
>mvn org.apache.maven.plugins:maven-clean-plugin:2.3:clean
```

2. 간단한 방식 : 몇 가지 조건을 만족하는 경우 **artifactID**의 **prefix:version:goal**와 같이 간단하게 기능을 호출할 수 있다.

```
 Maven clean 기능을 사용하고자 할 때, 다음과 같이 사용한다.
>mvn clean:clean
```

기본적으로 Maven에서 빌드 Lifecycle을 호출하여 기능을 수행하고자 할 때, Full Name으로 호출을 해야 한다. 그러나, 그것이 너무 번거로운 관계로 몇 가지 조건을 만족하는 경우 간단한 방식으로 호출할 수 있다. 그 조건은 다음과 같다.

1. groupID가 **org.apache.maven.plugins** 혹은 **org.codehaus.mojo**이다.
   Maven은 groupID가 생략될 경우, 두 groupID를 찾아본 다음 없을 경우 **setting.xml에 지정된 pluginGroup 항목**을 찾고 그래도 없으면 오류를 낸다.
2. artifactID 명을 **maven-${prefix}-plugin** 혹은 **${prefix}-maven-plugin**으로 지정하고, **${prefix}**를 사용한다.
   예를 들어, clean의 경우 maven-clean-plugin에서 clean이 prefix가 된다.
