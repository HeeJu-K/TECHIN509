# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    player_id = input("Type in your nickname: \n")

    mode = input("Please type in 1 for single player and 2 for two players: \n")
    if mode == 1:
        game = Game(Human('X'), Bot('O'))
        winner = game.run()
    else:
        game = Game(Human('X'), Human('O'))
        winner = game.run()
    board = Board()
    board.writeRank(player_id, winner)
    # board.writeRank(player_id, "X")
    board.showRank()

