import urllib.request
import urllib.parse
import ssl
from html.parser import HTMLParser

class WikiSearchParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []
        self.in_div = False
        self.in_a = False
        self.current_href = ""
        self.current_title = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for attr in attrs:
                if attr[0] == "class" and "search_result" in attr[1]:
                    self.in_div = True
        elif tag == "a" and self.in_div:
            self.in_a = True
            for attr in attrs:
                if attr[0] == "href":
                    self.current_href = attr[1]

    def handle_endtag(self, tag):
        if tag == "a" and self.in_a:
            self.in_a = False
            if self.current_href and self.current_title:
                self.results.append((self.current_title, self.current_href))
                self.current_href = ""
                self.current_title = ""
        elif tag == "div":
            self.in_div = False

    def handle_data(self, data):
        if self.in_a:
            self.current_title += data.strip()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.egovframe.go.kr/wiki/doku.php?do=search&id=start&q=" + urllib.parse.quote('서버 자원')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    parser = WikiSearchParser()
    parser.feed(html)
    for title, href in parser.results:
        print(title, href)
except Exception as e:
    print("Error:", e)
