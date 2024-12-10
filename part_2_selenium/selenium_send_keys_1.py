import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome() as driver:
    driver.get(url)
    blocks = driver.find_elements(By.CLASS_NAME, 'form')

    for block in blocks:
        block.send_keys('text')

    button = driver.find_element(By.ID, 'btn')
    button.click()
    time.sleep(10)