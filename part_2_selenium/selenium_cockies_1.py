from pprint import pprint
from selenium import webdriver
# from seleniumwire import webdriver # чтобы использовать авторизованный прокси
from fake_useragent import UserAgent
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={UserAgent().random}')


with webdriver.Chrome(options=options) as webdriver:
    webdriver.get('https:stepik.org/')
    sleep(3)
    cookies = webdriver.get_cookies()

    # pprint(cookies)
    for cookie in cookies:
        print(cookie['name'])

    # print(webdriver.get_cookie('yp'))
    # print(webdriver.get_cookie('yandex_csy')['expiry'])