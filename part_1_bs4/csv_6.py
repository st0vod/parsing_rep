import csv
import requests
from bs4 import BeautifulSoup

schema = 'https://parsinger.ru/html/'
url = 'https://parsinger.ru/html/index1_page_1.html'


def my_requests(u: str):
    response = requests.get(u)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


main_urls = [schema + url['href'] for url in my_requests(url).select(' div.nav_menu a')]

with open('finall2.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    for i in range(len(main_urls)):
        pages = [schema + page['href'] for page in my_requests(main_urls[i]).select_one('.pagen').select('a')]

        for j in range(len(pages)):
            soup = my_requests(pages[j])

            for card in soup.select('.sale_button > a'):
                card_soup = my_requests(schema + card['href'])
                card_discription = card_soup.find('div', class_='description')

                name = card_discription.find("p", id="p_header").text
                article = card_discription.find(class_="article").text.split(": ")[1].strip()

                values = [value.text.split(': ')[1] for value in card_discription.find_all('li')]
                in_stock = card_discription.find(id="in_stock").text.split(": ")[1]

                prices = card_soup.find('div', class_='sale')
                price = prices.find(id="price").text
                old_price = prices.find(id="old_price").text


                names = [name.text.strip() for name in soup.find_all('a', class_='name_item')]
                descriptions = [desc.text.strip().split('\n') for desc in soup.find_all('div', class_='description')]
                prices = [price.text for price in soup.find_all('p', class_='price')]

                for name, desc, price in zip(names, descriptions, prices):
                    desc = [d.split(': ')[1] if ':' in d else d for d in desc]
                    writer.writerow([name, *map(str.strip, desc), price])
