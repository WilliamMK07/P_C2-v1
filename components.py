"""Holds the key functions required for game to run"""
import os
from datetime import datetime

def initialise_board(size = 8 ):
    """
    Docstring for initialise_board
    
    :param size: Holds the amount of rows/columns to make board off of is default 8
    """
    board = [['None ' for i in range(size)] for item in range(size)] 
    # creates 8*8 board of 'None '
    mid_row = size//2 -1
    #finds middle of board
    board[mid_row][mid_row] = 'Dark '
    board[mid_row+1][mid_row+1] = 'Dark '
    board[mid_row+1][mid_row] = 'Light'
    board[mid_row][mid_row+1] = 'Light'
    # adds the center squares 
    logging("\n\n NEW GAME")
    return board
def print_board(board):
    """Displaying the board"""
    print('', ['  0  ','  1  ','  2  ','  3  ','  4  ','  5  ','  6  ','  7  '])
    # helps user identify which column they are trying to select
    for i in range(len(board)):
        print(i , board[i])# prints row number then row
def check_length(x_direction,y_direction,start_coord,colour,board):
    """
    Docstring for check_length
    
    :param x_direction: which x direct needs to be checked
    :param y_direction: which x direct needs to be checked
    :param start_coord: The position to start checking from
    :param colour: WHich colour the plyer is 
    :param board: Holds the board to be used to check move length
    """
    #print("CHECK LENGTH ------------------------------------")
    current_coord = start_coord
    #print("made it to check length")
    opp_colour = 'Light'
    if colour == 'Dark ':
        opp_colour = 'Light'
    elif colour == 'Light':
        opp_colour = 'Dark '
    #print(x_direction,y_direction)
    current_coord[0] +=x_direction # adds the direction onto position
    current_coord[1] +=y_direction
    #print(board[current_coord[0]][current_coord[1]],current_coord[0],current_coord[1])
    #print(current_coord)
    while board[current_coord[0]][current_coord[1]] == opp_colour:
        #continuously checks if position is still opposite colour
        current_coord[0] += x_direction
        current_coord[1] += y_direction
        #adds the direction onto new position
        if current_coord[0] >= len(board) or current_coord[0] < 0 :
            return False
        if current_coord[1] >= len(board) or current_coord[1] < 0 :
            return False
        #checks if still on board
    #once position no longer opp colour for move to be valid it has to
    #be the players colour
    if board[current_coord[0]][current_coord[1]] == colour:
        return True # if it is players colour the direction was valid
    else:
        #print("CL = False")
        return False # if not it doesnt work
def legal_move(colour,coordinate = (0,0),board = []):
    """
    Docstring for legal_move
    Checks if users entered coordinate is a legal move
    :param colour: Colour of player is held 'Light' or 'Dark '
    :param coordinate: Position player has chosen that needs to be checked
    :param board: Current state of board
    """
    #print("LEGAL MOVE -------------------------------------")
    diff_y = [-1,0,1]
    diff_x = [-1,0,1]# define all different x directions
    legal = False
    # get the opposite colour
    opp_colour = 'Light'
    if colour == 'Dark ':
        opp_colour = 'Light'
    elif colour == 'Light':
        opp_colour = 'Dark '
    if (board[coordinate[0]][coordinate[1]]) == 'None ': # checks selected square is 'None' As required
        for i in range(len(diff_y)):
            for item in range(len(diff_x)): 
                if diff_y[i] == 0 and diff_x[item] == 0: # ignores when it checks starting square
                    pass
                elif coordinate[0]+diff_x[item] < 8 and coordinate[0]+diff_x[item] >= 0 : #89 + 90 checks if coordinate to be checked is on the board
                    if coordinate[1]+diff_y[i] < 8 and coordinate[1]+diff_y[i] >= 0 :
                        if board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]] == opp_colour:# Checks for square touching coordinate is opposite colour
                            legal = check_length(diff_x[item],diff_y[i],list(coordinate),colour,board)
                        if legal is True:
                            return True# will stop as soon as it finds one valid argument
    return False# if no valid arguments found will return false
def flip_peices(board,colour,coordinate = (0,0)):# coordinate is row,col
    """
    Docstring for flip_peices
    
    :param board: Current state of the board
    :param colour: colour of player
    :param coordinate: Starting position of peice
    """
    #print("FLIP_PEICES --------------------------------------")
    coordinate = list(coordinate)
    #print(coordinate)
    board[coordinate[0]][coordinate[1]] = colour
    #print(board[coordinate[0]][coordinate[1]],colour)
    if colour == 'Dark ':
        opp_colour ='Light'
    else:
        opp_colour = 'Dark '
    potential_direc = poi_coordinate(board,coordinate,opp_colour)
    #returns all directions around start square that are opposite colour
    reset_coordinate = coordinate
    #stores the original coordinate
    for i in range (len(potential_direc)): # for each direction
        coordinate = reset_coordinate.copy() # resets coordinat to start
        maybe = []# empty list to store
        flip = False
        attempt = False
        while attempt is False:
            #print(maybe)
            if flip is True: # once direction is found tp be valid
                for i in range(len(maybe)): # for each square checked
                    board[maybe[i][0]][maybe[i][1]] = colour # set to players colour
                #print("SET attempt to True")
                attempt = True # ends while loop
            elif -1 <coordinate[1]+potential_direc[i][1] < 8 : # checks position still on board to prevent error
                if -1 <coordinate[0]+potential_direc[i][0]<8:
                    if board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] == colour:
                        #if finds player colour direction is true
                        flip = True # will trigger flip
                    elif board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] != opp_colour:
                        attempt = True # if it isnt player colour or opposite colour direction 
                        #is not valid so ends check for this direc
                    else:
                        maybe.append([coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1]])
                        #if is opp colour stores incase needed to be flipped
                else:
                    attempt =True # if outside board direc is not valid
            else:
                attempt =True# if outside board direc is not valid
            if attempt is not True : # moves along to next square if direction not proven valid or invalid
                coordinate[1] = coordinate[1]+potential_direc[i][1]
                coordinate[0] = coordinate[0]+potential_direc[i][0]
    return board
def count_flip(board,colour,coordinate = (0,0)):# coordinate is row,col
    """
    Docstring for count_flip
    The minor difference is this will rturn the length of the flip and will not flip the peices this is required to make ai wor
    :param board: Current state of the board
    :param colour: colour of player
    :param coordinate: Starting position of peice
    """
    #print("Counting --------------------------------------")
    sum = 0 # sum is set before loops as purpose is to obtain total amount of peices flipped by one move
    #so needs to be tallied for each direction
    coordinate = list(coordinate)
    #print(coordinate)
    #print(board[coordinate[0]][coordinate[1]],colour)
    if colour == 'Dark ':
        opp_colour ='Light'
    else:
        opp_colour = 'Dark '
    potential_direc = poi_coordinate(board,coordinate,opp_colour)
    #returns all directions around start square that are opposite colour
    reset_coordinate = coordinate
    #stores the original coordinate 
    for i in range (len(potential_direc)): # for each direction
        coordinate = reset_coordinate.copy() # resets coordinat to start
        maybe = []# empty list to store
        flip = False
        attempt = False
        while attempt is False:
            if flip is True:
                for i in range(len(maybe)):
                    sum +=1 # once a direction is valid for each tile that would be flipped is added on to sum
                #print("SET attempt to True")
                attempt = True
            elif -1 <coordinate[1]+potential_direc[i][1] < 8 :
                if -1 <coordinate[0]+potential_direc[i][0]<8:
                    if board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] == colour:
                        #print("Correct Colour")
                        flip = True
                    elif board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] != opp_colour:
                        attempt = True
                    else:
                        maybe.append([coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1]])
                        #print("Checked",coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1] )
                else:
                    attempt =True
            else:
                attempt =True
            if attempt is not True :
                coordinate[1] = coordinate[1]+potential_direc[i][1]
                coordinate[0] = coordinate[0]+potential_direc[i][0]
        #print(maybe)
    return (board,sum)
def poi_coordinate(board,coordinate,opp_colour):
    """
    Docstring for poi_coordinate
    This returns list of all directions around a coordinate where 
    opposite colours is as that is direction needed to be checked 
    :param board: current version of board
    :param coordinate: Position on board needed to be checked
    :param opp_colour: Colour of peices that could potentially be flipped
    """
    potential_direc = [] # empty list to store all directions as ['','']
    for row_around in range(-1,2):
        for col_around in range(-1,2):
            if coordinate[0]+row_around >7:
                pass
                #print("Out of Row > 7")
            elif coordinate[0]+row_around <0:
                pass
                #print("Out of Row < 0 ")
            elif coordinate[1]+col_around >7:
                pass
                #print("Out of col > 7")
            elif coordinate[1]+col_around <0: # lines 212 - 223 are to ensure it only checks positions on the board to prevent errors
                #print("Out of col < 0 ")
                pass
            elif board[coordinate[0]+row_around][coordinate[1]+col_around] == opp_colour:
                if [row_around,col_around] != [0,0]: # stops it from entering own square
                    potential_direc.append([row_around,col_around])
    return potential_direc
def logging(update):
    """
    This takes in string of what needs to be saved to log file.
    """
    filename = "logging.log"
    update = update + " " + str(datetime.now().strftime("%H:%M:%S")) # adds a timestamp to the string 
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path): # if file doesnt exist
        with open(file_path, "a") as file: #makes file
            file.write(update + "\n")
            #print(file,"1")
    else:
        with open(file_path, "w") as file: # if file exists
            file.write(update +"\n") # adds to file
            #print(file,"2")

def has_legal_moves(board, colour):
    """
    Docstring for has_legal_moves
    This function will check whole board for if colour inputted has 
    a legal move available
    :param board: takes in current state of board
    :param colour: Takes in players colour
    """
    for y in range(len(board)):
        for x in range(len(board)):
            if legal_move(colour, (y, x), board): # checks each square of board searching for legal move
                return True # if found returns true
    return False # else will return false causing turn skip
