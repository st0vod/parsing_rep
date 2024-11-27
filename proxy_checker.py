import time
import re
import json
import requests
from requests.adapters import HTTPAdapter

session = requests.Session()


def creating_proxy_file(path: str) -> str:
    """Функция обрабатывает .txt файл со списком прокси, убирает всю лишнюю информацию и сохраняет в новом файле
    в виде JSON объекта"""

    print(f'Анализ прокси из файла: {path}')
    proxy_name = f'proxy_{time.localtime().tm_min + time.localtime().tm_sec}.txt'
    if path:

        with open(proxy_name, 'wt', encoding='utf-8') as f1:
            with open(path, 'rt', encoding='utf-8') as f2:

                while True:

                    line = f2.readline()
                    if line:

                        name = re.search('http|socks4|socks5', line).group()
                        ip = re.search(r'(\d{1,3}\.){3}\d{1,3}:\d+', line).group()

                        if name == 'http':
                            ready_line = f'"http": "http://{ip}", "https": "https://{ip}"'
                        else:
                            ready_line = f'"http": "{name}://{ip}", "https": "{name}://{ip}"'
                    else:
                        break

                    f1.write('{' + ready_line + '}\n')
    else:
        print('Файл не найден')

    return proxy_name


def proxy_getter(path: str) -> dict:
    """Генератор берет из файла строку с прокси"""
    with open(path, 'rt') as f:
        while True:
            line = f.readline()
            if line:
                yield json.loads(line)
            else:
                print('Прокси закончились')
                break


def make_request(proxy):
    adapter = HTTPAdapter()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    if not proxy:
        raise IndexError("Список закончился.")
    try:
        response = session.get('https://httpbin.org/get', proxies=proxy, timeout=5)
        print(f'Успех с прокси {proxy}: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Не удалось использовать прокси {proxy}: {str(e)}')
        return False

    return proxy  # Возврат True при успешной попытке


if __name__ == '__main__':

    data = creating_proxy_file('proxies.txt')
    gen_proxy = proxy_getter(data)

    with open('good_proxies.txt', 'a', encoding='utf-8') as finally_file:

        try:
            while True:
                result = make_request(next(gen_proxy))
                if result:
                    finally_file.write(json.dumps(result) + '\n')

        except Exception as err:
            print(err)

    session.close()


