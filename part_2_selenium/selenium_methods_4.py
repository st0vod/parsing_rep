from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/3/1.html'


options = webdriver.ChromeOptions()
options.add_argument("--headless")
data = []

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    for _ in range(30):
        total = 0
        for elem in browser.find_elements(By.CLASS_NAME, 'parent'):
            if elem.find_element(By.TAG_NAME, "input").is_selected():
                total += int(elem.find_element(By.TAG_NAME, "textarea").text)


        data.append(total)
        browser.refresh()

print(set(data))

#{25899, 25878, 25903}
#{25892, 25903, 25815, 25883, 25879}