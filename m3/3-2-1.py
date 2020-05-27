import requests

# 세션 열기
s = requests.Session()
# r = s.get("https://www.naver.com")

url = 'http://httpbin.org/cookies'
headers = {'user-agent': 'mypythonapp_1.0.0'}

r = s.get(url, headers=headers)
print(r.text)


# 세션 닫기
s.close()