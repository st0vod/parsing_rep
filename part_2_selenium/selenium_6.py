import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 способ работы с веб-страницей и закрытие её в конце
try:
    driver = webdriver.Chrome()
    driver.get(url='http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, 'sale_button')
    print(button)
    time.sleep(2)

    button.click()
    time.sleep(2)

finally:
    driver.quit()

# 2 способ работы с веб-страницей и закрытие её в конце

with webdriver.Chrome() as driver_2:
    driver_2.get(url='http://parsinger.ru/html/watch/1/1_1.html')
    time.sleep(2)

    button.click()
    time.sleep(2)

