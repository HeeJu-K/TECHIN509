# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner (board): 
    check_diag_0 = str(board[0][0]) + str(board[1][1]) + str(board[2][2])
    check_diag_1 = str(board[0][2]) + str(board[1][1]) + str(board[2][0])
    for i in range (0, 3): 
        check_hor = str(board[i][0]) + str(board[i][1]) + str(board[i][2])
        check_ver = str(board[0][i]) + str(board[1][i]) + str(board[2][i]) 
        if check_hor == 'OOO' or check_ver == 'OOO': 
            return "O"
        if check_hor == 'XXX' or check_ver == 'XXX':
            return "X"
    if check_diag_0 == 'OOO' or check_diag_1 == 'OOO':
        return "O"
    if check_diag_0 == 'XXX' or check_diag_1 == 'XXX':
        return "X"
    #when no winners
    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        return "O" 
    if player == "O":
        return "X"