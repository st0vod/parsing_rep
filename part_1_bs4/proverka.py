import csv
import requests
from bs4 import BeautifulSoup

# Создание CSV файла и запись заголовков
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'])

# Парсинг страниц и запись данных в CSV
for i in range(1, 6):
    url = f'https://parsinger.ru/html/index{i}_page_1.html'
    schema = 'https://parsinger.ru/html/'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        spisok_url = soup.find('div', class_='pagen').find_all('a')
    else:
        print('Нет данной страницы')

    # Обход всех подстраниц
    for j in spisok_url:
        url = f'{schema}{j["href"]}'
        response = requests.get(url=url)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            details = soup.find_all('div', class_='sale_button')
        else:
            print('Нет данной страницы')

        # Извлечение информации о каждом товаре
        for k in details:
            url = f'{schema}{k.find('a')['href']}'
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            if response.status_code == 200:
                # Извлечение свойств товара
                name = [soup.find('p', id='p_header').text]
                article = [soup.find('p', class_='article').text.split(':')[-1].strip()]
                brand = [soup.find('li', id='brand').text.split(':')[-1].strip()]
                model = [soup.find('li', id='model').text.split(':')[-1].strip()]
                stock = [soup.find('span', id='in_stock').text.split(':')[-1].strip()]
                new_price = [soup.find('span', id='price').text]
                old_price = [soup.find('span', id='old_price').text]

                # Запись данных в CSV файл
                with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    num = 1
                    for name, article, brand, model, stock, new_price, old_price, url in zip(name, article, brand,
                                                                                             model,
                                                                                             stock, new_price,
                                                                                             old_price, [url]):
                        # Формируем строку для записи
                        print(num, url)

                        flatten = name, article, brand, model, stock, new_price, old_price, url
                        print(flatten)
                        num += 1
                        writer.writerow(flatten)
            else:
                print('Нет данной страницы')

print('Файл res.csv создан')