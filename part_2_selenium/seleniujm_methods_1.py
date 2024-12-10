# метод refresh
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/1/index.html'
cnt = 0
with webdriver.Chrome() as browser:
    browser.get(url)

    while True:
        temp = browser.find_element(By.ID, 'result').text
        cnt += 1
        if temp != 'refresh page':
            sleep(3)
            print(temp)
            break
        browser.refresh()
print(cnt)

# 4168138981270992
