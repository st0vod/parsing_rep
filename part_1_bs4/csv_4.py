import requests
import csv
from bs4 import BeautifulSoup

headers = 'Наименование;Артикул;Бренд;Модель;Тип;Технология экрана;Материал корпуса;Материал браслета;Размер;Сайт производителя;Наличие;Цена;Старая цена;Ссылка на карточку с товаром'


def writing_csv(*args) -> None:
    """Функиця добавляет запись в .csv файл"""
    with open('watches.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(*args)


schema = 'https://parsinger.ru/html/'
writing_csv(headers.split(';'))

for i in range(1, 5):

    url_current = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url_current)
    soup = BeautifulSoup(response.content, 'html.parser')

    for card in soup.select('.sale_button > a'):
        card_url = schema + card['href']

        card_response = requests.get(card_url)
        card_soup = BeautifulSoup(card_response.content, 'html.parser')
        card_discription = card_soup.find('div', class_='description')

        name = card_discription.find("p", id="p_header").text
        article = card_discription.find(class_="article").text.split(": ")[1].strip()

        values = [value.text.split(': ')[1] for value in card_discription.find_all('li')]
        in_stock = card_discription.find(id="in_stock").text.split(": ")[1]

        prices = card_soup.find('div', class_='sale')

        price = prices.find(id="price").text
        old_price = prices.find(id="old_price").text

        writing_csv([name, article, *values, in_stock, price, old_price, card_url])