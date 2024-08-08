

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

board = [       [O, X, X],
            [EMPTY, EMPTY, X],
            [O, O, O]]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = np.array(board)
    diagonal_board_1 = board.diagonal()
    diagonal_board_2 = np.fliplr(board).diagonal()

    if all (i == diagonal_board_1[0] for i in diagonal_board_1):
        print("diagonal 1")
        return diagonal_board_1[0]
    if all (i == diagonal_board_2[0] for i in diagonal_board_2):
        print("diagonal 2")

        return diagonal_board_2[0]
    else:
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2]:
                print("row")

                return board[i][0]
                
            if board[0][i] == board[1][i] == board[2][i]:
                print("column")
                return board[0][i]
    return None


print(winner(board))
        
