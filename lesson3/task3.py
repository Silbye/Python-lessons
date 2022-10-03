import os
import random
from sys import flags
os.system('cls')

l1 = []
def fill_list(list):
    rand = random.randint(1, 5)
    for i in range(rand):
        list.append(float(input("Enter Number: ")))
    return list

def find_fraction_difference(list):
    for i in range(len(list)):
        list[i] = list[i]%1
    maximum = list[0]
    minimum = list[0]
    diff = 0
    for i in range(len(list)):
        if list[i] == 0.0:
            continue
        if minimum == 0.0:
            minimum = list[i]
        if list[i] > maximum:
            maximum = list[i]
        if list[i] < minimum:
            minimum = list[i]
    print(maximum, minimum)
    diff = maximum - minimum
    return round(diff, 3)
    
print(fill_list(l1))
print(find_fraction_difference(l1))