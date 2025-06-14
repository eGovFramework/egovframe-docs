---
title: "공통컴포넌트 테이블 구성 정보"
linkTitle: "테이블 구성"
description: "공통컴포넌트의 데이터베이스 테이블 구조에 대해 설명합니다."
url: /common-component/common-intro/table-structure/
menu:
  depth:
    name: "공통컴포넌트 테이블 구성 정보"
    weight: 4
    parent: "common-intro"
    identifier: "table-structure"
---

# 공통컴포넌트 테이블 구성 정보

## 개요

공통컴포넌트를 적용 시 공통컴포넌트의 종류별 특징을 고려하여 현장 상황에 맞게 적용할 수 있도록 관련 정보를 제공한다.

- 공통기술의 데이터 엔터티 및 어트리뷰트는 공통기술 웹 어플리케이션이 구동되기 위한 최소한의 필수 항목들로 구성되어 있으며, 공통컴포넌트를 이용하여 개발하는 각 기관에서 기관의 업무환경 및 시스템 구성에 맞도록 구체화하여 사용하여야 한다.(관련ERD 참조)
- 요소기술은 Util과 같이 타 어플리케이션 개발 시 참조하여 기능이 재구현되어야 하는 패키지이고, 공통기술은 각 배포단위별로 웹 어플리케이션을 실행 가능한 패키지로 구성되어 있다.
- 요소기술은 관련 데이터 엔터티가 존재하지 않으며, 공통기술은 관련 데이터 엔터티가 존재한다.

## 테이블 목록

| NO | 구분 | 테이블ID | 테이블명 |
|----|------|----------|----------|
| 1 | - | COMTECOPSEQ | Sequence 저장테이블 |
| 2 | - | IDS | 테이블별 아이디생성 |
| 3 | 사용자디렉토리/통합인증 | COMTNGNRLMBER | 일반회원 |
| 4 | 사용자디렉토리/통합인증 | COMTNORGNZTINFO | 조직정보 |
| 5 | 사용자디렉토리/통합인증 | COMTNEMPLYRINFO | 업무사용자정보 |
| 6 | 사용자디렉토리/통합인증 | COMTNENTRPRSMBER | 기업회원 |
| 7 | 사용자디렉토리/통합인증 | COMVNUSERMASTER | 사용자정보뷰 |
| 8 | 사용자디렉토리/통합인증 | COMTNLOGINPOLICY | 로그인정책 |
| 9 | 사용자디렉토리/통합인증 | COMTNEMPLYRSCRTYESTBS | 사용자보안설정 |
| 10 | 사용자디렉토리/통합인증 | COMTNMENUINFO | 메뉴정보 |
| 11 | 사용자디렉토리/통합인증 | COMTHEMPLYRINFOCHANGEDTLS | 업무사용자정보변경내역 |
| 12 | 보안관리 | COMTNAUTHORGROUPINFO | 권한그룹정보 |
| 13 | 보안관리 | COMTNAUTHORINFO | 권한정보 |
| 14 | 보안관리 | COMTNROLES_HIERARCHY | 롤 계층구조 |
| 15 | 보안관리 | COMTNROLEINFO | 롤정보 |
| 16 | 보안관리 | COMTNAUTHORROLERELATE | 권한롤관계 |
| 17 | 협업 | COMTNBLOG | 블로그게시판 |
| 18 | 협업 | COMTNBLOGUSER | 블로그사용자 |
| 19 | 협업 | COMTHEMAILDSPTCHMANAGE | 메일발신관리 |
| 20 | 협업 | COMTNTMPLATINFO | 템플릿 |
| 21 | 협업 | COMTNBBSMASTER | 게시판마스터 |
| 22 | 협업 | COMTNBBS | 게시판 |
| 23 | 협업 | COMTNBBSUSE | 게시판활용 |
| 24 | 협업 | COMTNCMMNTY | 커뮤니티 속성 |
| 25 | 협업 | COMTNCLUB | 동호회속성 |
| 26 | 협업 | COMTNBBSMASTEROPTN | 게시판마스터옵션 |
| 27 | 협업 | COMTNCOMMENT | 댓글 |
| 28 | 협업 | COMTNSCRAP | 스크랩 |
| 29 | 협업 | COMTNSTSFDG | 만족도 |
| 30 | 협업 | COMTHCONFMHISTORY | 승인이력 |
| 31 | 협업 | COMTNCMMNTYUSER | 커뮤니티사용자 |
| 32 | 협업 | COMTNCLUBUSER | 동호회사용자 |
| 33 | 협업 | COMTNSMS | 문자메시지 |
| 34 | 협업 | COMTNSMSRECPTN | 문자메시지수신 |
| 35 | 협업 | COMTNMTGINFO | 회의정보 |
| 36 | 협업 | COMTNSCHDULINFO | 일정정보 |
| 37 | 협업 | COMTNDIARYINFO | 일지정보 |
| 38 | 협업 | COMTNLEADERSTTUS | 간부상태 |
| 39 | 협업 | COMTNLEADERSCHDUL | 간부일정 |
| 40 | 협업 | COMTNLEADERSCHDULDE | 간부일정일자 |
| 41 | 협업 | COMTNDEPTJOB | 부서업무 |
| 42 | 협업 | COMTNDEPTJOBBX | 부서업무함 |
| 43 | 협업 | COMTNWIKMNTHNGREPRT | 주간/월간보고 |
| 44 | 협업 | COMTNMEMOTODO | 메모할일 |
| 45 | 협업 | COMTNMEMOREPRT | 메모보고 |
| 46 | 협업 | COMTNNCRD | 명함정보속성 |
| 47 | 협업 | COMTNNCRDUSER | 명함사용자속성 |
| 48 | 협업 | COMTNADBKMANAGE | 주소록관리 |
| 49 | 협업 | COMTNADBK | 주소록 |
| 50 | 사용자지원 | COMTNFILE | 파일속성 |
| 51 | 사용자지원 | COMTNFILEDETAIL | 파일상세정보 |
| 52 | 사용자지원 | COMTNSITEMAP | 사이트맵 |
| 53 | 사용자지원 | COMTNINFRMLSANCTN | 약식결재 |
| 54 | 사용자지원 | COMTNSTPLATINFO | 약관정보 |
| 55 | 사용자지원 | COMTNINDVDLPGECNTNTS | 마이페이지 컨텐츠 |
| 56 | 사용자지원 | COMTNINDVDLPGEESTBS | 마이페이지 설정 |
| 57 | 사용자지원 | COMTNCNTNTSLIST | 컨텐츠목록 |
| 58 | 사용자지원 | COMTNCPYRHTINFO | 저작권정보 |
| 59 | 사용자지원 | COMTNINDVDLINFOPOLICY | 개인정보정책확인 |
| 60 | 사용자지원 | COMTNHPCMINFO | 도움말정보 |
| 61 | 사용자지원 | COMTNWORDDICARYINFO | 용어사전정보 |
| 62 | 사용자지원 | COMTNFAQINFO | FAQ정보 |
| 63 | 사용자지원 | COMTNQAINFO | QA정보 |
| 64 | 사용자지원 | COMTNADMINISTRATIONWORD | 행정용어사전관리 |
| 65 | 사용자지원 | COMTNONLINEMANUAL | 온라인메뉴얼 |
| 66 | 사용자지원 | COMTNCNSLTLIST | 상담내역 |
| 67 | 사용자지원 | COMTNQUSTNRTMPLAT | 설문템플릿 |
| 68 | 사용자지원 | COMTNQESTNRINFO | 설문지정보 |
| 69 | 사용자지원 | COMTNQUSTNRRESPONDINFO | 설문응답자정보 |
| 70 | 사용자지원 | COMTNQUSTNRQESITM | 설문문항 |
| 71 | 사용자지원 | COMTNQUSTNRRSPNSRESULT | 설문응답결과 |
| 72 | 사용자지원 | COMTNQUSTNRIEM | 설문항목 |
| 73 | 사용자지원 | COMTNONLINEPOLLMANAGE | 온라인POLL관리 |
| 74 | 사용자지원 | COMTNONLINEPOLLIEM | 온라인POLL항목 |
| 75 | 사용자지원 | COMTNONLINEPOLLRESULT | 온라인POLL결과 |
| 76 | 사용자지원 | COMTNNEWSINFO | 뉴스정보 |
| 77 | 사용자지원 | COMTNSITELIST | 사이트목록 |
| 78 | 사용자지원 | COMTNRECOMENDSITEINFO | 추천사이트정보 |
| 79 | 사용자지원 | COMTNEVENTINFO | 행사/이벤트정보 |
| 80 | 사용자지원 | COMTNEXTRLHRINFO | 외부인사정보 |
| 81 | 사용자지원 | COMTNPOPUPMANAGE | 팝업 정보 관리 |
| 82 | 사용자지원 | COMTNNTFCINFO | 정보알림 |
| 83 | 사용자지원 | COMTNBANNER | 배너 |
| 84 | 사용자지원 | COMTNLOGINSCRINIMAGE | 로그인화면이미지 |
| 85 | 사용자지원 | COMTNRECENTSRCHWRDMANAGE | 최근검색어관리 |
| 86 | 사용자지원 | COMTNRECENTSRCHWRD | 최근검색어 |
| 87 | 사용자지원 | COMTNMAINIMAGE | 메인이미지 |
| 88 | 사용자지원 | COMTNUNITYLINK | 통합링크 |
| 89 | 사용자지원 | COMTNUSERABSNCE | 사용자부재 |
| 90 | 사용자지원 | COMTNINTNETSVC | 인터넷서비스 |
| 91 | 사용자지원 | COMTNTWITTER | 트위터인증키관리 |
| 92 | 사용자지원 | COMTNWIKIBKMK | Wiki북마크 |
| 93 | 사용자지원 | COMTNRSS | RSS태그관리 |
| 94 | 사용자지원 | COMTNNOTE | 쪽지관리 |
| 95 | 사용자지원 | COMTNNOTETRNSMIT | 쪽지송신 |
| 96 | 사용자지원 | COMTNNOTERECPTN | 쪽지수신 |
| 97 | 사용자지원 | COMTNMTGPLACEMANAGE | 회의실관리 |
| 98 | 사용자지원 | COMTNFXTRSMANAGE | 비품관리 |
| 99 | 사용자지원 | COMTNMTGPLACEFXTRS | 회의실비품 |
| 100 | 사용자지원 | COMTNMTGPLACERESVE | 회의실예약 |
| 101 | 사용자지원 | COMTNCTSNNMANAGE | 경조관리 |
| 102 | 사용자지원 | COMTNVCATNMANAGE | 휴가관리 |
| 103 | 사용자지원 | COMTNBNDTDIARY | 당직관리 |
| 104 | 사용자지원 | COMTNBNDTMANAGE | 당직관리정보 |
| 105 | 사용자지원 | COMTNBNDTCECKMANAGE | 당직체크관리정보 |
| 106 | 사용자지원 | COMTNINDVDLYRYCMANAGE | 개인별연차관리 |
| 107 | 사용자지원 | COMTNRWARDMANAGE | 포상관리 |
| 108 | 사용자지원 | COMTNANNVRSRYMANAGE | 기념일관리 |
| 109 | 사용자지원 | COMTNEVENTMANAGE | 행사관리 |
| 110 | 사용자지원 | COMTNEVENTATDRN | 행사참석자 |
| 111 | 사용자지원 | COMTNCOMMUTE | 출퇴근관리 |
| 112 | 사용자지원 | COMTNROUGHMAP | 약도관리 |
| 113 | 통계/리포팅 | COMTSBBSSUMMARY | 게시물통계요약 |
| 114 | 통계/리포팅 | COMTSUSERSUMMARY | 사용자통계요약 |
| 115 | 통계/리포팅 | COMTNREPRTSTATS | 보고서통계 |
| 116 | 통계/리포팅 | COMTNDTAUSESTATS | 자료이용현황통계 |
| 117 | 통계/리포팅 | COMTNNTTSTATS | 게시물통계 |
| 118 | 디지털자산관리 | COMTNDAMMAPTEAM | 지식맵(조직유형) |
| 119 | 디지털자산관리 | COMTNDAMKNOIFM | 지식정보 |
| 120 | 디지털자산관리 | COMTNDAMMAPKNO | 지식맵(지식유형) |
| 121 | 디지털자산관리 | COMTNDAMPRO | 지식전문가 |
| 122 | 디지털자산관리 | COMTNDAMCALRES | 지식정보제공/지식정보요청 |
| 123 | 시스템/서비스연계 | COMTNCNTCINSTT | 연계기관 |
| 124 | 시스템/서비스연계 | COMTNCNTCSERVICE | 연계서비스 |
| 125 | 시스템/서비스연계 | COMTNCNTCSYSTEM | 연계시스템 |
| 126 | 시스템/서비스연계 | COMTNSYSTEMCNTC | 시스템연계 |
| 127 | 시스템/서비스연계 | COMTNCNTCMESSAGE | 연계메시지 |
| 128 | 시스템/서비스연계 | COMTNCNTCMESSAGEITEM | 연계메시지항목 |
| 129 | 시스템관리 | COMTCCMMNCLCODE | 공통분류코드 |
| 130 | 시스템관리 | COMTCCMMNCODE | 공통코드 |
| 131 | 시스템관리 | COMTCCMMNDETAILCODE | 공통상세코드 |
| 132 | 시스템관리 | COMTNLOGINLOG | 접속로그 |
| 133 | 시스템관리 | COMTSSYSLOGSUMMARY | 시스템로그요약 |
| 134 | 시스템관리 | COMTSWEBLOGSUMMARY | 웹로그 요약 |
| 135 | 시스템관리 | COMTNPROGRMLIST | 프로그램목록 |
| 136 | 시스템관리 | COMTHPROGRMCHANGEDTLS | 프로그램변경내역 |
| 137 | 시스템관리 | COMTNMENUCREATDTLS | 메뉴생성내역 |
| 138 | 시스템관리 | COMTCZIP | 우편번호 |
| 139 | 시스템관리 | COMTRDNMADRZIP | 도로명주소 |
| 140 | 시스템관리 | COMTCADMINISTCODE | 행정코드 |
| 141 | 시스템관리 | COMTCADMINISTCODERECPTNLOG | 행정코드수신로그 |
| 142 | 시스템관리 | COMTNINSTTCODE | 기관코드 |
| 143 | 시스템관리 | COMTNINSTTCODERECPTNLOG | 기관코드수신로그 |
| 144 | 시스템관리 | COMTNSYSLOG | 시스템로그 |
| 145 | 시스템관리 | COMTNUSERLOG | 사용자로그 |
| 146 | 시스템관리 | COMTNTRSMRCVLOG | 송수신로그 |
| 147 | 시스템관리 | COMTSTRSMRCVLOGSUMMARY | 송수신로그요약 |
| 148 | 시스템관리 | COMTHSYSHIST | 시스템이력 |
| 149 | 시스템관리 | COMTNWEBLOG | 웹로그 |
| 150 | 시스템관리 | COMTNBKMKMENUMANAGERESULT | 바로가기 메뉴 등록 |
| 151 | 시스템관리 | COMTNBATCHOPERT | 배치작업 |
| 152 | 시스템관리 | COMTNBATCHRESULT | 배치결과 |
| 153 | 시스템관리 | COMTNBATCHSCHDUL | 배치스케줄 |
| 154 | 시스템관리 | COMTNBATCHSCHDULDFK | 배치스케줄요일 |
| 155 | 시스템관리 | COMTNBACKUPRESULT | 백업결과 |
| 156 | 시스템관리 | COMTNBACKUPOPERT | 백업작업 |
| 157 | 시스템관리 | COMTNBACKUPSCHDULDFK | 백업스케줄요일 |
| 158 | 시스템관리 | COMTNNTWRKINFO | 네트워크정보 |
| 159 | 시스템관리 | COMTNSERVEREQPMNINFO | 서버장비정보 |
| 160 | 시스템관리 | COMTNSERVERINFO | 서버정보 |
| 161 | 시스템관리 | COMTNSERVEREQPMNRELATE | 서버장비관계 |
| 162 | 시스템관리 | COMTNTROBLINFO | 장애 정보 |
| 163 | 시스템관리 | COMTNPRIVACYLOG | 개인정보조회 로그 |
| 164 | 요소기술 | COMTNRESTDE | 휴일관리 |
| 165 | 요소기술 | COMTNTRSMRCVMNTRNG | 송수신모니터링 |
| 166 | 요소기술 | COMTHTRSMRCVMNTRNGLOGINFO | 송수신모니터링로그정보 |
| 167 | 요소기술 | COMTNSYNCHRNSERVERINFO | 동기화 서버 정보 |
| 168 | 요소기술 | COMTNDBMNTRNG | DB서비스모니터링 |
| 169 | 요소기술 | COMTHDBMNTRNGLOGINFO | DB서비스모니터링로그정보 |
| 170 | 요소기술 | COMTNHTTPMON | HTTP모니터링 |
| 171 | 요소기술 | COMTHHTTPMONLOGINFO | HTTP서비스모니터링로그정보 |
| 172 | 요소기술 | COMTNPROCESSMON | 프로세스모니터링 |
| 173 | 요소기술 | COMTNPROCESSMONLOGINFO | 프로세스모니터링로그정보 |
| 174 | 요소기술 | COMTNNTWRKSVCMNTRNG | 네트워크서비스 모니터링 |
| 175 | 요소기술 | COMTNNTWRKSVCMNTRNGLOGINFO | 네트워크서비스모니터링로그정보 |
| 176 | 요소기술 | COMTNFILESYSMNTRNG | 파일시스템 모니터링 |
| 177 | 요소기술 | COMTNFILESYSMNTRNGLOGINFO | 파일시스템모니터링로그정보 |
| 178 | 요소기술 | COMTNPROXYINFO | 프록시정보 |
| 179 | 요소기술 | COMTNPROXYLOGINFO | 프록시 로그 정보 |
| 180 | 요소기술 | COMTNSERVERRESRCELOGINFO | 서버 자원 로그 정보 |
| 181 | 요소기술 | J_ATTACHFILE | Jfile업로드 |
| 182 | 요소기술 | IMGTEMP | 전자관인 이미지 |


## 테이블/초기데이터 생성 스크립트

공통컴포넌트는 배포파일을 통해 테이블/초기데이터 생성 스크립트를 제공하므로 전체 테이블/초기데이터 생성 스크립트는 공통컴포넌트의 all-in-one 파일을 통해 얻을 수 있다.

하지만, 전체 테이블/초기데이터에 대한 생성 스크립트만 필요한 경우를 위해 아래의 링크를 통해 제공하니 필요시 참조한다. 스크립트는 Altibase, Cubrid, Maria, MySQL, Oracle, Postgres, Tibero 및 Goldilocks 여덟 개의 DBMS에 해당하는 스크립트가 제공되며, Tibero는 Oracle의 테이블 생성 스크립트와 동일하다. 스크립트 파일은 기본적으로 **UTF-8**로 인코딩 되어있다.

다음 스크립트들을 직접 다운로드할 수 있습니다:

- [**전체 테이블 생성 스크립트 4.3.0**](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v4.3:ddl_dml_script_v4.3.0.zip)
- [**전체 코멘트(주석) 생성 스크립트 4.3.0**](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v4.3:comment_script_v4.3.0.zip)

> **※ 데이터베이스 성능 개선을 위하여 Index 추가 생성 및 query tuning 과 같은 작업을 각 프로젝트에 맞도록 시행해야 한다.**

### 초기 데이터 사용자 정보

제공되는 초기 데이터에는 테스트용 사용자 정보가 포함되어 있다.(**대소문자** 유의)

| 구분 | ID | PW | 비고 |
|------|----|----|------|
| 업무사용자 | TEST1 | rhdxhd12 | 영문으로 공통12 |
| | webmaster | rhdxhd12 | 영문으로 공통12 |
| 일반사용자 | USER | rhdxhd12 | 영문으로 공통12 |
| 기업사용자 | ENTERPRISE | rhdxhd12 | 영문으로 공통12 |