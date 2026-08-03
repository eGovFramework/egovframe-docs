---
title: "요소기술 Validation 체크"
linkTitle: "요소기술 Validation 체크"
description: "Jakarta Bean Validation 어노테이션과 EgovValidation.js를 이용한 공통컴포넌트 화면 입력값 유효성 검증 방법"
url: /common-component/elementary-technology/formatter-util/validation-check/
menu:
  depth:
    name: "요소기술 Validation 체크"
    weight: 25
    parent: "formatter-util"
---

# 요소기술 Validation 체크

## 개요

공통컴포넌트에서 기본으로 제공하는 화면(JSP)에는 입력항목에 대한 Validation 체크 기능이 구현되어 있다.
다만 요소기술은 개발하고자 하는 애플리케이션의 목적에 따라 재구현되어 사용되고 화면 또한 각각 상이하므로,
본 문서는 공통컴포넌트에 실제 적용된 방식을 사용 예로 제시하여 향후 구현 시 참고할 수 있는 가이드를 제공한다.

공통컴포넌트 5.0의 유효성 검증은 다음 두 계층으로 구성된다.

| 구분 | 검증 위치 | 사용 기술 |
| --- | --- | --- |
| 클라이언트측 검증 | 화면(JSP) 제출 직전 | `EgovValidation.js` (`validate*(form)` 함수) |
| 서버측 검증 | Controller 파라미터 바인딩 시점 | Jakarta Bean Validation(`@Valid`) + Spring `Validator` |

두 계층은 상호 보완 관계이며, 클라이언트측 검증은 사용자 편의를 위한 사전 확인이므로 서버측 검증을 반드시 함께 적용해야 한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 스크립트 | js/egovframework/com/cmm/EgovValidation.js | 클라이언트사이드 검증 라이브러리 |
| 메시지 | egovframework/message/com/message-validation_ko.properties | 검증 메시지 (한글/영문 제공) |
| 유틸리티 | egovframework.com.cmm.validation.EgovCommonValidator.java | 비밀번호 연속·반복·조합 검사 등 공통 검증 로직 |
| 공통처리 | egovframework.com.cmm.web.EgovValidationControllerAdvice.java | 검증 오류 메시지 공통 변환 및 전역 Validator 등록 |
| Validator | egovframework.com.sym.bat.validation.BatchOpertValidator.java | 커스텀 Validator 구현 |
| Validator | egovframework.com.sym.sym.bak.validation.BackupOpertValidator.java | 커스텀 Validator 구현 |
| Validator | egovframework.com.uss.umt.validation.PasswordManageMapValidator.java | 커스텀 Validator 구현 |

## 서버측 검증

### model(VO)에 검증 어노테이션 선언

검증 규칙은 model 클래스의 필드에 어노테이션으로 선언한다.
표준 Jakarta Bean Validation 어노테이션과 표준프레임워크 실행환경이 제공하는 확장 어노테이션을 함께 사용할 수 있다.

**Jakarta Bean Validation 표준 어노테이션** (`jakarta.validation.constraints.*`)

| 어노테이션 | 설명 |
| --- | --- |
| `@Size(max=n)` | 문자열 최대/최소 길이 |
| `@Pattern(regexp=..., message=...)` | 정규식 형식 검사 (날짜, 숫자 등) |
| `@NotNull` / `@NotBlank` / `@NotEmpty` | 필수 입력 |
| `@Min(n)` / `@Max(n)` / `@Positive` | 숫자 범위 |
| `@Email` | 이메일 형식 |
| `@AssertTrue(message=...)` | 두 개 이상의 필드를 함께 판단하는 교차 검증 |

**표준프레임워크 확장 어노테이션** (`org.egovframe.rte.ptl.reactive.validation.*`)

실행환경 라이브러리(`egovframe-rte-ptl-reactive`)는 다음 11개의 검증 어노테이션을 제공한다.

| 어노테이션 | 검증 내용 | 기본 메시지 키 |
| --- | --- | --- |
| `@EgovNullCheck` | 필수 입력값 여부 (`null`, 빈 문자열, 빈 배열·컬렉션 불가) | `validation.nullCheck` |
| `@EgovEmailCheck` | 이메일 주소 형식 | `validation.emailCheck` |
| `@EgovPwdCheck` | 비밀번호 형식 (8~20자, 공백 불가, 영문자·숫자·특수문자 조합, 동일 문자 3자 이상 반복 불가, 연속된 문자 3자 이상 불가) | `validation.pwdCheck` |
| `@EgovPhoneCheck` | 전화번호 형식 (하이픈 제외 9~11자리 숫자) | `validation.phoneCheck` |
| `@EgovMobilePhoneCheck` | 휴대전화번호 형식 (010, 011, 016~019로 시작) | `validation.mobilePhoneCheck` |
| `@EgovRrnCheck` | 주민등록번호 (형식 + 검증번호 계산, 2020년 10월 이전 발급 기준) | `validation.rrnCheck` |
| `@EgovCnCheck` | 법인등록번호 13자리 (형식 + 검증번호 계산) | `validation.cnCheck` |
| `@EgovCrnCheck` | 사업자등록번호 10자리 (형식 + 검증번호 계산) | `validation.crnCheck` |
| `@EgovIPCheck` | IP 주소 형식 (IPv4 / IPv6) | `validation.ipCheck` |
| `@EgovKoreanCheck` | 한글만 입력 | `validation.koreanCheck` |
| `@EgovEnglishCheck` | 영문만 입력 | `validation.englishCheck` |

전화번호, 휴대전화번호, 주민등록번호, 법인등록번호, 사업자등록번호는 값에서 하이픈(`-`)을 제거한 뒤 검사하므로
`010-1111-1111`, `01011111111` 형태를 모두 허용한다.
공통컴포넌트에서는 이 중 `@EgovNullCheck`, `@EgovEmailCheck`, `@EgovPwdCheck`를 사용하고 있다.

```java
// 날짜(Date) 입력값에 대한 Validation 예시
// egovframework.com.uss.ion.ans.service.AnnvrsryManage
@EgovNullCheck
@Size(max = 10)
@Pattern(regexp = "^\\d{4}-\\d{2}-\\d{2}$", message = "{validation.pattern.date}")
private String annvrsryDe;    // 기념일자
```

```java
// 숫자(Number) 입력값에 대한 Validation 예시
// egovframework.com.uss.ion.yrc.service.IndvdlYrycManage
@EgovNullCheck
@Positive
@Min(1)
private Double occrncYrycCo;  // 발생연차개수
```

`message` 속성에 지정한 `{validation.pattern.date}`, `{validation.pattern.integer}` 등의 키는
`message-validation_ko.properties`에 정의되어 있다.

### Controller에서 검증 수행

검증 대상 model 파라미터에 `@Valid`를 지정하고 바로 뒤에 `BindingResult`를 선언한 뒤,
`hasErrors()`로 오류 여부를 판단하여 입력 화면으로 되돌려 준다.

```java
// egovframework.com.utl.sys.htm.web.EgovHttpMonController
@PostMapping("/utl/sys/htm/EgovComUtlHttpMonRegist.do")
public String insertHttpMon(
        @Valid @ModelAttribute("httpMon") HttpMon httpMon,
        BindingResult bindingResult,
        ModelMap model,
        RedirectAttributes redirectAttributes) throws Exception {

    if (bindingResult.hasErrors()) {
        return "egovframework/com/utl/sys/htm/EgovComUtlHttpMonRegist";
    }

    egovHttpMonService.insertHttpMon(httpMon);
    return "forward:/utl/sys/htm/EgovComUtlHttpMonList.do";
}
```

### 커스텀 Validator (복합 검증)

어노테이션만으로 표현하기 어려운 검증(파일 존재 여부 확인, 필드 간 비교 등)은
Spring의 `Validator` 인터페이스를 구현한 커스텀 Validator로 처리한다.
공통컴포넌트에 구현되어 있는 커스텀 Validator는 다음과 같다.

| 클래스 | 빈 이름 | 검증 대상 | 검증 내용 |
| --- | --- | --- | --- |
| egovframework.com.sym.bat.validation.BatchOpertValidator | `batchOpertValidator` | `BatchOpert` | 배치작업에 지정한 배치프로그램이 실제 파일로 존재하는지, 파일이 맞는지, 접근 가능한지 검사 |
| egovframework.com.sym.sym.bak.validation.BackupOpertValidator | `backupOpertValidator` | `BackupOpert` | 백업 원본 디렉토리와 백업 대상 디렉토리가 실제로 존재하는지 검사 |
| egovframework.com.uss.umt.validation.PasswordManageMapValidator | `passwordManageMapValidator` | `PasswordManageVO` | 비밀번호 필수 입력·길이(8~20자)·연속문자·반복문자·3가지 조합 및 비밀번호 확인값 일치 검사 | -->

`BatchOpertValidator`와 `BackupOpertValidator`는 각각 `EgovBatchOpertController`, `EgovBackupOpertController`에서
주입받아 직접 호출한다. `PasswordManageMapValidator`는 빈으로 등록되어 있으므로 비밀번호 변경 화면 등
필요한 Controller에서 주입하여 사용한다.

```java
// egovframework.com.uss.umt.validation.PasswordManageMapValidator
@Component("passwordManageMapValidator")
public class PasswordManageMapValidator extends EgovCommonValidator implements Validator {

    @Override
    public boolean supports(@NonNull Class<?> clazz) {
        return PasswordManageVO.class.isAssignableFrom(clazz);
    }

    @Override
    public void validate(@NonNull Object target, @NonNull Errors errors) {
        PasswordManageVO passwordChgVO = (PasswordManageVO) target;
        String newPassword = passwordChgVO.getPassword();

        // 연속된 문자 검증 (EgovCommonValidator 제공)
        if (hasSeries(newPassword)) {
            errors.rejectValue("newPassword", "validation.password.series",
                    "연속된 3개 이상의 문자나 숫자를 사용할 수 없습니다.");
        }
    }
}
```

커스텀 Validator는 Controller에 주입한 뒤 `validate(대상, bindingResult)` 형태로 호출한다.

```java
// egovframework.com.sym.sym.bak.web.EgovBackupOpertController
@Resource(name = "backupOpertValidator")
private BackupOpertValidator backupOpertValidator;

// ...
backupOpertValidator.validate(backupOpert, bindingResult);
if (bindingResult.hasErrors()) {
    return "egovframework/com/sym/sym/bak/EgovBackupOpertRegist";
}
```

`EgovCommonValidator`는 커스텀 Validator에서 공통으로 사용할 수 있는 검사 메서드를 제공한다.

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `hasSeries(String password)` | `boolean` | 연속된 3개 이상의 문자나 숫자 포함 여부 |
| `hasRepeat(String password)` | `boolean` | 반복된 3개 이상의 문자나 숫자 포함 여부 |
| `hasComb3(String password)` | `boolean` | 영문자·숫자·특수문자 중 최소 3가지 조합 여부 |

### 검증 메시지 공통 처리

`egovframework.com.cmm.web.EgovValidationControllerAdvice`는 `@ControllerAdvice`로 선언된 공통 처리 클래스로,
`@InitBinder`를 통해 모든 Controller의 데이터 바인딩에 Jakarta Bean Validation을 수행하는 Validator를 등록한다.
검증 위반이 발생하면 어노테이션 종류를 판별하여 `message-validation_ko.properties`의 메시지로 변환한 뒤
`BindingResult`에 `validation.egov.error.필드명` 형태로 등록하므로, 화면에서는 `<form:errors>`로 그대로 출력하면 된다.

| 어노테이션 | 변환되는 메시지 키 |
| --- | --- |
| `@EgovNullCheck` | `validation.required` |
| `@EgovEmailCheck` | `validation.email.check` |
| `@EgovPwdCheck` | `validation.pwd.check` |
| `@EgovPhoneCheck` / `@EgovMobilePhoneCheck` | `validation.phone.check` / `validation.mobile.phone.check` |
| `@EgovRrnCheck` / `@EgovCnCheck` / `@EgovCrnCheck` | `validation.rrn.check` / `validation.cn.check` / `validation.crn.check` |
| `@EgovIPCheck` / `@EgovKoreanCheck` / `@EgovEnglishCheck` | `validation.ip.check` / `validation.korean.check` / `validation.english.check` |
| `@Size` | `validation.size.min` / `validation.size.max` (위반한 조건에 따라 선택) |

어노테이션에 `message` 속성을 직접 지정한 경우에는 해당 값이 우선 적용되며,
`message = "{validation.pattern.date}"`와 같이 `{키}` 형태로 작성하면 메시지 소스에서 조회한 값으로 치환된다.

### 화면에서 오류 메시지 출력

서버측 검증 결과는 Spring form 태그의 `<form:errors>`로 해당 입력항목 옆에 출력한다.

```jsp
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<form:form modelAttribute="httpMon" name="httpMon" method="post">
    <form:input path="siteUrl" size="100" maxlength="100"/>
    <form:errors path="siteUrl"/>
</form:form>
```

## 클라이언트측 검증

### EgovValidation.js

`EgovValidation.js`는 화면 제출 전 입력값을 확인하는 클라이언트사이드 검증 라이브러리로,
검증 규칙(`EgovValidation.rules`), 오류 메시지(`EgovValidation.messages`), 폼 검증 함수(`EgovValidation.validateForm`)로 구성된다.
`validateForm`은 오류 발생 시 메시지를 `alert`으로 표시하고 첫 번째 오류 항목에 포커스를 이동시킨 뒤 `false`를 반환한다.

주요 검증 규칙은 다음과 같다.

| 규칙 | 설명 |
| --- | --- |
| `required` | 필수 입력 |
| `maxlength` / `minlength` | 최대 / 최소 길이 |
| `integer` / `number` | 정수 / 숫자(소수점 포함) |
| `min` / `positive` | 최소값 / 양수 |
| `email` | 이메일 형식 |
| `telNo` / `urlFormat` | 연락처(숫자·하이픈) / URL 형식 |
| `english` / `englishWithSpace` / `alphanumeric` | 영문 / 영문+공백 / 영문·숫자·언더스코어 |
| `password1` ~ `password4` | 비밀번호 길이·특수문자·연속문자·반복문자 검사 |
| `pwdCheckComb3` / `pwdCheckComb4` | 비밀번호 3가지 / 4가지 문자 조합 검사 |
| `pwdCheckSeries` / `pwdCheckRepeat` | 비밀번호 연속 / 반복 문자 검사 |

### 화면별 검증 함수 작성

화면(폼)별 검증 함수는 `EgovValidation.js` 내에 `validate폼명(form)` 형태로 작성하며,
필드명별로 표시할 항목명(`label`)과 적용할 규칙(`rules`)을 선언한 뒤 `EgovValidation.validateForm()`에 전달한다.

```javascript
// 날짜(Date) 입력값에 대한 Validation 예시
function validateAnnvrsryManage(form) {
    const rules = {
        annvrsryDe: {
            label: '기념일자',
            rules: {
                required: true,
                maxlength: 10
            }
        }
    };
    return EgovValidation.validateForm(form, rules);
}
```

```javascript
// 숫자(Number) 입력값에 대한 Validation 예시
function validateIndvdlYrycManage(form, diffValueMessage) {
    const rules = {
        occrncYrycCo: {
            label: '발생연차개수',
            rules: {
                required: true,
                maxlength: 10,
                number: true,
                positive: true,
                min: 1
            }
        }
    };

    if (!EgovValidation.validateForm(form, rules)) {
        return false;
    }

    // 규칙으로 표현할 수 없는 필드 간 비교는 함수 내에서 직접 처리한다.
    if (parseFloat(form.occrncYrycCo.value) < parseFloat(form.useYrycCo.value)) {
        alert(diffValueMessage);
        return false;
    }
    return true;
}
```

### 화면(JSP)에 적용

JSP에 `EgovValidation.js`를 포함시키고, 저장 처리 함수에서 해당 검증 함수를 호출한 뒤 통과한 경우에만 폼을 전송한다.

```jsp
<script type="text/javascript" src="<c:url value="/js/egovframework/com/cmm/EgovValidation.js" />"></script>

<script type="text/javaScript" language="javascript">
function fn_egov_regist_HttpMon(form) {
    if (confirm("<spring:message code="common.save.msg" />")) {
        if (!validateHttpMon(form)) {
            return;
        } else {
            form.submit();
        }
    }
}
</script>

<form:form modelAttribute="httpMon" name="httpMon" method="post">
    ...
    <input class="s_submit" type="submit" value="저장"
           onclick="fn_egov_regist_HttpMon(document.httpMon); return false;" />
</form:form>
```

## 메시지 관리

검증 메시지는 `egovframework/message/com/message-validation_ko.properties`(영문은 `_en`)에 정의하며,
`context-common.xml`의 `messageSource` 설정(`classpath*:egovframework/message/com/**/*`)에 의해 자동으로 로딩된다.

```properties
validation.required = 필수입력항목입니다.
validation.size.max = {0}자 이상 입력할수 없습니다.
validation.pattern.integer = 숫자만 입력 가능합니다.
validation.pattern.date = 날짜 유형만 허용됩니다.
validation.password.series = 연속된 3개 이상의 문자나 숫자를 사용할 수 없습니다.
```

표준프레임워크 확장 어노테이션의 기본 메시지(`{validation.nullCheck}`, `{validation.emailCheck}` 등)는
실행환경 라이브러리(`egovframe-rte-ptl-reactive`)의 `messages/message-validation.properties`에 정의되어 있다.

## 4.x 이하 버전과의 차이

공통컴포넌트 5.0에서 유효성 검증 방식이 다음과 같이 변경되었다.

| 구분 | 4.x 이하 | 5.0 |
| --- | --- | --- |
| 서버측 검증 | Commons Validator XML(`egovframework/validator/**/*.xml`) | model 클래스의 Bean Validation 어노테이션 + `@Valid` |
| 검증 규칙 등록 | `context-validator.xml`에 XML 파일 등록 | 별도 등록 불필요 (어노테이션 선언만으로 적용) |
| 클라이언트측 검증 | Spring Modules `commons-validator` 태그 + `/validator.do` 동적 스크립트 | `EgovValidation.js`의 `validate*(form)` 함수 |
| 검증 API 패키지 | `javax.validation` | `jakarta.validation` |

기존 Commons Validator 기반 화면을 5.0으로 이관하는 경우, validator XML의 `field`/`depends` 정의를
model 클래스의 어노테이션과 `EgovValidation.js`의 검증 규칙으로 각각 옮겨 작성한다.

## 참고자료

- 실행환경 Bean Validation 참조:
    [Bean Validation (JSR-303)](../../egovframe-runtime/presentation-layer/web-servlet-declarative-validation.md)
- 실행환경 Validator 참조:
    [Spring의 Validator 인터페이스와 유효성 검증](../../egovframe-runtime/presentation-layer/web-servlet-validation.md)
