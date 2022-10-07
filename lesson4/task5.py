from asyncore import read
from cgi import print_arguments
import os
import re
os.system('cls')

file1 = 'lesson4/mnog1.txt'
file2 = 'lesson4/mnog2.txt'
sum_file = 'lesson4/mnogsum.txt'

def read_file(file):
    with open(str(file), 'r') as data:
        mnog = data.read()
    return mnog

def write_file(file, mnog):
    with open(file, 'w') as data:
        data.write(mnog)

def find_coeffs(mnog):
    mnog = mnog.replace('x^5', ' ')
    mnog = mnog.replace('x^4', ' ')
    mnog = mnog.replace('x^3', ' ')
    mnog = mnog.replace('x^2', ' ')
    numbers = re.compile('-?\d+')
    numbers = list(map(int, numbers.findall(mnog)))
    numbers.pop()
    return numbers

def mnog_sum(mnog1, mnog2, mnog1_len, mnog2_len):
    bigger = len(mnog2)
    if len(mnog1) > len(mnog2): bigger = len(mnog1)
    max_range = max(mnog1_len, mnog2_len)
    results = [0] * (max_range)
    for j in range(0, bigger):
        if len(mnog1) < len(mnog2): mnog1 = [0] + mnog1
        if len(mnog2) < len(mnog1): mnog2 = [0] + mnog2
    for index in range(len(mnog1)):
        results[index] = mnog1[index]
    for index in range(len(mnog2)):
        results[index] += mnog2[index]
    return results

def write_sum(k, mnog_sum):
    mnog_sum.reverse()
    coefficient = [mnog_sum[i] for i in range(k)]
    mnog='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(coefficient) if j][::-1])
    mnog=mnog.replace('x^1+', 'x+')
    mnog=mnog.replace('x^0', '')
    mnog=mnog.replace('+-', '-')
    mnog+=('', '1')[mnog[-1]=='+']
    mnog=(mnog, mnog[:-2])[mnog[-2:]=='^1']
    mnog+=' = 0'
    return mnog

mnog1 = find_coeffs(read_file(file1))
mnog2 = find_coeffs(read_file(file2))

print(mnog1)
print(mnog2)

summ = mnog_sum(mnog1, mnog2, len(mnog1), len(mnog2))
k = len(summ)
sum = write_sum(k, summ)

print(sum)
write_file(sum_file, sum)
