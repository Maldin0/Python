'''PSCP Program'''
def main(board):
    '''8423-TicTacToe 07/11/2022'''
    # Check horizontal
    for i in board:
        for j in ['X', 'O']:
            if i.count(j) == 3:
                return '%s WIN' % j
    # Check vertical
    for i in range(3):
        for j in ['X', 'O']:
            if board[0][i] == j and board[1][i] == j and board[2][i] == j:
                return '%s WIN' % j
    # Check diagonal
    for j in ['X', 'O']:
        if ((board[0][0] == j and board[2][2] == j) or (board[2][0] == j\
             and board[0][2] == j)) and board[1][1] == j:
            return '%s WIN' % j
    return 'DRAW'
print(main([list(input()) for _ in range(3)]))
