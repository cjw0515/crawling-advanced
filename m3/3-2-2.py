import requests

# 세션 열기
s = requests.Session()

url = 'https://jsonplaceholder.typicode.com/posts/1'

r = s.get(url)
print(r.text)
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)
print(r.raw)

# 세션 닫기
s.close()