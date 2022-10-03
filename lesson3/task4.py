import os
os.system('cls')

n = int(input())

def convert_to_binary(number):
    b_num = ''
    while number > 0:
        b_num = str(number%2) + b_num
        number = number // 2
    return int(b_num)
print(convert_to_binary(n))