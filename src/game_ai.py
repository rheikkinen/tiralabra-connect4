from random import randint
from time import time
from constants import ROW_COUNT, COL_COUNT, ORDER

class AI:
    def __init__(self, game, level=1, player=2):
        self.level = level
        self.ai_player = player
        self.nodes = 0
        self.row= None
        self.col = None
        self.game = game

    def player(self):
        return self.ai_player

    def store_last_move(self, row, column):
        self.row = row
        self.col = column

    def get_available_columns(self, board):
        """Palauttaa vapaana olevat sarakkeet listana, joka
        on järjestetty keskimmäisistä reunimmaisiin sarakkeisiin."""
        valid_columns = []
        for column in range (COL_COUNT):
            if self.game.column_is_available(board, column):
                valid_columns.append(column)

        return sorted(valid_columns, key=lambda val: ORDER.index(val))

    def get_next_available_row(self, board, column):
        for row in range(0, 6):
            if board[row][column] == 0:
                return row

    def best_column(self, game_board):
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm - 1]
            column = randint(0, COL_COUNT-1)

        if self.level == 1:
            # Asetetaan läpi käytyjen solmujen lukumäärä nollaksi
            self.nodes = 0

            start_time = time()

            value, column = self.minimax(game_board, self.row, self.col, depth=4, maximizing=False)

            end_time = time()

            print(f"Minimax valitsi sarakkeen {column+1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes} kpl")
            print(f"Minimax-algoritmin suoritusaika: {end_time - start_time} sekuntia")

        return column

    def minimax(self, board, last_row, last_col, depth, maximizing: bool):
        self.nodes += 1
        last_player = 2 if maximizing else 1
        end_state = self.game.end_state(board, last_row, last_col, last_player)

        if end_state:
            if end_state == 1: # pelaaja 1 voitti
                return 10000000, None
            if end_state == 2: # pelaaja 2 voitti
                return -10000000, None
            return 0, None # tasapeli

        if depth == 0:
            value = self.evaluate_board(board, last_player)
            return value, None

        if maximizing: # vastustajan (MAX) vuoro
            max_value = -9999
            valid_columns = self.get_available_columns(board)
            best_column = valid_columns[0]

            for column in valid_columns:
                row = self.get_next_available_row(board, column)

                self.game.drop_disc(board, row=row, column=column, player=1)
                value = self.minimax(board, row, column, depth-1, maximizing=False)[0]

                # Kumotaan siirto
                board[row][column] = 0

                if value > max_value:
                    max_value = value
                    best_column = column

            return max_value, best_column

        else: # tekoälyn (MIN) vuoro
            min_value = 9999
            valid_columns = self.get_available_columns(board)
            best_column = valid_columns[0]

            for column in valid_columns:
                row = self.get_next_available_row(board, column)

                self.game.drop_disc(board, row=row, column=column, player=2)
                value = self.minimax(board, row, column, depth-1, maximizing=True)[0]

                # Kumotaan siirto
                board[row][column] = 0

                if value < min_value:
                    min_value = value
                    best_column = column

            return min_value, best_column

    def evaluate_board(self, board, player):
        """Pisteyttää peliruudukon tilanteen vuorossa olevan pelaajan kannalta"""

        value = 0
        opponent = (player % 2) + 1

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT): # väli on [0, 5], kun ROW_COUNT = 6
            for column in range(COL_COUNT - 3): # väli on [0, 3] kun COL_COUNT = 7
                evaluation_block = [board[row][val] for val in range(column, column+4)]
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
                evaluation_block = [board[val][column] for val in range(row, row + 4)]

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
