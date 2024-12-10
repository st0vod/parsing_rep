from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

url = 'https://parsinger.ru/selenium/2/2.html'
pattern = '16243162441624'
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument(f'user-agent={UserAgent().random}')

with webdriver.Chrome(options=option) as driver:

    driver.get(url)
    driver.find_element(By.LINK_TEXT, pattern).click()
    print(driver.find_element(By.ID, 'result').text)