---
title: "설치법"
linkTitle: "설치법"
description: "실행환경 통합예제 설치법"
url: /runtime-example/integrated-example/intro/installation/
menu:
  depth:
    name: "설치법"
    weight: 2
    parent: "integrated-example-intro"
---



# 설치법

## 설치 순서

- 기본순서

 전자정부 표준프레임워크 홈페이지에서 소스파일을 다운 받아 압축을 풀고, m2 이클립스가 설치되어 있다는 가정하에 설명한다.

```bash
1. Package Explorer에서 오른쪽 마우스를 클릭하여 소스를 임포트한다.
```

 ![image](./images/개요-사용자_지정_3.jpg)

```bash
2. General > Existing Project into Workspace를 선택하여 압축을 풀어놓은 폴더를 선택한다.
```

 ![image](./images/개요-사용자_지정_4.jpg)

```bash
3. 임포드 된 소스에서 DB정보를 알맞게 바꿔준다. 위치:src/main/resources/egovframework/property/globals.properties
```

 ![image](./images/개요-사용자_지정_2.jpg)

```bash
4. script 폴더의 script, data 파일을 참고하여 테이블을 생성한다.
```

 ![image](./images/개요-db.jpg)

```bash
5. 프로젝트를 실행시킨다. (오른쪽마우스 클릭 > Run As > Run On Server)
```

 ![image](./images/개요-사용자_지정_15.jpg)

```bash
6. 설치된 톰캣 버전을 선택하고 next 또는 finish를 클릭하여 프로젝트를 실행한다.
```

 ![image](./images/개요-사용자_지정_16.jpg)

## 오류 발생 시 대처 순서

 기본 순서 절차처럼 실행시 오류가 날 경우 대처 순서를 설명한다.

```bash
1. Maven의 설정을 초기화 한다.(Maven > Update Project Configration)
```

 ![image](./images/개요-사용자_지정_18.jpg)

```bash
2. Dependency 파일을 다시한번 인스톨 한다. (Run As > Maven Install)
```

 ![image](./images/개요-사용자_지정_23.jpg)

```bash
3. 콘솔 창의 Build Success를 확인한다.
```

 ![image](./images/개요-사용자_지정_24.jpg)

```bash
4. maven을 초기화 할 경우, .classpath파일이 자동으로 변경되는 경우가 있다.
```

 ![image](./images/개요-사용자_지정_21.jpg)

```bash
5.  .classpath를 살펴보고 아래와 같이 변경한다.
```

 ![image](./images/개요-사용자_지정_22.jpg)