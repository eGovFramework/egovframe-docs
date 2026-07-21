# 요소기술 Validation 체크

> **참고 (5.0.0)**: 표준프레임워크 5.0.0부터 유효성 검증은 Jakarta Bean Validation(`@Valid`) 기반으로 전환되어, 본 문서의 Commons Validator 방식(validator XML)은 4.x 이하 버전에서 참고할 수 있습니다. (출처: 표준프레임워크 업그레이드 가이드 v5.0, 2026-06)

## 개요

 개발된 모든 공통기술에는 기본으로 제공되는 화면(JSP)의 입력항목에 대해 validation 체크 기능이 제공되어 있으나, 요소기술의 경우 그 쓰임새가 개발하고자 하는 애플리케이션의 개발 목적에 따라 재구현되어 사용되며, 개발될 애플리케이션의 화면(JSP)이 각각 상이하므로 아래와 같은 사용 예를 통해 향후 구현될 수 있는 가이드를 제공한다.
 본 기능은 전자정부 표준프레임워크 실행환경에 구현되어 있는 Validator를 활용한다.

## 설명

```text
  ① 테스트 페이지 내에 날짜(Date) 입력값에 대한 Validation 기능 
  ② 테스트 페이지 내에 숫자(Integer) 입력값에 대한 Validation 기능
```

## 사용방법

 화면별로 체크해야할 날짜, 숫자 validator xml 파일을 작성한다.

```xml
1. 날짜 예시
<field property="fromDate" depends="required,maxlength,date">
    <arg0 key="frm.fromDate" resource="true"/>
    <arg1 key="8" resource="true"/>
    <var>
    <var-name>maxlength</var-name>
    <var-value>8</var-value>
    </var>
</field>
2. 숫자 예시
<field property="size" depends="required,integer">
    <arg0 key="frm.size" resource="true"/>
</field>
```

 체크할 validator xml 파일을 context-validator.xml에 추가한다.

```xml
(예시)
<value>classpath:/egovframework/validator/com/utl/sim/EgovSysInfo.xml</value>
```

 화면에서 validator 처리를 추가한다.

```jsp
(예시)
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="validator" uri="http://www.springmodules.org/tags/commons-validator" %>
<script type="text/javascript" src="<c:url value="/validator.do"/>"></script>
<validator:javascript formName="sysForm3" staticJavascript="false" xhtml="true" cdata="false"/>
 
<script type="text/javaScript" language="javascript">
function fnGetFreeMemory() {
	if(!validateSysForm3(document.sysForm3)){ 		
		return;
	}else{
		document.sysForm3.submit();
	}
}
</script>
 
<form:form name="sysForm3" action ="EgovPageLink.do" method="post">
<table width="430" border="0" cellpadding="0" cellspacing="1" class="table-register">
  <tr>
    <th width="150">유효메모리 체크</th>
    <td width="280"><input type = "button" method="post"  value="실행!" onclick="fnGetFreeMemory();"></td>
  </tr>
  <tr>
    <th width="150">사용할 메모리(MB)</td>
    <td width="280"><input type = "text" name="size" value="" size="40" style="ime-mode: disabled;"/></td>
    </tr>
</table>
</form:form>
```

## 참고자료

- 실행환경 Validator 참조: [Jakarta Commons Validator](../../egovframe-runtime/presentation-layer/security-jakarta-commons-validator.md)
