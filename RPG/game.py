#!/usr/bin/python3
from players import Player
from rule import Rule
from scoreboard import ScoreBoard

class Game:
    def __init__(self, players: list([Player]), rules: dict):
        self.players = players
        self.rules = rules
        self.scores = ScoreBoard(self)
        self.players_input = ""

    def get_players(self):
        return self.players
    
    def add_player(self, player: Player):
        self.players.append(player)

    def get_rules(self):
        return self.rules
    
    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def validate_input(self, input: str):
        rps = ["rock", "paper", "scissors"]
        try:
            if not input.lower() in rps:
                raise NameError("It has to be rock, peper or scissors")
        except Exception:
            print("It has to be rock, peper or scissors")

    def play(self, player1_input: str, player2_input: str):
        self.validate_input(player1_input)
        self.validate_input(player2_input)
        self.players_input = player1_input.lower() + player2_input.lower()
    
    def get_winner(self):
        if self.players_input in self.rules:
            return(self.rules[self.players_input])
        self.scores.update_scores(self.get_winner)