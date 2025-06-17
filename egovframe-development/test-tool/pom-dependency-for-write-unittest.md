---
title: "Unit Test 작성을 위한 pom.xml dependency 설정"
linkTitle: "Unit Test 작성을 위한 pom.xml dependency 설정"
description: "Unit Test 작성을 위한 pom.xml dependency 설정 방법을 코드로 보여준다."
url: /egovframe-development/test-tool/ref/pom-dependency-for-write-unittest
menu:
  depth:
    weight: 1
    parent: "ref"
---

## Unit Test 작성을 위한 pom.xml dependency 설정

```xml
	<dependencies>
       . . . 중략 . . .
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.4</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.easymock</groupId>
			<artifactId>easymock</artifactId>
			<version>2.4</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.easymock</groupId>
			<artifactId>easymockclassextension</artifactId>
			<version>2.4</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.dbunit</groupId>
			<artifactId>dbunit</artifactId>
			<version>2.4.3</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.unitils</groupId>
			<artifactId>unitils</artifactId>
			<version>2.2</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>1.5.6</version>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-nop</artifactId>
			<version>1.5.6</version>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
       . . . 중략 . . .
	</dependencies>

```
