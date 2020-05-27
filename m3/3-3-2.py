import requests, json
from bs4 import BeautifulSoup

LOGIN_INFO = {
    'email': 'cjw0515',
    'password': '13211321a'
}

req_url = 'https://www.inflearn.com/api/signin'

with requests.Session() as s:
    login_req = s.post(url=req_url, data=LOGIN_INFO)
    if login_req.status_code == 200 and login_req.json()['ok']:
        res = s.get("https://www.inflearn.com/orders")
        print(s.cookies)
        print(s.headers)


