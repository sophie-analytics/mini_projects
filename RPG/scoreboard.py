# #!/usr/bin/python3
from game import Game
from players import Player

class ScoreBoard:
    """ class that keeps and update the scores"""
    def __init__(self):
        self.scores = {
        f"{Player.players_name[0]}": {"win": 0, "loss": 0},
        f"{Player.players_name[1]}":  {"win": 0, "loss": 0}, 
        "draw": 0
        }
       
    def update_scores(self):
        """ Update the scores based on outcome from the game class """
        if Game.result['winner'] == 0:
            self.scores[f'{Player.players_name[0]}']['win'] += 1
            self.scores[f'{Player.players_name[1]}']['loss'] += 1
        elif Game.result['winner'] == 1:
            self.scores[f'{Player.players_name[1]}']['win'] += 1
            self.scores[f'{Player.players_name[0]}']['loss'] += 1
        elif Game.result['draw'] == 2:
            self.scores['draw'] += 1
   
    def display_scores(self):
        """ Displays the scores and personalized it with each player's name"""
        for player, score in self.scores.items():
            if player != 'draw':
                print(f"{player} - Wins - {score['win']} Loss - {score['loss']}")
            else:
                print(f"Draw - {score}")
