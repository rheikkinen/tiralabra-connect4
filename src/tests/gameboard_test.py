import unittest
from constants import ROW_COUNT
from gameboard import GameBoard

class TestGameBoard(unittest.TestCase):
    """Yksikkötestit GameBoard-luokan metodeille."""
    def setUp(self):
        """Alustusmetodi, jossa luodaan testejä varten tyhjä peliruudukko.
        Suoritetaan ennen jokaista testiä."""
        self.board = GameBoard() # Luo tyhjän peliruudukon/pelilaudan
        
    def test_column_is_available_returns_correct_boolean_values(self):
        """Tarkastaa, että colum_is_available-metodi palauttaa False,
        jos sarake on täynnä, ja muuten True."""
        # Täytetään peliruudukon neljäs sarake (indeksi 3)
        for row in range(ROW_COUNT):
            self.board.update_position(row, column=3, value=1)

        # Täysi sarake, pitäisi palauttaa False
        self.assertFalse(self.board.column_is_available(column=3))
        # Tyhjä sarake, pitäisi palauttaa True
        self.assertTrue(self.board.column_is_available(column=5))

    def test_horizontal_four_discs_in_a_row_is_a_winning_move(self):
        """Tarkastaa, että check_for_win-metodi tunnistaa vaakasuuntaisen voittavan siirron."""
        # Alustetaan pelilaudan tilanne
        # Asetetaan neljä kiekkoa vaakasuunnassa vierekkäin 
        for col in range(2,6):
            self.board.update_position(row=0, column=col, value=2)
        self.assertTrue(self.board.check_for_win())

    def test_vertical_four_discs_in_a_row_is_a_winning_move(self):
        """Tarkastaa, että check_for_win-metodi tunnistaa pystysuuntaisen voittavan siirron."""
        # Alustetaan pelilaudan tilanne
        # Asetetaan neljä kiekkoa pystysuunnassa peräkkäin
        for row in range (4):
            self.board.update_position(row, column=0, value=1)
        self.assertTrue(self.board.check_for_win())

    def test_four_discs_in_a_row_in_positive_diagonal_is_a_winning_move(self):
        """Tarkastaa, että check_for_win-metodi tunnistaa vinottaisen voittavan siirron
        nousevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # Asetetaan neljä kiekkoa vinottain nousevassa suunnassa peräkkäin
        #  0 0 0 2
        #  0 0 2 0
        #  0 2 0 0
        #  2 0 0 0
        self.board.update_position(row=0, column=0, value=2)
        self.board.update_position(row=1, column=1, value=2)
        self.board.update_position(row=2, column=2, value=2)
        self.board.update_position(row=3, column=3, value=2)

        self.assertTrue(self.board.check_for_win())

    def test_four_discs_in_a_row_in_negative_diagonal_is_a_winning_move(self):
        """Tarkastaa, että check_for_win-metodi tunnistaa vinottaisen voittavan siirron
        laskevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # Asetetaan neljä kiekkoa vinottain laskevassa suunnassa peräkkäin
        #  1 0 0 0
        #  0 1 0 0
        #  0 0 1 0
        #  0 0 0 1
        self.board.update_position(row=3, column=0, value=1)
        self.board.update_position(row=2, column=1, value=1)
        self.board.update_position(row=1, column=2, value=1)
        self.board.update_position(row=0, column=3, value=1)

        self.assertTrue(self.board.check_for_win())
