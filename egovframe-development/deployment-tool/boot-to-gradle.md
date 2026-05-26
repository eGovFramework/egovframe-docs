---
title: 표준프레임워크 Boot Sample 프로젝트를 Gradle로 빌드환경 전환
linkTitle: 표준프레임워크 Boot Sample 프로젝트를 Gradle로 빌드환경 전환
description: "표준프레임워크 Boot Sample 프로젝트를 Gradle로 빌드환경 전환 방법을 설명한다."
url: /egovframe-development/deployment-tool/build-tool/gradle/boot-to-gradle/
menu:
  depth:
    weight: 3
    parent: "gradle"
---
## 표준프레임워크 Boot Sample 프로젝트를 Gradle로 빌드환경 전환

### 빌드 환경 전환

1. Eclipse Gradle Plugin 설치

   * Buildship : [설치가이드](./gradle-buildship.md)
   
2. Sample 프로젝트 생성

   * 개발환경 > eGovFrame > New Boot Web Project > [프로젝트 정보 입력-Next] > Generate Example 체크 [Finish] (또는)
   * 개발환경 > file > New > eGovframe Boot Web Project > [프로젝트 정보 입력-Next] > Generate Example 체크 [Finish]

     ![생성 프로젝트 선택](./images/boot-gradle-sample-1.png)

     ![프로젝트 정보 입력](./images/boot-gradle-sample-2.png)
     
     ![게시판 컨텐츠 자동생성 체크](./images/boot-gradle-sample-3.png)

     ![메이븐 프로젝트 속성 확인](./images/boot-gradle-sample-4.png)

3. build.gradle 파일 추가

   * [build.gradle](#buildgradle-파일)

     ![파일생성](./images/boot-gradle-sample-5.png)

     ![파일명입력](./images/boot-gradle-sample-6.png)

4. 기존 Maven Nature 삭제

   * Mavne > Disable Maven Nature

     ![Maven Nature 삭제](./images/boot-gradle-sample-7.png) 
     
     ![Compile 오류](./images/boot-gradle-sample-8.png)

5. Gradle Nature 추가

   * Configure > Add Gradle Nature

     ![Gradle Nature 추가](./images/boot-gradle-sample-9.png) 
     
     ![Compile 오류 정리](./images/boot-gradle-sample-10.png)

6. pom.xml 삭제

7. Gradle 설정 확인

   * Gradle > Refresh Gradle Project

     ![Task 재구성](./images/boot-gradle-sample-11.png)

8. Gradle Tasks View 열기

   * Window > Show View > Gradle > Gradle Tasks

     ![Gradle Tasks View](./images/boot-gradle-sample-12.png)

9. Gradle Tasks View에 표시된 프로젝트 Build

   * 프로젝트에 구성된 Task를 시작메뉴를 이용하여 빌드실행

     ![기본 Task 실행](./images/boot-gradle-sample-13.png)

     ![Task 실행결과](./images/boot-gradle-sample-14.png)
     
10. Gradle 프로젝트 실행

    * Run As > Spring Boot App

![Gradle 프로젝트 실행](./images/boot-gradle-sample-15.png)

### build.gradle 파일

```groovy
plugins {
    id 'java'
    id 'org.springframework.boot' version '3.5.6'
    id 'io.spring.dependency-management' version '1.1.7'
}

configurations {
    all {
        exclude group: 'org.springframework.boot', module: 'spring-boot-starter-logging'
    }
}

group = 'egovframe'
version = '1.0.0'
java.sourceCompatibility = JavaVersion.VERSION_17

repositories {
    mavenCentral()
    maven {
        url 'https://maven.egovframe.go.kr/maven'
    }
}

dependencyManagement {
    imports {
        mavenBom 'org.egovframe.boot:egovframe-boot-starter-parent:5.0.0'
    }
}

dependencies {
    implementation 'org.egovframe.rte:egovframe-rte-ptl-mvc'
    implementation 'org.egovframe.rte:egovframe-rte-psl-dataaccess'
    implementation 'org.egovframe.rte:egovframe-rte-fdl-idgnr'
    implementation 'org.egovframe.rte:egovframe-rte-fdl-property'
    implementation 'org.egovframe.rte:egovframe-rte-ptl-reactive'

    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
    implementation 'org.springframework.boot:spring-boot-starter-log4j2'
    implementation 'org.springframework.boot:spring-boot-starter-validation'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'

    implementation 'org.apache.commons:commons-dbcp2'
    implementation 'org.hsqldb:hsqldb'

    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'

    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'org.seleniumhq.selenium:selenium-java'
}

bootJar {
    exclude('org/projectlombok/lombok')
}

test {
    useJUnitPlatform()
}
```
