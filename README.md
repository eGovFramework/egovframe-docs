# 전자정부 표준프레임워크 가이드

- 본 GitHub 저장소 생성 목적은 표준프레임워크 포털에서 제공하고 있는 DokuWiki 가이드 문서를 간단하고 직관적인 Markdown 형식의 문서로 변환하여 기여받는 것입니다.
- 이 프로젝트의 목적은 쉽게 접근 가능한 Markdown 형식의 문서를 통해 사용자와 개발자들이 표준프레임워크를 더욱 편리하게 활용할 수 있도록 돕는 것입니다.
- 이 프로젝트의 특징은 기여자가 문서 및 이미지를 기여하면 그 즉시 자동으로 배포되어 웹사이트를 통해 결과를 확인할 수 있는 것입니다.
- 2025년 표준프레임워크 가이드 컨트리뷰션 범위는 개발환경, 실행환경, 실행환경 예제, 공통컴포넌트입니다(2024년도에는 실행환경 문서로 한정).

## 가이드 문서 보기

- https://egovframework.github.io/egovframe-docs/

## 프론트매터(Frontmatter) 작성 방법

[프론트매터 작성 방법](./how-to-write-Frontmatter.md)을 참고해 주시기 바랍니다.

## PR 방법

### 최초 준비

- Github의 [egovframe-docs 레포지토리](https://github.com/eGovFramework/egovframe-docs)를 Fork합니다.
- Fork하여 생성된 개인 레포지토리를 clone하여 로컬에 코드를 받아옵니다.
  - `git clone {Fork하여 생성된 개인 레포지토리의 URL}`
- upstream으로 egovframe-docs 레포지토리를 연결합니다.
  - `git remote add upstream https://github.com/eGovFramework/egovframe-docs.git`
  - 정상적이라면 `git remote -v`명령시 origin에는 개인 repository URL이, upstream에는 https://github.com/eGovFramework/egovframe-docs.git이 설정되어 있습니다.

### 작업 시작

- 작업 시작 전에 upstream인 egovframe-docs 레포지토리의 main 브랜치와 싱크를 맞춥니다.
  - `git fetch upstream main`
- 내 로컬의 메인 브랜치(main)로 체크아웃 합니다.
  - `git checkout main`
- upstream과 병합합니다(또는 리베이스).
  - 병합 : `git merge upstream/main`
  - 리베이스 : `git rebase upstream/main`
- 충돌이 발생한다면 해결합니다.
- (선택)내 origin에도 동기화를 해둡니다.
  - `git push origin main`
- 작업을 진행합니다.

### 작업 완료

- 변경사항을 스테이징한 후 커밋합니다.
  - `git add .`
  - `git commit -m "커밋 메시지 작성"`
- **push 하기 전에 upstream인 egovframe-docs 레포지토리의 main 브랜치와 다시 한 번 싱크를 맞춥니다(충돌 방지 및 자동 배포 목적).**
  - `git fetch upstream main`
- upstream과 병합합니다(또는 리베이스).
  - 병합 : `git merge upstream/main`
  - 리베이스 : `git rebase upstream/main`
- 충돌이 발생한다면 해결합니다.
  - 충돌난 파일을 열어서 수정
  - 수정된 파일을 스테이징 : `git add .` 또는 `git add {file}`
  - 병합(또는 리베이스) 완료
    - 병합 : `git commit` # 자동으로 머지 커밋 메시지가 설정됨
    - 리베이스 : `git rebase --continue`
  - 병합(또는 리베이스)을 원복하려면
    - 병합 취소(원복) : `git merge --abort`
    - 리베이스 취소(원복) : `git rebase --abort`
- 내 origin에 push 합니다.
  - `git push origin main`

### PR 생성

- Github에서 내 개인 레포지토리(egovframe-docs를 포크한 레포지토리) 페이지로 이동합니다.
- “Compare & pull request” 버튼을 클릭합니다.
- 제목과 설명 입력 후 “Create pull request” 버튼을 클릭합니다.

### 결과 확인

#### PR 자동 Merge 성공시

- 작성자가 남긴 PR이 자동으로 Merge가 성공했다면,[egovframe-docs의 PR탭](https://github.com/eGovFramework/egovframe-docs/pulls)에서 본인이 남긴 PR이 closed 처리됩니다.
- 그 후 자동으로 빌드 및 배포과정이 진행됩니다. 이 과정은 [egovframe-docs의 Actions탭](https://github.com/eGovFramework/egovframe-docs/actions)에서 확인 가능합니다.
- 잠시 후 본인의 PR에 대한 배포가 완료되면, [egovframe-docs 사이트](https://egovframework.github.io/egovframe-docs/)에서 작업 결과를 확인하실 수 있습니다.

#### PR 자동 Merge 실패시

- 작성자가 남긴 PR이 자동으로 Merge가 실패했다면,[egovframe-docs의 PR탭](https://github.com/eGovFramework/egovframe-docs/pulls)에서 본인이 남긴 PR이 여전히 open 상태로 남아 있습니다.
- 다시 위 "작업 완료" 부분에 `git fetch upstream main`부터 실행하여 `git push origin main`까지를 완료합니다.
- 그러면 추가적인 PR을 작성하지 않더라도, 본인이 이전에 남긴 PR에서 자동으로 새로운 commit이 추가되고, 다시 자동 Merge 과정을 거칩니다.
- 자동으로 Merge 성공시, 위 "PR 자동 Merge 성공시"에 서술된 프로세스가 진행됩니다.

## 디렉토리 구조

- 현재 개발가이드와 유사하게 구성되어 있습니다.

  - [공통컴포넌트 가이드-개요](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.3:init)
  - [공통컴포넌트 가이드-상세](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.3:init_guide)
  - [개발환경 개발가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:dev4.3)
    - [실행환경 개발가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte4.3)
  - [실행환경 예제 개발가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte:ex:개발프레임워크_실행환경_예제)
- 문서 파일과 관련 리소스는 다음과 같은 디렉토리 구조를 따릅니다.
- 모든 _index.md 파일과 아래 코드블럭에서 표시된 MD파일은 identifier 값을 갖고 있습니다(egovframe-runtime 제외). 프론트매터의 url, parent 등을 작성할 때 아래 디렉토리 구조를 참고 부탁드립니다.

```
/common-component                 #공통컴포넌트
  /collaboration                    #협업
    /address.md                       #주소록/명함록
    /board.md                         #게시판
    /community.md                     #커뮤니티
    /edsm.md                          #전자결재
    /schedule.md                      #일정관리
    /sms.md                           #문자메세지
  /digital-asset-management         #디지털 자산관리
    /knowledge-map.md                  #지식맵
  /elementary-technology            #요소기술
    /calendar.md                      #달력
    /cookie-session.md                #쿠키/세션
    /external-components.md           #외부 추가 컴포넌트
    /formatter-util.md                #포맷/계산/변환
    /interface.md                     #인터페이스/화면
    /message-process.md               #메시지 처리
    /new-components-v3.2.md           #신규 컴포넌트(v3.2)
    /print.md                         #인쇄/출력
    /system.md                        #시스템
    /webeditor.md                    #웹에디터
  /intro                            #개요
  /security                         #보안
    /authority-management.md          #권한관리
  /statistics-reporting             #통계/리포팅
  /system-management                #시스템관리
    /batch-manage.md                  #배치관리
    /common-code-manage.md            #공통코드관리
    /error-manage.md                  #장애관리
    /log-manage.md                    #로그관리
    /menu-manage.md                   #메뉴관리
    /program-manage.md                #프로그램관리
    /system-manage.md                 #시스템관리
  /system-service-linkage           #시스템/서비스연계
  /user-authentication              #사용자디렉토리/통합인증
    /login.md                         #일반 로그인
  /user-support                     #사용자지원
    /information-provided.md          #정보제공/알림
    /member-manage.md                 #사용자관리
    /online-help.md                   #온라인헬프
    /online-practice.md               #온라인참여
    /personalization.md               #개인화
    /terms-manage.md                  #약관관리

/egovframe-development            #개발환경
  /configuration-management-tool    #형상 관리 도구
    /change-management.md             #Change Management
    /configuration-management.md      #Configuration Management
  /deployment-tool                  #배포 도구
    /build-tool.md                    #Build Tool
      /docker.md                        #컨테이너 가상화(Docker) 빌드
      /gradle.md                        #개인빌드(Gradle)
      /maven.md                         #개인빌드(Maven)
  /development-etcdevtool-guide     #활용 가이드
  /implementation-tool              #구현 도구
    /editor.md                        #Editor
    /batch-IDE.md                      #Batch IDE
    /code-generation.md                #Code Genetation
    /code-inspection.md                #Code Inspection
    /dbio-editor.md                    #DBIO Editor
    /server-connection-management.md   #Server Connection Management
    /uml-editor.md                     #UML Editor
    /debug.md                         #Debug
  /individual-install-guide          #구성 가이드
  /install-guide                    #설치 가이드
  /intro                            #소개
  /operation-guide                  #운영 가이드
  /test-tool                        #테스트 도구
    /test-automation.md               #Test Automation
    /unit-test.md                     #Unit Test

/egovframe-runtime                #실행환경
  /batch-layer                      #배치처리
  /business-logic-layer             #업무처리
  /foundation-layer-core            #공통기반 핵심
  /foundation-layer                 #공통기반
  /integration-layer                #연계통합
  /intro                            #실행환경 소개
  /persistence-layer                #데이터처리
  /presentation-layer               #화면처리

/runtime-example                  #실행환경 예제
  /individual-example               #실행환경 개별 예제
    /batch-layer                      #배치처리 예제
    /business-logic-layer             #업무처리 예제
    /foundation-layer                 #공통기반 예제
    /foundation-layer-core            #공통기반 핵심 예제
    /integration-layer                #연계통합 예제
      /cloud-data-stream.md             #Cloud Data Stream
    /persistence-layer                #데이터처리 예제
    /presentation-layer               #화면처리 예제
/integrated-example                 #실행환경 통합 예제
```

## 문서 구조

- 각 문서는 다음과 같은 구조와 템플릿을 따릅니다.

```
# [문서 제목]

## 개요
문서의 목적과 주요 내용을 간략히 설명합니다.

## 주요 개념
### [개념 1]
개념 1에 대한 설명을 제공합니다.

### [개념 2]
개념 2에 대한 설명을 제공합니다.

## 관련 문서
- [문서 제목 1](링크)
- [문서 제목 2](링크)

## 설명
문서의 주요 내용을 상세히 설명합니다. 필요 시 하위 섹션을 추가하여 내용을 체계적으로 나눕니다.

### IoC Container of Spring Framework
#### BeanFactory
BeanFactory 인터페이스와 관련된 내용을 설명합니다.

#### ApplicationContext
ApplicationContext 인터페이스와 관련된 내용을 설명합니다.

## 참고자료
- [참고자료 1](링크)
- [참고자료 2](링크)
```

- 헤더
  - 문서의 제목과 섹션 제목은 각각 `#`와 `##`, `###`로 구분합니다.
- 개요
  - 문서의 목적, 중요성, 다룰 내용을 간략히 소개합니다.
- 주요 개념
  - 문서에서 다룰 주요 개념을 상세히 설명합니다.
- 관련문서
  - 관련된 외부 문서나 추가 자료의 링크를 제공합니다.
- 설명
  - 문서의 핵심 내용을 구체적으로 설명합니다.
  - 필요에 따라 하위 섹션으로 나눕니다.
- 참고자료
  - 문서 작성 시 참조한 자료나 독자가 추가로 참고할 수 있는 자료의 링크를 제공합니다.

## 문서 작성 규칙

- 파일명은 설명하는 내용을 간결하게 나타내도록 하며, 소문자와 하이픈(-)을 사용합니다.
  - 예) `ioc-container.md`
- 이미지 파일은 작성하는 폴더의 하위에 위치한 'images' 폴더에 저장하고, 문서에서 `![이미지 설명](이미지 파일 경로)` 형식을 사용합니다.
  - 예) `![IoC Container 구조](./images/ioc-container-structure.png)`
- 코드 예시는 삼중 백틱 `(```언어명```)` 으로 감싸서 표시합니다.

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

- 외부 링크는 절대 경로를 사용하고, 내부 링크는 상대 경로를 사용합니다.
  - 예) `[Spring Framework Documentation](https://docs.spring.io/spring-framework/docs/5.3.27/reference/html)`

## 문장 구성 스타일 가이드

- 문체
  - 일관된 공식 문체를 사용하며, 기술 용어는 첫 사용 시 정의합니다.
  - 문장은 격식을 유지하고, 신뢰감을 줄 수 있도록 작성합니다.
  - 문장은 명확하고 간결하게 작성합니다. 복잡한 개념은 짧은 문장으로 나누어 설명하며, 가능한 한 간단하게 표현합니다.
  - 일관된 용어와 표현을 사용하며, 문서 전체에서 동일한 어휘와 문체를 유지합니다.
- 어조
  - 주관적인 의견을 피하고, 사실에 근거한 정보를 제공하며, 명확하고 중립적인 어조를 유지합니다.
  - 내용을 잘 이해할 수 있도록 교육적이고 안내하는 어조를 사용합니다.
- 예시
  - "Inversion of Control(역제어)은 객체의 생성 및 생명주기 관리를 개발자가 아닌 컨테이너가 담당하는 것을 의미한다."
  - "Spring Framework의 IoC Container는 다양한 기능을 제공하며, 이를 통해 애플리케이션의 유연성과 확장성을 향상시킬 수 있다."
  - "의존성 주입(Dependency Injection)은 빈 설정 정보를 바탕으로 컨테이너가 클래스 간의 의존 관계를 자동으로 연결해주는 방법이다."

## 예제 및 참고자료

### 샘플 문서

- [표준프레임워크 실행환경 소개](https://github.com/eGovFramework/egovframe-docs/blob/main/egovframe-runtime/intro/overview.md)
- [IoC Container](https://github.com/eGovFramework/egovframe-docs/blob/main/egovframe-runtime/foundation-layer-core/ioc-container.md)

### 참고자료

- [Markdown 기본 문법](https://www.markdownguide.org/basic-syntax/)
- [Markdown 고급 문법](https://www.markdownguide.org/extended-syntax/)
