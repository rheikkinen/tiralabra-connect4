import unittest

from gameboard import GameBoard
from ai import AI

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.ai = AI()

    def test_ai_chooses_winning_move_horizontally(self):
        for col in range(3):
            self.board.update_position(row=0, column=col, value=2)
            self.board.update_position(row=1, column=col, value=1)

        for col in range(4, 7):
            self.board.update_position(row=1, column=col, value=2)
            self.board.update_position(row=0, column=col, value=1)

        self.ai.store_last_move(row=1, column=2)

        best_column = self.ai.best_column(self.board)

            # 0 1 2 3 4 5 6 <-- sarakeindeksit
            # 0 0 0 0 0 0 0 # 5
            # 0 0 0 0 0 0 0 # 4
            # 0 0 0 0 0 0 0 # 3
            # 0 0 0 0 0 0 0 # 2 
            # 1 1 1 0 2 2 2 # 1 
            # 2 2 2 0 1 1 1 # 0 rivi-indeksit

        # Tekoälyn tulisi valita sarakeindeksi 3
        self.assertEqual(best_column, 3, "Sarakkeen pitäisi olla 3!")

