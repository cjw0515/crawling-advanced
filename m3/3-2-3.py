import requests, json

# 세션 열기
s = requests.Session()
url = 'http://httpbin.org/stream/20'

r = s.get(url, stream=True)
# print(r.text)
print(r.encoding)
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line)
    for e in b.keys():
        print("key: ", e, "/", "values: ", b[e])
    # print(b['headers'])


# 세션 닫기
s.close()