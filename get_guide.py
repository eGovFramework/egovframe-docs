import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.1:init_guide"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a'):
        if '인쇄' in a.text or '출력' in a.text:
            print(a.text.strip(), a.get('href'))
except Exception as e:
    print(e)
