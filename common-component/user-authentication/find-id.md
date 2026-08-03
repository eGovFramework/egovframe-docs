---
title: "아이디 찾기"
linkTitle: "아이디 찾기"
description: "아이디 찾기는 일반회원, 기업회원, 업무사용자 구분에 따라 이름과 이메일주소 정보로 사용자 아이디를 조회하는 기능을 제공한다."
url: /common-component/user-authentication/find-id-password/find-id/
menu:
  depth:
    name: "아이디 찾기"
    weight: 1
    parent: "find-id-password"
---

# 아이디 찾기

## 비즈니스 규칙

 일반 회원, 기업 회원, 업무담당자 세 개의 사용자 구분에 따라 이름, 이메일 정보를 갖고 아이디를 찾기 처리할 수 있다.
 사용자 구분에 따라 조회 대상 테이블과 비교 항목이 달라지며, 상태가 정상(`P`)인 사용자만 조회된다.

| 사용자 구분 | `userSe` | 조회 테이블 | 이름 비교 항목 | 이메일 비교 항목 |
| --- | --- | --- | --- | --- |
| 일반 회원 | `GNR` | COMTNGNRLMBER | 회원명(`mber_nm`) | 회원이메일주소(`mber_email_adres`) |
| 기업 회원 | `ENT` | COMTNENTRPRSMBER | 회사명(`cmpny_nm`) | 신청자이메일주소(`applcnt_email_adres`) |
| 업무 사용자 | `USR` | COMTNEMPLYRINFO | 사용자명(`user_nm`) | 이메일주소(`email_adres`) |

## 관련코드

### 요청 VO

 아이디 찾기 입력값은 `SearchIdRequestVO`로 전달되며, 필수 입력과 이메일 형식은 Bean Validation 어노테이션으로 검증한다.

```java
// egovframework.com.cmm.SearchIdRequestVO
public class SearchIdRequestVO extends BaseRequestVO {

    /** 이름 */
    @EgovNullCheck
    private String name;

    /** 이메일주소 */
    @EgovNullCheck
    @EgovEmailCheck
    private String email;
}
```

 사용자구분(`userSe`)은 상위 클래스인 `BaseRequestVO`에 정의되어 있다.

### jsp

```html
<!-- 1. 사용자 업무구분 : 탭 선택 시 hidden 필드 userSe 값이 변경된다. -->
<form:form name="idForm" modelAttribute="searchIdRequestVO"
           action="${pageContext.request.contextPath}/uat/uia/searchId.do" method="post">
<div class="login_type">
  <ul>
    <li><a id="idGnr" onClick="fnCheckUsrId('GNR');" class="on">일반</a></li>
    <li><a id="idEnt" onClick="fnCheckUsrId('ENT');">기업</a></li>
    <li><a id="idUsr" onClick="fnCheckUsrId('USR');">업무</a></li>
  </ul>
</div>

<!-- 2. 아이디를 찾기위한 조건 : 이름, 이메일주소 -->
<label for="name">이름</label>
<input type="text" name="name" maxlength="20" />
<label for="email">이메일</label>
<input type="text" name="email" maxlength="30" />

<input name="userSe" type="hidden" value="GNR">
</form:form>
```

 서버측 검증에서 오류가 발생하면 `BindingResult`의 필드 오류를 조회하여 입력항목 아래에 메시지를 출력한다.

```jsp
<c:set var="idErrors" value="${requestScope['org.springframework.validation.BindingResult.searchIdRequestVO']}"/>
<c:if test="${not empty idErrors && idErrors.hasFieldErrors('name')}">
    ${idErrors.getFieldError('name').defaultMessage}
</c:if>
```

### controller

```java
// egovframework.com.uat.uia.web.EgovLoginController
@RequestMapping(value = "/uat/uia/searchId.do")
public String searchId(@Valid @ModelAttribute("searchIdRequestVO") SearchIdRequestVO searchIdRequestVO,
                       BindingResult bindingResult, ModelMap model) throws Exception {

    // Validation 에러 체크
    if (bindingResult.hasErrors()) {
        // 비밀번호 힌트 공통코드 조회 (폼 재표시를 위해)
        ComDefaultCodeVO vo = new ComDefaultCodeVO();
        vo.setCodeId("COM022");
        List<CmmnDetailCode> code = cmmUseService.selectCmmCodeDetail(vo);
        model.addAttribute("pwhtCdList", code);
        return "egovframework/com/uat/uia/EgovIdPasswordSearch";
    }

    // SearchIdRequestVO에서 LoginVO로 데이터 복사
    LoginVO loginVO = new LoginVO();
    String name = searchIdRequestVO.getName();
    loginVO.setName(name != null ? name.replaceAll(" ", "") : "");
    loginVO.setEmail(searchIdRequestVO.getEmail());
    loginVO.setUserSe(searchIdRequestVO.getUserSe());

    // 1. 아이디 찾기
    LoginVO resultVO = loginService.searchId(loginVO);

    if (resultVO != null && resultVO.getId() != null && !resultVO.getId().equals("")) {
        model.addAttribute("resultInfo", "아이디는 " + resultVO.getId() + " 입니다.");
        return "egovframework/com/uat/uia/EgovIdPasswordResult";
    } else {
        model.addAttribute("resultInfo", egovMessageSource.getMessage("fail.common.idsearch"));
        return "egovframework/com/uat/uia/EgovIdPasswordResult";
    }
}
```

 입력한 이름과 이메일을 가지고 사용자 테이블에서 아이디를 조회한다.
 이름은 공백을 제거한 뒤 조회 조건으로 사용하며, 조회 결과는 `EgovIdPasswordResult.jsp` 화면에 출력한다.

## 관련화면 및 수행매뉴얼

### 1. 아이디 찾기

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 아이디조회 | /uat/uia/searchId.do | searchId | LoginUsr.searchId |

 업무구분, 이름, 이메일주소 정보를 가지고 사용자 아이디를 조회한다.

 ![image](./images/uat-findid-idpwfind1.jpg)
 업무구분 선택: 사용자 업무구분을 선택한다.
 이름 입력: 이름을 입력한다.
 이메일 입력: 이메일을 입력한다.
 아이디 찾기: 업무구분, 이름, 이메일 정보를 통해 사용자 아이디를 조회한다.
