# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    mode = input("Please type in 1 for single player and 2 for two players:\n")
    if mode == 1:
        game = Game(Human('X'), Bot('O'))
        winner = game.run()
    else:
        game = Game(Human('X'), Human('O'))
        winner = game.run()


    # board = make_empty_board()
    # #makes a board of 3*3 None
    # winner = None
    # #initialize first player 
    # player = "O"
    # count = 0
    # while winner == None:
    #     print("Turn: "+player)
    #     x = input("enter x coordinate :" )
    #     y = input("enter y coordinate :" )
    #     if x<0 or x>2 or y<0 or y>2:
    #         print("coordinate is out of range")
    #     else:
    #         #when the coordinate entered is None, replace it with O or X
    #         if board[x][y] == None:
    #             # board[x] = str(board[x][:y])+player+str(board[x][y+1:])
    #             board[x][y]=(player)
    #             player = other_player(player) #update player only when 
    #         winner = get_winner(board)
    #         count += 1
    #     print("updated board", board)
    #     if count == 9 and winner == None:
    #         winner = "full"
    # if winner == "full":
    #     print("There is no winner")
    # else:
    #     print(winner+ " is the winner")
   