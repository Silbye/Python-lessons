import os
import random
os.system('cls')

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
