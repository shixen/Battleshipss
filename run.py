from random import randint

board = []
# creates a board of 5x5 
for x in range(0,5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print((" ").join(row))


# creates random ships on board
def random_row(board):
    return randint(0, len(board) - 1)
  
   
def random_col(board):
     return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

# ask for username and display rules for game
username = input("please enter your name: ")
print(f"hello {username} welcome to a game of battleships!")
print("There is a hidden ship on the board and your job is to guess a number between 0-4 untill you hit with 10 attempts!")