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
win = 0
loss = 0
draw = 0
player1_win = 0
player1_loss = 0
player2_win = 0
player2_loss = 0
Players_draw = 0

while(True):
    # This gets the number of players to play the game
    try:
        no_of_players = int(input("How many players are playing (max 2): "))
        print(f"You have selected {no_of_players}")
        if no_of_players == 1:
            print("You will be playing with the computer")
            print("----------------------------------------")
            print("Let's Play!")
            # User's selection of the game choice
            user_choice = input("Select (Rock, Paper Or Scissors): ")
            modified_input = user_choice.title()
            comp_choice= random.choice(rpg_list)
                
            print(f"Computer >>> {comp_choice}")
            if modified_input == "Paper" and comp_choice == "Rock":
                print("You Won")
                win += 1
            elif modified_input == "Rock" and comp_choice == "Scissors":
                print("You Won")
                win += 1
            elif modified_input == "Scissors" and comp_choice == "Paper":
                print("You Won")
                win += 1
            elif modified_input == "Paper" and comp_choice == "Scissors":
                print("You Lost")
                loss += 1
            elif modified_input == "Rock" and comp_choice == "Paper":
                print("You Lost")
                loss += 1
            elif modified_input == "Scissors" and comp_choice == "Rock":
                print("You Lost")
                loss += 1
            elif modified_input == "paper" and comp_choice == "paper":
                print("No Winner")
                draw += 1
            elif modified_input == "Rock" and comp_choice == "Rock":
                print("No Winner")
                draw += 1
            elif modified_input == "Scissors" and comp_choice == "Scissors":
                print("No Winner")
                draw += 1
            else:
                print("You have to select rock, paper or scissors")

            game_on = input("Would you like to continue playing (y/n): ")
            if game_on == "n":
                print("----------------------------------------")
                print("Final Scores")
                print("----------------------------------------")
                print(f"You won a total of {win} games")
                print(f"You loss a total of {loss} games")
                print(f"You drew a total of {draw} games")
                
                print("----------------------------------------")

                if win > loss:
                    print("Congratualtions! You are the overall winner\n")
                elif loss > win:
                    print("Sorry! The computer is the overall winner\n")
                elif win == loss:
                    print("Bummer! It ended in a tie.\n")
                break
        elif no_of_players == 0:
            print("You have not selected a valid number of players, Try Again")
            continue
        elif no_of_players == 2:
            print("You are player 1\nSecond player is player 2")
            print("----------------------------------------")
            print("Let's Play!")
            # User's selection of the game choice
            user1_choice = input("Player 1 Select (Rock, Paper Or Scissors): ")
            modified_input1 = user1_choice.title()
            user2_choice = input("Player 2 Select (Rock, Paper Or Scissors): ")
            modified_input2 = user2_choice.title()

            if modified_input1 == "Paper" and modified_input2 == "Rock":
                print("Player 1 Won")
                player1_win += 1
                player2_loss += 1
            elif modified_input1 == "Rock" and modified_input2 == "Scissors":
                print("Player 1 Won")
                player1_win += 1
                player2_loss += 1
            elif modified_input1 == "Scissors" and modified_input2 == "Paper":
                print("Player 1 Won")
                player1_win += 1
                player2_loss += 1
            elif modified_input1 == "Paper" and modified_input2 == "Scissors":
                print("Player 2 Won")
                player1_loss += 1
                player2_win += 1
            elif modified_input1 == "Rock" and modified_input2 == "Paper":
                print("Player 2 Won")
                player1_loss += 1
                player2_win += 1
            elif modified_input1 == "Scissors" and modified_input2 == "Rock":
                print("Player 2 Won")
                player1_loss += 1
                player2_win += 1
            elif modified_input1 == "paper" and modified_input2 == "paper":
                print("No Winner")
                Players_draw += 1
            elif modified_input1 == "Rock" and modified_input2 == "Rock":
                print("No Winner")
                Players_draw += 1
            elif modified_input1 == "Scissors" and modified_input2 == "Scissors":
                print("No Winner")
                Players_draw += 1
            else:
                print("You have to select rock, paper or scissors")

            game_on1 = input("Would you like to continue playing (y/n): ")
            if game_on1 == "n":
                print("----------------------------------------")
                print("Final Scores")
                print("----------------------------------------")
                print(f"Player 1 won a total of {player1_win} games\nPlayer 2 won a total of {player2_win} games")
                print(f"Player 1 loss a total of {player1_loss} games\nPlayer 2 loss a total of {player2_loss} games")
                print(f"Players drew a total of {Players_draw} games")
                
                print("----------------------------------------")

                if player1_win > player2_win:
                    print("Congratualtions Player 1! You are the overall winner\n")
                elif player2_win > player1_win:
                    print("Congratualtions Player 2! You are the overall winner\n")
                elif win == loss:
                    print("Bummer! It ended in a tie.\n")
                break
        elif no_of_players > 2:
            print("Sorry, only maximum of 2 players are allowed in this game! Try Again")
    # Captures the value error and prints a more readable reply
    except ValueError:
        print("Sorry, you have to input a digit")
