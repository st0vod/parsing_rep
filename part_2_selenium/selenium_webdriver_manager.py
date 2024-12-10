# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# with webdriver.Chrome(ChromeDriverManager().install()) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# Или
"""
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)
"""

# Рабочий вариант без webdriver_manager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(service=ChromiumService(), options=webdriver.ChromeOptions()) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)

# Рабочий вариант
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Путь к вашему Chromium

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
    driver.get("https://stepik.org/course/104774")
    sleep(5)