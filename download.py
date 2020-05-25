import urllib.request as dw

img_url = "http://cafefiles.naver.net/20101205_110/gpdnjs2744_1291515989689d5yOt_jpg/608134866_12902505481_gpdnjs2744.jpg"
html_url = "http://google.com"

save_path = "c:/crawling/imgs/puppy.jpg"
save_path2 = "c:/crawling/imgs/index.html"

# dw.urlretrieve(img_url, save_path)
# dw.urlretrieve(html_url, save_path2)

# img
f = dw.urlopen(img_url).read()

f2 = dw.urlopen(html_url).read()
save_file1 = open(save_path, 'wb') # w: write, r: read, a: add
save_file1.write(f)
save_file1.close()

# html
# with 사용 - 메모리 자동 반납 구문
with open(save_path2, 'wb') as save_file2:
    save_file2.write(f2)

print('다운로드 완료')

