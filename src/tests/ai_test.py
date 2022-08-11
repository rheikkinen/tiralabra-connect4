import unittest

from gameboard import GameBoard
from ai import AI

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.ai = AI()

    def test_ai_chooses_winning_move_horizontally(self):
        # Alustetaan pelilauta
        for col in range(3):
            self.board.update_position(row=0, column=col, value=2)
            self.board.update_position(row=1, column=col, value=1)

        for col in range(5, 7):
            self.board.update_position(row=1, column=col, value=2)
            self.board.update_position(row=0, column=col, value=1)

            # PELILAUDAN TILANNE
            # 2 = tekoälyn kiekko
            # 0 = tyhjä ruutu

            #  0 1 2 3 4 5 6  <-- sarakeindeksit
            #  0 0 0 0 0 0 0  # 5
            #  0 0 0 0 0 0 0  # 4
            #  0 0 0 0 0 0 0  # 3
            #  0 0 0 0 0 0 0  # 2
            #  1 1 1 0 0 2 2  # 1
            #  2 2 2 0 0 1 1  # 0 rivi-indeksit

        # Tekoälyn tulisi valita sarakeindeksi 3 (voitto)
        best_column, _ = self.ai.best_column(self.board)
        self.assertEqual(best_column, 3, "Sarakkeen pitäisi olla 3!")

    def test_ai_chooses_winning_move_in_positive_diagonal(self):
        # Alustetaan pelilauta
        self.board.update_position(row=0, column=0, value=2)
        self.board.update_position(row=0, column=1, value=1)
        self.board.update_position(row=0, column=2, value=2)
        self.board.update_position(row=0, column=3, value=2)
        self.board.update_position(row=0, column=4, value=1)
        self.board.update_position(row=1, column=0, value=1)
        self.board.update_position(row=1, column=1, value=2)
        self.board.update_position(row=1, column=2, value=1)
        self.board.update_position(row=1, column=3, value=1)
        self.board.update_position(row=2, column=3, value=1)
        self.board.update_position(row=3, column=3, value=2)

            # PELILAUDAN TILANNE
            # 2 = tekoälyn kiekko
            # 0 = tyhjä ruutu

            #  0 1 2 3 4 5 6  <-- sarakeindeksit
            #  0 0 0 0 0 0 0  # 5
            #  0 0 0 0 0 0 0  # 4
            #  0 0 0 2 0 0 0  # 3
            #  0 0 0 1 0 0 0  # 2
            #  1 2 1 1 0 0 0  # 1
            #  2 1 2 2 1 0 0  # 0 rivi-indeksit

        # Tekoälyn tulisi valita sarakeindeksi 2 (voitto)
        best_column, _ = self.ai.best_column(self.board)
        self.assertEqual(best_column, 2, "Sarakkeen pitäisi olla 2!")

    def test_ai_chooses_winning_move_in_negative_diagonal(self):
        pass

    def test_ai_chooses_winning_move_vertically(self):
        pass

    def test_ai_evaluates_draw_state_correctly(self):
        pass