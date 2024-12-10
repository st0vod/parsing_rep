import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()


def resp(url):
    response = session.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


schema = 'https://parsinger.ru/html/'
header = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
url = 'https://parsinger.ru/html/index4_page_1.html'
pagen = [schema + a['href'] for a in resp(url).find('div', class_='pagen').find_all('a')]
func_ = lambda x: x.split(': ')[1].strip()
data = []
try:
    for link in pagen:
        soup = resp(link)
        names = [name.text.strip() for name in soup.find_all(class_='name_item')]
        descriptions = [tuple(map(func_, description.text.strip().split('\n'))) for description in
                        soup.find_all('div', class_='description')]
        prices = [price.text.strip() for price in soup.find_all('p', class_='price')]

        for name, desc, price in zip(names, descriptions, prices):
            data.append(dict(zip(header, [name, *desc, price])))

        print(f'Запись данных со страницы: {link} в файл hdd.json выполнена')

except requests.RequestException as err:
    print(f'Произошла ошибка: {err}')
else:
    with open('hdd.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('Запись завершена.')
