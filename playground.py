

EMPTY = None
X = "X"
O = "O"

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


import numpy as np

board = [       [X, O, X],
               [X, O, X],
                [O, X, O]]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = np.array(board)
    diagonal_board_1 = board.diagonal()
    diagonal_board_2 = np.fliplr(board).diagonal()
    
    if all (i == diagonal_board_1[0] for i in diagonal_board_1):
        if diagonal_board_1[0] != EMPTY:
            print("diagonal 1")
            return diagonal_board_1[0]
    if all (i == diagonal_board_2[0] for i in diagonal_board_2):
        if diagonal_board_2[0] != EMPTY:
            print("diagonal 2")
            return diagonal_board_2[0]
    else:
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] != EMPTY:
                    return board[i][0]
                
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] != EMPTY:
                    print("column")
                    return board[0][i]
    return None



        
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    output = winner(board)
    if output == "X":
        return 1
    elif output == "O":
        return -1
    else:
        return 0
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or EMPTY not in np.array(board):
        print(winner(board))
        return True
    return False


print(terminal(board))