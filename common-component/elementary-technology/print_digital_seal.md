---
  title: 전자관인출력
  linkTitle: 전자관인출력
  description: "기관코드, 관인구분을 받아 해당 관인이미지를 출력하는 기능을 제공한다."
  url: /common-component/elementary-technology/print_digital_seal/
  menu:
    depth:
      name: 전자관인출력
      weight: 3
      parent: "print"
      identifier: "print_digital_seal"
---



# 요소기술 - 전자관인 출력

## 개요

 기관코드, 관인구분을 받아 해당 관인이미지를 출력하는 기능을 제공한다.

## 설명

 입력된 URL의 해당 관인이미지를 출력한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | egovframework.com.utl.pao.web.EgovErncslController.java | 전자관인 출력 controller |  |
| VO | egovframework.com.utl.pao.service.PrntngOutptVO.java | 전자관인 VO |  |
| Controller | egovframework.com.utl.pao.web.EgovPrntngOutptController.java | 테스트용 controller |  |
| Service | egovframework.com.utl.pao.service.EgovPrntngOutpt.java | 테스트용 인터페이스 |  |
| ServiceImpl | egovframework.com.utl.pao.service.impl.EgovPrntngOutptImpl.java | 테스트용 구현 |  |
| DAO | egovframework.com.utl.pao.service.impl.PrntngOutptDAO.java | 테스트용 데이터 처리 |  |
| JSP | /WEB-INF/jsp/egovframework/cmm/utl/EgovErncslOutpt.jsp | 테스트 페이지 |  |

## 사용방법

```html
<%@page import="egovframework.com.utl.pao.service.EgovPrntngOutpt"  %>
 
<img src="/utl/pao/EgovErncsl.do?sOrgCode=<%=sOrgCode%>&sErncslSe=<%=sErncslSe%>">
```

 관인정보에 확인에 필요한 sOrgCode : 기관코드, sErncslSe : 관인구분으로 해당관인을 직접 출력한다.