from flask import Flask, render_template, request,jsonify
import game_engine
import components 
import json
app = Flask(__name__)
board = components.initialise_board()
colour = 'Dark '
Counter = 60
AIcolour = 'Light'
AI = False

@app.route('/')
def index():
    return (render_template('Index.html',game_board = board,colour = 'Dark ',))

@app.route('/move', methods=['GET'])
def move():
    global board
    global colour
    global Counter
    global AI
    global AIcolour
    print(AI,"HELLO")
    if request.method == 'GET':
        x = int(request.args.get('x'))-1
        y = int(request.args.get('y'))-1
    if components.legal_move(colour,(y,x),board) == True:
        new_board = components.flip_peices(board,colour,(y,x))
        board = new_board
        Counter -=1
        status = "success"
        if not has_legal_moves(board, colour):
            if colour == 'Dark ':
                colour = 'Light'
            else:
                colour = 'Dark '
            if not has_legal_moves(board, colour):
                Winner(board)
                return{'finished':True}

        if AI and has_legal_moves(board, AIcolour):
            AI_Move_Select(board, AIcolour)
            Counter -= 1
            if not has_legal_moves(board, colour) and not has_legal_moves(board, AIcolour):
                Winner(board)
                return{'finished':True}
        
    else:
        status = 'fail'
        print("Cant move there")
    return{"status": status,
  "board": board,"player":colour,
}
@app.route('/AI', methods=['GET'])
def AI_toggle():
    global board
    global colour
    global Counter
    global AIcolour
    global AI
    if AI == True:
        AI = False
    elif AI == False:
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
    
    return({'status':'Creating','Board':board})#
def AI_Move_Select(board,Ai_colour):
    Bestflip = [0,'']
    #print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 'None ':
                Pot_flip = components.Count_flip(board,Ai_colour,(y,x))
                #print(Pot_flip)
                if Pot_flip[1] > Bestflip[0]:
                    Bestflip[0] = Pot_flip[1]
                    Bestflip[1] = (y,x)
                    print(Bestflip)
    components.flip_peices(board,Ai_colour,Bestflip[1])
def has_legal_moves(board, colour):
    for y in range(len(board)):
        for x in range(len(board)):
            if components.legal_move(colour, (y, x), board):
                return True
    return False
def Winner(board):
    dark_count = 0
    light_count = 0
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 'Dark ':
                dark_count+=1
            if board[y][x] == 'Light':
                light_count+=1
    if light_count > dark_count :
        print("Light won", light_count,"to ", dark_count)
    if light_count < dark_count :
        print("Dark won", dark_count,"to ", light_count)
    else:
        print("It was a draw", dark_count ," to ", light_count)
if __name__ == '__main__':
    app.run()
    