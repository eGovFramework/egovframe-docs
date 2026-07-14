---
title: 구현 도구(VS Code)
linkTitle: 구현 도구(VS Code)
description: "Visual Studio Code 표준프레임워크 구현도구"
url: /egovframe-development/vscode-implementation-tool/
menu:
  depth:
    weight: 4
    parent: "egovframe-development"
    identifier: "vscode-implementation-tool"
---

# 구현 도구(VS Code)

## 개요

구현 도구(VS Code)는 VS Code 환경에서 표준프레임워크 기반 개발을 지원하는 eGovFrame Initializr 확장 기능을 제공한다. 프로젝트 생성, CRUD 코드 생성, 설정 파일 생성을 지원한다.

## 주요 개념

VS Code Extension은 Eclipse 기반 구현 도구를 설치하지 않고도 표준프레임워크 프로젝트를 생성하고, 템플릿 기반으로 CRUD 코드와 각종 설정(Configuration)을 생성할 수 있게 한다.

## 관련 문서

### 시작하기

- [eGovFrame Initializr Settings](./vscode-egov-settings.md) — 확장 기능 설정
- [Project Generation](./vscode-project-generation.md) — 프로젝트 생성

### Code Generation

- [CRUD Code Generation](./vscode-code-generation.md) — 코드 생성 개요
- [Generate CRUD Code](./vscode-code-generation-generate-crud-code.md) — CRUD 코드 생성
- [Generate with Custom Templates](./vscode-code-generation-custom-templates.md) — 사용자 정의 템플릿
- [Download Template Context](./vscode-code-generation-template-context.md) — 템플릿 컨텍스트 다운로드

### Configuration Generation

- [Configuration Generation](./vscode-config-generation.md) — 설정 생성 개요
- [Cache](./vscode-config-generation-cache.md) · [Common](./vscode-config-generation-common.md) · [Datasource](./vscode-config-generation-datasource.md)
- [ID Generation](./vscode-config-generation-id-generation.md) · [Logging](./vscode-config-generation-logging.md) · [Property](./vscode-config-generation-property.md)
- [Scheduling](./vscode-config-generation-scheduling.md) · [Transaction](./vscode-config-generation-transaction.md)

## 참고자료

- [VS Code Extension 설치 가이드](../install-guide/vscode-extension-install-guide.md)
- [VS Code 활용 가이드](../development-etcdevtool-guide/vscode-usage.md)
