# Передача пользовательских параметров

import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\Стас\\AppData\\Local\\Google\\Chrome\\User Data')
# options_chrome.add_argument("--profile-directory=Profile 1") # в случае если несколько профилей в Хроме или необходимо
# работать параллельно с включенным Хромом

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(10)