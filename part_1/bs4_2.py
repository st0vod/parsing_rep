import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Допишите поиск и извлечение email
    emails = soup.select('.student .email_field strong')

    return [email.next_sibling.strip() for email in emails]




response = requests.get('https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'

print(get_html(response.text))




