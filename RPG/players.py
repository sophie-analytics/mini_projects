# #!/usr/bin/python3
class Player:
    """ The player class should be able to play the game, choose a winner, keep scores"""
    def __init__(self, player_input: list):
        """ Initialize with the choice of input """
        self.player_input = [player_input]
        self.scores = {
        "player1": {"win": 0, "loss": 0},
        "player2":  {"win": 0, "loss": 0}, 
        "draw": 0
        }

    def player2_input(self, player2_input: str):
        """ Collects the second player's input """
        self.player_input.append(player2_input)
    
    def result(self):
        """ Act as a judge and selects the winner and loser"""
        if (
            (self.player_input[0] == "paper" and self.player_input[1] == "rock") or 
            (self.player_input[0] == "rock" and self.player_input[1] == "scissors") or
            (self.player_input[0] == "scissors" and self.player_input[1] == "paper")
            ) :
            self.scores['player1']['win'] += 1
            return 'Player 1 Wins!'

        elif (
            (self.player_input[1] == "paper" and self.player_input[0] == "rock") or 
            (self.player_input[1] == "rock" and self.player_input[0] == "scissors") or
            (self.player_input[1] == "scissors" and self.player_input[0] == "paper")
            ) :
            self.scores['player2']['win'] += 1
            return 'Player 2 Wins!'

        elif (self.player_input[0] == self.player_input[1]):
            self.scores['draw'] += 1
            return 'No Winner'
        
    def final_scores(self):
        """ Prints the final scores"""
        for player, score in self.scores.items():
            if player != 'draw':
                print(f"{player} - Wins - {score['win']} Loss - {score['loss']}")
            else:
                print(f"Draw - {score}")
