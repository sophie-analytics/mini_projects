#!/usr/bin/python3
import random

class Game():
    """ The Game should be able to start the game and also end the game"""
    word_list = ["daddy", "apple", "later", "heard"]

    welcome = """
                    Welcome To The WORDLE Game
    -> Where you have the chance to guess a 5 letter word choosen randomly by the computer
    -> The word guessed must be a 5 letter word
    -> You have a total of 6 trials
    """
    print(welcome)

    def __init__(self, word: str):
        self.word = word
    
    def random_word(self):
        self.rand_word = random.choice(Game.word_list)

    def is_correct(self):
        if self.rand_word == self.word:
            return True
        else:
            False
