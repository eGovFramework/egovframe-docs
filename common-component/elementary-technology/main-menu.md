---
title: "메인메뉴"
linkTitle: "메인메뉴"
description: "메인메뉴"
url: /common-component/elementary-technology/system/main-menu/
menu:
  depth:
    name: "메인메뉴"
    weight: 52
    parent: "system"
---

## 개요

시스템의 상단 또는 메인 화면에 출력되는 주요 메뉴(GNB: Global Navigation Bar) 정보를 계층형 데이터 구조로 구성하여 제공하는 기능을 수행한다.

## 주요 기능

* **메뉴 구조화**: 데이터베이스나 설정 파일에 저장된 메뉴 정보를 상위/하위 트리 형태로 재구성한다.
* **권한별 메뉴 필터링**: 현재 로그인한 사용자의 권한 등급에 따라 접근 가능한 메뉴 목록만 추출하여 반환한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `List<MenuManageVO>` | `selectMainMenu(String authCode)` | 주어진 사용자 권한 코드에 해당하는 메인 메뉴 목록을 조회하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovMainMenuUtil;
import java.util.List;

public class MainMenuExample {
    public void getMenu() throws Exception {
        String userAuthCode = "ROLE_ADMIN";
        
        // 메인 메뉴 목록 조회
        List<MenuManageVO> menuList = EgovMainMenuUtil.selectMainMenu(userAuthCode);
        
        for (MenuManageVO menu : menuList) {
            System.out.println("Menu Name: " + menu.getMenuNm());
            System.out.println("Menu URL: " + menu.getChkURL());
        }
    }
}
```
