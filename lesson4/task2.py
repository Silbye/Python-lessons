import os
os.system('cls')

N = int(input("Enter N: "))

def find_factors(N):
    i = 2
    factors = []
    while i * i <=N:
        while N % i == 0:
            factors.append(i)
            N = N / i
        i = i + 1
    if N > i:
        factors.append(int(N))
    return factors
print(find_factors(N))