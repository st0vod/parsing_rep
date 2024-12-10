import requests
import csv
from bs4 import BeautifulSoup

headers = ['Название', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Игровая', 'Подсветка', 'Размер', 'Разрешение',
           'Сайт производителя', 'В наличии', 'Цена', 'Старая цена']


def writing_csv(*args) -> None:
    """Функиця добавляет запись в .csv файл"""
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(*args)


schema = 'https://parsinger.ru/html/'
writing_csv(headers)

for i in range(1, 5):

    url_current = f'https://parsinger.ru/html/index3_page_{i}.html'
    response = requests.get(url_current)
    soup = BeautifulSoup(response.content, 'html.parser')

    for card in soup.select('.sale_button > a'):
        card_url = schema + card['href']

        card_response = requests.get(card_url)
        card_soup = BeautifulSoup(card_response.content, 'html.parser')
        card_discription = card_soup.find('div', class_='description')

        name = card_discription.find("p", id="p_header").text
        article = card_discription.find(class_="article").text.split(": ")[1]
        brand = card_discription.find(id="brand").text.split(": ")[1]
        model = card_discription.find(id="model").text.split(": ")[1]
        type_ = card_discription.find(id="type").text.split(": ")[1]
        purpose = card_discription.find(id="purpose").text.split(": ")[1]
        light = card_discription.find(id="light").text.split(": ")[1]
        size = card_discription.find(id="size").text.split(": ")[1]
        dpi = card_discription.find(id="dpi").text.split(": ")[1]
        site = card_discription.find(id="site").text.split(": ")[1]

        in_stock = card_discription.find(id="in_stock").text.split(": ")[1]

        prices = card_soup.find('div', class_='sale')

        price = prices.find(id="price").text
        old_price = prices.find(id="old_price").text

        writing_csv([name, article, brand, model, type_, purpose, light, size, dpi, site, in_stock, price, old_price])
