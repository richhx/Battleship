# @author Richard Huang
# @date   April 19, 2015
# Made with the help of Codecademy

from random import randint

# The board to play the game
board = []
# Instantiate the board
for x in range(5):
    board.append(["O"] * 5)

# Function name: print_board()
# Purpose:       Prints the board to stdout
def print_board(board):
    for row in board:
        print " ".join(row)

### Start game ###
print "\nLet's play Battleship! You have 4 tries.\n"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# for debugging purposes, print the row and column
#print ship_row
#print ship_col

for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "\nCongratulations! You sunk my battleship!\n"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or \
           (guess_col < 0 or guess_col > 4):
            print "\nOops, that's not even in the ocean.\n"
        elif(board[guess_row][guess_col] == "X"):
            print "\nYou guessed that one already.\n"
        else:
            print "\nYou missed my battleship!\n"
            board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
        print_board(board)
        
        if turn == 3:
            print "Game Over"
