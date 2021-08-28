# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    return str(number) == str(number)[::-1]


a = 25
b = 55
def created_list (a, b):
    list = []
    while a <= b:
        list.append(a)
        a += 1
    return list

def sum_palindrom():
    sum = 0
    for num in (created_list(a, b)):
        if palindrome(num):
            sum +=1
    return sum

print(sum_palindrom())
