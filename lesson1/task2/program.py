import os
os.system('cls')
print('x y z f')
for x in range (2):
    for y in range (2):
        for z in range (2):
            f = not(x or y or z) == (not x and not y and not z)
            if f == True:
                f = 1
            else:
                f = 0
            print (x,y,z,f)