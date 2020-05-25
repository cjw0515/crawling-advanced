import urllib.request as req
from urllib.parse import urlparse

url = "https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query=1t+ssd"
mem = req.urlopen(url)

# print("geturl", mem.geturl())
# print("status", mem.status)
# print("headers", mem.getheaders())
# print("info", mem.info())
# print("code", mem.getcode())
# print("read", mem.read())
# print("read", mem.read().decode("utf-8"))
print(urlparse(url))