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

        self.ai_times = [] # Listaa tekoälyn suoritusajat

    def print_board(self): # UI
        print(self.column_numbers, "\n")
        self.board.print_board()

    def drop_disc(self, row, column, player):
        self.board.update_position(row, column, value=player)

    def column_is_available(self, column):
        """Palauttaa True, jos sarake on vapaa. Muuten palauttaa False."""
        return self.board.column_is_available(column)

    def game_ended_in_tie(self):
        """Palauttaa True, jos kaikki sarakkeet ovat täynnä, muuten palauttaa False."""
        return self.board.board_is_full()

    def player_won(self):
        """Palauttaa True, jos viimeksi pudotettu kiekko muodostaa lähellä olevien
        kiekkojen kanssa voittavan kiekkojonon. Muuten palauttaa False."""
        return self.board.check_for_win()

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
        player = 1 # Aloittava pelaaja

        print(f"Peli alkoi. Tekoäly on pelaaja nro {self.ai.player()}\n")

        while not self.game_over:
            self.print_board()


            if player != self.ai.player():
                message = f"\nPelaaja {player}, syötä haluamasi sarake väliltä 1-7 tai lopeta peli syöttämällä q: "
                user_input = input(message)
                print("")
                if user_input == "q" or user_input == "Q":
                    print("Peli lopetetaan.")
                    self.game_over = True
                elif not self.valid_input(user_input):
                    print("Antamasi syöte on virheellinen!\n")
                    continue
                else:
                    selected_column = int(user_input) - 1

            else:
                print(f"Pelaaja {player} (tekoäly) valitsee sarakkeen.\n")
                selected_column, _, runtime = self.ai.best_column(self.board)
                self.ai_times.append(runtime)

            if self.board.column_is_available(selected_column):
                row = self.board.get_next_available_row(selected_column)

                self.drop_disc(row, selected_column, player)

                if self.player_won():
                    print(f"\nPelaaja {player} voitti pelin!\n")
                    self.print_board()

                    self.game_over = True

                elif self.game_ended_in_tie():
                    print("\nTasapeli!\n")
                    self.print_board()

                    self.game_over = True

                player = (player % 2) + 1
            else:
                print(f"\nSarake {selected_column} on täynnä! Valitse toinen sarake.\n")

        average_time = sum(self.ai_times) / len(self.ai_times)
        print(f"\nTekoälyn suoritusaika keskimäärin: {average_time} sekuntia")
