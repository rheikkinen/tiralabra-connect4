
import numpy as np

from constants import COL_COUNT, ROW_COUNT, ORDER

class GameBoard:
    def __init__(self, rows=ROW_COUNT, columns=COL_COUNT, winning_row=4):
        self.rows = rows
        self.columns = columns
        self._board = self.init_board(self.rows, self.columns)
        self._winning_row = winning_row

    def init_board(self, rows, columns):
        return np.zeros((rows, columns), dtype=int)

    def reset_board(self):
        self._board = self.init_board(self.rows, self.columns)

    def get_board(self):
        return self._board

    def update_position(self, row, column, value):
        self._board[row][column] = value

    def get_position(self, row, column):
        return self._board[row][column]

    def column_is_available(self, column):
        return self.get_position(ROW_COUNT-1, column) == 0

    def get_available_columns(self):
        valid_columns = []
        for column in ORDER:
            if self.column_is_available(column):
                valid_columns.append(column)

        return valid_columns

    def get_next_available_row(self, column):
        for row in range(ROW_COUNT):
            if self.get_position(row, column) == 0:
                return row

    def all_columns_are_filled(self):
        for column in range(COL_COUNT):
            if self.column_is_available(column):
                return False
        return True

    def end_state(self, row, column, player):
        if self.check_for_win(row, column, player):
            return player # 1 tai 2
        if self.all_columns_are_filled():
            return 0 # tasapeli
        return None

    def check_for_win(self, row, column, player):
        return self.check_horizontal_discs(row, column, player) \
            or self.check_vertical_discs(row, column, player) \
            or self.check_positive_diagonal(row, column, player) \
            or self.check_negative_diagonal(row, column, player) \
            or False

    def check_horizontal_discs(self, last_row, last_col, player_disc):
        """Tarkastaa muodostaako pudotettu kiekko vaakasuunnassa voittavan
        kiekkojonon (oletus 4 kiekkoa). Palauttaa True, jos voittava jono löytyy.
        Muuten palauttaa None."""

        discs_in_a_row = 1

        # Tarkastetaan pudotetun kiekon oikea puoli
        for col in range(last_col + 1, last_col + 4):
            if col > 6 or self.get_position(last_row, col) != player_disc:
                break
            if self.get_position(last_row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Tarkastetaan pudotetun kiekon vasen puoli
        for col in range(last_col - 1, last_col - 4, -1):
            if col < 0 or self.get_position(last_row, col) != player_disc:
                break
            if self.get_position(last_row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return None

    def check_vertical_discs(self, last_row, last_col, player_disc):
        """Tarkastaa, muodostaako pudotettu kiekko pystysuunnassa
        voittavan neljän kiekon jonon. Palauttaa True, jos neljän kiekon jono löytyy.
        Muuten paluttaa None."""

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

    def check_positive_diagonal(self, last_row, last_col, player_disc):
        """Tarkastaa, muodostaako pudotettu kiekko vinottain (nouseva suunta)
        voittavan neljän kiekon jonon. Palauttaa True jos neljän kiekon jono löytyy.
        Muuten paluttaa None."""

        discs_in_a_row = 1

        # Oikea yläviisto
        for row, col in zip(range(last_row + 1, last_row + 4),\
                            range(last_col + 1, last_col + 4)):
            if row > 5 or col > 6 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Vasen alaviisto
        for row, col in zip(range(last_row - 1, last_row - 4, -1),\
                            range(last_col - 1, last_col - 4, -1)):
            if row < 0 or col < 0 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return None

    def check_negative_diagonal(self, last_row, last_col, player_disc):
        """Tarkastaa, muodostaako pudotettu kiekko vinottain (laskeva suunta)
        voittavan neljän kiekon jonon. Palauttaa True jos neljän kiekon jono löytyy.
        Muuten paluttaa None."""

        discs_in_a_row = 1

        # Vasen yläviisto
        for row, col in zip(range(last_row + 1, last_row + 4),\
                            range(last_col - 1, last_col - 4, -1)):
            if row > 5 or col < 0 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        # Oikea alaviisto
        for row, col in zip(range(last_row - 1, last_row - 4, -1),\
                            range(last_col + 1, last_col + 4)):
            if row < 0 or col > 6 or self.get_position(row, col) != player_disc:
                break
            if self.get_position(row, col) == player_disc:
                discs_in_a_row += 1
            if discs_in_a_row == self._winning_row:
                return True

        return None
