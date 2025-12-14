import os
import json
from flask import Flask, render_template, request,jsonify
import components
app = Flask(__name__)
board = components.initialise_board()
colour = 'Dark '
Counter = 60
AIcolour = 'Light'
AI = False

@app.route('/')
def index():
    """
    Docstring for index
    Uses function in index to display the board and take in player
    colour to be used to display correct messages
    """
    return render_template('Index.html',game_board = board,colour = 'Dark ',)

@app.route('/move', methods=['GET'])
def move():
    """
    Docstring for move
    This uses the html to recieve the coordinates user has selected
    """
    #print(os.getcwd())
    global board
    global colour
    global Counter
    global AI
    global AIcolour
    print(AI,"HELLO")
    if request.method == 'GET':
        x = int(request.args.get('x'))-1
        y = int(request.args.get('y'))-1# -1 as i used 0-7 not 1-8
    if components.legal_move(colour,(y,x),board) is True: # is move legal
        components.logging(f"{colour} moved")
        new_board = components.flip_peices(board,colour,(y,x)) # make move
        board = new_board
        Counter -=1
        status = "success"
        opp_colour = colour
        if colour == 'Dark ': #switch colour
            colour = 'Light'
        else:
            colour = 'Dark '
        if not components.has_legal_moves(board, colour): # if other colour has no moves
            if colour == 'Dark ': # switch colour back
                colour = 'Light'
            else:
                colour = 'Dark '
            if not components.has_legal_moves(board, colour): # if both colours have no moves
                who = winner(board) # end game
                print("Both teams have no moves")
                return{'finished': f"Team {who}has won",'board':board}

        if AI and components.has_legal_moves(board, AIcolour): # if ai is on and has legal move
            components.logging(f"{colour} moved")
            ai_move_select(board, colour) # make best move
            opp_colour = colour
            if colour == 'Dark ': # switch colour
                colour = 'Light'
            else:
                colour = 'Dark '
            Counter -= 1
        if not components.has_legal_moves(board, colour) and not components.has_legal_moves(board, opp_colour): 
            # if both colours have no legal moves end game
            who = winner(board)
            print("AI Has no moves")
            print("Player has no moves")
            return{'finished': f"Team {who}has won",'board':board}    
    else: # incorrect coordinate given ouptuts error
        status = 'fail'
        print("Cant move there")
        components.logging(("--------------------- \n User entered coordinates that are not a legal move\n---------------------"))
    return{"status": status,
  "board": board,"player":colour,
} 
@app.route('/AI', methods=['GET'])
def ai_toggle():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    if AI is True: # turns ai off if already on
        components.logging(("AI turned off"))
        AI = False
    elif AI is False: # turns ai on if already off
        components.logging(("AI turned on"))
        AI = True
    return{}
@app.route('/save')
def save():
    global board
    global colour
    global Counter
    with open('Information.json','w') as file:
        json.dump({'Board': board,'Colour':colour,'Count':Counter},file) # converts to json and store all in file
    components.logging("Made a save")
    return jsonify({'status':'saved'})
@app.route('/load', methods=['GET'])
def load():
    global board
    global colour
    global Counter
    with open('Information.json','r') as file: # loads all data and saves to corresponding variable
        data = json.load(file)
        print(board)
        board = data['Board']
        print(board)
        Counter = data['Count']
        colour = data['Colour']
    components.logging("Loaded data")
    return({'status':'loaded','Board':board})#
@app.route('/new', methods=['GET']) # ran when reset is clicked
def new():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    board = components.initialise_board() #creates empty board
    colour = 'Dark ' # resets all variables
    Counter = 60
    return({'status':'Creating','Board':board})# to be outputted
def ai_move_select(board,ai_colour):
    bestflip = [0,'']
    #print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 'None ': # checks whole board for empty squares
                pot_flip = components.count_flip(board,ai_colour,(y,x)) # gets the amount of flips made by each move
                #print(Pot_flip)
                if pot_flip[1] > bestflip[0]: # compares new amount to temp storage to see if new flip is better
                    bestflip[0] = pot_flip[1] # if it is sets new temp score to new score
                    bestflip[1] = (y,x) # saves coordinate of flip
                    #print(bestflip)
                # this is repeated for everymove to find move that flips most amount of peices
    board = components.flip_peices(board,ai_colour,bestflip[1]) # makes the best move
def winner(board):
    dark_count = 0
    light_count = 0
    for y in range(len(board)):
        for x in range(len(board)): # count which team has most peices
            if board[y][x] == 'Dark ':
                dark_count+=1
            if board[y][x] == 'Light':
                light_count+=1
    if light_count > dark_count : #compare and output the winner
        components.logging(f"light won{light_count} to{dark_count}" )
        return("Light won", light_count,"to ", dark_count)
    if light_count < dark_count :
        components.logging(f"dark won{dark_count} to{light_count}" )
        return("Dark won", dark_count,"to ", light_count)
    else:
        components.logging(f"It was a draw {dark_count} to {light_count}" )
        return("It was a draw", dark_count ," to ", light_count)
if __name__ == '__main__':
    app.run()
