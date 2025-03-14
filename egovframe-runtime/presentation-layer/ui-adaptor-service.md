---
title: UI Adaptor Service
linkTitle: "UI Adaptor"
description: 전자정부 표준프레임워크에서는 Spring MVC Annotation을 기반으로 요청 URI와 Controller 메소드를 매핑하며, 메소드 파라미터로 업무용 DTO 객체를 사용할 수 있도록 가이드한다. UI 솔루션과의 연동 방식은 프로젝트 특성에 맞게 설계해야 하며, 보통 Controller에서 데이터를 DTO 형태로 변환하여 업무 로직으로 넘기는 방식이 많이 사용된다.
url : /egovframe-runtime/presentation-layer/ui-adaptor-service/
menu:
    depth:
        name: UI Adaptor
        weight: 7
        parent: "presentation-layer"
---
# UI Adaptor Service

## 개요

전자정부 표준프레임워크와 UI 솔루션(Rich Internet Application) 연동에 대해 살펴 본다.
UI Adaptor를 적용하는 방식은 특정한 하나의 방법을 표준화하기 어렵다.
보통 Web Framework 과 UI 솔루션과의 연동을 하는 방법 중 가장 많이 사용하는 방식은
Controller 역할을 수행하는 Servlet 객체에서 업무 로직을 호출 전 데이터를 DTO 형태로 변화하여 업무 로직으로 넘기는 방식이다.

전자정부 표준프레임워크에서는 Spring MVC Annotation 기반으로 개발 시 요청되는 URI 와 Controller 클래스내의 메소드를 매핑하고 있다.
따라서 메소드의 파라미터로 넘어오는 객체가 request 객체가 아닌 업무용 DTO 클래스로 넘어올 수 있도록 가이드 하는 방식을 선택했다.
(사실 @ModelAttribute 를 이용하는 것과 같다.)
하지만 프로젝트 별로 비기능 요구사항의 특성을 고려하여 적합한 구조를 정의하여 적용하는 것이 필요하다.

UI 솔루션 업체별 상세 가이드
- [연동_샘플_설명서포함_.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:rte:ptl:%EB%A7%88%EC%9D%B4%ED%94%8C%EB%9E%AB%ED%8F%BC_%EC%97%B0%EB%8F%99_%EC%83%98%ED%94%8C_%EC%84%A4%EB%AA%85%EC%84%9C%ED%8F%AC%ED%95%A8_.zip) - written by 고석률(MiPlatform)
- [XPlatform.zip](https://maven.egovframe.go.kr/publist/HDD1/public/XPlatform.zip) - XPlatform 제공(신규 템플릿)
- 넥사크로
  - [넥사크로플랫폼 UI Adaptor 개발가이드.zip](https://maven.egovframe.go.kr/publist/HDD1/public/nexacro14/nexacroPlatform_UI%20Adaptor-Guide.zip) - 넥사크로플랫폼
  - [nexacro14_2015.03.05.01(14.0.0.143).zip](https://maven.egovframe.go.kr/publist/HDD1/public/nexacro14/nexacro14_2015.03.05.01(14.0.0.143).zip) - nexacro14
  - [eGovFrame-3.2.7z](https://maven.egovframe.go.kr/publist/HDD1/public/nexacro14/eGovFrame-3.2.7z) - 개발프로젝트
- 토마토시스템즈
- SHIFT(Gauce)

## 설명

중점적으로 우리가 살펴볼 내용은 Controller 앞단에서 UI 솔루션으로부터 넘어온 데이터를 DTO 로 변환하는 과정이다.
데이타 변환을 위해 우리는 ArgumentResolver 를 이용한 방법을 살펴보도록 하겠다.
UI 솔루션으로 넘어오는 데이터 객체는 request 객체에 포함되어 넘어온다. 우리가 필요한 것은 업무용 DTO 클래스이다.
업무용 DTO 클래스는 URI(@RequestMapping)와 매핑 된 Controller 메소드의 파라미터로 존재하게 된다.
Controller 메소드의 파라미터에 설정된 클래스(여기서는 DTO)를 AnnotationMethodHandlerAdapter 에서
그에 해당하는 ArgumentResolvers(customArgumentResolvers포함) 를 호출해준다.
따라서 우리는 ArgumentResolver를 확장하여 CustomRiaArgumentResolver 개발하여 AnnotationMethodHandlerAdapter에 등록한다.
CustomRiaArgumentResolver 에서 리턴되는 객체는 Contorller 단의 메소드의 파라미터로 이용된다.
* 참고 : AnnotationMethodHandlerAdapter 는 URI 와 매핑되는 Contorller 의 메소드를 실행 시 파라미터로 존재하는 객체타입에대한 ArgumentResolver를 실행하여 가져온다.

그리고 Controller단의 실행 결과는 ViewResovler를 통해 RiaView 로 전송되며 RiaVeiw는 결과물인 DTO 를 UI 솔루션 데이터 타입으로 변환하여 response로 보내어 진다.
다시 핵심적인 내용을 정리하자면 다음과 같다.

1. AnnotationMethodHandlerAdapter 의 CustomRiaArgumentResolver 등록 ⇒ CustomRiaArgumentResolver
2. UIAdaptor 등록 ⇒ UIAdaptorImpl
3. RiaView 등록 ⇒ RiaView

사용되는 DTO 를 아래 클래스로 생각하고 살펴보겠다.

UdDTO.java(샘플)

```java
...
public class UdDTO implements Serializable {
 
    private Map variableList ;
    private Map dataSetList ;
    private Map Objects ;
 
    public void setVariableList(Map variableList) {
	this.variableList= variableList;
    }
 
    public void setDataSetList(Map dataSetList) {
	this.dataSetList= dataSetList;
    }
 
    public Map getVariableList() {
        return variableList;
    }
 
    public Map getDataSetList() {
        return dataSetList;
    }
 
    public void setObjects(Map objects) {
	Objects = objects;
    }
 
    public Map getObjects() {
	return Objects;
    }
}
...
```

### UI솔루션데이타에서 DTO로 변환

다음은 UTO 를 가져와 UI 솔루션에 의해 들어오는 객체로부터 UTO 로 변환하는 부분을 설명한다.
변환을 담당하는 UIAdaptorImpl 객체는 AnnotationMethodHandlerAdapter 의 **CustomRiaArgumentResolver** 에 설정된다.

**설정정보(CustomRiaArgumentResolver)**

```xml
<bean class="org.springframework.web.servlet.mvc.annotation.AnnotationMethodHandlerAdapter">
    <property name="webBindingInitializer">
        <bean class="egovframework.rte.fdl.web.common.EgovBindingInitializer" />
    </property>
    <property name="customArgumentResolvers">
        <list>
            <bean class="egovframework.rte.fdl.sale.web.CustomRiaArgumentResolver">
                <property name="uiAdaptor">
                    <ref bean="riaAdaptor" />
                </property>
            </bean>
        </list>
    </property>
</bean>
```

WebArgumentResolver의 구현체인 CustomRiaArgumentResolver 는 uiAdaptor 에 세팅된 Adaptor 를 실행해준다.

**CustomRiaArgumentResolver.java**

```java
public class CustomRiaArgumentResolver implements WebArgumentResolver {
 
	private UiAdaptor uiA;
 
	public void setUiAdaptor(UiAdaptor uiA) {
		this.uiA = uiA;
	}
 
	public Object resolveArgument(MethodParameter methodParameter, NativeWebRequest webRequest) throws Exception {
 
		Class<?> type = methodParameter.getParameterType();
		Object uiObject = null;
 
		if (uiA == null)
			return UNRESOLVED;
 
		//Controller의 실행되는 메소드의 파라미터타입 정보가 MethodParameter를 통해 넘어온다. 
		//설정한 UIAdaptro 구현체에 등록되어 있는 UTO 와 비교한다.
		if (type.equals(uiA.getModelName())) {
			HttpServletRequest request = (HttpServletRequest) webRequest.getNativeRequest();
			// 여기서 데이타 만들어 넘긴다.
			uiObject = (UdDTO) uiA.convert(request);
			return uiObject;
		}
 
		return UNRESOLVED;
	}
...
```

UiAdaptor 의 구현체는 아래와 같다. 여기서는 Miplatform 의 예를 들어 코드를 작성하였다.
UI 솔루션의 객체에서 DTO 로 데이터를 옮기는 역할은 converte4In 메소드에서 수행된다.

**RiaAdaptorImpl.java(MiPlatform ⇒ UdDTO)**

```java
public class RiaAdaptorImpl implements UiAdaptor {
 
  protected Log log = LogFactory.getLog(this.getClass());
 
 
  //resolveArgument 메소드에서 호출하는 메소드 
	public Object convert(HttpServletRequest request) throws Exception {
 
		PlatformRequest platformRequest = null;
 
		try {
			platformRequest = new PlatformRequest(request, PlatformRequest.CHARSET_UTF8);
			platformRequest.receiveData();
		} catch (IOException ex) {
			ex.getStackTrace();
			// throw new IOException("PlatformRequest error");
		}
    //UI 솔루션 데이터에서 DTO 객체로 변환
		UdDTO dto = converte4In(platformRequest);
		return dto;
	}
 
	private UdDTO converte4In(PlatformRequest platformRequest) {
		UdDTO dto = new UdDTO();
		//... DTO 또는 VO 값 채우기 
		.....
		return dto;
	}
 
	public Class getModelName() {
		return UdDTO.class;
	}
}
```

### Controller 메소드 구현

UdDTO 클래스는 CustomRiaArgumentResolver 에서 만들어져 Controller 의 메소드의 parameter 형태로 가져온다.
아래 예는 Controller 단의 메소드 이다.

**XXCategoryController.java**

```java
...
	@RequestMapping("/sample/miplatform.do")
	public ModelAndView selectCategoryList4Mi(UdDTO miDto, Model model) throws Exception {
 
		ModelAndView mav = new ModelAndView("riaView");
 
		//조회조건이 있을 경우 사용될 Map
		Map<String, String> smp = new HashMap<String, String>();
		try {
 
		  //Biz Layer 를 호출 한다. 
			List resultList = categoryService.selectCategoryList(smp);
 
			//결과값을 모델에 저장 
			mav.addObject("MiDTO", resultList);
 
		} catch (Exception ex) {
			log.info(ex.getStackTrace(), ex);
		}
		return mav;
	}
```

### BeanNameViewResolver 설정

모델 객체의 이름이 riaView 이다. 이것은 Bean Name을 직접 명시한 것으로 아래와 같은 설정(BeanNameViewResolver)이 필요하다.

```xml
<bean class="org.springframework.web.servlet.view.BeanNameViewResolver" p:order="0" />
 
<bean class="org.springframework.web.servlet.view.UrlBasedViewResolver"
		p:order="1" p:viewClass="org.springframework.web.servlet.view.JstlView"
		p:prefix="/WEB-INF/jsp/" p:suffix=".jsp" />
 
<bean id="riaView" class="egovframework.rte.fdl.sale.web.RiaView" />
```

### RiaView 구현

RiaView 의 코드는 아래와 같다. DTO 를 업체에 맞춰 다시 가져 나가기 위해 convert 하는 모듈이다.
여기서는 Miplatform 객체로 변환한다. egovDs 라는 DataSet 으로 객체화 한후 stream 형태로 보내는 로직이다.
따라서 업체별 데이타 형태로 변환하여 보내도록 수정하면 된다.

**RiaView.java(DTO ⇒ MiPlatform)**

```java
....
public class RiaView extends AbstractView {
 
	protected Log log = LogFactory.getLog(this.getClass());
 
	@SuppressWarnings("unchecked")
	@Override
	protected void renderMergedOutputModel(Map model, HttpServletRequest request, HttpServletResponse response)
	        throws Exception {
		VariableList miVariableList = new VariableList();
		DatasetList miDatasetList = new DatasetList();
		PlatformData platformData = new PlatformData(miVariableList, miDatasetList);
 
		List list = (List) model.get("MiDTO");
 
		Iterator<Map> iterator = list.iterator();
		Iterator<Map> dataIterator = list.iterator();
 
		Dataset dataset = new Dataset("egovDs");
 
		while (iterator.hasNext()) {
			// Header 세팅
			Map<String, Object> record = iterator.next();
			Iterator<String> si = record.keySet().iterator();
 
			while (si.hasNext()) {
				String key = si.next();
				dataset.addColumn(key, ColumnInfo.COLUMN_TYPE_STRING, (short) 255);
			}
		}
 
		while (dataIterator.hasNext()) {
			Map<String, Object> record = dataIterator.next();
			Iterator<String> si = record.keySet().iterator();
			// Header 세팅
			while (si.hasNext()) {
				String key = si.next();
				dataset.addColumn(key, ColumnInfo.COLUMN_TYPE_STRING, (short) 255);
			}
 
			// Value 세팅
			int row = dataset.appendRow();
			Iterator<String> si2 = record.keySet().iterator();
			while (si2.hasNext()) {
				String key = si2.next();
				String value = (String) record.get(key);
 
				System.out.println("key = " + key + " , value = " + value);
				dataset.setColumn(row, key, value);
			}
			miDatasetList.add(dataset);
		}
		try {
 
			new PlatformResponse(response, PlatformConstants.CHARSET_UTF8).sendData(platformData);
 
		} catch (IOException ex) {
			if (log.isErrorEnabled()) {
				log.error("Exception occurred while writing xml to MiPlatform Stream.", ex);
			}
 
			throw new Exception();
		}
 
	}
 
}
```

# 참고자료


