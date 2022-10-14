import os
os.system('cls')

# Урок 2 Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print("Old code\n")

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

print("\nNew code\n")

num = float(input("Enter number: "))
print("Digits sum is:", sum(map(int, str(num).replace('.', ''))))