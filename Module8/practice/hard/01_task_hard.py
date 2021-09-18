# "Банкомат"
# В банкомате есть купюры 5000, 2000, 1000 и 500 рублей.
# Напишите функцию, которая будет рассчитывать количество купюр, которыми можно будет выдать
# запрошенную пользователем сумму и возвращать ее в виде словаря, ключами в котором будут номиналы банкнот,
# а значениями кол-во банкнот. Если пользователь запросил некорректную сумму,
# нужно вывести дружественное сообщение об ошибке.
# Результат работы программы - текстовый отчет о номиналах и количестве купюр.


try:
    give_out = int(input('Введите, какую сумму выдать: '))
except ValueError:
    print('Введите сумму цифрами')
    give_out = int(input('Введите, какую сумму выдать: '))


def count_bills(summ):
    count_5000 = summ//5000
    count_2000 = (summ - 5000*count_5000)//2000
    count_1000 = (summ - (5000*count_5000+2000*count_2000))//1000
    count_500 = (summ - (5000*count_5000 + 2000*count_2000 + 1000*count_1000))//500
    remainder = summ - (5000*count_5000 + 2000*count_2000 + 1000*count_1000 + 500*count_500)
    lst_bils = ("Купюра 5000 ", "Купюра 2000 ", "Купюра 1000 ", "Купюра 500 ")
    lst_count = []
    while True:
        if remainder == 0:
            lst_count.append(count_5000)
            lst_count.append(count_2000)
            lst_count.append(count_1000)
            lst_count.append(count_500)
            print (create_dict_bills(lst_bils, lst_count))
            break

        else:
            print("Сумма запрашиваемая Вами не может быть выдана. Введите сумму кратную 500 рублей.")
            give_out = int(input('Введите, какую сумму выдать: '))
            count_bills(give_out)
            break


def create_dict_bills(lst1, lst2):
    return dict(zip(lst1, lst2))

count_bills(give_out)
