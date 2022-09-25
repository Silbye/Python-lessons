import os
os.system('cls')
day = int(input("Enter day number: "))
if day == 6 or day == 7:
    print("Your day is weekend")
elif day < 1 or day > 7:
    print("There is no such day")
else:
    print("Your day is not weekend")