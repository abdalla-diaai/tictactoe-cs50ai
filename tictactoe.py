"""
Tic Tac Toe Player
"""

import math

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
    if terminal(board):
        return None
    elif board == initial_state():
        return "X"
    
    raise NotImplementedError


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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
