import sys
import numpy as np
from termcolor import colored
from constants import COLUMN_NUMBERS
from gameboard import GameBoard
from ai import AI


class ConnectFour:
    """Luokan vastuulle tulee jäämään pelilogiikkaa suorittavat metodit."""
    def __init__(self):
        self.board = GameBoard()
        self.ai = AI() # pylint: disable=invalid-name
        self.column_numbers = np.array(COLUMN_NUMBERS, dtype=int, ndmin=2)
        self.starting_player = 1
        self.player_in_turn = 1
        self.game_over = False

        self.ai_times = [] # Listaa tekoälyn suoritusajat

    def print_board(self): # UI
        print("")
        print(np.flip(self.board.get_board(), 0))
        print("")
        print(self.column_numbers)

    def print_welcome(self):
        print("\nTervetuloa Connect 4 -peliin!\n")

    def ask_input(self):
        message = f"\nPelaaja {self.player_in_turn}, syötä haluamasi sarake väliltä 1-7 tai lopeta peli syöttämällä q: "
        return input(message)

    def print_endgame_message(self):
        if self.game_ended_in_tie():
            message = "\nTasapeli!\n"
        else:
            message = f"\nPelaaja {self.player_in_turn} voitti pelin!\n"
        print(colored(message, "red"))

    def new_game(self):
        user_input = input("\nUusi peli (y = kyllä / n = ei)? ")
        return user_input in ["y", "Y"]

    def quit_game(self):
        self.game_over = True

    def change_turn(self):
        self.player_in_turn = (self.player_in_turn % 2) + 1

    def drop_disc(self, column, player):
        row = self.board.get_next_available_row(column)
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
        row, column, player = self.board.get_last_move()
        return self.board.check_for_win(row, column, player)

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
        self.print_welcome()
        print("1 = helppo")
        print("2 = keskitaso")
        print("3 = vaikea\n")
        level = input("Valitse pelitekoälyn vaikeustaso: ")
        try:
            self.ai = AI(level=int(level))
        except ValueError:
            pass

        self.starting_player = int(input("\nAloittava pelaaja (1 = käyttäjä, 2 = tekoäly): "))
        self.player_in_turn = self.starting_player

        print(f"\nPeli alkoi. Tekoäly on pelaaja nro {self.ai.player()}\n")

        while not self.game_over:
            self.print_board()

            if self.player_in_turn != self.ai.player():
                user_input = self.ask_input()
                print("")
                if user_input in ["q", "Q"]:
                    self.game_over = True
                elif not self.valid_input(user_input):
                    print("Antamasi syöte on virheellinen!\n")
                    continue
                selected_column = int(user_input) - 1

            else:
                print(f"\nPelaaja {self.player_in_turn} (tekoäly) valitsee sarakkeen.\n")
                selected_column, _, runtime = self.ai.best_column(self.board)
                self.ai_times.append(runtime)

            if self.board.column_is_available(selected_column):
                self.drop_disc(selected_column, self.player_in_turn)

                if self.player_won() or self.game_ended_in_tie():
                    self.print_endgame_message()
                    self.print_board()

                    if self.new_game():
                        self.starting_player = self.starting_player % 2 + 1
                        self.player_in_turn = self.starting_player
                        self.board.reset_board()
                        continue
                    self.game_over = True

                self.change_turn()
            else:
                print(f"\nSarake {selected_column+1} on täynnä! Valitse toinen sarake.\n")

        average_time = sum(self.ai_times) / len(self.ai_times)
        print(f"\nTekoälyn suoritusaika keskimäärin: {average_time} sekuntia")
