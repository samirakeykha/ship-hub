import random

# Set up game parameters
board_size = 5
num_ships = 4
ship_size = 3


# Define helper functions
def print_board(board):
    for row in board:
        print(" ".join(row))


def get_random_row_col(board_size):
    row = random.randint(0, board_size - 1)
    col = random.randint(0, board_size - 1)
    return row, col


# Set up game board
board = []
for i in range(board_size):
    board.append(["O"] * board_size)

# Place ships on board
ships = []
for i in range(num_ships):
    ship = []
    row, col = get_random_row_col(board_size)
    for j in range(ship_size):
        if random.randint(0, 1) == 0:
            ship.append([row, col + j])
        else:
            ship.append([row + j, col])
    ships.append(ship)

# Start game loop
print("Welcome to ULTIMATE BATTLESHIPS!!")
print(f"Board Size: {board_size}. Number of ships: {num_ships}")
print("Top left corner is row: 0, col: 0")
print()
player_name = input("Please enter your name: ")
print()

num_turns = 0
while True:
    # Print board and ask for user input
    print_board(board)
    print(f"{player_name}, it's your turn!")
    try:
        guess_row = input("Guess row (0-4): ")
        if not isinstance(guess_row, int):
            raise TypeError(
                "You must enter your response in integer format"
            )
    except TypeError as d:
        print(f"Invalid response: {d}") 
                      
    guess_col = int(input("Guess col (0-4): "))
    print()

    # Check if guess is a hit or a miss
    if [guess_row, guess_col] in ships:
        print("HIT!")
        ships.remove([guess_row, guess_col])
        board[guess_row][guess_col] = "X"
    else:
        print("MISS!")
        board[guess_row][guess_col] = "M"

    # Check if game is over
    if not ships:
        print_board(board)
        print(f"Congratulations {player_name}, you sank all the ships!")
        print(f"You took {num_turns} turns.")
        break

    # Increment turn counter
    num_turns += 1
