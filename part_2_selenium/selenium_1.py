# Работа с браузером
# Добавление расширения
# import time
# from selenium import webdriver
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension(r'C:\Users\Стас\AppData\Local\Google\Chrome\User Data\Default\Extensions\gkkmpbaijflcgbbdfjgihbgmpkhgpgof\coordinates.crx')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/course/104774'
#     browser.get(url)
#     time.sleep(15)



# Работа с браузером в фоновом режиме
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from time import perf_counter

start = perf_counter()

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')  # не открывает окно браузера

# options_chrome.add_argument(f"user-agent={UserAgent().random}")  # чтобы сайт не распознал попытку автоматичесего парсинга

options_chrome.add_argument('--disable-gpu') # отключает графический процессор, что полезно в headless режиме на системах
# без GPU, где его использование не нужно и может вызывать ошибки.

options_chrome.add_argument('--no-sandbox') # отключает песочницу браузера, что полезно для устранения проблем с правами
# доступа и совместимостью в headless режиме, особенно на серверах и контейнерах.

options_chrome.add_argument('--disable-dev-shm-usage') # решает проблемы с нехваткой общей памяти (shared memory)
# на системах с ограниченными ресурсами (например, Docker-контейнеры) и предотвращает сбои браузера.

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/a/104774'
    browser.get(url)

    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.TAG_NAME, 'a')

    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))

print(perf_counter() - start)


# --headless 27.34328450000612
# + user_agent 26.256944000022486
# + --disable-gpu 16.295577300013974
# + --disable-gpu + --no-sandbox 26.682368999987375
# + --disable-dev-shm-usage + --disable-gpu + --no-sandbox 8.144946499960497


