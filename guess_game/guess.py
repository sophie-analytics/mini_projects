#!/usr/bin/python3
from random import randint

# Genearte a random beween 1 - 50
random_no = randint(1, 50)
trials = 1

# Welcome message
welcome = "Welcome To The Nunber Guessing Game"
print("----------------------------------------")
print (welcome)

while trials <= 10:
    print("Pick A  Number Between 1 to 50 ")
    user_choice = int(input(">>>  "))

    if user_choice < random_no:
        print(f"Yikes! That is low, Try Again\n[trial {trials}]")
    elif user_choice > random_no:
        print(f"That is high! Try Again\n[trial {trials}]")
    elif (user_choice == random_no) and (trials == 1):
        print("Correct! I Wish I Was As Smart As You")
    elif (user_choice == random_no) and (trials < 4):
        print("Correct! That's Incredible")
    elif (user_choice == random_no) and (4 <= trials <= 7):
        print("Correct! That's Superb")
    elif (user_choice == random_no) and (8 <= trials <= 10):
        print("At Last! You Nailed It")
    elif (user_choice != random_no) and (trials == 10):
        print("Yikes! So Bad You Couldn't Get It")

    if (trials == 10) or (user_choice == random_no):
        game_on = input("Would you like to continue playing (y/n): ")
        game_on_mod = game_on.lower()
        if game_on_mod == "n":
            break
        elif game_on_mod == "y":
            random_no = randint(1, 50)
            trials = 1
            continue
    trials += 1
