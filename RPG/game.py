#!/usr/bin/python3

class Game():
    welcome = """
        Welcome to the Rock, Papers, Scissors Game!
        ----------------------------------------
    """
    options = """
        Select 1: Play against the computer
        Select 2: Play against another user
    """
    print(welcome)
    @classmethod
    def display_welcome(cls):
        print(cls.options)

    def __init__(self, type):
        self.type = None
        if type == 1:
            print("\tPrepare to face the computer!\nYou are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("\t----------------------------------------")
            print("\tLet's Play!")
            self.type = type
        elif type == 2:
            print("\tYou are designated Player 1 in this game, while your opponent assumes the role of Player 2.")
            print("\t----------------------------------------")
            print("\tLet's Play!")
            self.type = type
        elif type <= 0:
            print("[ You have not selected a valid number of players, Try Again ]")
        elif type > 2:
            print("[ Sorry, only maximum of 2 players are allowed in this game! Try Again ]")
