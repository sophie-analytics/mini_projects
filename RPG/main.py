#!/usr/bin/python3
import random
from game import Game
from players import Player
rps = ["Rock", "Paper", "Scissors"]

while(True):
    Game.display_welcome()
    try:
        rps_game = Game(int(input(">>>  ")))
        if rps_game.type == 1:
            print("\tPrepare to face the computer!\nYou are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("\t----------------------------------------")
            print("\tLet's Play!\n")
        elif rps_game.type == 2:
            print("\tYou are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("\t----------------------------------------")
            print("\tLet's Play!\n")
        elif rps_game.type == 3:
            break
        elif rps_game.type <= 0:
            print("[ You have not selected a valid number of players, Try Again ]")
            continue
        elif rps_game.type > 2:
            print("[ Sorry, only maximum of 2 players are allowed in this game! Try Again ]")
            continue
    except ValueError:
        print("[ You have not selected a valid number of players, Try Again ]")
        continue

    player = Player(input("Select Rock, Paper or Scissors:  "))
    if rps_game.type == 1:
        player1_mod = player.player_input[0].lower()
        player2 = random.choice(rps)
        player2_mod = player2.lower()
        player.player2_input(player2_mod)
        print(f"Computer >>> {player2}")

    else:
        player2 = input("Select Rock, Paper or Scissors:  ")
        player2_mod = player2.lower()
        player.player2_input(player2_mod)

    print(player.result())
    Game.display_exit_msg()
    while(1):
        try:
            answer = int(input(">>> "))
            if answer == 2:
                player.final_scores()
                break
            elif answer == 1:
                break
        except ValueError:
            print("You have not provided a valid answer")
    if answer == 2:
        break
