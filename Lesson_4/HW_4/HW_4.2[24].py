# 4.2[24]: В фермерском хозяйстве в Карелии
# выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по
# окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке
# растет N кустов. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух
# соседних с ним.
# Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом.
# На входе задано количество ягод на каждом кусте.
# Не обязательно вводить их с клавиатуры, можно
# задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

# Кусты на окружности. По итогу надо выдать номер куста и сумму центрального и соседних
# № Куста:     1   2   3   4   5   6   7   8
num_berries = [1, 2, 3, 4, 5, 6, 7, 8]

count_bush = len(num_berries)

sum_berries = []

# Поставил условия на начало и конец циклв, чтобы из него невыпасть и посчитать значения
for idx in range(count_bush):
    if idx == 0:
        sum_berries.append(sum(num_berries[:idx+2]) + num_berries[-1])
    elif idx == count_bush-1:
        sum_berries.append(sum(num_berries[idx-1:idx+1]) + num_berries[0])
    else:
        sum_berries.append(sum(num_berries[idx-1:idx+2]))
    
    print(f"{idx+1}-куст = {sum_berries[idx]}")

max_berries = max(sum_berries)

print(f"Макс. кол-во ягод {max_berries}, собрано с куста № {sum_berries.index(max_berries)+1}")
