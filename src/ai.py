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
        self.nodes_visited = 0
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
            self.nodes_visited = 0

            start_time = time()

            value, column = self.minimax(game_board, self.row, self.col, depth=4, maximizing=False)

            end_time = time()

            print(f"Minimax valitsi sarakkeen {column + 1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes_visited} kpl")
            print(f"Minimax-algoritmin suoritusaika: {end_time - start_time} sekuntia")

        return column

    def minimax(self, board: GameBoard, last_row, last_col, depth, maximizing: bool):
        self.nodes_visited += 1

        last_player = self.ai_player if maximizing else self.opponent

        end_state = board.end_state(last_row, last_col, last_player)

        if end_state:
            if end_state == self.ai_player: # tekoälyn (min) voitto
                return -10_000_000, None
            if end_state == self.opponent: # toisen pelaajan (max) voitto
                return 10_000_000, None
            return 0, None # tasapeli

        if depth == 0:
            value = self.evaluate_board(board, last_player)
            return value, None

        if maximizing: # maksimoiva pelaaja
            max_value = -inf
            valid_columns = board.get_available_columns()
            best_column = None

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

        # minimoiva pelaaja (tekoäly)
        min_value = inf
        valid_columns = board.get_available_columns()
        best_column = None

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

    def evaluate_board(self, board: GameBoard, player: int):
        """Pisteyttää peliruudukon tilanteen vuorossa olevan pelaajan kannalta"""

        value = 0

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT): # väli on [0, 5], kun ROW_COUNT = 6
            for column in range(COL_COUNT - 3): # väli on [0, 3] kun COL_COUNT = 7
                evaluation_block = [board.get_position(row, val) for val in range(column, column+4)]

                value += self.get_block_value(evaluation_block, player)

        # PYSTYSUUNTAISET NELJÄN RUUDUN LOHKOT

        for column in range(COL_COUNT): # väli on [0, 6], kun COL_COUNT = 7
            for row in range(ROW_COUNT - 3): # väli on [0, 2] kun ROW_COUNT = 6
                evaluation_block = [board.get_position(val, column) for val in range(row, row + 4)]

                value += self.get_block_value(evaluation_block, player)

        # VINOSUUNTAISET NELJÄN RUUDUN LOHKOT

        # NOUSEVAT SUORAT (/)
        for row in range(ROW_COUNT - 3): # käy läpi rivit [0, 1, 2]
            for col in range(COL_COUNT - 3): # käy läpi sarakkeet [0, 1, 2, 3]
                evaluation_block = [board.get_position(row+val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        # LASKEVAT SUORAT (\)
        for row in range(ROW_COUNT - 1, ROW_COUNT - 4, -1): # käy läpi rivit [5, 4, 3]
            for col in range(COL_COUNT - 3): # käy läpi sarakkeet [0, 1, 2, 3]
                evaluation_block = [board.get_position(row-val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        if player == self.ai_player:
            return -value

        return value

    def get_block_value(self, evaluation_block: list, player: int):
        opponent = (player % 2) + 1

        player_discs = 0
        opponent_discs = 0
        empty_count = 0

        value = 0

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

        return value
