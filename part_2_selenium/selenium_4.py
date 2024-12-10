from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

url = 'https://2ip.ru/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-name={UserAgent().random}')

#Вариант нахождения своего IP

# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#
#     sleep(2)
#
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

# Вариант проверки прокси под видом своего IP

# proxy = '113.160.133.32:8080'
#
# chrome_options.add_argument(f'--proxy-server={proxy}')  # ('--proxy-server=%s' % proxy)
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     sleep(2)
#
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

# Вариант с перебором прокси
proxies = ['74.255.219.229:3129', '143.110.226.180:8888', '222.252.194.29:8080', '113.160.133.32:8080', '15.235.153.57:8089',
           '15.235.153.57:8089', '123.126.158.50:80', '160.86.242.23:8080']

for PROXY in proxies:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        url = 'https://2ip.ru/'

        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(5) # подобие timeout в requests

            proxies.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue