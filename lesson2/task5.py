from imghdr import what
import os
import random
os.system('cls')

N = int(input("Enter list size: "))
whatever_list = []

def fill_list(N):
    for i in range(N):
        whatever_list.append(str(input("Enter list member: ")))
    return whatever_list
print(fill_list(N))

def shuffle_list(whatever_list, N):
    temp = ''
    for i in range(N-1):
        index = random.randint(0, N-1)
        temp = whatever_list[i]
        whatever_list[i] = whatever_list[index]
        whatever_list[index] = temp
    return whatever_list
print(shuffle_list(whatever_list, N))