import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

total = 0
for row in soup.find_all('tr')[1:]:
    # r > td:nth-child(15)
    """Селектор находит 15ю дочернюю ячейку строки"""
    mult_temp = row.select_one('tr > td:nth-child(15)')

    # mult_temp = float(row.find('td', class_='orange').text) * float(row.find_all('td')[14].text)
    total += float(mult_temp.string)

print(total)
