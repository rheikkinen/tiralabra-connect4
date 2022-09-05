
import numpy as np

from constants import COL_COUNT, EMPTY, ROW_COUNT, ORDER

class GameBoard:
    """Luokan vastuulla on pelitilanteen ylläpito ja muut pelilautaan kohdistuvat metodit."""
    def __init__(self, rows=ROW_COUNT, columns=COL_COUNT, winning_row=4):
        self.rows = rows
        self.columns = columns
        self._board = self.init_board(self.rows, self.columns)
        self._winning_row = winning_row
        self._last_move = None, None, None

    def init_board(self, rows: int, columns: int):
        """Palauttaa 2-ulotteisen taulukon (oletuskoko 7x6), joka on täytetty nollilla."""
        return ([[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]])

    def reset_board(self):
        """Palauttaa pelilaudan alkutilaan (kaikki ruudut tyhjiä eli arvoiltaan 0)."""
        self._board = self.init_board(self.rows, self.columns)

    def set_game_situation(self, game_situation: np.ndarray):
        """Testauksessa pelitilanteen määrittämiseen käytettävä metodi, joka
        asettaa peliruudukoksi parametrina annetun taulukon."""
        self._board = np.flip(game_situation, 0)

    def get_board(self):
        return self._board

    def store_last_move(self, row: int, column: int, player: int):
        """Tallentaa muuttujaan viimeisimmän siirron koordinaatit
        ja siirron tehneen pelaajan."""
        self._last_move = row, column, player

    def get_last_move(self):
        """Palauttaa viimeisimmän siirron sijainnin pelilaudalla
        (rivi ja sarake) ja siirron tehneen pelaajan."""
        return self._last_move

    def update_position(self, row: int, column: int, value: int):
        """Asettaa parametrina annetun arvon annettuihin koordinaatteihin
        ja tallettaa siirron tiedot muuttujaan."""
        self._board[row][column] = value
        self.store_last_move(row, column, value)

    def clear_position(self, row: int, column: int):
        """Tyhjentää ruudun eli asettaa ruudun arvon nollaksi parametrina
        annetussa sijainnissa."""
        self._board[row][column] = EMPTY

    def get_position(self, row: int, column: int):
        """Palauttaa parametrina annetussa sijainnissa olevan ruudun arvon."""
        return self._board[row][column]

    def column_is_available(self, column: int):
        """Tarkastaa, onko annettu sarake vapaa.

        :param column: Tarkastettava sarake

        :rtype: bool
        :return: Palauttaa True, jos sarakkeen ylin ruutu on tyhjä (arvo 0).
        Muuten palauttaa False.
        """
        return self.get_position(ROW_COUNT-1, column) == EMPTY

    def get_available_columns(self):
        """Palauttaa listana peliruudukon vapaana olevat sarakkeet
        järjestyksessä keskimmäisistä reunimmaisiin."""
        valid_columns = []
        for column in ORDER:
            if self.column_is_available(column):
                valid_columns.append(column)
        return valid_columns

    def get_next_available_row(self, column: int):
        """Hakee seuraavan vapaana olevan rivin annetussa sarakkeessa ja palauttaa
        rivin indeksin."""
        for row in range(ROW_COUNT):
            if self.get_position(row, column) == 0:
                return row
        return None

    def board_is_full(self):
        """Tarkastaa, onko peliruudukko täynnä.

        :rtype: bool
        :return: Palauttaa True, jos yksikään ruudukon sarakkeista ei ole vapaa.
        Muuten palauttaa False."""
        for column in range(COL_COUNT):
            if self.column_is_available(column):
                return False
        return True

    def check_for_win(self, row: int, column: int, player: int):
        """Tarkastaa, muodostaako parametrina annettu siirto
        voittavan kiekkojonon vaakasuunnassa, pystysuunnassa tai vinottain.

        :param row: Siirron rivi-indeksi
        :param column: Siirron sarake-indeksi
        :param player: Siirron tehnyt pelaaja, 1 tai 2

        :rtype: bool
        :return: Palauttaa True, jos siirto on voittava siirto. Muuten palauttaa False.
        """
        return self.check_horizontal_win(row, column, player) \
            or self.check_vertical_win(row, column, player) \
            or self.check_positive_diagonal_win(row, column, player) \
            or self.check_negative_diagonal_win(row, column, player)

    def check_horizontal_win(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako annettu siirto vaakasuunnassa voittavan
        kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava jono löytyy.
        Muuten palauttaa False."""
        discs_in_a_row = 1

        # Tarkastetaan pudotetun kiekon oikealla puolella olevat ruudut
        for col in range(last_col + 1, last_col + 4):
            if col > 6 or self.get_position(last_row, col) != player_disc:
                break
            if self.get_position(last_row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Tarkastetaan pudotetun kiekon vasemmalla puolella olevat ruudut
        for col in range(last_col - 1, last_col - 4, -1):
            if col < 0 or self.get_position(last_row, col) != player_disc:
                break
            if self.get_position(last_row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return False

    def check_vertical_win(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako annettu siirto pystysuunnassa voittavan
        kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava jono löytyy.
        Muuten palauttaa False."""
        discs_in_a_row = 1

        # Tarkastetaan pudotetun kiekon alapuolella olevat ruudut
        for row in range(last_row - 1, last_row - 4, -1):
            if row < 0 or self.get_position(row, last_col) != player_disc:
                break
            if self.get_position(row, last_col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return False

    def check_positive_diagonal_win(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako annettu siirto vinottain (nouseva suunta)
        voittavan kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava
        jono löytyy. Muuten paluttaa False."""
        discs_in_a_row = 1

        # Tarkastetaan ruudut pudotetusta kiekosta oikeaan yläviistoon
        for row, col in zip(range(last_row + 1, last_row + 4),\
                            range(last_col + 1, last_col + 4)):
            if row > 5 or col > 6 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Tarkastetaan ruudut pudotetusta kiekosta vasempaan alaviistoon
        for row, col in zip(range(last_row - 1, last_row - 4, -1),\
                            range(last_col - 1, last_col - 4, -1)):
            if row < 0 or col < 0 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return False

    def check_negative_diagonal_win(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako annettu siirto vinottain (laskeva suunta)
        voittavan kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava
        jono löytyy. Muuten palauttaa False."""
        discs_in_a_row = 1

        # Tarkastetaan ruudut pudotetusta kiekosta vasempaan yläviistoon
        for row, col in zip(range(last_row + 1, last_row + 4),\
                            range(last_col - 1, last_col - 4, -1)):
            if row > 5 or col < 0 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Tarkastetaan ruudut pudotetusta kiekosta oikeaan alaviistoon
        for row, col in zip(range(last_row - 1, last_row - 4, -1),\
                            range(last_col + 1, last_col + 4)):
            if row < 0 or col > 6 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True
        return False
