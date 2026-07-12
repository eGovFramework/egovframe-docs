---
title: "Facebook 연동"
linkTitle: "Facebook 연동"
description: "Facebook 연동"
url: /common-component/user-support/information-provided/facebook-integration/
menu:
  depth:
    name: "Facebook 연동"
    weight: 32
    parent: "information-provided"
---

# Facebook 연동

## 개요

Facebook 연동은 Facebook 로그인(사인인) 후 프로필, 피드, 앨범 정보를 조회하는 외부 서비스 연동 기능이다. Spring Social 기반 Controller와 JSP로 구성되며, 사용을 위해 Facebook 개발자 앱 등록(앱 ID·시크릿 발급)이 필요하다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 사용자지원(정보제공/알림) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.uss.ion.fbk.web.EgovFacebookController.java | EgovFacebookController Class |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/fbk/EgovFacebookAlbum.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/fbk/EgovFacebookAlbums.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/fbk/EgovFacebookFeed.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/fbk/EgovFacebookProfile.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/uss/ion/fbk/EgovFacebookSignin.jsp |  |

### 주요 메서드 (EgovFacebookController (RequestMapping))

| URL | 메서드 | 설명 |
| --- | --- | --- |
| `/uss/ion/fbk/EgovFacebookSignin.do` (GET) | `home` | Facebook 사인인 화면 |
| `/uss/ion/fbk/feed.do` (GET/POST) | `showFeed` | 피드 조회/작성 |
| `/uss/ion/fbk/albums.do` (GET) | `showAlbums` | 앨범 목록 조회 |
| `/uss/ion/fbk/album/{albumId}` (GET) | `showAlbum` | 앨범 상세 조회 |
| `/uss/ion/fbk/profile.do` (GET) | `profile` | 프로필 조회 |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
