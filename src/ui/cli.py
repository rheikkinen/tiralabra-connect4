import numpy as np
import sys
from termcolor import colored
from connect4 import ConnectFour, connect_four as game
from constants import COLUMN_NUMBERS, ROW_COUNT
from gameboard import GameBoard

class CLI:
    """Komentorivikäyttöliittymä"""
    def __init__(self):
        self.play = False
        self.ai_mode = False

        self.levels = {
            1: "helpoin",
            2: "keskitaso",
            3: "vaikea"
        }

        self.player_discs = {
            1: "X",
            2: "O"
        }

    def print_menu(self):
        while not self.play:
            print("\n============== Komennot ==============")
            print(colored("[1]", "green"), "- aloita peli")
            print(colored("[2]", "green"), f"- aseta vaikeustaso (valittu: {self.levels[game.ai_level]})")
            print(colored("[q]", "green"), "- lopeta peli")
            print("======================================\n")
            command = input(colored("Syötä komento >> ", "green"))

            if command == "1":
                print("\nValitse pelitapa:")
                print(">> 1 = ihminen vs ihminen")
                print(">> 2 = ihminen vs tekoäly")
                user_input = self.ask_input()
                if user_input == "1":
                    self.ai_mode = False
                elif user_input == "2":
                    self.ai_mode = True
                self.play = True
            elif command == "2":
                self.choose_ai_level()
            elif command in ["q", "Q"]:
                sys.exit()
            else:
                self.print_error("Virheellinen komento!")

    def choose_ai_level(self):
        while True:
            print("\nValitse tekoälypelaajan vaikeustaso:")
            print(">> 1 = helpoin")
            print(">> 2 = keskitaso")
            print(">> 3 = vaikea")
            user_input = self.ask_input()
            if user_input in ["1", "2", "3"]:
                game.set_ai_level(int(user_input))
                break
            else:
                self.print_error("Virheellinen syöte!")

    def print_board(self, gameboard: GameBoard): 
        print("")
        board = np.flip(gameboard.get_board(), 0)
        numbers = "|"
        for number in COLUMN_NUMBERS:
            numbers += f"{number}|"
        print(numbers)
        for row in range(ROW_COUNT):
            row_to_print = "|"
            for position in board[row]:
                if position == 1:
                    row_to_print += colored(self.player_discs[1], "red")
                elif position == 2:
                    row_to_print += colored(self.player_discs[2], "yellow")
                else:
                    row_to_print += "_"
                row_to_print += "|"
            print(row_to_print)
        print(numbers)
        print("")

    def print_welcome(self):
        print(colored("\nTervetuloa Connect 4 -peliin!\n", "green"))

    def select_move(self, player):
        while True:
            print(f"\nPelaaja {player} ('{self.player_discs[player]}'), valitse sarake väliltä 1-7:")
            print("(Lopeta peli komennolla q)")
            user_input = self.ask_input()
            if user_input in ["q", "Q"]:
                return None
            elif self.is_valid_input(user_input):
                return int(user_input)
            self.print_error("Virheellinen syöte!")
            self.print_board(game.board)

    def select_starting_player(self):
        while True:
            if self.ai_mode:
                print("\nValitse aloittava pelaaja (1 = ihminen, 2 = tekoäly)")
            else:
                print("\nValitse aloittava pelaaja (1 tai 2)")
            
            user_input = self.ask_input()

            if user_input in ["1", "2"]:
                return int(user_input)
            else:
                self.print_error("Virheellinen syöte!")

    def print_endgame_message(self, game: ConnectFour):
        if game.game_ended_in_tie():
            message = "\nTasapeli!"
        else:
            message = f"\nPelaaja {game.player_in_turn} voitti pelin!"
        print(colored(message, "green"))

    def new_game(self):
        while True:
            print(colored("\nUusi peli (y = kyllä / n = ei)?", "green"))
            user_input = self.ask_input()
            if user_input in ["y", "Y"]:
                return True
            if user_input in ["n", "N"]:
                return False
            else:
                self.print_error("Virheellinen syöte!")

    def is_valid_input(self, user_input):
        """Validoi käyttäjän antaman syötteen."""
        try:
            user_input = int(user_input)
        except ValueError:
            return False
        for column in COLUMN_NUMBERS:
            if user_input == column:
                return True
        return False

    def print_error(self, message):
        print(colored(f"\n{message}\n", "red"))

    def ask_input(self):
        return input(colored("\n>> ", "green"))

    def print_stats(self):
        tie_count, first_player_win_count, second_player_win_count = game.results
        print("")
        print(colored(f"P1 voitot: {first_player_win_count}", "red"))
        print(colored(f"P2 voitot: {second_player_win_count}", "yellow"))
        print(f"Tasapelit: {tie_count}")

    def start_game(self):
        self.print_welcome()
        while True:
            self.print_menu()

            game.starting_player = self.select_starting_player()
            game.player_in_turn = game.starting_player

            if self.ai_mode:
                print(f"\nPeli alkoi. Tekoäly on pelaaja nro {game.ai.player()}\n")

            while self.play:
                self.print_board(game.board)
                if not self.ai_mode or game.player_in_turn != game.ai.player():
                    selection_done = self.select_move(game.player_in_turn)
                    if not selection_done: # Peli lopetettu
                        game.board.reset_board()
                        self.play = False
                        break
                    else:
                        selected_column = selection_done - 1
                else:
                    print(f"\nPelaaja {game.player_in_turn} (tekoäly) valitsee sarakkeen.\n")
                    selected_column, value, runtime = game.ai.best_column(game.board)
                    print(colored(f"Tekoäly valitsi sarakkeen {selected_column + 1} pisteytyksellä {value}", "green"))

                    game.ai_times.append(runtime)

                if game.board.column_is_available(selected_column):
                    game.drop_disc(selected_column, game.player_in_turn)

                    if game.player_won() or game.game_ended_in_tie():
                        self.print_endgame_message(game)
                        self.print_board(game.board)
                        self.print_stats()
                        game.board.reset_board()

                        if self.new_game():
                            game.change_starting_player()
                            game.player_in_turn = game.starting_player
                            continue
                        else:
                            self.play = False

                    game.change_turn()
                else:
                    self.print_error(f"Sarake {selected_column+1} on täynnä! Valitse toinen sarake.")

            if game.ai_times:
                average_time = sum(game.ai_times) / len(game.ai_times)
                print(f"\nAlgoritmin suoritusaika keskimäärin: {round(average_time, 7)} sekuntia")
                game.ai_times.clear()
