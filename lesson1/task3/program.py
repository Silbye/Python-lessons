import os
os.system('cls')
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
if x == 0 or y == 0:
    print("Invalid X or Y")
elif x > 0 and y > 0:
    print("1st quarter")
elif x > 0 and y < 0:
    print("4th quarter")
elif x < 0 and y < 0:
    print("3rd quarter")
else:
    print("2nd quarter")