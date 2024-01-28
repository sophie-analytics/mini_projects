# #!/usr/bin/python3

class ScoreBoard:
    """ class that keeps and update the scores"""
    def __init__(self, game_instance: object):
        self.game = game_instance
        self.scores = {
        f"{self.game.players[0].get_name()}": {"win": 0, "loss": 0},
        f"{self.game.players[1].get_name()}":  {"win": 0, "loss": 0}, 
        "draw": 0
        }

    def update_scores(self, winner):
        """ updates the scores"""
        if winner == f"{self.game.players[0].get_name()} Wins":
            self.scores[f'{self.game.players[0].get_name()}']['win'] += 1
            self.scores[f'{self.game.players[1].get_name()}']['loss'] += 1
        elif winner == f"{self.game.players[1].get_name()} Wins":
            self.scores[f'{self.game.players[1].get_name()}']['win'] += 1
            self.scores[f'{self.game.players[0].get_name()}']['loss'] += 1
        elif winner == 'No Winner':
            self.scores['draw'] += 1
    def display_scores(self):
        """ Displays the scores and personalized it with each player's name"""
        for player, score in self.scores.items():
            if player != 'draw':
                print(f"{player} - Wins - {score['win']} Loss - {score['loss']}")
            else:
                print(f"Draw - {score}")
