# Security Service

## 개요

인증, 권한 같은 일반적인(통상적인) 개념의 Security 서비스는 Spring Security를 활용한 공통기반 레이어에서 제공한다.
화면 처리 레이어의 Security 서비스는 입력값 유효성 검증 기능을 제공한다.
입력값 유효성 검증(validation)을 위한 기능은 Valang, Jakarta Commons, Spring 등에서 제공하는데, 여기서는 기반 오픈소스로 Jakarta Commons Validator를 선택했다.
MVC 프레임워크인 Spring MVC와 Jakarta Commons Validator의 연계와 활용방안 설명한다.

## 설명

Jakarta Commons Validator는 필수값, 각종 primitive type(int,long,float…), 최대-최소길이, 이메일, 신용카드번호등의 값 체크등을 할 수 있도록 Template이 제공된다.
또한 client-side, server-side의 검증을 함께 할 수 있으며,
Configuration과 에러메시지를 client-side, server-side 별로 따로 하지 않고 한곳에 같이 쓰는 관리상의 장점이 있다.
자세한 설명은 아래의 문서를 참조하라.

- [Spring Framework에서 Commons Validator 사용](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.9:ptl:security:jakarta_commons_validator) : 입력값을 Jakarta Commons Validator를 이용하여 client-side, server-side 검증(validation)함.
- [Commons Validator에 validation rule 추가](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.9:ptl:validation:add_rules_in_commons_validator) : Commons Validator에 주민등록번호 validation rule을 추가해본다.

## 참고자료


