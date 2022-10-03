import os
os.system('cls')

N = int(input("Enter N: "))

def find_fibonacci(n):
    if n > -1:
        if n == 0 or n == 1:
            return n
        else:
            return find_fibonacci(n-1) + find_fibonacci(n-2)
    if n <= -1:
        return (((-1) ** ((abs(n)+1))) * find_fibonacci(abs(n)))

for i in range(-N, N+1):
    print(find_fibonacci(i), end = ' ')