def initialise_board(size = 8 ):
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
    return(board)
def print_board(board):
    print('', ['  0  ','  1  ','  2  ','  3  ','  4  ','  5  ','  6  ','  7  '])
    for i in range(len(board)):
        print(i , board[i])
def check_length(x_direction,y_direction,start_coord,colour,board):
    print("CHECK LENGTH ------------------------------------")
    current_coord = start_coord
    #print("made it to check length")
    if colour == 'Dark ':
        opp_colour = 'Light'
    elif colour == 'Light':
        opp_colour = 'Dark '
    print(x_direction,y_direction)
    current_coord[0] +=x_direction
    current_coord[1] +=y_direction
    print(board[current_coord[0]][current_coord[1]],current_coord[0],current_coord[1])
    #print(current_coord)
    while board[current_coord[0]][current_coord[1]] == opp_colour:
        print(current_coord)
        current_coord[0] += x_direction
        current_coord[1] += y_direction
        if current_coord[0] >= len(board) or current_coord[0] < 0 :
            return False
        if current_coord[1] >= len(board) or current_coord[1] < 0 :
            return False
        #print(current_coord)
    if board[current_coord[0]][current_coord[1]] == colour:
        print(current_coord)
        return (True)
    else:
        print("CL = False")
        return(False)

def legal_move(colour,coordinate = (0,0) ,board=[]):
    print("LEGAL MOVE -------------------------------------")
    diff_y = [-1,0,1]
    diff_x = [-1,0,1]
    legal = False
    if colour == 'Dark ':
        opp_colour = 'Light'
    elif colour == 'Light':
        opp_colour = 'Dark '
    if (board[coordinate[0]][coordinate[1]]) == 'None ':
        for i in range(len(diff_y)):
            for item in range(len(diff_x)):
                if diff_y[i] == 0 and diff_x[item] == 0:
                    a =0
                #print(len(board))
                #else: 
                    #print(board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]],diff_x[item],diff_y[i])
                #print(coordinate[0]+diff_x[item] < len(board))
                if coordinate[0]+diff_x[item] < 8 and coordinate[0]+diff_x[item] >= 0 : #53 + 54 checks if coordinate to be checked is on the board
                    if coordinate[1]+diff_y[i] < 8 and coordinate[1]+diff_y[i] >= 0 :
                        #print_board(board)
                        #print(opp_colour,board[4][6])
                        #print("hello",board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]],[coordinate[0]+diff_x[item]],[coordinate[1]+diff_y[i]])
                        if board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]] == opp_colour:# Checks for square touching coordinate is opposite colour                        check_length(diff_x[item],diff_y[i],coordinate,board)# if it is it checks along line until free space is found
                            print(board[coordinate[0]+diff_x[item]][coordinate[1]+diff_y[i]],diff_x[item],diff_y[i])
                            legal = check_length(diff_x[item],diff_y[i],list(coordinate),colour,board)
                        if legal == True:
                            return(True)
    return(False)
def flip_peices(board,colour,coordinate = (0,0)):# coordinate is row,col
    print("FLIP_PEICES --------------------------------------")
    coordinate = list(coordinate)
    #print(coordinate)
    board[coordinate[0]][coordinate[1]] = colour
    #print(board[coordinate[0]][coordinate[1]],colour)
    if colour == 'Dark ':
        opp_colour ='Light'
    else:
        opp_colour = 'Dark '
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
                potential_direc.append([row_around,col_around])
    print(potential_direc,"HAVE to check in these directions")
    Reset_coordinate = coordinate
    for i in range (len(potential_direc)):
        coordinate = Reset_coordinate.copy()
        print("STart: ", coordinate)
        print("FOr direct",potential_direc[i])
        print("Checking square", coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1])#row,col
        Maybe = [] # empty list to store 
        Flip = False
        Attempt = False
        Loop = 0
        while Attempt  == False:
            Loop+=1
            print(Loop)
            #print(Maybe)
            if Flip == True:
                for i in range(len(Maybe)):
                    print("Im FLipping it", Maybe[i][0],Maybe[i][1],board[Maybe[i][0]][Maybe[i][1]])
                    board[Maybe[i][0]][Maybe[i][1]] = colour
                print("SET attempt to True")
                Attempt = True
            elif -1 <coordinate[1]+potential_direc[i][1] < 8 :
                if -1 <coordinate[0]+potential_direc[i][0]<8:
                    print([coordinate[0]+potential_direc[i][0]],[coordinate[1]+potential_direc[i][1]],"hello",board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]])
                    if board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] == colour:
                        print("Correct Colour")
                        Flip = True
                    elif board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] != opp_colour:
                        Attempt = True
                    else:
                        Maybe.append([coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1]])
                        print("Checked",coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1] )
                else:
                    Attempt =True
            else:
                Attempt =True
            if Attempt != True :
                coordinate[1] = coordinate[1]+potential_direc[i][1]
                coordinate[0] = coordinate[0]+potential_direc[i][0]
        print(Maybe)
    return (board)
def Count_flip(board,colour,coordinate = (0,0)):# coordinate is row,col
    print("Counting --------------------------------------")
    Sum = 0
    coordinate = list(coordinate)
    #print(coordinate)
    #print(board[coordinate[0]][coordinate[1]],colour)
    if colour == 'Dark ':
        opp_colour ='Light'
    else:
        opp_colour = 'Dark '
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
    print(potential_direc,"HAVE to check in these directions")
    Reset_coordinate = coordinate
    for i in range (len(potential_direc)):
        coordinate = Reset_coordinate.copy()
        print("STart: ", coordinate)
        print("FOr direct",potential_direc[i])
        print("Checking square", coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1])#row,col
        Maybe = [] # empty list to store 
        Flip = False
        Attempt = False
        Loop = 0
        while Attempt  == False:
            Loop+=1
            if Loop < 100:
                print(Loop)
                #print(Maybe)
                if Flip == True:
                    for i in range(len(Maybe)):
                        Sum +=1 
                    print("SET attempt to True")
                    Attempt = True
                elif -1 <coordinate[1]+potential_direc[i][1] < 8 :
                    if -1 <coordinate[0]+potential_direc[i][0]<8:
                        print([coordinate[0]+potential_direc[i][0]],[coordinate[1]+potential_direc[i][1]],"hello",board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]])
                        if board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] == colour:
                            print("Correct Colour")
                            Flip = True
                        elif board[coordinate[0]+potential_direc[i][0]][coordinate[1]+potential_direc[i][1]] != opp_colour:
                            Attempt = True
                        else:
                            Maybe.append([coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1]])
                            #print("Checked",coordinate[0]+potential_direc[i][0],coordinate[1]+potential_direc[i][1] )
                    else:
                        Attempt =True
                else:
                    Attempt =True
                if Attempt != True :
                    coordinate[1] = coordinate[1]+potential_direc[i][1]
                    coordinate[0] = coordinate[0]+potential_direc[i][0]
        print(Maybe)
    return (board,Sum)
board = initialise_board()

#board = [['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'Dark ', 'Light', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'Light', 'Dark ', 'Dark ', 'Dark ', 'None '], ['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None '], ['None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ', 'None ']]
#print_board(board)
#print(board[4][7])
#print(legal_move('Light',(4,7),board))
#print(board)
