# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

length_of_list_1 = 10 #int(input('Введите кол-во элементов первого множества: '))
length_of_list_2 = 10 #int(input('Введите кол-во элементов второго множества: '))

list_1 = {random.randint(1, 20) for _ in range(length_of_list_1)}
list_2 = {random.randint(1, 20) for _ in range(length_of_list_2)}

print(list_1)
print(list_2)

full = list_1.union(list_2)
print(full)

# list_3 = set()

# for i in list_2:
#     for m in list_1:
#         if m not in list_2:
#             list_3.add(m)
#     list_3.add(i)
# print(list_3)