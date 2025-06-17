---
title: Test Automation
linkTitle: Test Automation
description: "개발자가 작성한 다수의 단위테스트 클래스를 자동으로 테스트하고 그 결과 리포트를 생성하는 기능에 대해 설명한다."
url: /egovframe-development/test-tool/test-automation/
menu:
  depth:
    weight: 2
    parent: "test-tool"
    identifier: "test-automation"
---

# Test Automation

## 개요

[Test Automation](http://en.wikipedia.org/wiki/Test_automation)은 개발자가 작성한 다수의 단위테스트 클래스를 자동으로 테스트하고 그 결과 리포트를 생성하는 기능을 제공하는 것을 말한다. Test Automation의 개념과 방법에 대해 알아본다.

## 설명

**Test Automation**은 **지속적인 통합**([Continuous Integration - CI](http://www.martinfowler.com/articles/continuousIntegration.html))를 실천하기 위한 방안 중 하나인 "[Make Your Build Self-Testing](http://www.martinfowler.com/articles/continuousIntegration.html#MakeYourBuildSelf-testing)" 개념에서 나온 것으로 개발자 코드에 대해 작성된 단위테스트 클래스들을 자동으로 테스트를 수행하도록 하고, 매일 지속적으로 테스트를 수행하고 그 결과를 확인함으로써 지속적인 통합의 이점을 극대화시키고자 하는 목적을 갖고 있다.

[Code-driven testing](http://en.wikipedia.org/wiki/Test_automation#Code-driven_testing)에서도 설명하고 있듯이, 개발자가 대상 코드에 대한 여러 개의 단위테스트 클래스를 작성하고 나면, 이를 몇 개 그룹으로 묶거나, 빌드도구를 활용하여 TestCase를 한꺼번에 수행하여 그 결과 리포트를 생성할 수 있다.  
그리고, CI서버와 연계하여 주기적으로 빌드를 수행하는 프로세스 중 하나로 포함시킴으로써 **지속적인 테스트**의 기초가 될 수 있다.

좀 더 관심이 있으신 분은 IBM 사이트에 연재되었던 Article ["사람을 위한 자동화:연속 테스팅"](http://www.ibm.com/developerworks/kr/library/j-ap03137/)을 참고하기 바란다.

### Test Automation 오픈소스

Test Automation 수행을 위한 오픈소스로는 Ant와 Maven이 있으며, TestCase 작성을 위한 프레임워크인 JUnit에서 테스트 자동 수행과 리포팅을 위한 기능을 제공한다.

| 기능 | Maven Plug-in | Ant Task |
|------|---------------|----------|
| 빌드도구 | [Maven](http://maven.apache.org/) 2.0 | [Ant](http://ant.apache.org/) 1.6.5 이상 |
| 테스트 자동 수행 | [Maven Surefire Plugin](http://maven.apache.org/plugins/maven-surefire-plugin/) | [Ant JUnit Task](http://ant.apache.org/manual/OptionalTasks/junit.html) |
| 테스트 리포트 생성 | [Maven Surefire Report Plugin](http://maven.apache.org/plugins/maven-surefire-report-plugin/) | [Ant JUnit Report Task](http://ant.apache.org/manual/OptionalTasks/junitreport.html) |

본 개발환경에서는 좀더 많이 사용되는 Ant를 선정했었으나, 배포도구에서 Maven을 선정하였으므로 Ant와 Maven을 이용한 모든 사용법을 함께 설명한다. 그러나, 기본적으로 사용법만 다를 뿐이다.

### Test Automation 프로세스

* [Write TestSuite](./write-testsuite.md) : 작성된 다수의 TestCase 클래스들을 수행을 위해 몇 개 그룹 혹은 하나로 묶는다.
* [Run TestSuite](./run-testsuite.md) : TestCase 그룹들의 테스트를 한꺼번에 수행한다.
* [Test Reporting](./test-reporting.md) : 테스트 수행 결과를 Text, XML, HTML, Excel 형태의 리포트로 생성한다.

## 환경설정

* Ant, Maven Eclipse Plugin 설치
* JUnit Eclipse Plugin 설치1)
* TestSuite 작성을 위한 라이브러리 추가 (pom.xml) : [Unit Test 작성을 위한 pom.xml dependency 설정](./pom-dependency-for-write-unittest.md) 참고
* 엑셀 리포팅을 사용할 경우 [setting.xml에 설정](./setting-for-excel-reporting.md) 추가

## 사용법

Test Automation을 수행하기 위해서는 다음과 같이 진행한다.

* [Write TestSuite](./write-testsuite.md) : TestSuite 클래스를 작성하거나, 빌드도구에서 테스트 수행을 하기 위한 TestCase들을 명시한다.
* [Run TestSuite](./run-testsuite.md) : 빌드도구의 이클립스 플러그인을 이용하여 테스트를 수행한다.
* [Test Reporting](./test-reporting.md) : 테스트 수행 결과 생성된 Text, XML, HTML, Excel 형태의 리포트를 확인한다.

## 샘플

### Test Automation - Maven

다음과 같이 설정할 수 있다.

```XML
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 
	<modelVersion>4.0.0</modelVersion>
	<groupId>egovframework.guideprogram</groupId>
	<artifactId>egovframework.guideprogram.testcase</artifactId>
	<packaging>war</packaging>
	<name>egovframework.guideprogram.testcase</name>
	<version>2.0.0</version>
 
	<properties>
		<spring.maven.artifact.version>3.0.5.RELEASE</spring.maven.artifact.version>
		<compileSource>1.5</compileSource>
		<encoding>UTF-8</encoding>
	</properties>
 
	<dependencies>
            . . . 중략 . . .
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.4</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.easymock</groupId>
			<artifactId>easymock</artifactId>
			<version>3.0</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.easymock</groupId>
			<artifactId>easymockclassextension</artifactId>
			<version>2.4</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.dbunit</groupId>
			<artifactId>dbunit</artifactId>
			<version>2.4.8</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.unitils</groupId>
			<artifactId>unitils</artifactId>
			<version>2.2</version>
			<scope>test</scope>
		</dependency>
            . . . 중략 . . .
	</dependencies>
 
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
					<excludes>
						<exclude>**/Abstract*.java</exclude>
					</excludes>
					<includes>
						<include>**/*Test.java</include>
					</includes>
				</configuration>
			</plugin>
			<!-- Egovframework JUnit Excel Reporting -->
			<plugin>
				<groupId>egovframework.dev</groupId>
				<artifactId>egovtest-maven-plugin</artifactId>
				<version>1.0.0-SNAPSHOT</version>
			</plugin>
		</plugins>
	</build>
	<reporting>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-report-plugin</artifactId>
				<version>2.4.2</version>
			</plugin>
		</plugins>
	</reporting>
 
</project>
```

### Test Automation - Ant

다음과 같이 설정할 수 있다.

```XML
<?xml version="1.0" encoding="UTF-8"?>
 
<project name="egovframework-dev-tst-ant" basedir="." . . .>
 
    <property name="src.dir" value="src/main/java" />
    <property name="resource.dir" value="src/main/resources" />
    <property name="build.dir" value="build/classes" />
 
    <property name="testsrc.dir" value="src/test/java" />
    <property name="testresource.dir" value="src/test/resources" />
    <property name="testbuild.dir" value="build/testclasses" />
 
    <property name="testreports.dir" value="build/junit-reports" />
 
    <property name="lib.dir" value="lib" />
    <property name="buildlib.dir" value="build/lib" />
 
    <path id="master-classpath">
        <path location="${lib.dir}/ant-1.6.5.jar" />
         . . . 중략 . . .
    </path>
 
    <path id="test-classpath">
        <path location="${lib.dir}/ant-testutil-1.7.1.jar" />
         . . . 중략 . . .
    </path>
 
    <target name="clean">
        <delete failonerror="false" includeEmptyDirs="true">
            <fileset dir="${build.dir}" />
            <fileset dir="${testbuild.dir}" />
            <fileset dir="${testreports.dir}" />
        </delete>
    </target>
 
    <target name="build">
        <mkdir dir="${build.dir}" />
 
        <javac destdir="${build.dir}"
               source="1.5"
               target="1.5"
               debug="true"
               encoding="UTF-8"
               deprecation="false"
               optimize="false"
               failonerror="true">
            <src path="${src.dir}" />
            <classpath refid="master-classpath" />
        </javac>
 
        <jar jarfile="build/${ant.project.name}.jar" compress="true">
            <fileset dir="${build.dir}">
                <include name="**/*" />
            </fileset>
        </jar>
 
        <copy todir="${build.dir}" preservelastmodified="true">
            <fileset dir="${resource.dir}" includes="**/*" />
        </copy>
    </target>
 
    <target name="tests" depends="build" description="Run tests">
 
        <delete dir="${testbuild.dir}" />
        <mkdir dir="${testbuild.dir}" />
        <delete dir="${testreports.dir}" />
        <mkdir dir="${testreports.dir}" />
 
        <javac srcdir="${testsrc.dir}"
               destdir="${testbuild.dir}"
               debug="true"
               encoding="UTF-8"
               deprecation="true">
            <classpath path="${build.dir}" />
            <classpath refid="master-classpath" />
            <classpath refid="test-classpath" />
        </javac>
 
        <copy todir="${testbuild.dir}" preservelastmodified="true">
            <fileset dir="${build.dir}" includes="**/*" />
            <fileset dir="${testresource.dir}" includes="**/*" />
        </copy>
 
        <junit forkmode="perBatch"
               printsummary="true"
               haltonfailure="yes"
               haltonerror="yes">
            <classpath refid="master-classpath" />
            <classpath refid="test-classpath" />
            <classpath path="${testbuild.dir}" />
            <sysproperty key="ant.home" value="${ant.home}" />
 
            <formatter type="xml" />
 
            <batchtest fork="yes" todir="${testreports.dir}">
                <fileset dir="${testbuild.dir}">
                    <include name="**/*Test.class" />
                    <exclude name="**/Abstract*Test.class" />
                </fileset>
            </batchtest>
        </junit>
 
    </target>
 
    <!-- Junit Test Result Report  -->
    <target name="junitreport" depends="tests">
        <junitreport todir="${testhtml.dir}">
            <fileset dir="${testreports.dir}">
                <include name="TEST-*.xml" />
            </fileset>
            <report format="frames" todir="${testhtml.dir}" />
        </junitreport>
    </target>
 
    <path id="egov.lib">
        <path refid="master-classpath" />
        <path location="${antlib.dir}/egovtest/egovframework-dev-tst-ant.jar" />
    </path>
 
    <taskdef resource="egovtest.properties"
             classpathref="egov.lib"
             description="egovtest junit tasks:" />
 
    <!-- JUnit Excel Report -->
    <target name="egovtest" depends="tests">
        <egov-junitreport todir="${testxls.dir}">
            <fileset dir="${testreports.dir}" includes="**/TEST-*.xml" />
        </egov-junitreport>
    </target>
 
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
 
</project>
```

## 참고자료

* JUnit Home : <http://junit.org/>
* Maven Surefire Plugin Home : <http://maven.apache.org/plugins/maven-surefire-plugin/>
* Maven Surefire Report Plugin Home : <http://maven.apache.org/plugins/maven-surefire-report-plugin/>
* Maven Emma Plugin Home : <http://emma.sourceforge.net/maven-emma-plugin/>
* Ant JUnit Task : <http://ant.apache.org/manual/OptionalTasks/junit.html>
* Ant JUnit Report Task : <http://ant.apache.org/manual/OptionalTasks/junitreport.html>
* EMMA Home : <http://emma.sourceforge.net>
* EclEmma Home : <http://www.eclemma.org>
* m2eclipse Home : <http://m2eclipse.sonatype.org/index.html>
* '행위의 중복'을 없애는, 사람을 위한 자동화 시리즈 <http://www.ibm.com/developerworks/kr/series/j-ap.html>