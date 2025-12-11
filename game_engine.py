from components import *
def cli_coords_input():
    while True:
            y = int(input("Enter Coordinate of row  0 - 7"))
            x = int(input("Enter Coordinates of column 0 - 7 "))
            break
    return((x,y))#in order col,row
def check_legal_move(board,colour):
    if colour == 'Dark ':
        Opp_colour = 'Light'
    else:
        Opp_colour = 'Dark '
    Opp_squares = []
    for row in range(len(board)):
        #print(board[row])
        for column in range(len((board[row]))):
            #print(column)
            if board[row][column] == Opp_colour :
                #print(row,column,"helle")
                In_list = False
                for i in range(len(Opp_squares)):
                    if Opp_squares[i] == [row,column]:
                        In_list = True
                if In_list == False:
                    Opp_squares.append([row,column])
    #print(Opp_squares,"BBBBBBBBBBBBBBBBBBBBBBBBB")
    for i in range(len(Opp_squares)):
        for row in range(-1,2):
            for col in range(-1,2):
                #print([row,col])
                if [row, col] !=[0,0]: # doesnt check sqare already selected
                    if Opp_squares[i][0]+row >=8:
                        print("Out of Row > 8")
                    if Opp_squares[i][0]+row <0:
                        print("Out of Row < 0 ")
                    if Opp_squares[i][1]+col >=8:
                        print("Out of col > 8")
                    if Opp_squares[i][1]+col <0:
                        print("Out of col < 0 ")   
                    elif board[Opp_squares[i][0]+row][Opp_squares[i][1]+col] == 'None ':
                        legal = legal_move(colour,(Opp_squares[i][0]+row,Opp_squares[i][1]+col),board)
                        if legal == True:
                            return(True)
                    #if board[i[0]row ]
    return(False)

def simple_game_loop():
    print("Hello game has started ")
    board = initialise_board()
    moves = 60
    colour = 'Dark '
    print("Step 1")
    while moves != 0:
        if check_legal_move(board,colour) == False: 
            print("No available moves")
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '
        print_board(board)
        print(colour,":")
        Coords =cli_coords_input()#(in order row,col)
        board = flip_peices(board,colour,(y,x))
        print(board[4][3])
        moves -= 1
        if colour == 'Dark ':
            colour = 'Light' 
        else:
            colour = 'Dark '
        #print_board(board)
    Light_count = 0
    Dark_count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'Light':
                Light_count += 1
            elif board[row][col] == 'Dark ':
                Dark_count += 1
    if Light_count > Dark_count :
        print("Light won", Light_count,"to ", Dark_count)
    if Light_count < Dark_count :
        print("Dark won", Dark_count,"to ", Light_count)
    else:
        print("It was a draw", Dark_count ," to ", Light_count)
#simple_game_loop()

