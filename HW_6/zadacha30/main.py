# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
element = 7 #int(input('Введите число: '))
diff = 2 #int(input('Введите разность: '))
quantity = 5 #int(input('Введите количество элементов: '))

my_list = []

for i in range(quantity):
    my_list.append(element + i * diff)

print(my_list)