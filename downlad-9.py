from bs4 import BeautifulSoup
import re #regex

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
test = soup.find('a', string="naver")
# print(soup.find(id="naver"))
# 정규 표현식
li = soup.findAll(href=re.compile(r"^https://"))
for e in li:
    print(e.string)
    print(e.attrs['href'])

