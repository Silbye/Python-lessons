import os
os.system('cls')

from import_export import import_data
from import_export import export_data
from print_data import print_data

def choose_separate():
    separate = input("Enter separator (,) (;) (:) ():")
    if separate == "":
        separate = None
    return separate

def input_data():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    commentary = input("Enter commentary: ")
    return [surname, name, phone_number, commentary]

def select():
    data = ''
    program_working = True
    while program_working == True:    
        print("Options:\n\
        1 - Print;\n\
        2 - Add;\n\
        3 - Import;\n\
        4 - Export;\n\
        5 - Exit.")
        ch = input("Enter number: ")
        if ch == '1':
            print_data(data)
        elif ch == '2':
            data = input_data()
        elif ch == '3':
            data = import_data()
        elif ch == '4':
            export_data(data, choose_separate())
        elif ch == '5':
            print("Goodbye!")
            program_working = False
        else:
            print("Incorrect input!")