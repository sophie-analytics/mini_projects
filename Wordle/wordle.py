#!/usr/bin/python3
import random

word_list = ["daddy", "apple", "later", "heard"]

# Welcome message
welcome = """
Welcome To The WORDLE Game
-> Where you have the chance to guess a 5 letter word choosen randomly by the computer
-> The word guessed must be a 5 letter word
-> You have a total of 6 trials
"""
print("----------------------------------------")
print (welcome)
rand_word = random.choice(word_list)
trials = 1

while trials <= 6:
    print("GUESS A 5 LETTER WORD ")
    user_choice = input(">>>  ")
    user_choice = user_choice.lower()

    if user_choice == rand_word:
        print(f"Congratulations! You guessed the word right in your {trials} trial")
    else:
        for ch in user_choice:
            if ch in rand_word:
                position1 = rand_word.index(ch)
                position2 = user_choice.index(ch)
                if position1 == position2:
                    print(f"{ch} is in the system and it is the right position")
                else:
                    print(f"{ch} is in the system and at position {position1 + 1}")
            else:
                print(f"{ch} is not in the list")

    if (trials == 6) or (user_choice == rand_word):
        if trials == 6:
            print("Yikes! So Bad You couldn't get it")
        game_on = input("Would you like to continue playing (y/n): ")
        game_on_mod = game_on.lower()
        if game_on_mod == "n":
            break
        elif game_on_mod == "y":
            rand_word = random.choice(word_list)
            trials = 1
            continue
    trials += 1
