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
        self.last_row = None
        self.last_col = None

    def player(self):
        return self.ai_player

    def store_last_move(self, row, column):
        self.last_row = row
        self.last_col = column

    def best_column(self, board: GameBoard, depth=6):
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm - 1]
            column = randint(0, COL_COUNT-1)

        if self.level == 1:
            # Asetetaan käsiteltyjen solmujen lukumäärä nollaksi
            self.nodes_visited = 0

            start_time = time()

            row, col = self.last_row, self.last_col

            # Alfan ja betan alkuarvot
            alpha, beta = -inf, inf

            value, column = self.minimax(board, row, col, alpha, beta, depth, maximizing=False)

            end_time = time()
            runtime = end_time - start_time

            print(f"Minimax valitsi sarakkeen {column + 1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes_visited} kpl")
            print(f"Minimax-algoritmin suoritusaika: {runtime} sekuntia")


        return column, runtime

    def minimax(self, board:GameBoard, last_row, last_col, alpha, beta, depth:int, maximizing:bool):
        self.nodes_visited += 1

        # Edellisen siirron tehnyt pelaaja
        last_player = self.ai_player if maximizing else self.opponent

        end_state = board.end_state(last_row, last_col, last_player)

        if end_state:
            if end_state == self.ai_player: # Tekoälyn (min) voitto
                return -10_000_000, None
            if end_state == self.opponent: # Toisen pelaajan (max) voitto
                return 10_000_000, None
            return 0, None # Tasapeli

        if depth == 0:
            # Määritetään pelitilanteen arvo
            value = self.evaluate_board(board, last_player)
            return value, None


        if maximizing: # Maksimoiva pelaaja
            max_value = -999_999_999
            valid_columns = board.get_available_columns()
            best_column = None

            for column in valid_columns:
                row = board.get_next_available_row(column)
                board.update_position(row, column, value=self.opponent)
                value = self.minimax(board, row, column, alpha, beta, depth-1, maximizing=False)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value > max_value:
                    max_value = value
                    best_column = column

                alpha = max(alpha, max_value)

                if beta <= alpha:
                    break

            return max_value, best_column

        else: # Minimoiva pelaaja (tekoäly)
            min_value = 999_999_999
            valid_columns = board.get_available_columns()
            best_column = None

            for column in valid_columns:
                row = board.get_next_available_row(column)
                board.update_position(row, column, value=self.ai_player)
                value = self.minimax(board, row, column, alpha, beta, depth-1, maximizing=True)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value < min_value:
                    min_value = value
                    best_column = column

                beta = min(beta, min_value)

                if beta <= alpha:
                    break

            return min_value, best_column

    def evaluate_board(self, board: GameBoard, player: int):
        """Pisteyttää peliruudukon tilanteen vuorossa olevan pelaajan kannalta."""

        value = 0

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT):
            for column in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row, val) for val in range(column, column+4)]

                value += self.get_block_value(evaluation_block, player)

        # PYSTYSUUNTAISET NELJÄN RUUDUN LOHKOT

        for column in range(COL_COUNT):
            for row in range(ROW_COUNT - 3):
                evaluation_block = [board.get_position(val, column) for val in range(row, row + 4)]

                value += self.get_block_value(evaluation_block, player)

        # VINOTTAISET NELJÄN RUUDUN LOHKOT

        # Nouseva suunta (/)
        for row in range(ROW_COUNT - 3):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row+val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        # Laskeva suunta (\)
        for row in range(ROW_COUNT - 1, ROW_COUNT - 4, -1):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row-val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        # Jos pelaaja on tekoäly eli minimoiva pelaaja, palautetaan saadun arvon vastaluku
        if player == self.ai_player:
            return -value

        return value

    def get_block_value(self, evaluation_block: list, player: int):
        """Pisteyttää neljän ruudun kokoisen lohkon parametrina annetun pelaajan kannalta.
        Lohko sisältää neljä vierekkäistä ruutua vaaka-, pysty- tai vinosuunnassa."""

        opponent = (player % 2) + 1

        player_discs = 0
        opponent_discs = 0
        empty_count = 0

        for disc in evaluation_block:
            if disc == player:
                player_discs +=1
            elif disc == opponent:
                opponent_discs += 1
            else: # Ruutu on tyhjä
                empty_count += 1

        if player_discs == 3 and empty_count == 1:
            return 10
        if player_discs == 2 and empty_count == 2:
            return 4
        if opponent_discs == 3 and empty_count == 1:
            return -10

        return 0
