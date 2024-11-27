import requests

url = 'https://catalog.wb.ru/catalog/electronic22/v2/catalog?ab_testing=false&appType=1&curr=rub&dest=-1257786&page=1&sort=popular&s'

response = requests.get(url=url).json()
for item in response:
    #print(item["data"]["products"]["name"], item["data"]["products"]["sizes"]["price"]["product"])
    print(item)