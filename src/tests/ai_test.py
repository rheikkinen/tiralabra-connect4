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

        # Tekoälyn pitäisi valita sarakeindeksi 3 (voitto)
        best_column = self.ai.best_column(self.board)[0]
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

        # Tekoälyn pitäisi valita sarakeindeksi 2 (voitto)
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 2, "Sarakkeen pitäisi olla 2!")

    def test_ai_chooses_winning_move_in_negative_diagonal(self):
        # Alustetaan pelilauta
        self.board.update_position(row=0, column=0, value=2)
        self.board.update_position(row=0, column=1, value=1)
        self.board.update_position(row=0, column=2, value=1)
        self.board.update_position(row=0, column=3, value=2)
        self.board.update_position(row=1, column=0, value=1)
        self.board.update_position(row=1, column=1, value=1)
        self.board.update_position(row=1, column=2, value=2)
        self.board.update_position(row=1, column=3, value=1)
        self.board.update_position(row=2, column=0, value=1)
        self.board.update_position(row=2, column=1, value=2)

        # PELILAUDAN TILANNE
        # 2 = tekoälyn kiekko
        # 0 = tyhjä ruutu

        #  0 1 2 3 4 5 6  <-- sarakeindeksit
        #  0 0 0 0 0 0 0  # 5
        #  0 0 0 0 0 0 0  # 4
        #  0 0 0 0 0 0 0  # 3
        #  1 2 0 0 0 0 0  # 2
        #  1 1 2 1 0 0 0  # 1
        #  2 1 1 2 0 0 0  # 0 rivi-indeksit
        
        # Tekoälyn pitäisi valita sarakeindeksi 0 (voitto)
        best_column = self.ai.best_column(self.board, depth=4)[0]
        self.assertEqual(best_column, 0)

    def test_ai_chooses_winning_move_vertically(self):
        # Alustetaan pelilauta
        self.board.update_position(row=0, column=0, value=1)
        self.board.update_position(row=0, column=1, value=2)
        self.board.update_position(row=0, column=2, value=1)
        self.board.update_position(row=0, column=3, value=1)
        self.board.update_position(row=1, column=0, value=1)
        self.board.update_position(row=1, column=1, value=2)
        self.board.update_position(row=1, column=2, value=2)
        self.board.update_position(row=1, column=3, value=1)
        self.board.update_position(row=2, column=1, value=2)

        # PELILAUDAN TILANNE
        # 2 = tekoälyn kiekko
        # 0 = tyhjä ruutu

        #  0 1 2 3 4 5 6  <-- sarakeindeksit
        #  0 0 0 0 0 0 0  # 5
        #  0 0 0 0 0 0 0  # 4
        #  0 0 0 0 0 0 0  # 3
        #  0 2 0 0 0 0 0  # 2
        #  1 2 2 1 0 0 0  # 1
        #  1 2 1 1 0 0 0  # 0 rivi-indeksit
        
        # Tekoälyn pitäisi valita sarakeindeksi 1 (voitto)
        best_column = self.ai.best_column(self.board, depth=4)[0]
        self.assertEqual(best_column, 1)

    def test_ai_evaluates_draw_game_state_correctly(self):
        # Alustetaan pelilauta
        for i in range(0, 6):
            if i % 2 == 0:
                a, b = 2, 1
            else:
                a, b = 1, 2
            self.board.update_position(row=0, column=i, value=a)
            self.board.update_position(row=1, column=i, value=a)
            self.board.update_position(row=2, column=i, value=a)
            self.board.update_position(row=3, column=i, value=b)
            self.board.update_position(row=4, column=i, value=b)
            self.board.update_position(row=5, column=i, value=b)
        self.board.update_position(row=0, column=6, value=2)
        self.board.update_position(row=1, column=6, value=2)
        self.board.update_position(row=2, column=6, value=2)
        self.board.update_position(row=3, column=6, value=1)
        self.board.update_position(row=4, column=6, value=1)

        # PELILAUDAN TILANNE
        # 2 = tekoälyn kiekko
        # 0 = tyhjä ruutu

        #  0 1 2 3 4 5 6  <-- sarakeindeksit

        #  1 2 1 2 1 2 0  # 5
        #  1 2 1 2 1 2 1  # 4
        #  1 2 1 2 1 2 1  # 3
        #  2 1 2 1 2 1 2  # 2
        #  2 1 2 1 2 1 2  # 1
        #  2 1 2 1 2 1 2  # 0 rivi-indeksit

        # Tekoälyn pitäisi valita sarake-indeksi 6 (viimeinen vapaa ruutu) pisteytyksellä 0 (tasapeli)
        column, value, _ = self.ai.best_column(self.board)

        self.assertEqual(column, 6)
        self.assertEqual(value, 0)
