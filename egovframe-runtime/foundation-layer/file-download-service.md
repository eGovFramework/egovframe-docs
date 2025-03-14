---
title: File Download Service
linkTitle: "File Download"
description: 파일 다운로드 기능을 구현한 DownloadController 예제와 JSP 페이지 설정을 설명한다.
url: /egovframe-runtime/foundation-layer/file-upload-download-service/file-download-service/
menu:
    depth:
        name: "File Download"
        weight: 2
        parent: "fileUpload-download"
        identifier: "fileDownload"

---
# File Download Service

## 개요

여기서 다운로드는 대개 큰 컴퓨터에서 작은 컴퓨터로 파일을 전송하는 것을 의미한다. 인터넷 사용자의 입장에서의 다운로드란 다른 컴퓨터에서 파일을 받는 것이다.

## 설명

EgovFrameWork에서는 파일 다운로드를 하기위한 DownloadController 클래스를 간단하게 구현하여 보았다.

**DownloadController** 클래스 예시

```java
@Controller("downloadController")
public class DownloadController {
 
	@Resource(name = "fileUploadProperties")
	Properties fileUploadProperties;
 
	@RequestMapping(value = "/download/downloadFile.do")
	public void downloadFile(
			@RequestParam(value = "requestedFile") String requestedFile,
			HttpServletResponse response) throws Exception {
 
		String uploadPath = fileUploadProperties
				.getProperty("file.upload.path");
 
		File uFile = new File(uploadPath, requestedFile);
		int fSize = (int) uFile.length();
 
		if (fSize > 0) {
 
			BufferedInputStream in = new BufferedInputStream(
					new FileInputStream(uFile));
			// String mimetype = servletContext.getMimeType(requestedFile);
			String mimetype = "text/html";
 
			response.setBufferSize(fSize);d
			response.setContentType(mimetype);
			response.setHeader("Content-Disposition", "attachment; filename=\""
					+ requestedFile + "\"");
			response.setContentLength(fSize);
 
			FileCopyUtils.copy(in, response.getOutputStream());
			in.close();
			response.getOutputStream().flush();
			response.getOutputStream().close();
		} else {
			//setContentType을 프로젝트 환경에 맞추어 변경
			response.setContentType("application/x-msdownload");
			PrintWriter printwriter = response.getWriter();
			printwriter.println("<html>");
			printwriter.println("<br><br><br><h2>Could not get file name:<br>"
					+ requestedFile + "</h2>");
			printwriter
					.println("<br><br><br><center><h3><a href='javascript: history.go(-1)'>Back</a></h3></center>");
			printwriter.println("<br><br><br>&copy; webAccess");
			printwriter.println("</html>");
			printwriter.flush();
			printwriter.close();
		}
	}
}
```

jsp 페이지로 간단하게 구현된 예시

```jsp
<%@ page contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Success</title>
</head>
 
<body>
 
<h1>Success</h1>
 
<p>All good</p>
 
<c:forEach var="file" items="${fileInfoList}" varStatus="status">
 
순번 : <c:out value="${status.count}" />
	<br />
uploadedFilePath : <c:out value="${file.filePath}" />
	<br />
파일명 : <a
		href="#" onclick="window.open(encodeURI('<c:url value='/download/downloadFile.do?'/>requestedFile=${file.fileName}'))"><c:out
		value="${file.fileName}" /></a>
	<br />
파일사이즈 : <c:out value="${file.fileSize}" />
	<br />
	<p />
</c:forEach>
 
</body>
</html>
```

Tomcat에서는 일반적으로 웹 어플리케이션이 GET과 POST 방식으로 파라미터를 넘겨 받을 때 request.setCharacterEncoding()을 통한 문자셋 인코딩이 필요하다.

파일을 다운로드시 한글이 깨지는 문제가 발생할 경우 제우스나 WebLogic의 경우는 JSP 페이지에 아래와 같이 넣어주면 한글 깨지는 문제가 해결된다.

```jsp
<%@ page contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
```

Tomcat에서는 한글이 깨지는 문제가 발생하는데 아래의 링크를 참조

- [Tomcat 한글 설정하기](file-download-service-tomcat-encoding.md)
