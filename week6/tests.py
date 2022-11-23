import unittest
import logic
#make_empty_board get_winner other_player


class TestLogic(unittest.TestCase):

    #testing test_get_winner function by inputting a board and checking if the result equals with the expected result
    def test_get_winner(self):
        board0 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board1 = [
            ['X', "O", 'O'],
            ['X', 'X', "O"],
            [None, 'O', 'O'],
        ]
        board2 = [
            ['X', "X", 'O'],
            ["O", 'X', "X"],
            ["X", 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board0), 'X')
        self.assertEqual(logic.get_winner(board1), 'O')
        self.assertEqual(logic.get_winner(board2), None)


    #testing test_other_player function by testing if function returns the other player when a player is given
    def test_other_player(self):
        playerO = "O"
        self.assertEqual(logic.other_player(playerO), "X")
        playerX = "X"
        self.assertEqual(logic.other_player(playerX), "O")

   #testing make empty board by checking if each element of the board made is None or not and the size of the board
    def test_make_empty_board(self):
        board = logic.make_empty_board()
        self.assertEqual(len(board), 3)
        for i in range (0,len(board)):
            for j in range(0,len(board[i])):
                self.assertEqual(len(board[i]), 3)
                self.assertEqual(board[i][j], None)





if __name__ == '__main__':
    unittest.main()
