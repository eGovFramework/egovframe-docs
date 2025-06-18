---
title: "EMMA 실행을 위한 pom.xml 설정 샘플"
linkTitle: "EMMA 실행을 위한 pom.xml 설정 샘플"
description: "EMMA 실행을 위한 pom.xml 설정 샘플을 코드로 보여준다."
url: /egovframe-development/test-tool/test-tool-ref/pom-example-for-run-emma/
menu:
  depth:
    weight: 11
    parent: "test-tool-ref"
---
## EMMA 실행을 위한 pom.xml 설정 샘플

다음은 EMMA를 이용하여 Test Coverage를 수행하기 위한 pom.xml 설정 샘플이다.
EMMA를 수행하기 위해서는 Test 수행을 위한 설정(maven-surefire-plugin)을 반드시 같이 써야 한다.

```xml
<build>
    <plugins>
        <!-- test -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <configuration>
                <skipTests>false</skipTests>
                <forkMode>always</forkMode>
                <reportFormat>xml</reportFormat>
            </configuration>
        </plugin>
        <!-- EMMA   -->
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>emma-maven-plugin</artifactId>
            <version>1.0-alpha-1</version>
        </plugin>
    </plugins>
</build>
 
<reporting>
    <plugins>
        <!-- EMMA Coverage Reporting -->
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>emma-maven-plugin</artifactId>
            <inherited>true</inherited>
        </plugin>
    </plugins>
</reporting>
```
