from math import inf
from random import randint
from time import time
from constants import ROW_COUNT, COL_COUNT
from gameboard import GameBoard

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.ai_player = player
        self.opponent = (player % 2) + 1
        self.nodes = 0
        self.row = None
        self.col = None

    def player(self):
        return self.ai_player

    def store_last_move(self, row, column):
        self.row = row
        self.col = column

    def best_column(self, game_board: GameBoard):
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm - 1]
            column = randint(0, COL_COUNT-1)

        if self.level == 1:
            # Asetetaan läpi käytyjen solmujen lukumäärä nollaksi
            self.nodes = 0

            start_time = time()

            value, column = self.minimax(game_board, self.row, self.col, depth=5, maximizing=False)

            end_time = time()

            print(f"Minimax valitsi sarakkeen {column+1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes} kpl")
            print(f"Minimax-algoritmin suoritusaika: {end_time - start_time} sekuntia")

        return column

    def minimax(self, board: GameBoard, last_row, last_col, depth, maximizing: bool):
        self.nodes += 1
        last_player = self.opponent if maximizing else self.ai_player
        end_state = board.end_state(last_row, last_col, last_player)

        if end_state:
            if end_state == self.ai_player: # tekoälyn (min) voitto
                return -10000000, None
            if end_state == self.opponent: # vastapelaajan (max) voitto
                return 10000000, None
            return 0, None # tasapeli

        if depth == 0:
            value = self.evaluate_board(board, last_player)
            return value, None

        if maximizing: # vastustajan (MAX) vuoro
            max_value = -inf
            valid_columns = board.get_available_columns()
            best_column = valid_columns[0]

            for column in valid_columns:
                row = board.get_next_available_row(column)

                board.update_position(row, column, value=self.opponent)

                value = self.minimax(board, row, column, depth-1, maximizing=False)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value > max_value:
                    max_value = value
                    best_column = column

            return max_value, best_column

        else: # tekoälyn (MIN) vuoro
            min_value = inf
            valid_columns = board.get_available_columns()
            best_column = valid_columns[0]

            for column in valid_columns:
                row = board.get_next_available_row(column)

                board.update_position(row, column, value=self.ai_player)

                value = self.minimax(board, row, column, depth-1, maximizing=True)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value < min_value:
                    min_value = value
                    best_column = column

            return min_value, best_column

    def evaluate_board(self, board: GameBoard, player):
        """Pisteyttää peliruudukon tilanteen vuorossa olevan pelaajan kannalta"""

        value = 0
        opponent = (player % 2) + 1

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT): # väli on [0, 5], kun ROW_COUNT = 6
            for column in range(COL_COUNT - 3): # väli on [0, 3] kun COL_COUNT = 7
                evaluation_block = [board.get_position(row, val) for val in range(column, column+4)]

                player_discs = 0
                opponent_discs = 0
                empty_count = 0

                for disc in evaluation_block:
                    if disc == player:
                        player_discs +=1
                    elif disc == opponent:
                        opponent_discs += 1
                    else: # ruutu on tyhjä
                        empty_count += 1

                if player_discs == 3 and empty_count == 1:
                    value += 10
                elif player_discs == 2 and empty_count == 2:
                    value += 4
                elif opponent_discs == 3 and empty_count == 1:
                    value -= 10

        # PYSTYSUUNTAISET NELJÄN RUUDUN LOHKOT

        for column in range(COL_COUNT): # väli on [0, 6], kun COL_COUNT = 7
            for row in range(ROW_COUNT - 3): # väli on [0, 2] kun ROW_COUNT = 6
                evaluation_block = [board.get_position(val, column) for val in range(row, row + 4)]

                player_discs = 0
                opponent_discs = 0
                empty_count = 0

                for disc in evaluation_block:
                    if disc == player:
                        player_discs +=1
                    elif disc == opponent:
                        opponent_discs += 1
                    else: # ruutu on tyhjä
                        empty_count += 1

                if player_discs == 3 and empty_count == 1:
                    value += 10
                elif player_discs == 2 and empty_count == 2:
                    value += 4
                elif opponent_discs == 3 and empty_count == 1:
                    value -= 10
        """
        # VINOSUUNTAISET NELJÄN RUUDUN LOHKOT
        print("VINOSUUNTAISET LOHKOT")
        self.game.print_board(board)
        for row in range(ROW_COUNT - 3): # rivit väliltä [0, 2]
            for column in range(COL_COUNT - 4): #sarakkeet väliltä [0, 2]
                evaluation_block = [board[row + val][column + val] for val in range(4)]
                print(evaluation_block)
        """
        if player == self.ai_player:
            return -value

        return value
