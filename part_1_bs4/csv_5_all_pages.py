import csv
import requests
from bs4 import BeautifulSoup


def writing_csv(*args) -> None:
    """Функиця добавляет запись в .csv файл"""
    with open('cards_list.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(*args)


def my_requests(u: str):
    """Функция возвращает объект класса bs4.element.Tag"""
    response = requests.get(u)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


schema = 'https://parsinger.ru/html/'
headers = 'Наименование;Артикул;Бренд;Модель;Наличие;Цена;Старая цена;Ссылка'
writing_csv(headers.split(';'))

try:
    for i in range(1, 6):  # Проход по разделам магазина
        for j in range(1, 5):  # Проход по страницам разделов
            page_soup = my_requests(f'https://parsinger.ru/html/index{i}_page_{j}.html')
            cards = [schema + card['href'] for card in page_soup.find_all('a', class_="name_item")]

            for link in cards:  # Проход по каждой карточке товара
                link_soup = my_requests(link)
                card_discription = link_soup.find('div', class_='description')

                name = card_discription.find("p", id="p_header").text
                article = card_discription.find(class_="article").text.split(": ")[1].strip()

                values = [value.text.split(': ')[1] for value in
                          card_discription.find_all('li')]  # Список характеристик товара
                in_stock = card_discription.find(id="in_stock").text.split(": ")[1]

                price = link_soup.select_one('.sale #price').text
                old_price = link_soup.select_one('.sale #old_price').text

                writing_csv([name, article, *values[:2], in_stock, price, old_price, link])

except requests.HTTPError as err:
    print(f'Сайт не доступен: {err}')

except requests.RequestException as err:
    print(f'Ошибка: {err}')

else:
    print('Парсинг сайта завершен.')
