from bs4 import BeautifulSoup
import requests
import lxml
import re


response = requests.get('https://parsinger.ru/4.3/4/index.html', timeout=10)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

all_p = soup.find_all('p')

sum_id_class = 0

for p in all_p:
    if len(p.text.replace(' ', '')) % 2 == 0:
        sum_id_class += sum(map(int, (p['id'], *p['class'])))

print(sum_id_class)