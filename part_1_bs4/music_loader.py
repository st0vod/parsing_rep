import requests
import random
import time
import lxml
import re

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


def song_loader(page):
    music_card = str(page.select('.tracks__list'))
    songs = re.findall(r'href="(\S+\.mp3)"', music_card)

    for song in songs:
        ua = UserAgent(min_percentage=4)
        fake_ua = {'User-Agent': ua.random}
        response_2 = requests.get(song, headers=fake_ua, proxies=proxy, stream=True, timeout=10)
        name = re.sub(r'(https://rus.hitmotop.com/get/music/\d+/)', '', song)
        print(name)
        with open(fr'C:\Users\Стас\Music\test\{name}', 'wb') as f1:
            for chunk in response_2.iter_content(chunk_size=1024 ** 2):
                f1.write(chunk)
        time.sleep(1) # задержка на скачу 3 секунды


if __name__ == '__main__':

    url = "https://rus.hitmotop.com/search?q=linking%20park"
    session = requests.Session()

    try:
        headers = {'User-Agent': random.choice(user_agents)}

        proxy = random.choice(proxies)

        response = session.get(url, headers=headers, proxies=proxy, timeout=5)

        soup = BeautifulSoup(response.text, 'lxml')



        song_loader(soup)
    except EOFError as err:
        print(f'Stop parsing, ERROR: {err}')
    except KeyboardInterrupt as stop:
        print('Преждевременная остановка программы')