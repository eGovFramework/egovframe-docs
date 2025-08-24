---
  title: 화면인쇄
  linkTitle: 화면인쇄
  description: "화면인쇄 서비스는 화면을 인쇄 할수 있는 기능과 인쇄 설정할수있는 기능을 제공한다."
  url: /common-component/elementary-technology/print_scrin/
  menu:
    depth:
      name: 화면인쇄
      weight: 1
      parent: "print"
      identifier: "print_scrin"
---



# 요소기술 - 화면인쇄

## 개요

 화면인쇄 서비스는 화면을 인쇄 할수 있는 기능과 인쇄 설정할수있는 기능을 제공한다.

## 설명

 화면인쇄 서비스는 인쇄미리보기, 인쇄바로하기, 페이지설정 기능으로 구분한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | egovframework.com.utl.fcc.web.EgovComUtlTestController.java | 테스트용 controller |  |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovPrint.jsp | 화면인쇄 테스트 페이지 |  |

##### 관련테이블

**N/A**

## 환경설정

**해당없음**

## 사용방법

익스플로러의경우 인터넷옵션→보완→사용자정의수준→ActiveX관련 항목을 사용을 선택한다.

```html
<script Language="Javascript">
<!--
var NS = 1;
if( document.all) NS = 0;
function PrintOption(type1,type2){
//네스케이프일 경우
        if (NS) {
                window.print();
//익스플로러일 경우
        } else {
                var active = '<OBJECT ID="active1" WIDTH=0 HEIGHT=0 CLASSID="CLSID:8856F961-340A-11D0-A96B-00C04FD705A2"></OBJECT>';
                document.body.insertAdjacentHTML('beforeEnd', active);
                active1.ExecWB(type1,type2); 
                active1.outerHTML ="";
        }
}
//-->
</script>
<input type=button value="인쇄 미리 보기" onclick="PrintOption(7,1)">  
<input type=button value="인쇄 바로 하기" onclick="PrintOption(6,-1)">
<input type=button value="페이지 설정" onclick="PrintOption(8,1)">
```

## 참고자료

 N/A