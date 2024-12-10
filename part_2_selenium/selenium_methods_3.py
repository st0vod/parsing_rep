# is_enabled()

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/2/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    for elem in browser.find_elements(By.CLASS_NAME, 'text-field'):
        if elem.is_enabled():
            elem.clear()

    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert

    print(alert.text)
    alert.accept()