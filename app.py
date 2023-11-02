import os
import random
import art

# Create a class called "Player" with methods to randomly choose and return either 'rock', 'paper' or 'scissors'.
# This class should have:
# - An attribute called "score", should be initialized to 0.,
# - An attribute called "name" should be initialized to an empty string.,
# - An attribute called "move" should be initialized to None.

class Player():
    def __init__(self):
        self.score = 0
        self.name = ''
        self.move = None
        ### Below is the attribute `self.moves` that is initialized to ['rock', 'paper', 'scissors'].
        self.moves = ['rock', 'paper', 'scissors']

    def random_choice(self):
        self.move = random.choice(['rock', 'paper', 'scissors'])
        return self.move
    
    ### Add a method called "add_score" that adds 1 to the score attribute.
    def add_score(self):
        self.score += 1
        return self.score
    
    ### Add a method called "reset_score" that sets the score attribute to 0.
    def reset_score(self):
        self.score = 0
        return self.score
    
    ### Add a method called "set_name" that sets the name attribute to a name passed into the method.
    def set_name(self, name):
        self.name = name
        return self.name
    
    ### Add a method called "get_name" that returns the name attribute.
    def get_name(self):
        return self.name
    
    ### Add a method called "get_score" that returns the score attribute.
    def get_score(self):
        return self.score
    
    ### Add a method called "get_move" that returns the move attribute.
    def get_move(self):
        return self.move
    
    ### Add a method called "set_move" that sets the move attribute to a move passed into the method.
    def set_move(self, move):
        self.move = move
        return self.move
    
    ### Add a method called "reset_move" that sets the move attribute to None.
    def reset_move(self):
        self.move = None
        return self.move
    
    ### Add a method called "inquire_move" that prompts the player for a move inside a input() (we show the keys of self.moves to the player during the prompt) then check
    ### if the move is valid (is in self.moves), if not valid, prompt the player again until a valid move is entered.
    def inquire_move(self):
        while True:
            move = input(f"What is your move? {self.moves} ").lower()
            if move in self.moves:
                return move
            else:
                print("Invalid move!")
    
### Create a class called "Game" with methods to play a game of rock, paper, scissors.
### This class should have:
### - An Attribute called "player" that is initialized to Player(),
### - An Attribute called "computer" that is initialized to Player(),
### - An Attribute called "moves" that is initialized to ['rock', 'paper', 'scissors'],
### - An Attribute called "rules" that is initialized to {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'},
### - An Attribute called "computer_score" that is initialized to 0,
### - An Attribute called "player_score" that is initialized to 0,
### - An Attribute called "rounds" that is initialized to 3,
### - An Attribute called "round_count" that is initialized to 0.

class Game():
    def __init__(self):
        self.player = Player()
        self.computer = Player()
        self.moves = ['rock', 'paper', 'scissors']
        self.rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        self.rounds = 3
        self.round_count = 0
    
    ### Add a method called "get_player" that returns the player attribute.
    def get_player(self):
        return self.player
    
    ### Add a method called "get_computer" that returns the computer attribute.
    def get_computer(self):
        return self.computer
    
    ### Add a method called "get_player_score" that returns the player_score attribute.
    def get_player_score(self):
        return self.player.score
    
    ### Add a method called "get_computer_score" that returns the computer_score attribute.
    def get_computer_score(self):
        return self.computer.score
    
    ### Add a method called "get_rounds" that returns the rounds attribute.
    def get_rounds(self):
        return self.rounds
    
    ### Add a method called "get_round_count" that returns the round_count attribute.
    def get_round_count(self):
        return self.round_count
    
    ### Add a method called "get_moves" that returns the moves attribute.
    def get_moves(self):
        return self.moves
    
    ### Add a method called "get_rules" that returns the rules attribute.
    def get_rules(self):
        return self.rules
    
    ### Add a method called "set_player" that sets the player attribute to a player passed into the method.
    def set_player(self, player):
        self.player = player
        return self.player
    
    ### Add a method called "set_computer" that sets the computer attribute to a computer passed into the method.
    def set_computer(self, computer):
        self.computer = computer
        return self.computer
    
    ### Add a method called "add_winner_score" that takes a winner as an argument and adds 1 to the score of the winner.
    def add_winner_score(self, winner):
        winner.add_score()
    

### Adapt the code below to use the Game class to play a game of rock, paper, scissors.
### Where:
### - The computer is the opponent and chooses a move randomly,
### - The player is first prompted for their name if is not already set, then prompted for their move,
### After each round the score is displayed and the player is prompted to play again.
###
### The code above should be used inside a while loop that continues until the player decides to quit.
### The while loop should be first tested inside a __name__ == "__main__" block.



if __name__ == "__main__":
    ### Firtsly, check what OS the game is running on and clear the screen accordingly.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    ### Display a prettified message to the player welcoming them to the game using the art library as ASCII art.
    ### The ASCII art should have a different color for each letter, and say "Welcome to Rock, Paper, Scissors!".
    print(art.text2art("Welcome to Rock, Paper, Scissors!"))


    try:

        ### Create the game loop here:
        game = Game()
        game.get_player().set_name(input("What is your name? "))
        ### Create a variable called "play_again" and set it to True
        ### This variable is the condition for the while loop and should only be changed to False when the player decides to quit.
        play_again = True
        while play_again:
            ### Inside the while loop:
            ### - Increment the round_count attribute by 1,
            game.round_count += 1
            ### - Set the player move to None,
            game.get_player().reset_move()
            ### - Set the computer move to None,
            game.get_computer().reset_move()
            ### - Display the round number,
            print(f"Round {game.get_round_count()}")
            ### - Display the player score, and its name,
            print(f"{game.get_player().get_name()} score: {game.get_player_score()}")
            ### - Display the computer score,
            print(f"Computer score: {game.get_computer_score()}")
            ### - Prompt the player for their move,
            game.get_player().set_move(game.get_player().inquire_move())
            ### - Randomly choose a move for the computer,
            game.get_computer().random_choice()
            ### - Display the player move,
            print(f"Player move: {game.get_player().get_move()}")
            ### - Display the computer move,
            print(f"Computer move: {game.get_computer().get_move()}")
            ### - Determine the winner of the round, then add 1 to the score of the winner, then display the winner of the round,
            ### otherwise display that it is a tie.
            if game.get_player().get_move() == game.get_computer().get_move():
                print("It's a tie!")
            elif game.get_player().get_move() == game.get_rules()[game.get_computer().get_move()]:
                print(f"{game.get_player().get_name()} wins!")
                game.add_winner_score(game.get_player())
            else:
                print("Computer wins!")
                game.add_winner_score(game.get_computer())
            ### - Display the winner of the round,
            ### - Prompt the player to play again,
            play_again = input("Play again? (y/n) ").lower() == 'y'
    except KeyboardInterrupt:
        pass

    ### Display a prettified message to the player thanking them for playing using the art library as ASCII art.
    ### The ASCII art should have a different color for each letter, and say "Thanks for playing!".
    print(art.text2art("Thanks for playing!"))





