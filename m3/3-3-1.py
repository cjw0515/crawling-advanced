import requests, json

# 세션 열기
s = requests.Session()
# url = 'http://api.github.com/events'
# r = requests.get(url)
#
# # 에러 처리
# r.raise_for_status()
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org', path='/cookies')

# r = requests.get('http://httpbin.org/cookies', cookies=jar)
# print(r.text)

# r = requests.get("https://github.com", timeout=3)
# print(r.text)

payload1 = {'key1': 'value1', 'key2': 'value2'} # dic
payload2 = {('key1', 'value1'), ('key2', 'value2')} # dic


# r = requests.post('http://httpbin.org/post', data=json.dumps(payload1))
r = requests.post('http://httpbin.org/post', payload1) # 제이슨으로 보낼 시 폼이 아니라 데이터로 들어간다.
print(r.text)


s.close()


