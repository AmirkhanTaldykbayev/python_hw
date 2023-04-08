# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

chocolateLength = 3
chocolateWidth = 2
slice = 4

if (slice < chocolateLength * chocolateWidth) and ((slice % chocolateLength == 0) or (slice % chocolateWidth == 0)):
    print('Шоколадку можно разделить на два прямоугольника')
else:
    print('Шоколад нельзя разделить на два прямоугольника')