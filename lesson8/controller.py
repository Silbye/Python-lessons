import os
os.system('cls')

from hometask import *
from scheudule import *

def mode_select():
    mode = 0
    mode_selected = False
    while mode_selected == False:
        print("Are you a teacher or a student?\n\
            1 - Student\n\
            2 - Teacher")
        mode = int(input())
        if mode == 1 or mode == 2:
            mode_selected = True
    return mode

def main_menu():
    mode = mode_select()
    program_working = True
    while program_working == True:
        print("Options:\n\
        1 - Scheudule;\n\
        2 - Hometask;\n\
        3 - Exit.")
        ch = input("Enter Number: ")
        if ch == '1':
            scheudule_menu(mode)
        elif ch == '2':
            task_menu(mode)
        elif ch == '3':
            print("Goodbye!")
            program_working = False
        else:
            print("Incorrect input!")