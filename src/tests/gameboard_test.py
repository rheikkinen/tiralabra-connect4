import unittest
import numpy as np
from constants import COL_COUNT, EMPTY, ROW_COUNT
from gameboard import GameBoard

class TestGameBoard(unittest.TestCase):
    """Yksikkötestit GameBoard-luokan metodeille."""
    def setUp(self):
        """Alustusmetodi, jossa luodaan testejä varten tyhjä peliruudukko
        GameBoard-oliona. Suoritetaan ennen jokaista testitapausta."""
        self.board = GameBoard()
        
    def test_column_is_available_returns_correct_boolean_values(self):
        """Tarkastaa, että metodi colum_is_available palauttaa False,
        jos sarake on täynnä, ja muuten True."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,1,0,0,0], # 5
                                   [0,0,0,2,1,0,0], # 4
                                   [0,0,0,2,2,0,0], # 3
                                   [0,0,0,1,2,0,0], # 2
                                   [0,0,0,1,1,0,0], # 1
                                   [0,0,0,2,1,0,0]])# 0

        self.board.set_game_situation(test_situation)

        # Täysi sarake, pitäisi palauttaa False
        self.assertFalse(self.board.column_is_available(column=3))
        # Tyhjä sarake, pitäisi palauttaa True
        self.assertTrue(self.board.column_is_available(column=5))
        # Melkein täysi sarake, pitäisi palauttaa True
        self.assertTrue(self.board.column_is_available(column=4))

    def test_check_for_win_identifies_horizontal_winning_move(self):
        """Tarkastaa, että metodi check_for_win tunnistaa vaakasuuntaisen voittavan siirron."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0], # 5
                                   [0,0,0,2,0,2,2], # 4
                                   [0,0,0,2,1,1,1], # 3
                                   [0,0,0,1,2,2,1], # 2
                                   [0,0,0,1,1,1,2], # 1
                                   [1,2,1,2,1,2,2]])# 0

        self.board.set_game_situation(test_situation)
        self.assertTrue(self.board.check_for_win(row=4, column=4, player=2))
        self.assertTrue(self.board.check_for_win(row=1, column=2, player=1))

    def test_check_fow_win_identifies_vertical_winning_move(self):
        """Tarkastaa, että metodi check_for_win tunnistaa pystysuuntaisen voittavan siirron."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0], # 5
                                   [0,0,0,0,0,0,1], # 4
                                   [0,2,0,0,0,0,1], # 3
                                   [0,2,0,0,1,0,1], # 2
                                   [2,2,0,0,1,0,2], # 1
                                   [2,1,1,2,1,0,2]])# 0

        self.board.set_game_situation(test_situation)
        self.assertTrue(self.board.check_for_win(row=4, column=1, player=2))
        self.assertTrue(self.board.check_for_win(row=3, column=4, player=1))
        self.assertTrue(self.board.check_for_win(row=5, column=6, player=1))


    def test_four_discs_in_a_row_in_positive_diagonal_is_a_winning_move(self):
        """Tarkastaa, että metodi check_for_win tunnistaa vinottaisen voittavan siirron
        nousevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0], # 5
                                   [0,0,0,0,0,0,0], # 4
                                   [0,0,0,2,0,0,0], # 3
                                   [0,0,2,1,2,0,0], # 2
                                   [0,2,1,2,1,0,0], # 1
                                   [0,1,1,2,2,0,0]])# 0

        self.board.set_game_situation(test_situation)

        self.assertTrue(self.board.check_for_win(row=0, column=0, player=2))
        self.assertFalse(self.board.check_for_win(row=0, column=0, player=1))
        self.assertTrue(self.board.check_for_win(row=3, column=4, player=1))
        self.assertFalse(self.board.check_for_win(row=3, column=4, player=2))

    def test_four_discs_in_a_row_in_negative_diagonal_is_a_winning_move(self):
        """Tarkastaa, että metodi check_for_win tunnistaa vinottaisen voittavan siirron
        laskevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0], # 5
                                   [0,0,0,1,0,0,0], # 4
                                   [0,2,0,1,1,0,0], # 3
                                   [0,1,0,1,2,0,0], # 2
                                   [0,2,1,2,1,1,1], # 1
                                   [0,1,1,2,2,2,1]])# 0

        self.board.set_game_situation(test_situation)

        self.assertTrue(self.board.check_for_win(row=2, column=2, player=2))
        self.assertFalse(self.board.check_for_win(row=2, column=2, player=1))
        self.assertTrue(self.board.check_for_win(row=2, column=5, player=1))
        self.assertFalse(self.board.check_for_win(row=2, column=5, player=2))

    def test_get_available_columns_does_not_return_filled_columns(self):
        """Tarkastaa, että metodi get_available_columns palauttaa vain vapaina olevat sarakkeet."""
        # Täytetään joka toinen sarake 0, 2, 4, ja 6 kokonaan
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[2,0,2,0,1,0,2], # 5
                                   [1,0,1,2,2,0,1], # 4
                                   [2,0,2,2,1,0,2], # 3
                                   [1,0,1,1,2,0,2], # 2
                                   [2,0,2,1,1,0,1], # 1
                                   [1,2,1,1,2,0,1]])# 0

        self.board.set_game_situation(test_situation)

        # Metodin pitäisi palauttaa lista, joka sisältää sarakeindeksit 1, 3 ja 5
        available_columns = self.board.get_available_columns()
        self.assertCountEqual(available_columns, [1, 3, 5])

    def test_get_next_available_row_returns_correct_row(self):
        """Tarkastaa, että mrtodi get_next_available_row palauttaa seuraavan vapaana olevan
        rivin indeksin."""
        # Alustetaan pelilaudan tilanne
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0], # 5
                                   [1,0,0,0,0,0,0], # 4
                                   [2,0,0,0,0,0,0], # 3
                                   [1,0,0,0,0,0,2], # 2
                                   [2,0,0,0,0,0,1], # 1
                                   [1,2,0,0,0,0,1]])# 0

        self.board.set_game_situation(test_situation)

        self.assertEqual(self.board.get_next_available_row(column=0), 5)
        self.assertEqual(self.board.get_next_available_row(column=1), 1)
        self.assertEqual(self.board.get_next_available_row(column=3), 0)
        self.assertEqual(self.board.get_next_available_row(column=6), 3)

    def test_board_is_full_returns_true_if_all_columns_are_filled(self):
        """Tarkastaa, että metodi board_is_full palauttaa True, jos peliruudukon kaikki
        sarakkeet on täytetty, ja muuten False."""
        # Täytetään koko peliruudukko
        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[2,2,2,1,2,1,2], # 5
                                   [1,2,2,1,2,1,2], # 4
                                   [2,1,2,2,1,2,2], # 3
                                   [1,1,2,1,1,2,1], # 2
                                   [2,2,1,1,2,1,2], # 1
                                   [1,2,1,2,2,1,2]])# 0

        self.board.set_game_situation(test_situation)
        # Metodin pitäisi palauttaa True
        self.assertTrue(self.board.board_is_full())
        # Tyhjennetään sarakkeen 2 ylin ruutu (asetetaan arvoksi 0)
        self.board.update_position(row=5, column=2, value=EMPTY)
        # Metodin pitäisi nyt palauttaa False
        self.assertFalse(self.board.board_is_full())
