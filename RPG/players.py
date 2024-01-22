#!/usr/bin/python3
"""A class module that defines a players of the game  """

class Rule():
    exit_msg = """
    Would you like to continue playing this game?
        Select 1 - Yes
        Select 2 - No
    """
    def __init__(self):
        self.players_input = []
        self.scores = {
           "player1": {"win": 0, "loss": 0},
            "player2":  {"win": 0, "loss": 0}, 
            "draw": 0
        }

    def add_player(self, player_input):
        self.players_input.append(player_input)

    def rule(self):
        if (
            (self.players_input[0] == "paper" and self.players_input[1] == "rock") or 
            (self.players_input[0] == "rock" and self.players_input[1] == "scissors") or
            (self.players_input[0] == "scissors" and self.players_input[1] == "paper")
         ) :
            self.scores['player1']['win'] += 1
            return 'Player 1 Wins!'

        elif (
            (self.players_input[1] == "paper" and self.players_input[0] == "rock") or 
            (self.players_input[1] == "rock" and self.players_input[0] == "scissors") or
            (self.players_input[1] == "scissors" and self.players_input[0] == "paper")
         ) :
            self.scores['player2']['win'] += 1
            return 'Player 2 Wins!'
        elif (self.players_input[0] == self.players_input[1]):
            self.scores['draw'] += 1
            return 'No Winner'

    def display_scores(self):
        for player, scores in self.scores.items():
            if player != "draw":
                print(f"{player}: Wins - {scores['win']}, Losses - {scores['loss']}")
            else:
                print(f"draws - {scores}")
    def exit(self):
        print(Rule.exit_msg)
