---
title: 전자정부 표준프레임워크 가이드
---

<br>
<br>
<br>

# 전자정부 표준프레임워크 가이드
- 본 GitHub 저장소는 표준프레임워크 포털에서 제공하고 있는 DokuWiki 가이드 문서를 간단하고 직관적인 Markdown 문서로 변환하여 기여받기 위해 생성되었습니다. 
- 이 프로젝트의 목적은 보다 쉽게 접근할 수 있는 문서 형식을 통해 사용자와 개발자들이 표준프레임워크를 더욱 효과적으로 활용할 수 있도록 돕는 것입니다.
- 표준프레임워크 가이드 컨트리뷰션 범위는 실행환경 문서로 한정하여 시작하려 합니다. 
## 문서 구조
### 파일 구조
- 문서 파일과 관련 리소스는 다음과 같은 디렉토리 구조를 따릅니다.
- 현재 개발가이드와 유사하게 구성되어 있습니다.
	- https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte4.2  참조
```
/egovframe-runtime
  /batch-layer #배치처리
    /images
  /business-logic-layer #업무처리
    /images
  /foundation-layer-core #공통기반 핵심
    - ioc-container.md
    - ioc-container-basics.md
    - ioc-container-dependencies.md
    - ioc-container-bean-scope.md
    - customizing-the-nature-of-a-bean.md
    - ...
    - aop.md
    - aop-aspectj.md
    - aop-xmlschema.md
    - ...
    /images
  /foundation-layer #공통기반
    /images
  /integration-layer #연계통합
    /images
  /persistence-layer #데이터처리
    /images
  /presentation-layer #화면처리
    /images
```
### 문서 구조
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
	- 예) `![IoC Container 구조](images/ioc-container-structure.png)`
- 코드 예시는 삼중 백틱 ` (```언어명```) ` 으로 감싸서 표시합니다.
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

