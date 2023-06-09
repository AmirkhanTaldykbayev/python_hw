# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве
# внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

number_of_bushes = 7  # int(input('Введите кол-во кустов: '))

bushes = [random.randint(1, 8) for _ in range(1, number_of_bushes)]
print(bushes)
best_harvest = 0

for i in range(len(bushes) * 2):
    size = len(bushes)
    left = bushes[i % size - 3]
    middle = bushes[i % size - 2]
    right = bushes[i % size - 1]
    triple = left + middle + right
    left_2 = bushes[i % size - 2]
    middle_2 = bushes[i % size - 1]
    right_2 = bushes[i % size]
    second_triple = left_2 + middle_2 + right_2
    if triple < second_triple:
        best_harvest = second_triple


print(best_harvest)
