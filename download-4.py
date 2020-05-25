from urllib.parse import urlencode
import urllib.request as req

api = "https://api.ipify.org"
values = {
    'format': 'json'
}
print('before', values)
params = urlencode(values)
print('after', params)

url = api + "?" + params
print("요청 url", url)

res = req.urlopen(url).read().decode("utf-8")
print("출력", res)