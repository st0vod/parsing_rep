import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()


def resp(url: str):
    # Функция выполгняет запрос по полученной ссылке и отправляется объект класса bs4.element.Tag
    response = session.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def sub_discription_dict(values: list) -> dict:
    # Функцтя создает словарь для ключа description
    res = {}
    for li in values:
        res[li['id']] = li.text.split(': ')[1].strip()
    return res


schema = 'https://parsinger.ru/html/'
url = 'https://parsinger.ru/html/index2_page_1.html'
data = []

try:

    pagens = (schema + a['href'] for a in resp(url).find('div', class_='pagen').find_all('a'))
    category = resp(url).find('div', class_='nav_menu').select('a div')[1][
                'id']  # заготовка для следующей задачи

    for pagen in pagens:  # проход по страницам раздела

        soup = resp(pagen)
        sale_buttons = (schema + a['href'] for div in soup.find_all('div', class_='sale_button') for a in
                        div.find_all('a'))

        for link in sale_buttons:  # проход по ссылкам товаров на странице

            soup = resp(link).find('div', class_='description')
            # result = {}  # начало формирование словаря
            result = {}
            result['categories'] = category
            result['name'] = soup.find('p', id='p_header').text.strip()
            result['article'] = soup.find('p', class_='article').text.split(': ')[1].strip()
            result['description'] = sub_discription_dict(soup.select_one('#description').find_all('li'))
            result['count'] = soup.find(id='in_stock').text.split(': ')[1].strip()
            result['price'] = soup.find(id='price').text.strip()
            result['old_price'] = soup.find(id='old_price').text.strip()
            result['link'] = link

            data.append(result)

except requests.HTTPError as err:
    print(f'Сайт не доступен: {err}')

except requests.RequestException as err:
    print(f'Ошибка: {err}')

else:
    with open('sale_cards.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('Парсинг сайта завершен. Файл записан.')