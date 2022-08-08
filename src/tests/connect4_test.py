import unittest
from gameboard import GameBoard

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        
    def test_column_is_available_returns_false_if_column_is_full(self):
        # Täytetään neljäs sarake
        for row in range(6):
            self.board.update_position(row, column=3, value=1)

        self.assertFalse(self.board.column_is_available(column=3))

    def test_horizontal_four_discs_in_a_row_is_a_winning_move(self):
        for col in range(2,6):
            self.board.update_position(row=0, column=col, value=2)
        self.assertTrue(self.board.check_for_win(row=0, column=6, player=2))

    def test_vertical_four_discs_in_a_row_is_a_winning_move(self):
        pass

    def test_diagonal_four_discs_in_a_row_is_a_winning_move(self):
        pass