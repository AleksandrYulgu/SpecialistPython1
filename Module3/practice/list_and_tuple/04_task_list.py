# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

my_list = [9, 5, -5, 6, -10, 8]
sum = 0
for i in my_list:
    if i > 0:
        sum += i
print(sum)
