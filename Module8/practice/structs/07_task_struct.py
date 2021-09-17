# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).

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


def data_for_test(name, surname, job):

    def uni_name(name, surname):
        uni_list_name = []
        for el in set(name):
            for el2 in set(surname):
                el3 = f'{el} {el2}'
                uni_list_name.append(el3)
        return uni_list_name

    unic_list_name = list(uni_name(name, surname))

    for name in unic_list_name:
        uniname = name.split()
        unijob = random.choice(job)
        salary = random.randint(22000, 120000)
        age = random.randint(20, 65)
        yield f'Имя - {uniname[0]}\nФамилия - {uniname[1]}\nВозраст - {age}\nПрофессия - {unijob}\nЗарплата - {salary}\n'
        print( f'Имя - {uniname[0]}\nФамилия - {uniname[1]}\nВозраст - {age}\nПрофессия - {unijob}\nЗарплата - {salary}\n')


string = list(data_for_test(names, surnames, jobs))
with open('data_baz2.txt', 'w', encoding='utf-8') as f:
    for el in string:
        f.write(f'{str(el)}\n')
