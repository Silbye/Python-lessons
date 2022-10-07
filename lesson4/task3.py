import os
import random
os.system('cls')

l1 = []

def fill_list(list):
    rand = random.randint(2, 15)
    for i in range(rand):
        list.append(random.randint(1, 10))
    return list

def find_unique(list):
    unique = []
    for i in range(1, 11):
        count = 0
        for number in list:
            if number == i:
                count += 1
        if count == 1:
            unique.append(i)
    return unique

print(fill_list(l1))
print(find_unique(l1))