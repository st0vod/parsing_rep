import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver

options = {'proxy': {
    'http': "socks5://31.59.35.200:13193", # убрал пароль и логин
    'https': "socks5://31.59.35.200:13193",
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)