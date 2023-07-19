def diagonal_winner(board):
    bool = False
    for n in range(len(board[0])-1):
        if((board[n][n] == board[n+1][n+1]) and board[n][n] != ' '):
            bool = True
        else:
            bool = False
            break
    
    if(bool == True):
        return bool
    
    for n in range(len(board[0])-1):    
        if((board[len(board)-n-1][n] == board[len(board)-n-2][n+1]) and board[len(board)-n-1][n] != ' '):
            bool = True
        else:
            bool = False
            break

    return bool

def row_winner(board):
    bool = False
    r = 0
    for r in range(len(board[0])):
        for n in range(len(board[0])-1):
            if(board[r][n] == board[r][n+1] and board[r][n] != ' '):
                bool = True
            else:
                bool = False
                break
            if(bool == True and n+1 == len(board[0])-1):
                return bool

    return bool
    
def column_winner(board):
    bool = False
    r = 0
    for r in range(len(board[0])):
        for n in range(len(board[0])-1):
            if(board[n][r] == board[n+1][r] and board[n][r] != ' '):
                bool = True
            else:
                bool = False
                break
            if(bool == True and n+1 == len(board[0])-1):
                return bool

    return bool

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
   joined_rows = []
   count = 0
   pm = '-'
   for n in range(len(board)-1):
       pm = pm + '+-'

   for row in board:
       count += 1
       joined_rows.append("|".join(row))
       if(count != len(board)):
           joined_rows.append(pm)
   return("\n".join(joined_rows))

def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    count = 0
    x = board_size * board_size
    for i in range(x):
        if(count < x):
            play_move(board, player1)
            count += 1
            if(winner(board)):
                print_winner(player1)
                break
        if(count < x):
            play_move(board, player2)
            count += 1
            if(winner(board)):
                print_winner(player2)
                break
        else:
            print_draw()
            break
