import os
os.system('cls')

def print_data(data):
    if len(data) > 0:
        for info in data:
            print(f"{info}")
    else:
        print("The list is empty!")