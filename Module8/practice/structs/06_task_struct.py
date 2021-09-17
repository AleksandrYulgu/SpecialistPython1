# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться

import random

names = ['Иван', 'Петр', 'Василий', 'Инокентий', 'Агафон', 'Илларион']
surnames = ['Иванов', 'Петров', 'Путин', 'Козлов', 'Петухов', 'Собакевич']
jobs = ['Директор', 'Програмист', 'Менеджер', 'Дворник', 'Плотник', 'Стажер']


def data_for_test(name, surname, job, ranges):
    for _ in range(ranges):
        unijob = random.choice(job)
        salary = random.randint(22000, 120000)
        age = random.randint(20, 65)
        yield f'Имя - {random.choice(name)}\nФамилия - {random.choice(surname)}\nВозраст - {age}\nПрофессия - {unijob}\nЗарплата - {salary}\n'
        print(f'Имя - {random.choice(name)}\nФамилия - {random.choice(surname)}\nВозраст - {age}\nПрофессия - {unijob}\nЗарплата - {salary}\n')

string = list(data_for_test(names, surnames, jobs, 100))

with open('data_baz.txt', 'w', encoding='utf-8') as f:
    for el in string:
        f.write(f'{str(el)}\n')
