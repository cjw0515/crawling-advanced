from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep

base = "https://www.inflearn.com/"
# quote = rep.quote_plus("추천-강좌")
# url = base + quote
url = base
res = req.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(res, "html.parser")

recommand = soup.select(".welcome_content .swiper-wrapper .swiper-slide")

cond = {"class":"course_title"}

print(soup.find("div", cond))


