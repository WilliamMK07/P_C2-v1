"""Holds the key functions required for game to run"""
import os
def initialise_board(size = 8 ):
    """
    Docstring for initialise_board
    
    :param size: Holds the amount of rows/columns to make board off of is default 8
    """
    board = [['None ' for i in range(size)] for item in range(size)]
    #for i in range(len(board)):
    #    print(board[i])
    mid_row = size//2 -1
    #print(mid_row)
    board[mid_row][mid_row] = 'Dark '
    board[mid_row+1][mid_row+1] = 'Dark '
    board[mid_row+1][mid_row] = 'Light'
    board[mid_row][mid_row+1] = 'Light'
    #for i in range(len(board)):
    #    print(board[i])
    logging("\n\n NEW GAME")
    return board
def print_board(board):
    """Displaying the board"""
    print('', ['  0  ','  1  ','  2  ','  3  ','  4  ','  5  ','  6  ','  7  '])
    for i in range(len(board)):
        print(i , board[i])
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
    current_coord[0] +=x_direction
    current_coord[1] +=y_direction
    #print(board[current_coord[0]][current_coord[1]],current_coord[0],current_coord[1])
    #print(current_coord)
    while board[current_coord[0]][current_coord[1]] == opp_colour:
        #print(current_coord)
        current_coord[0] += x_direction
        current_coord[1] += y_direction
        if current_coord[0] >= len(board) or current_coord[0] < 0 :
            return False
        if current_coord[1] >= len(board) or current_coord[1] < 0 :
            return False
        #print(current_coord)
    if board[current_coord[0]][current_coord[1]] == colour:
        #print(current_coord)
        return True
    else:
        #print("CL = False")
        return False
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
    diff_x = [-1,0,1]
    legal = False
    opp_colour = 'Light'
    if colour == 'Dark ':
        opp_colour = 'Light'
    elif colour == 'Light':
        opp_colour = 'Dark '
    if (board[coordinate[0]][coordinate[1]]) == 'None ':
        for i in range(len(diff_y)):
            for item in range(len(diff_x)):
                if diff_y[i] == 0 and diff_x[item] == 0:
                    pass
                elif coordinate[0]+diff_x[item] < 8 and coordinate[0]+diff_x[item] >= 0 : #53 + 54 checks if coordinate to be checked is on the board
                    if coordinate[1]+diff_y[i] < 8 and coordinate[1]+diff_y[i] >= 0 :
                        if board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]] == opp_colour:# Checks for square touching coordinate is opposite colour
                            legal = check_length(diff_x[item],diff_y[i],list(coordinate),colour,board)
                        if legal is True:
                            return True
    return False
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
    reset_coordinate = coordinate
    for i in range (len(potential_direc)):
        coordinate = reset_coordinate.copy()
        maybe = []# empty list to store
        flip = False
        attempt = False
        loop = 0
        while attempt  is False:
            loop+=1
            print(loop)
            #print(maybe)
            if flip is True:
                for i in range(len(maybe)):
                    board[maybe[i][0]][maybe[i][1]] = colour
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
                else:
                    attempt =True
            else:
                attempt =True
            if attempt is not True :
                coordinate[1] = coordinate[1]+potential_direc[i][1]
                coordinate[0] = coordinate[0]+potential_direc[i][0]
        #print(maybe)
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
    sum = 0
    coordinate = list(coordinate)
    #print(coordinate)
    #print(board[coordinate[0]][coordinate[1]],colour)
    if colour == 'Dark ':
        opp_colour ='Light'
    else:
        opp_colour = 'Dark '
    potential_direc = poi_coordinate(board,coordinate,opp_colour)
    #print(potential_direc,"HAVE to check in these directions")
    reset_coordinate = coordinate
    for i in range (len(potential_direc)):
        coordinate = reset_coordinate.copy()
        maybe = [] # empty list to store 
        flip = False
        attempt = False
        loop = 0
        while attempt  is False:
            loop+=1
            if loop < 100:
                #print(Loop)
                #print(maybe)
                if flip is True:
                    for i in range(len(maybe)):
                        sum +=1 
                    #print("SET attempt to True")
                    attempt = True
                elif -1 <coordinate[1]+potential_direc[i][1] < 8 :
                    if -1 <coordinate[0]+potential_direc[i][0]<8:
                        #print([coordinate[0]+potential_direc[i][0]],[coordinate[1]+potential_direc[i][1]],"hello",board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]])
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
    potential_direc = []
    for row_around in range(-1,2):
        for col_around in range(-1,2):
            if coordinate[0]+row_around >7:
                print("Out of Row > 7")
            elif coordinate[0]+row_around <0:
                print("Out of Row < 0 ")
            elif coordinate[1]+col_around >7:
                print("Out of col > 7")
            elif coordinate[1]+col_around <0:
                print("Out of col < 0 ")
            elif board[coordinate[0]+row_around][coordinate[1]+col_around] == opp_colour:
                if [row_around,col_around] != [0,0]:
                    potential_direc.append([row_around,col_around])
    return potential_direc
def logging(update):
    """
    This takes in string of what needs to be saved to log file.
    """
    #print("Ia m logging it")
    filename = "logging.txt"
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path): # if file doesnt exist
        with open(file_path, "a") as file: #makes file
            file.write(update + "\n")
            print(file,"1")
    else:
        with open(file_path, "w") as file: # if file exists
            file.write(update +"\n") # adds to file
            print(file,"2")
