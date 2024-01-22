#!/usr/bin/python3
import random
player = __import__('players').Rule
game = __import__('game').Game

def main():
    while (True):
        game.display_welcome()
        start = None
        try:
            start = game(int(input(">>> ")))
            if start.type is None or start.type <= 0 or start.type > 2:
                continue
        except (ValueError):
            print("[ Sorry, you have to input a valid digit ]")
            continue

        players = player()
        rpg_list = ["Rock", "Paper", "Scissors"]

        if start is not None and start.type == 1:
            player_input = input("Select rock, paper or scissors:  ")
            player_mod_input = player_input.lower()
            players.add_player(player_mod_input)

            user2_input = random.choice(rpg_list)
            user2_mod_input = user2_input.lower()
            players.add_player(user2_mod_input)
            print(f"Computer >>> {user2_mod_input}")
            
        else:
            for i in range(1, 3):
                player_input = input(f"Player{i} Select rock, paper or scissors:  ")
                players.add_player(player_input)

        print(players.rule())
        # result = players.rule()
        # print(result)
        players.exit()
        while(1):
            try:
                answer = int(input(">>> "))
                if answer == 2:
                    players.display_scores()
                    break
                elif answer == 1:
                    break
            except ValueError:
                print("You have not provided a valid answer")
        if answer == 2:
            break

if __name__ == "__main__":
    main()
