import unittest
from connect4 import ConnectFour

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.connect4 = ConnectFour()
        self.board = self.connect4.init_board(6,7)
        
    def test_column_is_available_returns_false_if_column_is_full(self):
        # Täytetään neljäs sarake
        self.board[:, 3] = 1

        self.assertFalse(self.connect4.column_is_available(self.board, 3))

    def test_horizontal_four_discs_in_a_row_is_a_winning_move(self):
        for col in range(2,6):
            self.connect4.drop_disc(self.board, 0, col, player=2)
        self.assertTrue(self.connect4.player_won(self.board, 0, 6, player=2))

    def test_vertical_four_discs_in_a_row_is_a_winning_move(self):
        pass

    def test_diagonal_four_discs_in_a_row_is_a_winning_move(self):
        pass