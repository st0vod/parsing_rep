import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://parsinger.ru/selenium/3/3.html'
url_stepik = 'https://stepik.org/lesson/709437/step/12?unit=710000'
option = webdriver.ChromeOptions()

#option.add_argument('--headless')

option.add_argument('user-data-dir=C:\\Users\\Стас\\AppData\\Local\\Google\\Chrome\\User Data')


with webdriver.Chrome(options=option) as driver:
    driver.get(url)
    # values = sum(map(lambda x: int(x.text), driver.find_elements(By.TAG_NAME, 'p'))) Сумма всех абзацев

    values = sum(map(lambda x: int(x.text), driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")))
    print(values)

    driver.get(url_stepik)
    # driver.execute_script("window.scrollBy(0, 150);") выполняет JS скрипт в браузере
    wait = WebDriverWait(driver, 20)

    input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.number-quiz__input.number-input')))

    input_field.clear()
    input_field.send_keys(values)

    driver.find_element(By.XPATH, "//button[@class='submit-submission']").click()
    time.sleep(5)

