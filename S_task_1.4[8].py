# 1.4[8]. Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Дольки по вертикали = "))
m = int(input("Дольки по горизонтали = "))
k = int(input("Сколько отломить? = "))

# Сначала проверка на то что k не превышает колличество долек
# Далее проверяем можно ли разбить ровным прямоугольником
if k <= n * m and (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")
