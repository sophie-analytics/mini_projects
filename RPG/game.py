#!/usr/bin/python3
from players import Player

class Game:
    """ Keeps the updated version of the winner gotten from the game"""
    result = {
        'winner': 0,
        'loser':  0,
        'draw': 0
        }
  
    def __init__(self, game_mode: int):
        """ initialize with the mode of the game choosen"""
        self.game_mode = game_mode
        self.player_choice = []

    def get_player_choice(self, choice: str):
        """ gets the players choice """
        self.player_choice.append(choice)
        
    def determine_round_winner(self):
        """ determines who wins each round """
        if (
            (self.player_choice[0] == "paper" and self.player_choice[1] == "rock") or 
            (self.player_choice[0] == "rock" and self.player_choice[1] == "scissors") or
            (self.player_choice[0] == "scissors" and self.player_choice[1] == "paper")
            ) :
            Game.result['winner'] = 0
            return f'{Player.players_name[0].title()} Wins!'

        elif (
            (self.player_choice[1] == "paper" and self.player_choice[0] == "rock") or 
            (self.player_choice[1] == "rock" and self.player_choice[0] == "scissors") or
            (self.player_choice[1] == "scissors" and self.player_choice[0] == "paper")
            ) :
            Game.result['winner'] = 1
            return f'{Player.players_name[1].title()} Wins!'

        elif (self.player_choice[0] == self.player_choice[1]):
            Game.result['draw'] = 2
            return 'No Winner'

















#     """"The game class should be able to start the game, play the game and stop the game"""
#     welcome = """
#         Welcome to the Rock, Papers, Scissors Game!
#         ----------------------------------------
#     """
#     options = """
#         Select 1: Play vs Computer
#         Select 2: Play Vs Another User
#         Select 3: Quit Game
#     """
#     exit_msg = """
#         Would you like to continue playing this game?
#         Select 1 - Yes
#         Select 2 - No
#     """
#     print(welcome)
#     def __init__(self, players: list[Player]):
#         self.type = type
#         self.winner: Player
#         self.loser: Player
#         self.players = players

#     @classmethod
#     def display_welcome(cls):
#         """ Displays the start options for the game """
#         print(cls.options)
    
#     @classmethod
#     def display_exit_msg(cls):
#         """ Displays the start options for the game """
#         print(cls.exit_msg)
