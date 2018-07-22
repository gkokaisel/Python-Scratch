board = [' ' for i in range(10)]
player = 1
running = 0
game = running
win = 1
draw = 2


def draw_board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


def check_winner():
        global game
        # Horizontal winning condition
        if len(set(board[1:4])) == 1 and ' ' not in board[1]:
            game = win
        elif len(set(board[4:7])) == 1 and ' ' not in board[4]:
            game = win
        elif len(set(board[7:10])) == 1 and ' ' not in board[7]:
            game = win
        # Vertical Winning Condition
        elif len(set(board[1:8:3])) == 1 and ' ' not in board[1]:
            game = win
        elif len(set(board[2:9:3])) == 1 and ' ' not in board[2]:
            game = win
        elif len(set(board[3:10:3])) == 1 and ' ' not in board[3]:
            game = win
        # Diagonal Winning Condition
        elif len(set(board[1:10:4])) == 1 and ' ' not in board[1]:
            game = win
        elif len(set(board[3:8:2])) == 1 and ' ' not in board[3]:
            game = win
        # Match Tie or Draw Condition
        elif ' ' not in board[1:10]:
            game = draw
        else:
            game = running


def play():
    global player
    global game
    draw_board()
    while game is running:

        if player % 2 != 0:
            print("Player 1's turn")
            mark = 'X'
        else:
            print("Player 2's turn")
            mark = 'O'

        choice = int(input("Where do you want to place your mark? [a number between 1 and 9]:"))
        board[choice] = mark
        draw_board()
        check_winner()
        player += 1
        if game is draw:
            print("game draw")
        elif game is win:
            player -= 1
            if player % 2 != 0:
                print("Player 1 won")
            else:
                print("Player 2 won")


play()


