# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Введите количество монеток: '))

current_coin = 0
emblem = 1
tails = 0
index = 0
count_emblem = 0
count_tails = 0


while index < n:
    current_coin = random.randint(0, 1)
    if current_coin == emblem:
        count_emblem += 1  
    else:
        count_tails += 1
    print(current_coin)
    index += 1
if count_emblem < count_tails:
    print(f'Нужно перевернуть {count_emblem} монеток, чтобы все монетки были повернуты вверх одной и той же стороной')
else:
    print(f'Нужно перевернуть {count_tails} монеток, чтобы все монетки были повернуты вверх одной и той же стороной')

