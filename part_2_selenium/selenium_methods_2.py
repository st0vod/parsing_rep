# alert = browser.switch_to.alert
# alert.text - получаем текст из всплывающего окна
# alert.accept() - автоматически нажимает кнопку "ОК"
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/5.5/1/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    for box in browser.find_elements(By.CLASS_NAME, 'text-field'):
        box.clear()

    browser.find_element(By.ID, 'checkButton').click()
    sleep(2)
    alert = browser.switch_to.alert
    sleep(2)

    print(alert.text)
    alert.accept() # после alert не доступен

