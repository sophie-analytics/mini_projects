#!/usr/bin/python3
import random
from game import Game
from players import Player
from scoreboard import ScoreBoard
# from rule import Rule


rps = ["Rock", "Paper", "Scissors"]
#Welcome message
welcome = """
        Welcome to the Rock, Papers, Scissors Game!
        =========================================== """
print(welcome)

exit_msg = """
        Would you like to continue playing this game?
        Select 1 - Yes
        Select 2 - No
   """
i = 0
while True:
        options = """
                Select 1: Play vs Computer
                Select 2: Play Vs Another User
                Select 3: Quit Game
                """
        print(options)
        choice = input(">>> ")

        if i <= 0:
                player1 = Player(input("Enter your name:  "))
                if choice == "1":
                        player2 = Player("Computer")

                elif choice == "2":
                        player2 = Player(input("Enter yor name:  "))
                elif choice == "3":
                        break
                else:
                        print("[You have not provided a valid input]")
                        continue


        rules = {
                "rockpaper": f"{player2.get_name()} Wins",
                "paperrock": f"{player1.get_name()} Wins",
                "rockscissors":f"{player2.get_name()} Wins",
                "scissorsrock": f"{player1.get_name()} Wins",
                "scissorspaper": f"{player1.get_name()} Wins",
                "paperscissors": f"{player2.get_name()} Wins",
                "paperpaper": "No Winner",
                "scissorsscissors": "No Winner",
                "rockrock": "No Winner"
        }

        game = Game([player1, player2], rules)
        scores = ScoreBoard(game)
        if choice == "1":
            comp_choice = random.choice(rps)
            game.play(input("Select Rock, Paper Or Scissors >>>>   "), comp_choice)
            print(f"Computer >>> {comp_choice}")
            print(game.get_winner())
        elif choice == "2":
            game.play(input("Select Rock, Paper Or Scissors >>>>  "),input("Select Rock, Paper Or Scissors >>>>   "))
            print(game.get_winner())

        scores.update_scores(game.get_winner())
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
