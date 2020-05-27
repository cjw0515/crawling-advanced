from selenium import webdriver

driver = webdriver.Chrome('c:/crawling/crawling-advanced/chrome_driver/chromedriver.exe')
# 무조건 5초가 아니라, 로드가 다 되면 넘어간다.
driver.implicitly_wait(5)
driver.get('https://sites.google.com/a/chromium.org/chromedriver/downloads')


