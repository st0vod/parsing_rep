from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы, с которой будем извлекать данные
url = 'https://parsinger.ru/html/index1_page_1.html'

# Выполняем HTTP-запрос к указанному URL-адресу
response = requests.get(url=url)

# Устанавливаем кодировку ответа в 'utf-8', чтобы корректно отображать кириллицу
response.encoding = 'utf-8'

# Создаем объект BeautifulSoup для анализа HTML-кода страницы
# Второй аргумент 'lxml' указывает на используемый парсер
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице первый элемент 'div' с классом 'item'
div = soup.find('div', 'item')

# Выводим найденный элемент на экран
print(div)