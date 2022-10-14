import os
import random
os.system('cls')

# Урок 3 Задание 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

print("Old code\n")

l1 = []

def fill_list(list):
    rand = random.randint(2, 10)
    for i in range(rand):
        list.append(random.randint(0, 10))
    return list

def find_uneven_sum(list):
    sum = 0
    for i in range(len(list)):
        if i == 0:
            continue
        if i % 2 == 1:
            sum+=list[i]
    return sum

print(fill_list(l1))
print(find_uneven_sum(l1))

print("\nNew code\n")

l2 = [random.randint(0, 10) for x in range(random.randint(2,10))]
summ = sum(list(v for i, v in enumerate(l2) if i%2 !=0))
print(f"{l2}\n{summ}")