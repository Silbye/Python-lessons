import os
os.system('cls')

N = str(input("Enter your PI accuracy: "))

def find_digits(N):
    if '.' in N:
        return abs(N.find('.') - len(N)) - 1
    else:
        return 0

def find_pi(N):
    k = 1
    x = 0
    i = int(N)
    for k in range(1, 10000000):
        x = x+4*((-1)**(k+1))/(2*k-1)
    return float("%0.*f" % (i, x))
print(find_pi(find_digits(N)))