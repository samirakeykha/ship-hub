from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Class representing the game board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = ["." for x in range(size) for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses =[]
        self.ship =[]

    def print(self):
        for row in self.board:
            print("".join(row))

    def guess(self, x, y):  # Add the guess to the list of guesses
        self.guesses.append(x, y)
        self.board[x][y] = "x"
    if (x, y) in self.ships:
        self.board[x][y] = "*"  # Mark the board with a hit
        print(f"{self.name} hit a ship!")
        return "Hitt"
    else

     self.board[x][y] = "x"  # Mark the board with a miss
    print(f"{self.name} missed.")
    return "Miss"
 def play_game():
     
    """
    Function to play a single game of Battleship.
    
    """
    # Create the player and computer boards
    player_board = Board(5, 2, "Player", "human")
    computer_board = Board(5, 2, "Computer", "computer")

    # Loop through the game until all ships are sunk
    while True:
        # Print the game boards
        print("Player Board:")
        player_board.print()
        print("Computer Board:")
        computer_board.print()
        
        # Player's turn
        print("Player's turn:")
        while True:
            try:
                x = int(input("Enter a row number: "))
                y = int(input("Enter a column number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers for row and column numbers.")
        result = computer_board.guess(x, y)
        if result == "Hit":
            print("Player hit a ship!")
        if computer_board.num_ships == sum(row.count("*") for row in computer_board.board):
            print("Player wins!")
            return "player"
        
        # Computer's turn
        print("Computer's turn:")
        x = randint(0, 4)
        y = randint(0, 4)
        result = player_board.guess(x, y)
        if result == "Hit":
            print("Computer hit a ship!")
        if player_board.num_ships == sum(row.count("*") for row in player_board.board):
            print("Computer wins!")
            return "computer"

def main():
    """
    Function to play multiple games of Battleship and keep track of the overall score.
    """
    scores = {"player": 0, "computer": 0}
    num_games = int(input("How many games do you want to play? "))
    for i in range(num_games):
        print(f"Starting game {i+1}...")
        winner = play_game()
        scores[winner] += 1
        print(f"Current score: Player - {scores)   


    