---
title: Cache Configuration
linkTitle: "Cache Config"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 Configuration Generation 기능에서 Cache 설정 항목을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-config-generation/vscode-config-generation-cache/
menu:
  depth:
    weight: 2
    parent: "vscode-config-generation"
    identifier: "vscode-config-generation-cache"
---
# Cache Configuration

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 Configuration Generation 기능 중 **Cache** 카테고리의 설정 유형을 안내한다.

Cache 카테고리는 다음 2가지 설정 유형을 제공한다.

| 설정 유형 | 설명 |
|---|---|
| New Cache | Ehcache 기반의 일반 캐시 설정 파일 생성 |
| New Ehcache Configuration | Spring CacheManager에 Ehcache를 등록하는 설정 파일 생성 |

공통 입력 항목(Generation Type, File Name, Package Name 등)은 [Common Configuration](./vscode-config-generation-common)을 참고한다.

---

## New Cache

Ehcache 기반의 일반 캐시 설정 파일을 생성한다. 기본 캐시(default cache) 설정과 하나의 명명된 캐시(named cache) 설정을 포함한다.

### 지원 형식

| 형식 | 기본 파일명 |
|---|---|
| XML | `ehcache` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| File Name | ✓ | 생성될 XML 파일명 (기본값: `ehcache`) |

#### Configuration

**Default Cache 설정**

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Disk Store | | 캐시 디스크 저장소 경로. 예) `java.io.tmpdir` |
| Default Max Elements | | 기본 캐시의 최대 저장 요소 수 |
| Default Eternal | | 기본 캐시의 영구 보존 여부 (`true` / `false`) |
| Default Idle Time | | 기본 캐시의 유휴 만료 시간 (초). `0`이면 만료 없음 |
| Default Live Time | | 기본 캐시의 최대 생존 시간 (초). `0`이면 만료 없음 |
| Default Overflow To Disk | | 기본 캐시가 최대 요소 수 초과 시 디스크 오버플로우 허용 여부 |
| Default Disk Persistent | | 기본 캐시의 디스크 영속성 여부 |
| Default Disk Expiry | | 기본 캐시의 디스크 만료 주기 (분) |

**Named Cache 설정**

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Cache Name | | 명명된 캐시 이름 |
| Max Elements | | 명명된 캐시의 최대 저장 요소 수 |
| Eternal | | 명명된 캐시의 영구 보존 여부 |
| Idle Time | | 명명된 캐시의 유휴 만료 시간 (초) |
| Live Time | | 명명된 캐시의 최대 생존 시간 (초) |
| Overflow To Disk | | 명명된 캐시의 디스크 오버플로우 여부 |
| Disk Persistent | | 명명된 캐시의 디스크 영속성 여부 |
| Memory Policy | | 캐시 메모리 정책 |

---

## New Ehcache Configuration

Spring 환경에서 `CacheManager`에 Ehcache 설정 파일 경로를 제공하는 설정 파일을 생성한다.

### 지원 형식

| 형식 | 기본 파일명 / 클래스명 |
|---|---|
| XML | `context-cache` |
| JavaConfig | `EgovCacheConfig` |

### 설정 항목

#### Default Settings

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Generation Type | ✓ | XML 또는 JavaConfig |
| File Name / Class Name | ✓ | 생성될 파일명 또는 클래스명 |
| Package Name | ✓ (JavaConfig) | Java 패키지명 (JavaConfig 선택 시 표시) |

#### Configuration

| 항목 | 필수 | 설명 |
|---|:---:|---|
| Config Location | | Ehcache 설정 파일 경로. 예) `classpath:ehcache.xml` |
| Component Scan Base Package | | Spring 컴포넌트 스캔 기본 패키지. 예) `egovframework.example` |
