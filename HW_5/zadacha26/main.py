# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(num, pow):                    # def power(3, 5)
    if pow == 1:                        # условие выхода из рекурсии
        return num                      # число, возведенное в степень
    return num * power(num, pow - 1)    # num(3) * power(num(3), pow(5 - 1); num = 9, pow = 4
                                        # num(9) * power(num(3), pow(4 - 1)); num = 27, pow = 3
                                        # num(27) * power(num(3), pow(3 - 1)); num = 81, pow = 2
                                        # num(81) * power(num(3), pow(2 - 1); num = 243, pow = 1(выход из рекурсии)


number = int(input('Введите число: '))
degree = int(input('Введите степень: '))

print(power(number, degree))
