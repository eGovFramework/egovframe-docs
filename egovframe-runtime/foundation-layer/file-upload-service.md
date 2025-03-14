---
title: File Upload Service
linkTitle: "File Upload"
description: 파일 업로드를 위한 Spring의 CommonsMultipartResolver 설정 및 구현 방법을 설명하며, JSP 폼과 컨트롤러를 통해 파일을 업로드하는 예제를 제공한다. 파일 저장 경로는 properties 파일에서 설정하며, 다중 파일 업로드 시 폼 이름을 다르게 설정해야 한다.
url: /egovframe-runtime/foundation-layer/file-upload-download-service/file-upload-service/
menu:
    depth:
        name: "File Upload"
        weight: 1
        parent: "fileUpload-download"
        identifier: "fileUpload"
---
# File Upload Service

## 개요

업로드는 한 컴퓨터 시스템에서 다른 시스템으로 파일을 전송하는 것을 말하는데, 대개 작은 컴퓨터에서 큰 컴퓨터로 옮길 때 이런 용어를 사용한다. 네트웍 사용자의 관점에서 보면, 파일을 업로드하는 것은 그 파일을 받을 수 있도록 설정된 다른 컴퓨터에 파일을 보내는 것이다. 전자게시판 상의 다른 사용자와 이미지 파일을 공유하기를 원하는 사람들은 그 전자게시판에 파일을 업로드하면 된다.

그러면 반대편 입장에 있는 사람은 그 파일을 다운로드하게 되는데, 여기서 다운로드는 대개 큰 컴퓨터에서 작은 컴퓨터로 파일을 전송하는 것을 의미한다. 인터넷 사용자의 입장에서의 다운로드란 다른 컴퓨터에서 파일을 받는 것이다.

## 설명

파일 업로드 기능을 구현하기 위해서는 먼저 빈 설정 파일에 다음과 같이 **MultiCommonsMultipartResolver**를 정의해야한다. 본 가이드에서는 Apache Commons FileUpload에서 재공하는 CommonsMultipartResolver를 사용하기를 권장한다. CommonsMultipartResolver를 수정하여 사용할 경우 많은 부분에 시간과 노력이 들어갈 것이다.

```xml
<!-- Custom MultiFile resolver -->
<bean id="local.MultiCommonsMultipartResolver"
	class="egovframework.rte.util.web.resolver.MultiCommonsMultipartResolver">
	<property name="maxUploadSize" value="100000000" />
	<property name="maxInMemorySize" value="100000000" />
</bean>
```
[권장]만약 스프링에서 제공하는 Apache Commons FileUpload API를 이용하여 파일 업로드를 처리하는 CommonsMultipartResolver를 사용하려고 하면 빈 설정파일에 다음과 같이 정의한다.
```xml
<!-- MULTIPART RESOLVERS -->
<!-- regular spring resolver -->
<bean id="spring.RegularCommonsMultipartResolver"
	class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
	<property name="maxUploadSize" value="100000000" />
	<property name="maxInMemorySize" value="100000000" />
</bean>
```
또한 해당 컨트롤러의 property로 파일의 업로드 위치를 지정해주고 컨트롤러에서 setter 메소드를 통해 지정된 파일 업로드 위치를 불러올 수 있다. 사용예는 다음과 같다.

#### fileUploadProperties.properties

```properties
# windows NT일 경우  
file.upload.path=C:\\temp
 
# Unix일 경우
file.upload.path=/usr/file/upload
```

```java
@Resource(name = "fileUploadProperties")
Properties fileUploadProperties;
..
..
..
	String uploadPath = fileUploadProperties
			.getProperty("file.upload.path");
	File saveFolder = new File(uploadPath);
..
..
..
```
파일 업로드를 위해 **JSP**파일의 입력 폼 타입을 file로 지정하고 form의 enctype을 multipart/form-data로 지정한다. 예시는 다음과 같다. 이때 **CommonsMultipartResolver**를 사용할 경우 form의 name을 다르게 설정하여야 한다. 중복된 이름을 사용할 경우 에러가 발생한다.
```html
<form method="post" action="<c:url value='/upload/genericMulti.do'/>"
enctype="multipart/form-data">
  <p>Type:
    <input type="text" name="type" value="genericFileMulti" size="60" />
  </p>
  <p>File1:
    <input type="file" name="file[]" size="60" />
  </p>
  <p>File2:
    <input type="file" name="file[]" size="60" />
  </p>
  <p>
    <input type="submit" value="Upload" />
  </p>
</form>
```

다음은 파일 업로드를 위해 Controller를 구현한 모습이다.

```java
@Controller("genericFileUploadController")
public class GenericFileUploadController {
 
@Resource(name = "multipartResolver")
CommonsMultipartResolver multipartResolver;
 
@Resource(name = "fileUploadProperties")
Properties fileUploadProperties;
 
@SuppressWarnings("unchecked")
@RequestMapping(value = "/upload/genericMulti.do")
public String multipartProcess(final HttpServletRequest request, Model model)
	throws Exception {
 
final long startTime = System.nanoTime();
 
/*
 * validate request type
 */
Assert.state(request instanceof MultipartHttpServletRequest,
		"request !instanceof MultipartHttpServletRequest");
final MultipartHttpServletRequest multiRequest = (MultipartHttpServletRequest) request;
 
/*
 * validate text input
 */
Assert.state(request.getParameter("type").equals("genericFileMulti"),
		"type != genericFileMulti");
 
/*
 * extract files
 */
final Map<String, MultipartFile> files = multiRequest.getFileMap();
Assert.notNull(files, "files is null");
Assert.state(files.size() > 0, "0 files exist");
 
/*
 * process files
 */
String uploadPath = fileUploadProperties
		.getProperty("file.upload.path");
File saveFolder = new File(uploadPath);
 
// 디렉토리 생성
if (!saveFolder.exists() || saveFolder.isFile()) {
	saveFolder.mkdirs();
}
 
Iterator<Entry<String, MultipartFile>> itr = files.entrySet()
		.iterator();
MultipartFile file;
List fileInfoList = new ArrayList();
String filePath;
 
while (itr.hasNext()) {
	Entry<String, MultipartFile> entry = itr.next();
	System.out.println("[" + entry.getKey() + "]");
 
	file = entry.getValue();
	if (!"".equals(file.getOriginalFilename())) {
		filePath = uploadPath + "\\" + file.getOriginalFilename();
		file.transferTo(new File(filePath));
 
		FileInfoVO fileInfoVO = new FileInfoVO();
		fileInfoVO.setFilePath(filePath);
		fileInfoVO.setFileName(file.getOriginalFilename());
		fileInfoVO.setFileSize(file.getSize());
		fileInfoList.add(fileInfoVO);
	}
}
 
// 여기서는 DB에 파일관련 정보를 저장하지 않고 단순히 success 페이지로 포워딩 하여 재확인 가능토록 함
model.addAttribute("fileInfoList", fileInfoList);
model.addAttribute("uploadPath", uploadPath);
 
final long estimatedTime = System.nanoTime() - startTime;
System.out.println(estimatedTime + " " + getClass().getSimpleName());
 
return "success";
 
	}
}
```

Tomcat에서는 일반적으로 웹 어플리케이션이 GET과 POST 방식으로 파라미터를 넘겨 받을 때 request.setCharacterEncoding()을 통한 문자셋 인코딩이 필요하다.

## 예제
- [파일업로드 예제](../../runtime-example/individual-example/foundation-layer/file-upload-example.md)