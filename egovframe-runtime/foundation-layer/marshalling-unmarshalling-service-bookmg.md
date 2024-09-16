# BookMg.java

## 개요 

Marshalling/Unmarshallig 서비스 예제입니다. 

**Writer.java**

```java
public class BookMg 
{
  private String isbn;
  private String title;
  private List<Writer> writers;
 
  public BookMg() { }
  // 생성자
  @ isbn 책번호
  @ title 책제목
  @ writers 작가리스트
  public BookMg(String isbn, String title, List<Writer> writers) {
    this.isbn = isbn;
    this.title = title;
    this.writers = writers;
  }
   // 생성자
  @ isbn 책번호
  @ title 책제목
  @ writer 작가
  public BookMg(String isbn, String title, Writer writer) {
    this.isbn = isbn;
    this.title = title;
    this.writers = new LinkedList<Writer>();
    writers.add(writer);
  }
 // 책번호 설정
 @ isbn 책번호
  public void setIsbn(String isbn) {
    this.isbn = isbn;
  }
 // 책번호 리턴 
  public String getIsbn() {
    return isbn;
  }
 // 책제목 설정
 @ title 책제목
  public void setTitle(String title) {
    this.title = title;
  }
 // 책제목 리턴
  public String getTitle() {
    return title;
  }
 // 작가리스트 설정
 @ writers 작가리스트
  public void setWriters(List<Writer> writers) {
    this.writers = writers;
  }
 // 작가리스트 리턴 
  public List<Writer> getWriters() {
    return writers;
  }
 // 작가리스트에 작가 추가
 @ writer 작가
  public void addWriter(Writer writer) {
    writers.add(writer);
  }
}
```