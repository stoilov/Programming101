import unittest
from board import Board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_have_winner_winner_at_row(self):
        grid = [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]]
        self.assertTrue(self.board.have_winner("O", grid))

    def test_have_winner_winner_at_col(self):
        grid = [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]]
        self.assertTrue(self.board.have_winner("O", grid))

    def test_have_winner_winner_at_main_diagonal(self):
        grid = [["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]]
        self.assertTrue(self.board.have_winner("O", grid))

    def test_have_winner_winner_at_other_diagonal(self):
        grid = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]
        self.assertTrue(self.board.have_winner("O", grid))

    def test_have_winner_winner_no_winner(self):
        grid = [[" ", " ", " "], ["X", "O", "O"], [" ", " ", " "]]
        self.assertFalse(self.board.have_winner("O", grid))

    def test_get_empty_spots(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        expected_empty = [(0, 0), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(self.board.get_empty_spots(grid), expected_empty)

    def test_put_mark_player(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        new_grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", "O"]]
        self.assertEqual(self.board.put_mark_player((2, 2), grid), new_grid)

    def test_put_mark_ai(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        new_grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", "X"]]
        self.assertEqual(self.board.put_mark_ai((2, 2), grid), new_grid)

    def test_minimax(self):
        grid = [["O", "X", "X"], ["X", "O", " "], ["X", "O", "O"]]
        expected_grid1 = [["O", "X", "X"], ["X", " ", " "], ["X", "O", "O"]]
        expected_grid2 = [["O", "X", "X"], ["X", " ", "O"], ["X", "O", "O"]]
        expected_result = [{"grid": expected_grid1, "score": -10}, {"grid": expected_grid2, "score": 10}]
        self.assertListEqual(self.board.minimax("O", grid, 0), expected_result)

if __name__ == '__main__':
    unittest.main()
