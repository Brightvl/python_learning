# 2.2[12]: Петя и Катя – брат и сестра. Петя –
# студент, а Катя – школьница. Петя помогает
# Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет
# сумму этих чисел S и их произведение P. Помогите Кате
# отгадать задуманные Петей числа.

#     Примеры/Тесты:
#     4 4 -> 2 2
#     5 6 -> 2 3

# **Примечание.**
# Здесь нужно составить два уравнения. Которые приведут
# к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение -
# посмотрите  в сети. Обойдите дополнительной проверкой
# возможность комплексных решений. Можно игнорировать то,
# что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение
# в степень 0.5 или  ```(*)``` **Усложнение.** найдите
# самостоятельно в сети какая функция стандартной библиотеки
# вычисляет квадратный корень и как до нее добраться.

import math

# X,Y ≤ 1000
# summ - сумма
# mult - произведение

# summ = X+Y
# mult = X*Y

# X = summ - Y
# X = mult/Y

# summ-Y = mult/Y
# (summ-Y)Y = mult

# 0 = -(Y^2) + Y*summ - mult  

# a = -1
# summ = b = int(input("Сумма чисел = "))
# mult = int(input("Произведение чисел = "))
# c = -mult

summ = summ = int(input("Сумма чисел = "))
mult = int(input("Произведение чисел = "))

D = summ**2 - (4*1*mult)  # Дискриминант если = 0, то 1 корень уравнения
if D == 0:
    y = summ/2
    print(f"y = {y}")
    x = summ - y
    print(f"x = {x}")

elif D < 0:
    print("Так как дискриминант меньше нуля, то уравнение не имеет действительных решений.")

else:
    y = (-summ + math.sqrt(D))/2*-1
    print(f"y1 = {y}")
    x = summ - y
    print(f"x1 = {x}")





# D = b**2 - (4*a*c)  # Дискриминант если = 0, то 1 корень уравнения
# if D == 0:
#     y = -b/2*a
#     print(f"y = {y}")
#     x = S - y
#     print(f"x = {x}")

# elif D < 0:
#     print("""Так как дискриминант меньше нуля, то уравнение не имеет действительных решений.""")

# else:
#     y1 = (-b + math.sqrt(D))/2*a
#     print(f"y1 = {y1} y2 = {y2}")
#     x1 = S - y1
#     print(f"x1 = {x1} x2 = {x2}")
