# Program to implement Tic-Tac-TOe game using python.
board = [' ' for _ in range(9)]


def print_board():
    print("-----------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("-----------")


def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i*1] == board[i+2] == player:
            return True

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False


def play_game():
    player1 = '0'
    player2 = '1'
    current_player = player1
    while True:
        print_board()
        move = input("Player "+ current_player +", enter your move(1-9):")
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move)-1] != ' ':
            print(" Invalid move ! Try again.")
            continue
        board[int(move)-1] = current_player
        if check_win(current_player):
            print_board()
            print(" Player ", current_player, " wins! ")
            break
        if ' ' not in board:
            print_board()
            print(" It's a draw!")
            break
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
play_game()
