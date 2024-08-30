from tictactoe import *
EMPTY = None
X = "X"
O = "O"

board = [
    [X, O, O],
    [X, X, EMPTY],
    [O,X , EMPTY]
    ]

print(result(board, (3,3)))
