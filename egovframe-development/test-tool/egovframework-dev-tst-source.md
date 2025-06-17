---
title: "egovframework-dev-tst 프로젝트 소스 코드"
linkTitle: "egovframework-dev-tst 프로젝트 소스 코드"
description: "egovframework-dev-tst 프로젝트 소스 코드이다."
url: /egovframe-development/test-tool/ref/egovframework-dev-tst-source
menu:
  depth:
    weight: 2
    parent: "ref"
---
## egovframework-dev-tst 프로젝트 소스 코드

egovframework-dev-tst 프로젝트는 JUnit Test XML 파일을 파싱하고, 템플릿 엑셀 파일을 읽어 들여, 해당값을 매핑한 후 엑셀 형식 리포트로 생성하는 주요 작업을 구성하는 라이브러리이다. 여기에서는 소스 코드에 대한 설명을 하도록 하고, 자세한 내용은 API 문서나 소스를 직접 참조하기 바란다.

### JUnit Test XML 파일 예

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<testsuite errors="0" skipped="1" tests="6" time="3.359" failures="0" name="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest">
  <properties>
    <property value="Sun Microsystems Inc." name="java.vendor"/>
    <property value="C:\Documents and Settings\juroh\.m2\repository" name="localRepository"/>
   . . . . 중략 . . . .
  </properties>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="0.594" name="testNonXmlReportFileListException"/>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="0" name="testNotExistXmlReportFileListException"/>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="0" name="testNonOutputDirException"/>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="0" name="testNotExistOutputDirException"/>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="0.016" name="testGenerateExcelDefault">
    <skipped/>
  </testcase>
  <testcase classname="egovframework.dev.tst.report.junit.JUnitExcelReportGeneratorTest" time="2.609" name="testGenerateExcelFile"/>
</testsuite>
```

### Report VO 클래스

* `ReportTestCase`는 위 XML에서 `<testcase>` 태그 정보를 하나씩 담는다.
* `ReportTestSuite`는 위 XML에서 `<testsuite>` 태그의 요약 정보를 담는다.

### TestSuiteXmlParser

JUnit Test XML 파일을 파싱하는 `<strong>TestSuiteXmlParser</strong>` 클래스에 대해 알아보자.

`TestSuiteXmlParser` 클래스는 SAX 파서를 이용하여 XML을 파싱한다. 클래스의 구조는 다음과 같으며, `org.xml.sax.helpers.DefaultHandler` 클래스의 메소드 중 필요한 부분을 구현하면 된다.

#### Super Class

* `org.xml.sax.helpers.DefaultHandler`를 상속받는다.
  ```java
  public class TestSuiteXmlParser extends DefaultHandler {
   . . .
  }
  ```

#### Methods

* `<strong>Collection parse(String xmlPath)</strong>`
  대상 XML 파일 Full Path을 입력받아 XML 파싱을 하여 `ReportTestCase`와 `ReportTestSuite` 객체에 정보를 담는다. `JUnitReportParser`가 호출한다.

  ```java
      public Collection parse(String xmlPath) throws ParserConfigurationException, SAXException, IOException {
          SAXParserFactory factory = SAXParserFactory.newInstance();
   
          SAXParser saxParser = factory.newSAXParser();
   
          classesToSuites = new HashMap();
   
          saxParser.parse(new File(xmlPath), this);
   
          if (currentSuite != defaultSuite) {
              // defaultSuite
              if (defaultSuite.getNumberOfTests() == 0){
                  classesToSuites.remove(defaultSuite.getFullClassName());
              }
          }
          return classesToSuites.values();
      }
  ```

  ✔ **사용 예**는 TestCase(`TestSuiteXmlParserTest`)를 통해 확인할 수 있다.
* 기타

  * `void startElement(String uri, String localName, String qName, Attributes attributes)` : 시작 태그에 대한 처리 부분을 담고 있다.
  * `void endElement(String uri, String localName, String qName)` : 끝 태그에 대한 처리 부분을 담고 있다.
  * `void characters(char ch[], int start, int length)` : element 내의 문자 데이터 처리에 대한 로직
  * `private List parseCause(String detail)` : Fail 원인에 대한 처리를 위해 내부적으로 사용하는 메소드
  * `private List parseCause(String detail, String compareTo)` : Fail 원인에 대한 처리를 위해 내부적으로 사용하는 메소드

### JUnitReportParser

`JUnitReportParser`는 파싱한 XML 정보를 담고 있는 `ReportTestCase`와 `ReportTestSuite`을 이용하여 리포팅에 필요한 정보로 재조정한다.

#### Fields

JUnit Test XML 파일 Full Path 목록과, TestSuite List를 사용한다.

```xml
    /** JUnit Test XML 파일 Full Path 목록 */
    List<File> xmlReportFileList;
 
    /** TestSuite 목록 */
    List<ReportTestSuite> testSuites = new ArrayList<ReportTestSuite>();
```

#### Methods

* `<strong>List parseXMLReportFiles()</strong>` - JUnit Test XML 파일을 파싱하는 메인 함수

  ```java
  public List parseXMLReportFiles() throws EgovTestException {
      Collection suites = null;
   
      if (xmlReportFileList != null && xmlReportFileList.size() > 0) {
   
          TestSuiteXmlParser parser = new TestSuiteXmlParser();
          for (int idx = 0; idx < xmlReportFileList.size(); idx++) {
              File currentReport = (File) xmlReportFileList.get(idx);
   
              try {
                  suites = parser.parse(currentReport.getAbsolutePath());
              } catch (. . .) { . . .}
   
              testSuites.addAll(suites);
          }
      }
   
      return testSuites;
  }
  ```

  ✔ **사용 예**는 TestCase(`JUnitReportParserTest`)에서 확인할 수 있다.
* 기타

  * `Map getSummary(List suites)` : `ReportTestSuite`으로부터 전체 Summary 정보를 모은다.
  * `Map getSuitesGroupByPackage(List testSuitesList)` : `ReportTestSuite`으로부터 패키지별 요약 정보를 모은다.
  * `computeSuccessRate(int tests, int errors, int failures, int skipped)` : 성공률을 백분률로 계산한다.

### EgovJUnitExcelReportGenerator

#### Fields

* XML로부터 테스트 결과 정보를 갖기 위한 정보
  ```xml
      /** JUnit XML Parser */
      private JUnitReportParser parser;
   
      /** JUnit Test XML 파일 Full Path 목록 */
      List<File> xmlReportFileList;
   
      /** Test Suite Lists */
      private List<ReportTestSuite> testSuites;
  ```
* 엑셀 파일 생성을 위해 필요한 정보
  ```java
      /** Excel 리포트의 템플릿 리포트 파일의 Full Path */
      private File templatePath;
   
      /** Excel 파일이 작성될 디렉토리 위치 */
      private File outputDirectory;
   
      /** Excel 리포트 파일명 */
      private String outputName;
  ```
* POI의 엑셀 처리 관련 객체 - 엑셀 파일 정보
  ```
      /** ExtenXLS object representing MS Excel Document */
      private HSSFWorkbook book;
  ```
* 템플릿 엑셀 파일의 각 헤더 위치 정보
  ```java
      /** Summary 헤더 위치 정보 */
      private int[] summaryPosInfos = { 0, 0, 3 }; // sheet, col, row
   
      /** Package 헤더 위치 정보 */
      private int[] packagePosInfos = { 0, 0, 7 }; // sheet, col, row
   
      /** TestCase Lists 헤더 위치 정보 */
      private int[] listsPosInfos = { 1, 0, 3 }; // sheet, row, col
  ```
* 템플릿 엑셀 파일의 헤더 위치 정보를 담고 있는 Array의 인덱스 상수
  ```java
      /** Sheet 정보 IDX_SHEET */
      public final static int IDX_SHEET = 0;
   
      /** Column 정보 IDX_COL */
      public final static int IDX_COL = 1;
   
      /** Row 정보 IDX_ROW */
      public final static int IDX_ROW = 2;
  ```

#### Constructor

생성자에서 입력 받아야 하는 정보는 다음과 같다.

```java
    /**
     * 생성자
     * 
     * @param xmlReportFileList JUnit Test XML 파일의 Full Path List
     */
    public EgovJUnitExcelReportGenerator(List<File> xmlReportFileList)
    {
        this.xmlReportFileList = xmlReportFileList;
    }
 
    /**
     * 생성자
     * 
     * @param xmlReportFileList JUnit Test XML 파일의 Full Path List
     * @param templatePath 템플릿 엑셀 파일 객체
     * @param outputDirectory 파일 생성 위치 객체
     * @param outputName 생성될 엑셀 파일 명
     */
    public EgovJUnitExcelReportGenerator(List<File> xmlReportFileList,
            File templatePath, File outputDirectory, String outputName)
    {
        this.xmlReportFileList = xmlReportFileList;
        this.templatePath = templatePath;
        this.outputDirectory = outputDirectory;
        this.outputName = outputName;
    }
```

### EgovExcelUtil

#### 엑셀 파일 읽어서 Workbook 생성하기

템플릿 엑셀 파일을 읽어 Workbook을 생성하는 방법은 `EgovExcelUtil` 클래스의 `readExcelFile` 메소드에서 담당한다.

```java
    public static HSSFWorkbook readExcelFile(File xlsFullPath) throws EgovTestException {
        POIFSFileSystem fs = null; // POI FileSystem
        HSSFWorkbook wb = null; // HSSFWorkbook 엑셀 Workbook
 
        try {
            FileInputStream fis = new FileInputStream(xlsFullPath);
            fs = new POIFSFileSystem(fis);
            wb = new HSSFWorkbook(fs);
        } catch (...) { . . . }
        return wb;
    }
```

#### 엑셀파일 저장

엑셀 파일로 저장하는 기능은 `writeExcelReport` 메소드에서 담당한다.

```java
    public static void writeExcelReport(File fullPath, HSSFWorkbook wb) {
        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(fullPath);
            wb.write(fos);
            fos.close();
        } catch (...) { . . . }
    }
```

#### Cell에 값을 세팅

Cell은 엑셀 파일의 Sheet 내에서 column과 row 값을 갖는 단위를 말한다. Cell에 값을 세팅하는 기능은 `setCellValues`에서 담당한다.

```java
    public static void setCellValues(HSSFRow row, List values, int startColumn, HSSFRow startRow) {
        HSSFCellStyle style = null;
        HSSFCell cell = null;
        HSSFCell startCell = null;
 
        int currentColumn = startColumn;
 
        for (int index = 0; index < values.size(); index++) {
            cell = row.getCell(currentColumn);
 
            if (cell == null) {
                cell = row.createCell(currentColumn);
            }
 
            setCellValue(cell, values.get(index));
 
            // Style을 세팅한다.
            if (startRow != null) {
                startCell = startRow.getCell(currentColumn);
                if (startCell != null) {
                    style = startCell.getCellStyle();
                    cell.setCellStyle(style);
                }
            }
 
            currentColumn++;
        }
    }
 
    public static void setCellValues(HSSFRow row, int currentCol, Object value) {
        HSSFCell cell = null;
 
        if (value != null) {
            cell = row.getCell(currentCol);
 
            if (cell == null) {
                cell = row.createCell(currentCol);
            }
 
            setCellValue(cell, value);
        }
    }
 
    public static void setCellValue(HSSFCell cell, Object value) {
        if (value != null) {
            if (value instanceof String) {
                cell.setCellValue(new HSSFRichTextString((String) value));
 
            } else if (value instanceof Integer) {
                cell.setCellValue((Integer) value);
 
            } else if (value instanceof Double) {
                cell.setCellValue((Double) value);
 
            } else if (value instanceof Float) {
                cell.setCellValue((Float) value);
            }
        }
    }
```
