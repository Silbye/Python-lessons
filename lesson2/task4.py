import os
os.system('cls')

N = int(input("Enter N: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

N_sequence = []

def fill_sequence(N):
    for i in range(-N, N+1):
        N_sequence.append(i)
    return N_sequence
print(fill_sequence(N))

def find_product(N_sequence, a, b):
    product = 0
    product = N_sequence[a-1] * N_sequence[b-1]
    return product
print(find_product(N_sequence, a, b))