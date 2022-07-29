import unittest
from connect4 import ConnectFour

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.connect4 = ConnectFour()
        self.board = self.connect4.init_board(6,7)
        
    def test_column_is_available_returns_False_if_column_is_full(self):
        # Täytetään neljäs sarake
        self.board[:, 3] = 1

        self.assertFalse(self.connect4.column_is_available(self.board, 4))