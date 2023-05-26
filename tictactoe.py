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
    count = 0
    len_board = len(board)
    for i in range(len_board):
        for j in range(len_board):
         if board[i][j] != EMPTY :
                count += 1
        
    if  count == 0 :
        return X
  
    return X if count % 2 == 0 else O 

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Possible_moves = set()
    len_board = len(board)
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] == EMPTY: 
                Possible_moves.add((i,j))
    
    return Possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyboard = copy.deepcopy(board)
    if action not in actions(copyboard):
        raise Exception('result', 'error')
    
    state = player(copyboard)
    copyboard[action[0]][action[1]] = state
    return copyboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    len_board = len(board)
    for state in [X,O]:
         for i in range(len_board):
            if board[i][0] == board[i][1] == board[i][2] == state:
                    return state
            elif board[0][i] == board[1][i] == board[2][i] == state:
                    return state
            elif board[0][0] == board[1][1] == board[2][2] == state:
                    return state
            elif board[0][2] == board[1][1] == board[2][0] == state:
                    return state
        
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        # the game is still in progress.
        if len(actions(board)) > 0:
                return False
    
    # the game is over,
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if the game is over
    if terminal(board) :
        winner_player = winner(board)
        if winner_player == X:
            return 1
        if winner_player == O:
            return -1
        else:
            return 0
    
    raise Exception('utility', 'error')


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the game is over
    if terminal(board) :
        return None
    
    state = player(board)
    alpha = -math.inf
    beta = math.inf
    if state == X:
        return Max_Value(board, alpha, beta)[1]
    elif state == O:
        return Min_Value(board, alpha, beta)[1]
     
        
def Max_Value(board, alpha, beta):
    
    if terminal(board):
      return [utility(board), None]
  
    # the negative infinity
    v = -math.inf
    optimal_action = None
    possible_moves = actions(board)
    for action in possible_moves:
        min = Min_Value(result(board, action), alpha, beta)[0]
        if  min > v : 
           v = min
           optimal_action = action
           
        alpha= max(alpha, v)  
        if beta<=alpha :
            break

    return [v,optimal_action]

def Min_Value(board, alpha, beta):
    
    if terminal(board):
      return [utility(board), None]
  
    # the positive infinity
    v = math.inf
    optimal_action = None
    possible_moves = actions(board)
    for action in possible_moves:
        max = Max_Value(result(board, action), alpha, beta)[0]
        if  max < v :
            v = max
            optimal_action = action
            
        beta= min(beta, v)  
        if beta<=alpha :
            break    
            
    return  [v,optimal_action]
