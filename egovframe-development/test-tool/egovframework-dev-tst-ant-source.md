---
title: "egovframework-dev-tst-ant 프로젝트 소스 코드"
linkTitle: "egovframework-dev-tst-ant 프로젝트 소스 코드"
description: "egovframework-dev-tst-ant 프로젝트 소스 코드이다."
url: /egovframe-development/test-tool/ref/egovframework-dev-tst-ant-source/
menu:
  depth:
    weight: 1
    parent: "ref"
---
## egovframework-dev-tst-ant 프로젝트 소스 코드

egovframework-dev-tst-ant에는 Custom Ant Task 클래스를 포함한다.

### build.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
 
<project ... >
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
 
    <target name="build-report-junit-excel"
            depends="clean, egovtest"
            description="clean, egovtest" />
 
    <target name="build-report-junit-excel-full"
            depends="clean, egovtest-full"
            description="clean, egovtest-full" />
</project>
```

### EgovJUnitExcelReportTask

```java
public class EgovJUnitExcelReportTask extends Task {
    /** Excel 파일이 작성될 디렉토리 위치 */
    String todir;
 
    /** Excel 파일이 작성될 디렉토리 위치 */
    File outputDirectory;
 
    /** Excel 리포트 파일명 */
    String outputname;
 
    /** Excel 리포트의 템플릿 리포트 파일의 Full Path */
    String templatepath;
 
    /** Excel 리포트의 템플릿 리포트 파일의 Full Path */
    File templateFile;
 
    /** Template Excel 파일의 Summary Header 위치 정보 */
    String summary;
 
    /** Template Excel 파일의 Package Header 위치 정보 */
    String packages;
 
    /** Template Excel 파일의 TestCase Lists Header 위치 정보 */
    String lists;
 
    public void setTodir(String todir) {
        this.todir = todir;
    }
 
    public void setOutputname(String outputname) {
        this.outputname = outputname;
    }
 
    public void setTemplatepath(String templatepath) {
        if (templatepath != null && templatepath.length() > 0) {
            this.templatepath = templatepath;
        }
    }
 
    public void setSummary(String summary) {
        this.summary = summary;
    }
 
    public void setPackages(String packages) {
        this.packages = packages;
    }
 
   . . .
 
    List filesets = new ArrayList();
 
    public void addFileset(FileSet fileset) {
        filesets.add(fileset);
    }
```
