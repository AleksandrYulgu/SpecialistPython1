# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for i in numbers:
    if i > 0 and int(i**0.5) == i**0.5:
        new_list.append(int(i**0.5))
print(new_list)
