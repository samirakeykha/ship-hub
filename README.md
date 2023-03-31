![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome samira keykha,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

1. This line imports thry Python ´random´ module, which is used to generate random numbers and make random 
selections from sequences.

2. These three line set up the game paraneters.
´bord_size´ Represnts the length and width of the game board (which is square).
´num_ships´ is the number ogf ships that the player need to sink to win.
´ship_size´ is the length of each ship.
bord_size = 5  
num_ships = 4  
ship_size = 3  

3. This function takes a game board as input and prints it to the console, row by row. Each row is joined into a single
string with spaces between the characters, so that the output looks like a grid.
def print_board(board):
for row in board:
print(" ".join(row))

4. This function takes the board size as input and retuns a random row and column on the board. The´random.randint()´ 
Function is used to generate random integers between 0 and ´board_size - 1´ ,Which are then returned as tuple.


    def get_random_row_col(board_size):
    row = random.randint(0, board_size - 1) 
    col = random.randint(0, board_size - 1) 
    return row, col

5. This code initializes the game boarde to a list of lists, with each inner list representing a row on the board.
The 'for' loop runs 'boarde_size' times and adds a new row to the board, which is filled with the sting "0" (representing "ocean") using the ´*´ operator.
    board = []
    for i in range(board_size):  
    board.append(["O"] * board_size) 


6. This code initializes  the ship on the game boarde. The for loop runs 'num_ship' times and adds a new ship to 'ship' list.

    Each ship is represented as a list of coordinates (row, column) om the game board. The 'get_random_row_col()' function is used to generate a andom starting pointfot the ship. Then, a 'for' loop runt 'shio_size'times and adds the coordinates of the ship's cellsto the 'ship' list.  The 'if' statement inside the loop randomly chooses whether to add cells horizontally or vertically to the ship.
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

   7. These lines introduce the game and ask the player for their name.



