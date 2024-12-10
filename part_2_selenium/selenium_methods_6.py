from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/5/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    blocks = browser.find_elements(By.CSS_SELECTOR, "#main-container > div")
    for i, block in enumerate(blocks, 1):
        color = block.find_element(By.TAG_NAME, "span").text

        block.find_element(By.CSS_SELECTOR, f"option[value='{color}']").click()

        block.find_element(By.CSS_SELECTOR, f"button[data-hex='{color}']").click()

        block.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()

        block.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(color)

        block.find_element(By.CSS_SELECTOR, "#main-container > div > button").click()

    browser.find_element(By.CSS_SELECTOR, "body > button").click()
    sleep(1)

    alert = browser.switch_to.alert
    print(alert.text)
    sleep(1)
    alert.accept()

