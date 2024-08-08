"""
Tic Tac Toe Player
"""
from copy import deepcopy
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
        return X
    if count[X] == count[O]:
        return X
    else:
        return O

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
    board_copy = deepcopy(board)
    current_player = player(board_copy)
    if board_copy[action[0]][action[1]] != EMPTY:
        raise ValueError("In valid move!")
    else:
        board_copy[action[0]][action[1]] = current_player
        return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = np.array(board)
    diagonal_board_1 = board.diagonal()
    diagonal_board_2 = np.fliplr(board).diagonal()
    
    if all (i == diagonal_board_1[0] for i in diagonal_board_1):
        if diagonal_board_1[0] != EMPTY:
            return diagonal_board_1[0]
    if all (i == diagonal_board_2[0] for i in diagonal_board_2):
        if diagonal_board_2[0] != EMPTY:
            return diagonal_board_2[0]
    else:
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] != EMPTY:
                    return board[i][0]
                
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] != EMPTY:
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
    if terminal(board):
        return None
    if player(board) == X:
        score = -math.inf
        action_to_take = None
        for action in actions(board):
            min_val = minvalue(result(board, action))
            if min_val > score:
                score = min_val
                action_to_take = action
        return action_to_take
    elif player(board) == O:
        score = math.inf
        action_to_take = None
        for action in actions(board):
            max_val = maxvalue(result(board, action))
            if max_val < score:
                score = max_val
                action_to_take = action
        return action_to_take
    
def minvalue(board):
    # if game over, return the utility of state
    if terminal(board):
        return utility(board)
    # iterate over the available actions and return the minimum out of all maximums
    max_value = math.inf  
    for action in actions(board):
        max_value = min(max_value, maxvalue(result(board, action)))
    return max_value

def maxvalue(board):
    # if game over, return the utility of state
    if terminal(board):
        return utility(board)
    # iterate over the available actions and return the maximum out of all minimums
    min_val = -math.inf
    for action in actions(board):
        min_val = max(min_val, minvalue(result(board, action)))
    return min_val

def counter(board):
    """
    Helper function.
    Returns the count of both X and O and determine the player to play.
    """
    count = {X: 0, O: 0}
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == X:
                count[X] += 1
            elif board[i][j] == O:
                count[O] += 1
    return count