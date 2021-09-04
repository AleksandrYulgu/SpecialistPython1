# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random
def gen_list(n, m=-10, k=30):
    list = []
    for _ in range(10):
        list.append(random.randint(m, k))
    return list

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = [1 , 2, 4, 5, 6, 2, 5, 2]

def short_list(lst2):
    new_list = []
    for num in set(lst2):
        if lst2.count(num) == 1:
            new_list.append(num)
    return new_list

print(set(lst))
print(short_list(lst2))
