import os
os.system('cls')

number = float(input("Enter number: "))

def find_digits_sum(number):
    str_num = str(number)
    str_num = str_num.replace('.', '')
    number = int(str_num)
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return str(sum)
print("Digits sum is: " + find_digits_sum(number))