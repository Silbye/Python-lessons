from cgi import print_arguments
import os
import random
os.system('cls')

def make_mnog(k):
    if k > 5:
        print("k is too big")
    else:
        coefficient = [random.randint(-100, 100) for i in range(k)]+[random.randint(-100, 100)]
        mnog='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(coefficient) if j][::-1])
        mnog=mnog.replace('x^1+', 'x+')
        mnog=mnog.replace('x^0', '')
        mnog=mnog.replace('+-', '-')
        mnog+=('', '1')[mnog[-1]=='+']
        mnog=(mnog, mnog[:-2])[mnog[-2:]=='^1']
        mnog+=' = 0'
    return mnog

mnog1 = make_mnog(int(input("Enter k (maximum is 5): ")))
print(mnog1)

with open('lesson4/mnog1.txt', 'w') as file:
    file.write(mnog1)
    file.close()

mnog2 = make_mnog(int(input("Enter k (maximum is 5): ")))
print(mnog2)

with open('lesson4/mnog2.txt', 'w') as file2:
    file2.write(mnog2)
    file2.close()