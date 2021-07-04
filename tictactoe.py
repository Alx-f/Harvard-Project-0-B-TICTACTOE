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

    count = {"O": 0, "X": 0, "None": 0}

    for vert in board:
        for horz in vert:
            count[str(horz)] += 1

    if count[O] >= count[X]:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = [[],[],[]]

    for i in range(3):
        for j in range(3):
            # This means that the current segment needs to change!
            if i == action[0] and j == action[1]:
                board_copy[i].append(player(board))
            else:
                board_copy[i].append(board[i][j])

    return board_copy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks horz
    for i in range(3):
        if board[i].count(X) == 3:
            return X
        if board[i].count(O) == 3:
            return O
    
    # Checks vert
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O
    
    # Check diags
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for vert in board:
        for horz in vert:
            if horz == EMPTY:
                return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_score = winner(board)

    if win_score == X:
        return 1
    elif win_score == O:
        return -1
    else:
        return 0


def minimax(board):    
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # Player X is playing if this is true
    if player(board) == X:
        v = -math.inf
        best_move = None

        for action in actions(board):
            min_value = recursive_minimax(result(board, action), False)

            if min_value > v:
                v = min_value
                best_move = action 

    elif player(board) == O:
        v = math.inf
        best_move = None

        for action in actions(board):
            max_value = recursive_minimax(result(board, action), True)

            if max_value < v:
                v = max_value
                best_move = action

    return best_move


def recursive_minimax(board_copy, max_check):

    # search is over test
    if terminal(board_copy):
        return utility(board_copy)


    if max_check:
        v = -math.inf
        
        for action in actions(board_copy):            
            v = max(v, recursive_minimax(result(board_copy, action), False))
    
    else:
        v = math.inf

        for action in actions(board_copy):
            v = min(v, recursive_minimax(result(board_copy, action), True))

    return v
