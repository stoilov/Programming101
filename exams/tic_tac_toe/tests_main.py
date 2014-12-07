import unittest
from main import Board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_get_empty_spots(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        expected_empty = [[0, 0], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(self.board.get_empty_spots(grid), expected_empty)

    def test_get_new_state_player_turn(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        move = [2, 2]
        new_grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", "O"]]
        self.assertListEqual(self.board.get_new_state(grid, move), new_grid)

    def test_get_new_state_ai_turn(self):
        grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", " "]]
        move = [2, 2]
        new_grid = [[" ", "X", "O"], ["X", "O", "O"], [" ", " ", "X"]]
        self.board.player_turn, self.board.ai_turn = self.board.ai_turn, self.board.player_turn
        self.assertListEqual(self.board.get_new_state(grid, move), new_grid)

    def test_game_win_at_row(self):
        grid = [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]]
        self.assertTrue(self.board.game_win(grid, Board.PLAYER))

    def test_game_win_at_col(self):
        grid = [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]]
        self.assertTrue(self.board.game_win(grid, Board.PLAYER))

    def test_game_win_at_main_diagonal(self):
        grid = [["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]]
        self.assertTrue(self.board.game_win(grid, Board.PLAYER))

    def test_game_win_at_other_diagonal(self):
        grid = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]
        self.assertTrue(self.board.game_win(grid, Board.PLAYER))

    def test_have_winner_winner_no_winner(self):
        grid = [[" ", " ", " "], ["X", "O", "O"], [" ", " ", " "]]
        self.assertFalse(self.board.game_win(grid, Board.PLAYER))

    def test_score_player_wins(self):
        grid = [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]]
        self.assertEqual(self.board.score(grid, 3), 7)

    def test_score_ai_wins(self):
        grid = [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]
        self.assertEqual(self.board.score(grid, 3), -7)

    def test_score_nobody_wins(self):
        grid = [[" ", " ", " "], ["X", "O", "O"], [" ", " ", " "]]
        self.assertEqual(self.board.score(grid, 3), 0)

    def test_is_game_over_is_over(self):
        self.board.grid = [["O", "X", "O"], ["X", "O", "O"], ["X", "X", "O"]]
        self.assertTrue(self.board.is_game_over())

    def test_is_game_over_not_over(self):
        self.assertFalse(self.board.is_game_over())

    def test_minimax(self):
        pass

if __name__ == '__main__':
    unittest.main()
