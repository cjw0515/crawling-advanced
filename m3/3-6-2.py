from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options,
                          executable_path=r'c:/crawling/crawling-advanced/chrome_driver/chromedriver.exe')
driver.set_window_size(1920, 1080)
# 무조건 5초가 아니라, 로드가 다 되면 넘어간다.
driver.implicitly_wait(5)
driver.get('https://sites.google.com/a/chromium.org/chromedriver/downloads')
driver.save_screenshot('c:/crawling/imgs/screenshot/website_ch.png')

time.sleep(5)

driver.quit()

