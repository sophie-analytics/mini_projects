#!/usr/bin/python3
# Import module random to provide functon that allows items to be selected at random
import random

# Welcome message
welcome = "Welcome to the Rock, Papers, Scissors Game!"
print("----------------------------------------")
print (welcome)
#List of the options available for the game
rpg_list = ["Rock", "Paper", "Scissors"]
# To keep count of scores
player1_win = 0
player1_loss = 0
player2_win = 0
player2_loss = 0
Players_draw = 0

while(True):
    # This gets the number of players to play the game
    try:
        # no_of_players = int(input("Select 1 to play against computer\nSelect 2 to play against another user"))
        print("Select 1: Play against the computer\nSelect 2: Play against another user")
        no_of_players = int(input(">>>>  " ))
        print(f"You have selected {no_of_players}")
        if no_of_players == 1:
            print("Prepare to face the computer!\nYou are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("----------------------------------------")
            print("Let's Play!")
        elif no_of_players == 2:
            print("You are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("----------------------------------------")
            print("Let's Play!")
            # User's selection of the game choice
        elif no_of_players == 0:
            print("[ You have not selected a valid number of players, Try Again ]")
            continue
        elif no_of_players > 2:
            print("[ Sorry, only maximum of 2 players are allowed in this game! Try Again ]")
            continue
    # Captures the value error and prints a more readable reply
    except ValueError:
        print("Sorry, you have to input a digit")
        continue

    #start of the game
    user1_choice = input("Select (Rock, Paper Or Scissors): ")
    user1_mod_input = user1_choice.title()
    if no_of_players == 1:
        user2_mod_input = random.choice(rpg_list)
        print(f"Computer >>> {user2_mod_input}")
    else:
        user2_choice = input("Select (Rock, Paper Or Scissors): ")
        user2_mod_input = user2_choice.title()

    if (user1_mod_input == "Paper" and user2_mod_input == "Rock") or (user1_mod_input == "Rock" and user2_mod_input == "Scissors") or (user1_mod_input == "Scissors" and user2_mod_input == "Paper"):
        print("Player 1 Won")
        player1_win += 1
        player2_loss += 1
    elif (user1_mod_input == "Paper" and user2_mod_input == "Scissors") or (user1_mod_input == "Rock" and user2_mod_input == "Paper") or (user1_mod_input == "Scissors" and user2_mod_input == "Rock") :
        print("Player 2 Won")
        player1_loss += 1
        player2_win += 1
    elif user1_mod_input == user2_mod_input:
        print("No Winner")
        Players_draw += 1
    else:
        print("You have to select rock, paper or scissors")

    while(True):
        game_on = input("Would you like to continue playing (y/n): ")
        game_on_mod = game_on.lower()
        if game_on_mod == "n":
            # print("You have not selected a valid option, Try again")
            print("----------------------------------------")
            print("Final Scores")
            print("----------------------------------------")
            print(f"Player 1 won a total of {player1_win} games\nPlayer 1 loss a total of {player1_win} games")
            print(f"Player 2 won a total of {player2_win} games\nPlayer 2 loss a total of {player2_loss} games")
            print(f"Players drew a total of {Players_draw} games")
            
            print("----------------------------------------")

            if player1_win > player2_win:
                print("Congratualtions Player 1! You are the overall winner\n")
            elif player2_win > player1_win:
                print("Congratualtions Player 2! You are the overall winner\n")
            elif player1_win == player2_win:
                print("Bummer! It ended in a tie.\n")
            break
        elif game_on_mod == "y":
            break
        else:
            print("You have not selected a valid option, Try again")
    if game_on_mod == "n":
        break
