import numpy as np
from game_ai import AI
from constants import ROW_COUNT, COL_COUNT

class ConnectFour:
    def __init__(self):
        self.positions = [0]*COL_COUNT
        self.game_over = False
        self.column_numbers = np.array([1,2,3,4,5,6,7], dtype=int, ndmin=2)

    def init_board(self, rows, columns):
        return np.zeros((rows, columns), dtype=int)

    def print_board(self, board):
        print(self.column_numbers)
        print(np.flip(board, 0))

    def drop_disc(self, board, row, column, player):
        board[row][column] = player

    def column_is_available(self, board, column):
        """Palauttaa True, jos sarake on vapaa eli ylimmän ruudun arvo on 0, muuten palauttaa False."""
        return board[ROW_COUNT- 1][column] == 0

    def board_is_full(self, board):
        """Palauttaa True, jos kaikki sarakkeet ovat täynnä, muuten palauttaa False."""
        for column in range(0,7):
            if self.column_is_available(board, column):
                return False
        return True

    def check_horizontal(self, board, last_row, last_col, player):
        """Tarkastaa pudotetun kiekon oikealla ja vasemmalla puolella olevat kiekot"""
        discs_in_a_row = 1
        # Aloitetaan tarkastus pudotetun kiekon oikealta puolelta
        for col in range(last_col + 1, last_col + 4):
            if col > 6 or board[last_row][col] != player:
                break
            if board[last_row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

        # Jatketaan pudotetun kiekon vasemmalta puolelta
        for col in range(last_col - 1, last_col - 4, -1):
            if col < 0 or board[last_row][col] != player:
                break
            if board[last_row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

    def check_vertical(self, board, last_row, last_col, player):
        """Tarkastaa pudotetun kiekon alapuolella olevat kiekot"""
        discs_in_a_row = 1
        for row in range(last_row - 1, last_row - 4, -1):
            if row < 0 or board[row][last_col] != player:
                break
            if board[row][last_col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

    def check_diagonal(self, board, last_row, last_col, player):
        """Tarkastaa vinottaisissa suunnissa olevat kiekot"""
        discs_in_a_row = 1
        # Oikea yläviisto
        for row, col in zip(range(last_row + 1, last_row + 4), range(last_col + 1, last_col + 4)):
            if row > 5 or col > 6 or board[row][col] != player:
                break
            if board[row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

        # Vasen alaviisto
        for row, col in zip(range(last_row - 1, last_row - 4, -1), range(last_col - 1, last_col - 4, -1)):
            if row < 0 or col < 0 or board[row][col] != player:
                break
            if board[row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True 

        discs_in_a_row = 1
        # Vasen yläviisto
        for row, col in zip(range(last_row + 1, last_row + 4), range(last_col - 1, last_col - 4, -1)):
            if row > 5 or col < 0 or board[row][col] != player:
                break
            if board[row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

        # Oikea alaviisto
        for row, col in zip(range(last_row - 1, last_row - 4, -1), range(last_col + 1, last_col + 4)):
            if row < 0 or col > 6 or board[row][col] != player:
                break
            if board[row][col] == player:
                discs_in_a_row += 1
            if discs_in_a_row == 4:
                return True

    def end_state(self, board, last_row, last_col, player):
        if self.player_won(board, last_row, last_col, player):
            return player # 1 tai 2
        elif self.board_is_full(board): # tasapeli
            return 0
        return None

    def player_won(self, board, last_row, last_col, player):
        """Tarkastaa, onko viimeksi pudotetun kiekon läheisyydessä neljän suora."""
        return self.check_horizontal(board, last_row, last_col, player) \
            or self.check_vertical(board, last_row, last_col, player) \
            or self.check_diagonal(board, last_row, last_col, player) \
            or False

    def valid_input(self, input):
        """Validoi käyttäjän antaman syötteen."""
        try:
            input = int(input)
        except:
            return False
        for column in self.column_numbers[0]:
            if input == column:
                return True
        return False

    def start_game(self):
        board = self.init_board(ROW_COUNT, COL_COUNT)
        state = 0
        ai = AI(game=ConnectFour())
        print(f"Tekoäly on pelaaja nro {ai.player}")

        while not self.game_over:
            player = state + 1
            self.print_board(board)
            print("")
            if player != ai.player:
                selectedColumn = input(f"Pelaaja {player}, valitse sarake, johon haluat pudottaa kiekon: ")
                print("")
                if not self.valid_input(selectedColumn):
                    print("Antamasi syöte on virheellinen!\n")
                    continue
                selectedColumn = int(selectedColumn) - 1

            else:
                selectedColumn = ai.best_column(board)

            if self.column_is_available(board, selectedColumn):
                # Haetaan positions-muuttujan avulla sarakkeen seuraava vapaa rivi
                row = self.positions[selectedColumn]
                self.drop_disc(board, row, selectedColumn, player)
                self.positions[selectedColumn] += 1
                
                ai.store_last_move(row, selectedColumn)

                if self.player_won(board, row, selectedColumn, player):
                    print(f"\nPelaaja {player} voitti pelin!\n")
                    self.print_board(board)

                    self.game_over = True

                state = (state + 1) % 2
            else:
                print(f"\nSarake {selectedColumn} on täynnä! Valitse toinen sarake.\n")

connect_four = ConnectFour()