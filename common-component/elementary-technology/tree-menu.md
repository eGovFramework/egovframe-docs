---
title: "트리메뉴"
linkTitle: "트리메뉴"
description: "트리메뉴"
url: /common-component/elementary-technology/system/tree-menu/
menu:
  depth:
    name: "트리메뉴"
    weight: 73
    parent: "system"
---

## 개요

시스템의 좌측(LNB)이나 화면 내부에 표시되는 부서 조직도, 카테고리 등의 데이터를 상/하위 관계를 갖는 트리(Tree) 구조로 가공하여 반환하는 기능을 제공한다.

## 주요 기능

* **계층형 데이터 생성**: DB에 저장된 평면적인 메뉴 또는 부서 데이터를 부모-자식 관계에 따라 재귀적으로 구성한다.
* **접근 권한 처리**: 현재 로그인된 사용자가 접근 권한을 가진 트리 노드만 필터링하여 출력할 수 있도록 지원한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `List<MenuManageVO>` | `selectTreeMenu(String authCode)` | 트리 구조로 시각화하기 위한 계층형 메뉴 목록 데이터를 조회한다. |

```java
import egovframework.com.utl.fcc.service.EgovMainMenuUtil;

public class TreeMenuExample {
    public void getTreeData() throws Exception {
        String authCode = "ROLE_USER";
        
        // 트리 메뉴(좌측 메뉴 등) 정보 조회
        List<MenuManageVO> treeMenu = EgovMainMenuUtil.selectTreeMenu(authCode);
        
        for (MenuManageVO node : treeMenu) {
            System.out.println("Node: " + node.getMenuNm() + " (Parent: " + node.getUpperMenuId() + ")");
        }
    }
}
```
