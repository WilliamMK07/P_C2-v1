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
        y = int(request.args.get('y'))-1
    if components.legal_move(colour,(y,x),board) is True:
        components.logging(f"{colour} moved")
        new_board = components.flip_peices(board,colour,(y,x))
        board = new_board
        Counter -=1
        status = "success"
        if colour == 'Dark ':
            colour = 'Light'
        else:
            colour = 'Dark '
        if not has_legal_moves(board, colour):
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '
            if not has_legal_moves(board, colour):
                who = winner(board)
                print("Both teams have no moves")
                return{'finished': f"Team {who}has won",'board':board}

        if AI and has_legal_moves(board, AIcolour):
            components.logging(f"{colour} moved")
            ai_move_select(board, AIcolour)
            Counter -= 1
            if not has_legal_moves(board, colour) and not has_legal_moves(board, AIcolour):
                who = winner(board)
                print("AI Has no moves")
                return{'finished': f"Team {who}has won",'board':board}
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '     
    else:
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
    if AI is True:
        AI = False
    elif AI is False:
        AI = True
    if colour == 'Dark ':
        AIcolour = 'Light'
    else :
        AIcolour = 'Dark '

    return{}
@app.route('/save')
def save():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    with open('Information.json','w') as file:
        json.dump({'Board': board,'Colour':colour,'Count':Counter},file)
    components.logging("Made a save")
    return jsonify({'status':'saved'})
@app.route('/load', methods=['GET'])
def load():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    with open('Information.json','r') as file:
        data = json.load(file)
        print(board)
        board = data['Board']
        print(board)
        Counter = data['Count']
        colour = data['Colour']
    components.logging("Loaded data")
    return({'status':'loaded','Board':board})#
@app.route('/new', methods=['GET'])
def new():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    board = components.initialise_board()
    colour = 'Dark '
    Counter = 60
    AIcolour = 'Light'
    
    return({'status':'Creating','Board':board})
def ai_move_select(board,ai_colour):
    bestflip = [0,'']
    #print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 'None ':
                pot_flip = components.count_flip(board,ai_colour,(y,x))
                #print(Pot_flip)
                if pot_flip[1] > bestflip[0]:
                    bestflip[0] = pot_flip[1]
                    bestflip[1] = (y,x)
                    print(bestflip)
    board = components.flip_peices(board,ai_colour,bestflip[1])
def has_legal_moves(board, colour):
    for y in range(len(board)):
        for x in range(len(board)):
            if components.legal_move(colour, (y, x), board):
                return True
    return False
def winner(board):
    dark_count = 0
    light_count = 0
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 'Dark ':
                dark_count+=1
            if board[y][x] == 'Light':
                light_count+=1
    if light_count > dark_count :
        return("Light won", light_count,"to ", dark_count)
    if light_count < dark_count :
        return("Dark won", dark_count,"to ", light_count)
    else:
        return("It was a draw", dark_count ," to ", light_count)
if __name__ == '__main__':
    app.run()
