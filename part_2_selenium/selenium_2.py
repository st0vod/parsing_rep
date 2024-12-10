# Передача параметров

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument(f'user-agent={UserAgent().random}')
option.add_extension('coordinates.crx')

with webdriver.Chrome(options=option) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(10)

    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))