import requests

url = 'https://parsinger.ru/4.6/1/res.json'

response = requests.get(url=url).json()
categories = {}

for item in response:

    card = int(item["description"]["rating"]) * int(item["article"])
    categories[item["categories"]] = categories.get(item["categories"], 0) + card

print(categories)




