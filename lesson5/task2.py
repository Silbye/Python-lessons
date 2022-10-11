import os
import random
os.system('cls')

def candy_input(player):
    candy = int(input(f"It is {player}'s turn to say the amount of candies they take: "))
    while candy < 1 or candy > 28:
        candy = int(input(f"{player} entered invalid data, please say the proper amount of candies you want to take (1-28): "))
    return candy

def print_data(player, value, candy):
    print(f"{player} took {candy} candies, {value} candies remain")

def mode_selection():
    mode_selected = False
    while mode_selected == False:
        mode = int(input("Single player (0) or Multiplayer (1)? "))
        if mode == 0 or mode == 1:
            mode_selected = True
        else: continue
    return mode

def bot_game():
    player = "Player"
    bot = "Bot"
    valid_value = False
    value = int(input("Enter starting amount of candies (must be at least 30): "))
    while valid_value == False:
        if value >= 30:
            valid_value = True
        else:
            value = int(input("Enter starting amount of candies (must be at least 30): "))
    turn = True
    coinflip = random.randint(0, 2)
    if coinflip == 0: 
        turn = True
        print(f"{player} will start first")
    else: 
        turn = False
        print(f"{bot} will start first")
    while value > 28:
        if turn == True:
            candy = candy_input(player)
            value -= candy
            turn = False
            print_data(player, value, candy)
        else:
            candy = value%29
            if candy == 0: candy += 1
            value -= candy
            turn = True
            print_data(bot, value, candy)
    return turn

def people_game():
    player1 = "Player 1"
    player2 = "Player 2"
    valid_value = False
    value = int(input("Enter starting amount of candies (must be at least 30): "))
    while valid_value == False:
        if value >= 30:
            valid_value = True
        else:
            value = int(input("Enter starting amount of candies (must be at least 30): "))
    turn = True
    coinflip = random.randint(0, 2)
    if coinflip == 0: 
        turn = True
        print(f"{player1} will start first")
    else: 
        turn = False
        print(f"{player2} will start first")
    while value > 28:
        if turn == True:
            candy = candy_input(player1)
            value -= candy
            turn = False
            print_data(player1, value, candy)
        else:
            candy = candy_input(player2)
            value -= candy
            turn = True
            print_data(player2, value, candy)
    return turn

mode = mode_selection()
if mode == 0:
    res = bot_game()
    if res == True:
        print("Player won!")
    else:
        print("Bot won!")
else:
    res = people_game()
    if res == True:
        print("Player 1 won!")
    else:
        print("Player 2 won!")
