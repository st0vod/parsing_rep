import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 3,1415926535897932384626433832795028841971
url = 'https://parsinger.ru/selenium/4/4.html'
url_stepik = 'https://stepik.org/lesson/709437/step/13?unit=710000'

option_driver = webdriver.ChromeOptions()
option_driver.add_argument('user-data-dir=C:\\Users\\Стас\\AppData\\Local\\Google\\Chrome\\User Data')


with webdriver.Chrome(options=option_driver) as browser:
    browser.get(url)
    for check in browser.find_elements(By.CLASS_NAME, "check"):
        check.click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    message = browser.find_element(By.ID, "result").text
    print(message)

    browser.get(url_stepik)
    wait = WebDriverWait(browser, 20)
    input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.number-quiz__input.number-input')))
    input_field.clear()
    input_field.send_keys(message)
    browser.find_element(By.XPATH, "//button[@class='submit-submission']").click()

    time.sleep(10)