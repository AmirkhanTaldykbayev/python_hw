# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Введите количество элементов в массиве: '))
x_number = int(input('Введите искомое число: '))

list_1 = [random.randint(1,100) for i in range(1, n + 1)]
print(list_1)

upper = max(list_1)
lower = min(list_1)

for i in list_1:
    if i >= lower and i <= x_number:
        lower = i
    if i <= upper and i >= x_number:
        upper = i

if (x_number - lower) > (upper - x_number):
    print(f'Число {upper} ближе всего к числу {x_number}')
elif (x_number - lower) < (upper - x_number):
    print(f'Число {lower} ближе всего к числу {x_number}')
else:
    print(f'Число {x_number} присутствует в списке')