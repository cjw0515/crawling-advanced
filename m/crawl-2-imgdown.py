import errno
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("연예인")
url = base + quote

res = req.urlopen(url)
savePath = "C:\\crawling\\imgs\\lion\\"
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, div in enumerate(li_list,1):
    print("div =", div['data-source'])
    fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
    print(fullfilename)
    req.urlretrieve(div['data-source'],fullfilename)
    print(i)