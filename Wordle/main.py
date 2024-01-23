#!/usr/bin/python3
from game_w import Game
from player_w import Player

trials = 1

wordle = Game()
wordle.random_word()
while trials <= 6:
    print("GUESS A 5 LETTER WORD ")
    user = Player(input(">>>  "))

    if wordle.is_correct():
        print()
    
