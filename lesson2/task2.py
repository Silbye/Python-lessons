import os
os.system('cls')

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

