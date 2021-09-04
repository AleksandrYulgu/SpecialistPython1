# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

import random
def gen_list(n, m=-10, k=30):
    list = []
    for _ in range(10):
        list.append(random.randint(m, k))
    return list

lst = [1, 2, 14, 5, 16, 2, 5, 2]

count_elem = len(list(filter(lambda x: x<10, lst)))
print(count_elem)

s_positiv = sum(list(filter(lambda x: x>0, lst)))
print(s_positiv)

medium_even = sum(list(filter(lambda x: x%2 == 0, lst)))/len(list(filter(lambda x: x%2 == 0, lst)))
print(medium_even)
