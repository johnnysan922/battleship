from random import randint

board = []
for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row)) # [" ".join()] adds " " between elements

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#next 2 lines are knowing where ship is
#-------------------------
print("-----Testing-----")
print (ship_row)
print (ship_col)
print("------------------")
#-------------------------

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

#if guess is right
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    board[ship_row][ship_col] = "+"
    print_board(board)
    print("Game Over!")
    break
#if guess is not right
  else:
    #guess if outside of board
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    #guess is same as previous turns
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    #guess is wrong
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      
    # Print (turn + 1) here (turn is 0 based)
    print ("Turn: " + str(turn + 1))
    print_board(board)
    if turn == 3:
        print ("Game Over.")