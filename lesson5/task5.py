import os
os.system('cls')

l = [1, 5, 2, 3, 4, 6, 1, 7]

def get_succession(l):
    all_successions = []
    for i in range(len(l)):
        suc = []
        j = i
        current = 0
        while j < len(l):
            if l[j] > current: 
                suc.append(l[j])
                current = l[j]
            j += 1
        if len(suc) == 1:
            continue
        else:
            all_successions.append(suc)
    return all_successions
print(get_succession(l))