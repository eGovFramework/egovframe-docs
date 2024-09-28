# Writer.java

## 개요 

Marshalling/Unmarshallig 서비스 예제입니다. 

**Writer.java**

```java
public class Writer 
{
  private String Name;
  // 생성자
  public Writer() { }
  // 작가명
  public Writer(String Name) {
    this.Name = Name;
  }
  // 작가명 수정
  public void setName(String Name) {
    this.Name = Name;
  }
  // 작가명 리턴 
   public String getName() {
    return Name;
  }
}
```
