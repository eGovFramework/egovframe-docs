---
title: Test Reporting
linkTitle: Test Reporting
description: "테스트 수행 결과를 Text, XML, HTML, Excel 형태의 리포트를 생성한다."
url: /egovframe-development/test-tool/test-automation/test-reporting/
menu:
  depth:
    weight: 3
    parent: "test-automation"
    identifier: "test-reporting"
---
# Test Reporting

## 개요

Test Automation 수행 후에는 테스트 결과를 갖는 txt, XML 파일을 읽어 통계와 의미있는 테스트 결과를 보여주는 리포팅이 중요하다.  
여기에서는 테스트 결과 생성된 txt나 XML 파일을 읽고 HTML, Excel 형식의 리포트를 생성하는 방법에 대해 설명한다.

## 설명

테스트 수행한 결과를 의미있는 리포트를 만드는 데에도 Ant와 Maven 빌드도구를 사용한다.  
다만, 리포트를 생성하는 기능을 수행하는 Ant Task와 Maven Plug-in이 있어야 하는데, HTML 형식은 오픈소스에서 제공한다.  
각각 JUnit Report Task와 maven-surefire-report-plugin 이라는 라이브러리가 그것이다.  
그리고, Excel 형식의 리포트를 생성하는 기능은 전자정부 표준 프레임워크 개발환경에서 추가했는데, Ant Task와 Maven plugin으로 제공된다.

리포트를 생성하는 방법은 다음과 같다.

1. Script를 작성한다. (Ant - build.xml, Maven - pom.xml)
2. 이클립스 Plug-in으로 리포트 생성
3. 리포트 확인

리포트를 생성하는 방법도 기본적인 흐름은 테스트 수행과 동일하다. CI 서버에 등록할 경우의 goal 설정이나 target 설정만 리포트 생성을 위한 것으로 설정하면 된다.

생성된 리포트의 결과는 다음과 같은 모습이다.

* [Maven에서 생성한 테스트 결과 HTML 리포트](./maven-test-report.md)
* [Ant에서 생성한 테스트 결과 HTML 리포트](./ant-test-report.md)
* [테스트 결과 Excel 리포트](./excel-test-report.md)

## 환경설정

* Ant, Maven Eclipse Plugin 설치
* TestSuite 작성을 위한 라이브러리 추가 (pom.xml) : [TestReport 작성을 위한 pom.xml dependency](./pom-dependency-for-write-unittest.md) 설정 참고
* 엑셀 리포팅을 사용할 경우 [setting.xml에 설정](./setting-for-excel-reporting.md) 추가

## 사용법

테스트 결과 리포트는 텍스트(.txt), HTML(.html), XML(.xml), 엑셀(.xls) 형식으로 생성할 수 있다.  
텍스트와 XML 형식 리포트는 리포트라기보다 테스트 결과 데이터를 갖고 있는 파일이므로 주로 테스트 수행시에 생성하게 된다. 따라서, [테스트 수행](./run-testsuite.md)을 참조하도록 하고, 여기서는 HTML과 XML 형식의 리포트 생성 방법에 대해 설명한다.

### HTML 리포트 생성 방법

#### Maven에서 HTML 리포트 생성

1. pom.xml 작성 : [HTML 리포트 생성 샘플](#html-리포트-생성-샘플) 참조
2. 이클립스에서 리포트 생성 : [이클립스에서 Maven 실행하기](./run-maven-on-eclipse.md)를 참고하여 goal에 **surefire-report:report**를 입력하고, Console View에서 **BUILD SUCCESSFUL**을 확인한다.
3. HTML 리포트 확인 : 디폴트로 target/site/surefire-report.html이 생성되므로 더블클릭하여 리포트를 확인한다. 그 모양은 [Maven에서 생성한 테스트 결과 HTML 리포트](./maven-test-report.md)와 같다.

#### Ant에서 HTML 리포트 생성

1. build.xml 작성 : [HTML 리포트 생성 샘플](#html-리포트-생성-샘플) 참조
2. 이클립스에서 리포트 생성 : [이클립스에서 Ant 실행하기](./run-ant-on-eclipse.md)를 참고하여 해당 target을 실행하고, Console View에서 **BUILD SUCCESSFUL**을 확인한다.
3. HTML 리포트 확인 : build.xml의 todir="${testhtml.dir}"(<report format="frames" todir="${testhtml.dir}"/>)에서 설정하며, 현재 설정대로라면 testhtml.dir에 설정된 디렉토리에 index.html을 더블클릭하여 확인할 수 있다. 그 모양은 [Ant에서 생성한 테스트 결과 HTML 리포트](./ant-test-report.md)와 같다.

### 엑셀 리포트 생성 방법

테스트 결과를 엑셀 형식으로 리포트하는 기능은 오픈소스가 아닌 전자정부 개발프레임워크 개발환경에서 추가 개발한 내용이다.  
해당 기능에 대해 자세한 내용은 [테스트 결과 Excel 리포트](./excel-test-report.md)를 참조하도록 하고, 여기에서는 디폴트로 설정하고 엑셀 리포트를 생성하는 방법에 대해 설명하도록 한다.  
기본적으로 Ant나 Maven을 사용할 경우 스타일이 달라지지는 않으며, 별도로 [커스터마이즈된 템플릿 엑셀 파일](./excel-test-report.md#템플릿-파일-커스터마이즈하여-사용하는-방법)을 사용할 경우 그 스타일에 따른 엑셀 리포트를 만들게 된다.

#### Maven에서 엑셀 리포트 생성

1. setting.xml 설정 : goal을 간단하게 사용하기 위해 setting.xml에 [설정](./setting-for-excel-reporting.md)이 추가되어 있어야 한다.
2. pom.xml 작성 : [엑셀 리포트 생성 샘플](#엑셀-리포트-생성-샘플) 참조
3. 이클립스에서 리포트 생성 : [이클립스에서 Maven 실행하기](./run-maven-on-eclipse.md)를 참조하여, goal에 **egovtest:junit-xls**를 입력하고 Console View에서 **BUILD SUCCESSFUL**을 확인한다.
4. 엑셀 리포트 확인 : 디폴트로 target/egovtest/egovtest-junit.xls이 생성되므로 더블클릭하여 리포트를 확인한다. 그 모양은 [테스트 결과 Excel 리포트](./excel-test-report.md)와 같다. [template-junit.xls](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:dev2:tst:template-junit.xls)파일은 디폴트 템플릿 엑셀 파일이다.

#### Ant에서 엑셀 리포트 생성

1. build.xml 작성 : [엑셀 리포트 생성 샘플](#엑셀-리포트-생성-샘플) 참조
2. 이클립스에서 리포트 생성 : [이클립스에서 Ant 실행하기](./run-ant-on-eclipse.md)를 참고하여 해당 target을 실행하고, Console View에서 **BUILD SUCCESSFUL**을 확인한다.
3. 엑셀 리포트 확인 : build.xml의 **todir="${testxls.dir}"**(<egov-junitreport todir="${testxls.dir}">)에서 설정하며, 디폴트 예의 설정대로라면 testxls.dir에 설정된 디렉토리에 egovtest-junit.xls이 생성되므로 더블클릭하여 리포트를 확인한다. 그 모양은 [테스트 결과 Excel 리포트](./excel-test-report.md) 리포트와 같다. template-junit.xls 파일은 디폴트 템플릿 엑셀 파일이다.

## 샘플

### HTML 리포트 생성 샘플

* **Maven - pom.xml**  
```xml
<reporting>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-report-plugin</artifactId>
      <version>2.4.2</version>
    </plugin>
  </plugins>
</reporting>
```
* **Ant - build.xml**  
```xml
<!-- Junit Test Result Report  -->
<target name="junitreport" depends="tests">
    <junitreport todir="${testhtml.dir}">
        <fileset dir="${testreports.dir}">
            <include name="TEST-*.xml" />
        </fileset>
      <report format="frames" todir="${testhtml.dir}" />
    </junitreport>
</target>
```

### 엑셀 리포트 생성 샘플

* **Maven - pom.xml**  
   1. 디폴트 설정  
   ```xml
   <build>
     <defaultGoal>egovtest:junit-xls</defaultGoal>
     <plugins>
         <!-- Egovframework JUnit Excel Reporting -->
         <plugin>
             <groupId>egovframework.dev</groupId>
             <artifactId>egovtest-maven-plugin</artifactId>
         </plugin>
     </plugins>
   </build>
   ```
   2. 전체 설정 예  
   ```xml
   	<plugin>
                  <groupId>egovframework.dev</groupId>
   		<artifactId>egovtest-maven-plugin</artifactId>
   		<version>2.0.1</version>
   		<configuration>
   		<outputDirectory>${project.build.directory}/egovtest</outputDirectory>
   		<reportsDirectory>${project.build.directory}/site/egovtest</reportsDirectory>
   		<outputName>egovtest-report.xls</outputName>
   		<templatePath>${basedir}/src/test/resources/template-kr.xls</templatePath>
   		<headerPosition>
   			<!-- <summary>0,A,4</summary>
   			<package>0,A,8</package> -->
   			<summary>0,B,6</summary>
   			<package>0,B,11</package>
   			<lists>1,A,4</lists>
   			</headerPosition>
   		</configuration>
   		<dependencies>
   		<!-- Dependencies for developing functions of reporting -->
   		<dependency>
   			 <groupId>egovframework.dev</groupId>
   			 <artifactId>egovframework-dev-tst</artifactId>
   			 <version>2.0.1</version>
   		</dependency>
   		<dependency>
   			<groupId>org.apache.poi</groupId>
   			<artifactId>poi</artifactId>
   			<version>3.6</version>
   		</dependency>
   		<dependency>
   			<groupId>commons-io</groupId>
   			<artifactId>commons-io</artifactId>
   			<version>1.4</version>
   			</dependency>
   		</dependencies>
   		</plugin>
               </plugins>
   ```
        
     * **Ant - build.xml**  
       - 디폴트 설정  
   ```xml
   <path id="egov.lib">
       <path refid="master-classpath" />
       <path location="${antlib.dir}/egovtest/egovframework-dev-tst-ant.jar" />
   </path>
        
   <taskdef resource="egovtest.properties" classpathref="egov.lib" />
        
   <!-- JUnit Excel Report -->
   <target name="egovtest" depends="tests">
       <egov-junitreport todir="${testxls.dir}">
           <fileset dir="${testreports.dir}" includes="**/TEST-*.xml" />
       </egov-junitreport>
   </target>
   ```
   3. 전체 설정 예  
   ```xml
   <path id="egov.lib">
       <path refid="master-classpath" />
       <path location="${antlib.dir}/egovtest/egovframework-dev-tst-ant.jar" />
   </path>
        
   <taskdef resource="egovtest.properties" classpathref="egov.lib" />
        
   <!-- JUnit Excel Report -->
   <target name="egovtest-full" depends="tests">
       <egov-junitreport todir="${testxls.dir}"
                         outputname="egovtest-junit-full.xls"
                         templatepath="${basedir}/build/template-kr.xls"
                         summary="0,B,6"
                         packages="0,B,11"
                         lists="1,A,5">
           <fileset dir="${testreports.dir}"
                    includes="**/TEST-*.xml" />
       </egov-junitreport>
   </target>
   ```

## 참고자료

* Maven Surefire Plugin Home : <http://maven.apache.org/plugins/maven-surefire-plugin/>
* Maven Surefire Report Plugin Home : <http://maven.apache.org/plugins/maven-surefire-report-plugin/>
* Ant JUnit Task : <http://ant.apache.org/manual/OptionalTasks/junit.html>
* Ant JUnit Report Task : <http://ant.apache.org/manual/OptionalTasks/junitreport.html>
* m2eclipse Home : <http://m2eclipse.sonatype.org/index.html>
* [테스트 결과 Excel 리포트](./excel-test-report.md)
* [테스트 결과 Excel Report 상세](./excel-test-report-detail.md)
* template excel : [template-kr.xls (한글)](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:dev2:tst:template-kr.xls), [template-junit.xls (영문)](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:dev2:tst:template-junit.xls)