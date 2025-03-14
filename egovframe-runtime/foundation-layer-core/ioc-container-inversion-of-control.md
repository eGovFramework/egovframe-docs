---
title: Inversion of Control
linkTitle: "Inversion of Control"
description: 이 문서는 Martin Fowler가 작성한 "Inversion of Control" 글을 번역하고 일부 의역한 내용이다.
url : "/egovframe-runtime/foundation-layer-core/ioc-container/ioc-container-iversion-of-control/"
menu:
  depth:
    name: Inversion of Control
    weight: 14
    parent: "ioc-container"
---
# Inversion of Control

## 개요

본 문서는 [Martin Fowler](https://martinfowler.com/)가 저술한 [Inversion of Control](https://martinfowler.com/bliki/InversionOfControl.html) 문서를 번역 및 일부 의역한 것이다.

## 설명

Inversion of Control(IoC)는 당신이 프레임워크를 확장할 때 마주치게 되는 일반적인 사상이다. 또한, 프레임워크를 정의하는 특징이기도 하다.

간단한 예제를 생각해보자. 명령줄의 질문을 통해 사용자로부터 어떠한 정보를 입력받는 프로그램을 작성한다고 생각해보자. 나는 아마 다음과 같은 것을 작성할 것이다.

```ruby
#ruby
puts 'What is your name?'
name = gets
process_name(name)
puts 'Waht is your quest?'
quest = gets
process_quest(quest)
```

위 예제에서, 내가 작성한 코드는 제어권을 가지고 있다 : 질문을 언제 할 것인지, 대답은 언제 읽을 것인지, 그리고 그런 결과들을 언제 처리할 것인지 등을 결정하고 있다.

만약 같은 일을 하기 위해서 윈도우 시스템을 사용한다면, 나는 다음과 같이 윈도우를 설정할 것이다.

```ruby
require 'tk'
root = TkRoot.new()
name_label = TkLabel.new() {text "What is Your Name?"}
name_label.pack
name = TkEntry.new(root).pack
name.bind("FocusOut") {process_name(name)}
quest_label = TkLabel.new() {text "What is Your Quest?"}
quest_label.pack
quest = TkEntry.new(root).pack
quest.bind("FocusOut") {process_quest(quest)}
Tk.mainloop()
```
위 두 프로그램은 제어의 흐름에 있어서 큰 차이점을 가지고 있다. 특히 process_name과 process_quest 메소드가 호출되는 시점에 대한 제어가 다르다. 명령줄 방식을 사용한 프로그램의 경우, 나는 메소드들이 호출되는 시점을 직접 제어했다. 하지만, 윈도우를 사용한 프로그램은 그러지 않았다. 대신 나는 윈도우 시스템에게 제어권을 넘겨주었다(Tk.mainloop 명령어를 사용하여). 윈도우 시스템은 내가 폼을 생성할 때 만든 결합 정보를 이용하여 내 메소드들을 호출할 시점을 결정한다. 즉, 제어가 역전된 것이다 - 내가 프레임워크를 호출하는 것이 아니라 프레임워크가 나를 호출하는 것이다. 이 사상이 Inversion of Control이다(또한 Hollywood Principle - “Dont' call us, we'ss call you”라고도 한다).

*프레임워크의 가장 중요한 특징은, 사용자가 프레임워크를 사용하기 위해 만든 메소드들이 사용자 어플리케이션 코드에서 호출되는 것보다 프레임워크에 의해 호출되는 것이 더 종종 일어난다는 것이다. 프레임워크는 어플리케이션의 활동을 조합하고 순차적으로 수행하는 메인 프로그램의 역할을 수행한다. 이러한 제어의 역전이 프레임워크가 확장가능한 뼈대로서의 기능을 수행할 수 있도록 해준다. 사용자는 프레임워크가 정의한 일반적인 알고리즘을 확장하여 특정 어플리케이션을 위한 메소드를 생성한다.*

- [Ralpth Johnson and Brian Foote](http://www.laputan.org/drc/drc.html)

Inversion of Control은 프레임워크를 라이브러리와 구별짓게 만드는 핵심이다. 라이브러리는 본질적으로 당신이 호출할 수 있는 기능들의 집합이다(요즘은 이러한 기능들이 클래스를 구성하고 있다). 한번 호출되면 작업을 수행하고 클라이언트에게 다시 제어권을 넘긴다.

프레임워크는 일부 추상적인 설계를 가지고 있으며, 미리 정의된 행동 방식을 가지고 있다. 프레임워크를 사용하기 위해서 당신은 프레임워크가 제공하는 클래스를 상속하거나 또는 작성한 클래스를 프레임워크에 삽입함으로써 프레임워크에 존재하는 확장 지점에 당신이 원하는 행동 방식을 삽입해야 한다. 그러면 프레임워크는 각각의 확장 지점에서 당신의 코드를 호출할 것이다.

당신이 만든 코드를 삽입하는 방식에는 여러가지가 있다. 위 ruby 예제의 경우, 우리는 이벤트 이름과 [Closure](https://martinfowler.com/bliki/Lambda.html)를 변수로 갖는 text entry field의 bind 메소드를 호출했다. Text entry box는 이벤트를 감지할 때 마다 closure의 코드를 호출한다. 이처럼 closure를 이용하는 것은 매우 간편하지만, 이를 지원하는 언어는 많지 않다.

또다른 방법으로는 프레임워크가 이벤트를 정의하고, 클라이언트가 이들 이벤트를 받는 방법이 있다 .NET 플랫폼이 이벤트를 선언할 수 있는 언어적 특징을 가진 좋은 예이다. 당신은 delegate를 사용하여 메소드와 이벤트를 연결할 수 있다.

위 방식(실제로는 둘은 같다)은 단순한 경우에는 잘 동작한다. 하지만 때때로 당신은 하나의 확장 지점에서 여러개의 메소드를 접합하기를 원할 수도 있다. 이런 경우 프레임워크는 인터페이스를 정의하고 클라이언트가 이를 구현할 수 있다.

EJB가 이런 inversion of control 형식의 좋은 예이다. 당신이 session bean을 개발할 때, 당신은 여러 생명주기 지점에서 EJB 컨테이너에 의해 호출되는 다양한 메소드를 구현할 수 있다. 예를 들어, Session Bean 인터페이스는 ejbRemote, ejbPassivate(2차 저장소에 저장됨), 그리고 ejbActivate(비활성 상태에서 복원됨)를 정의한다. 당신은 이 메소드들이 호출되는 시점에 대한 제어권을 가지지 않고, 다만 무엇을 할 것인지만 결정한다. 컨테이너가 우리를 호출하고, 우리는 그러지 않는다.

Inversion of Control의 복잡한 경우가 존재하지만, 당신은 좀더 단순한 상황에서 효과를 볼 수 있다. Template method가 좋은 예이다: 부모클래스는 제어의 흐름을 정의하고, 자식클래스는 메소드를 재정의하거나 추상메소드를 구현함으로써 확장할 수 있다. JUnit에서, 프레임워크는 당신이 테스트 기반을 생성하고 삭제하기 위해 작성한 setUp과 tearDown 메소드를 호출한다. 프레임워크가 호출하면, 당신의 코드는 반응한다. 즉, 제어가 역전된 것이다.

요즘 IoC 컨테이너의 등장에 따라 inversion of control의 의미에 대한 일부 혼동이 발생하고 있다. 몇몇 사람들은 이 문서에서 설명한 일반적인 원리와 이들 컨테이너에서 사용하고 있는 inversion of control의 특수한 형식인 dependency injection을 혼동하고 있다. 이름에서 약간 혼란이 야기된다고 할 수 있는데,(또한 모순적이기도 하다) IoC 컨테이너는 일반적으로 EJB의 경쟁상대로 간주되지만 EJB가 inversion of control을 더 많이 사용하기 때문이다.

어원: 내가 알기론, Inversion of Control이란 단어는 1988년 Object-Oriented Programming 저널에 발표된 Johnson and Foote의 논문 Designing Reusable Classes에서 처음 사용되었다. 이 논문은 잘 작성된 눈문 중의 하나로, 발표 이후 15년에 이른 현재까지도 읽을만한 가치가 있다. 그들은 어딘가 다른 곳에서 단어를 가져왔다고 하지만, 어디였는지는 기억하지 못한다. 이 단어는 object-oriented 커뮤니티 속으로 점점 더 녹아들었고 결국 책 Gang of Four에도 나타나게 되었다. 좀 더 화려한 별칭인 'Hollywood Principle'은 1983년 Mesa에 실린 [Richard Sweet의 논문](https://www.digibarn.com/friends/curbow/star/XDEPaper.pdf)에서 고안된 걸로 보인다. 설계 목표에서 그는 다음과 같이 기술하고 있다. *“Don't call us, we'll call you (Hollywood's Law): A tool should arrange for Tajo to notify it when the user wishes to communicate some event to the tool, rather than adopt an' ask the user for a command and execute it' model.”* John Vlissides는 column for C++ report에서 ['Hollywood Principle'](https://www.dre.vanderbilt.edu/~schmidt/hollywood-principle.txt) 의 개념을 잘 설명하고 있다. (어원에 대해서 도움을 준 Brian Foote과 Ralph Johnson에게 감사드린다.)

## 참고자료
  - http://martinfowler.com/bliki/InversionOfControl.html