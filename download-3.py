from urllib.parse import urlencode
import urllib.request as req

# api = "https://api.ipify.org"
api = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000"
values = {
    'format': 'json'
}
print('before', values)
params = urlencode(values)
print('after', params)

# url = api + "?" + params
print("요청 url", api)

res = req.urlopen(api).read().decode("utf-8")
print("출력", res)