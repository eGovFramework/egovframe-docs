---
title: 구현 도구
linkTitle: 구현 도구
description: "구현 도구"
url: /egovframe-development/implementation-tool/
menu:
  depth:
    weight: 3
    parent: "egovframe-development"
    identifier: "implementation-tool"
---

# 구현 도구

## 개요

구현 도구는 Eclipse 기반 IDE로 표준프레임워크 응용SW 개발에 필요한 기능을 제공한다. 프로젝트 생성 마법사, Code Generation, Code Inspection, DBIO·ERD·UML·WebFlow 에디터, 디버그, 서버 연결 관리 등을 지원한다.

## 주요 개념

구현 도구는 표준프레임워크 템플릿 프로젝트와 공통컴포넌트를 마법사로 생성하고, 모델(UML·XMI)이나 템플릿을 기반으로 코드를 생성하며, 정적분석(Inspection)으로 코드 품질을 점검한다. 배치·모바일 개발을 위한 Batch IDE, Mobile IDE도 함께 제공한다.

## 관련 문서

### IDE

- [IDE](./ide.md) — 구현 도구 IDE 개요
- [Template Project Wizard](./ide-template-project.md) — 템플릿 프로젝트 생성
- [Boot Template Project Wizard](./ide-boot-template-wizard.md) · [MSA Boot Template Project Wizard](./ide-msa-template-wizard.md)
- [Common Component Wizard](./ide-common-component-wizard.md) — 공통컴포넌트 생성
- [Editor](./editor.md) · [SourceCode Editor](./sourcecode-editor.md) · [Console](./console.md)
- [Customize Development Tool](./customize-development-tool.md) — 개발 도구 커스터마이즈

### Batch IDE

- [Batch IDE](./batch-IDE.md) — 배치 개발 환경
- [Batch Template Project Wizard](./batch-ide-batch-template-wizard.md) · [Batch Job Wizard](./batch-ide-batch-job-wizard.md)
- [Batch Job Launcher Wizard](./batch-ide-batch-job-launcher-wizard.md) · [Batch Configuration](./batch-ide-batch-configuration.md)

### Mobile IDE

- [Mobile IDE](./mobile-ide.md) · [Mobile Template Project Wizard](./mobile-ide-template-project-wizard.md)

### Code Generation

- [Code Generation](./code-generation.md) — 코드 생성 개요
- [템플릿 기반 Code Generation](./code-generation-template.md) — [CRUD](./code-generation-template-crud.md) · [Configuration](./code-generation-template-configuration.md) · [Custom Templates](./code-generation-template-custom.md)
- [모델 기반 Code Generation](./code-generation-model.md) — [UML 기반](./code-generation-model-uml.md) · [XMI 기반](./code-generation-model-xmi.md) · [XMI Export](./code-generation-model-xmi-export.md)

### Code Inspection

- [Code Inspection](./code-inspection.md) — 정적분석 개요
- [Inspection 도구 활용](./code-inspection-tool.md) · [Inspection 사용자정의 룰 활용](./code-inspection-custom-rule.md)

### 에디터

- [DBIO Editor](./dbio-editor.md) — [Mapper Editor](./dbio-editor-mapper-editor.md) · [Mapper Configuration Editor](./dbio-editor-mapper-configuration-editor.md) · [DBIO Search View](./dbio-editor-dbio-search-view.md) · [Data Source Explorer](./dbio-editor-data-source-explorer.md)
- [ERD Editor](./erd-editor.md) — 데이터 모델링
- [UML Editor](./uml-editor.md) — [Class](./uml-editor-class-diagram-editor.md) · [Use Case](./uml-editor-use-case-diagram-editor.md) · [Sequence](./uml-editor-sequence-diagram-editor.md) · [Activity](./uml-editor-activity-diagram-editor.md)
- [WebFlow Editor](./webflow-editor.md) — 화면 흐름 정의

### Debug

- [Debug](./debug.md) — [Local Debug](./debug-local-debug.md) · [Remote Debug](./debug-remote-debug.md)

### 서버 연결 관리

- [Server Connection Management](./server-connection-management.md) — [SVN Repositories View](./server-connection-management-svn.md) · [Nexus](./server-connection-management-nexus.md)

### 기타

- [jsp-api.jar import 가이드](./importjspapi-guide.md)
- [참조 문서 목록](./implementation-tool-ref.md)

## 참고자료

- [개발환경 설치 가이드](../install-guide/_index.md)
- [구현 도구(VS Code)](../vscode-implementation-tool/_index.md)
