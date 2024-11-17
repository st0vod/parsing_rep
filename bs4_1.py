from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_1.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице первый элемент <div> с классом 'item' и извлекаем из него все вложенные элементы <li>
div = [x.text for x in soup.find('div', 'item').find_all('li')]

print(*div, sep='\n')