import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()


def resp(url):
    response = session.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


schema = 'https://parsinger.ru/html/'
url = 'https://parsinger.ru/html/index1_page_1.html'
nav_menu = [schema + a['href'] for a in resp(url).find('div', class_='nav_menu').find_all('a')]
data = []

try:
    for section in nav_menu:
        pagen_menu = [schema + a['href'] for a in resp(section).find('div', class_='pagen').find_all('a')]

        for pagen in pagen_menu:
            soup = resp(pagen)
            item_names = [name.text.strip() for name in soup.find_all('a', class_='name_item')]
            item_prices = [price.text.strip() for price in soup.find_all('p', class_='price')]

            descriptions = (descriptions.text.strip().split('\n') for descriptions in
                            soup.find_all('div', class_='description'))
            item_values = []
            item_headers = []

            for values in descriptions:
                item_values.append(list(map(lambda x: x.split(':')[1].strip(), values)))
                item_headers.append(
                    [['Наименование'] + list(map(lambda x: x.split(':')[0].strip(), values)) + ['Цена']])

            for head, name, desc, price in zip(item_headers, item_names, item_values, item_prices):
                data.append(dict(zip(*head, [name, *desc, price])))

except requests.RequestException as err:
    print(f'Произошла ошибка: {err}')
else:
    with open('full.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print('Запись завершена.')

""" Интересное решение задачи
import requests
from bs4 import BeautifulSoup
import json


def get_sell_value(selectors):
    result = {}
    for selector in selectors:
        key, value = el.select_one(selector).text.split(': ', 1)
        result[key.strip()] = value.strip()
    return result


selectors = ['li:first-child', 'li:nth-child(2)', 'li:nth-child(3)', 'li:last-child']
data = []

for categories in range(1, 6):
    for page in range(1, 5):
        url = f'https://parsinger.ru/html/index{categories}_page_{page}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'  

        soup = BeautifulSoup(response.text, 'html.parser')
        for el in soup.find_all('div', class_='img_box'):
            elems = {"Наименование": el.select_one('.name_item').text.strip()} | get_sell_value(selectors) | {"Цена": el.select_one('p.price').text}
            data.append(elems)
    print(f'Успешная выгрузка товаров по адресу: https://parsinger.ru/html/index{categories}')


with open('data1.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print('Выгрузка завершена успешно')
"""