#!/usr/bin/python3
class Game():
    """"The game class should be able to start the game, play the game and stop the game"""
    welcome = """
        Welcome to the Rock, Papers, Scissors Game!
        ----------------------------------------
    """
    options = """
        Select 1: Play vs Computer
        Select 2: Play Vs Another User
        Select 3: Quit Game
    """
    exit_msg = """
        Would you like to continue playing this game?
        Select 1 - Yes
        Select 2 - No
    """
    print(welcome)

    def __init__(self, type: int):
        """ Intialize the game class
        args:
        type: The choice to play vs computer, or another user or not play the game"""
        self.type = type
    
    @classmethod
    def display_welcome(cls):
        """ Displays the start options for the game """
        print(cls.options)
    
    @classmethod
    def display_exit_msg(cls):
        """ Displays the start options for the game """
        print(cls.exit_msg)
