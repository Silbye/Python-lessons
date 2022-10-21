import os
os.system('cls')

from print_data import print_data

def import_data():
    with open('lesson8/scheudule.csv', 'r') as file:
        return file.read()

def scheudule_menu(mode):
    data = ''
    menu_open = True
    while menu_open == True:
        print("Options:\n\
        1 - Open scheudule file;\n\
        2 - Show shceudule;\n\
        3 - Add new scheudule;\n\
        4 - Exit.")
        ch = input("Enter number: ")
        if ch == '1':
            data = import_data()
        elif ch == '2':
            print_data(data)
        elif ch == '3' and mode == 2:
            add_scheudule()
        elif ch == '3' and mode == 1:
            print("You dont have rights to do this!")
        elif ch == '4':
            menu_open = False
        else:
            print("Incorrect input!")

def add_scheudule():
    data = ''
    confirmed = False
    with open('lesson8/scheudule.csv', 'w') as file:
        data = input("Enter the day's scheudule: ")
        print(f"Today's scheudule: {data}")
        while confirmed == False:
            ch = input("Are you sure you want to overwrite the scheudule? (Y/N)")
            if ch == 'Y' or ch == 'y':
                file.write(data)
                confirmed = True
            elif ch == 'N' or ch == 'n':
                data = ''
                confirmed = True
            else:
                print("Incorrect input!")