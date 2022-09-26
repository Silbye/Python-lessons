import os
os.system('cls')
quarter = int(input("Enter your quarter: "))
if quarter < 1 or quarter > 4:
    print("Invalid data")
elif quarter == 1:
    print("x > 0 and y > 0")
elif quarter == 2:
    print("x < 0 and y > 0")
elif quarter == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 and y < 0")