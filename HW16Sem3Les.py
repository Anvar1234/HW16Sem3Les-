# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 3-> 1

# Вариант 1. Решение, используя список counter, сформированный как часть решения в методе сортировки подсчетом
# import random
# n = int(input("Введите кол-во элементов списка: "))
# #x = int(input("Введите искомое число: "))
# list_5 = []*n

# # list_5 = [5, 1, 3, 2, 1, 0, 0, 1]
# for i in range(n):
#     list_5.append(random.randint(0,5))
# print(list_5)

# size = len(list_5)
# max = list_5[0]

# for i in range(1,size):
#     if list_5[i] > max:
#         max = list_5[i]
# counter = [0]*(max + 1)
# #print(max)

# for i in range(size):
#     counter[list_5[i]] += 1
# #print(counter)
# x = int(input("Введите искомое число: "))
# print(f"Число {x} встречается {counter[x]} раз(-а)")

# # index = 0
# # for i in range(max + 1):
# #     for j in range(counter[i]):
# #         list_5[index] = i
# #         index += 1
# # print(list_5)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Вариант 2.

# import random
# n = int(input("Введите кол-во элементов списка: "))
# list_5 = []

# for i in range(n):
#     list_5.append(random.randint(0,5))
# print(list_5)

# x = int(input("Введите искомое число: "))
# count_x = 0
# for i in list_5:
#     if x == i:
#         count_x +=1

# print(f"Число {x} встречается {count_x} раз(-а)")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример: *
# 5
# 1 2 3 4 5
# 6 -> 5

import random
n = int(input("Введите кол-во элементов списка: "))
list_5 = []

for i in range(n):
    list_5.append(random.randint(0, 5))
print(list_5)

x = int(input("Введите искомое число: "))

temp = list_5[0]
# нужно найти самую минимальную разность между элементами массива и k
raznost = abs(x - list_5[0])

for i in range(n):
    if (abs(x - list_5[i])) < raznost: 
        raznost = abs(x - list_5[i])
        temp = list_5[i]

print(f"Первый ближайший к числу {x} по величине элемент списка= {temp}")
