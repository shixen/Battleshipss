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


def guess_ship(board):

    for turn in range(10):
        print("turn", turn + 1)

        # ask the user to input a number
        try:
            guess_row = int(input("Guess a row between 0-4: "))
            guess_col = int(input("Guess a column between 0-4: "))
        except ValueError:
            print("must be numbers.")
            continue
            
        # checks if guess matches the random ship
        if guess_row == ship_row and guess_col == ship_col:
            print(f"well done! {username} you sunk my battleship!")
            board[guess_row][guess_col] = "@"
            print_board(board)
            break   
        else:
            if (guess_row not in range(5) or guess_col not in range(5)):
                print("you must guess between 0-4")

            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that already")
        
            else:
                print("That's a miss!")
                board[guess_row][guess_col] = "X"
                            # ask player to play again when turns are out
            if turn == 9:
                    play_again = input("Game over. play again ? y/n: ")
                    if play_again == "y":
                        main()
                        break
                        
                        
                        
            print_board(board)


# main function to print game
def main():
    print_board(board)
    random_row(board)
    random_col(board)
    guess_ship(board)



main()
