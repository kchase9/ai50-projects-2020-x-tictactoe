"""
Tic Tac Toe Player
"""
import math
import copy

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

    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):  # move = row(i), column(j)
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):  # do not alter original board
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    
    else:
        raise Exception("Location unavailable")





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xcount = 0
    ocount = 0
    for row in board:
        xcount = row.count(X)
        ocount = row.count(O)

        if xcount == 3:
            return X
        elif ocount == 3:
            return O

    #check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        if board[0][j] == board[1][j] == board[2][j] == O:
            return O

    #check diagonals
    #only two possible combos for a diagonal win
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X


    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    #No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    check = 0
    if winner(board) == X or winner(board) == O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                check += 1
    if check == 9:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    team = player(board)

    if terminal(board):
        return None

    if team == X:
        a = -math.inf
        best_move = None

        for action in actions(board):
            factor = min_value(result(board,action))

            if factor > a:
                a = factor
                best_move = action

        return best_move

    else:
        b = math.inf
        best_move = None

        for action in actions(board):
            maxmove = max_value(result(board, action))

            if maxmove < b:
                b = maxmove
                best_move = action

        return best_move

def max_value(board):
    n = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        n = max(n, min_value(result(board, action)))
    return n

def min_value(board):
    n = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        n = min(n, max_value(result(board, action)))

    return n