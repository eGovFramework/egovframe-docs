# Markdown Frontmatter 작성방법

## 프론트매터(Frontmatter)란?

프론트매터는 문서 상단에 아래처럼 작성된 코드 부분을 말한다.

```go
---
title:
linkTitle:
description:
url:
menu:
    depth:
        name:
        weight:
        parent:
        identifier:
---
```

프론트매터는 문서의 제목, 속성 등의 메타데이터를 지정하기 위해 작성되는 코드를 말한다.
`---` 사이에 작성되며, Yaml 형식이 사용된다.

## 프론트매터(Frontmatter) 작성방법

### 형식

```go
title: "wiki의 제목"
linkTitle: "메뉴 등 링크에서 보여지는 이름"
description: "본문에 대한 요약"
url: "https://egovframework.github.io/egovframe-docs 이후부터 시작되는 url 경로"
menu:
    depth:
        name: "wiki의 제목"
        weight: "사이드 네비게이션에 동일한 depth(=동일한 parent를 가진 자식)에서 정렬하는 순번"
        parent: "부모 파일의 menu에 정의된 identifier 값"
        identifier: "현재 파일의 id(자식 파일이 있을 때 필요)"
```

- **title**
    - `title: "IoC Container Basics”`
    
    ![1.png](https://github.com/user-attachments/assets/78a0ba1f-1da9-420c-89bf-c87617c55942)
    
    - MD 파일의 전체적인 제목
    - 우측 사이드 페이지 네비게이션에 "이 페이지의 구성" 바로 아래에 표시됨
    
- **linkTitle**
    - `linkTitle: "Basics”`
    
    ![2.png](https://github.com/user-attachments/assets/1383cad9-7a74-4d13-8182-4f656a881b7f)
    
    - 좌측 사이드메뉴, 브레드크럼 등에서 사용
    - 링크 형식으로 사용되는 타이틀이므로 최대한 간략하게 작성

- **decription**
    
    `description: Spring IoC Container는 객체(빈) 관리, 의존성 주입, Bean의 초기화와 소멸 등을 제공하며, 다양한 스코프와 프로파일 설정을 지원한다. 또한, Spring은 XML 스키마 기반 AOP, AspectJ 어노테이션, 그리고 리소스를 활용한 메시지 제공 서비스 등을 통해 개발자의 생산성을 높인다.`
    
    ![3.png](https://github.com/user-attachments/assets/7d2a7831-6dd8-4f9e-9299-ab3312cd7c6b)

    
    - MD 파일에 대한 설명
    - "_index.md"의 내용이 비어 있고, 그 파일과 같은 디렉토리에 폴더(다른 md파일을 포함)가 있을 경우, 그 폴더 내 다른 md파일들의 description이 그 "_index.md"의 화면에서 표시된다.

- **url**
    - `url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-basics/”`
    
    ![4.png](https://github.com/user-attachments/assets/2748478b-687e-4efd-9cae-26c92ee9a478)
    
    - 브레드크럼에서 사용
    *브레드크럼의 경우 현재 위치는 표시되지 않음
    - 물리적인 파일 위치와 다름
        
        : 물리적인 파일 위치 : /egovframe-runtime/foundation-layer-core/ioc-container-basics
        
    - `https://egovframework.github.io/egovframe-docs` 이후부터 시작되는 url 경로로서, wiki의 depth 순서로 작성 필요
        
        ![기존 Wiki의 메뉴 구조](https://github.com/user-attachments/assets/acf900b7-62b6-411b-b99a-368e342f341a)

        
        기존 Wiki의 메뉴 구조
        
        - 공통기반핵심(foundation-layer-core) > IoC Container > Basics 순서로 url 작성

- **menu**
    - **depth** : menu-depth 까지 좌측 사이드메뉴의 그룹형태로 모든 frontmatter 동일
    - **name** : md의 이름
    - **weight** : parent의 몇 번째 자식인지 설정 → 좌측 사이드메뉴에 동일 depth에서 표시되는 순서
        - wiki에 기재되어있지 않은 파일을 추가하는 경우 weight은 마지막 파일의 weight+1로 지정할 것
    - **parent** : 참조하는 부모 파일이 있는 경우 기재 (부모 파일의 identifier와 동일하게 작성)
    - **identifier** : 하위(자식) md파일에서 참조할 수 있는 현재 파일의 id
        - 하위 파일이 있는 경우
            
            ```go
            ...
            url: "/egovframe-runtime/foundation-layer-core/ioc-container/"
            menu:
              depth:
                name: IoC Container
                weight: 1
                parent: "foundation-layer-core"
                identifier: "ioc-container"
            ```
            
            - **name** : IoC container
            - **weight** : parent인 foundation-layer-core의 1번째 파일
            - **parent** : 부모인 foundation-layer-core를 참조함
            - **identifier** : 이 파일의 id는 ioc-container
            
            - 상위 파일이 있는 경우
                
                ```go
                url: "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-bean_scope/"
                menu:
                    depth:
                        name: Bean Scopes
                        weight: 3
                        parent: "ioc-container"
                ```
                
                - **name** : Basics
                - **weight** : ioc-container의 3번째 파일
                    - 기존 wiki의 순서 확인
                    
                    ![6.png](https://github.com/user-attachments/assets/af08ff39-c8d9-47f2-9e3d-79992fba4a37)
                    
                - **parent** : 위의 ioc-container 파일에서 지정한 identifier의 이름을 지정해 부모-자식관계 형성

### 유의점

1. 내용에 “-” 등 특수문자 사용이 필요한 경우 내용 전체를 “”(큰따옴표)로 감싸서 사용
2. weight와 url 작성 시에는 기존 Wiki를 기준으로 작성
3. 작성 시 frontmatter의 key 값은 수정 X, value만 작성
