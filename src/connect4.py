import numpy as np
from constants import COLUMN_NUMBERS
from gameboard import GameBoard
from ai import AI


class ConnectFour:
    def __init__(self):
        self.board = GameBoard()
        self.ai = AI() # pylint: disable=invalid-name
        self.game_over = False
        self.column_numbers = np.array(COLUMN_NUMBERS, dtype=int, ndmin=2)

    def print_board(self): # UI
        print(self.column_numbers)
        print(np.flip(self.board.get_board(), 0))

    def drop_disc(self, row, column, player):
        self.board.update_position(row, column, value=player)

    def column_is_available(self, column):
        """Palauttaa True, jos sarake on vapaa. Muuten palauttaa False."""
        return self.board.column_is_available(column)

    def game_is_tied(self):
        """Palauttaa True, jos kaikki sarakkeet ovat täynnä, muuten palauttaa False."""
        return self.board.all_columns_are_filled()

    def player_won(self, last_row, last_col, player):
        """Palauttaa True, jos viimeksi pudotettu kiekko muodostaa lähellä olevien
        kiekkojen kanssa voittavan kiekkojonon. Muuten palauttaa False."""
        return self.board.check_for_win(last_row, last_col, player)

    def valid_input(self, user_input):
        """Validoi käyttäjän antaman syötteen."""
        try:
            user_input = int(user_input)
        except ValueError:
            return False
        for column in COLUMN_NUMBERS:
            if user_input == column:
                return True
        return False

    def start_game(self):
        player = 1

        print(f"Tekoäly on pelaaja nro {self.ai.player()}")

        while not self.game_over:
            self.print_board()
            print("")

            if player != self.ai.player():
                message = f"Pelaaja {player}, valitse sarake, johon haluat pudottaa kiekon: "
                selected_column = input(message)
                print("")
                if not self.valid_input(selected_column):
                    print("Antamasi syöte on virheellinen!\n")
                    continue
                selected_column = int(selected_column) - 1

            else:
                print(f"Pelaaja {player} (tekoäly) valitsee sarakkeen.\n")
                selected_column = self.ai.best_column(self.board)

            if self.board.column_is_available(selected_column):
                # Haetaan positions-muuttujan avulla sarakkeen seuraava vapaa rivi
                row = self.board.get_next_available_row(selected_column)
                self.drop_disc(row, selected_column, player)

                self.ai.store_last_move(row, selected_column)

                if self.player_won(row, selected_column, player):
                    print(f"\nPelaaja {player} voitti pelin!\n")
                    self.print_board()

                    self.game_over = True

                elif self.game_is_tied():
                    print("Tasapeli!")

                    self.game_over = True

                player = (player % 2) + 1
            else:
                print(f"\nSarake {selected_column} on täynnä! Valitse toinen sarake.\n")
