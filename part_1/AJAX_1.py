import requests
from random import choice
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent(min_percentage=25)

headers = {'user-agent': ua.random,
           'x-requested-with': 'XMLHttpRequest'}
"""
# передаем значения через params
params = {"GiveName": 'Sberbank', "GetName": 'Bitcoin', "Sum": 200000, "Direction": 0}
url = "https://bitality.cc/Home/GetSum?"
response = requests.get(url=url, headers=headers, params=params, proxies={"http": "http://15.235.153.57:8089"}).json()

print(response)

# в писываем значения непосредственно в ссылке
url = "https://bitality.cc/Home/GetSum?GiveName=Sberbank&GetName=Bitcoin&Sum=500000&Direction=0?"
response = requests.get(url=url, headers=headers, params=params, proxies={"http": "http://15.235.153.57:8089"})

print(response.json())
"""

# скрипт на генерирование случайных валют
url = 'https://bitality.cc/Home/'
response = requests.get(url, headers=headers, proxies={"http": "http://15.235.153.57:8089"})

soup = BeautifulSoup(response.text, 'lxml')
# ('span', class_="ml-2 b-choose__item-txt")]


crypts = [value['data-name'] for value in soup.find_all('div', {'data-exchange-ps-type': 'crypto'})]
banks = [value['data-name'] for value in soup.find_all('div', {'data-exchange-ps-type': 'bank'})] + crypts




while True:
    v1 = choice(banks)
    v2 = choice(crypts)
    if v1 == v2:
        continue
    url = f"https://bitality.cc/Home/GetSum?GiveName={v1}&GetName={v2}&Sum=1&Direction=0?"
    response = requests.get(url=url, headers=headers, proxies={"http": "http://15.235.153.57:8089"}).json()

    print(f' {response['giveSum']} {v1} = {response['getSum']} {v2} ')
    sleep(3)