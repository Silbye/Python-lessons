import os
os.system('cls')

# Урок 2 Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.

print("Old code\n")

N = int(input("Enter N: "))
numberSequence = []

def fill_sequence_list(N):
    num = 0
    for i in range(1, N+1):
        num = (1+(1/i))**(i)
        numberSequence.append(str(num))
    return numberSequence
print(fill_sequence_list(N))

def find_summ(numberSequence):
    sum = 0
    for i in numberSequence:
        i = float(i)
        sum += i
    return round(sum, 3)
print(find_summ(numberSequence))

print("\nNew code\n")

N = int(input("Enter N: "))
l2 = [(1+(1/i))**(i) for i in range(1, N+1)]
summ = round(sum(l2), 3)
print(f"{l2}\n{summ}")