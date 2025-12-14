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
            break
        except ValueError:
            print("Incorrect format")
            logging("--------------------- \n User entered invalid coordinates \n---------------------")
    return((x,y))#in order col,row
def check_legal_move(board,colour):
    """
    Docstring for check_legal_move - checks if a move is legal
    returning true or false if it is or isnt
    
    :param board: Takes in current state of the board
    :param colour: current coour of player
    """
    if colour == 'Dark ':
        opp_colour = 'Light'
    else:
        opp_colour = 'Dark '
    opp_squares = []
    for row in range(len(board)):
        #print(board[row])
        for column in range(len((board[row]))):
            #print(column)
            if board[row][column] == opp_colour :
                #print(row,column,"helle")
                in_list = False
                for i in range(len(opp_squares)):
                    if opp_squares[i] == [row,column]:
                        in_list = True
                if in_list is False:
                    opp_squares.append([row,column])
    #print(Opp_squares,"BBBBBBBBBBBBBBBBBBBBBBBBB")
    for i in range(len(opp_squares)):
        for row in range(-1,2):
            for col in range(-1,2):
                #print([row,col])
                if [row, col] !=[0,0]: # doesnt check sqare already selected
                    if opp_squares[i][0]+row >=8:
                        print("Out of Row > 8")
                    if opp_squares[i][0]+row <0:
                        print("Out of Row < 0 ")
                    if opp_squares[i][1]+col >=8:
                        print("Out of col > 8")
                    if opp_squares[i][1]+col <0:
                        print("Out of col < 0 ")
                    elif board[opp_squares[i][0]+row][opp_squares[i][1]+col] == 'None ':
                        legal=legal_move(colour,(opp_squares[i][0]+row,opp_squares[i][1]+col),board)
                        if legal is True:
                            return True
                    #if board[i[0]row ]
    return False

def simple_game_loop():
    """
    Docstring for simple_game_loop
    This runs the game as a test to see if it all functions as intended 
    in terminal
    """
    print("Hello game has started ")
    board = initialise_board()
    moves = 60
    colour = 'Dark '
    print("Step 1")
    while moves != 0:
        if check_legal_move(board,colour) is False:
            print("No available moves")
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '
        print_board(board)
        while True:
            print(colour,":")
            coords =cli_coords_input()#(in order row,col)
            if legal_move(colour,(coords[1],coords[0]),board) is True:
                break
            else:
                logging(("--------------------- \n User entered coordinates that are not a legal move\n---------------------"))
        board = flip_peices(board,colour,(coords[1],coords[0]))
        print(board[4][3])
        moves -= 1
        if colour == 'Dark ':
            colour = 'Light'
        else:
            colour = 'Dark '
        #print_board(board)
    light_count = 0
    dark_count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'Light':
                light_count += 1
            elif board[row][col] == 'Dark ':
                dark_count += 1
    if light_count > dark_count :
        print("Light won", light_count,"to ", dark_count)
    if light_count < dark_count :
        print("Dark won", dark_count,"to ", light_count)
    else:
        print("It was a draw", dark_count ," to ", light_count)
simple_game_loop()
