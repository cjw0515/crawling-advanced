from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>파이썬 beautifulsoup 공부</h1>
        <p>태그 선택자</p>
        <p>css 선택자</p>
    </body>
</html>
"""

# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print('soup', type(soup))
# print('pretty', soup.prettify())

h1 = soup.html.body.h1
print('h1', h1)
print(h1.string)
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling
print(p2)