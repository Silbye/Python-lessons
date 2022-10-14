import os
os.system('cls')

# Урок 2 Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print("Old code\n")

N = int(input("Enter N: "))
products = []

def find_products(N):
    product = 1
    if N == 0:
        products.append(1)
    else:
        for i in range(1, N+1):
            product*=i
            products.append(product)
    return products
print(find_products(N))

print("\nNew code\n")

N = int(input("Enter N (higher than 0): "))
fact = list(map(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n), range(1, N+1)))
print(fact)