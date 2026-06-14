---
title: Crypto
linkTitle: "Crypto"
description: Encryption/Decryption과 crypto 간소화를 crypto라는 목록에 넣기 위해 생성
url: /egovframe-runtime/foundation-layer/crypto/
menu:
    depth:
        name: Crypto
        weight: 12
        parent: "foundation-layer"
        identifier: "crypto"
---

## 개요

표준프레임워크 실행환경의 Foundation Layer에서 제공하는 암호화(Crypto) 서비스에 대해 설명한다.

시스템 내에서 처리되는 민감한 정보(비밀번호, 개인정보 등)를 안전하게 보호하기 위해, 단방향 해시(Hash) 알고리즘과
양방향 대칭키/비대칭키 암호화(Encryption/Decryption) 알고리즘을 간편하게 적용할 수 있는 유틸리티 및 빈(Bean) 구조를 제공한다.

## 주요 제공 방식

* **ARIACryptoService**: 행정안전부 표준 암호 알고리즘인 ARIA를 손쉽게 사용할 수 있도록 추상화된 서비스
* **Spring Security Crypto 연동**: Spring Security에서 제공하는 강력한 비밀번호 해시 엔진(Bcrypt 등)과의 호환
* **설정 간소화**: XML이나 Java Config 기반으로 키(Key) 관리와 알고리즘 선택을 최소한의 설정으로 구현할 수 있도록 지원한다.
