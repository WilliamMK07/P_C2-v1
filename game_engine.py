"""
The prpose of this file is to run a simple version of the game using modules from components
"""
from components import *
def cli_coords_input():
    """
    Docstring for cli_coords_input
    Used to take the inputs of the player of position they choose
    """
    while True:
        try:
            y = int(input("Enter Coordinate of row  0 - 7"))
            x = int(input("Enter Coordinates of column 0 - 7 "))
            if 0<=y<8:
                if 0<=x<8: # validates input is in correct range
                    break
        except ValueError: # catches errors if user inputs wrong value
            print("Incorrect format") 
            logging("--------------------- \n User entered invalid coordinates \n---------------------") # adds error to log
    return((x,y))#in order col,row

def simple_game_loop():
    """
    Docstring for simple_game_loop
    This runs the game as a test to see if it all functions as intended 
    in terminal
    """
    print("Hello game has started ")
    board = initialise_board()
    moves = 60 #sets moves to 60
    colour = 'Dark '#sets first move to dark
    print("Step 1")
    while moves != 0:
        if has_legal_moves(board,colour) is False: # checks if legal move for colour
            print("No available moves")
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '
        print_board(board)
        if has_legal_moves(board,colour) is False: # checks if legal move for colour after swapping
            print("No available moves") # if both dont exits game loop and outputs winner
            break
        while True: # loops until user enters a legal move
            print(colour,":")
            coords =cli_coords_input()#(in order row,col)
            if legal_move(colour,(coords[1],coords[0]),board) is True:
                break # once legal move chosen breaks loop
            else:
                logging(("--------------------- \n User entered coordinates that are not a legal move\n---------------------"))
        board = flip_peices(board,colour,(coords[1],coords[0]))# makes move
        moves -= 1
        if colour == 'Dark ': # switches colour
            colour = 'Light'
        else:
            colour = 'Dark '
        #print_board(board)
    #once game finish display winner
    light_count = 0
    dark_count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'Light':
                light_count += 1
            elif board[row][col] == 'Dark ':
                dark_count += 1
    #counts amount of tiles each colour has
    if light_count > dark_count :
        print("Light won", light_count,"to ", dark_count)
    if light_count < dark_count :
        print("Dark won", dark_count,"to ", light_count)
    else:
        print("It was a draw", dark_count ," to ", light_count)
    #prints winner
simple_game_loop()
