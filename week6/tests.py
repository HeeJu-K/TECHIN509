import unittest
import logic
#make_empty_board get_winner other_player


class TestLogic(unittest.TestCase):

    def test_Board(self):
        #testing board initialization and printing function __str__
        board = logic.Board()
        for i in range (0,3):
            for j in range(0,3):
                self.assertEqual(board.get(i, j), None)
        self.assertEqual(board.__str__(), "\n| | | |\n| | | |\n| | | |\n")

    def test_get_winner(self):
        board0 = logic.Board()
        board1 = logic.Board()
        board2 = logic.Board()

        board0._rows = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board1._rows = [
            ['X', "O", 'O'],
            ['X', 'X', "O"],
            [None, 'O', 'O'],
        ]
        board2._rows = [
            ['X', "X", 'O'],
            ["O", 'X', "X"],
            ["X", 'O', 'O'],
        ]
        self.assertEqual(board0.get_winner(), 'X')
        self.assertEqual(board1.get_winner(), 'O')
        self.assertEqual(board2.get_winner(), None)

    def test_Human(self):
        player_X = logic.Human('X')
        self.assertEqual(player_X.symbol, "X")
        player_O = logic.Human('O')
        self.assertEqual(player_O.symbol, "O")

    
if __name__ == '__main__':
    unittest.main()
