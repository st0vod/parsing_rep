import requests
import re

data = []
proxies_dict = {}
url = 'http://httpbin.org/ip'


with open('proxies.txt', 'r', encoding='utf-8') as file1:

    for line in file1.readlines():
        key = re.search(r'http|https|socks4|socks5', line).group()
        ip = line.split()[-1]
        proxies_dict[key] = proxies_dict.get(key, []) +[ip]

with open('proxies_2.txt', 'wt', encoding='utf-8') as file2:
    session = requests.Session()
    number = 1
    for key in proxies_dict.keys():
        for p in proxies_dict[key]:
            if key in ('http', 'https'):
                proxy = {'http:': f'http://{p}',
                         'https': f'https://{p}'}
            else:
                proxy = {'http': f'{key}://{p}',
                         'https': f'{key}://{p}'}

            try:
                response = session.get(url, params=proxy)

                print(f'{number} -----Good connection: {key}://{p}-----')

                file2.write('{"http": "' + key +'://' + p +'", "https": "' + key + '://' + p +'"}\n')

            except OSError as err:
                print(f'{number} -----Bad connection: {key}://{p}-----')
            except Exception as err:
                print(f'Programm mistake: {err}')
                break
            finally:
                number += 1

