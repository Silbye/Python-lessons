import os
os.system('cls')
xa = int(input("Enter xa: "))
xb = int(input("Enter xb: "))
ya = int(input("Enter ya: "))
yb = int(input("Enter yb: "))
A = float((xa-ya)**(2))
B = float((xb-yb)**(2))
d = A+B
distance = d**(0.5)
distance = int(distance*100)/100
print(distance)