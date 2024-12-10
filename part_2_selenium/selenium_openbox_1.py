from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    total_sum = sum(int(line.text) for line in browser.find_elements(By.TAG_NAME, 'option'))

    browser.find_element(By.ID, 'input_result').send_keys(str(total_sum))
    sleep(2)

    print(f'Общая сумма: {total_sum}')
    browser.find_element(By.CLASS_NAME, 'btn').click()

    result = browser.find_element(By.ID, 'result')
    sleep(2)

    print(result.text)