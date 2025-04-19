board = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}

player1 = ''
player2 = ''

def reset_board() :
    for place, value in board.items():
        value = ''

def check_free_spaces() :
    free = 0
    for place, value in board.items():
        if value == '' :
            free+=1
    return free

def player1_move():
    while True:
        move = input("Player 1's turn. Enter your move (1-9):")
        if board[move] != '' :
            print("Invalid move!")
        else:
            board[move] = player1
            break

def player2_move():
    while True:
        move = input("Player 2's turn. Enter your move (1-9):")
        if board[move] != '' :
            print("Invalid move!")
        else:
            board[move] = player2
            break
def check_winner():
    for i in range(3):
        x = 1 + 3*i
        if board[str(x)] == board[str(x+1)] == board[str(x+2)] :
           return board[str(x)]
    for i in range(3):
        x = 1 + i
        if board[str(x)] == board[str(x+3)] == board[str(x+6)] :
           return board[str(x)] 
    if board['1'] == board['5'] == board['9'] :
       return board['1']
    if board['3'] == board['5'] == board['7'] :
       return board['3']
    return ''
def print_winner(winner):
    if winner == player1:
       print("PLAYER 1 WON!")
    elif winner == player2:
        print("PLAYER 2 WON!")
    else:
        print("IT'S A TIE!")

def print_board(board):
    print()
    print(f" {board[str(1)]} | {board[str(2)]} | {board[str(3)]} ")
    print("---+---+---")
    print(f" {board[str(4)]} | {board[str(5)]} | {board[str(6)]} ")
    print("---+---+---")
    print(f" {board[str(7)]} | {board[str(8)]} | {board[str(9)]} ")
    print()



if __name__ == "__main__":
   
    print("Welcome to Tic Tac Toe!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    while True:
        reset_board()
        while True:
            print_board(board)
            player1_move()
            winner = check_winner()
            if winner != '' or check_free_spaces() == 0:
                break
            print_board(board)
            player2_move()
            winner = check_winner()
            if winner != '' or check_free_spaces() == 0:
                break
        print_board(board)
        print_winner(winner)
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break
