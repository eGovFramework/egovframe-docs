---
title: "Twitter연동"
linkTitle: "Twitter연동"
description: "Twitter연동"
url: /common-component/user-support/information-provided/twitter-integration/
menu:
  depth:
    name: "Twitter연동"
    weight: 19
    parent: "information-provided"
---

# Twitter연동

## 개요

Twitter(X) 연동은 OAuth 인증을 거쳐 X(구 Twitter) 계정 정보 조회와 게시물(포스트) 작성·조회를 제공하는 외부 서비스 연동 기능이다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있으며, 사용을 위해 X 개발자 앱 등록(클라이언트 키 발급)이 필요하다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.tir.web.EgovTwitterController.java | EgovTwitterController Class |
| Controller | egovframework.com.uss.ion.tir.web.EgovXAuthController.java | EgovXAuthController Class |
| Controller | egovframework.com.uss.ion.tir.web.EgovXController.java | EgovXController Class |
| Service | egovframework.com.uss.ion.tir.service.EgovXOAuthService.java | Service Interface |
| Service | egovframework.com.uss.ion.tir.service.EgovXService.java | Service Interface |
| ServiceImpl | egovframework.com.uss.ion.tir.service.EgovXServiceImpl.java |  |
| Class | egovframework.com.uss.ion.tir.service.EgovXClient.java |  |
| DAO | egovframework.com.uss.ion.tir.service.impl.EgovTwitterDao.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/tir/EgovTwitterMain.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/tir/EgovTwitterPopup.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/tir/EgovXAuthCallback.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/tir/EgovXV2Demo.jsp |  |
| Query XML | resources/egovframework/mapper/com/uss/ion/tir/EgovTwitter_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovXOAuthService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getAuthorizationUrl(HttpSession, String, String)` | `String` | Twitter(X) OAuth 2.0 + PKCE 인증 URL 생성 및 토큰 발급을 처리하는 서비스. / |
| `requestAccessToken(HttpSession, String, String)` | `String` | OAuth 인가 코드와 state를 이용해 액세스 토큰을 발급받는다. 세션에 임시 저장된 OAuth 컨텍스트는 사용 후 즉시 제거한다. |
| `extractAccessToken(String)` | `private String` | 토큰 응답 JSON 문자열에서 access_token 값을 추출한다. |

### 주요 메서드 (EgovXService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getAccount(String)` | `String` | Twitter(X) API 호출 기능을 제공하는 서비스 인터페이스. / public interface EgovXService { / 액세스 토큰으로 내 계정 정보 |
| `writeTweet(String, String)` | `String` | 트윗을 등록한다. |
| `deleteTweet(String, String)` | `String` | 트윗 ID로 트윗을 삭제한다. |
| `getLatestTweets(String, String)` | `String` | 사용자 ID 기준 최근 트윗 목록을 조회한다. |
| `getNextTweets(String, String, String)` | `String` | pagination token 기준 다음 트윗 목록을 조회한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
