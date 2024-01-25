#!/usr/bin/python3
import random
from game import Game
from players import Player
from scoreboard import ScoreBoard

rps = ["Rock", "Paper", "Scissors"]
#Welcome message
welcome = """
        Welcome to the Rock, Papers, Scissors Game!
        ---------------------------------------- """
print(welcome)

exit_msg = """
        Would you like to continue playing this game?
        Select 1 - Yes
        Select 2 - No
    """
i = 0
while True:    #Infinite loop
    #Displays game modes
    options = """
            Select 1: Play vs Computer
            Select 2: Play Vs Another User
            Select 3: Quit Game
        """
    print(options)

    try:
        game = Game(int(input(">>>  ")))    #instantiate the game class with player choice of game mode
        if game.game_mode == 1:
            print("\tPrepare to face the computer!")
            print("\t----------------------------------------")
            print("\tLet's Play!\n")
        elif game.game_mode == 2:
            print("\tYou are have choosen to play vs another player in this game")
            print("\t----------------------------------------")
            print("\tLet's Play!\n")
        elif game.game_mode == 3:
            print("game will quit")
            break
        elif game.game_mode <= 0 or game.game_mode > 3:
            print("[ You have not selected a valid game mode, Try Again ]")
            continue
    except ValueError:
        print("[ You have not selected a valid number of players, Try Again ]")
        continue
    
    if i <= 0:   # This prevents the player input name to pop up after requesting for it once
        players = Player(input("Enter your name Player 1 >>> "))   #Instantiate Player class with each Players name
        if game.game_mode == 1:
            players.add_player("Computer") #player2 is the computer
        elif game.game_mode == 2:
            players.add_player(input("Enter your name Player 2 >>> "))

    game.get_player_choice(input(f"({Player.players_name[0].title()}) Select Rock, Paper or Scissors >>>  "))  #Request for the player's input choice
    game.player_choice[0] = game.player_choice[0].lower()   #Converts it to lowercase for consistency

    if game.game_mode == 1:
        computer = random.choice(rps)    #computer randomly generates an input
        game.get_player_choice(computer)   
        game.player_choice[1] = game.player_choice[1].lower()  #Converts to lowercase
        print(f"({Player.players_name[1].title()}) >>> {computer}")  #Prints computer choice
    elif game.game_mode == 2:
        game.get_player_choice(input(f"({players.name[0].title()}) Select Rock, Paper or Scissors >>>  "))  #if there is a 2nd player, this gets the user input

    print(game.determine_round_winner())  #Determines the winner of exh round

    scores = ScoreBoard() 
    scores.update_scores()   #Updates the scoreboard
    print(exit_msg)
    while(1): # Another infinte loop to ensure correct exit input
        try:
            exit_ans = int(input(">>> "))
            if exit_ans == 2:
                scores.display_scores()
                break
            elif exit_ans == 1:
                break
        except ValueError:
            print("You have not provided a valid answer")
    i += 1
    if exit_ans == 2:
        break
