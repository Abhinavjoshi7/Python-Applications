game_board = ["-","-","-",
              "-","-","-",
              "-","-","-"]
# global variables
game_still_going = True
winner = None
current_player = 'X'
def display_board():
     print(game_board[0]+ " | " + game_board[1]+ " | " + game_board[2])
     print(game_board[3]+ " | " + game_board[4]+ " | " + game_board[5])
     print(game_board[6]+ " | " + game_board[7]+ " | " + game_board[8])
     

def play_game():
    display_board()
    while game_still_going:
      handle_position(current_player)   
      check_game_is_over()
      flip_player()
    #The game is ended
    if(winner == 'X' or winner == 'O'):
        print(winner + " won.")
    elif winner == None:
        print("Tie")
    
def handle_position(player):
    print(player + "'s turn.")
   
    position = input("Chose a position from 1 to 9 ")
    valid = False
    while not valid:
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
         position = input("Chose a position from 1 to 9 ")
         
        position = int(position) - 1
        if game_board[position] == "-":
            valid = True
            #if it is true break out from the loop and assign the value in the list
        else:
            print("Position is already occupied, pick a different one")
            #if it is not true remain in the while loop and ask for the input again
         # assign tha value in the list 
    game_board[position] = player
    display_board()
    


def check_game_is_over():
    check_if_win()
    check_if_tie()


def check_if_win():
  global winner
  row_winner = check_rows()
  coln_winner = check_coln()
  diagnol_winner = check_diagnols()
  if row_winner:
      winner = row_winner
  elif coln_winner:
      winner = coln_winner
  elif diagnol_winner:
      winner = diagnol_winner
  else:
      winner = None
  return
 
    
def check_if_tie():
    global game_still_going
    if "-" not in game_board:
        game_still_going = False
        
    return
    
def flip_player():
    #accessing the global variable
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_rows():
    global game_still_going
    row1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row3 = game_board[6] == game_board[7] == game_board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return game_board[0]
    if row2:
        return game_board[3]
    if row3:
        return game_board[6]
    return
def check_coln():
    global game_still_going
    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return game_board[0]
    if column_2:
        return game_board[1]
    if column_3:
        return game_board[2]
    return
def check_diagnols():
    global game_still_going
    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return game_board[0]
    if diagonal_2:
        return game_board[6]
    return

play_game()