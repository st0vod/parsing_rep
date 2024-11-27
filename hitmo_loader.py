import requests
import re
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agents = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')

proxies = [{"http": "http://143.110.226.180:8888"},
           {"http": "http://222.252.194.29:8080"},
           {"http": "http://113.160.133.32:8080"},
           {"http": "http://15.235.153.57:8089"},
           ]

session = requests.Session()

url = input('Укажите ссылку:')
user_path = input('Укажите путь куда сохранить песни:')
try:
    # https://rus.hitmotop.com/search/start/48?q=sabaton
    # https://rus.hitmotop.com/genre/39/start/48
    i = 0

    while True:
        if i == 0:
            response = session.get(url, timeout=10)
        elif 'search' in url:
            response = session.get(f'https://rus.hitmotop.com/search/start/{i}{re.search(r'\?q=.+', url)}', timeout=10)
        elif 'genre' in url:
            response = session.get(f'{url}/start/{i}', timeout=10)
        else:
            raise EOFError("Can't find href...")

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            music_card = str(soup.select('.tracks__list'))

            song = re.search(r'href="(\S+\.mp3)"', music_card).group().replace('href=', '').strip('"')

            ua = UserAgent(min_percentage=4)
            fake_ua = {'User-Agent': ua.random}
            response_2 = requests.get(song, headers=fake_ua, proxies={"http": "http://143.110.226.180:8888"}, stream=True, timeout=10)

            name = re.sub(r'(https://rus.hitmotop.com/get/music/\d+/)', '', song)
            print(name)
            path = f'{user_path}\\{name}'

            with open(path, 'wb') as f1:
                for chunk in response_2.iter_content(chunk_size=1024 ** 2):
                    f1.write(chunk)
            print(f'{i + 1}. {path} скачено')
            i += 1
            time.sleep(2)
        else:
            print('Download finished')
            break

except EOFError as err:
    print(f'Stop parsing, ERROR: {err}')
except KeyboardInterrupt:
    print(f'Program stopped')