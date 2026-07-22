# 비밀번호 찾기

## 비즈니스 규칙

 일반 회원, 기업 회원, 업무담당자 세 개의 사용자 구분에 따라 아이디, 이름, 이메일, 비밀번호 힌트, 비밀번호 정답 정보를 갖고 임시 비밀번호를 메일발송 처리할 수 있다.

## 관련코드

### jsp

```html
1. 사용자 업무구분
<tr>
  <td><input name="rdoSlctUsr" type=radio value=radio checked onClick="fnCheckUsrId('GNR');">일반</td>
  <td><input name="rdoSlctUsr" type=radio value=radio unchecked onClick="fnCheckUsrId('ENT');">기업</td>
  <td><input name="rdoSlctUsr" type=radio value=radio unchecked onClick="fnCheckUsrId('USR');">업무</td>
</tr>
 
2. 비밀번호 힌트 공통코드를 조회하여 콤보박스 형태로 선택
<select name="passwordHint">
  <option selected value=''>--선택하세요--</option>
  <c:forEach var="result" items="${pwhtCdList}" varStatus="status">
  <option value='<c:out value="${result.code}"/>'><c:out value="${result.codeNm}"/></option>
  </c:forEach>
</select>
```text

### controller

```java
1. 비밀번호 힌트 공통코드 조회
ComDefaultCodeVO vo = new ComDefaultCodeVO();
vo.setCodeId("COM022");
List code = cmmUseService.selectCmmCodeDetail(vo);
model.addAttribute("pwhtCdList", code);
 
2. 비밀번호 찾기
boolean result = loginService.searchPassword(loginVO);
```text

 컨트롤러 클래스에서 비밀번호 힌트 공통코드 목록을 조회하여 화면에 보여준다.
 입력받은 아이디, 이름, 이메일, 비밀번호 힌트, 비밀번호 정답 정보를 갖고 임시 비밀번호를 메일 발송한다.

### service

```java
1. 아이디, 이름, 이메일주소, 비밀번호 힌트, 비밀번호 정답이 DB와 일치하는 사용자 Password를 조회한다.
LoginVO loginVO = loginDAO.searchPassword(vo);
 
2. 임시 비밀번호를 생성한다.(영+영+숫+영+영+숫=6자리)
String newpassword = "";
for (int i = 1; i <= 6; i++) {
	// 영자
	if (i % 3 != 0) {
		newpassword += EgovStringUtil.getRandomStr('a', 'z');
	// 숫자
	} else {
		newpassword += EgovNumberUtil.getRandomNum(0, 9);
	}
}
 
3. 임시 비밀번호를 암호화하여 DB에 저장한다.
LoginVO pwVO = new LoginVO();
String enpassword = EgovFileScrty.encryptPassword(newpassword);
pwVO.setId(vo.getId());
pwVO.setPassword(enpassword);
pwVO.setUserSe(vo.getUserSe());
loginDAO.updatePassword(pwVO);
 
4. 임시 비밀번호를 이메일 발송한다.
SndngMailVO sndngMailVO = new SndngMailVO();
sndngMailVO.setDsptchPerson("webmaster");
sndngMailVO.setRecptnPerson(vo.getEmail());
sndngMailVO.setSj("[MOPAS] 임시 비밀번호를 발송했습니다.");
sndngMailVO.setEmailCn("고객님의 임시 비밀번호는 " + newpassword + " 입니다.");
sndngMailVO.setAtchFileId("");
```

 서비스 구현 클래스에서 입력받은 아이디, 이름, 이메일, 비밀번호 힌트, 비밀번호 정답 정보를 갖고 사용자 정보를 조회한다.
 영어, 숫자 혼용 6자리 임시 비밀번호를 생성하여 암호화한 뒤, 데이터베이스에 비밀번호를 수정한다.
 임시 비밀번호를 요소기술 중 발송요청메일 등록 기능을 사용하여 전송한다.
 비밀번호 이메일 발송은 전자우편연계 기능을 참조한다.

## 관련화면 및 수행매뉴얼

### 2. 비밀번호 찾기

| Action | URL | Controller method | QueryID |
| --- | --- | --- | --- |
| 비밀번호조회 | /uat/uia/searchPassword.do | searchPassword | loginDAO.searchPassword |
| 비밀번호힌트조회 | /uat/uia/egovIdPasswordSearch.do | idPasswordSearchView |  |

 아이디, 이름, 이메일, 비밀번호 힌트, 비밀번호 정답 정보를 갖고 사용자 정보를 조회하고 임시 비밀번호를 메일 발송한다.

 ![image](./images/uat-findpw-idpwfind1.jpg)
 업무구분 선택: 사용자 업무구분을 선택한다.
 아이디 입력: 아이디를 입력한다.
 이름 입력: 이름을 입력한다.
 이메일 입력: 이메일을 입력한다.
 비밀번호힌트 선택: 회원가입시 등록한 비밀번호 힌트를 선택한다.
 비밀번호정답 입력: 비밀번호힌트에 대한 정답을 입력한다.
 비밀번호 찾기: 업무구분, 아이디, 이름, 이메일, 비밀번호 힌트, 비밀번호 정답을 통해 사용자 임시 비밀번호를 생성하고 메일 발송한다.
