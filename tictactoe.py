"""
Tic Tac Toe Player
"""
import math
import numpy as np

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = counter(board)
    if terminal(board):
        return None
    elif board == initial_state():
        return "X"
    if count[X] == count[O]:
        print(X)
    else:
        print(O)

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or EMPTY not in np.array(board):
        return True
    return False


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


def counter(board):
    """
    Returns a dictionary with the count of both X and O.
    """
    count = {X: 0, O: 0}
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == X:
                count[X] += 1
            elif board[i][j] == O:
                count[O] += 1
    return count