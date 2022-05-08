# imports
from guizero import App, Waffle, Text
import random

# vars @ cons
board_W = 10
board_H = 10
players = ["yellow", "black", "green","blue", "red"]

player1 = random.choice(players)
print("player1 = ", player1)
out = players.index(player1)
players.pop(out)
player2 = random.choice(players)
print("player2 = ", player2)
active_players = [player1, player2]
player = random.choice(active_players)
player1_dots = 0
player2_dots = 0

# functions @ classes
def end_of_game():
    print("validare end of game")
    message_game_status.value = " - end of game - "
    if player1_dots > player2_dots:
        message_test.value = player1 + " wins !"
        message_player.value = ""
    elif player2_dots > player1_dots:
        message_test.value = player2 + " wins !"
        message_player.value = ""
    elif player2_dots == player1_dots:
        message_test.value =  "equal game !"
        message_player.value = ""
       
def flip_player():
    global player
    if player == player1: 
        player = player2
    elif player == player2:
        player = player1

def count():
    global player1_dots, player2_dots
    player1_dots = 0
    player2_dots = 0
    for x in range(board_W):
        for y in range(board_H):
            if board.get_pixel(x, y ) == player1:
                player1_dots += 1
            elif board.get_pixel(x, y) == player2:
                player2_dots += 1
    message_count_yellow.value = player1 + " :" + str(player1_dots)
    message_count_black.value = player2 + " :" + str(player2_dots)

def check_around_and_flip(x ,y):
    # check possitioning on the board
    if (y == 0 or y == 1) and 0 < x < board_W-1:
        print(x+1,y+1,': choice on the top borders')

        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)
        if board.get_pixel(x-1,y+1) != "white":
            if board.get_pixel(x-2,y+2) == player:
                board.set_pixel(x-1,y+1, player)
        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)
        if board.get_pixel(x+1,y+1) != "white":
            if board.get_pixel(x+2,y+2) == player:
                board.set_pixel(x+1,y+1, player)
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)

    elif (x == 0 or x == 1) and 0 < y < board_H-1:
        print(x+1,y+1,': choice on the left borders')

        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)
        if board.get_pixel(x+1,y-1) != "white":
            if board.get_pixel(x+2,y-2) == player:
                board.set_pixel(x+1,y-1, player) 
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)
        if board.get_pixel(x+1,y+1) != "white":
            if board.get_pixel(x+2,y+2) == player:
                board.set_pixel(x+1,y+1, player)
        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)

    elif (x == board_W-1 or x == board_W-2) and 0 < y < board_H-1:
        print(x+1,y+1,': choice on the right borders')

        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)
        if board.get_pixel(x-1,y-1) != "white":
            if board.get_pixel(x-2,y-2) == player:
                board.set_pixel(x-1,y-1, player)                
        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)
        if board.get_pixel(x-1,y+1) != "white":
            if board.get_pixel(x-2,y+2) == player:
                board.set_pixel(x-1,y+1, player)
        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)

    elif (y == board_H-1 or y == board_H -2) and 0 < x < board_W-1:
        print(x+1,y+1,': choice on the bottom borders')

        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)
        if board.get_pixel(x-1,y-1) != "white":
            if board.get_pixel(x-2,y-2) == player:
                board.set_pixel(x-1,y-1, player)
        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)
        if board.get_pixel(x+1,y-1) != "white":
            if board.get_pixel(x+2,y-2) == player:
                board.set_pixel(x+1,y-1, player)
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)

    elif (x == 0 and y == 0) or (x == 1 and y == 1):
        print(x+1,y+1,': choice on the top left corners')

        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)
        if board.get_pixel(x+1,y+1) != "white":
            if board.get_pixel(x+2,y+2) == player:
                board.set_pixel(x+1,y+1, player)
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)

    elif (x == board_W-1 and y == 0) or (x == board_W-2 and y == 1):
        print(x+1,y+1,': choice on the top right corners')

        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)
        if board.get_pixel(x-1,y+1) != "white":
            if board.get_pixel(x-2,y+2) == player:
                board.set_pixel(x-1,y+1, player)
        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)         
        
    elif (y == board_H-1 and x == 0) or (y == board_H-2 and x == 1):
        print(x+1,y+1,': choice on the left bottom corners')

        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)
        if board.get_pixel(x+1,y-1) != "white":
            if board.get_pixel(x+2,y-2) == player:
                board.set_pixel(x+1,y-1, player) 
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)

    elif ( y == board_H -1 and x == board_W - 1 ) or (y == board_H -2 and x == board_W - 2):
        print(x+1,y+1, ": choice on the right bottom corners")

        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)
        if board.get_pixel(x-1,y-1) != "white":
            if board.get_pixel(x-2,y-2) == player:
                board.set_pixel(x-1,y-1, player)
        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)

    else:
        print(x+1,y+1,": choice inside the board")

        if board.get_pixel(x-1,y+1) != "white":
            if board.get_pixel(x-2,y+2) == player:
                board.set_pixel(x-1,y+1, player)
        if board.get_pixel(x,y+1) != "white":
            if board.get_pixel(x,y+2) == player:
                board.set_pixel(x,y+1, player)
        if board.get_pixel(x+1,y+1) != "white":
            if board.get_pixel(x+2,y+2) == player:
                board.set_pixel(x+1,y+1, player)
        if board.get_pixel(x+1,y) != "white":
            if board.get_pixel(x+2,y) == player:
                board.set_pixel(x+1,y, player)
        if board.get_pixel(x+1,y-1) != "white":
            if board.get_pixel(x+2,y-2) == player:
                board.set_pixel(x+1,y-1, player)       
        if board.get_pixel(x,y-1) != "white":
            if board.get_pixel(x,y-2) == player:
                board.set_pixel(x,y-1, player)
        if board.get_pixel(x-1,y-1) != "white":
            if board.get_pixel(x-2,y-2) == player:
                board.set_pixel(x-1,y-1, player)
        if board.get_pixel(x-1,y) != "white":
            if board.get_pixel(x-2,y) == player:
                board.set_pixel(x-1,y, player)

def validate_move(x, y):
    if board.get_pixel(x, y) == "white": 
        return True
    else:
        return False

def validate_board():
    status_board = 0
    for i in range(board_W):
        for j in range(board_H):
            if board.get_pixel(i, j)== "white":
                status_board += 1
    if status_board == 0 :
        end_of_game()

def play(x, y):
    if validate_move(x, y):
        message_test.value = player + " had a valide move"
        board.set_pixel(x,y ,player)
        check_around_and_flip(x, y)
        flip_player()
        message_player.value = player + " has to move"
        count()
        validate_board()
    else:
        message_test.value = player + " had an invalide move, choose another location"    

# apps
app = App("Grande Flippy")
board = Waffle(app, width = board_W, height = board_H , dotty = True, command=play)
for x  in range(board_W):
    for y in range(board_H):
        if (x == board_W/2-1 and y == board_H/2-1) or (x == board_W/2 and y == board_H/2):
            board.set_pixel(x, y , player2)
        elif (x == board_W/2-1 and y == board_H/2) or (x == board_W/2 and y == board_H/2-1):
            board.set_pixel(x, y , player1)
        else:
            board.set_pixel(x, y , "white")
message_game_status = Text(app)
message_game_status.value = " - game on - "
message_test = Text(app)
message_test.value = ""
message_player = Text(app)
message_player.value = player +" has to move 1st"
message_empty_line = Text(app)
message_empty_line.value = ""
message_count_yellow = Text(app)
message_count_yellow.value = player1 + " : 2" 
message_count_black = Text(app)
message_count_black.value = player2 + " : 2" 
app.display()