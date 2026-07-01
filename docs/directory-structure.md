# 

## 공통컴포넌트 디렉토리 구조

```
/common-component                           공통컴포넌트
├── /intro                                     개요
│   ├── /getting-started.md                        공통컴포넌트 시작하기
│   ├── /environment-setup.md                      공통컴포넌트 환경설정
│   ├── /deployment-structure.md                   공통컴포넌트 배포 파일의 구성
│   ├── /table-structure.md                        공통컴포넌트 테이블 구성 정보
│   └── /package-reference.md                      패키지 간 참조 관계
├── /user-authentication                       사용자디렉토리/통합인증
│   ├── /login.md                                  일반 로그인
│   │   └── /sso-service.md                            SSO 연계 서비스
│   ├── /certificate-login.md                      인증서 로그인
│   └── /login-policy-management.md                로그인정책관리
├── /security                                  보안
│   ├── /authority-management.md                   권한관리
│   │   ├── /authority-management-function.md          권한관리 기능
│   │   └── /authority-role-management.md              권한별 롤관리
│   ├── /authority-group-management.md             권한그룹관리
│   ├── /group-management.md                       그룹관리
│   ├── /role-management.md                        롤관리
│   ├── /department-role-management.md             부서권한관리
│   ├── /encrypt_decrypt.md                        암호화/복호화
│   ├── /login_session_management.md               로그인 시간관리
│   └── /pw_expiration_management.md               비밀번호 만료기간 관리
├── /statistics-reporting                      통계/리포팅
│   ├── /post-statistics.md                        게시물 통계
│   ├── /user-statistics.md                        사용자 통계
│   ├── /connection-statistics.md                  접속 통계
│   ├── /screen-statistics.md                      화면 통계
│   ├── /report-statistics.md                      보고서 통계
│   └── /data-use-statistics.md                    자료이용현황 통계
├── /collaboration                             협업
│   ├── /board.md                                  게시판
│   │   ├── /blog-management.md                        블로그관리
│   │   ├── /board-management.md                       게시판관리
│   │   ├── /board-guestbook.md                        게시판(방명록)
│   │   ├── /board-integrated.md                       게시판(통합게시판)
│   │   ├── /template-management.md                    템플릿관리
│   │   ├── /comment-management.md                     댓글관리
│   │   ├── /scrap-management.md                       스크랩관리
│   │   └── /satisfaction-survey.md                    만족도조사
│   ├── /community.md                              커뮤니티
│   │   ├── /community-creation.md                     커뮤니티생성관리
│   │   ├── /community-use.md                          커뮤니티사용관리
│   │   └── /community-member.md                       커뮤니티회원관리
│   ├── /sms.md                                    문자메시지
│   │   └── /sms-service.md                            문자메시지서비스
│   ├── /schedule-manage.md                        일정관리
│   │   ├── /department-schedule.md                    부서일정관리
│   │   ├── /schedule-management.md                    일정관리
│   │   ├── /journal-management.md                     일지관리
│   │   ├── /all-schedule.md                           전체일정
│   │   ├── /executive-schedule.md                     간부일정관리
│   │   ├── /department-task-box.md                    부서업무함관리
│   │   ├── /weekly-monthly-report.md                  주간/월간보고관리
│   │   ├── /memo-todo.md                              메모할일관리
│   │   └── /memo-report.md                            메모보고
│   ├── /email.md                                  전자우편
│   │   └── /mail-solution-interface.md                메일솔루션 연동 인터페이스
│   ├── /address.md                                주소록/명함록
│   │   ├── /business-card-management.md               명함관리
│   │   └── /address-book.md                           주소록관리
│   └── /edsm.md                                   전자결재
│       └── /brief-approval.md                         약식결재
├── /user-support                              사용자지원
│   ├── /user-manage.md                            사용자관리
│   │   ├── /company-member-management.md              기업 회원 관리
│   │   ├── /user-management.md                        사용자 관리
│   │   └── /member-management.md                      회원 관리
│   ├── /personalization.md                        개인화
│   │   └── /mypage.md                                 마이페이지
│   ├── /terms-manage.md                           약관관리
│   │   ├── /terms-management.md                       약관관리
│   │   ├── /copyright-policy.md                       저작권보호정책
│   │   └── /privacy-policy.md                         개인정보보호정책확인
│   ├── /online-help.md                            온라인헬프
│   │   ├── /help.md                                   도움말
│   │   ├── /glossary.md                               용어사전
│   │   ├── /faq-management.md                         FAQ관리
│   │   ├── /qna-management.md                         Q&A관리
│   │   ├── /admin-terminology.md                      행정전문용어사전관리
│   │   └── /online-manual.md                          온라인매뉴얼
│   ├── /online-participate.md                     온라인참여
│   │   ├── /counseling-management.md                  상담관리
│   │   ├── /survey-management.md                      설문관리
│   │   ├── /survey.md                                 설문조사
│   │   ├── /survey-template.md                        설문템플릿관리
│   │   ├── /survey-respondent.md                      설문응답자관리
│   │   ├── /survey-question.md                        설문질문관리
│   │   ├── /survey-item.md                            설문항목관리
│   │   ├── /meeting-management.md                     회의관리
│   │   └── /online-poll.md                            온라인POLL관리
│   └── /information-provided.md                   정보제공/알림
│       ├── /news-management.md                        뉴스관리
│       ├── /site-management.md                        사이트관리
│       ├── /sitemap.md                                사이트맵
│       ├── /recommended-site.md                       추천사이트관리
│       ├── /event-campaign.md                         행사/이벤트/캠페인
│       ├── /popup-management.md                       팝업창관리
│       ├── /info-notifier.md                          정보알림이
│       ├── /banner-management.md                      배너관리
│       ├── /login-image.md                            로그인화면이미지관리
│       ├── /recent-keyword.md                         최근검색어조회
│       ├── /main-image.md                             메인이미지관리
│       ├── /integrated-link.md                        통합링크관리
│       ├── /user-absence.md                           사용자부재관리
│       ├── /internet-service-guide.md                 인터넷서비스안내및관리
│       ├── /meeting-room.md                           회의실관리
│       ├── /meeting-room-reservation.md               회의실예약관리
│       ├── /wiki.md                                   Wiki기능
│       ├── /rss-tag.md                                RSS태그관리
│       ├── /twitter-integration.md                    Twitter연동
│       ├── /message-management.md                     쪽지관리
│       ├── /received-message.md                       받은쪽지함관리
│       ├── /sent-message.md                           보낸쪽지함관리
│       ├── /staff-event.md                            직원경조사관리
│       ├── /vacation-management.md                    휴가관리
│       ├── /duty-management.md                        당직관리
│       ├── /award-management.md                       포상관리
│       ├── /anniversary.md                            기념일관리
│       ├── /event-application.md                      행사신청관리
│       ├── /event-reception.md                        행사접수관리
│       ├── /map-management.md                         약도관리
│       ├── /personal-annual-leave.md                  개인연차관리
│       └── /facebook-integration.md                   Facebook 연동
├── /system-management                         시스템관리
│   ├── /common-code-manage.md                     공통코드관리
│   │   ├── /common-class-code.md                      공통분류코드
│   │   ├── /common-detail-code.md                     공통상세코드
│   │   ├── /common-code.md                            공통코드
│   │   ├── /zipcode-management.md                     우편번호관리
│   │   ├── /admin-code-management.md                  행정코드관리
│   │   ├── /org-code-receive.md                       기관코드수신
│   │   ├── /org-code.md                               기관코드
│   │   ├── /legal-dong-code.md                        법정동코드
│   │   └── /road-name-address.md                      도로명주소연계
│   ├── /log-manage.md                             로그관리
│   │   ├── /log-management.md                         로그관리
│   │   ├── /use-log-management.md                     사용로그관리
│   │   ├── /send-receive-log-management.md            송/수신 로그관리
│   │   ├── /system-history-management.md              시스템 이력관리
│   │   ├── /web-log-management.md                     웹로그관리
│   │   ├── /access-log-management.md                  접속로그관리
│   │   └── /privacy-log-management.md                 개인정보조회로그관리
│   ├── /menu-manage.md                            메뉴관리
│   │   ├── /menu-management.md                        메뉴관리
│   │   ├── /menu-creation.md                          메뉴생성관리
│   │   └── /shortcut-menu.md                          바로가기메뉴관리
│   ├── /program-manage.md                         프로그램관리
│   │   └── /program-management.md                     프로그램관리
│   ├── /batch-manage.md                           배치관리
│   │   ├── /batch-job-management.md                   배치작업관리
│   │   ├── /batch-result-management.md                배치결과관리
│   │   └── /schedule-processing.md                    스케줄처리
│   ├── /system-manage.md                          시스템관리
│   │   ├── /backup-management.md                      백업관리
│   │   ├── /network-management.md                     네트워크관리
│   │   └── /server-info-management.md                 서버정보관리
│   └── /error-manage.md                           장애관리
│       ├── /error-application.md                      장애신청관리
│       └── /error-result.md                           장애처리결과관리
├── /system-service-linkage                    시스템/서비스연계
│   ├── /system-linkage-manage.md                  시스템연계관리
│   ├── /linkage-status-manage.md                  연계현황관리
│   ├── /linkage-message-manage.md                 연계메시지관리
│   └── /linkage-org-manage.md                     연계기관관리
├── /digital-asset-management                  디지털 자산관리
│   ├── /personal-knowledge-manage.md              개인지식관리
│   ├── /knowledge-map.md                          지식맵
│   │   ├── /org-knowledge-map-management.md           지식맵관리(조직)
│   │   ├── /type-knowledge-map-management.md          지식맵관리(유형)
│   │   └── /knowledge-info-provision.md               지식정보제공
│   ├── /knowledge-expert-manage.md                지식전문가관리
│   ├── /knowledge-info-manage.md                  지식정보관리
│   └── /knowledge-evaluation-manage.md            지식평가관리
└── /elementary-technology                     요소기술
    ├── /new-components-v3.2.md                    신규 컴포넌트(v3.2)
    │   ├── /doublesubmit.md                           이중등록(Double Submit) 방지
    │   ├── /httprequesthelper.md                      Http Request 정보 취득
    │   ├── /numberformat.md                           숫자 지역화 처리
    │   ├── /dateformat.md                             날짜 지역화 처리
    │   ├── /showmodaldialog.md                        showModalDialog 대체 기능
    │   ├── /urlrewrite.md                             HTTPS UrlRewrite filter
    │   ├── /multilogin.md                             중복 로그인 방지 기능
    │   ├── /cmtmanage.md                              출퇴근 관리
    │   ├── /resourceclose.md                          Resource close 처리
    │   └── /basiclog.md                               Basic 로그
    ├── /external-components.md                    외부 추가 컴포넌트
    │   ├── /easybatch.md                              EasyBatch(v3.2 신규)
    │   ├── /social_login_naver_google_kakao.md        Social Login(Naver, Google, KAKAO)
    │   ├── /ldap.md                                   LDAP조직도관리(v3.2 신규)
    │   └── /websocket_messenger.md                    웹소켓메신저(v3.2 신규)
    ├── /message-process.md                        메시지 처리
    │   ├── /warning_message.md                        경고메시지
    │   ├── /error_message.md                          에러메시지
    │   ├── /info_message.md                           정보메시지
    │   └── /confirm_message.md                        확인메시지
    ├── /print.md                                  인쇄/출력
    │   ├── /print_scrin.md                            화면인쇄
    │   ├── /print_status.md                           프린터상태확인
    │   └── /print_digital_seal.md                     전자관인출력
    ├── /cookie-session.md                         쿠키/세션
    │   ├── /handling_session.md                       세션처리
    │   └── /handling_cookie.md                        쿠키처리
    ├── /calendar.md                               달력
    │   └── /holiday-management.md                     공휴일관리(달력)
    ├── /interface.md                              인터페이스/화면
    │   ├── /main-menu.md                              메인메뉴
    │   └── /tree-menu.md                              트리메뉴
    ├── /webeditor.md                              웹에디터
    │   ├── /webeditor_20.md                           웹에디터(공통컴포넌트 2.0 매뉴얼 참조)
    │   └── /wysiwygEditorV3_2.md                      WYSIWYG Editor(v3.2 신규)
    ├── /formatter-util.md                         포맷/계산/변환
    │   ├── /date-time-day-calculation.md              날짜/시간/요일 계산
    │   ├── /date-time-day-conversion.md               날짜/시간/요일 변환
    │   ├── /date-time-day-validation.md               날짜/시간/요일 유효성체크
    │   ├── /date-time-day-format.md                   날짜/시간/요일 포맷변경
    │   ├── /random-date.md                            랜덤날짜구하기
    │   ├── /random-string.md                          랜덤문자열구하기
    │   ├── /random-number.md                          랜덤숫자구하기
    │   ├── /string-search.md                          문자열검색
    │   ├── /string-conversion.md                      문자열변환
    │   ├── /string-validation.md                      문자열유효성체크
    │   ├── /string-replacement.md                     문자열치환
    │   ├── /id-number-validation.md                   번호유효성체크
    │   ├── /unit-calculation.md                       단위계산
    │   ├── /number-search.md                          숫자검색
    │   ├── /number-conversion.md                      숫자변환
    │   ├── /number-validation.md                      숫자유효성체크
    │   ├── /number-replacement.md                     숫자치환
    │   ├── /format-validation.md                      포멧유효성체크
    │   ├── /real-int-negative-check.md                실수/정수/음수체크
    │   ├── /solar-lunar-conversion.md                 양력/음력변환
    │   ├── /encoding-decoding.md                      인코딩/디코딩
    │   ├── /special-string-processing.md              특수문자열처리
    │   ├── /exchange-rate-calculation.md              환율계산
    │   └── /timestamp-value.md                        TIMESTAMP값구하기
    └── /system.md                                 시스템
        ├── /network-status-check.md                   네트워크상태체크
        ├── /network-info-check.md                     네트워크정보확인
        ├── /directory-watch.md                        디렉토리감시
        ├── /directory-permission-check.md             디렉토리권한체크
        ├── /directory-copy.md                         디렉토리복사
        ├── /directory-delete.md                       디렉토리삭제
        ├── /directory-create.md                       디렉토리생성
        ├── /directory-attribute-check.md              디렉토리속성정보체크
        ├── /directory-compress-extract.md             디렉토리 압축/해제
        ├── /directory-move.md                         디렉토리이동
        ├── /send-receive-monitoring.md                송수신모니터링
        ├── /db-service-monitoring.md                  DB서비스모니터링
        ├── /log-pattern-check.md                      로그패턴검사
        ├── /directory-date-check.md                   디렉토리일자체크
        ├── /directory-exist-check.md                  디렉토리존재체크
        ├── /disk-attribute-check.md                   디스크속성정보체크
        ├── /disk-capacity-check.md                    디스크유효용량체크
        ├── /disk-exist-check.md                       디스크존재체크
        ├── /server-info-check.md                      서버정보확인
        ├── /system-info-check.md                      시스템정보확인
        ├── /valid-memory-check.md                     유효메모리체크
        ├── /client-info-check.md                      클라이언트정보확인
        ├── /file-permission-check.md                  파일권한체크
        ├── /process-monitoring.md                     프로세스모니터링
        ├── /network-service-monitoring.md             네트워크서비스모니터링
        ├── /file-system-monitoring.md                 파일시스템모니터링
        ├── /file-download.md                          파일다운로드
        ├── /file-conversion.md                        파일변환
        ├── /file-security.md                          파일보안
        ├── /file-copy.md                              파일복사
        ├── /file-compare.md                           파일비교
        ├── /file-delete.md                            파일삭제
        ├── /file-create.md                            파일생성
        ├── /file-attribute-check.md                   파일속성정보체크
        ├── /file-send-receive.md                      파일송/수신
        ├── /file-compress-extract.md                  파일압축/해제
        ├── /proxy-service.md                          프록시서비스
        ├── /file-sync.md                              파일동기화
        ├── /login-session-check.md                    로그인세션정보체크
        ├── /file-upload.md                            파일업로드
        ├── /file-move.md                              파일이동
        ├── /file-date-check.md                        파일일자체크
        ├── /file-exist-check.md                       파일존재체크
        ├── /file-parsing.md                           파일파싱
        ├── /process-id-check.md                       프로세스ID확인
        ├── /property.md                               프로퍼티
        ├── /xml-data-assembly.md                      XML 데이터조립
        ├── /xml-data-parsing.md                       XML 데이터파싱
        ├── /server-resource-monitoring.md             서버자원모니터링
        ├── /web-standard-check.md                     웹표준검사
        └── /http-service-monitoring.md                HTTP서비스모니터링
```