# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input('Введите число N: '))

degree = 0
number = 2
result = 0

while result <= n:
    result = number ** degree
    print(f'2 в степени {degree} = {result}')
    degree += 1
