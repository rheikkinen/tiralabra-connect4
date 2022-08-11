
import numpy as np

from constants import COL_COUNT, ROW_COUNT, ORDER

class GameBoard:
    def __init__(self, rows=ROW_COUNT, columns=COL_COUNT, winning_row=4):
        self.rows = rows
        self.columns = columns
        self._board = self.init_board(self.rows, self.columns)
        self._winning_row = winning_row
        self.last_move = None, None, None

    def init_board(self, rows: int, columns: int):
        return np.zeros((rows, columns), dtype=int)

    def reset_board(self):
        self._board = self.init_board(self.rows, self.columns)

    def print_board(self): # UI
        print(np.flip(self._board, 0))

    def get_board(self):
        return self._board

    def store_last_move(self, row: int, column: int, player: int):
        """Tallentaa oliolle viimeisimmän siirron koordinaatit
        ja siirron tehneen pelaajan."""
        self.last_move = row, column, player

    def get_last_move(self):
        """Palauttaa viimeisimmän siirron sijainnin pelilaudalla
        (rivi ja sarake) ja siirron tehneen pelaajan."""
        return self.last_move

    def update_position(self, row: int, column: int, value: int):
        self._board[row][column] = value
        self.store_last_move(row, column, value)

    def get_position(self, row: int, column: int):
        return self._board[row][column]

    def column_is_available(self, column: int):
        return self.get_position(ROW_COUNT-1, column) == 0

    def get_available_columns(self):
        """Palauttaa listana peliruudukon vapaana olevat sarakkeet
        järjestyksessä keskimmäisistä reunimmaisiin."""
        valid_columns = []
        for column in ORDER:
            if self.column_is_available(column):
                valid_columns.append(column)
        return valid_columns

    def get_next_available_row(self, column: int):
        for row in range(ROW_COUNT):
            if self.get_position(row, column) == 0:
                return row
        return None

    def board_is_full(self):
        for column in range(COL_COUNT):
            if self.column_is_available(column):
                return False
        return True

    def check_for_win(self, row, column, player):
        return self.check_horizontal_discs(row, column, player) \
            or self.check_vertical_discs(row, column, player) \
            or self.check_positive_diagonal(row, column, player) \
            or self.check_negative_diagonal(row, column, player) \
            or False

    def check_horizontal_discs(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako pudotettu kiekko vaakasuunnassa voittavan
        kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava jono löytyy.
        Muuten palauttaa None."""

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

        return None

    def check_vertical_discs(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako pudotettu kiekko pystysuunnassa voittavan
        kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava jono löytyy.
        Muuten palauttaa None."""

        discs_in_a_row = 1

        # Tarkastetaan pudotetun kiekon alapuolella olevat ruudut
        for row in range(last_row - 1, last_row - 4, -1):
            if row < 0 or self.get_position(row, last_col) != player_disc:
                break
            if self.get_position(row, last_col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return None

    def check_positive_diagonal(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako pudotettu kiekko vinottain (nouseva suunta)
        voittavan kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava
        jono löytyy. Muuten paluttaa None."""

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

        return None

    def check_negative_diagonal(self, last_row: int, last_col: int, player_disc: int):
        """Tarkastaa, muodostaako pudotettu kiekko vinottain (laskeva suunta)
        voittavan kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava
        jono löytyy. Muuten palauttaa None."""

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

        return None
