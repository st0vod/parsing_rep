from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/6/6.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    number = browser.find_element(By.ID, 'text_box').text

    if all([x in " 01234567890()*/+-" for x in number ]):

        number = eval(number)
        print(f"Looking for {number}")
        browser.find_element(By.CLASS_NAME, 'content').click()
        sleep(1)

        browser.find_element(By.XPATH, f"//option[text()={number}]").click()
        sleep(2)

        browser.find_element(By.CLASS_NAME, 'content').click()
        sleep(1)

        browser.find_element(By.CLASS_NAME, 'btn').click()

        result = browser.find_element(By.ID, 'result').text
        sleep(2)

        print(f"Answer is {result}")
    else:
        print('Argument Error!')
