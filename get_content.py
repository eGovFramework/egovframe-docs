import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_wiki(wiki_id):
    url = f"https://www.egovframe.go.kr/wiki/doku.php?id={urllib.parse.quote(wiki_id)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.find('div', class_='page')
        if content:
            print(f"=== {wiki_id} ===")
            print(content.text.strip())
        else:
            print(f"Content not found for {wiki_id}")
    except Exception as e:
        print(f"Error fetching {wiki_id}: {e}")

fetch_wiki('egovframework:화면인쇄')
fetch_wiki('egovframework:전자관인출력')
fetch_wiki('egovframework:프린터상태확인')
