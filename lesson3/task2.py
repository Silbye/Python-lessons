import os
import random
os.system('cls')

l1 = []

def fill_list(list):
    rand = random.randint(1, 10)
    for i in range(rand):
        list.append(random.randint(0, 10))
    return list

def find_pairs_product(list):
    l2 = []
    i = 0
    j = -1
    while i < len(list)/2:
        l2.append(list[i]*list[j])
        i+=1
        j-=1
    return l2

print(fill_list(l1))
print(find_pairs_product(l1))