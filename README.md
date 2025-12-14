# Readme

## Introduction

This is a readme file of all code in my 3 .py files there is additional changes to Index.html however will not be referenced in this document as all involve adding buttons and switches with all main code happening in the flask_game_engine so I did not feel justification was required.

The draw.io( website used to create flowcharts) will be included in zip file so if image is illegible it will be easy to view on there. Also some of my functions are rather similar so I have not created a flowchart to showcase these (e.g. count_flip and flip_peices) I will justify use of two functions although they do similar things.

## Components.py

### Initialise_board

In Flowchart 1 it shows the function Initialise board which is used to create the board it works with two for loops to create 8\*8 grid then the middle pieces are added as shown at bottom of flowchart.
<img width="403" height="720" alt="image" src="https://github.com/user-attachments/assets/f13a0a67-d825-48ef-b0a8-277e4e8220c6" />

<img width="940" height="386" alt="image" src="https://github.com/user-attachments/assets/d9df53cc-e432-406f-aaea-0500bd34dd73" />

This is the actual code for the function line 9 showcases the double for loops demonstrated in flowchart that will create the 8\*8 grid

### Print_board

As this is a simple function I didn’t create a flowchart for this however it works by looping through each row of the grid and outputting .
<img width="940" height="258" alt="image" src="https://github.com/user-attachments/assets/2491e301-0dff-495b-a00b-7525d2fef25a" />

I also added number labels to help user identify what row and column they want to select. As shown below:
<img width="940" height="166" alt="image" src="https://github.com/user-attachments/assets/36544ea2-ca5d-4507-9bdd-c3af2c19903b" />

It was also at this point I decided to use the python numbering with rows and cols starting from 0 as it should help with simplicity off coding.

### Check_length

This function is used to identify if in given direction the move is valid and will return response. It is used in legal move to identify if position player selected was legal.

In flowchart 2 it shows how the code will continuously check in direction given until either move is shown to be valid(finds player colour) or it is not (out of board or last square is ‘None’)
<img width="803" height="1086" alt="image" src="https://github.com/user-attachments/assets/2562ede0-9acf-4f77-b043-a846a189e0d8" />
<img width="940" height="852" alt="image" src="https://github.com/user-attachments/assets/1fb34f3c-880e-4bd8-b01d-cd241bd04930" />

This is the code for this section which shows how it will continue looping (line 49 – 57) until found square which is either not on board or is not the opp_colour. Then will return true if found square is player colour. The reason for using separate function was to help break down code into smaller modules as I had struggled with debugging this section as I kept running into logic errors.

### Legal_move

This code is used to test if coordinate user inputted is valid it works by checking all squares around there position and then using check_length on all directions around position that are opp_colour. As the purpose of this function was only to identify if a move is valid it will return true as soon as it finds that a move is legal it wont check all directions.
<img width="878" height="1166" alt="image" src="https://github.com/user-attachments/assets/3561db2b-6c63-4e64-acfa-dc60445c2615" />
<img width="940" height="414" alt="image" src="https://github.com/user-attachments/assets/499c756b-bd02-48c2-8d95-17e6f43720fb" />

The code for this section shows how since making flowchart I had to add line 84 to ensure that the starting square is ‘None’ as u were able to select previously used squares this is because when later functions check if a colour has a valid move it will check every square of board so this is required to filter out those tries. It shows how it uses 2 for loops to check each square around the start position and will return true as soon as valid argument found.

### Flip_peices

This function is similar to check_length as it is used to change all pieces that need to be changed for a given move. It uses the same function poi_coordinates which will be explained later but functions similarly to legal_moves part where it checks which directions around a point could be needed to be flipped(is other colour). This flowchart is structured differently where I used a decision square to showcases a for loop for each possible direction. It works similar to check_length where it will continue along the direction given until it proves direction is valid or invalid. It differs by storing all squares in direction travelled such that if direction proved to be valid it will then loop through the list and set the colour of squares to players colour . If not it will clear list and repeat for next direction. After each direction is checked it will then return the board with all changes.
<img width="940" height="814" alt="image" src="https://github.com/user-attachments/assets/db51b20b-2823-47be-b1be-2fb23d10dbc9" />
<img width="940" height="798" alt="image" src="https://github.com/user-attachments/assets/c5820736-c149-46b9-a6d9-b33db510b809" />

This is the code for flip_peices ive added this to be able to compare with Count_flip. Line 113 shows where poi_coordinate is used to gather all potential directions used in for loop.

### Count_flip

There is no flowchart for this as this does the same as Flip_peices however it does not change the board it will instead count the amount of pieces that will be flipped if a coordinate is used. This is used by the AI in stage 3 to help it choose the move that will flip the most pieces.
<img width="940" height="811" alt="image" src="https://github.com/user-attachments/assets/88bda170-e835-4ef6-946a-60b47b8b2905" />

This differences between this code can be seen by the introduction of variable sum which is used to record the total amount of tiles flipped by the specific move. The reason for making this function separate to flip_peices is due to needing different returns as for flip_peices the amount of tiles flipped was not needed whereas it is for count_flip.

### Poi_coordinate

It stands for point of interest coordinates which are the important directions around a point. This takes in a coordinate, the opposite colour of player and the board and it will then return all directions around the coordinate that are the opposite colour. Which is required for previously described functions to work.
<img width="677" height="751" alt="image" src="https://github.com/user-attachments/assets/dd0e3f29-b7ee-466a-aab2-aeb8e50dc062" />

### 

Since making the graph some error handling was required so I added additional checks to ensure that before a position is checked it is ensured that it is on the board and will not cause an error. This is shown in the code below.
<img width="940" height="455" alt="image" src="https://github.com/user-attachments/assets/4a74ca8b-c424-4ae4-a1fd-a5f8b9faaf9b" />

### Logging

This function takes in a string and adds to logging file if file exists else it will create the file and then add it. Logging creates a text file that will store the games history and movement it will document which player moves if they try to enter a move that is not valid and if they save, load or reset the game and if they toggle the AI on or off. On line 235 a time stamp is added to the string to record when the inputs were made
<img width="940" height="301" alt="image" src="https://github.com/user-attachments/assets/a3d6d9bc-fd64-4f1d-b055-4a426178d96c" />

Example of the file 
<img width="828" height="569" alt="image" src="https://github.com/user-attachments/assets/ddc0ee92-bef8-4592-9ae3-4a334525c530" />

### Has_legal_move

This function takes in the board and players colour then will search through every square until it finds a valid move for player otherwise it will return false causing player to lose their turn
<img width="451" height="568" alt="image" src="https://github.com/user-attachments/assets/af7a8a59-87ba-4f59-bbc7-b1491410015a" />

In flowchart 7 it shows 2 for loops to loop through every row and every column of row to check each square for a valid move. As the board is relatively small this is able to be executed quickly thus not requiring a more efficient method to be used.
<img width="940" height="254" alt="image" src="https://github.com/user-attachments/assets/2f83a367-381a-4558-969c-63a87c5d4828" />

This is the python for this function which showcases the implementation of the flowchart.

## Game_engine.py

### Cli_coords_input

This function is used to take in user inputs and validate they have been entered correctly
<img width="531" height="556" alt="image" src="https://github.com/user-attachments/assets/4e1b2ac9-46f1-4d42-b6ac-5ec66b6a2137" />

This shows the error checking to ensure only valid inputs are attained. This function also has no parameters and it will return the coordinates as a tuple.
<img width="940" height="263" alt="image" src="https://github.com/user-attachments/assets/b305e05b-4594-4bdf-bb03-2bc53346aa9f" />

The code ensures it loops until valid coordinates are inputted (in terms of structure not if move is legal)

### Simple_game_loop()

This function is used to create a python based version of the game it initiialises the board and sets first player to dark it will then loop through game loop allowing users to make moves and checks before to see if they have a valid move
<img width="681" height="888" alt="image" src="https://github.com/user-attachments/assets/b8da12ea-a3aa-44e4-bc4e-b7ceed8f0af6" />

This shows the flowchart of how it will continuously loop through game until neither colour can make a move or move counter is equal to 0.
<img width="940" height="808" alt="image" src="https://github.com/user-attachments/assets/c9aa689d-b205-4dd4-852e-cbde7daaa94d" />

## Flask_game_engine
<img width="570" height="234" alt="image" src="https://github.com/user-attachments/assets/05523f7d-8ce7-4942-aade-29affa6aff15" />

Import and declare all global variables and all functions
<img width="770" height="188" alt="image" src="https://github.com/user-attachments/assets/c051d4ac-a326-4a9b-84e6-525c5a75a037" />

Defaults the game to be displayed and sets player colour

### Move

This function is where bulk of game decisions is made. It works by taking in users input as x and y checking they are legal moves using legal_move function then it makes move if legal it then flips the players colours. I also have AI run as the player makes their input so it checks if both AI is on and the AI has a legal move if it does it uses ai_move_select function to find coordinates of best move and make move then switches colour back for player. It will also check if both colours are able to move in line 67 if they do it will use function winner to workout who won the game. If the player doesn’t make a valid move it will add to log and output message saying invalid move.
<img width="803" height="803" alt="image" src="https://github.com/user-attachments/assets/845edb70-d8b8-40ee-b0be-5805f5807d4c" />

### AI_toggle

This is used to accompany the switch in game which will switch the global variable AI from true to false. It works by calling the ai_toggle function which causes the mode to change without passing any data
<img width="513" height="309" alt="image" src="https://github.com/user-attachments/assets/f89cd16c-223a-4b20-8903-760f9ed08348" />

Above is the python script showing the ai being flipped it also shows it logging it being turned on and off
<img width="528" height="153" alt="image" src="https://github.com/user-attachments/assets/50bbce84-7a06-4725-85d4-376c0eb76b1f" />

Above shows the script from html which just calls the python script causing the toggle
<img width="611" height="137" alt="image" src="https://github.com/user-attachments/assets/0726d539-61b6-45d1-9374-e9c98006d3cf" />
<img width="246" height="133" alt="image" src="https://github.com/user-attachments/assets/d0140b03-2046-41e5-a373-6486f2951c0c" />

This is code for the switch shown on the left.

So every time the switch is toggled the script will run.

### Save and Load

These both work by converting a dictionary to and from a json file named Information. The purpose of this is so that once a save is made even if code is terminated the game can be loaded and resumed. TO do this I decided that it was necessary to save the board, move count and whose turn it was. 
<img width="940" height="403" alt="image" src="https://github.com/user-attachments/assets/00f7b640-a097-4d7c-a0cd-10633b77fcbd" />

When making the code I added logging such that log will show when game was loaded or saved.

### New
<img width="940" height="263" alt="image" src="https://github.com/user-attachments/assets/07f92fff-8656-43fa-8c24-2daef3caeb30" />

The purpose of this function is for when the player wants to play another game they have to be able to reset board to do this I have added a reset button to set all global variables back to start and reset the game.

### Ai_move_select

This is the function used in Move where the ai calculates the best move to make that maximises the amount of tiles it flips. It does this by searching whole board then identifying empty squares and from their it uses count_flip from components then it will compare the amount of tiles flipped with the current highest amount of tiles to be flipped if the new score is higher it will replace the old score and the coordinates of move will be recorded. This repeats for each square in board then should be left with the highest scoring move which it then does using flip_peices. Although this AI does find the best move it is incapable of making the most calculated move or best move for long run. This is due to my time constraints however to further improve the AI would be better to prioritize corner squares as is a good strategy to help win.

### Winner

This function checks every square of the board and will count how many of each colour there are it will then return a string to be outputted to say who won.

## GUI

This is the display of the game.

To play the user selects a square starting with dark first the board will then update and a message will pop up in game log saying it is lights turn. If the user wants to turn AI on they can use the switch which will turn on the AI to move for the other player and so forth until it is turned off. Save will make a save of current board and will display a message to show has worked. Then if user wants to use the save they can click load which will bring up the saved data. Reset can be used to return the board to this state.
<img width="722" height="643" alt="image" src="https://github.com/user-attachments/assets/320448ba-a6f6-4a2e-b0f9-be108c81c3ba" />

Once the game has finished this message will pop up to signify which team has won. To then play a new game reset button has to be pressed.
