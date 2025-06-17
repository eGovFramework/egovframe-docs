---
title: "EMMA 실행을 위한 build.xml 설정 샘플"
linkTitle: "EMMA 실행을 위한 build.xml 설정 샘플"
description: "EMMA 실행을 위한 build.xml 설정 샘플을 코드로 보여준다."
url: /egovframe-development/test-tool/ref/build-example-for-run-emma/
menu:
  depth:
    weight: 12
    parent: "ref"
---
## EMMA 실행을 위한 build.xml 설정 샘플

다음은 EMMA를 이용하여 Test Coverage를 수행하기 위한 build.xml 설정 샘플이다.
EMMA를 수행하기 위해서는 Test 수행을 위한 설정(junit)을 반드시 같이 써야 한다.

✔ 자세한 내용은 [EMMA 사이트](http://emma.sourceforge.net/userguide_single/userguide.html#introANT "http://emma.sourceforge.net/userguide_single/userguide.html#introANT")와 함께 [Using EMMA With ANT For JUnit Test Coverage Reporting](http://wiki.metawerx.net/wiki/UsingEMMAWithANTForJUnitTestCoverageReporting "http://wiki.metawerx.net/wiki/UsingEMMAWithANTForJUnitTestCoverageReporting")을 참조하기 바란다.

```xml
<property name="artifactsDir" value="${basedir}/build/report" />
 
<!-- 1. EMMA Task 라이브러리 설정 -->
<property name="emma.enabled" value="true" />
 
<path id="emma.lib" description="define the basic classpath for emma instrumentation">
    <fileset dir="${antlib.dir}/emma">
        <include name="*.jar" />
    </fileset>
</path>
 
<taskdef resource="emma_ant.properties"
         classpathref="emma.lib"
         description="this loads <emma> and <emmajava> custom tasks:" />
 
<!-- 2. EMMA Instrument -->
<target name="emma-jars" depends="build" description="Uses Emma to instrument the jar files">
    <emma enabled="${emma.enabled}">
        <instr mode="fullcopy"
               outdir="${basedir}/build/temp"
               merge="yes"
               filter="egovframework.dev.tst.*"
               metadatafile="${artifactsDir}/test-coverage/coverage.em">
            <instrpath>
                <fileset dir="build/" includes="${ant.project.name}.jar" />
            </instrpath>
        </instr>
    </emma>
</target>
 
<target name="test.with.emma" depends="emma-jars">
    <delete dir="${testbuild.dir}" />
    <mkdir dir="${testbuild.dir}" />
 
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
 
    <mkdir dir="${artifactsDir}/test-results/xml" />
    <junit fork="yes"
           printsummary="yes"
           haltonfailure="no"
           failureproperty="test.failed"
           errorproperty="test.failed"
           dir="${basedir}">
        <classpath>
            <path refid="master-classpath" />
            <path refid="test-classpath" />
            <path refid="emma.lib" />
            <fileset dir="${basedir}/build/temp/lib" includes="${ant.project.name}.jar" />
            <pathelement location="${testbuild.dir}" />
        </classpath>
 
        <formatter type="xml" />
        <batchtest fork="yes" todir="${artifactsDir}/test-results/xml">
            <fileset dir="${testbuild.dir}">
                <include name="**/*Test.class" />
            </fileset>
        </batchtest>
    </junit>
</target>
 
<!-- 3. EMMA Test Coverage Reporting -->
<!-- Test Code Coverage Report  -->
<target name="emmareport" depends="test.with.emma">
    <move file="${basedir}/coverage.ec"
          todir="${artifactsDir}/test-coverage" />
    <emma description="now we can generate the emma report"
          enabled="${emma.enabled}">
        <report sourcepath="${src.dir}"
                sort="+name,+method,+class"
                metrics="method:70,line:80,class:100"
                depth="method"
                columns="name,class,method,block,line"
                encoding="UTF-8">
            <infileset dir="${artifactsDir}/test-coverage"
                       includes="*.em, *.ec" />
            <!-- XML Report -->
            <xml outfile="${artifactsDir}/test-coverage/coverage.xml" />
            <!-- Text Report -->
            <txt outfile="${artifactsDir}/test-coverage/coverage.txt" />
            <!-- HTML Report -->
            <html outfile="${artifactsDir}/test-coverage/coverage.html" />
        </report>
    </emma>
</target>
```
