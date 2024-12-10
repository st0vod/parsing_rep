from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    # Проходимся по списку найденных элементов и выводим их текст
    for i, p_element in enumerate(p_elements):
        print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")


# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    # Открываем URL
    browser.get(url)

    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'text')

    # Проходимся по каждому div
    for i, div in enumerate(divs):
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')

        # Выводим их текст
        print(f"Для div #{i + 1}, первый p: {first_p.text}, третий p: {third_p.text}")

