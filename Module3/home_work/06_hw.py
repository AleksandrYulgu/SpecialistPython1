# Данные о товарах на складе хранятся в словаре
from typing import Dict, List, Union

items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")
brand_list = []
for i in items:
    brand_list.append(i.get("brand"))
print (", ".join(set(brand_list)))

print("На складе больше всего товаров брэнда(ов): ")

brand_list = []
counts = []
best_list = []
for i in items:
    brand_list.append(i.get("brand"))
    for j in brand_list:
        cou = brand_list.count(j)
        counts.append(cou)
        if max(counts) == brand_list.count(j):
            best_list.append(j)
print(", ".join(set(best_list)))




print("На складе самый дорогой товар брэнда(ов): ")
# Вариант 1 он быстрый, но выдает только 1 первый ответ
#cost_list = []
#for j in items:
#    cost_list.append(j["price"])# создаем список со всеми ценами
#id = cost_list.index(max(cost_list)) #узнаем индекс списка где максимальная цена

#print(items[id]["brand"])

#Вариант 2 медленный, но выдает все ответы
brand_list = []
price_list = []
for i in items:
    brand_list.append(i.get("price"))
    for k in brand_list:
        price_list.append(k)
    max_price = max(price_list)
for a in items:
    if a["price"] == max_price:
        print(a["brand"])
