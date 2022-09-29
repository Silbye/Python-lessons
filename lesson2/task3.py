import os
os.system('cls')

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