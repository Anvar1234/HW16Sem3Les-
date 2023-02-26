# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 3-> 1

import random
n = int(input("Введите кол-во элементов списка: "))
#x = int(input("Введите искомое число: "))
list_5 = []*n

# list_5 = [5, 1, 3, 2, 1, 0, 0, 1]
for i in range(n):
    list_5.append(random.randint(0,5+1))
print(list_5)

size = len(list_5)
max = list_5[0]

for i in range(1,size):
    if list_5[i] > max:
        max = list_5[i]
counter = [0]*(max + 1)
#print(max)

for i in range(size):
    counter[list_5[i]] += 1
#print(counter)
x = int(input("Введите искомое число: "))
print(f"Число {x} встречается {counter[x]} раз(-а)")

# index = 0
# for i in range(max + 1):
#     for j in range(counter[i]):
#         list_5[index] = i
#         index += 1
# print(list_5)