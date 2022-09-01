import numpy as np
import sys
from termcolor import colored
from connect4 import ConnectFour, connect_four as game
from constants import COLUMN_NUMBERS, ROW_COUNT
from gameboard import GameBoard

class CLI:
    """Komentorivikäyttöliittymä"""
    def __init__(self):
        self.quit = False
        self.play = False
        self.ai_mode = False

        self.levels = {
            0: "helpoin",
            1: "keskitaso",
            2: "vaikea"
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
                print("1 = ihminen vs ihminen")
                print("2 = ihminen vs tietokone")
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
            print("0 = helpoin")
            print("1 = keskitaso")
            print("2 = vaikea")
            user_input = self.ask_input()
            if user_input in ["0", "1", "2"]:
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
            for i in board[row]:
                if i == 1:
                    row_to_print += colored("X", "red")
                elif i == 2:
                    row_to_print += colored("O", "yellow")
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
            print(f"\nPelaaja {player} ({self.player_discs[player]}), valitse haluamasi sarake väliltä 1-7:")
            print("(Lopeta peli komennolla q)")
            user_input = self.ask_input()
            if user_input in ["q", "Q"]:
                self.play = False
                self.quit = True
                return -1
            elif self.is_valid_input(user_input):
                return int(user_input)
            self.print_error("Virheellinen syöte!")
            self.print_board(game.board)

    def select_starting_player(self):
        while True:
            if self.ai_mode:
                print("\nValitse aloittava pelaaja (1 = ihminen, 2 = tekoäly)\n")
            else:
                print("\nValitse aloittava pelaaja (1 tai 2)\n")
            
            user_input = self.ask_input()

            if user_input in ["1", "2"]:
                return int(user_input)
            else:
                self.print_error("Virheellinen syöte!")

    def print_endgame_message(self, game: ConnectFour):
        if game.game_ended_in_tie():
            message = "Tasapeli!"
        else:
            message = f"Pelaaja {game.player_in_turn} voitti pelin!"
        print(colored(message, "green"))

    def new_game(self):
        while True:
            print(colored("\nUusi peli (y = kyllä / n = ei)?", "green"))
            user_input = self.ask_input()
            if user_input in ["y", "Y"]:
                return True
            if user_input in ["n", "N"]:
                self.play = False
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
        return input(colored(">> ", "green"))

    def print_stats(self):
        tie_count, player1_win_count, player2_win_count = game.results
        print("Tulokset")
        print("--------------------")
        print(f"P1 voitot: {player1_win_count}")
        print(f"P2 voitot: {player2_win_count}")
        print(f"Tasapelit: {tie_count}")

    def start_game(self):
        self.print_welcome()
        while True:
            self.print_menu()

            game.starting_player = self.select_starting_player()
            game.player_in_turn = game.starting_player

            print(f"\nPeli alkoi. Tekoäly on pelaaja nro {game.ai.player()}\n")

            while not game.game_over:
                self.print_board(game.board)
                if game.player_in_turn != game.ai.player() or not self.ai_mode:
                    user_input = self.select_move(game.player_in_turn)
                    if self.quit:
                        game.quit_game()
                    selected_column = user_input - 1
                else:
                    print(f"\nPelaaja {game.player_in_turn} (tekoäly) valitsee sarakkeen.\n")
                    selected_column, _, runtime = game.ai.best_column(game.board)
                    game.ai_times.append(runtime)

                if game.board.column_is_available(selected_column):
                    game.drop_disc(selected_column, game.player_in_turn)

                    if game.player_won() or game.game_ended_in_tie():
                        self.print_endgame_message(game)
                        self.print_board(game.board)
                        self.print_stats()

                        if self.new_game():
                            game.change_starting_player()
                            game.player_in_turn = game.starting_player
                            game.board.reset_board()
                            continue
                        game.game_over = True

                    game.change_turn()
                else:
                    self.print_error(f"Sarake {selected_column+1} on täynnä! Valitse toinen sarake.")

            if game.ai_times:
                average_time = sum(game.ai_times) / len(game.ai_times)
                print(f"\nTekoälyn suoritusaika keskimäärin: {average_time} sekuntia")