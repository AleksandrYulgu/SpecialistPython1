# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
number_list = []

while first_number <= second_number:
    if first_number % 3 == 0:
        number_list.append(first_number)
    first_number += 1

print(number_list)
