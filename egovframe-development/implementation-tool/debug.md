---
title: Debug
linkTitle: Debug
description: "디버깅"
url: /egovframe-development/implementation-tool/debug/
menu:
  depth:
    weight: 2
    parent: "implementation-tool"
    identifier: "debug"
---
## 개요

Implentation Tool에는 로컬 또는 원격으로 실행 중인 프로그램에서 오류를 발견하고 진단할 수 있는 디버거가 포함되어 있다.

## 설명

디버거를 사용하면 중단점을 설정하고, 실행된 프로그램을 일시중단하고, 코드를 단계별로 진행하고, 변수 컨텐츠를 검토하여 프로그램 실행을 제어할 수 있다.

디버거에는 클라이언트/서버 설계가 있으므로 워크스테이션에서 로컬로 실행 중인 프로그램은 물론 네트워크의 다른 시스템에서 원격으로 실행 중인 프로그램도 디버그할 수 있습니다. 디버그 클라이언트는 워크스테이션의 Workbench에서 실행합니다. 디버거 서버는 디버그할 프로그램과 동일한 시스템에서 실행합니다. 이 디버거 서버는 워크스테이션에서 실행된 프로그램에 있을 수도 있고(로컬 디버깅) 네트워크를 통해 액세스할 수 있는 시스템에 있을 수도(원격 디버깅) 있습니다

## 참고자료

* Eclipse Help - Java development user guide
* [http://help.eclipse.org/ganymede/topic/org.eclipse.jdt.doc.user/concepts/cdebugger.htm](http://help.eclipse.org/ganymede/topic/org.eclipse.jdt.doc.user/concepts/cdebugger.htm)
