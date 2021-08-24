# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.


def lucky_ticket(ticket_number):
    def sum_number(num):
        return (num //100) + (num //10 % 10) + (num % 100 % 10)

    str1 = int(str(ticket_number)[:3])
    str2 = int(str(ticket_number)[3:])
    return sum_number(str1) == sum_number(str2)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
