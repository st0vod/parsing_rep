from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/4/1.html'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)

    for div in browser.find_elements(By.CLASS_NAME, 'parent'):
        gray_block = div.find_element(By.XPATH, "textarea[@color='gray']")
        div.find_element(By.XPATH, "textarea[@color='blue']").send_keys(gray_block.text)
        gray_block.clear()

        div.find_element(By.TAG_NAME, "button").click()


    browser.find_element(By.ID, "checkAll").click()
    result = browser.find_element(By.ID, "congrats")

    print(result.text)