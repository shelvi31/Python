import numpy
import random

# Creates an empty board
def create_board():
    board = numpy.zeros((3,3), dtype=int)
    return board


def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

# board = create_board()
# place(board, 1, (0, 0))          #used place to have Player 1 place a marker on location (0, 0)


# Check for empty place on the board
def possibilities(board):        #could also use np.where(board == 0)
    l = []
    
    for i in range(len(board)): 
        for j in range(len(board)):
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l)


# Select a random place for the player
random.seed(1) 
def random_place(board, player): 
    selection = possibilities(board) 
    current_loc = random.choice(selection) 
    place(board, player, current_loc)
    return board



# #PRINTING BOARD WITH 5 MOVES
# random.seed(1)
# board = create_board()
# for i in range(5):
#     for player in [1, 2]:
#         random_place(board, player)
# # print(board)

 
# Checks whether the player has three  of their marks in a horizontal row
def row_win(board, player):
    if numpy.any(numpy.all(board==player, axis=1)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False
# print(row_win(board, 1))


# Checks whether the player has three of their marks in a vertical row 
def col_win(board, player):
    if numpy.any(numpy.all(board==player, axis=0)): # this checks if any column contains all positions equal to player
        return True
    else:
        return False
#print(col_win(board, 1))


# Checks whether the player has three of their marks in a diagonal row 
def diag_win(board, player):
    if numpy.all(numpy.diag(board)==player) or numpy.all(numpy.diag(numpy.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False
# print(diag_win(board, 2))


# Evaluates whether there is a winner or a tie 
def evaluate(board): 
    winner = 0
      
    for player in [1, 2]: 
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)): 
                 
            winner = player 
              
    if numpy.all(board != 0) and winner == 0: 
        winner = -1
    return winner


# Main function to start the game 
random.seed(1)

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

# results = [play_game() for i in range(1000)]               #Harvardx answer code
# results.count(1)


# #Improving Player 1 strategy : where Player 1 always starts with the middle square
# def play_strategic_game():       
#     board = create_board()
#     place(board, 1, (1, 1))

#     winner = 0
#     while winner == 0:
#         for player in [1, 2]:
#             random_place(board, player)
#             winner = evaluate(board)
#             if winner != 0:
#                 break
#     return winner


#Improving Player 1 strategy : where Player 1 always starts with the middle square
random.seed(1)
def play_strategic_game():
    board, winner, counter = create_board(), 0, 1 
      
    while winner == 0: 
        for player in [1, 2]:
            place(board, 1, (1, 1))
            board = random_place(board, player)
            # print(board)
            counter += 1
            winner = evaluate(board) 
            if winner != 0: 
                break
    return(winner)


#Driver Code 

player1_win = 0
player2_win = 0
random.seed(1)
for z in range(1000):
    wingame = play_strategic_game()
    if wingame == 1:
        player1_win += 1
    if wingame == 2: 
        player2_win += 1    
    else:
        pass

print(player1_win, player2_win)

if player1_win > player2_win:
    print("winner is player 1")
elif player1_win == player2_win:
    print("there is a tie")
else:
    print("winner is player 2")