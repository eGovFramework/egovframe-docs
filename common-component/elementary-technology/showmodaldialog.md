---
  title: showModalDialog 대체 기능
  linkTitle: showModalDialog 대체 기능
  description: "다국어 지원을 위한 국가간 날짜 표시 변환 기능을 제공한다."
  url: /common-component/elementary-technology/showmodaldialog/
  menu:
    depth:
      name: showModalDialog 대체 기능
      weight: 5
      parent: "new-components-v3.2"
      identifier: "showmodaldialog"
---



# 요소기술 - showModalDialog 대체 기능

## 개요

 JavaScript의 Modal 방식의 dialog를 지원하는 windows.showModalDialog의 기능이 chrome 37 버전부터 지원하지 않음에 따라 대체 기능을 제공한다.

## 설명

 showModalDialog 대체 기능은 기존 showModalDialog 함수를 그대로 사용할 수 있도록 처리되었으면, 파라미터 전달 및 return 전달에 필요한 경우 추가적인 함수만을 호출하도록 제공된다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| js | /js/egovframework/com/cmm/showModalDialog.js | 기존 showModalDialog 대체 기능 제공 | showModalDialog() 함수를 호출하는 페이지에 필요 |
| js | /js/egovframework/com/cmm/showModalDialogCallee.js | 기존 showModalDialog 대체 기능 제공 | 팝업으로 호출되는 페이지에 필요 |

 [showmodaldialog.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3:cmm:showmodaldialog.zip)

## 환경설정

 **해당 없음**

## 사용방법

### 1. 본 화면(opener) JSP 상에 javascript 포함

```xml
<script type="text/javascript" src="<c:url value='/js/egovframework/com/cmm/showModalDialog.js'/>" ></script>
```

 혹, 공통된 형태로 js 상에 기능을 제공하는 경우는 6번 항목 참조한다.

### 2. 호출된 팝업화면 JSP 상에 javascript 포함

```xml
<script type="text/javascript" src="<c:url value='/js/egovframework/com/cmm/showModalDialogCallee.js'/>" ></script>
```

### 3. 팝업 화면 상에서 "window.dialogArguments" 처리

 팝업 화면 상에서 본 화면에서 넘기는 argument를 “window.dialogArguments”를 통해 가져오는 경우 다음과 같이 수정 필요

 * 기존

```javascript
	var varParam = window.dialogArguments;
```

 * 변경

```javascript
	getDialogArguments();
 
	var varParam = window.dialogArguments;
```

### 4. 본 화면 (opener) 상으로 결과를 넘기기 위해 "window.returnValue" 처리

 팝업 화면 상에서 본 화면으로 “window.returnValue = retVal” 형태로 결과를 넘기는 경우 다음과 같이 수정 필요

 * 기존

```javascript
	parent.window.returnValue = retVal;
	parent.window.close();
```

 * 변경

```javascript
	setReturnValue(retVal);
 
	parent.window.returnValue = retVal;
	parent.window.close();
```

### 5. 본 화면 (opener) 상으로 넘어온 결과를 처리하는 부분

 본 화면 상에서 팝업으로부터 데이터를 가져와 처리하는 부분은 다음과 같이 showModalDialogCallback() function 정의 필요

```javascript
function showModalDialogCallback(retVal) {
	if (retVal) {
 
		alert('retVal = ' + retVal);
	}
}
```

 위 showModalDialogCallback function에는 기존 showModalDialog에서 리턴된 값을 처리하는 부분을 지정함

 다만, 기존에 사용되는 변수 등의 값이 전달되지 않기 때문에 전역변수로 선언된 otherParameters 배열 변수를 다음과 같이 활용 할 수 있음

 * 기존

```javascript
function fn_caller(frm, sDate, vDate) {
 
	retVal = window.showModalDialog(url, varParam, openParam);
 
	if (retVal) {
		if(fn_egov_NormalCalendar.arguments.length == 2){
			sDate.value = retVal.vDate;
		}else{
			sDate.value = retVal.sDate;
			vDate.value = retVal.vDate;
		}
	}
 
}
```

 * 변경

```javascript
function fn_caller(frm, sDate, vDate) {
 
	retVal = window.showModalDialog(url, varParam, openParam);
 
	otherParameters[0] = fn_egov_NormalCalendar.arguments.length;
	otherParameters[1] = sDate;
	otherParameters[2] = vDate;
 
	if (retVal) {
		if(fn_egov_NormalCalendar.arguments.length == 2){
			sDate.value = retVal.vDate;
		}else{
			sDate.value = retVal.sDate;
			vDate.value = retVal.vDate;
		}
	}
 
}
 
function showModalDialogCallback(retVal) {
	if (retVal) {
		if (otherParameters[0] == 2) {
			otherParameters[1].value = retVal.vDate;
		} else {
			otherParameters[1].value = retVal.sDate;
			otherParameters[2].value = retVal.vDate;
		}
	}
}
```

### 6. 공통 js 파일을 통해 처리하는 경우 js 파일 처리

 공통 js를 통해 공통 기능이 제공되는 경우 원 js 파일에 대하여 다음과 처리하면 개별 JSP 파일에 &lt;script&gt;를 추가하실 필요는 없음

 다음과 같이 활용할 수 있다.

```javascript
function dirname(path) {
	if (path.lastIndexOf("/") == -1)
		return "./";
	return path.replace(//g, '/').replace(//[^/]*/?$/, '') + "/";
}
 
function getActiveScript() {
	var d = document.getElementsByTagName("script");
	var path = dirname(d[d.length - 1].src);
	delete d;
 
	var offset=path.indexOf(location.host)+location.host.length;
	return path.substring(offset);
} 
 
 
function getContextPath(){
    var offset=location.href.indexOf(location.host)+location.host.length;
    var ctxPath=location.href.substring(offset, location.href.indexOf('/',offset+1));
 
    if ((/^/js/).test(getActiveScript())) {
    	return "";
    }
 
    return ctxPath;
}
 
function loadScript(src, f) {
  var head = document.getElementsByTagName("head")[0];
  var script = document.createElement("script");
  script.src = src;
  var done = false;
  script.onload = script.onreadystatechange = function() { 
    // attach to both events for cross browser finish detection:
    if ( !done && (!this.readyState ||
      this.readyState == "loaded" || this.readyState == "complete") ) {
      done = true;
      if (typeof f == 'function') f();
      // cleans up a little memory:
      script.onload = script.onreadystatechange = null;
      head.removeChild(script);
    }
  };
  head.appendChild(script);
}
 
loadScript(getContextPath() + '/js/egovframework/com/cmm/showModalDialog.js');
```

### 7. showModalDialog 여러 개인 경우

 하나의 JSP 상에 여러 showModalDialog를 사용하는 경우 각 호출마다 다른 callback 메소드를 호출하여야 한다.

 이런 경우 다음과 같이 callback 메소드 명을 추가로 지정하면 된다.

```javascript
	var openParam = "dialogWidth:700px;dialogHeight:365px;scroll:no;status:no;center:yes;resizable:yes;";
 
	retVal = window.showModalDialog(url, varParam, openParam, "zipCallback");
```

 참고로 공통 js로 제공되는 달력, 우편번호, 결재자 지정은 자체적은 callback 메소드를 사용하기 때문에 개별 업무에서 별도의 callback 메소드 명을 지정할 필요가 없다.

 (자제적으로 여러 개 showModalDialog를 갖는 경우, 지정 필요)

## 참고자료

 **해당없음**