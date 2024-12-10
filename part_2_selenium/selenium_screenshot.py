#сохранение скриншота страницы

from selenium import webdriver

url = 'https://en.wikipedia.org/wiki/Main_Page'
options = webdriver.ChromeOptions()
options.add_argument('--headless')

with webdriver.Chrome(options=options) as br:
    br.get(url)
    br.save_screenshot('wiki.png')