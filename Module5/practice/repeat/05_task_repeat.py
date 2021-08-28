
# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.
import math

def pagination(num_items, items_on_page):
    num_page = math.ceil(num_items / items_on_page)
    return num_page

def count_items (num_items, items_on_page):

    return num_items - (pagination(num_items, items_on_page)-1)*items_on_page

print(count_items(11, 6))
